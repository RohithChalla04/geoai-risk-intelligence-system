from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = [
    "High rainfall increases infrastructure failure risk.",
    "Heavy traffic leads to road wear and accidents.",
    "Distance from highways reduces risk exposure."
]

embeddings = model.encode(documents)

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))

def search(query):
    q_embed = model.encode([query])
    D, I = index.search(np.array(q_embed), k=2)
    return [documents[i] for i in I[0]]
