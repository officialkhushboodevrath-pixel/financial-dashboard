# Tech Mahindra Financial Dashboard

## About the Project
This project is based on the financial analysis of Tech Mahindra using quarterly financial data collected from Screener.in. The aim of this project is to clean the data, perform statistical analysis, build machine learning models, and create an interactive dashboard using Streamlit.

## Tools and Technologies Used
- Python
- Google Colab
- Pandas
- Matplotlib
- Scikit-learn
- Streamlit

## Data Collection
The financial data was collected from Screener.in using:
- Quarterly Results
- Profit & Loss statements

The data was converted into CSV format and used for further analysis.

## Data Cleaning and Processing
The following steps were performed:
- Removed unnecessary rows and formatting issues
- Removed commas and percentage symbols from values
- Converted data into numerical format
- Filled missing values
- Created Profit Trend column
- Calculated Sales Growth and Net Profit Growth

## Analysis Performed
Statistical analysis was performed on:
- Sales
- Net Profit
- OPM

The following values were calculated:
- Mean
- Median
- Standard Deviation

## Machine Learning Models
Two models were trained to predict profit trends:

1. Logistic Regression
2. Decision Tree Classifier

The accuracy of both models was compared.

## Dashboard
A Streamlit dashboard was created with:
- Latest Sales, Net Profit, and OPM values
- Sales and Net Profit trend chart
- OPM percentage chart
- Net Profit box plot
- Model comparison table

## Deployment
The dashboard was deployed using Streamlit Community Cloud and is publicly accessible.

## Author
Khushboo Devrath
