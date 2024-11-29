import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Function to visualize data trends and distributions
def visualize_data():
    """
    Generates visualizations for web traffic trends and error distribution.
    """
    conn = sqlite3.connect("web_traffic.db")

    # Query daily traffic data
    daily_traffic = pd.read_sql_query("""
        SELECT DATE(timestamp) as date, COUNT(*) as visits
        FROM web_traffic_logs
        GROUP BY date
        ORDER BY date
    """, conn)

    # Plot traffic trend over time
    plt.figure(figsize=(10, 5))
    plt.plot(daily_traffic['date'], daily_traffic['visits'], marker='o')
    plt.title('Daily Traffic Trend')
    plt.xlabel('Date')
    plt.ylabel('Number of Visits')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Query error code distribution
    error_distribution = pd.read_sql_query("""
        SELECT status_code, COUNT(*) as occurrences
        FROM web_traffic_logs
        WHERE status_code >= 400
        GROUP BY status_code
    """, conn)

    # Plot error code distribution
    plt.figure(figsize=(8, 5))
    plt.bar(error_distribution['status_code'], error_distribution['occurrences'])
    plt.title('Error Code Distribution')
    plt.xlabel('Status Code')
    plt.ylabel('Occurrences')
    plt.show()

    conn.close()