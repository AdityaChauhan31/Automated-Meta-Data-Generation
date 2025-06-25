from keybert import KeyBERT
from sentence_transformers import SentenceTransformer
import spacy
from transformers import pipeline
import torch
device = "cuda" if torch.cuda.is_available() else "cpu"

# KeyBERT with custom model
custom_model = SentenceTransformer('paraphrase-MiniLM-L6-v2', device=device)
kw_model = KeyBERT(model=custom_model)

# spaCy (spaCy manages its own device if using transformer backend)
nlp = spacy.load("en_core_web_trf")

# Summarizer and Classifier with device param
summarizer = pipeline("summarization", model="facebook/bart-large-cnn", device=0 if device == "cuda" else -1)
classifier = pipeline("zero-shot-classification", model="MoritzLaurer/deberta-v3-large-zeroshot-v2.0", device=0 if device == "cuda" else -1)
