# REDDIT POST ANALYSIS

In the r/git subreddit, u/cerwen80 posted a panicked support request titled "Git destroyed everything i made today." The post received a score of 0 and sparked 44 comments. The author is a self-taught amateur coder who spent an entire day working on their website. They had a private repository and had pushed to it the previous week. When they tried to commit and push today, Git told them their version was behind and they needed to pull. After clicking pull then push, they tested their project and found that "EVERYTHING HAD GONE." They tried troubleshooting with ChatGPT but couldn't locate their missing edits. Feeling terrified, they deleted both the GitHub repo and the git folders on their computer, asking "WHY IS GIT SO EVIL AND DANGEROUS????"

# REDDIT COMMENTS ANALYSIS

OP's Story and Learning Journey (19 Comments - 19 Upvotes)
The original poster, u/cerwen80, responded extensively across the thread to explain exactly what happened. They described clicking the "amend" box in Visual Studio because they thought it would update files on GitHub, not realizing they hadn't successfully made an actual commit yet. They said they clicked reset after ChatGPT suggested it, but their edits still weren't there. The OP revealed they are self-taught, have ADHD/autism, and usually figure out software by looking at it rather than reading documentation. They explained that deleting the repo was a "cut-and-run tactic" to prevent further damage. By the end of the thread, they said they now understand Git is "just like an incremental backup tool" and have been using it properly without hiccups.

Git Explanations and Recovery Advice (12 Comments - 25 Upvotes)
Several commenters tried to untangle what went wrong. u/lolcrunchy explained that a commit is like a snapshot of changes, and the "amend" option modifies the last commit rather than creating a new one. They emphasized that "if you committed your changes, then git didn't delete any of your work." u/lolcrunchy also clarified that commands like push, pull, fetch, and remote are related to the internet, while everything else is local. u/randominsomnia advised following the mantra "commit early, commit often." u/Cool-Walk5990 suggested checking the reflog for recovery. u/FlipperBumperKickout explained that Git literally keeps warning you and prevents data loss unless you add the "--force" flag.

Direct Criticism and Tough Feedback (6 Comments - 12 Upvotes)
A handful of commenters were blunt about the OP's mistakes. u/divestblank said "You sound like someone who just discovered electricity" and advised learning the tool properly. u/chpatton013 stated the OP "did exactly the wrong things every step of the way," noting that GUI issues are the GUI's fault, not Git's. u/Tempus_Nemini called it a "Skill issue," saying "You don't use tools if you don't understand how they are working." u/behind-UDFj-39546284 used analogies comparing Git to a knife and matchsticks, criticizing the OP for yelling about Git being evil without making backups first.

Relatability, Empathy, and Shared Struggles (6 Comments - 27 Upvotes)
The most-upvoted comment was u/kin_of_the_caves asking "Why am I so bad at git?" which resonated with many learners. u/dominonermandi offered kind advice about reading documentation and using the command line, and later shared that they have ADHD and recognized the frustration. u/khooke pointed out that "If you hadn't deleted your repo and .git folder this probably would have been easy to recover from." u/dreg_master shared their own frustrating experience with Git causing merge conflicts and said they prefer simple backups to Git as a single developer.

Clarifying Questions (1 Comment - 1 Upvote)
u/surveypoodle asked whether the OP deleted the repo specifically to make sure it was really gone, prompting the OP to explain it was a deliberate "cut-and-run tactic."

(Total: 44 Comments - 84 Upvotes)

# TOP COMMENTS

## 10+ Upvotes

u/kin_of_the_caves
"Why am I so bad at git?" (17 Upvotes) - https://www.reddit.com/r/git/comments/1mgqgk7/git_destroyed_everything_i_made_today/n6qicqt/

# ORIGINAL POST

"Git destroyed everything i made today

I have been trying to use git because everyone says I should.
i spent all day working on some stuff for my website. 
i have a PRIVATE repo. i pushed to it last week when i made it. 
i decided after all my work today that i should do the thing... apparently i need to press commit and then push. so i did it and it told me my verSion was behind and I needed to PULL. 
this was confusing as it's private, I am the only person making any changes. 

I had no other options, so  clicked on pull then push. after waiting for a while, i tested my project again and EVERYTHING HAD GONE.

I've tried troubleshooting this with chatgpt, tried to find where my edits have gone, but as far as i can tell they have vanished.

I don't understand this, first of all, it wouldn't let me upload all my changes, then it deleted them all and even worse they are unretreivable. 
isn't this the exact opposite of what git is suposed to do???

I am quite frankly terrified of this thing now. I've deleted the repo off github and deleted the git folders on my computer. 

I am just mystified and I want to know.

WHY IS GIT SO EVIL AND DANGEROUS????"
