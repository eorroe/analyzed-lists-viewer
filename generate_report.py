#!/usr/bin/env python3
"""Generate Reddit thread analysis report for j4x6ky."""

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
# CLUSTERING
# ============================================================

def classify_comment(body, author, comment_id):
    """Classify comment into thematic cluster."""
    body_lower = body.lower()
    
    # Comprehensive manual mapping based on content review
    special_cases = {
        # Religious Doctrinal
        'kx214km': 'religious_doctrinal',
        'kvgqnbi': 'religious_doctrinal',
        'kvp6tx4': 'religious_doctrinal',
        'kupu5os': 'religious_doctrinal',
        'Outrageous_Work_8291': 'religious_doctrinal',
        'Perfect-Landscape414': 'religious_doctrinal',
        'legokingnm': 'religious_doctrinal',
        'SocioDexter70': 'religious_doctrinal',
        'PlusIndividual1489': 'religious_doctrinal',
        'Tall_Efficiency1447': 'religious_doctrinal',
        'OMGYuKKi': 'religious_doctrinal',
        'Kraapzii': 'religious_doctrinal',
        'Ali-The-Conqurer': 'religious_doctrinal',
        'NeverKillAgain': 'religious_doctrinal',
        'indiacurious': 'religious_doctrinal',
        'Bluestorm717': 'religious_doctrinal',
        'No_Selection_9686': 'religious_doctrinal',
        'These-Percentage-632': 'religious_doctrinal',
        'Norfolk_Enchantz': 'religious_doctrinal',
        '117icarus': 'religious_doctrinal',
        'Zealousideal_Try6122': 'religious_doctrinal',
        'QuickSilver010': 'religious_doctrinal',
        'Alqatraz070': 'religious_doctrinal',
        'Snoo_80142': 'religious_doctrinal',
        'New-Feeling-5644': 'religious_doctrinal',
        'Round-Ad5063': 'religious_doctrinal',
        'Metho221': 'religious_doctrinal',
        'nichrigga101': 'religious_doctrinal',
        'EconomistPlus3522': 'religious_doctrinal',
        'LeastOfEvils': 'religious_doctrinal',
        'bia-visan720': 'religious_doctrinal',
        'MarsMonkey88': 'religious_doctrinal',
        'GoodDamage2000': 'religious_doctrinal',
        'Theblessedmother': 'religious_doctrinal',
        'bgd_bgd': 'religious_doctrinal',
        'Supermarket07': 'religious_doctrinal',
        'eepplesandbenenees': 'religious_doctrinal',
        'Background_Ad_371': 'religious_doctrinal',
        'indicasativagemini': 'religious_doctrinal',
        'SqaceFood': 'atheist_skeptical',
        'Ok-Inspector-287': 'religious_doctrinal',
        'R0yalCl4w': 'theological_defense',
        'Silly_Proposal_9185': 'theological_defense',
        'MasterBassion': 'theological_defense',
        'PoopSommelier': 'philosophical',
        'Big-Bodybuilder-7025': 'religious_doctrinal',
        'RamiRustom': 'atheist_skeptical',
        'drck--': 'religious_doctrinal',
        'Daytron2020': 'religious_doctrinal',
        'ZestyAppointment8519': 'religious_doctrinal',
        'Key-Fisherman-3606': 'religious_doctrinal',
        'Automatic_Signal_940': 'religious_doctrinal',
        'Concrete-Information8': 'religious_doctrinal',
        'V0lat1lestary': 'religious_doctrinal',
        'Local-Delivery-4757': 'religious_doctrinal',
        'UrbenNorm': 'religious_doctrinal',
        'National_Frame_8525': 'religious_doctrinal',
        'godthinksyouresmart': 'religious_doctrinal',
        'Bananaman9029': 'religious_doctrinal',
        'Chingachgook': 'religious_doctrinal',
        'One_Frosting_3279': 'religious_doctrinal',
        'ph_ameta': 'religious_doctrinal',
        'Real_Slim_Shady97': 'religious_doctrinal',
        'Gredranmor': 'religious_doctrinal',
        'CalligrapherIll3679': 'religious_doctrinal',
        'Hawkling2': 'religious_doctrinal',
        'Brutal-Bias': 'religious_doctrinal',
        'Brainy-Chain-2450': 'religious_doctrinal',
        'Pvrn': 'religious_doctrinal',
        'Outrageous_Ad_1604': 'religious_doctrinal',
        'Capital_Dog8719': 'religious_doctrinal',
        'Anonamoose78': 'religious_doctrinal',
        'Just_A_Redditor_56': 'religious_doctrinal',
        'Honest-Manufacturer3': 'religious_doctrinal',
        'Three_Purple_Scarfs': 'religious_doctrinal',
        'Yugen_Khan': 'religious_doctrinal',
        'BasketballGuy123': 'religious_doctrinal',
        'AmirioTheMuzzy': 'religious_doctrinal',
        'IntrepidOrchid': 'religious_doctrinal',
        'ismcanga': 'religious_doctrinal',
        'AllahAlmighty': 'religious_doctrinal',
        'HeadlessReptile': 'religious_doctrinal',
        'RedditDani97': 'religious_doctrinal',
        'A_Bruised_Reed': 'religious_doctrinal',
        '11finger11': 'religious_doctrinal',
        'Many-Rest': 'religious_doctrinal',
        'No_Mushroom7749': 'religious_doctrinal',
        'SaveEmail': 'religious_doctrinal',
        'PurpleDevilR': 'religious_doctrinal',
        'BrokeChristian': 'religious_doctrinal',
        'Thunderstarer': 'religious_doctrinal',
        'Taqwacore': 'religious_doctrinal',
        'exxcat': 'religious_doctrinal',
        'A_Bruised_Reed': 'religious_doctrinal',
        'Injured_Practice_377': 'religious_doctrinal',
        'Theosebes': 'religious_doctrinal',
        'angryDecipher': 'religious_doctrinal',
        'Fast-Sympathy5390': 'religious_doctrinal',
        'Atheist_Pro-Life': 'atheist_skeptical',
        'Taqwacore': 'religious_doctrinal',
        'InvisibleElf': 'religious_doctrinal',
        'A_Bruised_Reed': 'religious_doctrinal',
        'MuitoMaioria': 'religious_doctrinal',
        'Man_Who_Hates_Cats': 'atheist_skeptical',
        'TheMedic8888': 'religious_doctrinal',
        'UristMcRandom': 'religious_doctrinal',
        'Theflemishink': 'religious_doctrinal',
        'Strange-Effort-8503': 'religious_doctrinal',
        'onemansquest': 'theological_defense',
        'Senior-Firefighter67': 'theological_defense',
        'Falun_Dafa_Li': 'religious_doctrinal',
        'Electrical_Bar5184': 'atheist_skeptical',
        'bk19xsa': 'theological_defense',
        'Pamtookmyboyfriend': 'meta_debate',
        'Bsismyname01': 'atheist_skeptical',
        'Riskthecat': 'atheist_skeptical',
        'Bizarely27': 'atheist_skeptical',
        'LaserWang69': 'personal_experience',
        'Clear-Introduction-5': 'meta_debate',
        'chemist442': 'meta_debate',
        'Fun_Ad6732': 'meta_debate',
        'Pochez': 'philosophical',
        'Righteous_Allogenes': 'theological_defense',
        'chad1962': 'theological_defense',
        'Simon_Di_Tomasso': 'theological_defense',
        'WifeBeater3001': 'atheist_skeptical',
        'SuggestionEmergency2': 'philosophical',
        'SecretDevilsAdvocate': 'atheist_skeptical',
        'flashj007': 'atheist_skeptical',
        'Accomplished_Loan596': 'atheist_skeptical',
        '99_Gray_Ghost_99': 'religious_doctrinal',
        'deepestroy': 'philosophical',
        'Vast-Situation-6152': 'historical_comparative',
        'Asleep-Ad-6266': 'historical_comparative',
        'Prentice1996': 'meta_debate',
        'No_One_023': 'meta_debate',
        'thePantherT': 'atheist_skeptical',
        'lazpz786': 'theological_defense',
        'ExaminationVirtual12': 'theological_defense',
        'bob-weeaboo': 'philosophical',
        'Expert_Breadfruit698': 'philosophical',
        'vynepa': 'religious_doctrinal',
        'MelodicHeron9327': 'theological_defense',
        'RemoveOk9319': 'philosophical',
        'honglong1976': 'philosophical',
        'IMEGI007': 'religious_doctrinal',
        'CasualBrowseA': 'historical_comparative',
        'MentalHelpNeeded': 'personal_experience',
        'trippalip': 'theological_defense',
        'lovelyrain100': 'theological_defense',
        'suavestgrunt1': 'meta_debate',
        'Webbraham': 'philosophical',
        'GoodDamage2000': 'religious_doctrinal',
        'Difficult_Map_9762': 'atheist_skeptical',
        'Benito_Juarez5': 'atheist_skeptical',
        'Alert_Ad6239': 'religious_doctrinal',
        'manpagal': 'atheist_skeptical',
        'Christinamancini': 'meta_debate',
        'TyphonBeach': 'atheist_skeptical',
        'backpainbed': 'atheist_skeptical',
        'Fun_Maintenance_2667': 'historical_comparative',
        'gornstfonst': 'atheist_skeptical',
        'Etymolotas': 'philosophical',
        'Metho221': 'religious_doctrinal',
        'ZtheGreat': 'meta_debate',
        'Don_Alucard': 'philosophical',
        'Dianthe777': 'personal_experience',
        'NeverTheLateOne': 'meta_debate',
        'Pockmobileacc': 'meta_debate',
        'calamiso': 'meta_debate',
        'JD_2OOO': 'theological_defense',
        'Admirable_Yoghurt_50': 'historical_comparative',
        'LeastOfEvils': 'religious_doctrinal',
        'TheNotoriousN_Rod': 'meta_debate',
        'SecretDevilsAdvocate': 'atheist_skeptical',
        'Krenick_': 'meta_debate',
        'Simon_Di_Tomasso': 'theological_defense',
        'Pamtookmyboyfriend': 'meta_debate',
        'RichRocky': 'meta_debate',
        'sunpalm64': 'religious_doctrinal',
        'GijsHarbers2311': 'meta_debate',
        'Ok-Art9205': 'meta_debate',
        'Fun_Ad6732': 'meta_debate',
        'PjTheGotti6': 'meta_debate',
        'Futureinspiration-23': 'atheist_skeptical',
        'Legitimate_Grocery66': 'meta_debate',
        'Antisympathy': 'atheist_skeptical',
        'RedditFullOChildren': 'meta_debate',
        'bigbakedbean18181': 'meta_debate',  # preach brother
    }
    
    if comment_id in special_cases:
        return special_cases[comment_id]
    if author in special_cases:
        return special_cases[author]
    
    # Fallback: keyword-based
    scores = defaultdict(int)
    body_lower = body.lower()
    
    islam_keywords = ['islam', 'islamic', 'muslim', 'allah', 'quran', 'hadith', 'muhammad']
    christian_keywords = ['bible', 'christian', 'jesus', 'christ', 'gospel', 'scripture', 'biblical', 'heaven', 'hell', 'salvation', 'resurrection', 'catholic', 'protestant', 'acts 24:15', 'matthew', 'romans']
    jewish_keywords = ['judaism', 'jewish', 'torah', 'hebrew', 'monotheistic']
    doctrinal_keywords = ['doctrine', 'teaching', 'exception', 'pardoned', 'not punished', 'different judgement', 'separate test', 'opportunity', 'purified', 'chance to turn', 'will be tested', 'judged based on', 'never heard']
    
    religious_content = any(k in body_lower for k in islam_keywords + christian_keywords + jewish_keywords)
    exception_content = any(k in body_lower for k in doctrinal_keywords)
    
    if religious_content:
        scores['religious_doctrinal'] += 2
    if exception_content:
        scores['religious_doctrinal'] += 2
    
    atheist_keywords = ['atheist', 'atheism', 'not real', 'doesn\'t exist', 'myth', 'cult', 'nonsense', 'garbage', 'made up', 'fairy tale', 'no evidence', 'lack of evidence', 'doesn\'t show', 'hiding', 'shy']
    skeptical_keywords = ['question', 'doubt', 'skeptical', 'ridiculous', 'absurd', 'illogical', 'contradiction', 'doesn\'t make sense', 'makes no sense', 'doesn\'t answer', 'dodged', 'terrifying']
    
    if any(k in body_lower for k in atheist_keywords):
        scores['atheist_skeptical'] += 3
    if any(k in body_lower for k in skeptical_keywords):
        scores['atheist_skeptical'] += 1
    
    freewill_keywords = ['free will', 'freewill', 'choice', 'accountability', 'rebel', 'sin', 'satan', 'omnipotent', 'omniscient', 'justice', 'benevolent', 'grace', 'mercy']
    if any(k in body_lower for k in freewill_keywords):
        scores['theological_defense'] += 2
    
    historical_keywords = ['crusades', 'inquisition', 'forced conversion', 'history', 'historical', 'ancient', 'roman', 'medieval', 'spanish', 'nazi', 'hitler', 'holocaust', 'slavery', 'persecution']
    comparative_keywords = ['judaism', 'jewish', 'hindu', 'buddhism', 'monotheistic', 'abrahamic']
    
    if any(k in body_lower for k in historical_keywords):
        scores['historical_comparative'] += 3
    if any(k in body_lower for k in comparative_keywords) and not religious_content:
        scores['historical_comparative'] += 2
    
    personal_keywords = ['i was', 'i grew up', 'my family', 'my church', 'i experienced', 'i saw', 'i met', 'my story', 'i was abused', 'i prayed']
    if any(k in body_lower for k in personal_keywords):
        scores['personal_experience'] += 2
    
    meta_keywords = ['nice post', 'change my mind', 'op is', 'you are wrong', 'you are correct', 'this doesn\'t answer', 'you dodged', 'off topic', 'moderator', 'rule', 'removed', 'you didn\'t', 'you just', 'whole lot of nothing', 'makes no sense', 'your comment', 'your argument']
    if any(k in body_lower for k in meta_keywords):
        scores['meta_debate'] += 2
    
    philosophical_keywords = ['what if', 'imagine', 'suppose', 'consider', 'think about', 'question is', 'problem with', 'issue is', 'the problem', 'logic', 'logical', 'fair', 'unfair', 'implications']
    if any(k in body_lower for k in philosophical_keywords):
        scores['philosophical'] += 1
    
    if not scores:
        return 'other'
    
    best_cluster = max(scores, key=scores.get)
    return best_cluster

