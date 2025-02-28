import os
import re
import requests
import subprocess
from urllib.parse import urljoin, urlparse
from datetime import datetime
import ipaddress
from colorama import init
import sys

# Initialize colorama for Windows compatibility and force color output in GitHub Actions
init(strip=False, convert=False)

# ANSI escape codes
class Colors:
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

# Configuration

def get_repo_root():
    """Find the root directory of the Git repository."""
    try:
        return subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
    except subprocess.CalledProcessError:
        return '.'  # Default to current directory if not in a Git repo

REPO_PATH = get_repo_root()
LOG_DIR = os.path.join(REPO_PATH, 'scripts/python/url-checker/logs')
os.makedirs(LOG_DIR, exist_ok=True)
TIMEOUT = 5  # Seconds
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; LinkChecker/1.0)"}  # Mimic a real browser

# Regex to find markdown URLs
MD_URL_REGEX = re.compile(r'\[.*?\]\((.*?)\)')
EMAIL_REGEX = re.compile(r'^mailto:')
ANSI_ESCAPE_REGEX = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')

# List of known valid URLs to skip checking
KNOWN_VALID_URLS = [
    "https://whatismyip.com",
    "https://www.linkedin.com",
    # Add more known valid URLs here
]

def find_markdown_files():
    """Find all markdown files in the repository, skipping 'archive' folders."""
    md_files = []
    for root, dirs, files in os.walk(REPO_PATH):
        # Skip 'archive' folders
        dirs[:] = [d for d in dirs if d.lower() != 'archive']
        for file in files:
            if file.endswith(".md"):
                md_files.append(os.path.join(root, file))
    return md_files

def extract_urls(md_file):
    """Extract all URLs from a markdown file."""
    urls = []
    with open(md_file, 'r', encoding='utf-8') as f:
        for line in f:
            matches = MD_URL_REGEX.findall(line)
            urls.extend(matches)
    return urls

def is_ip_based_url(url):
    """Check if a URL is IP-based."""
    try:
        host = urlparse(url).hostname
        ipaddress.ip_address(host)
        return True
    except ValueError:
        return False

def check_absolute_url(url, retries=3):
    """Check if an absolute URL is reachable, always using GET requests."""
    if url in KNOWN_VALID_URLS:
        log_entry = f"{Colors.OKGREEN}[OK] {url} (known valid URL){Colors.ENDC}"
        print(log_entry)
        return log_entry

    print(f"Checking absolute URL: {url}")
    attempt = 0
    while attempt < retries:
        try:
            response = requests.get(url, headers=HEADERS, allow_redirects=True, timeout=TIMEOUT, stream=True)
            
            if response.status_code < 400:
                log_entry = f"{Colors.OKGREEN}[OK] {url}{Colors.ENDC}"
                print(log_entry)
                return log_entry
            else:
                log_entry = f"{Colors.FAIL}[BROKEN ABSOLUTE] {url} - Status Code: {response.status_code}{Colors.ENDC}"
                print(log_entry)
                return log_entry
        except requests.RequestException as e:
            log_entry = f"{Colors.FAIL}[BROKEN ABSOLUTE] {url} - Error: {e}{Colors.ENDC}"
            print(log_entry)
            attempt += 1
            if attempt < retries:
                print(f"Retrying... ({attempt}/{retries})")
            else:
                return log_entry

def check_relative_url(url, md_file):
    """Check if a relative file exists."""
    file_path = os.path.join(os.path.dirname(md_file), url)
    print(f"Checking relative URL: {file_path}")
    if os.path.exists(file_path):
        log_entry = f"{Colors.OKGREEN}[OK] {file_path}{Colors.ENDC}"
        print(log_entry)
        return log_entry
    else:
        log_entry = f"{Colors.FAIL}[BROKEN RELATIVE] {file_path} (relative path in {md_file}){Colors.ENDC}"
        print(log_entry)
        return log_entry

def strip_ansi_escape_codes(text):
    """Remove ANSI escape codes from the text."""
    return ANSI_ESCAPE_REGEX.sub('', text)

