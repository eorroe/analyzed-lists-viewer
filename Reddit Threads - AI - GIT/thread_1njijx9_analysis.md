# REDDIT POST ANALYSIS

A Reddit user named GitKraken shared in r/git that the post "Git tricks we wish we knew 5 years ago" received 1083 upvotes and sparked 148 comments. The post was created by GitKraken and focuses on 5 essential Git commands that solve common pain points: git reflog for recovering lost work, git bisect for finding bugs, git stash for context switching, git cherry-pick for applying specific commits, and git worktree for working on multiple branches simultaneously.

# REDDIT COMMENTS ANALYSIS

Other (44 Comments - 148 Upvotes)
Comments that did not fit into the main categories above, including off-topic discussions and miscellaneous remarks.
u/[deleted] noted: "[removed]..." (30 Upvotes)
u/beatsbydvorak noted: "ReuseRecordedResolutions. git will record when you resolve a merge conflict and reuse it if it detects the same conflict again in the future...." (18 Upvotes)
u/LossPreventionGuy noted: "literally never used it. can't think of any time I really wanted to..." (14 Upvotes)

Stash Alternatives & Context Switching (29 Comments - 142 Upvotes)
Discussion around git stash for saving work-in-progress, with some commenters noting they prefer alternatives like WIP commits or git worktree for context switching.
u/xenomachina noted: "I almost never use `git stash` anymore. Pretty much the only time I use it is if I intend to pop the stash in the next ~10 minutes.

Otherwise, I make a "wip" commit. That way I'm far less likely to h..." (41 Upvotes)
u/escuchameray noted: "No but it makes sense to stash and unstash your untracked files with your tracked ones. You might have other untracked files on the other branch or accidentally discard an untracked file or something...." (20 Upvotes)
u/RevRagnarok noted: "Extra hint for `cherry-pick`: Use `-x` whenever possible. It adds the hash that was picked _from_ to the commit message so you can instantly "go look over there" for the context months later...." (18 Upvotes)

General Git Tips & Config (28 Comments - 172 Upvotes)
A variety of additional Git tips including enabling rerere for automatic merge conflict resolution, using git config aliases, and preferring git push --force-with-lease over --force.
u/beatsbydvorak noted: "git config rerere.enabled true is a great setting to have if you find yourself resolving the same merge conflicts over and over..." (51 Upvotes)
u/jdlyga noted: "It’s not just for deleting branches. It’s for getting commit hashes, which is useful for any sort of tricky operation like rebases or undoing merges..." (24 Upvotes)
u/NodeJSmith noted: "Rerere is fantastic and I don't know why it's not on by default..." (12 Upvotes)

Questions & Clarifications (14 Comments - 37 Upvotes)
Several users asked for clarification on specific commands or asked follow-up questions about use cases and best practices.
u/n8henrie noted: "I've still yet to figure out why or how people use worktree.

Where does this fit in your workflow?..." (15 Upvotes)
u/martinus noted: "Why not just switch branch? That's what I do. I've tried worktrees a few times but it somehow never was useful for me. ..." (6 Upvotes)
u/VerboseGuy noted: "If you squash your merge requests, does rebasing matter?..." (3 Upvotes)

Reflog Praise & Usage (11 Comments - 109 Upvotes)
Commenters praised git reflog as a lifesaver for recovering lost commits and accidentally deleted branches. Many noted they use it not just for recovery but also for finding commit hashes for complex operations.
u/jdlyga noted: "I'm amazed how many people don't know about git reflog. It's a lifesaver...." (93 Upvotes)
u/shagieIsMe noted: "https://ohshitgit.com

The first item:

> Oh shit, I did something terribly wrong, please tell me git has a magic time machine!?!

    git reflog
    # you will see a list of every thing you've
    # ..." (5 Upvotes)
u/DoctorDabadedoo noted: "Many don't know and another many are afraid of it, to make things simple I usually suggest making a local bkp branch whenever making destructive changes to your branch (rebase, squash, merge, delete, ..." (2 Upvotes)

Agreement & Support (9 Comments - 18 Upvotes)
Brief comments expressing agreement with the post or sharing personal experiences confirming the value of these Git commands.
u/NoHalf9 noted: "This is the way! There is much less than can go wrong with this approach, and bonus when you rebase your wip changes are included...." (9 Upvotes)
u/elbkind_ noted: "git rebase --onto SHA branch

