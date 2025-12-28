import os
import argparse

from openai import OpenAI

client = OpenAI()

parser = argparse.ArgumentParser(description="")

parser.add_argument("--theme", "-t", type=str, required=True)
parser.add_argument("--post", "-p", type=str, required=True)
args = parser.parse_args()

with open('Prompt.md', 'r', encoding='utf-8') as f:
    prompt = f.read()
with open(f'Themes/{args.theme}.md', 'r', encoding='utf-8') as f:
    plan = f.read()
prompt += f"{plan}"

input = (
    f"Task: Following all guidelines provided, write post {args.post} for the theme {args.theme}.\n\n"
    "Response: Respond with a markdown formatted article no more than 1000 words. You may perform web searches using wikipedia as needed."
)

output = f"./Posts/{args.theme}/{args.post}.md"
os.makedirs(f"./Posts/{args.theme}", exist_ok=True)

response = client.responses.create(
    model="gpt-5",
    instructions=prompt,
    input=input,
    tools=[{
        "type": "web_search",
        # "filters": {
        #     "allowed_domains": ["en.wikipedia.org"]
        # },
    }],
)
print(response.output_text)

with open(output, 'w') as f:
    f.write(response.output_text)
