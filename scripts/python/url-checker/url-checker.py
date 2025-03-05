# =============================================================================
# URL Checker for Markdown Files
# =============================================================================
# This script scans all Markdown files in a repository for URLs and checks
# whether they are valid. It handles both absolute URLs (http/https) and
# relative file paths, providing a detailed report of broken links.
# =============================================================================

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

# =============================================================================
# CONFIGURATION
# =============================================================================

# ANSI color codes for terminal output
class Colors:
    OKGREEN = '\033[92m'  # Green for success
    FAIL = '\033[91m'     # Red for errors
    INFO = '\033[96m'     # Cyan for neutral/informational
    NEUTRAL = '\033[93m'  # Yellow for "no links found" category
    ENDC = '\033[0m'

def get_repo_root():
    """Find the root directory of the Git repository."""
    try:
        return subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
    except subprocess.CalledProcessError:
        return '.'  # Default to current directory if not in a Git repo

# Script configuration settings
REPO_PATH = get_repo_root()
LOG_DIR = os.path.join(REPO_PATH, 'scripts/python/url-checker/logs')
os.makedirs(LOG_DIR, exist_ok=True)
TIMEOUT = 15  # Request timeout in seconds - increase this if you get many timeout errors
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; LinkChecker/1.0)"}  # Browser-like user agent

# Regular expressions for URL detection and processing
MD_URL_REGEX = re.compile(r'\[.*?\]\((.*?)\)')  # Finds markdown links: [text](url)
EMAIL_REGEX = re.compile(r'^mailto:')  # Detects email links
ANSI_ESCAPE_REGEX = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')  # For stripping color codes
HEADER_LINK_REGEX = re.compile(r'#[-\w]+$')  # Matches markdown header links like #header-name

# URLs to skip checking - add frequently timing out domains here
KNOWN_VALID_URLS = [
    "https://whatismyip.com",
    "https://www.linkedin.com",
    "https://learn.microsoft.com",
    "https://icanhazip.com",
    "https://shell.azure.com",
    # Add more URLs to skip here as needed
]

# Image file extensions to identify image links
IMAGE_EXTENSIONS = ['.png', '.jpg', '.jpeg', '.gif', '.webp', '.bmp', '.ico']
# SVG files get special treatment
SVG_EXTENSIONS = ['.svg']

# =============================================================================
# FILE & URL PROCESSING FUNCTIONS
# =============================================================================

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
    """Extract all URLs from a markdown file using regex."""
    urls = []
    with open(md_file, 'r', encoding='utf-8') as f:
        for line in f:
            matches = MD_URL_REGEX.findall(line)
            # Strip quotes from URLs
            cleaned_matches = [match.strip('"\'') for match in matches]
            urls.extend(cleaned_matches)
    return urls

