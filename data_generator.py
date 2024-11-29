import random
from datetime import datetime, timedelta

# Function to generate simulated web server log data
def generate_log_data(file_path, num_records):
    """
    Generates a log file with simulated web server log data.
    """
    ips = ["192.168.1.1", "203.0.113.5", "172.16.0.3", "10.0.0.8"]
    urls = ["/home", "/about", "/products", "/contact", "/faq"]
    status_codes = [200, 404, 500, 301]
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
        "Mozilla/5.0 (Linux; Android 10)",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)"
    ]

    with open(file_path, "w") as file:
        for _ in range(num_records):
            ip = random.choice(ips)
            url = random.choice(urls)
            status = random.choice(status_codes)
            user_agent = random.choice(user_agents)
            timestamp = (datetime.now() - timedelta(seconds=random.randint(0, 86400))).strftime("%Y-%m-%d %H:%M:%S")
            # Write a line to the log file
            file.write(f"{ip} {timestamp} {url} {status} {user_agent}\n")