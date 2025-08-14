import sys
import re
from user_agents import parse

def parse_log(file):
    pattern = re.compile(r'(?P<ip>\S+) - - \[(?P<time>.*?)] "(?P<method>.*?) (?P<url>.*?) (?P<protocol>.*?)"'
                         r' (?P<status>\d+) (?P<size>\d+) "(?P<referrer>.*?)" "(?P<user_agent>.*?)"')

    with open(file, 'r') as f:
        for line in f:
            match = pattern.match(line)
            if match:
                data = match.groupdict()
                user_agent = parse(data['user_agent'])
                data['browser'] = user_agent.browser.family
                data['os'] = user_agent.os.family
                if user_agent.device.family:
                    data['device'] = user_agent.device.family
                else:
                    data['device'] = "Unknown"
                print(data)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 logparser.py <nginx_access_log_file>")
        sys.exit(1)

    log_file = sys.argv[1]
    parse_log(log_file)

