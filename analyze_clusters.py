#!/usr/bin/env python3
"""Analyze Reddit thread j4x6ky and generate markdown report."""

import json
import re
from collections import Counter, defaultdict

# Load data
with open('data/j4x6ky/flat.json') as f:
    all_comments = json.load(f)

# Filter out deleted/removed/AutoModerator
real_comments = []
for c in all_comments:
    author = c.get('author', '')
    body = c.get('body', '')
    if author in ('[deleted]', 'AutoModerator'):
        continue
    if body in ('[deleted]', '[removed]'):
        continue
    real_comments.append(c)

total_analyzed = len(real_comments)
print(f"Total comments analyzed: {total_analyzed}")

# Sort by score descending
real_comments_sorted = sorted(real_comments, key=lambda x: x['score'], reverse=True)

total_upvotes = sum(c['score'] for c in real_comments)
avg_upvotes = total_upvotes / total_analyzed

# ============================================================
# CLUSTERING - Manual thematic analysis based on content review
# ============================================================

# Based on reading all 387 comments, I identified these themes:
# 1. Religious Doctrinal Responses (Islam/Christianity exceptions) ~80 comments
# 2. Atheist/Skeptical Challenges ~100 comments  
# 3. Theological Defenses (free will, justice, omnipotence) ~90 comments
# 4. Historical/Comparative Religion Debates ~60 comments
# 5. Personal Experience/Anecdotes ~30 comments
# 6. Meta/Debate Structure ~27 comments

# Let me do a more systematic analysis using keyword matching
# and then manually verify

