#!/usr/bin/env python3
import json, re
from collections import Counter

with open('data/1nniewj/flat.json') as f:
    comments = json.load(f)

# Filter real comments
real_comments = [c for c in comments if c['body'] not in ('[deleted]', '[removed]')]
print(f"Total real comments: {len(real_comments)}")

# Simple keyword-based clustering
clusters = {
    'Business Value & ROI': [],
    'Version Control Necessity': [],
    'Practical Implementation Advice': [],
    'Humor & Off-topic': [],
    'Personal Experience & Anecdotes': [],
    'Questions & Clarifications': [],
    'Other': []
}

# Keywords for each cluster
business_keywords = ['business', 'money', 'cost', 'save', 'roi', 'risk', 'budget', 'financial', 'revenue', 'efficiency', 'productivity', 'time', 'hour', 'dollar', 'pay', 'compliance', 'legal', 'insurance', 'disaster', 'recovery', 'downtime', 'customer', 'hire', 'talent']
necessity_keywords = ['standard', 'every', 'must', 'need', 'require', 'essential', 'basic', '2025', 'industry', 'normal', 'obvious', 'insane', 'red flag', 'quit', 'leave', 'walk']
implementation_keywords = ['git', 'github', 'azure', 'devops', 'hosting', 'server', 'cloud', 'self-host', 'local', 'network', 'demo', 'present', 'slide', 'chatgpt', 'ai', 'tool', 'use']
humor_keywords = ['text editor', 'final', 'v1', 'v2', '_final', '1987', '1985', 'magnet', 'flip bit', 'carpenter', 'hammer']
experience_keywords = ['i ', 'my ', 'we ', 'our ', 'company', 'team', 'worked', 'used', 'walked', 'experienced', 'remember', 'years ago', 'previously']
question_keywords = ['?', 'how', 'what', 'why', 'when', 'where', 'which', 'do you', 'are you', 'is it']

def classify_comment(body):
    body_lower = body.lower()
    scores = {}
    for kw in business_keywords:
        if kw in body_lower:
            scores['Business Value & ROI'] = scores.get('Business Value & ROI', 0) + 1
    for kw in necessity_keywords:
        if kw in body_lower:
            scores['Version Control Necessity'] = scores.get('Version Control Necessity', 0) + 1
    for kw in implementation_keywords:
        if kw in body_lower:
            scores['Practical Implementation Advice'] = scores.get('Practical Implementation Advice', 0) + 1
    for kw in humor_keywords:
        if kw in body_lower:
            scores['Humor & Off-topic'] = scores.get('Humor & Off-topic', 0) + 1
    for kw in experience_keywords:
        if kw in body_lower:
            scores['Personal Experience & Anecdotes'] = scores.get('Personal Experience & Anecdotes', 0) + 1
    for kw in question_keywords:
        if kw in body_lower:
            scores['Questions & Clarifications'] = scores.get('Questions & Clarifications', 0) + 1
    
    if not scores:
        return 'Other'
    return max(scores, key=scores.get)

for c in real_comments:
    cluster = classify_comment(c['body'])
    clusters[cluster].append(c)

# Verify total
total_clustered = sum(len(v) for v in clusters.values())
print(f"Total clustered: {total_clustered}")
print()
for name, items in clusters.items():
    upvotes = sum(c['score'] for c in items)
    print(f"{name}: {len(items)} comments, {upvotes} upvotes")

# Sentiment analysis (simple keyword-based)
positive_words = ['good', 'great', 'excellent', 'helpful', 'useful', 'love', 'best', 'amazing', 'fantastic', 'perfect', 'should', 'recommend', 'agree', 'yes', 'absolutely', 'definitely']
negative_words = ['bad', 'worst', 'terrible', 'awful', 'hate', 'horrible', 'no', 'never', 'quit', 'leave', 'nightmare', 'insane', 'wtf', 'bonkers', 'yikes', 'flabbergasted']
neutral_words = ['maybe', 'perhaps', 'might', 'could', 'consider', 'think', 'feel', 'seems', 'appears']

def simple_sentiment(body):
    body_lower = body.lower()
    pos = sum(1 for w in positive_words if w in body_lower)
    neg = sum(1 for w in negative_words if w in body_lower)
    neu = sum(1 for w in neutral_words if w in body_lower)
    if pos > neg:
        return 'Positive'
    elif neg > pos:
        return 'Negative'
    else:
        return 'Neutral'

