from extract_text import extract_text
from preprocess import preprocess_text
from generate_metadata import generate_metadata
from models import kw_model, nlp, summarizer, classifier

import json

# Example file
file_name = '/content/drive/MyDrive/Credit_Card_Behaviour_Score_Prediction_Project/Credit_Default_project_23124001.pdf'

#Extract text from file
extracted_text = extract_text(file_name)

#Preprocess the text
preprocessed_text = preprocess_text(extracted_text)

#Define label categories for classification
labels = ["Technology", "Healthcare", "Finance", "Education", "Personal", "Travel", "Sports", "Politics"]
#Generate metadata
metadata = generate_metadata(
    file_name=file_name,
    text=preprocessed_text,
    keyword_model=kw_model,
    ner_model=nlp,
    summarizer=summarizer,
    classifier=classifier,
    labels=labels
)

#Display metadata
print(json.dumps(metadata, indent=2))
