from data_generator import generate_log_data
from database_handler import create_database, load_data_to_db
from data_analysis import analyze_data
from visualization import visualize_data
import sqlite3
import pandas as pd

# File path for the generated log file
log_file = "webserver.log"

# Function to check the database content
def check_database():
    """
    Verifies the database content by checking the total number of rows
    and printing the first few entries.
    """
    conn = sqlite3.connect("web_traffic.db")
    cursor = conn.cursor()

    # Check total number of rows
    cursor.execute("SELECT COUNT(*) FROM web_traffic_logs;")
    total_rows = cursor.fetchone()[0]
    print(f"Total rows in the database: {total_rows}")

    # Print the first 5 rows from the table
    cursor.execute("SELECT * FROM web_traffic_logs LIMIT 5;")
    rows = cursor.fetchall()
    if rows:
        print("Sample rows from the database:")
        for row in rows:
            print(row)
    else:
        print("No data found in the database.")

    # Check distinct dates to validate timestamps
    cursor.execute("SELECT DISTINCT DATE(timestamp) as date FROM web_traffic_logs;")
    dates = cursor.fetchall()
    if dates:
        print("Distinct dates in the database:")
        for date in dates:
            print(date[0])
    else:
        print("No valid dates found in the database.")

    conn.close()

# Function to debug daily traffic data
def debug_daily_traffic():
    """
    Debugs the daily traffic data by printing query results before visualization.
    """
    conn = sqlite3.connect("web_traffic.db")
    daily_traffic = pd.read_sql_query("""
        SELECT DATE(timestamp) as date, COUNT(*) as visits
        FROM web_traffic_logs
        GROUP BY date
        ORDER BY date
    """, conn)

    print("Daily traffic data for visualization:")
    print(daily_traffic)

    conn.close()

# Main function to execute the workflow
if __name__ == "__main__":
    # Step 1: Generate log data
    generate_log_data(log_file, 1000)
    print("Log data generated.")

    # Step 2: Create database and load data
    create_database()
    load_data_to_db(log_file)
    print("Data loaded into the database.")

    # Step 3: Check database content
    check_database()

    # Step 4: Debug daily traffic data
    debug_daily_traffic()

    # Step 5: Analyze data
    analyze_data()

    # Step 6: Visualize data
    visualize_data()