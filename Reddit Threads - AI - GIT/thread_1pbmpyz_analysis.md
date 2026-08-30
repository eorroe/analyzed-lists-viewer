# REDDIT POST ANALYSIS

The post "Hot take: Worktrees are underrated, and most teams should be using them" was submitted to r/git by u/GitKraken and received 233 upvotes. The author argues that Git worktrees are underrated and that most teams should use them. They explain that while most developers context-switch by stashing changes and checking out branches, Git worktrees allow multiple branches to be checked out simultaneously in separate directories. This means you can quickly check something on main while mid-feature without stashing or risking uncommitted changes. The author notes worktrees have been in Git since 2015 but are rarely used, and asks the community why—whether due to lack of awareness, cognitive overhead, poor tooling, or failed adoption attempts.

# REDDIT COMMENTS ANALYSIS

## Stash, WIP Commits, and Rebase Preferences (21 Comments - 150 Upvotes)

A large group of commenters defended their existing git workflows over worktrees. Many argued that making WIP commits, using git stash, or doing interactive rebases already solves context switching. One user wrote: "The WIP commit and basic rebase comfort is vastly superior to stash. Stash is just a shitty commit you can lose track of." Others shared detailed rebase workflows or mentioned using temporary "attic" branches for work-in-progress code. The overall sentiment is skeptical of worktrees as a necessary improvement—these developers see their current habits as sufficient.

## Positive Worktree Experiences (31 Comments - 151 Upvotes)

This cluster includes developers who already use worktrees regularly and report meaningful benefits. They described workflows where multiple checked-out directories eliminate the friction of stashing and switching branches. One user shared: "I found them depressingly late...and it's been a big change. We have a fairly mono-ish repo so a separate wt for each area I want to work in." Another iOS engineer explained how worktrees help avoid expensive IDE and cache warmups. Several users mentioned using worktrees for code reviews, debugging multiple branches, or keeping main separate from experimental work.

## IDE, Tooling, and Configuration Friction (68 Comments - 196 Upvotes)

This is the largest cluster, filled with practical concerns about adopting worktrees. Many worried about managing multiple directories, especially with IDEs that treat each directory as a separate project. One user noted: "Having a dynamic number of directories makes effective usage of the IDE more cumbersome." Others mentioned issues with environment variables, Docker containers, port conflicts, and submodules. A recurring theme was that tooling is often built around a single project directory, so spreading work across multiple directories requires extra setup.

## Skepticism and Negative Criticisms (5 Comments - 15 Upvotes)

A smaller but vocal group was openly hostile to the worktree concept. One user wrote: "Its SHIT and obviously not even close to worth it. It's basically a shortcut to avoid having to clone a new version of the repo into a new folder... It's the kind of stupidity that people use because they understand how it works, and thus think it's smart to use, while ignoring the cost and anti-pit-of-success pattern that it is." Others called worktrees overrated or said they simply don't see the use case.

## Jujutsu and Alternative Tool Advocacy (10 Comments - 13 Upvotes)

Several commenters advocated for Jujutsu (jj) or other version control tools as better alternatives. One user explained: "The solution for most usecases you describe is jujutsu... which can switch without stashing and can do smooth rebasing." Others shared that they used to use worktrees extensively but switched to Jujutsu, which eliminated the need for worktrees by removing the concept of a dirty HEAD. Some mentioned that Jujutsu even supports worktrees, but the core advantage is that it makes context switching essentially free.

(Total: 135 Comments - 525 Upvotes)
The sum of all X Comments values above (135) equals the total number of comments analyzed (135). Every comment fetched has been assigned to exactly one cluster.

# TOP COMMENTS

Each entry below is the verbatim text of the top comment in that upvote range, copied exactly as it appears on Reddit.

## 70+ Upvotes

u/r0flcopt3r

"Sometimes build systems depends on stupid things, like the directory name, or other random things that break using work trees. These are all bugs, but bugs i don't have time or energy to fix.

I find most people barely understand the purpose of a commit to begin with..." (73 Upvotes) - https://www.reddit.com/r/git/comments/1pbmpyz/hot_take_worktrees_are_underrated_and_most_teams/nrrijwy/

## 30+ Upvotes

u/dashkb

"The WIP commit and basic rebase comfort is vastly superior to stash. Stash is just a shitty commit you can lose track of." (35 Upvotes) - https://www.reddit.com/r/git/comments/1pbmpyz/hot_take_worktrees_are_underrated_and_most_teams/nrrvcah/

## 20+ Upvotes

u/lollysticky

"in separate directories, like you would have if you cloned the repo multiple times? Or am I missing an important distinction?" (28 Upvotes) - https://www.reddit.com/r/git/comments/1pbmpyz/hot_take_worktrees_are_underrated_and_most_teams/nrrhpa6/

## 10+ Upvotes

u/avinthakur080

"I came to know of them a few months ago. But one discomfort I see is that it is difficult to manage different directories for one thing.
* Many tools use the project's absolute path to link metadata to it. It is also more common/comfortable to have absolute paths in the temporary tools/scripts that we create to work in the project. Having different branches in different directories means every directory will be treated as a different project, or needs effort to sync tools.
* Conventionally, we prefer to keep the folder name the same as the project/repo name. Worktrees either make us go against this convention or force us to have multiple nested directories like `<branch-x>/<proj-name>`.
* Select all and stash is convenient enough to stash all tracked/untracked changes. And since we can work on only one thing at a time, having one branch checked out at a time doesn't cause any issue.
All said, I am interested in knowing the perspective of a worktree power-user to see what answers they have to the above questions, and in what scenarios they use worktrees." (15 Upvotes) - https://www.reddit.com/r/git/comments/1pbmpyz/hot_take_worktrees_are_underrated_and_most_teams/nrrk3xt/

# ORIGINAL POST

**Title:** Hot take: Worktrees are underrated, and most teams should be using them

"Here's something we've been thinking about.

Most devs still context switch by stashing changes, checking out another branch, doing the thing, then switching back and unstashing. It's muscle memory at this point.

But Git worktrees let you have multiple branches checked out simultaneously in separate directories. Need to quickly check something on main while you're mid-feature? Just cd into your main worktree. No stash, no checkout, no "oh sh\*t, I had uncommitted changes."

We've seen teams adopt worktrees and it fundamentally changes how they work. Suddenly reviewing a PR doesn't mean interrupting your current work. Suddenly "quick fixes" don't derail your flow.

The weird part? Worktrees have been in Git since 2015, but almost nobody uses them. We're curious why. 

Is it:

Lack of awareness?

Too much cognitive overhead?

Tooling doesn't support them well?

Actually tried them and they didn't stick?

For those who do use worktrees regularly, what made you adopt them? And for those who don't, what would it take?

"
