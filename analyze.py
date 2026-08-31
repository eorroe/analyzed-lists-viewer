import json
from collections import Counter

with open('data/1vqyo7y/flat.json') as f:
    comments = json.load(f)

real_comments = [c for c in comments if c['author'] != '[deleted]']
print(f"Total real comments: {len(real_comments)}")

# Print all with index
for i, c in enumerate(real_comments):
    body = c['body'].replace('\n', ' ')[:200]
    print(f"{i+1:3d}. [{c['author']:20s}] {c['score']:4d} | {body}")
