import csv
from io import StringIO


def extract_emails_from_csv(csv_data, field='Email'):
    emails = []

    # Use StringIO to create a file-like object from the string
    csv_file = StringIO(csv_data)

    reader = csv.DictReader(csv_file)

    for row in reader:
        # Check if 'email' column is present and not empty
        if field in row and row[field]:
            emails.append(row[field])

    return ';'.join(emails)


# Replace 'your_csv_data_here' with the actual CSV data as a string
csv_data = """
"""

formatted_emails = extract_emails_from_csv(csv_data)

print(formatted_emails)