# Classify all comments
classifications = []
for c in real_comments:
    cluster = classify_comment(c['body'], c['author'], c['id'])
    classifications.append({
        'comment': c,
        'cluster': cluster,
    })

# Assign 5 unclassified to appropriate clusters
for item in classifications:
    if item['cluster'] == 'other':
        body_lower = item['comment']['body'].lower()
        if 'preach' in body_lower or 'fr man' in body_lower or 'glad to see' in body_lower:
            item['cluster'] = 'meta_debate'
        elif 'fantastic belief' in body_lower:
            item['cluster'] = 'atheist_skeptical'
        elif 'constitutes' in body_lower or 'effort' in body_lower:
            item['cluster'] = 'meta_debate'
        else:
            item['cluster'] = 'meta_debate'

# Final distribution
cluster_counts = Counter(c['cluster'] for c in classifications)
print("Final cluster distribution:")
for cluster, count in cluster_counts.most_common():
    print(f"  {cluster}: {count}")
print(f"Total: {sum(cluster_counts.values())}")

# Verify total
assert sum(cluster_counts.values()) == total_analyzed, f"Total mismatch: {sum(cluster_counts.values())} != {total_analyzed}"

# ============================================================
# SENTIMENT ANALYSIS
# ============================================================

def simple_sentiment(body):
    """Simple rule-based sentiment analysis."""
    body_lower = body.lower()
    
    positive_words = ['agree', 'correct', 'yes', 'good', 'great', 'true', 'love', 'beautiful', 'wonderful', 'amazing', 'fantastic', 'glad', 'happy', 'hope', 'faith', 'believe', 'trust', 'grace', 'mercy', 'forgive', 'salvation', 'heaven', 'paradise', 'blessed', 'thankful', 'appreciate', 'wonderful']
    negative_words = ['wrong', 'no', 'not', 'never', 'hate', 'bad', 'evil', 'terrible', 'horrible', 'awful', 'garbage', 'nonsense', 'myth', 'lie', 'false', 'contradiction', 'illogical', 'ridiculous', 'absurd', 'unfair', 'cruel', 'torture', 'hell', 'damn', 'punish', 'sin', 'rebel', 'fallen', 'problem', 'issue', 'question', 'doubt', 'skeptical', 'angry', 'mad', 'terrifying', 'disgust']
    
    pos_count = sum(1 for w in positive_words if w in body_lower)
    neg_count = sum(1 for w in negative_words if w in body_lower)
    
    # Neutral if very short or balanced
    if len(body.split()) < 5:
        return 'Neutral'
    
    if pos_count > neg_count:
        return 'Positive'
    elif neg_count > pos_count:
        return 'Negative'
    else:
        return 'Neutral'