Sometimes rebase is unable to determine the relevant commits, this tells it exactly where to cut..." (2 Upvotes)
u/ShiHouzi noted: "Here’s a pretty useful one from Claude Code Best Practices but you can definitely make a mess with it. 

c. Use git worktrees
This approach shines for multiple independent tasks, offering a lighter-we..." (1 Upvotes)

Cherry-Pick & Worktree Tips (7 Comments - 21 Upvotes)
Commenters discussed using git cherry-pick for applying specific commits across branches and git worktree for managing multiple branches simultaneously without switching.
u/l8rabbit noted: "Thanks for worktree, can't believe I missed that...." (11 Upvotes)
u/ladrm noted: "`git add --interactive` \- **The Surgical Staging**

[https://git-scm.com/book/en/v2/Git-Tools-Interactive-Staging](https://git-scm.com/book/en/v2/Git-Tools-Interactive-Staging)

Lets you add individu..." (3 Upvotes)
u/FlipperBumperKickout noted: "You have better project structure than my company then.


I don't usually create and delete worktrees, but just have a bunch which I reuse when creating new branches. Prevents me from rebuilding the f..." (2 Upvotes)

Bisect Usage & Tips (3 Comments - 11 Upvotes)
Users shared experiences with git bisect for automatically finding the commit that introduced a bug through binary search, dramatically reducing debugging time.
u/TheDragonBallGuy75 noted: "Bisect has been my saviour. Working on game development pet projects, and finding something broke however long ago and not knowing when or where...." (10 Upvotes)
u/theUnknown777 noted: "can you elaborate on the part about argument against rebasing when it comes to bisect...." (1 Upvotes)

(Total: 141 Comments - 658 Upvotes)
The sum of all Comments values above equals the total number of comments analyzed. Every comment fetched was assigned to exactly one cluster.

# TOP COMMENTS

Each entry below is the verbatim text of the top comment in that upvote range, copied exactly as it appears on Reddit.

## 50+ Upvotes

u/jdlyga
"I'm amazed how many people don't know about git reflog. It's a lifesaver." (93 Upvotes) - https://www.reddit.com/r/git/comments/1njijx9/git_tricks_we_wish_we_knew_5_years_ago/neqmv74/

## 20+ Upvotes

u/xenomachina
"I almost never use `git stash` anymore. Pretty much the only time I use it is if I intend to pop the stash in the next ~10 minutes.

Otherwise, I make a "wip" commit. That way I'm far less likely to have trouble finding my in-progress work (or worse, forgetting it even exists!) when I return to that branch." (41 Upvotes) - https://www.reddit.com/r/git/comments/1njijx9/git_tricks_we_wish_we_knew_5_years_ago/nerpiuj/

## 10+ Upvotes

u/beatsbydvorak
"ReuseRecordedResolutions. git will record when you resolve a merge conflict and reuse it if it detects the same conflict again in the future." (18 Upvotes) - https://www.reddit.com/r/git/comments/1njijx9/git_tricks_we_wish_we_knew_5_years_ago/nesoaw0/

# ORIGINAL POST

"Git tricks we wish we knew 5 years ago"

Working with millions of developers, we keep seeing the same Git pain points. Here are 5 commands that solve the most common issues:

**1.** `git reflog` **- The Time Machine** Accidentally deleted a branch? Reset to the wrong commit? Reflog is your safety net.

    git reflog
    # Find your lost commit hash
    git checkout -b recovery-branch <hash>

**2.** `git bisect` **- The Bug Hunter** When you know something broke but don't know when:

    git bisect start
    git bisect bad HEAD
    git bisect good <known-good-commit>
    # Git will guide you to the problematic commit

**3.** `git stash --include-untracked` **- The Context Switcher** Need to switch branches but don't want to commit messy work:

    git stash push -u -m "work in progress on feature X"
    # Work on other branch
    git stash pop

**4.** `git cherry-pick` **- The Surgical Strike** Need just one commit from another branch:

    git cherry-pick <commit-hash>
    # Or for a range:
    git cherry-pick <start-hash>^..<end-hash>

**5.** `git worktree` **- The Parallel Universe** Work on multiple branches simultaneously:

    git worktree add ../feature-branch feature-branch
    # Now you have two working directories for the same repo

What Git commands did we miss?

u/GitKraken | r/git | 1083 Upvotes | 148 Comments

URL: https://www.reddit.com/r/git/comments/1njijx9/git_tricks_we_wish_we_knew_5_years_ago/