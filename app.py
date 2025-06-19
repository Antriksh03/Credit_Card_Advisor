import streamlit as st
from recommender import recommend_cards
from agent import ask_user_questions

st.set_page_config(page_title="Credit Card Advisor", layout="centered")
st.title("💳 Credit Card Advisor")

st.write("Hi! I'm your credit card assistant. Let's find your ideal credit card.")

if "chat" not in st.session_state:
    st.session_state.chat = []
if "answers" not in st.session_state:
    st.session_state.answers = {}

fields = {
    "Monthly Income": "monthly_income",
    "Spending habits (fuel, travel, groceries, dining)": "spending",
    "Preferred benefits (cashback, travel points, lounge access)": "preferred_benefits",
    "Existing cards (optional)": "existing_cards",
    "Credit score (or 'unknown')": "credit_score"
}

for label, key in fields.items():
    if key not in st.session_state.answers:
        user_input = st.text_input(label)
        if user_input:
            st.session_state.answers[key] = user_input

if len(st.session_state.answers) == len(fields):
    st.success("Thanks! Generating recommendations...")
    cards = recommend_cards(st.session_state.answers)

    for card in cards:
        st.image(card["image_url"], width=100)
        st.markdown(f"### {card['name']} ({card['issuer']})")
        st.markdown(f"**Rewards:** {card['reward_rate']}")
        st.markdown(f"**Perks:** {card['perks']}")
        st.markdown(f"[Apply Now]({card['apply_link']})", unsafe_allow_html=True)

    st.button("Restart", on_click=lambda: st.session_state.clear())
