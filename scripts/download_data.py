import requests

# URL to the dataset
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv"

# Path to save the file
data_path = "C:/Users/oscar/OneDrive/Escritorio/Python_Projects/automobile_sales_visualizations/data/historical_automobile_sales.csv"

# Send a GET request to download the file
response = requests.get(url)

# Write the content to the file
with open(data_path, "wb") as file:
    file.write(response.content)

print(f"Data downloaded and saved to {data_path}")
