# imports
import argparse
import pandas as pd
import requests

# Set the argument parser and parse argument
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--file", required=True, help="path to input file", default="resources/netflix_titles.csv")
ap.add_argument("-e", "--endpoint", required=True, help="endpoint url", default="https://my-project-1487175171975.ew.r.appspot.com/titles")
args = vars(ap.parse_args())
# get input file path
file_path = args["file"]
# get endpoint url
endpoint = args["endpoint"]


def post_data(data):
    """Posts data to the endpoint"""
    response = requests.post(endpoint, json=data)
    print(response.status_code)


def read_file():
    """Reads the file and sends every chunk to the specified endpoint"""
    # Operate on chunks of 1000 entries to not overload memory.
    for chunk in pd.read_csv(file_path, chunksize=500):
        result = chunk.to_json(orient="records")
        post_data(result)


read_file()