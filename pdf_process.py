import fitz  # PyMuPDF

def get_text_from_resume(file_path):
    resume_content = []
    document = fitz.open(file_path)
    
    for pg in document:
        resume_content.append(pg.get_text())
    
    document.close()
    return ''.join(resume_content)
