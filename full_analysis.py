import json
from collections import Counter, defaultdict

with open('data/1vqyo7y/flat.json') as f:
    comments = json.load(f)

real_comments = [c for c in comments if c['author'] != '[deleted]']

# Cluster assignments
cluster_names = {
    0: "Pro-IDE Advocates",
    1: "Text Editor/Terminal Purists", 
    2: "Hybrid/Context-Dependent Users",
    3: "Build Process & Compilation Control",
    4: "Performance, Resources & Bloat",
    5: "Education, Learning & Personal History"
}

assignments = [
    0, 1, 0, 0, 1, 1, 0, 1, 1, 3, 4, 0, 1, 1, 1, 2, 1, 4, 2, 1, 0, 0, 3, 0, 0, 5, 0, 3, 3, 3, 0, 0, 0, 0, 3, 0, 3, 0, 1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 2, 2, 1, 1, 2, 0, 5, 2, 1, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 0, 0, 1, 3, 2, 3, 3, 3, 2, 2, 2, 0, 2, 2, 1, 2
]

assert len(assignments) == len(real_comments)

clusters = defaultdict(list)
for i, c in enumerate(real_comments):
    clusters[assignments[i]].append(c)

# Sentiment analysis
sentiments = []
for c in real_comments:
    body = c['body'].lower()
    score = c['score']
    # Simple heuristic sentiment
    positive_words = ['love', 'great', 'best', 'amazing', 'awesome', 'good', 'nice', 'excellent', 'prefer', 'enjoy', 'fast', 'seamless', 'indispensable', 'like', 'helpful']
    negative_words = ['hate', 'worst', 'bad', 'slow', 'bloat', 'suck', 'pain', 'hard', 'difficult', 'annoying', 'clunky', 'burnt', 'sadistic', 'larp', 'caveman']
    
    pos_count = sum(1 for w in positive_words if w in body)
    neg_count = sum(1 for w in negative_words if w in body)
    
    if neg_count > pos_count:
        sentiments.append('Negative')
    elif pos_count > neg_count:
        sentiments.append('Positive')
    else:
        sentiments.append('Neutral')

sentiment_counts = Counter(sentiments)
print("Sentiment distribution:", sentiment_counts)
print(f"Positive: {sentiment_counts['Positive']/len(real_comments)*100:.1f}%")
print(f"Neutral: {sentiment_counts['Neutral']/len(real_comments)*100:.1f}%")
print(f"Negative: {sentiment_counts['Negative']/len(real_comments)*100:.1f}%")

# Keywords
all_text = ' '.join(c['body'].lower() for c in real_comments)
words = all_text.split()
# Remove punctuation
import re
words = [re.sub(r'[^a-z]', '', w) for w in words]
words = [w for w in words if len(w) > 3]

stopwords = {'that', 'this', 'with', 'just', 'have', 'from', 'they', 'what', 'when', 'your', 'will', 'about', 'would', 'could', 'should', 'also', 'than', 'them', 'more', 'some', 'like', 'because', 'been', 'were', 'been', 'being', 'have', 'has', 'had', 'does', 'doing', 'done', 'much', 'very', 'well', 'even', 'still', 'only', 'really', 'think', 'know', 'make', 'made', 'just', 'don', 'doesn', 'didn', 'won', 'wasn', 'weren', 'couldn', 'wouldn', 'shouldn', 'can', 'cannot', 'aint', 'aren', 'isn', 'wasn', 'weren', 'being', 'having', 'doing'}
filtered = [w for w in words if w not in stopwords and len(w) > 3]

keyword_counts = Counter(filtered)
print("\nTop 15 keywords:")
for kw, cnt in keyword_counts.most_common(15):
    print(f"  {kw}: {cnt}")

# Engagement metrics
print(f"\nTotal comments: {len(real_comments)}")
print(f"Total upvotes: {sum(c['score'] for c in real_comments)}")
print(f"Average upvotes: {sum(c['score'] for c in real_comments)/len(real_comments):.2f}")
print(f"Most upvoted: {real_comments[0]['author']} with {real_comments[0]['score']} upvotes")

top_authors = Counter(c['author'] for c in real_comments).most_common(10)
print("\nTop contributing users:")
for author, count in top_authors:
    print(f"  {author}: {count} comments")

# Top comments in 10+ bucket
sorted_comments = sorted(real_comments, key=lambda x: x['score'], reverse=True)
top_10_plus = [c for c in sorted_comments if c['score'] >= 10]
print(f"\nTop 10+ comments: {len(top_10_plus)}")
for c in top_10_plus:
    print(f"  {c['score']:4d} | {c['author']:20s} | {c['id']}")
