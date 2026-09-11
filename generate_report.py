#!/usr/bin/env python3
import json
import re
from collections import Counter

with open('/workspace/0a976afa-9d91-494d-85d2-5832b5541cb3/sessions/agent_0083bca8-f4c0-4f11-b7af-9ca7124132ea/data/1w5l8bw/flat.json') as f:
    comments = json.load(f)

real_comments = [c for c in comments if c.get('body') != '[deleted]']

mapping = {
    0: "Community & Moderation", 1: "Meta/Zuck & Competitive Landscape", 2: "Meta/Zuck & Competitive Landscape",
    3: "Benchmark Skepticism & Performance", 4: "Benchmark Skepticism & Performance", 5: "Release Timing & Open Weights",
    6: "Release Timing & Open Weights", 7: "Benchmark Skepticism & Performance", 8: "Benchmark Skepticism & Performance",
    9: "Benchmark Skepticism & Performance", 10: "Benchmark Skepticism & Performance", 11: "Benchmark Skepticism & Performance",
    12: "Benchmark Skepticism & Performance", 13: "Meta/Zuck & Competitive Landscape", 14: "Meta/Zuck & Competitive Landscape",
    15: "Meta/Zuck & Competitive Landscape", 16: "Meta/Zuck & Competitive Landscape", 17: "Meta/Zuck & Competitive Landscape",
    18: "Meta/Zuck & Competitive Landscape", 19: "Meta/Zuck & Competitive Landscape", 20: "Meta/Zuck & Competitive Landscape",
    21: "Meta/Zuck & Competitive Landscape", 22: "Meta/Zuck & Competitive Landscape", 23: "Meta/Zuck & Competitive Landscape",
    24: "Meta/Zuck & Competitive Landscape", 25: "Meta/Zuck & Competitive Landscape", 26: "Meta/Zuck & Competitive Landscape",
    27: "Meta/Zuck & Competitive Landscape", 28: "Model Specs, Size & Hardware", 29: "Meta/Zuck & Competitive Landscape",
    30: "Meta/Zuck & Competitive Landscape", 31: "Meta/Zuck & Competitive Landscape", 32: "Meta/Zuck & Competitive Landscape",
    33: "Meta/Zuck & Competitive Landscape", 34: "Meta/Zuck & Competitive Landscape", 35: "Meta/Zuck & Competitive Landscape",
    36: "Meta/Zuck & Competitive Landscape", 37: "Meta/Zuck & Competitive Landscape", 38: "Benchmark Skepticism & Performance",
    39: "Meta/Zuck & Competitive Landscape", 40: "Meta/Zuck & Competitive Landscape", 41: "Meta/Zuck & Competitive Landscape",
    42: "Meta/Zuck & Competitive Landscape", 43: "Meta/Zuck & Competitive Landscape", 44: "Benchmark Skepticism & Performance",
    45: "Benchmark Skepticism & Performance", 46: "Benchmark Skepticism & Performance", 47: "Benchmark Skepticism & Performance",
    48: "Benchmark Skepticism & Performance", 49: "Model Specs, Size & Hardware", 50: "Model Specs, Size & Hardware",
    51: "Model Specs, Size & Hardware", 52: "Benchmark Skepticism & Performance", 53: "Benchmark Skepticism & Performance",
    54: "Benchmark Skepticism & Performance", 55: "Model Specs, Size & Hardware", 56: "Model Specs, Size & Hardware",
    57: "Model Specs, Size & Hardware", 58: "Model Specs, Size & Hardware", 59: "Model Specs, Size & Hardware",
    60: "Release Timing & Open Weights", 61: "Release Timing & Open Weights", 62: "Release Timing & Open Weights",
    63: "Release Timing & Open Weights", 64: "Release Timing & Open Weights", 65: "Release Timing & Open Weights",
    66: "Release Timing & Open Weights", 67: "Release Timing & Open Weights", 68: "Release Timing & Open Weights",
    69: "Release Timing & Open Weights", 70: "Muse/Glimmer Model Discussion", 71: "Muse/Glimmer Model Discussion",
    72: "Muse/Glimmer Model Discussion", 73: "Muse/Glimmer Model Discussion", 74: "Muse/Glimmer Model Discussion",
    75: "Muse/Glimmer Model Discussion", 76: "Muse/Glimmer Model Discussion", 77: "Muse/Glimmer Model Discussion",
    78: "Muse/Glimmer Model Discussion", 79: "Muse/Glimmer Model Discussion", 80: "Muse/Glimmer Model Discussion",
    81: "Muse/Glimmer Model Discussion", 82: "Muse/Glimmer Model Discussion", 83: "Muse/Glimmer Model Discussion",
    84: "Muse/Glimmer Model Discussion", 85: "Muse/Glimmer Model Discussion", 86: "Muse/Glimmer Model Discussion",
    87: "Muse/Glimmer Model Discussion", 88: "Muse/Glimmer Model Discussion", 89: "Muse/Glimmer Model Discussion",
    90: "Muse/Glimmer Model Discussion", 91: "Muse/Glimmer Model Discussion", 92: "Muse/Glimmer Model Discussion",
    93: "Muse/Glimmer Model Discussion", 94: "Muse/Glimmer Model Discussion", 95: "Muse/Glimmer Model Discussion",
    96: "Muse/Glimmer Model Discussion", 97: "Muse/Glimmer Model Discussion", 98: "Muse/Glimmer Model Discussion",
    99: "Muse/Glimmer Model Discussion", 100: "Muse/Glimmer Model Discussion", 101: "Muse/Glimmer Model Discussion",
    102: "Benchmark Skepticism & Performance", 103: "Meta/Zuck & Competitive Landscape", 104: "Meta/Zuck & Competitive Landscape",
    105: "Meta/Zuck & Competitive Landscape", 106: "Meta/Zuck & Competitive Landscape", 107: "Meta/Zuck & Competitive Landscape",
    108: "Meta/Zuck & Competitive Landscape", 109: "Meta/Zuck & Competitive Landscape", 110: "Meta/Zuck & Competitive Landscape",
    111: "Meta/Zuck & Competitive Landscape", 112: "Meta/Zuck & Competitive Landscape", 113: "Meta/Zuck & Competitive Landscape",
    114: "Meta/Zuck & Competitive Landscape", 115: "Release Timing & Open Weights", 116: "Model Specs, Size & Hardware",
    117: "Model Specs, Size & Hardware", 118: "Meta/Zuck & Competitive Landscape", 119: "Meta/Zuck & Competitive Landscape",
    120: "Release Timing & Open Weights", 121: "Release Timing & Open Weights", 122: "Release Timing & Open Weights",
    123: "Release Timing & Open Weights", 124: "Release Timing & Open Weights", 125: "Release Timing & Open Weights",
    126: "Muse/Glimmer Model Discussion", 127: "Muse/Glimmer Model Discussion", 128: "Muse/Glimmer Model Discussion",
    129: "Muse/Glimmer Model Discussion", 130: "Muse/Glimmer Model Discussion", 131: "Release Timing & Open Weights",
    132: "Release Timing & Open Weights", 133: "Release Timing & Open Weights", 134: "Release Timing & Open Weights",
    135: "Release Timing & Open Weights", 136: "Muse/Glimmer Model Discussion", 137: "Muse/Glimmer Model Discussion",
    138: "Model Specs, Size & Hardware", 139: "Model Specs, Size & Hardware", 140: "Model Specs, Size & Hardware",
    141: "Model Specs, Size & Hardware", 142: "Model Specs, Size & Hardware", 143: "Model Specs, Size & Hardware",
    144: "Model Specs, Size & Hardware", 145: "Model Specs, Size & Hardware", 146: "Model Specs, Size & Hardware",
    147: "Muse/Glimmer Model Discussion", 148: "Meta/Zuck & Competitive Landscape", 149: "Meta/Zuck & Competitive Landscape",
    150: "Meta/Zuck & Competitive Landscape", 151: "Model Specs, Size & Hardware", 152: "Muse/Glimmer Model Discussion",
    153: "Release Timing & Open Weights", 154: "Release Timing & Open Weights", 155: "Release Timing & Open Weights",
    156: "Meta/Zuck & Competitive Landscape", 157: "Community & Moderation", 158: "Muse/Glimmer Model Discussion",
    159: "Muse/Glimmer Model Discussion", 160: "Muse/Glimmer Model Discussion", 161: "Muse/Glimmer Model Discussion",
    162: "Muse/Glimmer Model Discussion", 163: "Muse/Glimmer Model Discussion", 164: "Muse/Glimmer Model Discussion",
    165: "Muse/Glimmer Model Discussion", 166: "Muse/Glimmer Model Discussion", 167: "Model Specs, Size & Hardware",
    168: "Benchmark Skepticism & Performance", 169: "Model Specs, Size & Hardware", 170: "Model Specs, Size & Hardware",
    171: "Model Specs, Size & Hardware", 172: "Model Specs, Size & Hardware", 173: "Benchmark Skepticism & Performance",
    174: "Model Specs, Size & Hardware", 175: "Model Specs, Size & Hardware", 176: "Meta/Zuck & Competitive Landscape",
    177: "Model Specs, Size & Hardware", 178: "Release Timing & Open Weights", 179: "Muse/Glimmer Model Discussion",
    180: "Model Specs, Size & Hardware", 181: "Benchmark Skepticism & Performance", 182: "Benchmark Skepticism & Performance",
    183: "Model Specs, Size & Hardware", 184: "Meta/Zuck & Competitive Landscape", 185: "Meta/Zuck & Competitive Landscape",
    186: "Release Timing & Open Weights", 187: "Benchmark Skepticism & Performance", 188: "Benchmark Skepticism & Performance",
    189: "Community & Moderation", 190: "Release Timing & Open Weights", 191: "Community & Moderation",
    192: "Community & Moderation",
}

