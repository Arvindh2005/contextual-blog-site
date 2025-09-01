from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

app = Flask(__name__)

CORS(app)

API_URL = "http://localhost:3000/api/blog/all"
blogs = []
dimension = 384
index = faiss.IndexFlatL2(dimension)

print("--- Loading Sentence Transformer model... ---")
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
print("--- Model loaded successfully. ---")


def build_faiss(blog_list):
    global index
    print("--- Building FAISS index ---")
    if not blog_list:
        print("⚠️ No blogs to index.")
        return
    index.reset()
    embeddings = model.encode([b["title"] + " " + b["description"] for b in blog_list])
    index.add(np.array(embeddings).astype("float32"))
    print(f"FAISS index built with {index.ntotal} vectors.")

def fetch_and_build_index():
    global blogs
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()
        blogs = data.get('blogs', [])
        if blogs:
            print(f"Fetched {len(blogs)} blogs from API.")
            build_faiss(blogs)
        else:
            print("⚠️ No blogs found from API!")
    except Exception as e:
        print("❌ Error fetching blogs:", e)


@app.route("/search", methods=['POST'])
def search():
    data = request.get_json()

    if not data or 'query' not in data:
        return jsonify({"error": "Request must be JSON with a 'query' key"}), 400

    query = data['query']
    k = data.get('k', 5)

    query_vec = model.encode([query])
    distances, indices = index.search(np.array(query_vec).astype("float32"), k)

    results = []
    for idx in indices[0]:
        if idx != -1 and idx < len(blogs):
            results.append(blogs[idx])

    print(results)

    return jsonify({"results": results})

if __name__ == "__main__":
    fetch_and_build_index()

    app.run(host="0.0.0.0", port=8010, debug=True)
