def generate_metadata(file_name, text, keyword_model,ner_model, summarizer, classifier, labels):
    from keybert import KeyBERT
    import spacy

    #Keyword Extraction
    keywords = keyword_model.extract_keywords(
        text,
        keyphrase_ngram_range=(1, 3),
        stop_words='english',
        use_maxsum=True,
        nr_candidates=25,
        top_n=15
    )
    keywords_list = [kw[0] for kw in keywords]

    #Named Entity Recognition (spaCy)
    doc = ner_model(text)
    entities = {}
    for ent in doc.ents:
        entities.setdefault(ent.label_, set()).add(ent.text)
    # Convert sets to lists
    entities = {label: list(values) for label, values in entities.items()}

    #Summarization
    
    summary_result = summarizer(text[:1024], max_length=200, min_length=30, do_sample=False)
    summary = summary_result[0]['summary_text']
    #Zero-shot Classification
    classification = classifier(text, labels)
    top_label = classification['labels'][0]

    #Combine into JSON
    metadata = {
        "filename": file_name,
        "summary": summary,
        "keywords": keywords_list,
        "entities": entities,
        "category": top_label,
        "text_length": len(text)
    }

    return metadata
