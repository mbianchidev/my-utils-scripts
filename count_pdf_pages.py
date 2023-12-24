import os
import PyPDF2
import argparse

def count_pdf_pages(pdf_path):
    try:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            return len(pdf_reader.pages)
    except Exception as e:
        print(f"Error reading {pdf_path}: {str(e)}")
        return 0

def count_pages_in_folder(folder_path):
    total_pages = 0

    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith('.pdf'):
                pdf_path = os.path.join(root, file)
                total_pages += count_pdf_pages(pdf_path)

    return total_pages

def main():
    parser = argparse.ArgumentParser(description="Count the pages of PDFs in a folder.")
    parser.add_argument("folder_path", type=str, help="Path to the folder containing PDF files.")
    args = parser.parse_args()

    folder_path = args.folder_path
    total_pages = count_pages_in_folder(folder_path)
    print(f"Total pages in {folder_path}: {total_pages}")

if __name__ == "__main__":
    main()
