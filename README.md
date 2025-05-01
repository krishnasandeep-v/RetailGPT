# RetailGPT 🛍️ - AI-Powered Multimodal Retail Assistant

RetailGPT is an AI project that combines computer vision and NLP to create a smart assistant for retail experiences. It recommends products based on uploaded images, user preferences, and review-based sentiment analysis.

## 🔥 Features
- 📷 Image-Based Product Matching (CLIP-powered)
- 🧠 Personalized Recommendations (Rule-based placeholder, extensible to BERT4Rec)
- 💬 Review Sentiment Tags (NLP-based analysis)
- ⚡ FastAPI Backend (Easy integration & deployment)

## 🛠️ Tech Stack
- Python, FastAPI, PyTorch, CLIP (OpenAI), PIL
- Optional frontend: Streamlit (not included yet)

## 📂 Project Structure
```
RetailGPT/
├── app/
│   ├── main.py
│   ├── vision_model.py
│   ├── recommender.py
│   ├── sentiment_model.py
├── requirements.txt
├── README.md
```

## 🚀 Getting Started

1. Clone the repo or unzip the project folder:
```bash
git clone https://github.com/yourusername/RetailGPT.git
cd RetailGPT
```
2. Create a virtual environment & install requirements:
```bash
pip install -r requirements.txt
```
3. Run the app:
```bash
uvicorn app.main:app --reload
```

## 📌 Notes
- You can add sample images under `sample_catalog/images/` for testing.
- Extend the recommendation engine with actual collaborative filtering.

## 🎯 Why This Project?
- Demonstrates vision + NLP integration.
- Business relevance: Personalized commerce experiences.
- Shows system design and production-readiness.

## 📬 Contact
For questions, contact v.sandeepkrishna@gmail.com
