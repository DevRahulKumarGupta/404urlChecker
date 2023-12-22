import requests
import csv

def check_url(url):
    try:
        response = requests.get(url)
        # Check if the status code is 404
        if response.status_code == 404:
            return 'Not Found'
        else:
            return 'OK'
    except requests.exceptions.RequestException as e:
        print(e)
        return 'Recheck'

def add_statuses_to_csv(input_file):
    # Read the CSV file and get URLs from the first column
    with open(input_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        rows = list(csv_reader)

    # Add a header for the status column
      # Assuming the first row contains headers

    # Add statuses to each row
    for row in rows[1:]:
        url = row[0]
        status = check_url(url)
        row.append(status)
        print(status)

    # Write the modified rows back to the same CSV file
    with open(input_file, 'w', newline='') as csv_output:
        csv_writer = csv.writer(csv_output)
        csv_writer.writerows(rows)

# Example usage:
input_csv_file = str(input("Enter your CSV file name with .csv: "))
add_statuses_to_csv(input_csv_file)
