# Jumpstart Markdown URL Checker

This tool checks for broken URLs in all Markdown files within the repository. It can be run both manually or as part of an automated GitHub Actions workflow.

## Features

- Checks both absolute and relative URLs
- Skips email URLs, localhost/IP-based URLs
- Logs results to a timestamped log file
- Provides a summary of broken and valid URLs
- Integrated with GitHub Actions workflow
- Option to fail CI checks when broken links are found
- Supports short URLs

## Requirements

- Python 3.x
- `requests` library
- `colorama` library

You can install the required libraries using pip:

```sh
pip install requests colorama
```

## Manual Usage

To run the URL checker manually:

1. Navigate to the repository root:

```sh
cd arc_jumpstart_docs
```

2. Run the script:

```sh
python scripts/python/url-checker/url-checker.py
```

The script will scan all files in the repository, check URLs, and log the results.

## Automated GitHub Actions Workflow

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

## Output

The script generates a log file with a timestamp in the format `broken_urls_YYYY-MM-DD_HH-MM-SS.log`. The log file contains:

- Total broken absolute URLs
- Total OK absolute URLs
- Total broken relative URLs
- Total OK relative URLs
- Detailed lists of broken and valid URLs

## Example Output

```console
Starting URL check...
Processing markdown file: /path/to/file.md
Checking absolute URL: https://example.com
[OK] https://example.com
...
Check complete. See broken_urls_2023-10-01_12-00-00.log for details.

Summary:
Total broken absolute URLs: 2
Total OK absolute URLs: 10
Total broken relative URLs: 1
Total OK relative URLs: 5
```

## Notes

- The script skips URLs that start with `mailto:` and `http://localhost`
- The script also skips IP-based URLs (e.g., http://192.168.1.1)
- You can add known valid URLs to the `KNOWN_VALID_URLS` list in the script
- When run in GitHub Actions, the logs are uploaded as workflow artifacts
- The script exit code is 0 if no broken links are found, 1 if broken links are found

## Troubleshooting

### Timeouts

By default, the script has a 15-second timeout when checking URLs. If a URL takes longer to respond, it will be marked as broken with a "Read timeout" error. Common causes include:

- Slow-responding servers
- Network latency
- Complex pages that take time to load

You can modify this by changing the `timeout` parameter in the requests.get() calls in the script.

### False Positives

Some URLs may be incorrectly marked as broken due to:

- Timeout issues (especially with Microsoft documentation pages)
- Server-side rate limiting
- Temporary server issues

### Using KNOWN_VALID_URLS

The `KNOWN_VALID_URLS` list lets you specify URLs that should be considered valid without checking them. This is useful for:

- URLs that often timeout but you know are valid
- URLs behind authentication that the script can't access
- Reducing the total check time

To add a URL domain to the skip list, edit the script and add it to the `KNOWN_VALID_URLS` list:

```python
KNOWN_VALID_URLS = [
    "https://learn.microsoft.com",  # Will skip all Microsoft Learn URLs
    "https://example.com/specific-path"  # Will only skip this specific path
]
```

Adding a base URL like `https://learn.microsoft.com` will cause the script to skip checking any URL that starts with this string.
