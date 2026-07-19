# Personal Blog API - Dattatray Bhosale
# Strong Backend Project for Recruiters

from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

# Sample Blog Posts
posts = [
    {
        "id": 1,
        "title": "My Journey into Full Stack Development",
        "content": "Starting with PHP and moving to Python has been an amazing learning experience...",
        "date": "2026-07-01",
        "tags": ["python", "career"]
    }
]

@app.route('/')
def home():
    return jsonify({
        "message": "Personal Blog API is running",
        "status": "active",
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

@app.route('/posts', methods=['GET'])
def get_posts():
    return jsonify(posts)

@app.route('/posts', methods=['POST'])
def add_post():
    data = request.get_json()
    new_post = {
        "id": len(posts) + 1,
        "title": data.get("title"),
        "content": data.get("content"),
        "date": datetime.now().strftime("%Y-%m-%d"),
        "tags": data.get("tags", [])
    }
    posts.append(new_post)
    return jsonify({"message": "Post added successfully", "post": new_post}), 201

if __name__ == '__main__':
    print("🚀 Personal Blog API running on http://localhost:5000")
    app.run(debug=True)