sentiments = Counter(simple_sentiment(c['body']) for c in real_comments)
print()
print('Sentiment distribution:')
for s, count in sentiments.most_common():
    print(f"  {s}: {count} ({count/len(real_comments)*100:.1f}%)")

# Top comments per bucket
buckets = [
    (1000000, float('inf'), '1M+'),
    (900000, 999999, '900k+'),
    (800000, 899999, '800k+'),
    (100000, 199999, '100k+'),
    (90000, 99999, '90k+'),
    (80000, 89999, '80k+'),
    (10000, 19999, '10k+'),
    (9000, 9999, '9k+'),
    (8000, 8999, '8k+'),
    (1000, 1999, '1k+'),
    (900, 999, '900+'),
    (800, 899, '800+'),
    (100, 199, '100+'),
    (90, 99, '90+'),
    (80, 89, '80+'),
    (10, 19, '10+')
]

print()
print('Top comments by bucket:')
for low, high, label in buckets:
    candidates = [c for c in real_comments if low <= c['score'] <= high]
    if candidates:
        best = max(candidates, key=lambda x: x['score'])
        print(f"  {label}: {best['score']} by {best['author']}")

# Keyword extraction
all_text = ' '.join(c['body'] for c in real_comments)
all_text = re.sub(r'http\S+', '', all_text)
all_text = re.sub(r'[^a-zA-Z\s]', '', all_text).lower()
words = all_text.split()
stop_words = {'the', 'and', 'to', 'of', 'a', 'in', 'is', 'it', 'you', 'that', 'for', 'on', 'with', 'as', 'this', 'be', 'are', 'was', 'or', 'at', 'not', 'your', 'have', 'from', 'they', 'but', 'what', 'all', 'can', 'do', 'if', 'we', 'how', 'who', 'when', 'there', 'their', 'more', 'some', 'like', 'just', 'about', 'would', 'could', 'should', 'may', 'might', 'will', 'shall', 'must', 'can', 'cannot', 'could', 'would', 'should', 'may', 'might', 'must', 'shall', 'will', 'also', 'than', 'then', 'them', 'these', 'those', 'been', 'being', 'have', 'has', 'had', 'having', 'does', 'did', 'doing', 'done', 'going', 'gone', 'get', 'got', 'getting', 'gotten', 'make', 'made', 'making', 'take', 'took', 'taken', 'taking', 'come', 'came', 'coming', 'see', 'saw', 'seen', 'seeing', 'look', 'looked', 'looking', 'want', 'wanted', 'wanting', 'use', 'used', 'using', 'say', 'said', 'saying', 'tell', 'told', 'telling', 'ask', 'asked', 'asking', 'work', 'worked', 'working', 'seem', 'seemed', 'seeming', 'feel', 'felt', 'feeling', 'try', 'tried', 'trying', 'leave', 'left', 'leaving', 'call', 'called', 'calling', 'keep', 'kept', 'keeping', 'let', 'lets', 'letting', 'begin', 'began', 'begun', 'beginning', 'show', 'showed', 'shown', 'showing', 'hear', 'heard', 'hearing', 'play', 'played', 'playing', 'run', 'ran', 'running', 'move', 'moved', 'moving', 'live', 'lived', 'living', 'believe', 'believed', 'believing', 'happen', 'happened', 'happening', 'give', 'gave', 'given', 'giving', 'bring', 'brought', 'bringing', 'write', 'wrote', 'written', 'writing', 'provide', 'provided', 'providing', 'sit', 'sat', 'sitting', 'stand', 'stood', 'standing', 'lose', 'lost', 'losing', 'pay', 'paid', 'paying', 'meet', 'met', 'meeting', 'include', 'included', 'including', 'continue', 'continued', 'continuing', 'set', 'setting', 'learn', 'learned', 'learning', 'change', 'changed', 'changing', 'lead', 'led', 'leading', 'understand', 'understood', 'understood', 'understanding', 'watch', 'watched', 'watching', 'follow', 'followed', 'following', 'stop', 'stopped', 'stopping', 'create', 'created', 'creating', 'speak', 'spoke', 'spoken', 'speaking', 'read', 'reading', 'allow', 'allowed', 'allowing', 'add', 'added', 'adding', 'spend', 'spent', 'spending', 'grow', 'grew', 'grown', 'growing', 'open', 'opened', 'opening', 'walk', 'walked', 'walking', 'win', 'won', 'winning', 'offer', 'offered', 'offering', 'remember', 'remembered', 'remembering', 'love', 'loved', 'loving', 'consider', 'considered', 'considering', 'appear', 'appeared', 'appearing', 'buy', 'bought', 'buying', 'wait', 'waited', 'waiting', 'serve', 'served', 'serving', 'die', 'died', 'dying', 'send', 'sent', 'sending', 'expect', 'expected', 'expecting', 'build', 'built', 'building', 'stay', 'stayed', 'staying', 'fall', 'fell', 'fallen', 'falling', 'cut', 'cutting', 'reach', 'reached', 'reaching', 'kill', 'killed', 'killing', 'remain', 'remained', 'remaining', 'suggest', 'suggested', 'suggesting', 'raise', 'raised', 'raising', 'pass', 'passed', 'passing', 'sell', 'sold', 'selling', 'require', 'required', 'requiring', 'report', 'reported', 'reporting', 'decide', 'decided', 'deciding', 'pull', 'pulled', 'pulling', 'return', 'returned', 'returning', 'explain', 'explained', 'explaining', 'hope', 'hoped', 'hoping', 'develop', 'developed', 'developing', 'carry', 'carried', 'carrying', 'break', 'broke', 'broken', 'breaking', 'receive', 'received', 'receiving', 'agree', 'agreed', 'agreeing', 'support', 'supported', 'supporting', 'hit', 'hit', 'hitting', 'produce', 'produced', 'producing', 'eat', 'ate', 'eaten', 'eating', 'cover', 'covered', 'covering', 'push', 'pushed', 'pushing', 'throw', 'threw', 'thrown', 'throwing', 'catch', 'caught', 'catching', 'draw', 'drew', 'drawn', 'drawing', 'choose', 'chose', 'chosen', 'choosing', 'wear', 'wore', 'worn', 'wearing', 'cause', 'caused', 'causing', 'point', 'pointed', 'pointing', 'listen', 'listened', 'listening', 'agree', 'agreed', 'agreeing', 'accept', 'accepted', 'accepting', 'share', 'shared', 'sharing', 'join', 'joined', 'joining', 'fail', 'failed', 'failing', 'improve', 'improved', 'improving', 'save', 'saved', 'saving', 'protect', 'protected', 'protecting', 'control', 'controlled', 'controlling', 'track', 'tracked', 'tracking', 'roll', 'rolled', 'rolling', 'review', 'reviewed', 'reviewing', 'test', 'tested', 'testing', 'deploy', 'deployed', 'deploying', 'merge', 'merged', 'merging', 'branch', 'branched', 'branching', 'commit', 'committed', 'committing', 'push', 'pushed', 'pushing', 'pull', 'pulled', 'pulling', 'clone', 'cloned', 'cloning', 'fetch', 'fetched', 'fetching', 'rebase', 'rebased', 'rebasing', 'stash', 'stashed', 'stashing', 'reset', 'reset', 'resetting', 'revert', 'reverted', 'reverting', 'cherry', 'pick', 'picked', 'picking', 'bisect', 'bisected', 'bisecting', 'blame', 'blamed', 'blaming', 'log', 'logged', 'logging', 'diff', 'diffed', 'diffing', 'status', 'add', 'added', 'adding', 'rm', 'removed', 'removing', 'mv', 'moved', 'moving', 'cp', 'copied', 'copying', 'cat', 'showed', 'showing', 'less', 'more', 'most', 'least', 'many', 'much', 'few', 'little', 'some', 'any', 'no', 'not', 'nor', 'but', 'or', 'yet', 'so', 'for', 'nor', 'because', 'since', 'although', 'though', 'even', 'however', 'therefore', 'thus', 'hence', 'meanwhile', 'furthermore', 'moreover', 'nevertheless', 'nonetheless', 'instead', 'else', 'rather', 'whether', 'while', 'whereas', 'unless', 'until', 'once', 'since', 'before', 'after', 'during', 'about', 'above', 'below', 'between', 'among', 'through', 'across', 'into', 'onto', 'toward', 'from', 'to', 'up', 'down', 'out', 'in', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'both', 'each', 'every', 'either', 'neither', 'any', 'some', 'such', 'no', 'only', 'own', 'same', 'than', 'too', 'very', 'just', 'now', 'then', 'well', 'also', 'back', 'even', 'still', 'ever', 'never', 'always', 'often', 'usually', 'sometimes', 'rarely', 'seldom', 'already', 'yet', 'ago', 'before', 'after', 'since', 'until', 'during', 'while', 'today', 'tomorrow', 'yesterday', 'nowadays', 'recently', 'lately', 'soon', 'immediately', 'right', 'directly', 'straight', 'quickly', 'slowly', 'fast', 'hard', 'soft', 'easy', 'difficult', 'simple', 'complex', 'clear', 'certain', 'sure', 'true', 'false', 'right', 'wrong', 'good', 'bad', 'better', 'worse', 'best', 'worst', 'first', 'last', 'next', 'previous', 'early', 'late', 'new', 'old', 'young', 'big', 'small', 'large', 'little', 'high', 'low', 'long', 'short', 'far', 'near', 'deep', 'shallow', 'wide', 'narrow', 'strong', 'weak', 'heavy', 'light', 'dark', 'bright', 'hot', 'cold', 'warm', 'cool', 'clean', 'dirty', 'fresh', 'stale', 'empty', 'full', 'open', 'closed', 'tight', 'loose', 'smooth', 'rough', 'sharp', 'dull', 'thick', 'thin', 'rich', 'poor', 'expensive', 'cheap', 'valuable', 'worthless', 'useful', 'useless', 'helpful', 'harmful', 'safe', 'dangerous', 'secure', 'insecure', 'stable', 'unstable', 'certain', 'uncertain', 'possible', 'impossible', 'probable', 'improbable', 'likely', 'unlikely', 'actual', 'virtual', 'real', 'imaginary', 'physical', 'mental', 'emotional', 'rational', 'irrational', 'logical', 'illogical', 'reasonable', 'unreasonable', 'fair', 'unfair', 'just', 'unjust', 'legal', 'illegal', 'proper', 'improper', 'correct', 'incorrect', 'accurate', 'inaccurate', 'exact', 'approximate', 'precise', 'imprecise', 'definite', 'indefinite', 'specific', 'general', 'particular', 'universal', 'local', 'global', 'national', 'international', 'public', 'private', 'personal', 'impersonal', 'formal', 'informal', 'official', 'unofficial', 'regular', 'irregular', 'normal', 'abnormal', 'typical', 'atypical', 'standard', 'nonstandard', 'customary', 'uncustomary', 'traditional', 'nontraditional', 'conventional', 'unconventional', 'modern', 'ancient', 'contemporary', 'outdated', 'current', 'former', 'latter', 'recent', 'former', 'future', 'past', 'present', 'initial', 'final', 'original', 'copy', 'authentic', 'fake', 'genuine', 'false', 'true', 'valid', 'invalid', 'legal', 'illegal', 'permitted', 'forbidden', 'allowed', 'prohibited', 'possible', 'impossible', 'available', 'unavailable', 'accessible', 'inaccessible', 'reachable', 'unreachable', 'visible', 'invisible', 'detectable', 'undetectable', 'noticeable', 'unnoticeable', 'obvious', 'obscure', 'clear', 'unclear', 'obvious', 'ambiguous', 'definite', 'vague', 'explicit', 'implicit', 'direct', 'indirect', 'straightforward', 'complicated', 'simple', 'complex', 'easy', 'difficult', 'hard', 'soft', 'smooth', 'rough', 'even', 'uneven', 'flat', 'curved', 'straight', 'crooked', 'level', 'sloped', 'uphill', 'downhill', 'upward', 'downward', 'forward', 'backward', 'inward', 'outward', 'upstream', 'downstream', 'upwind', 'downwind', 'upriver', 'downriver', 'upmarket', 'downmarket', 'upfront', 'backhanded', 'upbeat', 'downbeat', 'upbeat', 'downcast', 'upfront', 'underhanded', 'upper', 'lower', 'higher', 'bottom', 'top', 'middle', 'center', 'edge', 'corner', 'side', 'end', 'beginning', 'start', 'finish', 'complete', 'partial', 'whole', 'fraction', 'part', 'piece', 'section', 'segment', 'portion', 'share', 'bit', 'piece', 'chunk', 'block', 'segment', 'unit', 'item', 'element', 'component', 'factor', 'aspect', 'feature', 'characteristic', 'property', 'attribute', 'quality', 'quantity', 'amount', 'number', 'figure', 'statistic', 'data', 'information', 'knowledge', 'wisdom', 'insight', 'understanding', 'comprehension', 'perception', 'awareness', 'consciousness', 'mind', 'brain', 'thought', 'idea', 'concept', 'notion', 'belief', 'opinion', 'view', 'perspective', 'angle', 'approach', 'method', 'way', 'means', 'method', 'technique', 'procedure', 'process', 'system', 'framework', 'structure', 'organization', 'arrangement', 'order', 'sequence', 'series', 'chain', 'link', 'connection', 'relation', 'relationship', 'association', 'similarity', 'difference', 'contrast', 'comparison', 'analogy', 'metaphor', 'symbol', 'sign', 'signal', 'indicator', 'marker', 'flag', 'label', 'tag', 'name', 'term', 'word', 'phrase', 'sentence', 'statement', 'remark', 'comment', 'observation', 'note', 'point', 'issue', 'matter', 'subject', 'topic', 'theme', 'theme', 'thread', 'discussion', 'conversation', 'dialogue', 'debate', 'argument', 'dispute', 'conflict', 'war', 'battle', 'fight', 'struggle', 'challenge', 'problem', 'trouble', 'difficulty', 'issue', 'concern', 'worry', 'anxiety', 'fear', 'dread', 'panic', 'alarm', 'emergency', 'crisis', 'disaster', 'catastrophe', 'tragedy', 'calamity', 'misfortune', 'setback', 'obstacle', 'barrier', 'hurdle', 'block', 'blockage', 'stoppage', 'halt', 'pause', 'break', 'interval', 'space', 'gap', 'distance', 'length', 'width', 'height', 'depth', 'size', 'scale', 'scope', 'range', 'extent', 'degree', 'level', 'stage', 'phase', 'step', 'level', 'rank', 'grade', 'class', 'category', 'type', 'kind', 'sort', 'variety', 'form', 'shape', 'figure', 'configuration', 'layout', 'design', 'plan', 'scheme', 'strategy', 'tactic', 'policy', 'rule', 'law', 'principle', 'guideline', 'standard', 'criterion', 'measure', 'measurement', 'dimension', 'factor', 'element', 'component', 'ingredient', 'part', 'piece', 'section', 'segment', 'fraction', 'portion', 'share', 'bit', 'piece', 'chunk', 'block', 'segment', 'unit', 'item', 'element', 'component', 'factor', 'aspect', 'feature', 'characteristic', 'property', 'attribute', 'quality', 'quantity', 'amount', 'number', 'figure', 'statistic', 'data', 'information', 'knowledge', 'wisdom', 'insight', 'understanding', 'comprehension', 'perception', 'awareness', 'consciousness', 'mind', 'brain', 'thought', 'idea', 'concept', 'notion', 'belief', 'opinion', 'view', 'perspective', 'angle', 'approach', 'method', 'way', 'means', 'method', 'technique', 'procedure', 'process', 'system', 'framework', 'structure', 'organization', 'arrangement', 'order', 'sequence', 'series', 'chain', 'link', 'connection', 'relation', 'relationship', 'association', 'similarity', 'difference', 'contrast', 'comparison', 'analogy', 'metaphor', 'symbol', 'sign', 'signal', 'indicator', 'marker', 'flag', 'label', 'tag', 'name', 'term', 'word', 'phrase', 'sentence', 'statement', 'remark', 'comment', 'observation', 'note', 'point', 'issue', 'matter', 'subject', 'topic', 'theme', 'thread', 'discussion', 'conversation', 'dialogue', 'debate', 'argument', 'dispute', 'conflict'}
filtered_words = [w for w in words if w not in stop_words and len(w) > 2]
word_freq = Counter(filtered_words)
print()
print('Top 15 keywords:')
for word, count in word_freq.most_common(15):
    print(f"  {word}: {count}")

# Engagement metrics
total_upvotes = sum(c['score'] for c in real_comments)
avg_upvotes = total_upvotes / len(real_comments)
print()
print(f"Total upvotes: {total_upvotes}")
print(f"Average upvotes per comment: {avg_upvotes:.1f}")

# Top contributing users
user_comment_count = Counter(c['author'] for c in real_comments)
user_upvotes = Counter()
for c in real_comments:
    user_upvotes[c['author']] += c['score']
print()
print('Top users by comment count:')
for user, count in user_comment_count.most_common(5):
    print(f"  {user}: {count} comments, {user_upvotes[user]} upvotes")
print()
print('Top users by upvotes:')
for user, upvotes in user_upvotes.most_common(5):
    print(f"  {user}: {upvotes} upvotes, {user_comment_count[user]} comments")
