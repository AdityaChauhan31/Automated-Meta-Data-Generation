import re
import string
from unidecode import unidecode

def preprocess_text(text):
    # Convert to ASCII to fix weird encodings (e.g., \u2013)
    text = unidecode(text)
    
    # Remove non-printable characters
    text = ''.join(c for c in text if c.isprintable())

    # Remove unwanted characters (optional: keep punctuation if needed)
    text = re.sub(r'[^A-Za-z0-9\s.,:;!?()\[\]\']+', ' ', text)

    # Replace multiple whitespace with single space
    text = re.sub(r'\s+', ' ', text)

    # Strip leading/trailing whitespace
    text = text.strip()

    return text

