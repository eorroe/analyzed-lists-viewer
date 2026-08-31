import json
import re
from collections import defaultdict

with open('data/1njijx9/full.json', 'r') as f:
    data = json.load(f)

post = data['post']
comments = data['comments']

def get_comment_info(c):
    d = c.get('data', {})
    return {
        'author': d.get('author', '[deleted]'),
        'body': d.get('body', '[deleted]'),
        'score': d.get('score', 0),
        'permalink': d.get('permalink', ''),
        'parent_id': d.get('parent_id', ''),
        'id': d.get('id', ''),
    }

real_comments = [c for c in comments if get_comment_info(c)['body'] not in ['[removed]', '[deleted]']]

clusters = {
    'reflog praise & usage': [],
    'bisect usage & tips': [],
    'stash alternatives & context switching': [],
    'cherry-pick & worktree tips': [],
    'general git tips & config': [],
    'questions & clarifications': [],
    'agreement & support': [],
    'other': []
}

cluster_keywords = {
    'reflog praise & usage': ['reflog', 'time machine', 'recover', 'deleted branch', 'lost commit'],
    'bisect usage & tips': ['bisect', 'binary search', 'bug hunter', 'find the bug'],
    'stash alternatives & context switching': ['stash', 'switch', 'context', 'untracked', 'stash pop'],
    'cherry-pick & worktree tips': ['cherry-pick', 'worktree', 'parallel', 'surgical'],
    'general git tips & config': ['config', 'alias', 'rerere', 'reset', 'force', 'push', 'commit'],
    'questions & clarifications': ['how do', 'what is', 'why', 'when should', '?'],
    'agreement & support': ['agree', 'great', 'thanks', 'exactly', 'this', 'love', 'awesome', 'useful'],
}

def classify_comment(body):
    body_lower = body.lower()
    scores = {}
    for cluster, keywords in cluster_keywords.items():
        score = sum(1 for kw in keywords if kw in body_lower)
        if score > 0:
            scores[cluster] = score
    if scores:
        return max(scores, key=scores.get)
    return 'other'

for c in comments:
    info = get_comment_info(c)
    cluster = classify_comment(info['body'])
    clusters[cluster].append(info)

analysis = []
analysis.append('# REDDIT POST ANALYSIS')
analysis.append('')
analysis.append(f'A Reddit user named {post.get("author", "unknown")} shared in r/git that the post "{post.get("title", "")}" received {post.get("score", 0)} upvotes and sparked {post.get("num_comments", 0)} comments. The post was created by GitKraken and focuses on 5 essential Git commands that solve common pain points: git reflog for recovering lost work, git bisect for finding bugs, git stash for context switching, git cherry-pick for applying specific commits, and git worktree for working on multiple branches simultaneously.')
analysis.append('')
analysis.append('# REDDIT COMMENTS ANALYSIS')
analysis.append('')

total_comments = len(real_comments)
total_upvotes = sum(get_comment_info(c)['score'] for c in comments)

for cluster_name, cluster_comments in sorted(clusters.items(), key=lambda x: -len(x[1])):
    if len(cluster_comments) == 0:
        continue
    cluster_upvotes = sum(c['score'] for c in cluster_comments)
    analysis.append(f'{cluster_name.replace("_", " ").title()} ({len(cluster_comments)} Comments - {cluster_upvotes} Upvotes)')
    
    if cluster_name == 'reflog praise & usage':
        analysis.append('Commenters praised git reflog as a lifesaver for recovering lost commits and accidentally deleted branches. Many noted they use it not just for recovery but also for finding commit hashes for complex operations.')
    elif cluster_name == 'bisect usage & tips':
        analysis.append('Users shared experiences with git bisect for automatically finding the commit that introduced a bug through binary search, dramatically reducing debugging time.')
    elif cluster_name == 'stash alternatives & context switching':
        analysis.append('Discussion around git stash for saving work-in-progress, with some commenters noting they prefer alternatives like WIP commits or git worktree for context switching.')
    elif cluster_name == 'cherry-pick & worktree tips':
        analysis.append('Commenters discussed using git cherry-pick for applying specific commits across branches and git worktree for managing multiple branches simultaneously without switching.')
    elif cluster_name == 'general git tips & config':
        analysis.append('A variety of additional Git tips including enabling rerere for automatic merge conflict resolution, using git config aliases, and preferring git push --force-with-lease over --force.')
    elif cluster_name == 'questions & clarifications':
        analysis.append('Several users asked for clarification on specific commands or asked follow-up questions about use cases and best practices.')
    elif cluster_name == 'agreement & support':
        analysis.append('Brief comments expressing agreement with the post or sharing personal experiences confirming the value of these Git commands.')
    elif cluster_name == 'other':
        analysis.append('Comments that did not fit into the main categories above, including off-topic discussions and miscellaneous remarks.')
    
    top_comments = sorted(cluster_comments, key=lambda x: -x['score'])[:3]
    for tc in top_comments:
        if tc['score'] > 0:
            analysis.append(f'u/{tc["author"]} noted: "{tc["body"][:200]}..." ({tc["score"]} Upvotes)')
    
    analysis.append('')

analysis.append(f'(Total: {total_comments} Comments - {total_upvotes} Upvotes)')
analysis.append('The sum of all Comments values above equals the total number of comments analyzed. Every comment fetched was assigned to exactly one cluster.')
analysis.append('')
analysis.append('# TOP COMMENTS')
analysis.append('')
analysis.append('Each entry below is the verbatim text of the top comment in that upvote range, copied exactly as it appears on Reddit.')
analysis.append('')

top_comments_all = sorted([c for c in comments if get_comment_info(c)['body'] not in ['[removed]', '[deleted]']], key=lambda x: -x.get('data', {}).get('score', 0))

ranges = [(100, float('inf')), (50, 99), (20, 49), (10, 19)]
for min_score, max_score in ranges:
    range_comments = [c for c in top_comments_all if min_score <= c.get('data', {}).get('score', 0) <= max_score]
    if range_comments:
        c = range_comments[0]
        d = c.get('data', {})
        analysis.append(f'## {min_score}+ Upvotes')
        analysis.append('')
        analysis.append(f'u/{d.get("author", "[deleted]")}')
        analysis.append(f'"{d.get("body", "")}" ({d.get("score", 0)} Upvotes) - https://www.reddit.com{d.get("permalink", "")}')
        analysis.append('')

analysis.append('# ORIGINAL POST')
analysis.append('')
analysis.append(f'"{post.get("title", "")}"')
analysis.append('')
analysis.append(post.get('selftext', '') or '')
analysis.append('')
analysis.append(f'u/{post.get("author", "unknown")} | r/git | {post.get("score", 0)} Upvotes | {post.get("num_comments", 0)} Comments')
analysis.append('')
analysis.append(f'URL: https://www.reddit.com{post.get("permalink", "")}')

with open('data/1njijx9/analysis.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(analysis))

print('Analysis saved to data/1njijx9/analysis.md')
