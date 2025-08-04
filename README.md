# NeuraCart 🛒 – AI-Powered Shopping Intelligence

NeuraCart is an AI-native retail assistant that combines cutting-edge computer vision and NLP to revolutionize online shopping. It helps users discover, compare, and choose products seamlessly by leveraging image-based search, personalized recommendations, and review sentiment insights.

## 🔥 Features
- 🖼️ Visual Search from Images (CLIP-powered)
- 🎯 Personalized Recommendations (Rule-based now; extensible to BERT4Rec or transformer models)
- 💬 Review Sentiment Tags (NLP-driven insights)
- ⚡ FastAPI Backend for scalable, production-ready deployment

## 🛠️ Tech Stack
- Python, FastAPI, PyTorch, OpenAI CLIP, PIL
- Optional frontend: Streamlit (for demos)

## 📂 Project Structure

```
NeuraCart/
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
git clone https://github.com/yourusername/NeuraCart.git
cd NeuraCart
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

## 👤 Founder Vision

I built NeuraCart to solve a personal pain point: the frustrating and inefficient way people search for products online. Leveraging deep experience in AI and software engineering, combined with a passion for retail technology, my goal is to transform online shopping into an intuitive, personalized experience. I believe AI-powered multimodal search is the future of eCommerce, and NeuraCart is positioned to lead that change — starting from pilot retail partnerships to large-scale adoption.

## 📬 Contact
For questions, contact v.sandeepkrishna@gmail.com
