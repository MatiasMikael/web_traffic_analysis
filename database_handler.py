import sqlite3

# Function to create the database and table schema
def create_database():
    """
    Creates a SQLite database and defines the schema for web traffic logs.
    """
    conn = sqlite3.connect("web_traffic.db")
    cursor = conn.cursor()

    # Create table if it doesn't already exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS web_traffic_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ip_address TEXT,
            timestamp TEXT,
            url TEXT,
            status_code INTEGER,
            user_agent TEXT
        )
    """)
    conn.commit()
    conn.close()

# Function to validate log lines
def validate_log_line(line):
    """
    Validates a single log line for proper structure.
    """
    try:
        parts = line.strip().split(" ", 4)
        if len(parts) != 5 or not parts[3].isdigit():
            return False
        return True
    except:
        return False

# Function to load log data into the database
def load_data_to_db(log_file):
    """
    Reads a log file and inserts the parsed data into the database.
    """
    conn = sqlite3.connect("web_traffic.db")
    cursor = conn.cursor()

    with open(log_file, "r") as file:
        for line in file:
            try:
                # Split the line into parts
                parts = line.strip().split(" ", 4)  # Split into 5 parts
                ip_address = parts[0]
                timestamp = parts[1] + " " + parts[2]
                url = parts[3]

                # Further split parts[4] into status_code and user_agent
                remaining = parts[4].split(" ", 1)
                status_code = int(remaining[0])  # Status code is the first part
                user_agent = remaining[1]       # User-Agent is the second part

                # Insert the data into the database
                cursor.execute("""
                    INSERT INTO web_traffic_logs (ip_address, timestamp, url, status_code, user_agent)
                    VALUES (?, ?, ?, ?, ?)
                """, (ip_address, timestamp, url, status_code, user_agent))
                print(f"Inserted: {ip_address}, {timestamp}, {url}, {status_code}, {user_agent}")
            except Exception as e:
                print(f"Error processing line: {line.strip()}")
                print(f"Error: {e}")

    conn.commit()
    conn.close()
    print(f"Data successfully loaded into the database from {log_file}")