cluster_assignments = [mapping[i] for i in range(193)]

positive_words = set([
    'good', 'great', 'awesome', 'excellent', 'amazing', 'love', 'best', 'fantastic', 'wonderful',
    'happy', 'excited', 'impressive', 'cool', 'nice', 'decent', 'superior', 'fast', 'accurate',
    'hope', 'finally', 'respect', 'better', 'worth', 'glad', 'pleased', 'solid', 'strong',
    'promising', 'underrated', 'overlooked', 'superb', 'outstanding', 'sota', 'frontier',
    'back', 'rejoined', 'good name', 'unironically', 'cooked', 'let\'s go', 'hype',
    'damn good', 'pretty good', 'far superior', 'decent amount', 'set the frontier',
    'officially a sota', 'rejoined the race', 'accurate and fast', 'blazing fast',
    'extremely competent', 'very interesting', 'pretty damn', 'damn good for benchmarks'
])

negative_words = set([
    'bad', 'terrible', 'awful', 'worst', 'hate', 'horrible', 'disappointing', 'slow', 'lazy',
    'garbage', 'nerfed', 'useless', 'sucks', 'mediocre', 'dogshit', 'stupid', 'sloppy', 'overkill',
    'boring', 'annoying', 'suspicious', 'sus', 'not convinced', "don't care", "don't believe",
    'too big', 'broke', 'expensive', 'pricier', 'greedy', 'afraid', 'can\'t afford',
    'nerfed to the max', 'useless crap', 'won\'t have', 'can\'t run', 'too big for me',
    'hard to understand', 'not a fan', 'caveman like', 'sloppy uis', 'dislike', 'not impressed',
    'not right', 'not okay', 'absolute dogshit', 'pretty damn mediocre', 'terrible people',
    'awful things', 'lazy model', 'stupid lazy', 'brain damaged', 'shill', 'garbage',
    'not useful', 'pretty shit', 'absolute dogshit', 'nerfed to the max', 'soon shit',
    'not really care', 'not a fan of', 'not believe', 'terrible'
])

