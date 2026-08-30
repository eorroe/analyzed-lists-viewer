# REDDIT POST ANALYSIS

A post in r/git by GitKraken shared a simple but powerful habit: spend an extra 30 seconds writing clear commit messages that explain what changed and why. The author explained that their team used to write throwaway messages like "fix stuff" or "oops," which made debugging difficult months later. After switching to descriptive commit messages, they could follow the story of their codebase without digging through diffs. They also mentioned Conventional Commits as an option for even more structure. The post asked the community for other small Git habits that improved their workflow. It earned 355 upvotes and sparked 121 comments, with many readers sharing their own commit message standards, tool integrations, and debugging tips. Overall, the discussion was largely constructive: about 31% of comments were positive, 55% were neutral questions or factual statements, and 15% were skeptical or critical. The 117 real comments drew 491 total upvotes, with an average of about 4 upvotes per comment. The most active participants were u/HommeMusical with 7 comments, u/moodswung with 6, and u/elephantdingo666 with 6, while the highest-upvoted single comment came from u/dnult with 103 upvotes for suggesting that including user story numbers in commit messages adds useful cross-referencing.

# REDDIT COMMENTS ANALYSIS

Commit Message Practices & Support (27 Comments - 146 Upvotes)
Many commenters agreed that clear commit messages are a basic but essential practice, and several shared their own formats and standards. One top comment noted that putting the user story number in the commit provides a useful cross-reference without replacing a good description. Others mentioned using Conventional Commits, writing long-form messages with summaries and explanations, and treating commit messages as documentation for future team members. A few cautioned against relying solely on ticket IDs since those can change when companies switch issue trackers.

Tool Integrations (Jira, GitLab, etc.) (11 Comments - 55 Upvotes)
Several readers described how their teams connect commits and branches to project management tools like Jira, GitLab, Bitbucket, and Azure DevOps. One popular setup names branches after Jira tickets and uses a GitLab bot to automatically post merge request links back into Jira tasks. Others noted that modern platforms can auto-link ticket numbers in commit messages or create traceability between issues, PRs, and code changes.

Skepticism / Criticism / Mocking (19 Comments - 71 Upvotes)
A notable portion of the thread pushed back on the post, with some commenters calling it "engagement bait" or saying the advice is so basic it should already be common sense. A few mocked GitKraken for treating commit messages as an afterthought despite developing Git tooling. Others argued that the premise sounds like a fake story designed to promote the author's products. One commenter sarcastically noted that "life improved when you took care and actually wrote meaningful commit messages? Well, I never!"

Git Bisect / Debugging Tips (13 Comments - 117 Upvotes)
A large chunk of the discussion shifted to git bisect, with several commenters describing it as a binary search through commits to find exactly when a bug was introduced. One top comment explained that bisect requires a known good and bad commit, then repeatedly checks out the middle commit and asks you to mark it as good or bad until the culprit is found. Others added that you can automate the process with `git bisect run` if you have a test script, and that this tool is especially valuable when debugging large codebases or tricky dependency issues.

Squash / Merge Workflow Debate (16 Comments - 35 Upvotes)
This cluster gathered comments about whether to keep individual commits or squash them before merging. Some argued that squashing cleans up messy histories and keeps the main branch tidy, while others insisted that squashing destroys valuable context about how a change was developed. One detailed response described decomposing work into multiple focused commits that tell a story for reviewers, and lamented that squash merges erase that history. The debate touched on long-running branches, feature workflows, and when squashing is appropriate versus when it hides useful information.

AI / Automation for Commit Messages (13 Comments - 8 Upvotes)
Several commenters mentioned using AI or scripts to generate commit messages, from LLMs like Copilot to custom scripts and command-line tools. Some found these helpful for drafting messages quickly, while others mocked the idea or argued that taking 30 seconds to write your own message is faster than setting up AI tooling. A small side discussion compared file-name-only commit messages to LLM-generated ones, with little consensus.

Branch Naming Conventions (8 Comments - 20 Upvotes)
A handful of comments focused specifically on naming branches after ticket numbers, with mixed reactions. Some teams use patterns like `JIRA-1234-short-description` or `work-1234-short-description` and find it helpful for tracking. Others argued that coupling branch names too tightly to ticketing systems is bad practice and that a short descriptive name is more useful than a bare ticket number.

Alternative Git Habits & Tools (2 Comments - 29 Upvotes)
A few commenters shared different Git habits, such as tying PRs to Jira tickets and using git blame to understand why code was written, or cleaning up feature branches before merging. These suggestions were presented as complementary approaches rather than replacements for good commit messages.

General Agreement & Best Practices (8 Comments - 10 Upvotes)
Several short comments expressed general support for the original advice, noting that writing good commit messages is standard practice, that it benefits your future self, or that it helps during code reviews. Others mentioned personal habits like using git stash for experiments or maintaining clean commit history as a form of self-review.

(Total: 117 Comments - 491 Upvotes)

# TOP COMMENTS

## 10+ Upvotes

u/dnult
"Putting the user story number in the comment also helps. Its not a substitute for a good comment, but does provide a cross reference to additional info. It also helps with writing release notes." (103 Upvotes) - https://www.reddit.com/r/git/comments/1ohjlmf/the_30second_habit_thats_saved_us_hours_in/nlod48x/

# ORIGINAL POST

"We used to treat commit messages like throwaways: "fix stuff" here, "oops" there.

It was fine… until we had to debug six months later and had no idea what "stuff" was fixed.

Now, our team spends an extra 30 seconds writing clear commit messages that explain what changed and why. Our team can finally follow the story of the codebase without spelunking through diffs.

Want to add even more context? Use Conventional Commits to prefix your commits. They even make generating changelogs and bumping semver easy.

It's wild how such a small habit changes collaboration speed.

Anyone else have a "tiny Git habit" that completely changed your workflow?"
