import sys
import re
from user_agents import parse
import json

def parse_log(file):
    # Create regex pattern based on nginx combined format
    pattern = re.compile(r'(?P<ip>\S+) - - \[(?P<time>.*?)] "(?P<method>.*?) (?P<url>.*?) (?P<protocol>.*?)"'
                         r' (?P<status>\d+) (?P<size>\d+) "(?P<referrer>.*?)" "(?P<user_agent>.*?)"')
    logs = []

    with open(file, 'r') as f:
        for line in f:
            match = pattern.match(line)
            if match:
                data = match.groupdict()
                # Extract enriched details from User-Agent field
                user_agent = parse(data['user_agent'])
                data['browser'] = user_agent.browser.family
                data['os'] = user_agent.os.family
                if user_agent.device.family:
                    data['device'] = user_agent.device.family
                else:
                    data['device'] = "Unknown"
                logs.append(data)

    return logs

if __name__ == "__main__":
    # Check for correct script usage
    if len(sys.argv) < 2:
        print("Usage: python3 logparser.py <nginx_access_log_file>")
        sys.exit(1)

    log_file = sys.argv[1]

    enriched_logs = parse_log(log_file)
    output_file = "output_logs.json"

    # Output parsed logs into JSON file
    with open(output_file, 'w') as f:
        json.dump(enriched_logs, f, indent=4)

