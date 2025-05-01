from PIL import Image
import torch
import clip
import os

model, preprocess = clip.load("ViT-B/32")
dataset_path = "sample_catalog/images/"

catalog_embeddings = []
catalog_files = []

def prepare_catalog():
    global catalog_embeddings, catalog_files
    for img_name in os.listdir(dataset_path):
        image = preprocess(Image.open(os.path.join(dataset_path, img_name))).unsqueeze(0)
        with torch.no_grad():
            embedding = model.encode_image(image)
        catalog_embeddings.append(embedding)
        catalog_files.append(img_name)

prepare_catalog()

def find_similar_products(file):
    image = preprocess(Image.open(file.file)).unsqueeze(0)
    with torch.no_grad():
        query_embedding = model.encode_image(image)
    
    similarities = [torch.cosine_similarity(query_embedding, emb).item() for emb in catalog_embeddings]
    top_indices = sorted(range(len(similarities)), key=lambda i: similarities[i], reverse=True)[:5]
    return [catalog_files[i] for i in top_indices]