# NGINX Access Log Parser

This is a Python script that transforms Nginx access logs into JSON format enriched with 
additional User Agent information.

## Features
- Parses standard Nginx access logs in the default combined format
- Extracts browser, OS and device information from User-Agent
- Outputs enriched parsed data into a JSON file

## Requirements
- Python 3.8+
- Dependencies listed in requirements.txt

## Installation
1. **Clone the repository**
```
git clone https://github.com/harithh07/govtechassessment
cd govtechassessment
```
2. **Install dependencies**
```
pip install -r requirements.txt
```
3. **Usage**
```
python3 logparser.py <nginx_access_log_file>
```
Example: 
```
python3 logparser.py sample_input
```
This creates an output file `output_logs.json`.

4. **Expected input format**  
This script expects Nginx logs in the default combined format, e.g.:
```
127.0.0.1 - - [13/Aug/2025:11:22:41 +0800] "GET /aboutus.html HTTP/1.1" 200 6430 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"
```

5. **Expected output**  
The output will be in JSON format, e.g.:
```
[
    {
        "ip": "127.0.0.1",
        "time": "13/Aug/2025:11:22:41 +0800",
        "method": "GET",
        "url": "/aboutus.html",
        "protocol": "HTTP/1.1",
        "status": "200",
        "size": "6430",
        "referrer": "-",
        "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15",
        "browser": "Safari",
        "os": "Mac OS X",
        "device": "Mac"
    }
]
```
6. **Assumptions**
- The input Nginx access logs are in the default combined format
- If device family is unknown, the `device` field will be set to "Unknown"