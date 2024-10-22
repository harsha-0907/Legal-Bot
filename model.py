import os
from transformers import DistilBertTokenizer, DistilBertModel
import torch
import faiss
import numpy as np

def load_model_and_tokenizer(model_name="distilbert-base-uncased"):
    tokenizer = DistilBertTokenizer.from_pretrained(model_name)
    model = DistilBertModel.from_pretrained(model_name)
    return model, tokenizer

def encode_text(text, tokenizer, model):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    embeddings = outputs.last_hidden_state.mean(dim=1)
    return embeddings.numpy()

def add_documents_to_faiss(documents, index, tokenizer, model):
    for doc in documents:
        embedding = encode_text(doc, tokenizer, model)
        faiss.normalize_L2(embedding)  # Normalize embeddings
        index.add(embedding.reshape(1, -1))

def create_faiss_index(dim):
    # Create a FAISS index for vector search
    index = faiss.IndexFlatL2(dim)
    return index

def save_faiss_index(index, index_file_path):
    faiss.write_index(index, index_file_path)
    print(f"FAISS index saved to {index_file_path}")


model, tokenizer = load_model_and_tokenizer()
dim = 768  # DistilBERT output size
index = create_faiss_index(dim)


directory_path = "/home/user/web/summarized-dataset"
files = os.listdir(directory_path)
documents = []
for file in files:
    with open(os.path.join(directory_path,file), 'r') as file1:
        text = file1.read()
        documents.append(text)

add_documents_to_faiss(documents, index, tokenizer, model)
index_file_path = "faiss_index.index"
save_faiss_index(index, index_file_path)
def search(query, k=5):
    global index, tokenizer, model, documents
    query_embedding = encode_text(query, tokenizer, model)
    faiss.normalize_L2(query_embedding)  # Normalize query
    D, Index = index.search(query_embedding.reshape(1, -1), k)
    search_results = []
    for i, idx in enumerate(Index[0]):
        search_results.append(documents[idx])
    return search_results
