#!/usr/bin/env python3
"""Analyze Reddit thread j4x6ky and generate markdown report."""

import json
import re
from collections import Counter, defaultdict
from urllib.parse import urljoin

# Load data
with open('data/j4x6ky/flat.json') as f:
    all_comments = json.load(f)

print(f"Total comments in flat.json: {len(all_comments)}")

# Filter out deleted/removed/AutoModerator
real_comments = []
for c in all_comments:
    author = c.get('author', '')
    body = c.get('body', '')
    if author == '[deleted]' or body == '[deleted]' or body == '[removed]':
        continue
    if author == 'AutoModerator':
        continue
    real_comments.append(c)

print(f"Real comments (after filtering): {len(real_comments)}")

# Ensure we have exactly 388
assert len(real_comments) == 388, f"Expected 388 real comments, got {len(real_comments)}"

# Basic stats
total_analyzed = len(real_comments)
total_upvotes = sum(c['score'] for c in real_comments)
avg_upvotes = total_upvotes / total_analyzed if total_analyzed > 0 else 0

print(f"Total upvotes: {total_upvotes}")
print(f"Average upvotes: {avg_upvotes:.2f}")

# Sort by score descending for top comments
real_comments_sorted = sorted(real_comments, key=lambda x: x['score'], reverse=True)

# Print top 10 to understand distribution
print("\nTop 10 comments by score:")
for c in real_comments_sorted[:10]:
    print(f"  {c['score']} upvotes | {c['author']} | {c['body'][:100]}...")

# Check score distribution
score_counts = Counter(c['score'] for c in real_comments)
print(f"\nScore distribution (top 10): {score_counts.most_common(10)}")

# Let's read all comment bodies to understand themes for clustering
print("\n\n--- SAMPLE COMMENTS FOR THEME ANALYSIS ---")
for i, c in enumerate(real_comments_sorted[:50]):
    print(f"{i+1}. [{c['score']}] {c['author']}: {c['body'][:200]}")
    print()