negations = set(['not', "n't", 'no', 'never', 'neither', 'nor', 'barely', 'hardly', 'scarcely'])

def simple_sentiment(text):
    if 'I am a bot' in text or '[deleted]' in text:
        return 'neutral'
    if text.strip() in ['Woah damn gang,thats crazy', 'Training_Rip_8901'] or 'grug given rock' in text:
        return 'neutral'
    if text.strip() == '👀':
        return 'neutral'
    if text.strip() == 'Intifada':
        return 'neutral'
    if text.strip() == 'Fuck ya :)':
        return 'positive'
    if 'Are we sure' in text or 'Didn\'t Zuck say' in text or 'Don\'t believe' in text or 'Now if only i could run it' in text:
        return 'neutral'
    if 'I am not really a fan' in text:
        return 'neutral'
    
    text_lower = text.lower()
    words = re.findall(r'\b\w+\b', text_lower)
    
    pos_count = 0
    neg_count = 0
    
    for i, w in enumerate(words):
        is_negated = i > 0 and words[i-1] in negations
        if w in positive_words:
            if is_negated:
                neg_count += 1
            else:
                pos_count += 1
        elif w in negative_words:
            if is_negated:
                pos_count += 1
            else:
                neg_count += 1
    
    pos_phrases = ['pretty damn good', 'damn good', 'really good', 'so good', 'great to see',
                   'pretty good', 'best instruct', 'far superior', 'decent amount', 'set the frontier',
                   'officially a sota', 'rejoined the race', 'good name', 'unironically good',
                   'you cooked', 'let\'s go', 'hype will', 'damn good for benchmarks',
                   'accurate and fast', 'blazing fast', 'extremely competent', 'very interesting',
                   'pretty damn', 'great to see more']
    neg_phrases = ["don't believe", 'not convinced', 'not okay', 'absolute dogshit',
                   'pretty damn mediocre', 'terrible people', 'nerfed to the max', 'useless crap',
                   "don't care", "won't have", "can't run", 'too big for me', 'too big',
                   'hard to understand', 'not a fan', 'caveman like', 'sloppy uis', 'dislike',
                   'not impressed', 'not right', 'not okay', 'not really care', 'not a fan of',
                   'lazy model', 'stupid lazy', 'brain damaged', 'shill comments', 'garbage',
                   'not useful', 'pretty shit', 'absolute dogshit', 'nerfed to the max',
                   'soon shit', 'not believe', 'terrible']
    
    for phrase in pos_phrases:
        if phrase in text_lower:
            pos_count += 2
    for phrase in neg_phrases:
        if phrase in text_lower:
            neg_count += 2
    
    if '👀' in text or 'Hype' in text or 'Let\'s go' in text or 'You cooked' in text:
        pos_count += 1
    
    if pos_count > neg_count:
        return 'positive'
    elif neg_count > pos_count:
        return 'negative'
    else:
        return 'neutral'

