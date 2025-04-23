
import json
from openai import OpenAI

client = OpenAI(api_key="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")

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
