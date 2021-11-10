# Thrifty-Nifty

API to fetch Nifty 50 Data.

# Google Sheet to Flask API.

# Supports
- Nifty 50
- Nifty IT
- Nifty Bank
- Nifty Auto
- Nifty Pharma

# API Format
{
  "AMARAJABAT": {
    "COMPANY": "Amara Raja Batteries Limited", 
    "CMP": 706.0, 
    "52WH": 1025.55, 
    "52WL": 665.0, 
    "OPEN": 707.05, 
    "YESTCLOSE": 707.05, 
    "CHANGE": -1.06, 
    "CHANGEPCT": -0.15, 
    "DAYHIGH": 714.0, 
    "DAYLOW": 704.05, 
    "MKTCAP": 120781460639, 
    "EPS": 41.47, 
    "TICKER": "AMARAJABAT"
  }, 
  ...
}
# Leveraging Google Finance Function of Google Sheets to collect the financial data.
# Using Python's Extraordinary CSV Processing Capabilities to Read data from the deployed google sheet.
# Data read is converted into json and supplied using Flask.

# Basically it turns data in google sheet to a flask api.

# Tech Stack
- Python
- Flask
- Ngrok
- Pandas
- Requests
- JSON
- Google Sheets

# There is delay of upto 20 mins in prices.
# Data is only for informational purposes and not to be used for investment purposes


## Google sheet link

-   https://docs.google.com/spreadsheets/d/1FaSibXFWRJ8bFoOIEy4vaoxG7z-S8nUhT6U9f4quvaU/edit?usp=sharing

# Project Idea

-   I used to track my equity portfolio using google sheets, then used that sheet to make a ETF Performance Tracking and Comparison-to-Benchmark sheet.
-   Eventually, it turned into Thrifty-Nifty.
