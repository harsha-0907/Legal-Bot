# First, install necessary packages
import os
from transformers import DistilBertTokenizer, DistilBertModel
import torch
import faiss
import numpy as np

# 1. Load the DistilBERT Model and Tokenizer
def load_model_and_tokenizer(model_name="distilbert-base-uncased"):
    tokenizer = DistilBertTokenizer.from_pretrained(model_name)
    model = DistilBertModel.from_pretrained(model_name)
    return model, tokenizer

model, tokenizer = load_model_and_tokenizer()
print("DistilBERT model and tokenizer loaded successfully.")

# 2. Prepare FAISS Index
def create_faiss_index(dim):
    # Create a FAISS index for vector search
    index = faiss.IndexFlatL2(dim)
    return index

# Dimensionality of DistilBERT embeddings
dim = 768  # DistilBERT output size

index = create_faiss_index(dim)
print("FAISS index created.")

# 3. Function to Encode Documents into Embeddings
def encode_text(text, tokenizer, model):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    # Use the last hidden state of the model
    embeddings = outputs.last_hidden_state.mean(dim=1)
    return embeddings.numpy()

# 4. Function to Add Documents to FAISS Index
def add_documents_to_faiss(documents, index, tokenizer, model):
    for doc in documents:
        embedding = encode_text(doc, tokenizer, model)
        faiss.normalize_L2(embedding)  # Normalize embeddings
        index.add(embedding)
    print(f"Added {len(documents)} documents to the FAISS index.")

# 5. Search Function in FAISS
def search_faiss(query, index, tokenizer, model, k=5):
    query_embedding = encode_text(query, tokenizer, model)
    faiss.normalize_L2(query_embedding)  # Normalize query
    D, I = index.search(query_embedding, k)  # Perform the search
    return D, I

# 6. Example: Load 100 documents, add to FAISS, and perform a search
directory_path = "/content/drive/MyDrive/dataset"
files = os.listdir(directory_path)
documents = []
for file in files:
    with open(os.path.join(directory_path,file), 'r') as file1:
        text = file1.read()
        documents.append(text)

# Add documents to FAISS
add_documents_to_faiss(documents, index, tokenizer, model)

def save_faiss_index(index, index_file_path):
    faiss.write_index(index, index_file_path)
    print(f"FAISS index saved to {index_file_path}")

# Example of saving the index
index_file_path = "faiss_index.index"
save_faiss_index(index, index_file_path)

# Perform a search on FAISS
query = "Intellectual property laws"
distances, indices = search_faiss(query, index, tokenizer, model, k=5)

print("Search results:")
for i, idx in enumerate(indices[0]):
    print(f"{i+1}. Document : {documents[idx]}")
