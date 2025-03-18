# Jumpstart Markdown URL Checker

This tool checks for broken URLs in all Markdown files within the repository. It can be run manually or as part of an automated GitHub Actions workflow.

## ✨ Features

- Validates both absolute URLs (http/https) and relative file paths
- Improved link type detection and classification:
  - Regular relative links (with and without anchors)
  - Root-relative links (starting with `/`)
  - Image links
  - SVG image links
  - Markdown header links (`#header-name`)
  - API reference links
- Advanced header link validation:
  - Extracts actual headers from markdown files
  - Validates in-page links (`#header-name`)
  - Cross-file header links (`file.md#header-name`)
  - Support for complex header formats with special characters
- Smart directory link handling:
  - Detects links ending with `/`
  - Looks for default files (`_index.md`, `index.md`, `README.md`)
  - Fallback to any markdown file in the directory
  - Improved directory traversal detection
- Detailed output with categorization by link type
- Colorized console output (including in GitHub Actions)
- Comprehensive log files with summary tables
- Exit code support for CI/CD workflows
- File location information for all discovered links (absolute and relative)
- Parallel processing for faster checking of multiple URLs
- Cache mechanism to avoid rechecking identical URLs

## 🧰 Requirements

- Python 3.8 or higher
- Required Python packages:
  - `requests` - For HTTP requests
  - `colorama` - For colored terminal output
  - `tqdm` - For progress bars (optional)

Install dependencies with:

```bash
pip install requests colorama tqdm
```

Or using the requirements file:

```bash
pip install -r requirements.txt
```

## 🐍 Python 3 Installation

If you don't have Python 3 installed, here's how to install it on different operating systems:

### Windows

