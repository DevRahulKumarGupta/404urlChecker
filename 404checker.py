import requests
import csv
from concurrent.futures import ThreadPoolExecutor

def check_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 404:
            return 'Not Found'
        else:
            return 'OK'
    except requests.exceptions.RequestException as e:
        print(e)
        return 'Recheck'

def add_statuses_to_csv(input_file):
    with open(input_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        rows = list(csv_reader)

    header = rows[0]  # Save the header
    header.append('Status')  # Add a header for the status column

    with ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(check_url, (row[0] for row in rows[1:])))

    for i, status in enumerate(results):
        rows[i + 1].append(status)
        print(status)

    with open(input_file, 'w', newline='') as csv_output:
        csv_writer = csv.writer(csv_output)
        csv_writer.writerows(rows)

# Example usage:
input_csv_file = str(input("Enter your CSV file name with .csv: "))
add_statuses_to_csv(input_csv_file)