# Build cluster data
cluster_data = {}
for cluster in set(cluster_assignments):
    cluster_data[cluster] = {'comments': [], 'scores': [], 'sentiments': []}

for idx, (c, cluster) in enumerate(zip(real_comments, cluster_assignments)):
    sentiment = simple_sentiment(c['body'])
    cluster_data[cluster]['comments'].append(c)
    cluster_data[cluster]['scores'].append(c['score'])
    cluster_data[cluster]['sentiments'].append(sentiment)

# Keywords
stop_words = set(['the', 'a', 'an', 'is', 'are', 'was', 'were', 'be', 'been', 'being',
                  'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should',
                  'may', 'might', 'shall', 'can', 'to', 'of', 'in', 'for', 'on', 'with', 'at',
                  'by', 'from', 'up', 'about', 'into', 'through', 'during', 'before', 'after',
                  'above', 'below', 'between', 'out', 'off', 'over', 'under', 'again', 'further',
                  'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'both',
                  'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not',
                  'only', 'own', 'same', 'so', 'than', 'too', 'very', 'just', 'because', 'but',
                  'and', 'or', 'if', 'while', 'that', 'this', 'it', 'its', 'they', 'them',
                  'their', 'what', 'which', 'who', 'whom', 'these', 'those', 'am', 'i', 'me',
                  'my', 'myself', 'we', 'our', 'ours', 'you', 'your', 'yours', 'he', 'him',
                  'his', 'she', 'her', 'hers', 'its', 'its', 'we', 'us', 'our', 'ours',
                  'they', 'them', 'their', 'theirs', 'what', 'which', 'who', 'whom', 'this',
                  'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been',
                  'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a',
                  'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while',
                  'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into',
                  'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from',
                  'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further',
                  'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all',
                  'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such',
                  'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very',
                  's', 't', 'just', 'don', 'now', 'also', 'like', 'get', 'got', 'think',
                  'know', 'see', 'way', 'many', 'much', 'well', 'back', 'even', 'still',
                  'new', 'one', 'two', 'make', 'made', 'really', 'thing', 'things', 'look',
                  'yeah', 'yes', 'oh', 'hey', 'lol', 'lmfao', 'fuck', 'shit', 'damn',
                  'pretty', 'quite', 'rather', 'enough', 'almost', 'enough', 'able', 'ever',
                  'every', 'everywhere', 'everyone', 'everything', 'something', 'nothing',
                  'anyone', 'anybody', 'anywhere', 'anyhow', 'anyway', 'anyways', 'however',
                  'whatever', 'whenever', 'wherever', 'however', 'moreover', 'furthermore',
                  'nevertheless', 'nonetheless', 'otherwise', 'instead', 'else', 'elsewhere',
                  'meanwhile', 'therefore', 'thus', 'hence', 'meanwhile', 'likewise', 'similarly',
                  'accordingly', 'consequently', 'otherwise', 'instead', 'rather', 'preferably',
                  'maybe', 'perhaps', 'possibly', 'probably', 'certainly', 'definitely',
                  'absolutely', 'totally', 'completely', 'entirely', 'utterly', 'hardly',
                  'scarcely', 'barely', 'almost', 'nearly', 'virtually', 'practically',
                  'basically', 'essentially', 'fundamentally', 'actually', 'in fact', 'as a matter of fact',
                  'first', 'second', 'third', 'finally', 'last', 'next', 'previous', 'early', 'late',
                  'today', 'tomorrow', 'yesterday', 'now', 'soon', 'later', 'already', 'yet',
                  'ago', 'before', 'after', 'since', 'until', 'during', 'while', 'when',
                  'whenever', 'while', 'whereas', 'wherever', 'though', 'although', 'even though',
                  'despite', 'in spite of', 'rather than', 'whether', 'either', 'neither',
                  'both', 'nor', 'yet', 'so', 'therefore', 'thus', 'meanwhile', 'otherwise',
                  'instead', 'rather', 'instead of', 'apart from', 'aside from', 'except',
                  'except for', 'besides', 'moreover', 'furthermore', 'likewise', 'similarly',
                  'accordingly', 'consequently', 'meanwhile', 'nevertheless', 'nonetheless',
                  'anyway', 'anyhow', 'anyway', 'anyhow', 'anyway', 'regardless', 'http', 'https',
                  'www', 'com', 'redd', 'preview', 'redd', 'format', 'auto', 'webp', 'width',
                  'height', 'png', 'jpg', 'jpeg', 'gif', 'svg', 'css', 'html', 'javascript',
                  'js', 'py', 'java', 'c', 'cpp', 'h', 'hpp', 'cs', 'go', 'rs', 'rb', 'php',
                  'swift', 'kt', 'kts', 'scala', 'sc', 'sql', 'r', 'm', 'mm', 'sh', 'bash',
                  'zsh', 'fish', 'ps1', 'bat', 'cmd', 'vbs', 'js', 'ts', 'jsx', 'tsx', 'vue',
                  'svelte', 'elm', 'clj', 'cljs', 'cljc', 'edn', 'lisp', 'el', 'lfe', 'erl',
                  'hrl', 'ex', 'exs', 'eex', 'heex', 'leex', 'slime', 'fasl', 'lsp', 'asd',
                  'ros', 'rdoc', 'md', 'markdown', 'txt', 'text', 'csv', 'tsv', 'json', 'xml',
                  'yaml', 'yml', 'toml', 'ini', 'cfg', 'conf', 'config', 'env', 'gitignore',
                  'dockerignore', 'editorconfig', 'prettierrc', 'eslintrc', 'babelrc', 'npmrc',
                  'yarnrc', 'pipfile', 'poetry', 'lock', 'gemspec', 'cargo', 'package',
                  'requirements', 'gemfile', 'makefile', 'cmake', 'mk', 'mak', 'am', 'in',
                  'ac', 'm4', 'autoconf', 'automake', 'libtool', 'ltmain', 'libtoolize',
                  'autoupdate', 'autoheader', 'autoscan', 'ifnames', 'aclocal', 'aclocal',
                  'config', 'h', 'config', 'h', 'in', 'config', 'log', 'config', 'status',
                  'configure', 'makefile', 'in', 'makefile', 'am', 'stamp', 'h1', 'stamp',
                  'h2', 'stamp', 'h3', 'stamp', 'h4', 'stamp', 'h5', 'stamp', 'h6', 'stamp',
                  'h7', 'stamp', 'h8', 'stamp', 'h9', 'stamp', 'h10'
])