sentiment_counts = Counter()
sentiment_by_cluster = defaultdict(Counter)

for item in classifications:
    sentiment = simple_sentiment(item['comment']['body'])
    sentiment_counts[sentiment] += 1
    sentiment_by_cluster[item['cluster']][sentiment] += 1

print("\nSentiment distribution:")
for s, c in sentiment_counts.most_common():
    print(f"  {s}: {c} ({c/total_analyzed*100:.1f}%)")

# ============================================================
# KEYWORD EXTRACTION
# ============================================================

def extract_keywords(comments, top_n=15):
    """Extract top keywords from comment bodies."""
    all_text = ' '.join(c['body'].lower() for c in comments)
    
    # Remove common stop words
    stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'from', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should', 'may', 'might', 'shall', 'can', 'need', 'dare', 'ought', 'used', 'it', 'its', 'this', 'that', 'these', 'those', 'i', 'you', 'he', 'she', 'we', 'they', 'me', 'him', 'her', 'us', 'them', 'my', 'your', 'his', 'its', 'our', 'their', 'mine', 'yours', 'hers', 'ours', 'theirs', 'who', 'whom', 'whose', 'which', 'what', 'where', 'when', 'why', 'how', 'all', 'each', 'every', 'both', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'not', 'only', 'same', 'so', 'than', 'too', 'very', 'just', 'because', 'as', 'until', 'while', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'up', 'down', 'out', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now', 'also', 'much', 'many', 'well', 'back', 'even', 'still', 'way', 'take', 'come', 'make', 'know', 'think', 'see', 'want', 'look', 'use', 'find', 'give', 'tell', 'work', 'call', 'try', 'ask', 'need', 'feel', 'become', 'leave', 'put', 'mean', 'keep', 'let', 'begin', 'seem', 'help', 'talk', 'turn', 'start', 'show', 'hear', 'play', 'run', 'live', 'believe', 'hold', 'bring', 'happen', 'write', 'provide', 'sit', 'stand', 'lose', 'pay', 'meet', 'include', 'continue', 'set', 'learn', 'change', 'lead', 'understand', 'watch', 'follow', 'stop', 'create', 'speak', 'read', 'allow', 'add', 'spend', 'grow', 'open', 'walk', 'win', 'offer', 'remember', 'love', 'consider', 'appear', 'buy', 'wait', 'serve', 'die', 'send', 'expect', 'build', 'stay', 'fall', 'cut', 'reach', 'kill', 'remain', 'real', 'post', 'comment', 'reddit', 'thread', 'user', 'people', 'person', 'thing', 'things', 'something', 'anything', 'everything', 'nothing', 'someone', 'anyone', 'everyone', 'no one', 'somebody', 'anybody', 'everybody', 'nobody', 'else', 'even', 'still', 'already', 'yet', 'ago', 'before', 'after', 'since', 'until', 'during', 'while', 'because', 'although', 'though', 'if', 'unless', 'whether', 'while', 'where', 'when', 'why', 'how', 'what', 'which', 'who', 'whom', 'whose', 'whether', 'either', 'neither', 'both', 'not', 'no', 'nor', 'neither', 'either', 'whether', 'rather', 'instead', 'else', 'otherwise', 'however', 'therefore', 'thus', 'hence', 'consequently', 'meanwhile', 'furthermore', 'moreover', 'additionally', 'likewise', 'similarly', 'conversely', 'instead', 'rather', 'otherwise', 'anyway', 'anyhow', 'anywhere', 'everywhere', 'nowhere', 'somewhere', 'anytime', 'everytime', 'sometimes', 'often', 'usually', 'always', 'never', 'rarely', 'seldom', 'frequently', 'occasionally', 'constantly', 'continuously', 'regularly', 'periodically', 'occasionally', 'once', 'twice', 'thrice', 'many', 'much', 'more', 'most', 'less', 'least', 'few', 'fewer', 'fewest', 'little', 'less', 'least', 'enough', 'plenty', 'sufficient', 'adequate', 'insufficient', 'deficient', 'lacking', 'abundant', 'ample', 'scarce', 'rare', 'unusual', 'common', 'ordinary', 'usual', 'typical', 'normal', 'standard', 'average', 'mediocre', 'exceptional', 'extraordinary', 'remarkable', 'notable', 'significant', 'important', 'crucial', 'critical', 'essential', 'vital', 'fundamental', 'basic', 'primary', 'principal', 'main', 'major', 'minor', 'secondary', 'subordinate', 'inferior', 'superior', 'higher', 'lower', 'upper', 'bottom', 'top', 'middle', 'center', 'side', 'edge', 'corner', 'point', 'line', 'curve', 'angle', 'circle', 'square', 'triangle', 'shape', 'form', 'figure', 'size', 'dimension', 'length', 'width', 'height', 'depth', 'volume', 'area', 'space', 'distance', 'time', 'date', 'year', 'month', 'week', 'day', 'hour', 'minute', 'second', 'moment', 'instant', 'period', 'duration', 'interval', 'frequency', 'rate', 'speed', 'velocity', 'acceleration', 'force', 'energy', 'power', 'work', 'heat', 'temperature', 'pressure', 'density', 'mass', 'weight', 'volume', 'capacity', 'amount', 'quantity', 'number', 'count', 'total', 'sum', 'average', 'mean', 'median', 'mode', 'range', 'variance', 'deviation', 'standard', 'normal', 'distribution', 'probability', 'chance', 'likelihood', 'possibility', 'potential', 'capability', 'ability', 'capacity', 'competence', 'skill', 'talent', 'gift', 'aptitude', 'genius', 'intelligence', 'wisdom', 'knowledge', 'information', 'data', 'fact', 'truth', 'reality', 'actual', 'actual', 'virtual', 'theoretical', 'practical', 'applied', 'abstract', 'concrete', 'specific', 'general', 'particular', 'individual', 'personal', 'private', 'public', 'social', 'political', 'economic', 'cultural', 'religious', 'spiritual', 'moral', 'ethical', 'legal', 'official', 'formal', 'informal', 'casual', 'proper', 'appropriate', 'suitable', 'acceptable', 'permissible', 'allowable', 'admissible', 'legitimate', 'valid', 'sound', 'reasonable', 'rational', 'logical', 'illogical', 'absurd', 'ridiculous', 'preposterous', 'ludicrous', 'laughable', 'foolish', 'silly', 'stupid', 'ignorant', 'naive', 'gullible', 'credulous', 'skeptical', 'doubtful', 'suspicious', 'questioning', 'incredulous', 'cynical', 'pessimistic', 'optimistic', 'hopeful', 'despairing', 'desperate', 'urgent', 'critical', 'emergency', 'crisis', 'disaster', 'catastrophe', 'calamity', 'tragedy', 'drama', 'comedy', 'farce', 'satire', 'parody', 'imitation', 'copy', 'replica', 'duplicate', 'original', 'authentic', 'genuine', 'real', 'actual', 'true', 'false', 'fake', 'artificial', 'synthetic', 'natural', 'organic', 'inorganic', 'chemical', 'physical', 'biological', 'psychological', 'mental', 'emotional', 'spiritual', 'intellectual', 'academic', 'scholarly', 'learned', 'educated', 'informed', 'aware', 'conscious', 'unconscious', 'subconscious', 'unaware', 'ignorant', 'uninformed', 'misinformed', 'misled', 'deceived', 'tricked', 'fooled', 'duped', 'cheated', 'swindled', 'robbed', 'stolen', 'taken', 'received', 'given', 'granted', 'bestowed', 'conferred', 'awarded', 'granted', 'denied', 'refused', 'rejected', 'accepted', 'approved', 'disapproved', 'condemned', 'criticized', 'praised', 'commended', 'admired', 'respected', 'honored', 'esteemed', 'regarded', 'considered', 'thought', 'believed', 'supposed', 'assumed', 'presumed', 'imagined', 'conceived', 'perceived', 'received', 'interpreted', 'understood', 'misunderstood', 'comprehended', 'grasped', 'apprehended', 'seized', 'captured', 'caught', 'trapped', 'ensnared', 'entangled', 'involved', 'engaged', 'committed', 'dedicated', 'devoted', 'loyal', 'faithful', 'true', 'false', 'faithless', 'treacherous', 'disloyal', 'unfaithful', 'infidel', 'heretic', 'apostate', 'renegade', 'traitor', 'betrayer', 'deceiver', 'liar', 'cheat', 'fraud', 'imposter', 'charlatan', 'phony', 'fake', 'false', 'fraudulent', 'deceptive', 'misleading', 'misdirecting', 'confusing', 'bewildering', 'perplexing', 'puzzling', 'confounding', 'baffling', 'mystifying', 'enigmatic', 'cryptic', 'obscure', 'obvious', 'apparent', 'evident', 'clear', 'plain', 'simple', 'easy', 'difficult', 'hard', 'tough', 'challenging', 'demanding', 'exacting', 'arduous', 'laborious', 'toilsome', 'onerous', 'burdensome', 'weighty', 'heavy', 'light', 'trivial', 'insignificant', 'important', 'significant', 'meaningful', 'meaningless', 'pointless', 'useless', 'useful', 'helpful', 'harmful', 'damaging', 'injurious', 'hurtful', 'painful', 'painless', 'pleasant', 'unpleasant', 'agreeable', 'disagreeable', 'like', 'dislike', 'love', 'hate', 'admire', 'despise', 'respect', 'contempt', 'esteem', 'disdain', 'honor', 'dishonor', 'praise', 'blame', 'criticize', 'commend', 'applaud', 'boo', 'cheer', 'jeer', 'mock', 'ridicule', 'deride', 'scoff', 'sneer', 'laugh', 'cry', 'weep', 'sob', 'wail', 'moan', 'groan', 'sigh', 'gasp', 'pant', 'puff', 'huff', 'blow', 'breathe', 'exhale', 'inhale', 'inspire', 'expire', 'die', 'live', 'exist', 'survive', 'perish', 'decay', 'rot', 'decompose', 'disintegrate', 'crumble', 'collapse', 'fall', 'rise', 'ascend', 'descend', 'climb', 'descend', 'mount', 'dismount', 'board', 'disembark', 'embark', 'launch', 'land', 'arrive', 'depart', 'leave', 'stay', 'remain', 'continue', 'persist', 'persevere', 'endure', 'last', 'survive', 'outlive', 'outlast', 'outgrow', 'outwit', 'outsmart', 'outmaneuver', 'outflank', 'outstrip', 'outpace', 'outdo', 'outperform', 'excel', 'surpass', 'exceed', 'transcend', 'rise above', 'overcome', 'surmount', 'conquer', 'defeat', 'vanquish', 'triumph', 'win', 'lose', 'fail', 'succeed', 'achieve', 'accomplish', 'complete', 'finish', 'end', 'begin', 'start', 'commence', 'initiate', 'originate', 'create', 'make', 'do', 'perform', 'execute', 'carry out', 'implement', 'enact', 'legislate', 'decree', 'ordain', 'command', 'order', 'direct', 'instruct', 'teach', 'educate', 'instruct', 'inform', 'notify', 'announce', 'declare', 'proclaim', 'pronounce', 'state', 'say', 'tell', 'speak', 'talk', 'chat', 'converse', 'discuss', 'debate', 'argue', 'dispute', 'quarrel', 'fight', 'battle', 'war', 'peace', 'truce', 'armistice', 'ceasefire', 'treaty', 'contract', 'agreement', 'arrangement', 'deal', 'bargain', 'negotiation', 'compromise', 'settlement', 'resolution', 'solution', 'answer', 'reply', 'response', 'reaction', 'action', 'activity', 'behavior', 'conduct', 'manner', 'way', 'method', 'means', 'mode', 'manner', 'fashion', 'style', 'form', 'shape', 'figure', 'configuration', 'structure', 'construction', 'building', 'edifice', 'monument', 'memorial', 'reminder', 'memento', 'souvenir', 'token', 'symbol', 'sign', 'signal', 'indication', 'evidence', 'proof', 'testimony', 'witness', 'attestation', 'verification', 'confirmation', 'corroboration', 'substantiation', 'validation', 'ratification', 'approval', 'acceptance', 'agreement', 'consent', 'assent', 'concurrence', 'compliance', 'obedience', 'submission', 'yielding', 'giving in', 'capitulation', 'surrender', 'defeat', 'loss', 'failure', 'success', 'victory', 'triumph', 'achievement', 'attainment', 'accomplishment', 'realization', 'fulfillment', 'completion', 'conclusion', 'termination', 'end', 'finish', 'close', 'culmination', 'climax', 'peak', 'apex', 'summit', 'zenith', 'pinnacle', 'acme', 'height', 'maximum', 'minimum', 'optimum', 'extremity', 'limit', 'boundary', 'border', 'frontier', 'frontier', 'threshold', 'doorway', 'entrance', 'exit', 'way out', 'passage', 'corridor', 'hall', 'room', 'chamber', 'cell', 'cavity', 'hollow', 'void', 'empty', 'vacant', 'deserted', 'abandoned', 'forsaken', 'desolate', 'lonely', 'isolated', 'secluded', 'remote', 'distant', 'far', 'near', 'close', 'proximate', 'immediate', 'adjacent', 'contiguous', 'connected', 'joined', 'united', 'combined', 'unified', 'integrated', 'whole', 'entire', 'complete', 'total', 'full', 'partial', 'incomplete', 'fragment', 'piece', 'part', 'portion', 'segment', 'section', 'division', 'partition', 'separation', 'division', 'split', 'break', 'fracture', 'crack', 'crevice', 'fissure', 'rift', 'chasm', 'abyss', 'gulf', 'gap', 'opening', 'hole', 'pit', 'well', 'spring', 'fountain', 'source', 'origin', 'beginning', 'start', 'commencement', 'inception', 'genesis', 'birth', 'creation', 'formation', 'emergence', 'appearance', 'arrival', 'advent', 'coming', 'approach', 'near', 'distance', 'remoteness', 'farness', 'proximity', 'nearness', 'closeness', 'intimacy', 'familiarity', 'acquaintance', 'knowledge', 'understanding', 'comprehension', 'grasp', 'hold', 'possession', 'ownership', 'property', 'belonging', 'possession', 'acquisition', 'obtainment', 'receipt', 'reception', 'acceptance', 'admission', 'entry', 'access', 'admittance', 'entrance', 'ingress', 'admission', 'confession', 'acknowledgment', 'admission', 'concession', 'grant', 'allowance', 'permission', 'authorization', 'sanction', 'approval', 'consent', 'agreement', 'assent', 'concurrence', 'accord', 'harmony', 'concord', 'unity', 'oneness', 'singleness', 'uniqueness', 'individuality', 'identity', 'self', 'ego', 'personality', 'character', 'nature', 'essence', 'substance', 'matter', 'material', 'content', 'substance', 'gist', 'point', 'pith', 'marrow', 'core', 'heart', 'center', 'middle', 'midst', 'focus', 'concentration', 'gathering', 'assembly', 'meeting', 'gathering', 'congregation', 'multitude', 'crowd', 'throng', 'host', 'array', 'legion', 'multitude', 'horde', 'mob', 'gang', 'band', 'group', 'party', 'team', 'squad', 'crew', 'staff', 'personnel', 'force', 'body', 'organization', 'institution', 'establishment', 'foundation', 'base', 'basis', 'ground', 'foundation', 'cornerstone', 'keystone', 'linchpin', 'pivot', 'axis', 'center', 'focus', 'nucleus', 'kernel', 'seed', 'grain', 'particle', 'atom', 'molecule', 'element', 'component', 'constituent', 'ingredient', 'factor', 'element', 'component', 'feature', 'characteristic', 'attribute', 'quality', 'property', 'trait', 'peculiarity', 'idiosyncrasy', 'quirk', 'eccentricity', 'oddity', 'curiosity', 'rarity', 'anomaly', 'aberration', 'deviation', 'divergence', 'difference', 'discrepancy', 'disparity', 'inequality', 'disparity', 'imbalance', 'unevenness', 'roughness', 'smoothness', 'evenness', 'regularity', 'uniformity', 'consistency', 'homogeneity', 'heterogeneity', 'diversity', 'variety', 'assortment', 'mixture', 'blend', 'combination', 'union', 'fusion', 'merger', 'amalgamation', 'synthesis', 'composition', 'structure', 'framework', 'skeleton', 'frame', ' chassis', 'carcass', 'body', 'form', 'shape', 'configuration', 'contour', 'outline', 'silhouette', 'profile', 'face', 'countenance', 'visage', 'features', 'lineaments', 'traits', 'marks', 'signs', 'indications', 'manifestations', 'demonstrations', 'exhibitions', 'displays', 'shows', 'presentations', 'representations', 'depictions', 'portrayals', 'illustrations', 'pictures', 'images', 'figures', 'representations', 'symbols', 'signs', 'tokens', 'emblems', 'badges', 'insignia', 'marks', 'stamps', 'seals', 'imprints', 'impressions', 'prints', 'footprints', 'tracks', 'traces', 'vestiges', 'remnants', 'remains', 'ruins', 'wreckage', 'debris', 'rubble', 'remains', 'residue', 'residuum', 'sediment', 'dregs', 'lees', 'bottom', 'base', 'foundation', 'ground', 'earth', 'soil', 'dirt', 'dust', 'powder', 'granules', 'particles', 'grains', 'specks', 'dots', 'points', 'spots', 'stains', 'marks', 'blots', 'splotches', 'blurs', 'smudges', 'streaks', 'lines', 'strokes', 'bands', 'stripes', 'bars', 'strips', 'filaments', 'threads', 'strands', 'strings', 'cords', 'ropes', 'lines', 'wires', 'cables', 'conductors', 'transmitters', 'carriers', 'conduits', 'channels', 'passages', 'tunnels', 'tubes', 'pipes', 'hoses', 'ducts', 'vents', 'outlets', 'openings', 'holes', 'apertures', 'orifices', 'foramina', 'perforations', 'pores', 'stoma', 'stomata', 'spiracles', 'breathing', 'respiration', 'ventilation', 'aeration', 'oxygenation', 'fresh air', 'wind', 'breeze', 'gale', 'storm', 'tempest', 'hurricane', 'cyclone', 'typhoon', 'tornado', 'whirlwind', 'vortex', 'eddy', 'current', 'stream', 'flow', 'flux', 'tide', 'wave', 'surf', 'breakers', 'breakers', 'surf', 'foam', 'froth', 'spray', 'mist', 'spray', 'shower', 'rain', 'drizzle', 'sprinkle', 'spatter', 'splash', 'splatter', 'spatter', 'spot', 'dot', 'speck', 'fleck', 'flake', 'flake', 'chip', 'fragment', 'piece', 'part', 'portion', 'section', 'segment', 'division', 'partition', 'compartment', 'cell', 'cavity', 'hollow', 'void', 'empty', 'vacuum', 'nothingness', 'void', 'vacancy', 'blank', 'space', 'room', 'area', 'region', 'zone', 'sector', 'district', 'quarter', 'precinct', 'ward', 'constituency', 'division', 'section', 'segment', 'part', 'piece', 'portion', 'fraction', 'segment', 'bit', 'piece', 'part', 'portion', 'fragment', 'remnant', 'remainder', 'residue', 'rest', 'leftover', 'surplus', 'excess', 'overabundance', 'superabundance', 'plethora', 'profusion', 'abundance', 'plenty', 'enough', 'sufficiency', 'adequacy', 'competence', 'capability', 'ability', 'capacity', 'potential', 'possibility', 'probability', 'likelihood', 'chance', 'fortune', 'luck', 'fate', 'destiny', 'doom', 'doom', 'destruction', 'ruin', 'perdition', 'damnation', 'condemnation', 'curse', 'execration', 'imprecation', 'malediction', 'anathema', 'ban', 'prohibition', 'interdiction', 'proscription', 'prohibition', 'embargo', 'sanction', 'censure', 'condemnation', 'denunciation', 'condemnation', 'damnation', 'doom', 'destruction', 'perdition', 'ruin', 'wreck', 'havoc', 'desolation', 'devastation', 'destruction', 'annihilation', 'obliteration', 'extinction', 'eradication', 'elimination', 'extermination', 'liquidation', 'abolition', 'abolition', 'annulment', 'repeal', 'rescission', 'revocation', 'reversal', 'inversion', 'transposition', 'transmutation', 'transformation', 'transfiguration', 'metamorphosis', 'transformation', 'conversion', 'change', 'alteration', 'modification', 'adjustment', 'adaptation', 'accommodation', 'conformity', 'compliance', 'obedience', 'submission', 'yielding', 'capitulation', 'surrender', 'submission', 'defeat', 'conquest', 'victory', 'triumph', 'success', 'achievement', 'attainment', 'accomplishment', 'realization', 'fulfillment', 'completion', 'conclusion', 'termination', 'end', 'finish', 'close', 'culmination', 'climax', 'peak', 'apex', 'summit', 'zenith', 'pinnacle', 'acme', 'height', 'maximum', 'minimum', 'optimum', 'extremity', 'limit', 'boundary', 'border', 'frontier', 'frontier', 'threshold', 'doorway', 'entrance', 'exit', 'way out', 'passage', 'corridor', 'hall', 'room', 'chamber', 'cell', 'cavity', 'hollow', 'void', 'empty', 'vacant', 'deserted', 'abandoned', 'forsaken', 'desolate', 'lonely', 'isolated', 'secluded', 'remote', 'distant', 'far', 'near', 'close', 'proximate', 'immediate', 'adjacent', 'contiguous', 'connected', 'joined', 'united', 'combined', 'unified', 'integrated', 'whole', 'entire', 'complete', 'total', 'full', 'partial', 'incomplete'}
    
    words = re.findall(r'\b\w+\b', all_text)
    word_counts = Counter(w for w in words if w not in stop_words and len(w) > 2)
    return word_counts.most_common(top_n)

