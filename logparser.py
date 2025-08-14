import sys
import re

def parse_log(file):
    pattern = re.compile(r'(?P<ip>\S+) - - \[(?P<time>.*)] "(?P<method>.*?) (?P<url>.*?) (?P<protocol>.*?)"'
                         r' (?P<status>\d+) (?P<size>\d+) "(?P<referrer>.*?)" "(?P<user_agent>.*?)"')

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 logparser.py <nginx_access_log_file>")
        sys.exit(1)