all_text = ' '.join(c['body'] for c in real_comments)
words = re.findall(r'\b[a-z]{3,}\b', all_text.lower())
filtered_words = [w for w in words if w not in stop_words]
word_freq = Counter(filtered_words)
top_keywords = [word for word, count in word_freq.most_common(15)]

# Engagement metrics
all_scores = [c['score'] for c in real_comments]
total_upvotes = sum(all_scores)
avg_score = total_upvotes / len(all_scores)

# Top comments by threshold buckets
buckets = [
    (100, float('inf'), "100+"),
    (50, 99, "50+"),
    (20, 49, "20+"),
    (10, 19, "10+"),
]

def get_top_comment_for_bucket(min_score, max_score, bucket_label):
    candidates = [(c, c['score']) for c in real_comments if min_score <= c['score'] <= max_score]
    if not candidates:
        return None
    candidates.sort(key=lambda x: x[1], reverse=True)
    return candidates[0][0]

top_comments = []
for min_s, max_s, label in buckets:
    top = get_top_comment_for_bucket(min_s, max_s, label)
    if top and top['score'] >= 10:
        top_comments.append((label, top))

# Sentiment totals
all_sentiments = [simple_sentiment(c['body']) for c in real_comments]
sent_counts = Counter(all_sentiments)
total = len(all_sentiments)
pos_pct = sent_counts.get('positive', 0) / total * 100
neu_pct = sent_counts.get('neutral', 0) / total * 100
neg_pct = sent_counts.get('negative', 0) / total * 100

