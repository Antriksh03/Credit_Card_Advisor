import json

def load_cards():
    with open("cards.json", "r") as f:
        return json.load(f)

def recommend_cards(user_inputs):
    cards = load_cards()
    recommendations = []

    for card in cards:
        if "cashback" in user_inputs["preferred_benefits"].lower() and "cashback" in card["reward_type"]:
            recommendations.append(card)
        elif "travel" in user_inputs["preferred_benefits"].lower() and "lounge" in card["perks"].lower():
            recommendations.append(card)

    return recommendations[:3]
