# %%

import requests
import pandas as pd
import datetime
import json
import time

# %%

# Fetch a specific endpoint from the API
def get_response(**kwargs):
    url = "https://www.tabnews.com.br/api/v1/contents"
    resp = requests.get(url, params=kwargs) # make GET request to the URL with parameters
    return resp

# Save data in two different formats in their respective folders (json and parquet)
def save_data(data, option='json'):
    now = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S.%f") # filename with hours, minutes, seconds, and milliseconds
    
    if option == 'json':
        with open (f"json/{now}.json", 'w') as open_file:
            json.dump(data, open_file, indent=4)
    
    elif option == 'parquet':
        df = pd.DataFrame(data)
        df.to_parquet(f"parquet/{now}.parquet", index=False)
    
# %%

page = 1 # start on page 1 to fetch the most recent data
date_stop = pd.to_datetime('2024-08-01') # set a limit date for data fetch
while True:
    print(page)
    resp = get_response(page=page, per_page=100, strategy="new")
    if resp.status_code == 200: # check if the request was successful
        data = resp.json()
        save_data(data)
        
        date = pd.to_datetime(data[-1]["update_at"]).date() # get the date of the last fetched data
        if len(data) > 100 or date < date_stop: # check if the length of data is more than 100 or date is earlier than date_stop
            break
        
        page += 1
        time.sleep(5) # pause for 5 seconds before making the next request
        
    else:
        print(resp.status_code)
        print(resp.json())
        time.sleep(60 * 15) # pause for 15 minutes before retrying
        

        



