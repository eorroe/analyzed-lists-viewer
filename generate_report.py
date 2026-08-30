import json

with open('data/1mg1mfp/flat.json') as f:
    comments = json.load(f)
real = [c for c in comments if c['author'] != '[deleted]']

# Cluster map
cluster_map = {
    "n6lbzug": 1, "n6qnit8": 5, "n6qrjiz": 5, "n6qszjp": 5, "n6r2zbw": 5,
    "n6lzteg": 2, "n6m2c55": 2, "n6m27b5": 5, "n6o1vwm": 5, "n6m3i3b": 5,
    "n6m4pzo": 5, "n6m6zn0": 5, "n6m9bd0": 5, "n6nrsaa": 2, "n6n4og4": 5,
    "n6ph76d": 5, "n6o23uk": 5, "n6p9uwe": 1, "n6qub39": 1, "n6mhl41": 6,
    "n6tzn8f": 2, "n6o3l6a": 6, "n6ldync": 2, "n6nacg1": 4, "n6m3ey9": 4,
    "n6qruv2": 4, "n6qsle9": 4, "n6u8qg7": 4, "n6vmo2d": 4, "n6vn8xz": 4,
    "n74jrro": 4, "n6ququl": 2, "n6qritb": 6, "n6lkxq2": 2, "n6myvey": 2,
    "n6o2dk5": 3, "n6nqkrs": 5, "n6u0b0b": 5, "n6lb3ah": 2, "n6lf67o": 1,
    "n6mw4xv": 1, "n6mx6pe": 1, "n6mzxgh": 1, "n6nw806": 6, "n6o4nvw": 5,
    "n6yebjc": 5, "n6qq32n": 6, "n6o3gkx": 5, "n6pod7l": 5, "n6vb207": 3,
    "n6nsgkz": 1, "n6ol91v": 1, "n6z16bm": 3, "n6zaffu": 6, "n6le8en": 3,
    "n6lire5": 6, "n6mxpk4": 5, "n6nxavd": 6, "n6lryly": 3, "n6oac4h": 5,
    "n6lz3o0": 6, "n6nx518": 6, "n6n0zf0": 3, "n6nhqtm": 3, "n71m7h3": 2,
    "n6lt6cm": 2, "n6lzs0l": 2, "n6m9ctw": 2, "n6nxffv": 2, "n6m26bm": 1,
    "n6qz6f0": 6, "n6r03xw": 6, "n6ra61q": 6, "n6qsf5b": 1, "n71mh10": 1,
    "n6lr11n": 1, "n6olpyx": 1, "n6m8tkl": 5, "n6lsa41": 2, "n6ob2sv": 2,
    "n6oi1zh": 6, "n6nsv6x": 2, "n6pmm06": 6, "n6qavsk": 6, "n6le8f7": 3,
    "n6lne87": 5, "n6lc89p": 2, "n6llf4a": 6, "n6lr1mk": 5, "n7grucu": 3,
    "n6m1psm": 6, "n6md600": 3, "n6q7bw7": 6, "n6pgv6k": 3, "n6q7wgn": 6,
    "n6q90ya": 3, "n6q6va2": 5, "n70ur8g": 1, "n6lc373": 4, "n6lem6d": 4,
    "n6le98q": 3, "n6lvbyx": 3, "n6mpse7": 4, "n6n1ia9": 4, "n6limtq": 3,
    "n6nx0o1": 4, "n6ts6s8": 2, "n6ubz0s": 2, "n6y3ggt": 1, "n7j7594": 2,
    "n6lqa3l": 4, "n6n6at6": 4, "n6lvtac": 4, "n6mkpqu": 4, "n6nkmjp": 2,
    "n6r4fv0": 1, "n6penqo": 6, "n6lxjz0": 6, "n6ndget": 5, "n6nh4w3": 6,
    "n6q0xaz": 1, "n6qacuz": 6, "n6qx89j": 5, "n6rd80f": 4, "n6ruveh": 4,
    "n6s73fp": 3, "n6tfomv": 1, "n6tjnlv": 4, "n6ts10o": 3, "n6ucm4z": 3,
    "n6v94cc": 3, "n6wpj8s": 3, "n6vmara": 1, "n6vxtfp": 5, "n6vz5r2": 4,
    "n6x9qjz": 3, "n6xrnwv": 5, "n6xt45g": 1, "n6yk9yk": 3, "n6yqlki": 6,
    "n71is01": 5, "n71l6kd": 2, "n73xy4a": 5, "n78thzo": 2, "n7ag7p4": 6,
    "n7bpi8s": 3, "n7i3ui3": 6, "n6mwb32": 3, "n6ls9ud": 5, "n6myawx": 3,
    "n6n8vrc": 1, "n6ne43j": 5, "n6pi0hi": 5, "n6ni9bx": 5, "n6nianm": 6,
    "n6nxq97": 4, "n6ozeea": 1, "n6nfh79": 3, "n6nxrza": 3, "n6nya31": 3,
    "n6lvnfz": 3, "n6nafrf": 3, "n6n3al3": 3, "n6n7obi": 2,
}

cluster_names = {
    1: "Pro-Rebase / Clean History",
    2: "Pro-Merge / Anti-Rebase Critics",
    3: "Squash Merge / Middle Ground",
    4: "AI/Rage Bait Skeptics",
    5: "Technical Nuances & Warnings",
    6: "Neutral / Experience Sharing",
}

# Build cluster data
from collections import defaultdict
clusters = defaultdict(list)
for c in real:
    cl = cluster_map[c['id']]
    clusters[cl].append(c)

