# REDDIT POST ANALYSIS

In the r/git subreddit, user themoderncoder posted a thoughtful question titled "Worktrees are just extra working directories right?" asking whether Git worktrees are essentially just extra working directories and whether there's anything more to them on a day-to-day basis. The post scored 20 upvotes and generated 31 comments. The author explains that while worktrees involve backend complexity like sharing or copying the repo files, they conceptually feel like just different working directories, and they're worried their recent video on the topic might be oversimplifying things. The core question is whether this mental model misses something important about how worktrees actually work.

# REDDIT COMMENTS ANALYSIS

Shared Object Store & Stash Benefits (5 Comments - 52 Upvotes)
This small but high-upvoted cluster focuses on one of worktrees' biggest practical perks: all worktrees share the same Git object store, so you don't have to fetch from the remote for each one. As u/dalbertom put it, "Because the object store is shared, that means the reflogs, including the stash are also the same, so you can stash save in one worktree and pop the stash in another." Other commenters added that stashes are shared because they're just refs and commits, while things like bisect refs are kept separate per worktree. The overall tone is positive and informative, with people excited about how worktrees remove repetitive remote operations.

Same Branch Limitation & Use Cases (12 Comments - 29 Upvotes)
This is the longest cluster and revolves around a key constraint: you can't have the same branch checked out in multiple worktrees at once. u/dominjaniec noted, "there is one small problem with them - you cannot have the same branch 'active' in multiple WT. which make sense, as synchronising this would be a mess." The discussion then branched into whether this actually matters in practice, with u/elephantdingo saying they don't understand why anyone would want the same branch in multiple worktrees, while u/IAmADev_NoReallyIAm shared a real-world example of using six or seven worktrees for different tickets and code reviews. The conversation stayed mostly neutral, with people working through the trade-offs and offering workarounds like detached heads or multiple branches pointing to the same commit.

Definition & Technical Clarification (7 Comments - 18 Upvotes)
Several commenters pushed back on the idea that worktrees are "just" working directories. u/elephantdingo wrote, "A worktree isn't just a working directory. It also has metadata," and quoted git help worktree to explain that a worktree is the combination of a working tree and repository metadata. u/StevenJOwens provided a detailed walkthrough of how Git normally handles the .git directory and working files, while u/Charming-Designer944 emphasized that worktrees force you to set up branches for every task because there's at most one worktree per branch. This cluster stayed neutral and educational, focused on getting the definitions right.

Feedback on the Poster's Video/UX (6 Comments - 8 Upvotes)
This smaller cluster addresses the original poster's video and some UX quirks of worktrees. u/n_c_brewer said, "I think it is fine how you used it in your video because you don't continue to refer to worktrees as working directories, just initially to help with understanding," but suggested making worktrees siblings of the main one rather than children to avoid .gitignore issues. u/themoderncoder replied that they were surprised there's no native indication when you're inside a worktree, and u/kaddkaka recommended using git-prompt. This cluster was constructive and neutral, offering friendly suggestions for the poster's setup.

Practical Pain Points (1 Comment - 1 Upvote)
A single comment from u/maverickmindster99 highlighted a real friction point: "I recently started using them but I the only issue I have is the node_modules have to be installed separately on a new worktree, which is more time taking in our application rather than just stashing and changing branch." This points to a practical downside where the shared-repo benefit of worktrees doesn't help if your dependencies need rebuilding for each isolated environment.

(Total: 31 Comments - 108 Upvotes)

# TOP COMMENTS

## 30+ Upvotes

u/dalbertom
"The cool thing about worktrees over separately cloning the repository multiple times is that the git object store is shared across them, so you don't have to fetch your remote on each one.

Because the object store is shared, that means the reflogs, including the stash are also the same, so you can stash save in one worktree and pop the stash in another." (38 Upvotes) - https://www.reddit.com/r/git/comments/1s2m0xm/worktrees_are_just_extra_working_directories_right/oc946eo/

## 10+ Upvotes

u/dominjaniec
"there is one small problem with them - you cannot have the same branch "active" in multiple WT. which make sense, as synchronising this would be a mess.

of course, as a "workaround" for most cases, one can have a detached head pointing to the same sha." (10 Upvotes) - https://www.reddit.com/r/git/comments/1s2m0xm/worktrees_are_just_extra_working_directories_right/oc95o07/

# ORIGINAL POST

"It feels like, if you boil it down, the only novel thing that worktrees add are easily accessible additional working  directories.

Accessing a snapshot of your project by checking out different commits, or using different branches to isolate work is already core Git functionality to isolate/track work, so I don't even actively think about anymore. Really the main annoyance is when Git makes it tedious to utilize those two things.

Like, I'd prefer not to think about version control until I really have to (i.e. when committing something or pushing a PR), so not having to think the Git-isms of working directory management (stashing, staging etc) before I absolutely have to is nice.  

All the backend stuff of worktrees creating a copy of files in a new folder, or sharing the main repo is cool backend implementation stuff, but really I just envision worktrees as different working directories. I feel that you could essentially use the words "workspace", "worktree" and "working directory" interchangeably.  

So I guess I'm interested in whether I'm off base with this, and there's something that I'm missing that might make this mental model not so durable. Then the secondary motivation is I just made a video that hinges on this point, and now I'm a bit worried I missed something."
