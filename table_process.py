import camelot

def get_pdf_tables(file_path):
    extracted_tables = camelot.read_pdf(file_path, pages='all')
    
    for index, tbl in enumerate(extracted_tables):
        output_filename = f"table_{index}.csv"
        tbl.to_csv(output_filename)
    
    return extracted_tables
