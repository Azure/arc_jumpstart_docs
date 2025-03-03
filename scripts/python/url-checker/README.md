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
- Advanced header link validation:
  - Extracts actual headers from markdown files
  - Validates in-page links (`#header-name`)
  - Cross-file header links (`file.md#header-name`)
- Smart directory link handling:
  - Detects links ending with `/`
  - Looks for default files (`_index.md`, `index.md`, `README.md`)
  - Fallback to any markdown file in the directory
- Detailed output with categorization by link type
- Colorized console output (including in GitHub Actions)
- Comprehensive log files with summary tables
- Exit code support for CI/CD workflows
- File location information for all discovered links (absolute and relative)

## 🧰 Requirements

- Python 3.x
- `requests` library
- `colorama` library

Install dependencies with:

```bash
pip install requests colorama
```

## 🛠️ Manual Usage

Run from the repository root:

```bash
python scripts/python/url-checker/url-checker.py
```

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

```text
Link Validation Summary (6122 links checked):
- Broken links: 42
  - Absolute URLs: 8
  - Relative URLs without anchors: 0
  - Relative URLs with anchors: 34
  - Root-relative URLs: 0
  - Image URLs: 0
  - SVG URLs: 0
  - Header links: 0
- No links found: 2 categories
  - Root-relative URLs
  - SVG URLs
- OK links: 6080
❌ Broken links were found. Check the logs for details.
```

### Sample Log File Structure

The log file is organized in sections, making it easy to review different types of issues:

```text
URL Checker Results

Log generated on: 2023-07-21_15-22-45
Runtime duration: 0:05:24.123456

=== Broken Absolute URLs ===

[BROKEN ABSOLUTE] https://example.com/missing-page - Status Code: 404 (in file: /docs/example/file.md)
[BROKEN ABSOLUTE] https://site.com/broken-link - Error: ConnectionError (in file: /docs/another/example.md)

=== Broken Relative URLs Without Anchors ===

✅ No broken relative URLs without anchors found.

=== Broken Relative URLs With Anchors ===

[BROKEN RELATIVE WITH ANCHOR] ../reference/file.md#section (relative path in /docs/guide/tutorial.md)

=== Broken Root-Relative URLs ===

✅ No broken root-relative URLs found.

// ... sections for other link types ...

Link Validation Summary (6122 links checked):
- Broken links: 42
  - Absolute URLs: 8
  - Relative URLs without anchors: 0
  - Relative URLs with anchors: 34
  - Root-relative URLs: 0
  - Image URLs: 0
  - SVG URLs: 0
  - Header links: 0
- No links found: 2 categories
  - Root-relative URLs
  - SVG URLs
- OK links: 6080
❌ Broken links were found. Check the logs for details.
```

## ⚙️ Configuration

The following can be customized in the script:

- `KNOWN_VALID_URLS`: URLs to skip checking (e.g., frequently timing out sites)
- `IMAGE_EXTENSIONS`: File extensions to treat as images
- `SVG_EXTENSIONS`: SVG file extensions
- `TIMEOUT`: Request timeout settings (default: 15 seconds)

### Using KNOWN_VALID_URLS

Add URLs that should be considered valid without checking:

```python
KNOWN_VALID_URLS = [
    "https://learn.microsoft.com",  # Will skip all Microsoft Learn URLs
    "https://icanhazip.com"
]
```

## 🔍 Troubleshooting

### Root-Relative URLs

URLs that start with `/` (like `/img/logo.png`) are now properly handled as relative to the repository root rather than the current document's directory.

### False Positives

Some URLs may be incorrectly marked as broken due to:

- Timeout issues (especially with Microsoft documentation pages)
- Server-side rate limiting
- Temporary server issues

Add these to the `KNOWN_VALID_URLS` list to skip checking them.

## 👋 Contributing

We'd love your help to make this tool even better! Whether you're fixing bugs, adding features, or improving documentation, your contributions are warmly welcomed.