1. Download the latest Python installer from the [official Python website](https://www.python.org/downloads/windows/)
2. Run the installer
3. Make sure to check "Add Python to PATH" during installation
4. Verify the installation by opening Command Prompt and typing:
   ```
   python --version
   ```

### macOS

Using Homebrew (recommended):
```bash
brew install python
```

Or download the installer from the [official Python website](https://www.python.org/downloads/macos/)

Verify the installation:
```bash
python3 --version
```

### Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install python3 python3-pip
```

Verify the installation:
```bash
python3 --version
```

### Linux (RHEL/CentOS/Fedora)

```bash
sudo dnf install python3 python3-pip
```

Verify the installation:
```bash
python3 --version
```

## 🛠️ Manual Usage

Run from the repository root:

```bash
python3 scripts/python/url-checker/url-checker.py
```

## 🚂 Performance Optimization

The URL checker now includes several performance enhancements:

- **Parallel processing**: External URLs are checked in parallel threads
- **Caching mechanism**: Identical URLs are only checked once
- **Selective checking**: Option to skip external URLs for faster local validation
- **Progress indicators**: Visual feedback during the checking process
- **Smart retries**: Automatic retry for potentially transient failures

These optimizations significantly improve checking speed, especially for repositories with many external links.

## 🚀 Automated GitHub Actions Workflow

This tool is integrated with GitHub Actions as the `Check Broken Links` workflow, which:

- Runs automatically every day at midnight (cron job)
- Runs on push to `main` or `canary` branches
- Can be manually triggered from the GitHub Actions tab

### Manual Workflow Trigger

1. Go to the repository on GitHub
2. Click on the "Actions" tab
3. Select "Check Broken Links" workflow from the left sidebar
4. Click "Run workflow" button
5. Choose whether to fail the workflow if broken links are found
6. Click "Run workflow"

### The "fail-on-broken-links" Option

When manually triggering the workflow, you have the option to set `fail-on-broken-links`:

- **true** (default): The workflow will fail if any broken links are found. This is useful when you want to confirm there are no broken links before merging changes.
- **false**: The workflow will complete successfully even if broken links are found. This mode is useful for auditing without blocking processes.

The option has no effect when the workflow runs automatically via schedule or push triggers.

### Workflow Behavior

The workflow behavior depends on how it was triggered and the configuration:

| Trigger Method | fail-on-broken-links | Broken Links Found | Result |
|----------------|----------------------|-------------------|--------|
| push/schedule | N/A | Yes | ✅ Workflow succeeds |
| push/schedule | N/A | No | ✅ Workflow succeeds |
| Manual | false | Yes | ✅ Workflow succeeds |
| Manual | false | No | ✅ Workflow succeeds |
| Manual | true | No | ✅ Workflow succeeds |
| Manual | true | Yes | ❌ Workflow fails |

### Workflow Results

After the workflow completes:

1. The summary will show how many broken links were found (if any)
2. Detailed logs are available as workflow artifacts
3. If configured, the workflow will fail when broken links are found

## 📊 Output

The script generates a log file with timestamp and provides detailed output including:

### Summary Table

Based on a recent log, a typical summary might look like:

```text
Link Validation Summary (5396 links checked):
- Broken links: 3
  - Absolute URLs: 3
- No links found: 2 categories
  - Root-relative URLs
  - SVG URLs
- Categories with no broken links: 3
  - Relative URLs: 479 OK links
  - Image URLs: 3073 OK links
  - Header links: 85 OK links
- OK links: 5393
❌ Broken links were found. Check the logs for details.
```

### Sample Log File Structure

The log file is organized in sections, making it easy to review different types of issues:

```text
URL Checker Results

Log generated on: 2025-03-17_17-51-09
Runtime duration: 0:10:02.686031

=== Broken Absolute URLs (3 links found) ===

[BROKEN ABSOLUTE] https://learn.microsoft.com/cli/azure/ml/endpoint?view=azure-cli-latest#az_ml_endpoint_create - Status Code: 404 (in file: /path/to/file.md)
[BROKEN ABSOLUTE] https://learn.microsoft.com/cli/azure/ml/endpoint?view=azure-cli-latest#az_ml_endpoint_invoke - Status Code: 404 (in file: /path/to/file.md)
[BROKEN ABSOLUTE] https://www.weave.works/oss/scope/ - Error: HTTPSConnectionPool(host='www.weave.works', port=443): Max retries exceeded (in file: /path/to/file.md)

=== Broken Relative URLs Without Anchors (0 links found) ===

No broken relative URLs without anchors found.

=== Broken Relative URLs With Anchors (0 links found) ===

No broken relative URLs with anchors found.

// ... sections for other link types ...

=== OK Absolute URLs (1756 links found) ===

[OK ABSOLUTE] https://github.com/Microsoft
[OK ABSOLUTE] https://github.com/Azure
// ... additional OK links ...

=== OK Relative URLs (479 links found) ===

[OK RELATIVE] /path/to/file.md
[OK RELATIVE] ../relative/path/file.md
// ... additional OK relative links ...

Link Validation Summary (5396 links checked):
- Broken links: 3
  - Absolute URLs: 3
- No links found: 2 categories
  - Root-relative URLs
  - SVG URLs
- Categories with no broken links: 3
  - Relative URLs: 479 OK links
  - Image URLs: 3073 OK links
  - Header links: 85 OK links
- OK links: 5393
❌ Broken links were found. Check the logs for details.
```

## ⚙️ Configuration

The following can be customized in the script:

- `KNOWN_VALID_URLS`: URLs to skip checking (e.g., frequently timing out sites)
- `IMAGE_EXTENSIONS`: File extensions to treat as images
- `SVG_EXTENSIONS`: SVG file extensions
- `TIMEOUT`: Request timeout settings (default: 15 seconds)
- `MAX_THREADS`: Maximum number of parallel threads (default: 10)
- `RETRY_COUNT`: Number of retry attempts for failed requests (default: 2)
- `CACHE_TTL`: Time-to-live for URL validation cache in seconds (default: 3600)
- `USER_AGENT`: Custom user agent string for HTTP requests

### Using KNOWN_VALID_URLS

Add URLs that should be considered valid without checking:

```python
KNOWN_VALID_URLS = [
    "https://learn.microsoft.com",  # Will skip all Microsoft Learn URLs
    "https://icanhazip.com"
]
```

### Environment Variables

The tool also supports configuration via environment variables:

- `URL_CHECKER_TIMEOUT`: Override default timeout
- `URL_CHECKER_MAX_THREADS`: Override default thread count
- `URL_CHECKER_SKIP_EXTERNAL`: Set to "1" to skip external URL validation
- `URL_CHECKER_USER_AGENT`: Custom user agent string

## 🔍 Troubleshooting

### Root-Relative URLs

URLs that start with `/` (like `/img/logo.png`) are now properly handled as relative to the repository root rather than the current document's directory.

### False Positives

Some URLs may be incorrectly marked as broken due to:

- Timeout issues (especially with Microsoft documentation pages)
- Server-side rate limiting
- Temporary server issues

Add these to the `KNOWN_VALID_URLS` list to skip checking them. From the logs, we can see that Microsoft Learn API references and some external services occasionally have connectivity issues.

## 👋 Contributing

We'd love your help to make this tool even better! Whether you're fixing bugs, adding features, or improving documentation, your contributions are warmly welcomed.

### Development Setup

1. Clone the repository
2. Install development dependencies: `pip install -r requirements-dev.txt`
3. Run tests: `pytest tests/`

## 📋 Changelog

### v1.2.0 (2023-09-15)
- Added parallel processing for external URLs
- Implemented URL validation cache
- Added progress bars for better visibility
- Support for custom user agents
- Added retry mechanism for failed requests

### v1.1.0 (2023-08-01)
- Improved header link validation
- Added support for API reference links
- Enhanced directory traversal detection
- Added JSON and CSV output formats

### v1.0.0 (2023-07-01)
- Initial release
