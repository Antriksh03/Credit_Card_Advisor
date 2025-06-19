# 💳 Credit Card Advisor

A conversational credit card recommendation tool built using OpenAI and Streamlit.

## 🔧 Features
- LLM-powered Q&A flow
- Personalized card recommendations
- Simple rule-based recommender engine
- Mobile-friendly interface

## 🚀 Getting Started

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/credit-card-advisor.git
cd credit-card-advisor
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables:**
- Create a `.env` file using the provided `.env.example`:
```env
OPENAI_API_KEY=your_actual_key_here
```

4. **Run the app:**
```bash
streamlit run app.py
```

## 📁 Notes
- Your `.env` file is ignored via `.gitignore` to keep your OpenAI key safe.
- Add your own credit card images to `cards.json` for a better visual experience.

## 🛡️ License
MIT License
