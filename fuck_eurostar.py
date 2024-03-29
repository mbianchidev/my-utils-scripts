import os
import fitz  # PyMuPDF


def split_pdf(input_pdf_path, output_dir):
    pdf_document = fitz.open(input_pdf_path)
    for i in range(len(pdf_document)):
        # page = pdf_document.load_page(i)
        # text = page.get_text()
        output_pdf_path = os.path.join(output_dir, f'page_{i+1}.pdf')
        new_pdf = fitz.open()
        new_pdf.insert_pdf(pdf_document, from_page=i, to_page=i)
        new_pdf.save(output_pdf_path)
        new_pdf.close()


# Example usage:
input_pdf_path = '/mnt/c/Users/mbian/Downloads/tickets.pdf'
output_dir = '/mnt/c/Users/mbian/Downloads/tickets'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

split_pdf(input_pdf_path, output_dir)