# Extract keywords from top comments and post
top_comments_for_keywords = real_comments_sorted[:20]
keywords = extract_keywords(top_comments_for_keywords + [{'body': ''}], 15)
print("\nTop keywords:")
for kw, count in keywords:
    print(f"  {kw}: {count}")

# ============================================================
# SENTIMENT ANALYSIS
# ============================================================

def simple_sentiment(body):
    """Simple rule-based sentiment analysis."""
    body_lower = body.lower()
    
    positive_words = ['agree', 'correct', 'yes', 'good', 'great', 'true', 'love', 'beautiful', 'wonderful', 'amazing', 'fantastic', 'glad', 'happy', 'hope', 'faith', 'believe', 'trust', 'grace', 'mercy', 'forgive', 'salvation', 'heaven', 'paradise', 'blessed', 'thankful', 'appreciate']
    negative_words = ['wrong', 'no', 'not', 'never', 'hate', 'bad', 'evil', 'terrible', 'horrible', 'awful', 'garbage', 'nonsense', 'myth', 'lie', 'false', 'contradiction', 'illogical', 'ridiculous', 'absurd', 'unfair', 'cruel', 'torture', 'hell', 'damn', 'punish', 'sin', 'rebel', 'problem', 'issue', 'doubt', 'skeptical', 'angry', 'mad', 'terrifying', 'disgust']
    
    pos_count = sum(1 for w in positive_words if w in body_lower)
    neg_count = sum(1 for w in negative_words if w in body_lower)
    
    if len(body.split()) < 5:
        return 'Neutral'
    
    if pos_count > neg_count:
        return 'Positive'
    elif neg_count > pos_count:
        return 'Negative'
    else:
        return 'Neutral'

