import json

with open('data/1vqyo7y/flat.json') as f:
    comments = json.load(f)

real_comments = [c for c in comments if c['author'] != '[deleted]']

# Sort by score descending
sorted_comments = sorted(real_comments, key=lambda x: x['score'], reverse=True)

print("Top comments:")
for c in sorted_comments[:15]:
    print(f"{c['score']:4d} | {c['author']:20s} | {c['body'][:100]}")

print("\n>=10 upvotes:")
for c in sorted_comments:
    if c['score'] >= 10:
        print(f"{c['score']:4d} | {c['author']:20s} | {c['id']}")
