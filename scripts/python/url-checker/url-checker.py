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
KNOWN_VALID_DOMAINS = [
    "learn.microsoft.com",
    "whatismyip.com",
    "www.linkedin.com",
    "linkedin.com",
    "icanhazip.com",
    "shell.azure.com",
    # Add more domains to skip here as needed
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

# Define a list of temporary error status codes
TEMPORARY_ERROR_CODES = [502, 503, 504, 429]  # Added 429 (Too Many Requests)

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
    # Extract domain from URL for domain-based verification
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    is_trusted_domain = domain in KNOWN_VALID_DOMAINS
    
    print(f"Checking absolute URL: {url}")
    print(f"Domain: {domain}, Trusted: {is_trusted_domain}")
    
    attempt = 0
    while attempt < retries:
        try:
            # Make the request with configured timeout
            response = requests.get(url, headers=HEADERS, allow_redirects=True, timeout=TIMEOUT, stream=True)
            
            if response.status_code < 400:
                log_entry = f"{Colors.OKGREEN}[OK ABSOLUTE] {url}{Colors.ENDC}"
                print(log_entry)
                return log_entry
            elif response.status_code in TEMPORARY_ERROR_CODES:
                # For temporary errors, handle differently based on trusted status
                print(f"Status Code {response.status_code} for {url}. Retrying... ({attempt + 1}/{retries})")
                attempt += 1
                
                if attempt >= retries:
                    file_info = f" (in file: {md_file})" if md_file else ""
                    
                    if is_trusted_domain:
                        # For trusted domains, mark as OK even with temporary errors
                        log_entry = f"{Colors.OKGREEN}[OK ABSOLUTE] {url} (trusted domain with temporary status code: {response.status_code}){file_info}{Colors.ENDC}"
                        print(log_entry)
                        return log_entry
                    else:
                        # For non-trusted domains, still mark as broken but note it might be temporary
                        log_entry = f"{Colors.FAIL}[BROKEN ABSOLUTE] {url} - Temporary error: {response.status_code}{file_info}{Colors.ENDC}"
                        print(log_entry)
                        return log_entry
            else:
                file_info = f" (in file: {md_file})" if md_file else ""
                # For non-temporary errors, mark as broken even for trusted domains
                log_entry = f"{Colors.FAIL}[BROKEN ABSOLUTE] {url} - Status Code: {response.status_code}{file_info}{Colors.ENDC}"
                print(log_entry)
                return log_entry
                
        except requests.RequestException as e:
            file_info = f" (in file: {md_file})" if md_file else ""
            
            # For connection errors on trusted domains, consider as temporarily unavailable
            if is_trusted_domain and isinstance(e, (
                requests.Timeout, 
                requests.ConnectionError,
                requests.TooManyRedirects
            )):
                # Last retry and it's a trusted domain with connection issues
                if attempt >= retries - 1:
                    log_entry = f"{Colors.OKGREEN}[OK ABSOLUTE] {url} (trusted domain, connection issue: {type(e).__name__}){file_info}{Colors.ENDC}"
                    print(log_entry)
                    return log_entry
            
            log_entry = f"{Colors.FAIL}[BROKEN ABSOLUTE] {url} - Error: {e}{file_info}{Colors.ENDC}"
            print(log_entry)
            attempt += 1
            if attempt < retries:
                print(f"Retrying... ({attempt}/{retries})")
            else:
                return log_entry

def find_case_insensitive_path(path):
    """
    Tries to find an existing path with case-insensitive matching.
    Useful for systems where the filesystem is case-sensitive but the URLs might not match case.
    
    Args:
        path: The path to check
        
    Returns:
        The correct path if found with different case, None otherwise
    """
    # If the path exists exactly as provided, no need to search
    if os.path.exists(path):
        return path
    
    # Not found, try to match case-insensitively
    dirname, basename = os.path.split(path)
    
    # If the directory doesn't exist, we can't check its contents
    if not os.path.isdir(dirname):
        return None

    try:
        # Check if a case-insensitive match exists in the parent directory
        for entry in os.listdir(dirname):
            if entry.lower() == basename.lower():
                return os.path.join(dirname, entry)
    except (PermissionError, FileNotFoundError):
        pass
            
    return None

def find_path_case_insensitive(base_path, rel_path):
    """
    Find a path with case-insensitive matching, handling multi-level paths.
    
    Args:
        base_path: Starting directory for the search
        rel_path: Relative path to find (can include multiple directories)
        
    Returns:
        Full corrected path if found, None otherwise
    """
    # Handle empty path
    if not rel_path:
        return base_path
    
    # Split the path into components, handling both forward and back slashes
    path_parts = re.split(r'[/\\]', rel_path)
    path_parts = [part for part in path_parts if part]  # Remove empty parts
    
    current_path = base_path
    print(f"Starting case-insensitive path search from: {current_path}")
    print(f"Looking for path components: {path_parts}")
    
    # Process each path component
    for i, part in enumerate(path_parts):
        # Skip if the component is '.' (current directory)
        if part == '.':
            continue
        
        # Handle '..' (parent directory) - just use it directly as it doesn't need case correction
        if part == '..':
            current_path = os.path.dirname(current_path)
            print(f"Going up to parent directory: {current_path}")
            continue
        
        # Try to find a case-insensitive match for this component
        found = False
        try:
            if os.path.exists(os.path.join(current_path, part)):
                # Exact match exists, use it directly
                current_path = os.path.join(current_path, part)
                found = True
                print(f"Exact match found for '{part}': {current_path}")
            else:
                # Try case-insensitive match
                for entry in os.listdir(current_path):
                    if entry.lower() == part.lower():
                        current_path = os.path.join(current_path, entry)
                        found = True
                        print(f"Case-insensitive match found for '{part}': {entry} at {current_path}")
                        break
        except (PermissionError, FileNotFoundError, NotADirectoryError) as e:
            print(f"Error accessing {current_path}: {str(e)}")
            return None
        
        if not found:
            print(f"No match found for component '{part}' in {current_path}")
            return None
    
    # Add trailing slash if the original path had one
    if rel_path.endswith('/') and not current_path.endswith(os.sep):
        current_path += os.sep
    
    print(f"Final resolved path: {current_path}")
    return current_path

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
        else:
            # Construct the target path based on the base_url
            target_file = os.path.join(os.path.dirname(md_file), base_url)
            
            # Handle the case where the base_url points to a directory
            if os.path.isdir(target_file):
                print(f"Base URL {base_url} points to a directory: {target_file}")
                # Check if an _index.md file exists in the directory
                index_file = os.path.join(target_file, "_index.md")
                if os.path.exists(index_file):
                    log_entry = f"{Colors.OKGREEN}[OK RELATIVE] {index_file}#{anchor} (directory with _index.md, anchor not validated){Colors.ENDC}"
                    print(log_entry)
                    return log_entry, False, False, False, has_anchor
                
                # Also check for other common index files
                for index_name in ["index.md", "README.md"]:
                    index_file = os.path.join(target_file, index_name)
                    if os.path.exists(index_file):
                        log_entry = f"{Colors.OKGREEN}[OK RELATIVE] {index_file}#{anchor} (directory with {index_name}, anchor not validated){Colors.ENDC}"
                        print(log_entry)
                        return log_entry, False, False, False, has_anchor
            
            # Check if file exists without case sensitivity
            case_insensitive_path = find_path_case_insensitive(os.path.dirname(md_file), base_url)
            if case_insensitive_path and os.path.exists(case_insensitive_path):
                # Found with case-insensitive match
                if os.path.isdir(case_insensitive_path):
                    # It's a directory, check for index files
                    for index_name in ["_index.md", "index.md", "README.md"]:
                        index_file = os.path.join(case_insensitive_path, index_name)
                        if os.path.exists(index_file):
                            log_entry = f"{Colors.OKGREEN}[OK RELATIVE] {index_file}#{anchor} (directory with {index_name}, case-insensitive match, anchor not validated){Colors.ENDC}"
                            print(log_entry)
                            return log_entry, False, False, False, has_anchor
                else:
                    # It's a file
                    log_entry = f"{Colors.OKGREEN}[OK RELATIVE] {case_insensitive_path}#{anchor} (file exists, case-insensitive match, anchor not validated){Colors.ENDC}"
                    print(log_entry)
                    return log_entry, False, False, False, has_anchor
            
            # Original check if file exists (case sensitive)
            if os.path.exists(target_file):
                log_entry = f"{Colors.OKGREEN}[OK RELATIVE] {target_file}#{anchor} (file exists, anchor not validated){Colors.ENDC}"
                print(log_entry)
                return log_entry, False, False, False, has_anchor
            else:
                log_entry = f"{Colors.FAIL}[BROKEN RELATIVE WITH ANCHOR] {target_file}#{anchor} (file not found){Colors.ENDC}"
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
    
    # -- New Approach: Handle case sensitivity more robustly --
    # Check if path exists directly
    path_exists = os.path.exists(file_path)
    
    # If path doesn't exist, try case-insensitive matching
    if not path_exists:
        print(f"Path not found: {file_path}")
        print(f"Trying case-insensitive path resolution...")
        
        # For directory URLs (ending with /)
        if url.endswith('/'):
            # Split the file_path into components
            path_parts = os.path.normpath(file_path).split(os.sep)
            
            # Start from an existing directory
            current = os.path.dirname(md_file) if not is_root_relative else REPO_PATH
            built_path = current
            
            # Process each segment of the relative path
            rel_segments = url.rstrip('/').split('/')
            print(f"Processing relative segments: {rel_segments}")
            
            for segment in rel_segments:
                if segment == '..':
                    # Go up one directory
                    current = os.path.dirname(current)
                    built_path = current
                    print(f"Going up to parent: {current}")
                elif segment == '.':
                    # Stay in current directory
                    continue
                else:
                    # Try to find a case-insensitive match for this segment
                    if os.path.exists(os.path.join(current, segment)):
                        # Exact case match
                        current = os.path.join(current, segment)
                        built_path = current
                        print(f"Exact match found: {segment}")
                    else:
                        found = False
                        try:
                            for item in os.listdir(current):
                                if item.lower() == segment.lower():
                                    current = os.path.join(current, item)
                                    built_path = current
                                    print(f"Case-insensitive match found: {segment} -> {item}")
                                    found = True
                                    break
                        except (PermissionError, FileNotFoundError, NotADirectoryError) as e:
                            print(f"Error accessing {current}: {str(e)}")
                        
                        if not found:
                            print(f"No match found for segment: {segment} in {current}")
                            break
            
            if os.path.exists(built_path):
                file_path = built_path
                path_exists = True
                print(f"Successfully resolved case-insensitive path: {built_path}")
                
                # Check for default files in the directory
                if os.path.isdir(built_path):
                    for default_file in ['_index.md', 'index.md', 'README.md']:
                        default_path = os.path.join(built_path, default_file)
                        if os.path.exists(default_path):
                            file_path = default_path
                            print(f"Found default file: {default_path}")
                            break
    
    # If path still doesn't exist and it's a directory URL, try to check for markdown files
    if not path_exists and url.endswith('/') and os.path.isdir(os.path.dirname(file_path)):
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
        log.write(f"=== Broken Absolute URLs ({len(broken_absolute_urls)} links found) ===\n\n")
        if broken_absolute_urls:
            log.write("\n".join(strip_ansi_escape_codes(url) for url in broken_absolute_urls) + "\n\n")
        else:
            log.write("No broken absolute URLs found.\n\n")
        
        log.write(f"=== Broken Relative URLs Without Anchors ({len(broken_relative_urls_without_anchor)} links found) ===\n\n")
        if broken_relative_urls_without_anchor:
            log.write("\n".join(strip_ansi_escape_codes(url) for url in broken_relative_urls_without_anchor) + "\n\n")
        else:
            log.write("No broken relative URLs without anchors found.\n\n")
        
        log.write(f"=== Broken Relative URLs With Anchors ({len(broken_relative_urls_with_anchor)} links found) ===\n\n")
        if broken_relative_urls_with_anchor:
            log.write("\n".join(strip_ansi_escape_codes(url) for url in broken_relative_urls_with_anchor) + "\n\n")
        else:
            log.write("No broken relative URLs with anchors found.\n\n")
        
        log.write(f"=== Broken Root-Relative URLs ({len(broken_root_relative_urls)} links found) ===\n\n")
        if broken_root_relative_urls:
            log.write("\n".join(strip_ansi_escape_codes(url) for url in broken_root_relative_urls) + "\n\n")
        else:
            log.write("No broken root-relative URLs found.\n\n")
        
        log.write(f"=== Broken Image URLs ({len(broken_image_urls)} links found) ===\n\n")
        if broken_image_urls:
            log.write("\n".join(strip_ansi_escape_codes(url) for url in broken_image_urls) + "\n\n")
        else:
            log.write("No broken image URLs found.\n\n")
        
        log.write(f"=== Broken SVG URLs ({len(broken_svg_urls)} links found) ===\n\n")
        if broken_svg_urls:
            log.write("\n".join(strip_ansi_escape_codes(url) for url in broken_svg_urls) + "\n\n")
        else:
            log.write("No broken SVG URLs found.\n\n")
        
        log.write(f"=== Broken Header Links ({len(broken_header_urls)} links found) ===\n\n")
        if broken_header_urls:
            log.write("\n".join(strip_ansi_escape_codes(url) for url in broken_header_urls) + "\n\n")
        else:
            log.write("No broken header links found.\n\n")
        
        log.write(f"=== OK Absolute URLs ({len(ok_absolute_urls)} links found) ===\n\n")
        if ok_absolute_urls:
            log.write("\n".join(strip_ansi_escape_codes(url) for url in ok_absolute_urls) + "\n\n")
        else:
            log.write("No absolute URLs found.\n\n")
        
        log.write(f"=== OK Relative URLs ({len(ok_relative_urls)} links found) ===\n\n")
        if ok_relative_urls:
            log.write("\n".join(strip_ansi_escape_codes(url) for url in ok_relative_urls) + "\n\n")
        else:
            log.write("No relative URLs found.\n\n")
        
        log.write(f"=== OK Root-Relative URLs ({len(ok_root_relative_urls)} links found) ===\n\n")
        if ok_root_relative_urls:
            log.write("\n".join(strip_ansi_escape_codes(url) for url in ok_root_relative_urls) + "\n\n")
        else:
            log.write("No root-relative URLs found.\n\n")
        
        log.write(f"=== OK Image URLs ({len(ok_image_urls)} links found) ===\n\n")
        if ok_image_urls:
            log.write("\n".join(strip_ansi_escape_codes(url) for url in ok_image_urls) + "\n\n")
        else:
            log.write("No image URLs found.\n\n")
        
        log.write(f"=== OK SVG URLs ({len(ok_svg_urls)} links found) ===\n\n")
        if ok_svg_urls:
            log.write("\n".join(strip_ansi_escape_codes(url) for url in ok_svg_urls) + "\n\n")
        else:
            log.write("No SVG URLs found.\n\n")
        
        log.write(f"=== OK Header Links ({len(ok_header_urls)} links found) ===\n\n")
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
        
        # Updated categorization logic
        no_links_types = []  # Categories with no links at all (neither broken nor OK)
        zero_broken_types = []  # Categories with OK links but no broken links
        broken_types = []  # Categories with broken links
        
        # Absolute URLs
        if len(broken_absolute_urls) == 0 and len(ok_absolute_urls) == 0:
            no_links_types.append(("Absolute URLs", 0))
        elif len(broken_absolute_urls) == 0:
            zero_broken_types.append(("Absolute URLs", len(ok_absolute_urls)))
        else:
            broken_types.append(("Absolute URLs", len(broken_absolute_urls)))
            
        # Relative URLs without anchors and with anchors combined
        if len(broken_relative_urls_without_anchor) == 0 and len(broken_relative_urls_with_anchor) == 0 and len(ok_relative_urls) == 0:
            no_links_types.append(("Relative URLs", 0))
        elif len(broken_relative_urls_without_anchor) == 0 and len(broken_relative_urls_with_anchor) == 0:
            zero_broken_types.append(("Relative URLs", len(ok_relative_urls)))
        else:
            # Count broken relative URLs with and without anchors separately
            if len(broken_relative_urls_without_anchor) > 0:
                broken_types.append(("Relative URLs without anchors", len(broken_relative_urls_without_anchor)))
            if len(broken_relative_urls_with_anchor) > 0:
                broken_types.append(("Relative URLs with anchors", len(broken_relative_urls_with_anchor)))
                
        # Root-relative URLs
        if len(broken_root_relative_urls) == 0 and len(ok_root_relative_urls) == 0:
            no_links_types.append(("Root-relative URLs", 0))
        elif len(broken_root_relative_urls) == 0:
            zero_broken_types.append(("Root-relative URLs", len(ok_root_relative_urls)))
        else:
            broken_types.append(("Root-relative URLs", len(broken_root_relative_urls)))
            
        # Image URLs
        if len(broken_image_urls) == 0 and len(ok_image_urls) == 0:
            no_links_types.append(("Image URLs", 0))
        elif len(broken_image_urls) == 0:
            zero_broken_types.append(("Image URLs", len(ok_image_urls)))
        else:
            broken_types.append(("Image URLs", len(broken_image_urls)))
            
        # SVG URLs
        if len(broken_svg_urls) == 0 and len(ok_svg_urls) == 0:
            no_links_types.append(("SVG URLs", 0))
        elif len(broken_svg_urls) == 0:
            zero_broken_types.append(("SVG URLs", len(ok_svg_urls)))
        else:
            broken_types.append(("SVG URLs", len(broken_svg_urls)))
            
        # Header links
        if len(broken_header_urls) == 0 and len(ok_header_urls) == 0:
            no_links_types.append(("Header links", 0))
        elif len(broken_header_urls) == 0:
            zero_broken_types.append(("Header links", len(ok_header_urls)))
        else:
            broken_types.append(("Header links", len(broken_header_urls)))
        
        # Write summary to log file
        log.write(f"Link Validation Summary ({total_links} links checked):\n")
        
        # Always show broken links section if there are any broken links
        if total_broken > 0:
            log.write(f"- Broken links: {total_broken}\n")
            # Only show categories that actually have broken links
            for category, count in broken_types:
                log.write(f"  - {category}: {count}\n")
        else:
            log.write("- Broken links: 0\n")
        
        # Show categories with no links found
        if no_links_types:
            log.write(f"- No links found: {len(no_links_types)} categories\n")
            for category, _ in no_links_types:
                log.write(f"  - {category}\n")
            
        # Show categories with no broken links (but have OK links)
        if zero_broken_types:
            log.write(f"- Categories with no broken links: {len(zero_broken_types)}\n")
            for category, count in zero_broken_types:
                log.write(f"  - {category}: {count} OK links\n")
            
        log.write(f"- OK links: {total_ok}\n")
        
        # Add final conclusion with emoji
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
    
    # Always show broken links section if there are any broken links
    if total_broken > 0:
        print(f"{Colors.FAIL}- Broken links: {total_broken}{Colors.ENDC}")
        # Only show categories that actually have broken links
        for category, count in broken_types:
            print(f"{Colors.FAIL}  - {category}: {count}{Colors.ENDC}")
    else:
        print(f"{Colors.INFO}- Broken links: 0{Colors.ENDC}")
        
    # Show categories with no links found
    if no_links_types:
        print(f"{Colors.NEUTRAL}- No links found: {len(no_links_types)} categories{Colors.ENDC}")
        for category, _ in no_links_types:
            print(f"{Colors.NEUTRAL}  - {category}{Colors.ENDC}")
    
    # Show categories with no broken links (but have OK links)
    if zero_broken_types:
        print(f"{Colors.INFO}- Categories with no broken links: {len(zero_broken_types)}{Colors.ENDC}")
        for category, count in zero_broken_types:
            print(f"{Colors.INFO}  - {category}: {count} OK links{Colors.ENDC}")
            
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