import sqlite3
import pandas as pd

# Function to analyze data from the database
def analyze_data():
    """
    Performs data analysis on web traffic logs stored in the database.
    """
    conn = sqlite3.connect("web_traffic.db")

    # Query to find the most popular URLs
    popular_pages = pd.read_sql_query("""
        SELECT url, COUNT(*) as visits
        FROM web_traffic_logs
        GROUP BY url
        ORDER BY visits DESC
        LIMIT 5
    """, conn)
    print("Most Popular Pages:")
    print(popular_pages)

    # Query to calculate daily traffic
    daily_traffic = pd.read_sql_query("""
        SELECT DATE(timestamp) as date, COUNT(*) as visits
        FROM web_traffic_logs
        GROUP BY date
        ORDER BY date
    """, conn)
    print("\nDaily Traffic:")
    print(daily_traffic)

    # Query to calculate error code distribution
    error_distribution = pd.read_sql_query("""
        SELECT status_code, COUNT(*) as occurrences
        FROM web_traffic_logs
        WHERE status_code >= 400
        GROUP BY status_code
    """, conn)
    print("\nError Code Distribution:")
    print(error_distribution)

    conn.close()