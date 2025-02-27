# Jumpstart Markdown URL Checker

This Python script (`url_checker.py`) checks for broken URLs in all Markdown within a Git repository. The script scans all files, extracts URLs, and verifies if they are reachable.

## Features

- Checks both absolute and relative URLs.
- Skips email URLs and localhost/IP-based URLs.
- Logs results to a timestamped log file.
- Provides a summary of broken and valid URLs.
- Supports short URLs.

## Requirements

- Python 3.x
- `requests` library
- `colorama` library

You can install the required libraries using pip:

```sh
pip install requests colorama
```

## Usage

1. Clone the repository and navigate to the directory:

```sh
git clone <repository-url>
cd arc_jumpstart_docs
```

2. Run the script:

```sh
python scripts/python/url_checker/url_checker.py
```

The script will start scanning all files in the repository, checking URLs, and logging the results.

## Output

The script generates a log file with a timestamp in the format `broken_urls_YYYY-MM-DD_HH-MM-SS.log`. The log file contains:

- Total broken absolute URLs
- Total OK absolute URLs
- Total broken relative URLs
- Total OK relative URLs
- Detailed lists of broken and valid URLs

## Example

```sh
python scripts/python/url_checker/url_checker.py
```

Output:

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

- The script skips URLs that start with `mailto:` and `http://localhost`.
- You can add known valid URLs to the `KNOWN_VALID_URLS` list in the script to skip checking them.
- The script supports short URLs.
