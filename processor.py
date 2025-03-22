from sentence_transformers import SentenceTransformer
import numpy as np
from config import EMBEDDING_MODEL

# Load the embedding model
model = SentenceTransformer(EMBEDDING_MODEL)

def generate_embeddings(texts):
    embeddings = model.encode(texts, show_progress_bar=True)
    return np.array(embeddings)

def process_data(data):
    """
    Processes a list of data entries (each with 'title' and 'description') and attaches embeddings.
    """
    texts = [entry['description'] for entry in data]
    embeddings = generate_embeddings(texts)
    for i, entry in enumerate(data):
        entry['embedding'] = embeddings[i]
    return data

if __name__ == "__main__":
    sample_data = [
        {"title": "CVE-XXXX", "description": "Sample vulnerability description."},
        {"title": "Security Report", "description": "New threat detected in XYZ."}
    ]
    processed = process_data(sample_data)
    print("Processed Data:", processed)