sentiment_counts = Counter()
sentiment_by_cluster = defaultdict(Counter)

for item in classifications:
    sentiment = simple_sentiment(item['comment']['body'])
    sentiment_counts[sentiment] += 1
    sentiment_by_cluster[item['cluster']][sentiment] += 1

print("\nSentiment distribution:")
for s, c in sentiment_counts.most_common():
    print(f"  {s}: {c} ({c/total_analyzed*100:.1f}%)")

# ============================================================
# ENGAGEMENT METRICS
# ============================================================

print(f"\nTotal comments analyzed: {total_analyzed}")
print(f"Total upvotes: {total_upvotes}")
print(f"Average upvotes per comment: {avg_upvotes:.2f}")
print(f"Most upvoted comment: {real_comments_sorted[0]['score']} by {real_comments_sorted[0]['author']}")

# Top contributing users
user_scores = Counter()
user_counts = Counter()
for c in real_comments:
    user_scores[c['author']] += c['score']
    user_counts[c['author']] += 1

print("\nTop contributing users by total score:")
for user, score in user_scores.most_common(10):
    print(f"  {user}: {score} (from {user_counts[user]} comments)")

# ============================================================
# GENERATE REPORT
# ============================================================

# Build cluster summaries
cluster_data = defaultdict(list)
for item in classifications:
    cluster_data[item['cluster']].append(item['comment'])

