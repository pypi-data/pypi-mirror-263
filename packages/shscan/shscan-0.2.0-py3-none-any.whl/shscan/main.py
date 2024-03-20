import sys, requests, warnings
from requests.exceptions import RequestException
from urllib3.exceptions import InsecureRequestWarning
from shscan import main


warnings.simplefilter('ignore', InsecureRequestWarning)

def get_security_headers(url, ssl=False):
    try:
        if ssl:
            response = requests.get(url, allow_redirects=True, timeout=5, verify=True)
        else:
            response = requests.get(url, allow_redirects=True, timeout=5, verify=False)
        security_headers = {
             'Content-Security-Policy': response.headers.get('Content-Security-Policy'),
             'Strict-Transport-Security': response.headers.get('Strict-Transport-Security'),
             'Referrer-Policy': response.headers.get('Referrer-Policy'),
             'Feature-Policy': response.headers.get('Feature-Policy'),
             'Permissions-Policy': response.headers.get('Permissions-Policy'),
             'X-Content-Type-Options': response.headers.get('X-Content-Type-Options'),
             'X-Frame-Options': response.headers.get('X-Frame-Options'),
             'X-XSS-Protection': response.headers.get('X-XSS-Protection'),
             'X-Download-Options': response.headers.get('X-Download-Options'),
             'X-Content-Security-Policy': response.headers.get('X-Content-Security-Policy'),
             'Content-Security-Policy-Report-Only': response.headers.get('Content-Security-Policy-Report-Only'),
             'Clear-Site-Data': response.headers.get('Clear-Site-Data'),
             'Cross-Origin-Embedder-Policy': response.headers.get('Cross-Origin-Embedder-Policy'),
             'Cross-Origin-Opener-Policy': response.headers.get('Cross-Origin-Opener-Policy'),
             'Cross-Origin-Resource-Policy': response.headers.get('Cross-Origin-Resource-Policy'),
             'X-Webkit-CSP': response.headers.get('X-Webkit-CSP'),

        }
        return security_headers
    except RequestException as e:
        print(f"Error requesting {url}: {e}")
        return {}

def display_menu(title, url, headers):
    title_length = len(title) + 2
    url_length = len(url) + 2
    border_length = max(title_length, url_length) + 4
    border = "==" * border_length
    print(f"\n{border}\n {title:^{border_length}} \n")
    print(f" URL: {url:^{border_length}} \n")
    print(border)

# emojis
    emoji_verde = '\033[32m\U0001F197\033[0m |'
    emoji_vermelho = '\033[31m\u274C\033[0m |'

    implemented_headers = []
    not_implemented_headers = []

    for header, value in headers.items():
        if value:
            implemented_headers.append(f"{emoji_verde} {header}: {value}")
        else:
            not_implemented_headers.append(f"{emoji_vermelho} {header}: ")

# Print headers

    if implemented_headers:
        print("\n-----------------------------------")
        print("Implemented Headers:")
        print("-----------------------------------\n")
        for header in implemented_headers:
            print(header)

    if not_implemented_headers:
        print("\n-----------------------------------")
        print("Not implemented Headers:")
        print("-----------------------------------\n")
        for header in not_implemented_headers:
            print(header)


def help_menu():

    print("Usage: python SHScan.py <URL> [-ssl]")
    print("\nOptions:")
    print("  -h: Open help menu.")
    print("  -ssl: Test the URL with SSL enabled.")
    print("  No options: Test the URL without SSL")

def main():
    if len(sys.argv) < 2 or sys.argv[1] == "-h":
        help_menu()
        return

    url = sys.argv[1]
    ssl = False

    if len(sys.argv) == 3 and sys.argv[2] == "-ssl":
        ssl = True


    headers = get_security_headers(url, ssl)
    if headers:
        display_menu("SECURITY HEADERS", url, headers)
        
if __name__ == "__main__":
    main()