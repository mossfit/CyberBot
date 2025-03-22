import faiss
import numpy as np
import os
import pickle
from config import FAISS_INDEX_FILE

class VectorDB:
    def __init__(self, embedding_dim):
        self.embedding_dim = embedding_dim
        self.index = faiss.IndexFlatL2(embedding_dim)
        self.metadata = []  # To store associated metadata for each embedding

    def add(self, embeddings, metadata):
        """
        embeddings: numpy array (n_samples, embedding_dim)
        metadata: list of dictionaries
        """
        self.index.add(np.array(embeddings, dtype=np.float32))
        self.metadata.extend(metadata)

    def search(self, query_embedding, top_k=5):
        query_embedding = np.array(query_embedding, dtype=np.float32).reshape(1, -1)
        distances, indices = self.index.search(query_embedding, top_k)
        results = []
        for idx, dist in zip(indices[0], distances[0]):
            if idx < len(self.metadata):
                result = self.metadata[idx].copy()
                result['distance'] = dist
                results.append(result)
        return results

    def save(self, filename=FAISS_INDEX_FILE):
        faiss.write_index(self.index, filename)
        with open(filename + ".meta", "wb") as f:
            pickle.dump(self.metadata, f)

    def load(self, filename=FAISS_INDEX_FILE):
        if os.path.exists(filename):
            self.index = faiss.read_index(filename)
            with open(filename + ".meta", "rb") as f:
                self.metadata = pickle.load(f)

if __name__ == "__main__":
    from processor import generate_embeddings
    texts = ["vulnerability in system", "new threat detected"]
    embeddings = generate_embeddings(texts)
    metadata = [
        {"title": "Entry 1", "description": texts[0]},
        {"title": "Entry 2", "description": texts[1]}
    ]
    db = VectorDB(embeddings.shape[1])
    db.add(embeddings, metadata)
    results = db.search(embeddings[0], top_k=2)
    print("Search Results:", results)