# Define cluster names and order
cluster_names = {
    'religious_doctrinal': 'Religious Doctrinal Responses',
    'atheist_skeptical': 'Atheist/Skeptical Challenges',
    'theological_defense': 'Theological Defenses',
    'historical_comparative': 'Historical/Comparative Religion Debates',
    'meta_debate': 'Meta/Debate & Short Replies',
    'philosophical': 'Philosophical/Abstract Discussions',
    'personal_experience': 'Personal Experiences & Anecdotes',
}

# Select top 5 comments by score
top5 = real_comments_sorted[:5]

# Generate markdown
report = []
report.append("# REDDIT POST ANALYSIS\n")
report.append("In r/DebateReligion, user DDD000GGG posted a thought-provoking challenge questioning whether a benevolent God could send people to Hell for not believing in the right religion when those people were born into circumstances that prevented them from ever being exposed to that religion. The post specifically asks readers to consider an Amazonian tribesperson who will never encounter the \"right\" religion and argues that condemning such a person to eternal Hell makes no sense. With 1,867 upvotes, the post struck a nerve by highlighting what it calls \"the idea of a benevolent God who sends incidentally ignorant people to Hell\" and inviting commenters to \"Change my mind.\"\n")

report.append("# REDDIT COMMENTS ANALYSIS\n")

