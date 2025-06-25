# 📄 Automated Metadata Generation System
## Overview
This project is an **Automated Metadata Generation System** designed to enhance the discoverability, classification, and semantic understanding of unstructured documents like PDFs, DOCX, and TXT files. By leveraging powerful NLP models, it extracts rich metadata that is consistent, scalable, and meaningful — all through a user-friendly web interface built with **Streamlit**.

---

## Objective

The system aims to:

- Automatically generate structured metadata for documents.
- Support various file formats including scanned PDFs (via OCR).
- Identify key concepts, entities, summaries, and categories.
- Provide a downloadable metadata JSON.
- Offer a smooth user experience via a web UI.

---

## Functioning Pipeline

The core pipeline consists of the following steps:

1. **File Upload**  
   Accept `.pdf`, `.docx`, or `.txt` files via a Streamlit interface. It also support OCR.

2. **Content Extraction**  
   - Plain text from TXT and DOCX files.
   - PDF text using PyMuPDF.
   - OCR support for scanned PDFs using `pytesseract` and `pdf2image`.

3. **Preprocessing**  
   Clean text by:
   - Removing non-ASCII characters.
   - Fixing encoding issues.
   - Stripping unwanted characters and normalizing whitespace.

4. **Keyword Extraction**  
   Using **KeyBERT** with a custom SentenceTransformer to identify relevant phrases.

5. **Named Entity Recognition (NER)**  
   Using **spaCy’s transformer pipeline** (`en_core_web_trf`) to extract names of people, organizations, locations, dates, etc.

6. **Summarization**  
   Generating concise summaries with **BART-large-CNN** from Hugging Face Transformers.

7. **Document Classification**  
   Classify document topics using **DeBERTa v3 (MoritzLaurer/deberta-v3-large-zeroshot-v2.0)** via zero-shot classification.

8. **Metadata Structuring**  
   Combine all outputs into a structured JSON metadata format.

9. **User Interface**  
    Display results and allow download via a **Streamlit web app**.

---

## 🤖 Models Used

| Purpose                  | Model Used                                                   |
|--------------------------|--------------------------------------------------------------|
| **Keyword Extraction**   | `KeyBERT` + `SentenceTransformer('paraphrase-MiniLM-L6-v2')` |
| **NER**                  | `spaCy` with `en_core_web_trf`                               |
| **Summarization**        | `facebook/bart-large-cnn`                                    |
| **Classification**       | `MoritzLaurer/deberta-v3-large-zeroshot-v2.0`               |

All models are loaded with GPU support when available using:
```python
device = "cuda" if torch.cuda.is_available() else "cpu"

