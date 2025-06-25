import streamlit as st
import json
import tempfile
import os

# Import your modules
from extract_text import extract_text
from preprocess import preprocess_text
from generate_metadata import generate_metadata
from models import kw_model, nlp, summarizer, classifier

# --- App Title ---
st.set_page_config(page_title="Document Metadata Extractor", layout="wide")
st.title("📄 Automated Metadata Generator")
st.markdown("Upload a `.pdf`, `.docx`, or `.txt` file and generate structured metadata.")

# --- File Upload ---
uploaded_file = st.file_uploader("Upload your file", type=["pdf", "docx", "txt"])

# --- Label Categories for Classification ---
labels = ["Technology", "Healthcare", "Finance", "Education", "Personal", "Travel", "Sports", "Politics"]
# --- Main Processing ---
if uploaded_file is not None:

    file_suffix = os.path.splitext(uploaded_file.name)[1]
    with tempfile.NamedTemporaryFile(delete=False, suffix=file_suffix) as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        tmp_path = tmp_file.name


    st.info("⏳ Processing file...")

    try:
        # Extract text
        extracted_text = extract_text(tmp_path)

        # Preprocess text
        preprocessed_text = preprocess_text(extracted_text)

        # Generate Metadata
        metadata = generate_metadata(
            file_name=uploaded_file.name,
            text=preprocessed_text,
            keyword_model=kw_model,
            ner_model=nlp,
            summarizer=summarizer,
            classifier=classifier,
            labels=labels
        )

        # Display Metadata
        st.success("✅ Metadata Generated!")
        st.subheader("📋 Summary")
        st.write(metadata["summary"])

        st.subheader("🏷️ Keywords")
        st.write(", ".join(metadata["keywords"]))

        st.subheader("🧠 Named Entities")
        st.json(metadata["entities"])

        st.subheader("📚 Category")
        st.write(metadata["category"])

        st.subheader("📏 Text Length")
        st.write(f"{metadata['text_length']} words")

        st.subheader("📦 Full Metadata (JSON)")
        st.json(metadata)

        #Allow Download
        json_metadata = json.dumps(metadata, indent=2)
        st.download_button("⬇️ Download Metadata as JSON", data=json_metadata, file_name="metadata.json", mime="application/json")

    except Exception as e:
        st.error(f"❌ An error occurred: {e}")
    finally:
        os.remove(tmp_path)
