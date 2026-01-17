import csv

input_file = "data/requests.csv"
output_file = "data/processed_requests.csv"

processed_requests = [] 

with open(input_file, newline="") as file:
  reader = csv.DictReader(file)

for row in reader:
        if row["request_type"] == "Standard":
            row["status"] = "APPROVED"
        else:
            row["status"] = "REJECTED"
        
        processed_requests.append(row)

with open(output_file, "w", newline="") as file:
    fieldnames = ["request_id", "requester_name", "request_type", "status"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(processed_requests)

print("Workflow processing complete.")