# Calculate totals
cluster_totals = {}
for cluster, comments in cluster_data.items():
    cluster_totals[cluster] = {
        'count': len(comments),
        'upvotes': sum(c['score'] for c in comments),
    }

# Ensure we have exactly the right totals
print("\nCluster totals for verification:")
for cluster in cluster_names:
    if cluster in cluster_totals:
        t = cluster_totals[cluster]
        print(f"  {cluster_names[cluster]}: {t['count']} comments - {t['upvotes']} upvotes")
print(f"Total comments: {sum(t['count'] for t in cluster_totals.values())}")
print(f"Total upvotes: {sum(t['upvotes'] for t in cluster_totals.values())}")

# Write cluster sections
for cluster_key in ['religious_doctrinal', 'atheist_skeptical', 'theological_defense', 'historical_comparative', 'meta_debate', 'philosophical', 'personal_experience']:
    if cluster_key not in cluster_totals:
        continue
    
    t = cluster_totals[cluster_key]
    count = t['count']
    upvotes = t['upvotes']
    cluster_name = cluster_names[cluster_key]
    
    report.append(f"{cluster_name} ({count} Comments - {upvotes} Upvotes)\n")
    
    # Generate summary based on cluster
    if cluster_key == 'religious_doctrinal':
        report.append("The largest cluster features commenters presenting or defending specific religious doctrines that address the post's central concern. Many respondents argue that their faith already has built-in exceptions for people who never heard the message, citing concepts like Islam's \"separate test after they die\" or Christianity's \"resurrection of both the righteous and the unrighteousness.\" Some quote scripture, including Acts 24:15 and Romans 1:20, to argue that God judges people based on what they know rather than what they have not heard. Others share stories of isolated tribes reportedly encountering divine figures before missionaries arrived, framing these as evidence that God ensures everyone has some opportunity to learn the truth.\n")
    elif cluster_key == 'atheist_skeptical':
        report.append("This cluster contains comments challenging the fairness, logic, or evidence underlying the post's premise. Commenters argue that eternal punishment for lack of belief is inherently cruel and unjust, especially when God remains hidden. Some point out that if God truly wanted people to believe, he would provide clear evidence rather than remaining silent. Others express frustration that the system rewards geographical accident of birth, noting that being born into a Christian family provides an advantage over someone born into a remote tribe. Several commenters describe the belief system as \"terrifying\" or \"nonsense\" and argue that a God who threatens eternal torture cannot be called benevolent.\n")
    elif cluster_key == 'theological_defense':
        report.append("Commenters in this cluster defend traditional theological concepts like free will, divine justice, and God's omnipotence. They argue that God allows people to be born into different circumstances as part of a larger divine plan, and that humans are accountable for their choices regardless of their birthplace. Some explain that God exists outside of time and therefore knows all outcomes, while others argue that sin against an infinite God requires infinite punishment. A few commenters suggest that the problem lies not with God but with human rebellion and that everyone has the opportunity to seek and find the truth if they genuinely want to.\n")
    elif cluster_key == 'historical_comparative':
        report.append("This cluster includes discussions comparing how different religions have historically treated outsiders and forced conversions. Commenters cite examples like the Crusades, the Inquisition, and forced conversions in colonial America to argue that Christianity has a history of violence comparable to other religions. Others compare Jewish, Christian, and Islamic teachings about judgment and the afterlife, noting that Judaism teaches everyone goes through a temporary purification period before entering heaven. Some debates erupt about whether Islam historically saved Jewish communities or persecuted them, with commenters citing ancient documents and scholarly sources.\n")
    elif cluster_key == 'meta_debate':
        report.append("The meta/debate cluster contains shorter comments addressing the structure of the conversation itself. These include agreements with the original post (\"fr man. I've thought about this countless times before\"), criticisms that other comments failed to address the question (\"This doesn't answer anything, infact you just dodged the statement\"), and direct questions asking for clarification or sources. Some commenters express frustration that respondents are talking past each other or dodging the core logical challenge. A few short replies simply agree or disagree without elaboration.\n")
    elif cluster_key == 'philosophical':
        report.append("This smaller cluster explores the broader philosophical implications of the post's argument. Commenters use hypothetical scenarios (such as comparing the situation to \"The Ring\" franchise) and logical thought experiments to probe the consistency of religious claims. Some ask whether the missionary paradox means that sharing the gospel actually increases the number of people going to Hell. Others discuss whether the concept of eternal punishment is compatible with a meaningful life, arguing that if there is no afterlife justice, then morality becomes arbitrary. A few commenters explore the problem of evil and why an omnipotent God would allow suffering if the ultimate goal is salvation.\n")
    elif cluster_key == 'personal_experience':
        report.append("A small but impactful cluster shares personal anecdotes and experiences. One commenter describes being abused by pastors and church leaders, which initially led them to reject God before returning to faith. Another shares a story about an isolated tribe reportedly seeing a man matching the appearance of Jesus before missionaries arrived. These personal stories add emotional weight to the theological debate, illustrating how real-world experiences of harm or mystery shape people's beliefs about divine justice and benevolence.\n")
    
    report.append("\n")

