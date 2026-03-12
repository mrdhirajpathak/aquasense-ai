import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Load knowledge base
with open("data/water_docs.txt", "r", encoding="utf-8") as f:
    docs = f.read().split("\n")

doc_embeddings = model.encode(docs)

dimension = doc_embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(np.array(doc_embeddings))


def retrieve_context(query, k=3):

    query_embedding = model.encode([query])

    distances, indices = index.search(np.array(query_embedding), k)

    results = []

    for i in indices[0]:
        results.append(docs[i])

    return "\n".join(results)