import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

SYSTEM_PROMPT = """
You are a professional NV Shoppe Sales Manager.
Rules:
- Be honest
- No income guarantee
- Clear objections
- Hindi + English mix allowed
- Close softly and ethically
"""

def ai_sales_reply(user_msg):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_msg}
        ],
        temperature=0.4
    )
    return response.choices[0].message.content