# Generate markdown
md = []
md.append("# REDDIT POST ANALYSIS\n")

md.append("A Reddit post in r/LocalLLaMA announced that Meta's Muse Spark model is getting open weights soon, sparking a massive discussion with 193 comments and over 2,200 upvotes. The original poster noted they are \"still waiting for Llama 5\" because \"Muse Spark will be too big for me, or just something between Glimmer and Spark.\" Commenters immediately debated whether Muse Spark's impressive benchmark scores are legitimate or just \"benchmaxxed,\" with one user pointing out that \"When a model does well in benchmarks but then fails to live up in real life coding and other tasks.\" Many users praised the smaller Muse Glimmer model as \"pretty good, very much overlooked\" and \"superior to Qwen 3.8:27b for non-coding tasks,\" while others worried about whether they could actually run Muse Spark on their home hardware. The thread also veered into jokes about Meta's codenames, with users noting the next model is called \"Watermelon\" and suggesting \"Metamelon\" as a better name.\n")

md.append("# REDDIT COMMENTS ANALYSIS\n")

cluster_order = [
    "Meta/Zuck & Competitive Landscape",
    "Muse/Glimmer Model Discussion",
    "Model Specs, Size & Hardware",
    "Release Timing & Open Weights",
    "Benchmark Skepticism & Performance",
    "Community & Moderation"
]

