import os
import re
import argparse

from openai import OpenAI

client = OpenAI()

parser = argparse.ArgumentParser(description="")

parser.add_argument("--theme", "-t", type=str, required=True)
parser.add_argument("--start", "-s", type=int, default=0)
parser.add_argument("--end", "-e", type=int, default=14)
args = parser.parse_args()

posts = []
with open(f'Themes/{args.theme}.md', 'r', encoding='utf-8') as f:
    for line in f.read().split('\n'):
        m = re.search(r"\*\*(.*):\*\*", line)
        if m:
            posts.append(m.group(1))

def write(num, theme, post):
    with open('Prompt.md', 'r', encoding='utf-8') as f:
        prompt = f.read()
    with open(f'Themes/{theme}.md', 'r', encoding='utf-8') as f:
        plan = f.read()
    prompt += f"{plan}"

    input = (
        f"Task: Following all guidelines provided, write post {post} for the theme {theme}.\n\n"
        "Response: Respond with a markdown formatted article no more than 1000 words. You may perform web searches using wikipedia as needed."
    )

    output = f"./Posts/{theme}/{num} - {post}.md"
    os.makedirs(f"./Posts/{theme}", exist_ok=True)

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

num = args.start + 1
for post in posts[args.start:args.end]:
    print(f'{args.theme}: {post}')
    write(num, args.theme, post)
    num += 1