def main():
    broken_absolute_urls = []
    ok_absolute_urls = []
    broken_relative_urls = []
    ok_relative_urls = []
    markdown_files = find_markdown_files()
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    log_file_with_timestamp = os.path.join(LOG_DIR, f'broken_urls_{timestamp}.log')
    
    print("Starting URL check...")
    start_time = datetime.now()
    with open(log_file_with_timestamp, 'a', encoding='utf-8') as log:
        log.write(f"Log generated on: {timestamp}\n")
        log.flush()
        for md_file in markdown_files:
            print(f"Processing file: {md_file}")
            urls = extract_urls(md_file)
            for url in urls:
                if EMAIL_REGEX.match(url):
                    print(f"Skipping email URL: {url}")
                    continue
                
                if url.startswith("http://localhost") or is_ip_based_url(url):
                    print(f"Skipping localhost or IP-based URL: {url}")
                    continue
                
                parsed_url = urlparse(url)
                if parsed_url.scheme in ('http', 'https'):
                    log_entry = check_absolute_url(url)
                    if "[OK]" in log_entry:
                        ok_absolute_urls.append(log_entry)
                    else:
                        broken_absolute_urls.append(log_entry)
                else:
                    log_entry = check_relative_url(url, md_file)
                    if "[OK]" in log_entry:
                        ok_relative_urls.append(log_entry)
                    else:
                        broken_relative_urls.append(log_entry)
                log.write(strip_ansi_escape_codes(log_entry) + "\n")
                log.flush()
    
    end_time = datetime.now()
    runtime_duration = end_time - start_time
    
    with open(log_file_with_timestamp, 'a', encoding='utf-8') as log:
        log.write(f"\nRuntime duration: {runtime_duration}\n")
        log.write(f"Total broken absolute URLs: {len(broken_absolute_urls)}\n")
        log.write(f"Total OK absolute URLs: {len(ok_absolute_urls)}\n")
        log.write(f"Total broken relative URLs: {len(broken_relative_urls)}\n")
        log.write(f"Total OK relative URLs: {len(ok_relative_urls)}\n")
        log.write("\n=== Broken Absolute URLs ===\n")
        log.write("\n".join(strip_ansi_escape_codes(url) for url in broken_absolute_urls) + "\n\n")
        
        log.write("\n=== OK Absolute URLs ===\n")
        log.write("\n".join(strip_ansi_escape_codes(url) for url in ok_absolute_urls) + "\n\n")
        
        log.write("\n=== Broken Relative URLs ===\n")
        log.write("\n".join(strip_ansi_escape_codes(url) for url in broken_relative_urls) + "\n\n")
        
        log.write("\n=== OK Relative URLs ===\n")
        log.write("\n".join(strip_ansi_escape_codes(url) for url in ok_relative_urls) + "\n\n")
    
    print(f"Check complete. See {log_file_with_timestamp} for details.")
    print(f"\nLog generated on: {timestamp}")
    print(f"Runtime duration: {runtime_duration}")
    print(f"Total broken absolute URLs: {len(broken_absolute_urls)}")
    print(f"Total OK absolute URLs: {len(ok_absolute_urls)}")
    print(f"Total broken relative URLs: {len(broken_relative_urls)}")
    print(f"Total OK relative URLs: {len(ok_relative_urls)}")
    print("\n=== Broken Absolute URLs ===")
    for url in broken_absolute_urls:
        print(f"{Colors.FAIL}{strip_ansi_escape_codes(url)}{Colors.ENDC}")
    print("\n=== Broken Relative URLs ===")
    for url in broken_relative_urls:
        print(f"{Colors.FAIL}{strip_ansi_escape_codes(url)}{Colors.ENDC}")
    print("\n=== OK Absolute URLs ===")
    for url in ok_absolute_urls:
        print(f"{Colors.OKGREEN}{strip_ansi_escape_codes(url)}{Colors.ENDC}")
    print("\n=== OK Relative URLs ===")
    for url in ok_relative_urls:
        print(f"{Colors.OKGREEN}{strip_ansi_escape_codes(url)}{Colors.ENDC}")

    # Print summary table
    print("\nSummary:")
    print(f"{Colors.FAIL}Total broken absolute URLs: {len(broken_absolute_urls)}{Colors.ENDC}")
    print(f"{Colors.OKGREEN}Total OK absolute URLs: {len(ok_absolute_urls)}{Colors.ENDC}")
    print(f"{Colors.FAIL}Total broken relative URLs: {len(broken_relative_urls)}{Colors.ENDC}")
    print(f"{Colors.OKGREEN}Total OK relative URLs: {len(ok_relative_urls)}{Colors.ENDC}")

    if broken_absolute_urls or broken_relative_urls:
        sys.exit(1)  # Exit with non-zero status to indicate failure
    else:
        sys.exit(0)  # Exit with zero status to indicate success

if __name__ == "__main__":
    main()
