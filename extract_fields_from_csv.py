import csv
from io import StringIO


def extract_selected_columns(csv_data):
    selected_data = []

    # Use StringIO to create a file-like object from the string
    csv_file = StringIO(csv_data)

    reader = csv.DictReader(csv_file)

    for row in reader:
        selected_row = {
            'Name': row.get('Name', ''),
            'Email': row.get('Email', ''),
            'Created Date': row.get('Created Date (+00:00 UTC)', '')
        }
        selected_data.append(selected_row)

    return selected_data


# Replace 'your_csv_data_here' with the actual CSV data as a string
csv_data = """
Reference,Name,Email,Created Date (+00:00 UTC),Completed Date (+00:00 UTC),Unique URL,Total Due (EUR),Total Paid (EUR),IP,VAT Number,Receipt Number,Payment Reference,Paid With,Discount Code,Refund Status,Refund Description,Total Refunded (EUR),Tickets Voided,Source,Source Type,KubeTrain Amsterdam-Paris Quantity,test ticket Quantity

"""

selected_data = extract_selected_columns(csv_data)

# Output the selected data in CSV format
output_csv = StringIO()
fieldnames = ['Name', 'Email', 'Created Date']

writer = csv.DictWriter(output_csv, fieldnames=fieldnames, delimiter=',')
writer.writerows(selected_data)

print(output_csv.getvalue())
