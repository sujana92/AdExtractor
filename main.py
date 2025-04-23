
import json
from openai import OpenAI

client = OpenAI(api_key="your_api_key")

# Load sample ads
with open('data/sample_ads.json') as f:
    ads = json.load(f)

# Load the prompt template
with open('prompt.txt') as f:
    prompt_template = f.read()

for ad in ads:
    prompt = prompt_template.replace("{{ad_text}}", ad["text"])

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    print(f"Ad ID {ad['id']} Response:\n", response.choices[0].message.content)