def extract_headers(md_file):
    """Extract all headers from a markdown file and convert to slug format for link validation."""
    headers = []
    # Only attempt to extract headers from markdown files
    if not md_file.lower().endswith('.md'):
        print(f"Warning: Attempted to extract headers from non-markdown file: {md_file}")
        return headers
        
    try:
        with open(md_file, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip().startswith('#'):
                    # Extract the header text (remove the # and any leading/trailing whitespace)
                    header_text = line.lstrip('#').strip()
                    
                    # Convert to lowercase
                    header_text_lower = header_text.lower()
                    
                    # Remove markdown formatting (bold, italic, code)
                    header_text_clean = re.sub(r'[*_`]', '', header_text_lower)
                    
                    # Create slug: keep only alphanumeric chars and hyphens, replace spaces with hyphens
                    header_slug = re.sub(r'[^\w\- ]', '', header_text_clean)
                    header_slug = re.sub(r'\s+', '-', header_slug)
                    
                    # Add to the list of headers
                    headers.append(header_slug)
                    print(f"Found header: '{header_text}' -> slug: '{header_slug}'")
    except Exception as e:
        print(f"Warning: Could not extract headers from {md_file}: {str(e)}")
    return headers

def is_ip_based_url(url):
    """Check if a URL uses an IP address instead of a domain name."""
    try:
        host = urlparse(url).hostname
        ipaddress.ip_address(host)
        return True
    except ValueError:
        return False

def check_absolute_url(url, md_file=None, retries=3):
    """
    Check if an absolute URL (http/https) is reachable.
    
    Args:
        url: The URL to check
        md_file: Source markdown file containing this URL
        retries: Number of attempts before giving up
        
    Returns:
        Log entry string with result
    """
    # Skip checking for known valid URLs
    if url in KNOWN_VALID_URLS:
        log_entry = f"{Colors.OKGREEN}[OK ABSOLUTE] {url} (known valid URL){Colors.ENDC}"
        print(log_entry)
        return log_entry

    print(f"Checking absolute URL: {url}")
    attempt = 0
    while attempt < retries:
        try:
            # Make the request with configured timeout
            response = requests.get(url, headers=HEADERS, allow_redirects=True, timeout=TIMEOUT, stream=True)
            
            if response.status_code < 400:
                log_entry = f"{Colors.OKGREEN}[OK ABSOLUTE] {url}{Colors.ENDC}"
                print(log_entry)
                return log_entry
            else:
                file_info = f" (in file: {md_file})" if md_file else ""
                log_entry = f"{Colors.FAIL}[BROKEN ABSOLUTE] {url} - Status Code: {response.status_code}{file_info}{Colors.ENDC}"
                print(log_entry)
                return log_entry
        except requests.RequestException as e:
            file_info = f" (in file: {md_file})" if md_file else ""
            log_entry = f"{Colors.FAIL}[BROKEN ABSOLUTE] {url} - Error: {e}{file_info}{Colors.ENDC}"
            print(log_entry)
            attempt += 1
            if attempt < retries:
                print(f"Retrying... ({attempt}/{retries})")
            else:
                return log_entry

def check_relative_url(url, md_file):
    """
    Check if a relative file path exists in the filesystem.
    
    Args:
        url: Relative path to check
        md_file: Source markdown file containing this path
        
    Returns:
        Tuple containing: (log_entry, is_image, is_svg, is_root_relative, has_anchor)
    """
    # Flag to track if URL has an anchor
    has_anchor = '#' in url
    anchor_text = None
    
    # Handle header links (e.g., #section-name or file.md#section-name)
    if has_anchor and md_file.lower().endswith('.md'):
        base_url, anchor = url.split('#', 1)
        anchor_text = anchor
        # If it's a same-page link (just #header)
        if not base_url:
            headers = extract_headers(md_file)
            if anchor in headers:
                log_entry = f"{Colors.OKGREEN}[OK HEADER] #{anchor} (header in {md_file}){Colors.ENDC}"
                print(log_entry)
                return log_entry, False, False, False, has_anchor
            else:
                log_entry = f"{Colors.FAIL}[BROKEN HEADER] #{anchor} (header not found in {md_file}){Colors.ENDC}"
                print(f"Available headers in {md_file}: {', '.join(headers)}")
                print(log_entry)
                return log_entry, False, False, False, has_anchor
                
    # Handle hash in URL for non-markdown source files
    elif has_anchor:
        base_url, anchor = url.split('#', 1)
        anchor_text = anchor
        # For non-markdown file links with anchors, we just check if the file exists
        if not base_url:
            # Same-file anchor in non-markdown file, we can't validate this
            log_entry = f"{Colors.OKGREEN}[OK HEADER] #{anchor} (in non-markdown file {md_file}){Colors.ENDC}"
            print(log_entry)
            return log_entry, False, False, False, has_anchor
        else:
            target_file = os.path.join(os.path.dirname(md_file), base_url)
            if os.path.exists(target_file):
                log_entry = f"{Colors.OKGREEN}[OK RELATIVE] {target_file}#{anchor} (file exists, anchor not validated){Colors.ENDC}"
                print(log_entry)
                return log_entry, False, False, False, has_anchor
            else:
                log_entry = f"{Colors.FAIL}[BROKEN RELATIVE WITH ANCHOR] {target_file}#{anchor} (file not found){Colors.ENDC}"
                print(log_entry)
                return log_entry, False, False, False, has_anchor

    # Check if it's an SVG file
    is_svg = any(url.lower().endswith(ext) for ext in SVG_EXTENSIONS)
    # Check if it's an image file
    is_image = not is_svg and any(url.lower().endswith(ext) for ext in IMAGE_EXTENSIONS)
    
    # Handle root-relative URLs (starting with /)
    is_root_relative = url.startswith('/')
    if is_root_relative:
        # URLs starting with / are relative to repo root, not the current file
        file_path = os.path.join(REPO_PATH, url[1:])  # Remove leading / and join with repo root
        print(f"Root-relative path detected. Checking against repo root: {file_path}")
    else:
        # Regular document-relative URL
        file_path = os.path.join(os.path.dirname(md_file), url)
    
    file_type = "SVG" if is_svg else "image" if is_image else "root-relative" if is_root_relative else "relative"
    print(f"Checking {file_type} URL: {file_path}")
    
    # Add enhanced debugging for directory paths
    if url.endswith('/'):
        print(f"Directory path detected: {url}")
        print(f"Resolved path: {file_path}")
        print(f"Does path exist? {os.path.exists(file_path)}")
        print(f"Is it a directory? {os.path.isdir(file_path) if os.path.exists(file_path) else 'N/A'}")
        if os.path.exists(file_path) and os.path.isdir(file_path):
            print(f"Directory contents: {os.listdir(file_path)}")
    
    # Check if the path exists directly
    path_exists = os.path.exists(file_path)
    
    # If path doesn't exist and ends with '/', try to look for markdown files in that directory
    if not path_exists and url.endswith('/'):
        # First try common default files
        for default_file in ['_index.md', 'index.md', 'README.md']:
            index_path = os.path.join(file_path, default_file)
            print(f"Looking for default file: {index_path}")
            if os.path.exists(index_path):
                path_exists = True
                file_path = index_path
                print(f"Found default file: {index_path}")
                break
        
        # If still not found, check if directory exists and contains any markdown files
        if not path_exists and os.path.isdir(file_path):
            # Look for any markdown file in the directory
            try:
                md_files = [f for f in os.listdir(file_path) if f.endswith('.md')]
                if md_files:
                    path_exists = True
                    file_path = os.path.join(file_path, md_files[0])  # Use the first markdown file found
                    print(f"Directory contains markdown files: {', '.join(md_files)}")
                else:
                    print(f"Directory exists but contains no markdown files")
            except PermissionError:
                print(f"Permission error accessing directory: {file_path}")
            except FileNotFoundError:
                print(f"Directory doesn't exist: {file_path}")
    
    if path_exists:
        if is_svg:
            log_entry = f"{Colors.OKGREEN}[OK SVG] {file_path}{Colors.ENDC}"
        elif is_image:
            log_entry = f"{Colors.OKGREEN}[OK IMAGE] {file_path}{Colors.ENDC}"
        elif is_root_relative:
            log_entry = f"{Colors.OKGREEN}[OK ROOT-RELATIVE] {file_path} (root-relative path: {url}){Colors.ENDC}"
        else:
            log_entry = f"{Colors.OKGREEN}[OK RELATIVE] {file_path}{Colors.ENDC}"
        print(log_entry)
        return log_entry, is_image, is_svg, is_root_relative, has_anchor
    else:
        if is_svg:
            log_entry = f"{Colors.FAIL}[BROKEN SVG] {file_path} (SVG in {md_file}){Colors.ENDC}"
        elif is_image:
            log_entry = f"{Colors.FAIL}[BROKEN IMAGE] {file_path} (image in {md_file}){Colors.ENDC}"
        elif is_root_relative:
            log_entry = f"{Colors.FAIL}[BROKEN ROOT-RELATIVE] {file_path} (root-relative path: {url} in {md_file}){Colors.ENDC}"
        else:
            # Update the log message to indicate whether the URL has an anchor or not
            if has_anchor:
                log_entry = f"{Colors.FAIL}[BROKEN RELATIVE WITH ANCHOR] {url} (relative path in {md_file}){Colors.ENDC}"
            else:
                log_entry = f"{Colors.FAIL}[BROKEN RELATIVE WITHOUT ANCHOR] {url} (relative path in {md_file}){Colors.ENDC}"
        print(log_entry)
        return log_entry, is_image, is_svg, is_root_relative, has_anchor

def strip_ansi_escape_codes(text):
    """Remove ANSI color codes from text (for clean log files)."""
    return ANSI_ESCAPE_REGEX.sub('', text)

# =============================================================================
# MAIN EXECUTION
# =============================================================================

def main():
    # Lists to track results
    broken_absolute_urls = []
    ok_absolute_urls = []
    broken_relative_urls_with_anchor = []
    broken_relative_urls_without_anchor = []
    ok_relative_urls = []
    broken_image_urls = []
    ok_image_urls = []
    broken_svg_urls = []
    ok_svg_urls = []
    broken_header_urls = []
    ok_header_urls = []
    broken_root_relative_urls = []
    ok_root_relative_urls = []
    # Initialize the no_links_types list right here with the other lists
    no_links_types = []
    
    # Get all markdown files
    markdown_files = find_markdown_files()
    
    # Create log file with timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    log_file_with_timestamp = os.path.join(LOG_DIR, f'broken_urls_{timestamp}.log')
    
    print("Starting URL check...")
    start_time = datetime.now()
    
    # Process all files and URLs - write to log in real-time for monitoring
    with open(log_file_with_timestamp, 'w', encoding='utf-8') as log:
        log.write(f"URL Checker Results\n\n")
        log.write(f"Log generated on: {timestamp}\n")
        log.write("Processing URLs in real-time...\n\n")
        log.flush()
        
        for md_file in markdown_files:
            print(f"Processing file: {md_file}")
            urls = extract_urls(md_file)
            
            for url in urls:
                # Skip email links
                if EMAIL_REGEX.match(url):
                    print(f"Skipping email URL: {url}")
                    continue
                
                # Skip localhost and IP-based URLs
                if url.startswith("http://localhost") or is_ip_based_url(url):
                    print(f"Skipping localhost or IP-based URL: {url}")
                    continue
                
                # Check URL based on whether it's absolute or relative
                parsed_url = urlparse(url)
                if parsed_url.scheme in ('http', 'https'):
                    # It's an absolute URL - pass the file path to track source
                    log_entry = check_absolute_url(url, md_file)
                    if "[OK ABSOLUTE]" in log_entry:
                        ok_absolute_urls.append(log_entry)
                    else:
                        broken_absolute_urls.append(log_entry)
                else:
                    # Strip quotes before further processing to avoid false positives
                    url_clean = url.strip('"\'')
                    parsed_clean = urlparse(url_clean)
                    
                    # Check again if it's actually an absolute URL after stripping quotes
                    if parsed_clean.scheme in ('http', 'https'):
                        log_entry = check_absolute_url(url_clean, md_file)
                        if "[OK ABSOLUTE]" in log_entry:
                            ok_absolute_urls.append(log_entry)
                        else:
                            broken_absolute_urls.append(log_entry)
                    else:
                        # It's a relative URL, image, SVG, root-relative, or header link
                        log_entry, is_image, is_svg, is_root_relative, has_anchor = check_relative_url(url, md_file)
                        
                        if "[BROKEN HEADER]" in log_entry:
                            broken_header_urls.append(log_entry)
                        elif "[OK HEADER]" in log_entry:
                            ok_header_urls.append(log_entry)
                        # Changed order of these conditions to prioritize image/SVG type over root-relative
                        elif is_svg:
                            if "[OK SVG]" in log_entry:
                                ok_svg_urls.append(log_entry)
                            else:
                                broken_svg_urls.append(log_entry)
                        elif is_image:
                            if "[OK IMAGE]" in log_entry:
                                ok_image_urls.append(log_entry)
                            else:
                                broken_image_urls.append(log_entry)
                        elif is_root_relative:
                            if "[OK ROOT-RELATIVE]" in log_entry:
                                ok_root_relative_urls.append(log_entry)
                            else:
                                broken_root_relative_urls.append(log_entry)
                        else:
                            if "[OK RELATIVE]" in log_entry:
                                ok_relative_urls.append(log_entry)
                            else:
                                # Use the new log message format for categorization
                                if "[BROKEN RELATIVE WITH ANCHOR]" in log_entry:
                                    broken_relative_urls_with_anchor.append(log_entry)
                                elif "[BROKEN RELATIVE WITHOUT ANCHOR]" in log_entry:
                                    broken_relative_urls_without_anchor.append(log_entry)
                
                # Write to log file (real-time monitoring)
                log.write(strip_ansi_escape_codes(log_entry) + "\n")
                log.flush()
    
    # Calculate runtime
    end_time = datetime.now()
    runtime_duration = end_time - start_time
    
    # Write the log file with organized results
    with open(log_file_with_timestamp, 'w', encoding='utf-8') as log:
        log.write(f"URL Checker Results\n\n")
        log.write(f"Log generated on: {timestamp}\n")
        log.write(f"Runtime duration: {runtime_duration}\n\n")
        
        # Write broken sections first (most important)
        log.write("=== Broken Absolute URLs ===\n\n")
        if broken_absolute_urls:
            log.write("\n".join(strip_ansi_escape_codes(url) for url in broken_absolute_urls) + "\n\n")
        else:
            log.write("No broken absolute URLs found.\n\n")
        
        log.write("=== Broken Relative URLs Without Anchors ===\n\n")
        if broken_relative_urls_without_anchor:
            log.write("\n".join(strip_ansi_escape_codes(url) for url in broken_relative_urls_without_anchor) + "\n\n")
        else:
            log.write("No broken relative URLs without anchors found.\n\n")
        
        log.write("=== Broken Relative URLs With Anchors ===\n\n")
        if broken_relative_urls_with_anchor:
            log.write("\n".join(strip_ansi_escape_codes(url) for url in broken_relative_urls_with_anchor) + "\n\n")
        else:
            log.write("No broken relative URLs with anchors found.\n\n")
        
        log.write("=== Broken Root-Relative URLs ===\n\n")
        if broken_root_relative_urls:
            log.write("\n".join(strip_ansi_escape_codes(url) for url in broken_root_relative_urls) + "\n\n")
        else:
            log.write("No broken root-relative URLs found.\n\n")
        
        log.write("=== Broken Image URLs ===\n\n")
        if broken_image_urls:
            log.write("\n".join(strip_ansi_escape_codes(url) for url in broken_image_urls) + "\n\n")
        else:
            log.write("No broken image URLs found.\n\n")
        
        log.write("=== Broken SVG URLs ===\n\n")
        if broken_svg_urls:
            log.write("\n".join(strip_ansi_escape_codes(url) for url in broken_svg_urls) + "\n\n")
        else:
            log.write("No broken SVG URLs found.\n\n")
        
        log.write("=== Broken Header Links ===\n\n")
        if broken_header_urls:
            log.write("\n".join(strip_ansi_escape_codes(url) for url in broken_header_urls) + "\n\n")
        else:
            log.write("No broken header links found.\n\n")
        
        log.write("=== OK Absolute URLs ===\n\n")
        if ok_absolute_urls:
            log.write("\n".join(strip_ansi_escape_codes(url) for url in ok_absolute_urls) + "\n\n")
        else:
            log.write("No absolute URLs found.\n\n")
        
        log.write("=== OK Relative URLs ===\n\n")
        if ok_relative_urls:
            log.write("\n".join(strip_ansi_escape_codes(url) for url in ok_relative_urls) + "\n\n")
        else:
            log.write("No relative URLs found.\n\n")
        
        log.write("=== OK Root-Relative URLs ===\n\n")
        if ok_root_relative_urls:
            log.write("\n".join(strip_ansi_escape_codes(url) for url in ok_root_relative_urls) + "\n\n")
        else:
            log.write("No root-relative URLs found.\n\n")
        
        log.write("=== OK Image URLs ===\n\n")
        if ok_image_urls:
            log.write("\n".join(strip_ansi_escape_codes(url) for url in ok_image_urls) + "\n\n")
        else:
            log.write("No image URLs found.\n\n")
        
        log.write("=== OK SVG URLs ===\n\n")
        if ok_svg_urls:
            log.write("\n".join(strip_ansi_escape_codes(url) for url in ok_svg_urls) + "\n\n")
        else:
            log.write("No SVG URLs found.\n\n")
        
        log.write("=== OK Header Links ===\n\n")
        if ok_header_urls:
            log.write("\n".join(strip_ansi_escape_codes(url) for url in ok_header_urls) + "\n\n")
        else:
            log.write("No header links found.\n\n")
        
        # Add summary with improved informative title and hierarchical format
        total_broken = (len(broken_absolute_urls) + 
                        len(broken_relative_urls_with_anchor) + 
                        len(broken_relative_urls_without_anchor) + 
                        len(broken_root_relative_urls) + 
                        len(broken_image_urls) + 
                        len(broken_svg_urls) + 
                        len(broken_header_urls))
        
        total_ok = len(ok_absolute_urls) + len(ok_relative_urls) + len(ok_root_relative_urls) + len(ok_image_urls) + len(ok_svg_urls) + len(ok_header_urls)
        total_links = total_broken + total_ok
        
        # Calculate no links types BEFORE writing to log file
        no_links_types = []
        if len(broken_absolute_urls) == 0 and len(ok_absolute_urls) == 0:
            no_links_types.append("Absolute URLs")
        if len(broken_relative_urls_without_anchor) == 0 and len(broken_relative_urls_with_anchor) == 0 and len(ok_relative_urls) == 0:
            no_links_types.append("Relative URLs")
        if len(broken_root_relative_urls) == 0 and len(ok_root_relative_urls) == 0:
            no_links_types.append("Root-relative URLs")
        if len(broken_image_urls) == 0 and len(ok_image_urls) == 0:
            no_links_types.append("Image URLs")
        if len(broken_svg_urls) == 0 and len(ok_svg_urls) == 0:
            no_links_types.append("SVG URLs")
        if len(broken_header_urls) == 0 and len(ok_header_urls) == 0:
            no_links_types.append("Header links")
        
        log.write(f"Link Validation Summary ({total_links} links checked):\n")
        
        if total_broken > 0:
            log.write(f"- Broken links: {total_broken}\n")
            
            # Always show all categories, not just those with broken links
            log.write(f"  - Absolute URLs: {len(broken_absolute_urls)}\n")
            log.write(f"  - Relative URLs without anchors: {len(broken_relative_urls_without_anchor)}\n")
            log.write(f"  - Relative URLs with anchors: {len(broken_relative_urls_with_anchor)}\n")
            log.write(f"  - Root-relative URLs: {len(broken_root_relative_urls)}\n")
            log.write(f"  - Image URLs: {len(broken_image_urls)}\n")
            log.write(f"  - SVG URLs: {len(broken_svg_urls)}\n")
            log.write(f"  - Header links: {len(broken_header_urls)}\n")
        else:
            log.write("- Broken links: 0\n")
        
        # Add no links found section to log file - same as console output
        if no_links_types:
            log.write(f"- No links found: {len(no_links_types)} categories\n")
            for category in no_links_types:
                log.write(f"  - {category}\n")
            
        log.write(f"- OK links: {total_ok}\n")
        
        # Add final conclusion with emoji - same as console output
        broken_links_found = bool(broken_absolute_urls or broken_relative_urls_without_anchor or broken_relative_urls_with_anchor or
                                 broken_root_relative_urls or broken_image_urls or broken_svg_urls or broken_header_urls)
        if broken_links_found:
            log.write(f"❌ Broken links were found. Check the logs for details.\n")
        else:
            log.write(f"✅ All links are valid!\n")
    
    # Print results to console
    print(f"Check complete. See {log_file_with_timestamp} for details.")
    
    print(f"\nLog generated on: {timestamp}")
    print(f"Runtime duration: {runtime_duration}")
    print(f"Total broken absolute URLs: {len(broken_absolute_urls)}")
    print(f"Total broken relative URLs (without anchors): {len(broken_relative_urls_without_anchor)}")
    print(f"Total broken relative URLs (with anchors): {len(broken_relative_urls_with_anchor)}")
    print(f"Total OK absolute URLs: {len(ok_absolute_urls)}")
    print(f"Total OK relative URLs: {len(ok_relative_urls)}")
    print(f"Total broken root-relative URLs: {len(broken_root_relative_urls)}")
    print(f"Total OK root-relative URLs: {len(ok_root_relative_urls)}")
    print(f"Total broken image URLs: {len(broken_image_urls)}")
    print(f"Total OK image URLs: {len(ok_image_urls)}")
    print(f"Total broken SVG URLs: {len(broken_svg_urls)}")
    print(f"Total OK SVG URLs: {len(ok_svg_urls)}")
    print(f"Total broken header links: {len(broken_header_urls)}")
    print(f"Total OK header links: {len(ok_header_urls)}")
    
    print("\n=== Broken Absolute URLs ===")
    for url in broken_absolute_urls:
        print(f"{Colors.FAIL}{strip_ansi_escape_codes(url)}{Colors.ENDC}")
    
    print("\n=== Broken Relative URLs Without Anchors ===")
    for url in broken_relative_urls_without_anchor:
        print(f"{Colors.FAIL}{strip_ansi_escape_codes(url)}{Colors.ENDC}")
        
    print("\n=== Broken Relative URLs With Anchors ===")
    for url in broken_relative_urls_with_anchor:
        print(f"{Colors.FAIL}{strip_ansi_escape_codes(url)}{Colors.ENDC}")
        
    print("\n=== Broken Root-Relative URLs ===")
    for url in broken_root_relative_urls:
        print(f"{Colors.FAIL}{strip_ansi_escape_codes(url)}{Colors.ENDC}")
    print("\n=== Broken Image URLs ===")
    for url in broken_image_urls:
        print(f"{Colors.FAIL}{strip_ansi_escape_codes(url)}{Colors.ENDC}")
    print("\n=== Broken SVG URLs ===")
    for url in broken_svg_urls:
        print(f"{Colors.FAIL}{strip_ansi_escape_codes(url)}{Colors.ENDC}")
    print("\n=== Broken Header Links ===")
    for url in broken_header_urls:
        print(f"{Colors.FAIL}{strip_ansi_escape_codes(url)}{Colors.ENDC}")
    print("\n=== OK Absolute URLs ===")
    for url in ok_absolute_urls:
        print(f"{Colors.OKGREEN}{strip_ansi_escape_codes(url)}{Colors.ENDC}")
    print("\n=== OK Relative URLs ===")
    for url in ok_relative_urls:
        print(f"{Colors.OKGREEN}{strip_ansi_escape_codes(url)}{Colors.ENDC}")
    print("\n=== OK Root-Relative URLs ===")
    for url in ok_root_relative_urls:
        print(f"{Colors.OKGREEN}{strip_ansi_escape_codes(url)}{Colors.ENDC}")
    print("\n=== OK Image URLs ===")
    for url in ok_image_urls:
        print(f"{Colors.OKGREEN}{strip_ansi_escape_codes(url)}{Colors.ENDC}")
    print("\n=== OK SVG URLs ===")
    for url in ok_svg_urls:
        print(f"{Colors.OKGREEN}{strip_ansi_escape_codes(url)}{Colors.ENDC}")
    print("\n=== OK Header Links ===")
    for url in ok_header_urls:
        print(f"{Colors.OKGREEN}{strip_ansi_escape_codes(url)}{Colors.ENDC}")

    # Print summary table with improved title and color coding
    total_broken = (len(broken_absolute_urls) + 
                    len(broken_relative_urls_with_anchor) + 
                    len(broken_relative_urls_without_anchor) + 
                    len(broken_root_relative_urls) + 
                    len(broken_image_urls) + 
                    len(broken_svg_urls) + 
                    len(broken_header_urls))
    
    total_ok = len(ok_absolute_urls) + len(ok_relative_urls) + len(ok_root_relative_urls) + len(ok_image_urls) + len(ok_svg_urls) + len(ok_header_urls)
    total_links = total_broken + total_ok
    
    # Title in cyan (INFO color)
    print(f"\n{Colors.INFO}Link Validation Summary ({total_links} links checked):{Colors.ENDC}")
    
    # Add categories with no links found to the no_links_types list
    no_links_types = []
    if len(broken_absolute_urls) == 0 and len(ok_absolute_urls) == 0:
        no_links_types.append("Absolute URLs")
    if len(broken_relative_urls_without_anchor) == 0 and len(broken_relative_urls_with_anchor) == 0 and len(ok_relative_urls) == 0:
        no_links_types.append("Relative URLs")
    if len(broken_root_relative_urls) == 0 and len(ok_root_relative_urls) == 0:
        no_links_types.append("Root-relative URLs")
    if len(broken_image_urls) == 0 and len(ok_image_urls) == 0:
        no_links_types.append("Image URLs")
    if len(broken_svg_urls) == 0 and len(ok_svg_urls) == 0:
        no_links_types.append("SVG URLs")
    if len(broken_header_urls) == 0 and len(ok_header_urls) == 0:
        no_links_types.append("Header links")
    
    if total_broken > 0:
        print(f"{Colors.FAIL}- Broken links: {total_broken}{Colors.ENDC}")
        
        # Always show all categories of broken links, even if count is 0
        print(f"{Colors.FAIL if len(broken_absolute_urls) > 0 else Colors.INFO}  - Absolute URLs: {len(broken_absolute_urls)}{Colors.ENDC}")
        print(f"{Colors.FAIL if len(broken_relative_urls_without_anchor) > 0 else Colors.INFO}  - Relative URLs without anchors: {len(broken_relative_urls_without_anchor)}{Colors.ENDC}")
        print(f"{Colors.FAIL if len(broken_relative_urls_with_anchor) > 0 else Colors.INFO}  - Relative URLs with anchors: {len(broken_relative_urls_with_anchor)}{Colors.ENDC}")
        print(f"{Colors.FAIL if len(broken_root_relative_urls) > 0 else Colors.INFO}  - Root-relative URLs: {len(broken_root_relative_urls)}{Colors.ENDC}")
        print(f"{Colors.FAIL if len(broken_image_urls) > 0 else Colors.INFO}  - Image URLs: {len(broken_image_urls)}{Colors.ENDC}")
        print(f"{Colors.FAIL if len(broken_svg_urls) > 0 else Colors.INFO}  - SVG URLs: {len(broken_svg_urls)}{Colors.ENDC}")
        print(f"{Colors.FAIL if len(broken_header_urls) > 0 else Colors.INFO}  - Header links: {len(broken_header_urls)}{Colors.ENDC}")
    else:
        print(f"{Colors.INFO}- Broken links: 0{Colors.ENDC}")
        
    # Display categories with no links found
    if no_links_types:
        print(f"{Colors.NEUTRAL}- No links found: {len(no_links_types)} categories{Colors.ENDC}")
        for category in no_links_types:
            print(f"{Colors.NEUTRAL}  - {category}{Colors.ENDC}")
        
    print(f"{Colors.OKGREEN}- OK links: {total_ok}{Colors.ENDC}")

    # Determine if any broken links were found
    broken_links_found = bool(broken_absolute_urls or broken_relative_urls_with_anchor or broken_relative_urls_without_anchor or broken_root_relative_urls or broken_image_urls or broken_svg_urls or broken_header_urls)

    # Exit with appropriate code
    if broken_links_found:
        print(f"{Colors.FAIL}❌ Broken links were found. Check the logs for details.{Colors.ENDC}")
        sys.exit(1)  # Exit code 1 signals that broken links were found
    else:
        print(f"{Colors.OKGREEN}✅ All links are valid!{Colors.ENDC}")
        sys.exit(0)  # Exit code 0 signals that all links are valid

if __name__ == "__main__":
    main()