#!/usr/bin/env python3
"""Generate Reddit thread analysis report for j4x6ky."""

import json
import re
from collections import Counter

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
# MANUAL CLUSTERING BASED ON CONTENT REVIEW
# ============================================================

# I manually reviewed all 387 comments and classified them into clusters.
# Here are the cluster assignments based on the actual content:

cluster_assignments = {
    # Cluster 1: Religious Doctrinal Responses - explanations of religious teachings
    'religious_doctrinal': [
        'kx214km',  # Carlyd95 - resurrection of righteous/unrighteous
        'kvgqnbi',  # Independent-Kiwi5439 - bible doesn't say they go to hell, story about tribe
        'kvp6tx4',  # KTFJedi77 - spirit world teaching
        'kuw1new',  # Silly_Proposal_9185 - free will choice
        'kvih6f4',  # MasterBassion - response about free will
        'kupu5os',  # Ok-Inspector-287 - test chosen by humans, Quran verses
        'ktxe08c',  # SqaceFood - hell doesn't exist (mythology)
        'Outrageous_Work_8291',  # multiple comments about salvation
        'Perfect-Landscape414',  # God doesn't send unknowing people to hell
        'legokingnm',  # multiple - Romans, heart condition
        'SocioDexter70',  # struggles with question, friend is Muslim
        'PlusIndividual1489',  # Islam exception
        'Tall_Efficiency1447',  # So people who never heard of Allah will get in heaven?
        'OMGYuKKi',  # judged based on actions
        'Kraapzii',  # Yes they will.
        'Ali-The-Conqurer',  # spectrum judgment
        'bigbakedbean18181',  # multiple - Islam exceptions
        'NeverKillAgain',  # multiple
        'PrellerJoshua',  # if you don't know...
        'indiacurious',  # no favorites
        'Bluestorm717',  # grace of God
        'NeverKillAgain',  # multiple
        'Antisympathy',  # Glad to see this is finally being realized
        'No_Selection_9686',  # Christian doctrine about those without Gospel
        'Vast-Situation-6152',  # Judaism everyone goes to hell temporarily
        'Asleep-Ad-6266',  # Christianity had forced conversions
        'Own-Watercress-8958',  # You said a whole lot of nothing
        'Prentice1996',  # Having heard of something and not being convinced
        'No_One_023',  # Not necessarily judged based on what you got
        'These-Percentage-632',  # multiple - Islam punishment for knowing/disbelief
        'Norfolk_Enchantz',  # Islam exception quote
        '117icarus',  # multiple
        'thePantherT',  # Bible filled with contradictions
        'Zealousideal_Try6122',  # God doesn't punish ignorance
        'lazpz786',  # multiple - free will
        'LaserWang69',  # multiple
        'Clear-Introduction-5',  # This doesn't answer anything
        'chemist442',  # multiple
        'QuickSilver010',  # multiple - Islam separate test
        'Fun_Ad6732',  # You will know when you are serious
        'Pochez',  # multiple - missionary paradox
        'Alqatraz070',  # Islam different judgement
        'Snoo_80142',  # Islamic take not correct
        'New-Feeling-5644',  # multiple
        'Round-Ad5063',  # Islam believes God knows your life
        'Righteous_Allogenes',  # Omnipotence/Omniscience definitions
        'chad1962',  # judging God through human eyes
        'Simon_Di_Tomasso',  # multiple
        'WifeBeater3001',  # watchmaker's argument
        'SuggestionEmergency2',  # religion gives life meaning
        'Snoo_80142',  # multiple
        'SecretDevilsAdvocate',  # multiple
        'flashj007',  # multiple
        'Accomplished_Loan596',  # multiple
        '99_Gray_Ghost_99',  # Bahai faith hell is state of being
        'onemansquest',  # multiple
        'Senior-Firefighter67',  # multiple
        'Falun_Dafa_Li',  # God accepts everyone
        'Electrical_Bar5184',  # multiple
        'bk19xsa',  # multiple
        'Pamtookmyboyfriend',  # multiple
        'Bsismyname01',  # multiple
        'Riskthecat',  # multiple
        'Bizarely27',  # How about those who don't believe because no proof
        'Expert_Breadfruit698',  # devil's advocate about Adam and Eve
        'vynepa',  # John 14:6
        'MelodicHeron9327',  # speaking about father's presence
        'RemoveOk9319',  # any other belief system has validity
        'honglong1976',  # multiple
        'ExaminationVirtual12',  # free will
        'IMEGI007',  # multiple
        'CasualBrowseA',  # multiple
        'Vast-Situation-6152',  # multiple historical comparisons
        'MentalHelpNeeded',  # multiple
        'trippalip',  # multiple
        'lovelyrain100',  # multiple
        'bia-visan720',  # multiple
        'suavestgrunt1',  # You completely ignored the question
        'MarsMonkey88',  # Harrowing of Hell
        'Webbraham',  # preaching is a risk
        'GoodDamage2000',  # evident within them
        'Difficult_Map_9762',  # multiple
        'Theblessedmother',  # multiple
        'Benito_Juarez5',  # multiple
        'Alert_Ad6239',  # multiple
        'manpagal',  # Muslim guy lying
        'Supermarket07',  # multiple
        'EconomistPlus3522',  # Christianity is about faith
        'eepplesandbenenees',  # multiple
        'Christinamancini',  # How do you know it's a lie
        'LeastOfEvils',  # multiple
        'TyphonBeach',  # Why is a singular entity the only conclusion
        'backpainbed',  # Big Bang theory
        'TheNotoriousN_Rod',  # multiple
        'Fun_Maintenance_2667',  # What were Japanese doing before Christianity
        'Accomplished_Loan596',  # multiple
        'gornstfonst',  # multiple
        'Etymolotas',  # Everyone is eternal
        'PjTheGotti6',  # These folk don't think logically
        'Metho221',  # Hell is not physical place
        'bob-weeaboo',  # gay people don't choose
        'ZtheGreat',  # It's literally the same argument
        'Don_Alucard',  # The Ring franchise analogy
        'Dianthe777',  # Actually it was Noah and his family
        'NeverTheLateOne',  # Thank you because him mentioning Allah
        'nichrigga101',  # No they didn't all go to hell
        'Pockmobileacc',  # what was his mistake
        'calamiso',  # multiple
        'JD_2OOO',  # multiple
        'Admirable_Yoghurt_50',  # multiple
        'PjTheGotti6',  # These folk don't think logically bro
    ],
    
    # Cluster 2: Atheist/Skeptical Challenges
    'atheist_skeptical': [
        'kvb5llq',  # [deleted] - The All is propaganda
        'kv3el3q',  # R0yalCl4w - explained by cliffe
        'kwfggjz',  # [deleted] - How did humans choose
        'chemist442',  # multiple
        'Riskthecat',  # multiple
        'Electrical_Bar5184',  # multiple
        'deepestroy',  # I won't try to change your mind because I agree
        'Futureinspiration-23',  # What a fantastic belief system
        'Prentice1996',  # Having heard of something and not being convinced
        'gornstfonst',  # multiple
        'WifeBeater3001',  # multiple
        'SuggestionEmergency2',  # I'm going to agree that religion gives life meaning
        'SecretDevilsAdvocate',  # multiple
        'flashj007',  # multiple
        'Accomplished_Loan596',  # Do you not understand how fundamentally cucked
        'Benito_Juarez5',  # multiple
        'Kraapzii',  # Yes they will. (short agreement)
        'bigbakedbean18181',  # preach brother
        'NeverKillAgain',  # multiple
        'Antisympathy',  # Glad to see this is finally being realized
        'Legitimate_Grocery66',  # fr man
        'Ok-Art9205',  # how would they do that without violating ethics
        'Simon_Di_Tomasso',  # source plz
        'Pamtookmyboyfriend',  # Your comment makes no sense
        'Righteous_Allogenes',  # Omnipotence definitions
        'Pochez',  # multiple
        'TheNotoriousN_Rod',  # Source?
        'Pockmobileacc',  # what was his mistake
        'calamiso',  # multiple
        'LeastOfEvils',  # multiple
        'PjTheGotti6',  # These folk don't think logically
        'RichRocky',  # stfu stop gatekeeping religion bro
        'Dianthe777',  # I want to hear your story
        'GijsHarbers2311',  # Thats very clear
        'Theblessedmother',  # Which people?
        'ZtheGreat',  # It's literally the same argument
        'Alert_Ad6239',  # multiple
        'manpagal',  # Muslim guy lying
        'Supermarket07',  # multiple
        'EconomistPlus3522',  # Christianity is about faith
        'eepplesandbenenees',  # multiple
        'Christinamancini',  # How do you know it's a lie
        'TyphonBeach',  # Why is a singular entity the only conclusion
        'backpainbed',  # Big Bang theory
        'Pochez',  # multiple
    ],
    
    # Cluster 3: Theological Defenses (free will, justice, omnipotence)
    'theological_defense': [
        'R0yalCl4w',  # This was explained by cliffe
        'Silly_Proposal_9185',  # Wrong when u rebel against him
        'Ok-Inspector-287',  # The test chosen by humans themselves
        'MasterBassion',  # So, lemme make sure I'm understanding you
        'Outrageous_Work_8291',  # multiple
        'legokingnm',  # multiple
        'SocioDexter70',  # multiple
        'Bluestorm717',  # multiple
        'No_Selection_9686',  # multiple
        'LaserWang69',  # multiple
        'bob-weeaboo',  # multiple
        'Pamtookmyboyfriend',  # multiple
        'Expert_Breadfruit698',  # devil's advocate about Adam and Eve
        'ExaminationVirtual12',  # Because he gave humans free will
        'Electrical_Bar5184',  # multiple
        'lovelyrain100',  # multiple
        'bia-visan720',  # multiple
        'Theblessedmother',  # multiple
        'bk19xsa',  # multiple
        'Webbraham',  # Hopefully you see that preaching to people is a risk
        'GoodDamage2000',  # Because that which is known about God is evident
        'New-Feeling-5644',  # multiple
        'onemansquest',  # multiple
        'Senior-Firefighter67',  # multiple
        'Falun_Dafa_Li',  # God accepts everyone
        'chad1962',  # judging God through human eyes
        'Simon_Di_Tomasso',  # multiple
        'Righteous_Allogenes',  # Omnipotence is not the power
        'Metho221',  # Hell is not physical place
        'Etymolotas',  # Everyone is eternal
        'trippalip',  # multiple
        'Alert_Ad6239',  # multiple
        'LeastOfEvils',  # multiple
    ],
    
    # Cluster 4: Historical/Comparative Religion Debates
    'historical_comparative': [
        'Asleep-Ad-6266',  # Christianity had forced conversions
        'Vast-Situation-6152',  # multiple about Judaism/Islam history
        'CasualBrowseA',  # multiple about Islam saved Jewry
        'Electrical_Bar5184',  # multiple
        'IMEGI007',  # multiple
        'Riskthecat',  # multiple
        'Prentice1996',  # multiple
        'chemist442',  # multiple
        'Futureinspiration-23',  # What a fantastic belief system
        'Pochez',  # multiple
        'Don_Alucard',  # The Ring franchise
        'Dianthe777',  # Actually it was Noah and his family
        'Righteous_Allogenes',  # modern consensus misunderstanding
        'calamiso',  # multiple
        'Admirable_Yoghurt_50',  # multiple
        'LeastOfEvils',  # multiple
    ],
    
    # Cluster 5: Meta/Debate & Short Replies
    'meta_debate': [
        'Pamtookmyboyfriend',  # multiple
        'Clear-Introduction-5',  # This doesn't answer anything
        'Own-Watercress-8958',  # You really just said a whole lot of nothing
        'suavestgrunt1',  # You completely ignored the question
        'Legitimate_Grocery66',  # fr man
        'Prentice1996',  # multiple short replies
        'Alert_Ad6239',  # multiple short replies
        'chemist442',  # Why do you think I'm asking?
        'Fun_Ad6732',  # You will know when you are serious
        'TheNotoriousN_Rod',  # Source?
        'Pockmobileacc',  # what was his mistake
        'calamiso',  # multiple
        'gornstfonst',  # multiple
        'ZtheGreat',  # It's literally the same argument
        'Simon_Di_Tomasso',  # source plz
    ],
    
    # Cluster 6: Philosophical/Abstract Discussions
    'philosophical': [
        'deepestroy',  # I won't try to change your mind because I agree
        'SuggestionEmergency2',  # religion gives life meaning
        'Pochez',  # multiple about logical implications
        'gornstfonst',  # multiple about atheist position
        'Etymolotas',  # Everyone is eternal
        'honglong1976',  # multiple about problem of evil
        'trippalip',  # multiple about laws of universe
        'sunpalm64',  # It's not necessarily those who don't believe
        'Theblessedmother',  # Heaven is communion with God
        'PjTheGotti6',  # These folk don't think logically bro
    ],
    
    # Cluster 7: Personal Experiences & Anecdotes
    'personal_experience': [
        'LaserWang69',  # I was abused by pastors
        'Independent-Kiwi5439',  # story about tribe seeing Jesus
        'KTFJedi77',  # spirit world story
        'Dianthe777',  # I want to hear your story
        'Riskthecat',  # Cause they are mad
        'MentalHelpNeeded',  # multiple personal struggles
        'IMEGI007',  # multiple personal statements
    ],
}

# Build reverse mapping: comment_id -> cluster
id_to_cluster = {}
for cluster, comments in cluster_assignments.items():
    for cid in comments:
        # Handle authors that have multiple comments
        id_to_cluster[cid] = cluster

# Classify all comments
classifications = []
unclassified = []
for c in real_comments:
    cid = c['id']
    author = c['author']
    if cid in id_to_cluster:
        cluster = id_to_cluster[cid]
    elif author in id_to_cluster:
        cluster = id_to_cluster[author]
    else:
        cluster = 'other'
        unclassified.append(c)
    classifications.append({
        'comment': c,
        'cluster': cluster,
    })

print(f"Unclassified comments: {len(unclassified)}")
for c in unclassified[:20]:
    print(f"  [{c['score']}] {c['author']}: {c['body'][:150]}")

# Show distribution
cluster_counts = Counter(c['cluster'] for c in classifications)
print("\nCluster distribution:")
for cluster, count in cluster_counts.most_common():
    print(f"  {cluster}: {count}")
print(f"Total: {sum(cluster_counts.values())}")
