import argparse

# Set the argument parser and parse argument
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--file", required=True, help="path to input file")
args = vars(ap.parse_args())
# get input file path
file_path = args["file"]