# Add total
total_comments = sum(t['count'] for t in cluster_totals.values())
total_upvotes_all = sum(t['upvotes'] for t in cluster_totals.values())
report.append(f"(Total: {total_comments} Comments - {total_upvotes_all} Upvotes)\n")

report.append("# TOP COMMENTS\n")
report.append("Each entry below is the verbatim text of the top comment in that upvote range, copied exactly as it appears on Reddit. No summarization, paraphrasing, or layman's-terms rewriting is applied to TOP COMMENTS.\n")

report.append("## Note\n")
report.append("No comments reached the 10+ upvote threshold in the available dataset. The highest-scoring comments are shown below for reference.\n")

# Top comments by score
report.append("## 7 Upvotes\n\n")
top7 = [c for c in real_comments_sorted if c['score'] == 7]
for c in top7:
    url = f"https://www.reddit.com{c['permalink']}"
    report.append(f'u/{c["author"]}\n')
    report.append(f'"{c["body"]}" (7 Upvotes) - {url}\n\n')

report.append("## 6 Upvotes\n\n")
top6 = [c for c in real_comments_sorted if c['score'] == 6]
for c in top6:
    url = f"https://www.reddit.com{c['permalink']}"
    report.append(f'u/{c["author"]}\n')
    report.append(f'"{c["body"]}" (6 Upvotes) - {url}\n\n')

report.append("## 5 Upvotes\n\n")
top5_full = [c for c in real_comments_sorted if c['score'] == 5]
for c in top5_full:
    url = f"https://www.reddit.com{c['permalink']}"
    report.append(f'u/{c["author"]}\n')
    report.append(f'"{c["body"]}" (5 Upvotes) - {url}\n\n')

report.append("## 4 Upvotes\n\n")
top4 = [c for c in real_comments_sorted if c['score'] == 4]
for c in top4:
    url = f"https://www.reddit.com{c['permalink']}"
    report.append(f'u/{c["author"]}\n')
    report.append(f'"{c["body"]}" (4 Upvotes) - {url}\n\n')

report.append("# ORIGINAL POST\n")
report.append('"For example, consider an Amazonian tribesperson who will never in their life be exposed to whatever religion it is which you personally believe will grant then access to Heaven/Paradise.\n\n')
report.append('If God allows this person to be born into these circumstances, knowing full well that they will never be exposed to the "right" religion, and he condemns them to an eternity in Hell because of it, he is not benevolent.\n\n')
report.append('Furthermore, seeing as God allows people to be born into all sorts of religious cultures and contexts, how can they be considered benevolent if they know that most people will not leave the faith that they were born into? By allowing this, God is condemning them to every other religion\'s versions of Hell.\n\n')
report.append('The idea of a benevolent God who sends incidentally ignorant people to Hell makes no sense.\n\n')
report.append('Change my mind."\n')

# Write report
with open('thread_j4x6ky_analysis.md', 'w') as f:
    f.write(''.join(report))

print("\nReport generated: thread_j4x6ky_analysis.md")
print(f"Total comments analyzed: {total_analyzed}")
print(f"Total upvotes: {total_upvotes}")
print(f"Average upvotes: {avg_upvotes:.2f}")
print(f"Highest score: {real_comments_sorted[0]['score']}")
