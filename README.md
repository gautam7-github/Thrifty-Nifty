# Thrifty-Nifty

API to fetch Nifty Indices Data.

# Google Sheet to Flask API.

# Supports
- Nifty 50
- Nifty IT
- Nifty Bank
- Nifty Auto
- Nifty Pharma
- Nifty Div Opps 50 (in dev..)
- Nifty FMCG (in dev..)

# Command Format
```
/API_KEY/data/nifty/<index>/all/sort/<sortby>
```
# API Response Format
```
{
  "ABCD": {
    "COMPANY": "ABCD ...", 
    "CMP": xxxx, 
    "52WH": xxxx, 
    "52WL": xxxx, 
    "OPEN": xxxx, 
    "YESTCLOSE": xxxx, 
    "CHANGE": xxxx, 
    "CHANGEPCT": xxxx, 
    "DAYHIGH": xxxx, 
    "DAYLOW": xxxx, 
    "MKTCAP": xxxx, 
    "EPS": xxxx, 
    "TICKER": "ABCD"
  }, 
  ...
}
```
- Leveraging Google Finance Function of Google Sheets to collect the financial data.
- Using Python's Extraordinary CSV Processing Capabilities to Read data from the deployed google sheet.

# It turns Data in google sheet to a Flask API.

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
