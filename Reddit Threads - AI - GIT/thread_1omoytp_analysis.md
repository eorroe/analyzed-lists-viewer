# REDDIT POST ANALYSIS

A developer named u/sshetty03 posted in r/git about switching from stashing or cloning repos to using "git worktree" for managing multiple branches. The post, which earned 165 upvotes, explains that instead of constantly stashing changes or juggling separate clones, they now spin up additional working folders from the same repository. This lets them work on different branches at the same time without the headache of switching contexts or losing unfinished work in stashes. The author describes the experience as "kinda loving it" and shared a Medium article explaining their setup.

# REDDIT COMMENTS ANALYSIS


Agreement/Support - Worktree success stories and tips (22 Comments - 74 Upvotes)
Most commenters here shared their own positive experiences with git worktrees, describing how the feature solved real workflow headaches. Several users mentioned keeping worktrees for specific maintenance branches or documentation, while others built custom tooling around tmux, Neovim, or IDE integrations to make switching between worktrees smoother. A common theme was that once developers adjusted their mental model, worktrees became a reliable part of their daily routine. As u/dalbertom put it, "Stashing and worktrees don't have to be mutually exclusive" — they noted that the stash is shared across worktrees, which is handy for supporting multiple maintenance versions.

Skepticism/Criticism - Concerns about worktree adoption (3 Comments - 5 Upvotes)
These commenters voiced practical concerns about adopting worktrees broadly, citing mental overhead, IDE integration pain, or incompatibility with their existing project structure. u/wildjokers felt worktrees stopped being handy once they realized each branch still needed to be opened as a separate IDE project, calling it "no different than cloning again into a different directory." u/DevelopmentScary3844 added that worktrees "don't work in complex monoliths," at least not for their use case.

Debate/Clarification - Directory structure preferences (11 Comments - 8 Upvotes)
This cluster captures an extended back-and-forth between u/waterkip and u/binarycow about how worktree directories should be organized. u/binarycow preferred keeping worktrees as siblings to the main repository folder, while u/waterkip wanted everything nested under a single project directory. The exchange grew slightly tense as the two talked past each other, but it highlighted a real design choice that new worktree users must make about their folder layout. u/binarycow eventually closed with "You do you!" after u/waterkip explained they manage over 100 repositories and found worktrees too disruptive to their existing setup.

Questions/Technical Concerns (4 Comments - 10 Upvotes)
Several commenters asked practical follow-up questions about edge cases, including how to handle untracked files like dependencies and environment configs, whether worktrees work smoothly inside IDEs like IntelliJ, and why someone would say worktrees fail in complex monoliths. u/schmurfy2 asked a simple "Why?" after a user claimed worktrees didn't work in complex monoliths, prompting u/dalbertom to share a counter-experience from a massive codebase with over 2 million lines of code.

Off-topic/Meta - Article access discussion (2 Comments - -1 Upvotes)
A small side thread emerged about whether the linked Medium article was behind a paywall. The original poster insisted it was free, while another user quoted the article's own paywall notice. This discussion had little to do with git worktrees themselves but reflected a common Reddit pattern of fact-checking shared links.

(Total: 42 Comments - 96 Upvotes)

# TOP COMMENTS


## 10+ Upvotes


u/dalbertom
"Stashing and worktrees don't have to be mutually exclusive. One of the things I like about worktrees is that the stash is shared, so I can stash push in one worktree and pop it in another one. This is pretty handy if you keep a worktree for each maintenance version your project has to support." (24 Upvotes) - https://www.reddit.com/r/git/comments/1omoytp/started_using_git_worktree_to_avoid_stashing_all/nmrzroq/


u/GeoffSobering
"Same here.

It has some downsides (ex. I can't just leave a project open in my ide and let it reload when I switch branches), but it's become my SOP." (10 Upvotes) - https://www.reddit.com/r/git/comments/1omoytp/started_using_git_worktree_to_avoid_stashing_all/nmqz1vd/


# ORIGINAL POST


"Used to stash or clone repos whenever I had to juggle multiple branches.  
Discovered `git worktree` , now I just spin up a second working folder from the same repo. No switching, no stashing.

Wrote a short post on how I use it: [https://medium.com/stackademic/one-git-repo-many-working-copies-meet-git-worktree-0bb650393248?sk=6d2e4e036443f12bc77d82dfb8084e04](https://medium.com/stackademic/one-git-repo-many-working-copies-meet-git-worktree-0bb650393248?sk=6d2e4e036443f12bc77d82dfb8084e04)"
