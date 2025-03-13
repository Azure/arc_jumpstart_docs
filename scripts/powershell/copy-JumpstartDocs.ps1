param(
    [Parameter(Mandatory=$true)]
    [string]$SourcePath,

    [Parameter(Mandatory=$true)]
    [string]$StorageAccountName,

    [Parameter(Mandatory=$true)]
    [string]$ContainerName
)

function Test-HasContentBeyondFrontMatter {
    param([string]$content)
    if ($content -match "(?ms)^---\s*\r?\n(.*?)\r?\n---\s*\r?\n(.+)") {
        return $matches[2].Trim().Length -gt 0
    }
    return $false
}

function Update-FrontMatter {
    param(
        [string]$content,
        [string]$sourcePath
    )
    if ($content -match "(?ms)^(---\s*\r?\n)(.*?)(\r?\n---\s*\r?\n)(.+)$") {
        $frontMatter = $matches[2]
        $separator = $matches[3]
        $mainContent = $matches[4]

        # Add source_path to front matter
        if ($frontMatter -match "source_path:") {
            $frontMatter = $frontMatter -replace "source_path:.*", "source_path: $sourcePath"
        } else {
            $frontMatter = $frontMatter.TrimEnd() + "`nsource_path: $sourcePath"
        }

        return "---`n" + $frontMatter + $separator + $mainContent
    }
    return $content
}

function Get-CleanPath {
    param([string]$path)
    return $path.TrimStart('/').TrimStart('\').Replace('\', '/')
}

# Ensure user is logged in to Azure
try {
    $context = Get-AzContext
    if (-not $context) {
        Write-Error "Not logged in to Azure. Please run Connect-AzAccount first."
        throw
    }
}
catch {
    Write-Error "Error checking Azure login status: $_"
    throw
}

# Create a temporary directory for filtered content
# $tempDir = Join-Path $env:TEMP "JumpstartDocs_$(Get-Random)"
$tempDir = "JumpstartDocs_$(Get-Random)"
New-Item -ItemType Directory -Path $tempDir -Force | Out-Null

try {
    # Get all _index.md files first
    Write-Host "Finding all _index.md files..."
    $allFiles = Get-ChildItem -Path $SourcePath -Recurse -Filter "_index.md"
    $totalFiles = $allFiles.Count
    $processed = 0

    # Create scriptblocks for the functions
    $testFunctionBlock = ${function:Test-HasContentBeyondFrontMatter}.ToString()
    $updateFunctionBlock = ${function:Update-FrontMatter}.ToString()
    $cleanPathBlock = ${function:Get-CleanPath}.ToString()

    # Process files in parallel
    $allFiles | ForEach-Object -ThrottleLimit 16 -Parallel {
        # Import functions into parallel scope
        ${function:Test-HasContentBeyondFrontMatter} = $using:testFunctionBlock
        ${function:Update-FrontMatter} = $using:updateFunctionBlock
        ${function:Get-CleanPath} = $using:cleanPathBlock

        $content = Get-Content -Path $_.FullName -Raw -Encoding UTF8
        if (Test-HasContentBeyondFrontMatter -content $content) {
            # Get the path relative to the source directory
            $relativePath = $_.FullName.Replace($using:SourcePath, '').TrimStart('/').TrimStart('\')
            $targetPath = Join-Path $using:tempDir $relativePath
            $targetDir = Split-Path $targetPath -Parent

            if (-not (Test-Path $targetDir)) {
                New-Item -ItemType Directory -Path $targetDir -Force | Out-Null
            }

            # Extract path starting from docs for the source_path in front matter
            $sourcePath = if ($_.FullName -match "(?i)docs[/\\](.*)") {
                "docs/" + (Get-CleanPath $matches[1])
            } else {
                Get-CleanPath $_.FullName
            }

            # Update content with modified source path and write to destination
            $updatedContent = Update-FrontMatter -content $content -sourcePath $sourcePath
            Set-Content -Path $targetPath -Value $updatedContent -Encoding UTF8 -Force
        }

        $Global:processed = $using:processed + 1
        Write-Progress -Activity "Filtering files" -Status "$Global:processed of $using:totalFiles" -PercentComplete (($Global:processed / $using:totalFiles) * 100)
    }

    # Set AzCopy optimizations
    $env:AZCOPY_AUTO_LOGIN_TYPE="AZCLI"
    $env:AZCOPY_CONCURRENCY_VALUE = "AUTO"
    $env:AZCOPY_BUFFER_GB = "4"

    # Use AzCopy sync
    Write-Host "Syncing content to Azure Storage..."
    $destUrl = "https://$StorageAccountName.blob.core.windows.net/$ContainerName"
    $cleanTempDir = (Get-Item $tempDir).FullName + "/*"

    $azcopyOutput = azcopy sync $cleanTempDir $destUrl --delete-destination=true `
                                                --log-level=ERROR `
                                                --recursive=true `
                                                --cap-mbps=0 `
                                                --block-size-mb=8

    if ($LASTEXITCODE -eq 0) {
        Write-Host "Synchronization completed successfully."
    }
    else {
        $errorDetail = switch ($LASTEXITCODE) {
            1 { "Fatal error encountered" }
            2 { "One or more files/folders skipped" }
            3 { "One or more files/folders modified during transfer" }
            4 { "No files/folders matched" }
            default { "Unknown error" }
        }
        Write-Error "AzCopy failed with exit code $LASTEXITCODE : $errorDetail"
        Write-Error "AzCopy output: $azcopyOutput"
        throw "AzCopy synchronization failed"
    }
}
catch {
    Write-Error "Error during synchronization: $_"
    throw
}
finally {
    # Cleanup temporary directory
    if (Test-Path $tempDir) {
        Remove-Item -Path $tempDir -Recurse -Force
    }
    # Clear AzCopy environment variables
    $env:AZCOPY_CRED_TYPE = $null
    $env:AZCOPY_CONCURRENCY_VALUE = $null
    $env:AZCOPY_BUFFER_GB = $null
}