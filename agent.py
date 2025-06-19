import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_user_questions(chat_history, question):
    messages = [{"role": "system", "content": "You're a credit card advisor. Ask the user questions to understand their needs, then recommend best-fit Indian credit cards."}]
    messages += chat_history
    messages.append({"role": "assistant", "content": question})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response.choices[0].message["content"]