def classify_comment(body, author):
    """Classify comment into thematic cluster."""
    body_lower = body.lower()
    
    # Cluster 1: Religious doctrinal responses about exceptions
    islam_keywords = ['islam', 'islamic', 'muslim', 'allah', 'quran', 'hadith', 'muhammad', 'islamqa', 'kuffaar', 'kafir']
    christian_keywords = ['bible', 'christian', 'jesus', 'christ', 'gospel', 'scripture', 'biblical', 'heaven', 'hell', 'salvation', 'resurrection', 'righteous', 'unrighteous', 'gehenna', 'sheol', 'hades', 'purgatory', 'catholic', 'protestant', 'acts 24:15', 'matthew', 'romans']
    jewish_keywords = ['judaism', 'jewish', 'torah', 'hebrew', 'monotheistic']
    doctrinal_keywords = ['doctrine', 'teaching', 'theology', 'theological', 'systematic', 'exegesis']
    
    # Check for religious doctrinal content
    has_religious_content = any(k in body_lower for k in islam_keywords + christian_keywords + jewish_keywords)
    
    # Cluster 2: Atheist/Skeptical
    atheist_keywords = ['atheist', 'atheism', 'no god', 'not real', 'doesn\'t exist', 'myth', 'cult', 'nonsense', 'garbage', 'bs', 'bullshit', 'made up', 'fairy tale', 'unconvincing', 'evidence', 'proof', 'lack of evidence', 'no evidence']
    skeptical_keywords = ['question', 'doubt', 'skeptical', 'ridiculous', 'absurd', 'illogical', 'contradiction', 'contradicts']
    
    # Cluster 3: Theological defenses (free will, justice, omnipotence)
    freewill_keywords = ['free will', 'freewill', 'choice', 'choose', 'accountability', 'responsible', 'rebel', 'sin', 'satan', 'fallen', 'omnipotent', 'omniscient', 'omnipresent', 'all-knowing', 'all-powerful', 'justice', 'just', 'benevolent', 'benevolence', 'grace', 'mercy']
    theological_keywords = ['god\'s plan', 'god\'s will', 'divine', 'supernatural', 'miracle', 'mystery', 'mystical']
    
    # Cluster 4: Historical/Comparative
    historical_keywords = ['crusades', 'inquisition', 'forced conversion', 'forced conversions', 'history', 'historical', 'ancient', 'roman', 'medieval', 'spanish', 'portuguese', 'nazi', 'hitler', 'holocaust', 'antisemitism', 'slave', 'slavery', 'persecution']
    comparative_keywords = ['judaism', 'jewish', 'hindu', 'buddhism', 'religion', 'monotheistic', 'abrahamic']
    
    # Cluster 5: Personal experience
    personal_keywords = ['i was', 'i grew up', 'my family', 'my church', 'i experienced', 'i saw', 'i met', 'my story', 'i was abused', 'i prayed', 'i cried']
    
    # Cluster 6: Meta/debate
    meta_keywords = ['nice post', 'change my mind', 'op is', 'you are wrong', 'you are correct', 'this doesn\'t answer', 'you dodged', 'off topic', 'moderator', 'rule']
    
    # Scoring
    scores = defaultdict(int)
    
    # Religious doctrinal responses
    if any(k in body_lower for k in islam_keywords + christian_keywords + jewish_keywords + doctrinal_keywords):
        # But check if it's actually arguing FOR the doctrine or criticizing it
        if not any(k in body_lower for k in atheist_keywords + skeptical_keywords):
            scores['religious_doctrinal'] += 2
    
    # Atheist/Skeptical
    if any(k in body_lower for k in atheist_keywords):
        scores['atheist_skeptical'] += 3
    if any(k in body_lower for k in skeptical_keywords):
        scores['atheist_skeptical'] += 1
    
    # Theological defenses
    if any(k in body_lower for k in freewill_keywords):
        scores['theological_defense'] += 2
    if any(k in body_lower for k in theological_keywords):
        scores['theological_defense'] += 1
    
    # Historical/Comparative
    if any(k in body_lower for k in historical_keywords):
        scores['historical_comparative'] += 3
    if any(k in body_lower for k in comparative_keywords) and not any(k in body_lower for k in islam_keywords + christian_keywords + jewish_keywords):
        scores['historical_comparative'] += 1
    
    # Personal experience
    if any(k in body_lower for k in personal_keywords):
        scores['personal_experience'] += 2
    
    # Meta
    if any(k in body_lower for k in meta_keywords):
        scores['meta_debate'] += 2
    
    # Special cases based on content review
    # Comments that are clearly discussing religious exceptions
    exception_keywords = ['exception', 'pardoned', 'not punished', 'not condemned', 'different judgement', 'separate test', 'resurrection of the unrighteous', 'opportunity', 'purified', 'chance to turn']
    if any(k in body_lower for k in exception_keywords):
        scores['religious_doctrinal'] += 3
    
    # Comments specifically about evidence/lack thereof
    evidence_keywords = ['evidence', 'proof', 'show that he exists', 'sufficient proof', 'didn\'t show', 'hidden', 'shy']
    if any(k in body_lower for k in evidence_keywords):
        scores['atheist_skeptical'] += 2
        scores['theological_defense'] += 1
    
    # Comments about missionaries/saving souls
    missionary_keywords = ['missionary', 'missionaries', 'preach', 'evangelize', 'share the word', 'save souls', 'conversion']
    if any(k in body_lower for k in missionary_keywords):
        scores['atheist_skeptical'] += 1
        scores['religious_doctrinal'] += 1
    
    # Get highest scoring cluster
    if not scores:
        return 'other', 0
    
    best_cluster = max(scores, key=scores.get)
    return best_cluster, scores[best_cluster]

# Classify all comments
classifications = []
for c in real_comments:
    cluster, confidence = classify_comment(c['body'], c['author'])
    classifications.append({
        'comment': c,
        'cluster': cluster,
        'confidence': confidence
    })

# Show distribution
cluster_counts = Counter(c['cluster'] for c in classifications)
print("\nInitial cluster distribution:")
for cluster, count in cluster_counts.most_common():
    print(f"  {cluster}: {count}")

# Review low-confidence classifications and other
print("\n\nComments classified as 'other':")
other_comments = [c for c in classifications if c['cluster'] == 'other']
for item in other_comments[:20]:
    print(f"  [{item['comment']['score']}] {item['comment']['author']}: {item['comment']['body'][:150]}")
    print()
