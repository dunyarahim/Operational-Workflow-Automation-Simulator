import csv

input_file = "data/requests.csv"
output_file = "data/processed_requests.csv"

processed_requests = [] 

with open(input_file, newline="") as file:
  reader = csv.DictReader(file)
