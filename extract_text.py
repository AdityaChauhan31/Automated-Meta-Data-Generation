
import os
import pytesseract
from pdf2image import convert_from_path
import fitz  
import docx
from PIL import Image

def extract_text_from_txt(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        return f.read()

def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_text_from_pdf(file_path, ocr_threshold=50):
    text = ""
    doc = fitz.open(file_path)
    for page in doc:
        text += page.get_text()
    doc.close()

    # If text length is too small, assume scanned PDF → apply OCR
    if len(text.strip()) < ocr_threshold:
        print(f"Performing OCR on scanned PDF: {os.path.basename(file_path)}")
        return ocr_pdf(file_path)
    else:
        return text

def ocr_pdf(file_path):
    images = convert_from_path(file_path)
    text = ""
    for img in images:
        text += pytesseract.image_to_string(img)
    return text

def extract_text(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext == '.txt':
        return extract_text_from_txt(file_path)
    elif ext == '.docx':
        return extract_text_from_docx(file_path)
    elif ext == '.pdf':
        return extract_text_from_pdf(file_path)
    else:
        raise ValueError(f"Unsupported file format: {ext}")