# Sort clusters by total upvotes descending
cluster_stats = []
for cl in sorted(clusters.keys(), key=lambda x: sum(c['score'] for c in clusters[x]), reverse=True):
    cluster_stats.append((cl, cluster_names[cl], clusters[cl]))

# Post data
with open('data/1mg1mfp/initial_raw.json') as f:
    post_data = json.load(f)[0]['data']['children'][0]['data']

post_title = post_data['title']
post_author = post_data['author']
post_score = post_data['score']
post_selftext = post_data['selftext']
post_url = f"https://www.reddit.com{post_data['permalink']}"

# Build report
lines = []
lines.append("# REDDIT POST ANALYSIS")
lines.append("")
lines.append(f"A developer posted in r/git sharing their experience switching from \"git merge\" to \"git rebase\" and \"git cherry-pick.\" The post, written by u/{post_author}, scored {post_score} upvotes and sparked a lively debate with {len(real)} comments. The author complained that merge commits created a messy history and said that for solo projects or small teams, using rebase and cherry-pick keeps the main branch \"clean, focused, and linear.\" They asked the community whether others preferred rebase or merge, and what caveats they had encountered.")
lines.append("")

lines.append("# REDDIT COMMENTS ANALYSIS")
lines.append("")

for cl, name, cms in cluster_stats:
    count = len(cms)
    upvotes = sum(c['score'] for c in cms)
    lines.append(f"{name} ({count} Comments - {upvotes} Upvotes)")
    
    if name == "Pro-Rebase / Clean History":
        lines.append('Supporters of rebase argued that a clean, linear history makes debugging and code review easier. u/dalbertom compared git history to city roads, saying "A small town will be fine with straight roads. Once the town becomes a city it will have more traffic, and merge lanes will be needed." Others noted that squashing work-in-progress commits into meaningful units helps reviewers understand changes, and that rebasing keeps the commit log readable for teams that care about their history.')
    elif name == "Pro-Merge / Anti-Rebase Critics":
        lines.append('Critics pushed back hard, defending merge commits and warning that rebasing can destroy valuable context. u/bohoky stated, \"I have never understood the interest in a clean commit history... Let the releases show cleanliness. Otherwise just let git be git.\" Several commenters pointed out that merge commits preserve the full story of how code evolved, help with bisecting bugs, and that rebasing can create \"semantic conflicts\" where the final code looks correct but behaves differently.')
    elif name == "Squash Merge / Middle Ground":
        lines.append('Many commenters suggested squash merge as the best compromise. u/fooljay wrote, \"Squash merges exist and are a lot easier than rebase and cherry pick.\" Others explained that squashing feature branches into a single commit before merging keeps main clean while still preserving the full pull request history for reference. This approach was popular among developers who want tidy main branches without rewriting history or abandoning merges entirely.')
    elif name == "AI/Rage Bait Skeptics":
        lines.append('A noticeable number of commenters suspected the original post was AI-generated or rage bait. u/yourfavteamsucks wrote, \"The original post... It\'s hard to articulate why but it feels like AI, and the em dashes are another clue.\" Others called it \"AI slop\" and \"rage bait,\" though some humans also chimed in to say they use similar workflows.')
    elif name == "Technical Nuances & Warnings":
        lines.append('Several comments focused on specific technical concerns. u/randomguy4q5b3ty warned, \"I don\'t think you really understand what problem cherry-pick is meant to solve, and which new ones it creates.\" Others discussed how rebasing can complicate bisecting, cause repeated conflict resolution, and make it harder to trace which change introduced a bug when multiple branches interact.')
    elif name == "Neutral / Experience Sharing":
        lines.append('Many commenters simply shared what they do at work without taking a strong stance. Some described using rebase for local cleanup then squash merging to main. Others mentioned working on large monorepos where merge commits help coordinate hundreds of contributors. A few asked beginner questions or made off-topic remarks, adding casual color to the technical debate.')
    
    lines.append("")

lines.append(f"(Total: {len(real)} Comments - {sum(c['score'] for c in real)} Upvotes)")
lines.append("The sum of all X Comments values above must equal the total number of comments analyzed. Every comment fetched must be assigned to exactly one cluster.")
lines.append("")

lines.append("# TOP COMMENTS")
lines.append("")
lines.append("Each entry below is the verbatim text of the top comment in that upvote range, copied exactly as it appears on Reddit. No summarization, paraphrasing, or layman's-terms rewriting is applied to TOP COMMENTS.")
lines.append("")

# Top comments by bucket
def get_top_comment(real, low, high):
    candidates = [c for c in real if low <= c['score'] <= high]
    if not candidates:
        return None
    return max(candidates, key=lambda c: c['score'])

# Check all relevant buckets
buckets_to_check = [
    (100, 199, "100+ Upvotes"),
    (40, 49, "40+ Upvotes"),
    (30, 39, "30+ Upvotes"),
    (20, 29, "20+ Upvotes"),
    (10, 19, "10+ Upvotes"),
]

for low, high, label in buckets_to_check:
    top = get_top_comment(real, low, high)
    if top:
        lines.append(f"## {label}")
        lines.append("")
        lines.append(f"u/{top['author']}")
        lines.append(f'"{top["body"]}" ({top["score"]} Upvotes) - https://www.reddit.com{top["permalink"]}')
        lines.append("")

lines.append("# ORIGINAL POST")
lines.append("")
lines.append(f'"{post_title}"')
lines.append("")
lines.append(f'"{post_selftext}"')
lines.append("")

report = "\n".join(lines)
with open('thread_1mg1mfp_analysis.md', 'w', encoding='utf-8') as f:
    f.write(report)

print("Report written to thread_1mg1mfp_analysis.md")
print(f"Total lines: {len(lines)}")
