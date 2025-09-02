# AI-Powered Blog Platform

An advanced blog site with AI integration that goes beyond traditional blogging.  
It not only allows creating and reading blogs, but also adds **AI-driven features** such as content moderation, blog generation, summarization, and semantic search.

## Features
- **AI Blog Generation** – Generate blogs using AI assistance  
- **AI Summarization** – Summarize long blogs into concise points  
- **Semantic Search** – Search blogs using natural language queries  
- **NSFW Detection** – Detect and block inappropriate **text** and **images** in blogs  

## 🛠 Tech Stack
- **Frontend**: React / Next.js (or your choice)  
- **Backend**: Node.js + Express + FastAPI  
- **Database**: MongoDB Atlas  
- **AI Models**: Hugging Face Transformers (for embeddings, summarization, and generation)  
- **Search Engine**: FAISS for vector similarity search  

## 🚀 Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/Arvindh2005/contextual-blog-site.git
   cd contextual-blog-site

2. For python-based server:
   ```bash
   cd python-ml
   python main.py
3. Open another terminal for second python server:
   ```bash
   python test.py
4. In /server, create a .env file with the following details: JWT_SECRET, ADMIN_EMAIL, ADMIN_PASSWORD, MONGODB_URI, IMAGEKIT_PUBLIC_KEY, IMAGEKIT_PRIVATE_KEY, IMAGEKIT_URL_ENDPOINT, GEMINI_API_KEY
5. In /client, create a .env file with the following details: VITE_BASE_URL
6. For Express js server:
   ```bash
   cd server
   npm install
   npm run server
7. For Front-end:
   ```bash
   cd client
   npm install
   npm run dev

  
    

   
   
