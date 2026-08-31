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
real_comments_sorted = sorted(real_comments, key=lambda x: x['score'], reverse=True)
total_upvotes = sum(c['score'] for c in real_comments)
avg_upvotes = total_upvotes / total_analyzed

# ============================================================
# CLUSTERING - Manual thematic analysis
# ============================================================

def classify_comment(body, author):
    """Classify comment into thematic cluster based on content analysis."""
    body_lower = body.lower()
    
    # Initialize scores
    scores = defaultdict(int)
    
    # 1. Religious Doctrinal Responses
    # Comments that present or explain religious teachings about exceptions
    islam_content = any(k in body_lower for k in ['islam', 'islamic', 'muslim', 'allah', 'quran', 'hadith', 'muhammad', 'kuffaar', 'kafir', 'islamqa'])
    christian_content = any(k in body_lower for k in ['bible', 'christian', 'jesus', 'christ', 'gospel', 'scripture', 'biblical', 'heaven', 'hell', 'salvation', 'resurrection', 'righteous', 'unrighteous', 'gehenna', 'sheol', 'hades', 'catholic', 'protestant', 'acts 24:15', 'matthew', 'romans', 'paul', 'apostle', 'parable'])
    jewish_content = any(k in body_lower for k in ['judaism', 'jewish', 'torah', 'hebrew', 'monotheistic', 'rabbinic'])
    religious_content = islam_content or christian_content or jewish_content
    
    doctrinal_keywords = ['doctrine', 'teaching', 'theology', 'theological', 'systematic', 'exegesis', 'exception', 'pardoned', 'not punished', 'not condemned', 'different judgement', 'separate test', 'opportunity', 'purified', 'chance to turn', 'will be tested', 'judged based on', 'not to know', 'never heard', 'did not receive the message']
    exception_content = any(k in body_lower for k in doctrinal_keywords)
    
    # Religious content + not strongly atheist
    if religious_content and exception_content:
        scores['religious_doctrinal'] += 3
    elif religious_content:
        scores['religious_doctrinal'] += 2
    
    # 2. Atheist/Skeptical Challenges
    atheist_keywords = ['atheist', 'atheism', 'not real', 'doesn\'t exist', 'does not exist', 'myth', 'cult', 'nonsense', 'garbage', 'bs ', 'bullshit', 'made up', 'fairy tale', 'unconvincing', 'insufficient proof', 'not enough proof', 'no evidence', 'lack of evidence', 'doesn\'t show', 'didn\'t show', 'hiding', 'shy']
    skeptical_keywords = ['question', 'doubt', 'skeptical', 'ridiculous', 'absurd', 'illogical', 'contradiction', 'contradicts', 'doesn\'t make sense', 'makes no sense', 'doesn\'t answer', 'dodged', 'terrifying', 'mad', 'angry']
    
    if any(k in body_lower for k in atheist_keywords):
        scores['atheist_skeptical'] += 3
    if any(k in body_lower for k in skeptical_keywords):
        scores['atheist_skeptical'] += 1
    if 'god isn\'t real' in body_lower or 'god is not real' in body_lower or 'there is no god' in body_lower:
        scores['atheist_skeptical'] += 3
    
    # 3. Theological Defenses
    freewill_keywords = ['free will', 'freewill', 'free choice', 'choice', 'accountability', 'responsible', 'rebel', 'rebellion', 'sin', 'satan', 'fallen', 'omnipotent', 'omniscient', 'omnipresent', 'all-knowing', 'all-powerful', 'justice', 'just', 'benevolent', 'benevolence', 'grace', 'mercy', 'forgive', 'forgiveness']
    theological_keywords = ['god\'s plan', 'god\'s will', 'divine', 'supernatural', 'miracle', 'mystery', 'mystical', 'perfect', 'formless', 'creator', 'creation', 'origin of the universe', 'big bang', 'intelligent design']
    
    if any(k in body_lower for k in freewill_keywords):
        scores['theological_defense'] += 2
    if any(k in body_lower for k in theological_keywords):
        scores['theological_defense'] += 1
    
    # Special case: defending against atheist challenges
    if religious_content and any(k in body_lower for k in ['not a biblical teaching', 'false teachings', 'traditional', 'interpretation', 'context']):
        scores['religious_doctrinal'] += 2
    
    # 4. Historical/Comparative Religion Debates
    historical_keywords = ['crusades', 'inquisition', 'forced conversion', 'forced conversions', 'history', 'historical', 'ancient', 'roman', 'medieval', 'spanish', 'portuguese', 'nazi', 'hitler', 'holocaust', 'antisemitism', 'slavery', 'slave', 'persecution', 'violence', 'kill', 'murder', 'genocide']
    comparative_keywords = ['judaism', 'jewish', 'hindu', 'buddhism', 'monotheistic', 'abrahamic', 'zoroastrian', 'comparison']
    
    if any(k in body_lower for k in historical_keywords):
        scores['historical_comparative'] += 3
    if any(k in body_lower for k in comparative_keywords) and not religious_content:
        scores['historical_comparative'] += 2
    
    # 5. Personal Experience/Anecdotes
    personal_keywords = ['i was', 'i grew up', 'my family', 'my church', 'i experienced', 'i saw', 'i met', 'my story', 'i was abused', 'i prayed', 'i cried', 'my former', 'my life', 'i have a', 'i\'ve had', 'i remember', 'my father', 'my mother', 'my parents']
    if any(k in body_lower for k in personal_keywords):
        scores['personal_experience'] += 2
    
    # 6. Meta/Debate Structure
    meta_keywords = ['nice post', 'change my mind', 'op is', 'you are wrong', 'you are correct', 'this doesn\'t answer', 'you dodged', 'off topic', 'moderator', 'rule', 'removed', 'you didn\'t', 'you just', 'whole lot of nothing', 'makes no sense', 'your comment', 'your argument', 'reply to']
    if any(k in body_lower for k in meta_keywords):
        scores['meta_debate'] += 2
    
    # 7. Philosophical/Abstract
    philosophical_keywords = ['what if', 'imagine', 'suppose', 'consider', 'think about', 'question is', 'problem with', 'issue is', 'the problem']
    if any(k in body_lower for k in philosophical_keywords):
        scores['philosophical'] += 1
    
    # 8. Science/Naturalism
    science_keywords = ['evolution', 'scientific', 'science', 'study', 'research', 'evidence', 'proof', 'empirical', 'falsification', 'verifiable']
    if any(k in body_lower for k in science_keywords):
        scores['science_naturalism'] += 1
    
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
print("Initial cluster distribution:")
for cluster, count in cluster_counts.most_common():
    print(f"  {cluster}: {count}")

# Review 'other' and low-confidence comments
print("\n\nComments in 'other' or low-confidence:")
for item in classifications:
    if item['cluster'] == 'other' or item['confidence'] == 0:
        print(f"  [{item['comment']['score']}] {item['comment']['author']}: {item['comment']['body'][:200]}")
        print(f"    -> cluster: {item['cluster']}, confidence: {item['confidence']}")
        print()
