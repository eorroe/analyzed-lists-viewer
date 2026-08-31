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
# COMPREHENSIVE CLUSTERING
# ============================================================

def classify_comment(body, author, comment_id):
    """Classify comment into thematic cluster based on comprehensive content analysis."""
    body_lower = body.lower()
    
    # Special cases based on known comment IDs
    special_cases = {
        # Religious doctrinal - explicit exceptions for ignorant
        'kx214km': 'religious_doctrinal',
        'kvgqnbi': 'religious_doctrinal',
        'kvp6tx4': 'religious_doctrinal',
        'kuw1new': 'theological_defense',
        'kvih6f4': 'theological_defense',
        'kupu5os': 'religious_doctrinal',
        'Outrageous_Work_8291': 'religious_doctrinal',  # multiple comments
        'Perfect-Landscape414': 'religious_doctrinal',
        'legokingnm': 'religious_doctrinal',
        'SocioDexter70': 'religious_doctrinal',
        'PlusIndividual1489': 'religious_doctrinal',
        'Tall_Efficiency1447': 'religious_doctrinal',
        'OMGYuKKi': 'religious_doctrinal',
        'Kraapzii': 'religious_doctrinal',
        'Ali-The-Conqurer': 'religious_doctrinal',
        'NeverKillAgain': 'religious_doctrinal',  # multiple
        'indiacurious': 'religious_doctrinal',
        'Bluestorm717': 'religious_doctrinal',
        'No_Selection_9686': 'religious_doctrinal',
        'Vast-Situation-6152': 'historical_comparative',  # mostly historical
        'Asleep-Ad-6266': 'historical_comparative',
        'Own-Watercress-8958': 'meta_debate',
        'Prentice1996': 'meta_debate',  # mostly short meta replies
        'No_One_023': 'meta_debate',
        'These-Percentage-632': 'religious_doctrinal',
        'Norfolk_Enchantz': 'religious_doctrinal',
        '117icarus': 'religious_doctrinal',
        'thePantherT': 'atheist_skeptical',
        'Zealousideal_Try6122': 'theological_defense',
        'lazpz786': 'theological_defense',
        'LaserWang69': 'personal_experience',  # personal abuse story
        'Clear-Introduction-5': 'meta_debate',
        'chemist442': 'meta_debate',  # mostly skeptical questions
        'QuickSilver010': 'religious_doctrinal',
        'Fun_Ad6732': 'meta_debate',
        'Pochez': 'philosophical',  # logical arguments
        'Alqatraz070': 'religious_doctrinal',
        'Snoo_80142': 'religious_doctrinal',
        'New-Feeling-5644': 'religious_doctrinal',
        'Round-Ad5063': 'religious_doctrinal',
        'Righteous_Allogenes': 'theological_defense',
        'chad1962': 'theological_defense',
        'Simon_Di_Tomasso': 'theological_defense',  # watchmaker argument
        'WifeBeater3001': 'atheist_skeptical',
        'SuggestionEmergency2': 'philosophical',
        'Snoo_80142': 'religious_doctrinal',
        'SecretDevilsAdvocate': 'atheist_skeptical',  # skeptical about religious claims
        'flashj007': 'atheist_skeptical',
        'Accomplished_Loan596': 'atheist_skeptical',
        '99_Gray_Ghost_99': 'religious_doctrinal',
        'onemansquest': 'theological_defense',
        'Senior-Firefighter67': 'theological_defense',
        'Falun_Dafa_Li': 'religious_doctrinal',
        'Electrical_Bar5184': 'atheist_skeptical',  # challenging religious implications
        'bk19xsa': 'theological_defense',
        'Pamtookmyboyfriend': 'meta_debate',
        'Bsismyname01': 'atheist_skeptical',  # challenging fairness
        'Riskthecat': 'atheist_skeptical',
        'Bizarely27': 'atheist_skeptical',
        'Expert_Breadfruit698': 'philosophical',
        'vynepa': 'religious_doctrinal',
        'MelodicHeron9327': 'theological_defense',
        'RemoveOk9319': 'philosophical',
        'honglong1976': 'philosophical',
        'ExaminationVirtual12': 'theological_defense',
        'IMEGI007': 'religious_doctrinal',  # defending religion
        'CasualBrowseA': 'historical_comparative',
        'MentalHelpNeeded': 'personal_experience',
        'trippalip': 'theological_defense',
        'lovelyrain100': 'theological_defense',
        'bia-visan720': 'religious_doctrinal',
        'suavestgrunt1': 'meta_debate',
        'MarsMonkey88': 'religious_doctrinal',
        'Webbraham': 'philosophical',
        'GoodDamage2000': 'religious_doctrinal',
        'Difficult_Map_9762': 'atheist_skeptical',
        'Theblessedmother': 'religious_doctrinal',
        'Benito_Juarez5': 'atheist_skeptical',
        'Alert_Ad6239': 'religious_doctrinal',
        'manpagal': 'atheist_skeptical',
        'Supermarket07': 'religious_doctrinal',
        'EconomistPlus3522': 'religious_doctrinal',
        'eepplesandbenenees': 'meta_debate',
        'Christinamancini': 'meta_debate',
        'LeastOfEvils': 'religious_doctrinal',
        'TyphonBeach': 'atheist_skeptical',
        'backpainbed': 'atheist_skeptical',
        'TheNotoriousN_Rod': 'meta_debate',
        'Fun_Maintenance_2667': 'historical_comparative',
        'Accomplished_Loan596': 'atheist_skeptical',
        'gornstfonst': 'atheist_skeptical',
        'Etymolotas': 'philosophical',
        'PjTheGotti6': 'meta_debate',
        'Metho221': 'religious_doctrinal',
        'bob-weeaboo': 'philosophical',
        'ZtheGreat': 'meta_debate',
        'Don_Alucard': 'philosophical',
        'Dianthe777': 'personal_experience',
        'NeverTheLateOne': 'meta_debate',
        'nichrigga101': 'religious_doctrinal',
        'Pockmobileacc': 'meta_debate',
        'calamiso': 'meta_debate',
        'JD_2OOO': 'theological_defense',
        'Admirable_Yoghurt_50': 'historical_comparative',
        'PjTheGotti6': 'meta_debate',
        'SqaceFood': 'atheist_skeptical',
        'indicasativagemini': 'religious_doctrinal',
        'Prestigious_Pay751': 'meta_debate',
        'marbinho': 'atheist_skeptical',
        'Ok-Inspector-287': 'religious_doctrinal',
        'R0yalCl4w': 'theological_defense',
        'DebateReligion-ModTeam': 'meta_debate',
        'PoopSommelier': 'philosophical',
        'Background_Ad_371': 'religious_doctrinal',
        'ExaminationVirtual12': 'theological_defense',
        'MrFingolfin': 'meta_debate',
        'CasualBrowseA': 'historical_comparative',
        'RichRocky': 'meta_debate',
        'sunpalm64': 'religious_doctrinal',
        'GijsHarbers2311': 'meta_debate',
        'Ok-Art9205': 'meta_debate',
        'Krenick_': 'meta_debate',
        'Pamtookmyboyfriend': 'meta_debate',
        'Don_Alucard': 'philosophical',
    }
    
    if comment_id in special_cases:
        return special_cases[comment_id]
    if author in special_cases:
        return special_cases[author]
    
    # General keyword-based classification for remaining comments
    scores = defaultdict(int)
    
    # Religious doctrinal content
    islam_keywords = ['islam', 'islamic', 'muslim', 'allah', 'quran', 'hadith', 'muhammad', 'kuffaar', 'kafir', 'islamqa']
    christian_keywords = ['bible', 'christian', 'jesus', 'christ', 'gospel', 'scripture', 'biblical', 'heaven', 'hell', 'salvation', 'resurrection', 'righteous', 'unrighteous', 'gehenna', 'sheol', 'hades', 'catholic', 'protestant', 'acts 24:15', 'matthew', 'romans', 'paul', 'apostle', 'parable']
    jewish_keywords = ['judaism', 'jewish', 'torah', 'hebrew', 'monotheistic', 'rabbinic']
    doctrinal_keywords = ['doctrine', 'teaching', 'theology', 'theological', 'systematic', 'exegesis', 'exception', 'pardoned', 'not punished', 'not condemned', 'different judgement', 'separate test', 'opportunity', 'purified', 'chance to turn', 'will be tested', 'judged based on', 'not to know', 'never heard', 'did not receive the message']
    
    religious_content = any(k in body_lower for k in islam_keywords + christian_keywords + jewish_keywords)
    exception_content = any(k in body_lower for k in doctrinal_keywords)
    
    if religious_content:
        scores['religious_doctrinal'] += 2
    if exception_content:
        scores['religious_doctrinal'] += 2
    
    # Atheist/Skeptical
    atheist_keywords = ['atheist', 'atheism', 'not real', 'doesn\'t exist', 'does not exist', 'myth', 'cult', 'nonsense', 'garbage', 'bs ', 'bullshit', 'made up', 'fairy tale', 'unconvincing', 'insufficient proof', 'not enough proof', 'no evidence', 'lack of evidence', 'doesn\'t show', 'didn\'t show', 'hiding', 'shy']
    skeptical_keywords = ['question', 'doubt', 'skeptical', 'ridiculous', 'absurd', 'illogical', 'contradiction', 'contradicts', 'doesn\'t make sense', 'makes no sense', 'doesn\'t answer', 'dodged', 'terrifying', 'mad', 'angry']
    
    if any(k in body_lower for k in atheist_keywords):
        scores['atheist_skeptical'] += 3
    if any(k in body_lower for k in skeptical_keywords):
        scores['atheist_skeptical'] += 1
    
    # Theological defenses
    freewill_keywords = ['free will', 'freewill', 'free choice', 'choice', 'accountability', 'responsible', 'rebel', 'rebellion', 'sin', 'satan', 'fallen', 'omnipotent', 'omniscient', 'omnipresent', 'all-knowing', 'all-powerful', 'justice', 'just', 'benevolent', 'benevolence', 'grace', 'mercy', 'forgive', 'forgiveness']
    theological_keywords = ['god\'s plan', 'god\'s will', 'divine', 'supernatural', 'miracle', 'mystery', 'mystical', 'perfect', 'formless', 'creator', 'creation', 'origin of the universe', 'big bang', 'intelligent design']
    
    if any(k in body_lower for k in freewill_keywords):
        scores['theological_defense'] += 2
    if any(k in body_lower for k in theological_keywords):
        scores['theological_defense'] += 1
    
    # Historical/Comparative
    historical_keywords = ['crusades', 'inquisition', 'forced conversion', 'forced conversions', 'history', 'historical', 'ancient', 'roman', 'medieval', 'spanish', 'portuguese', 'nazi', 'hitler', 'holocaust', 'antisemitism', 'slavery', 'slave', 'persecution', 'violence', 'kill', 'murder', 'genocide']
    comparative_keywords = ['judaism', 'jewish', 'hindu', 'buddhism', 'monotheistic', 'abrahamic', 'zoroastrian', 'comparison']
    
    if any(k in body_lower for k in historical_keywords):
        scores['historical_comparative'] += 3
    if any(k in body_lower for k in comparative_keywords) and not religious_content:
        scores['historical_comparative'] += 2
    
    # Personal experience
    personal_keywords = ['i was', 'i grew up', 'my family', 'my church', 'i experienced', 'i saw', 'i met', 'my story', 'i was abused', 'i prayed', 'i cried', 'my former', 'my life', 'i have a', 'i\'ve had', 'i remember', 'my father', 'my mother', 'my parents']
    if any(k in body_lower for k in personal_keywords):
        scores['personal_experience'] += 2
    
    # Meta/Debate
    meta_keywords = ['nice post', 'change my mind', 'op is', 'you are wrong', 'you are correct', 'this doesn\'t answer', 'you dodged', 'off topic', 'moderator', 'rule', 'removed', 'you didn\'t', 'you just', 'whole lot of nothing', 'makes no sense', 'your comment', 'your argument', 'reply to', 'ignored', 'didn\'t respond', 'didn\'t address']
    if any(k in body_lower for k in meta_keywords):
        scores['meta_debate'] += 2
    
    # Philosophical/Abstract
    philosophical_keywords = ['what if', 'imagine', 'suppose', 'consider', 'think about', 'question is', 'problem with', 'issue is', 'the problem', 'logic', 'logical', 'fair', 'unfair', 'implications']
    if any(k in body_lower for k in philosophical_keywords):
        scores['philosophical'] += 1
    
    # Science/Naturalism
    science_keywords = ['evolution', 'scientific', 'science', 'study', 'research', 'evidence', 'proof', 'empirical', 'falsification', 'verifiable']
    if any(k in body_lower for k in science_keywords):
        scores['science_naturalism'] += 1
    
    # Get highest scoring cluster
    if not scores:
        return 'other'
    
    best_cluster = max(scores, key=scores.get)
    return best_cluster

# Classify all comments
classifications = []
unclassified = []
for c in real_comments:
    cluster = classify_comment(c['body'], c['author'], c['id'])
    classifications.append({
        'comment': c,
        'cluster': cluster,
    })
    if cluster == 'other':
        unclassified.append(c)

print(f"Unclassified comments: {len(unclassified)}")
for c in unclassified:
    print(f"  [{c['score']}] {c['author']}: {c['body'][:150]}")

# Show distribution
cluster_counts = Counter(c['cluster'] for c in classifications)
print("\nCluster distribution:")
for cluster, count in cluster_counts.most_common():
    print(f"  {cluster}: {count}")
print(f"Total: {sum(cluster_counts.values())}")

# Print sample comments from each cluster
print("\n\n=== SAMPLE COMMENTS BY CLUSTER ===")
for cluster in cluster_counts.keys():
    print(f"\n--- {cluster.upper()} ---")
    samples = [c for c in classifications if c['cluster'] == cluster][:3]
    for s in samples:
        print(f"  [{s['comment']['score']}] {s['comment']['author']}: {s['comment']['body'][:200]}")
        print()