for cluster in cluster_order:
    data = cluster_data[cluster]
    count = len(data['comments'])
    total_score = sum(data['scores'])
    avg = total_score / count if count > 0 else 0
    sents = Counter(data['sentiments'])
    
    md.append(f"## {cluster} ({count} Comments - {total_score} Upvotes)\n")
    
    if cluster == "Meta/Zuck & Competitive Landscape":
        md.append("The largest cluster centered on Meta's positioning versus rivals like Anthropic, OpenAI, and Chinese labs. Users debated whether Meta has truly rejoined the frontier, with one claiming \"This latest iteration technically set the frontier. Meta is officially a SOTA lab again\" while another countered that \"there is no secret sauce\" and all labs are roughly on the same level. A side thread accused Anthropic of sitting on better models to drip-feed releases for IPO optics, with comments like \"Perhaps Anthropic can't afford to lower the api prices?\" and \"They want to IPO, they need the revenue projections.\"\n")
    elif cluster == "Muse/Glimmer Model Discussion":
        md.append("A strong contingent of users shared real-world experience with Muse Glimmer and Spark, praising Glimmer as \"pretty good, very much overlooked\" and noting it is \"far superior at reasoning with thinking turned off\" compared to Gemma. Several users reported switching from Qwen and Gemma to Muse because it is faster and less prone to overthinking, with one noting \"Muse is definitely faster. I recently switched away from Gemma to it as my model to run on a single GPU.\" Critics countered that Muse models are \"nerfed to the max\" and only useful for \"useless crap,\" while others asked why everyone is chasing coding when there is a gap for cheap, intelligent general-purpose models.\n")
    elif cluster == "Model Specs, Size & Hardware":
        md.append("Users intensely debated whether Muse Spark would fit on consumer hardware, with guesses ranging from \"a few hundred billion\" parameters to \"at least 2 trillion\" based on benchmark scores. Comments like \"if this fits on a DGX spark I will be so happy. If this only fits on 2 DGX spark I will be so broke\" captured the tension between excitement and affordability. Several users asked directly how many terabytes the model would be and whether it could run on 96GB or 512GB VRAM setups.\n")
    elif cluster == "Release Timing & Open Weights":
        md.append("Many users expressed frustration that Meta has been saying \"soon\" for months, with one bluntly stating \"They have been saying this soon shit from months\" while another pointed out that \"They promised Spark open weights when they announced Glimmer's release.\" Others defended the delay by noting Meta is releasing a new model every few weeks and that slow-cooking the model likely produced better results, citing OpenAI's rushed Llama 4 as a cautionary tale. A thread about Meta's fruit codenames generated jokes like \"Muse Twinkle\" and \"Metamelon\" before users clarified that Watermelon is the next frontier model after Avocado.\n")
    elif cluster == "Benchmark Skepticism & Performance":
        md.append("A skeptical cluster questioned whether Muse Spark's scores reflect real capability, with one user declaring \"Or benchmaxxes. I'm not convinced\" and another warning that \"When a model does well in benchmarks but then fails to live up in real life coding and other tasks.\" Several users suspected test-set training, noting it was \"a bit sus that they decided to report terminal bench 2.1, when 4 exists\" and that models trained on benchmark-style data can game narrow metrics like MRCR without gaining general ability. One user who tried Spark 1.2 reported it was \"pretty damn mediocre\" and \"extremely benchmaxxed\" based on a recent video review.\n")
    elif cluster == "Community & Moderation":
        md.append("A small cluster of meta-comments included a moderator bot announcement, a moderator note that the post was off-topic until weights were actually published, and playful banter about the thread's viral spread. One moderator wrote that \"Until such time that weights are published, this is off-topic for LocalLLaMA, but since nobody caught it before it gained 260 upvotes and 70+ comments, this post will stay up,\" while another user joked \"Where is your comment?\" after the moderator was called out for hypocrisy.\n")
    
    md.append("")

total_cluster_comments = sum(len(data['comments']) for data in cluster_data.values())
total_cluster_upvotes = sum(sum(data['scores']) for data in cluster_data.values())
md.append(f"(Total: {total_cluster_comments} Comments - {total_cluster_upvotes} Upvotes)\n")

md.append("# TOP COMMENTS\n")

for label, c in top_comments:
    permalink = f"https://reddit.com/r/LocalLLaMA/comments/1w5l8bw/muse_spark_open_weights_coming_soon/{c['id']}/"
    md.append(f"## {label}+ Upvotes\n")
    md.append(f"u/{c['author']}\n")
    md.append(f'"{c["body"]}" ({c["score"]} Upvotes) - {permalink}\n')

md.append("# ORIGINAL POST\n")
md.append('"I am still waiting for Llama 5, because Muse Spark will be too big for me, or just something between Glimmer and Spark"\n')
md.append("https://x.com/finkd/status/2095232032896946311\n")

report = ''.join(md)

with open('/workspace/0a976afa-9d91-494d-85d2-5832b5541cb3/sessions/agent_0083bca8-f4c0-4f11-b7af-9ca7124132ea/thread_1w5l8bw_analysis.md', 'w') as f:
    f.write(report)

print("Report written successfully!")
print(f"Total length: {len(report)} chars")
print(f"First 500 chars:\n{report[:500]}")
