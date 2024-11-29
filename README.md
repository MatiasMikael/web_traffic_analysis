# Web Traffic Analysis Project
This project simulates, analyzes, and visualizes web traffic data using Python. It includes features such as generating mock log data, storing it in a database, analyzing it for trends, and visualizing the results.

# Overview
This project performs the following tasks:
* Generates simulated web server log data.
* Creates a database schema to store log data.
* Loads data into a database for analysis.
* Analyzes popular pages, traffic trends, and error code distributions.
* Visualizes daily traffic trends and error code distributions.

# Screenshots
* Daily Traffic Trend: This graph visualizes how website traffic fluctuates over time, showing peaks and troughs during specific days. It helps identify when the website experiences higher traffic volumes, which can be useful for performance optimization and capacity planning.
* Error Code Distribution: This chart displays the frequency of different HTTP error codes (such as 404 and 500). It helps identify common errors that users encounter, which can assist in debugging and improving the user experience.

# How to Run
* Prerequisites
* Python 3.x must be installed on your system.
* Install the required libraries using pip:
```
pip install -r requirements.txt
```

# Steps
* Clone the repository.
```
git clone https://github.com/yourusername/web_traffic_analysis.git
cd web_traffic_analysis
```
* Run the application.
```
python app.py
```
* The results will be printed to the console, and visualizations will be displayed as plots.

# Dependencies
The following Python libraries are required (listed in requirements.txt):
* pandas
* matplotlib
* sqlite3

# License
This project is licensed under the MIT License.
