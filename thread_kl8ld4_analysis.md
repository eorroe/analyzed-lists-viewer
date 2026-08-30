# REDDIT POST ANALYSIS

In r/git, user felipec posted an AMA (Ask Me Anything) thread titled "I've been a Git developer since 2009. AMA." The post explains that felipec has contributed to Git since 2009, with work including small patches like the `@` shorthand, and larger projects such as git-remote-hg and git-remote-bzr (bridges between Git and Mercurial/Bazaar). He also built the zsh completion for Git, created tools like git-smartlist and git-reintegrate, and was featured in Git Rev News edition 70. The post earned 121 upvotes and generated 117 comments, with the community eager to ask about Git's user interface, workflow choices, and the challenges of contributing to such a mature project.

# REDDIT COMMENTS ANALYSIS

## UI/Porcelain & Git Pull (53 Comments - 149 Upvotes)
The largest conversation thread revolved around Git's user interface, which many users find confusing and inconsistent. felipec explained that the difficulty in improving Git's interface stems from the culture of the development team: long-time Git experts often don't see the usability problems that newcomers face. He noted that Git User Surveys consistently show the UI as the top area needing improvement, yet there is significant resistance to change and no major company funding UI work. The discussion also dove deep into the `git pull` command, with felipec proposing a three-mode system and explaining why the current default causes problems for most users. u801e pushed back with detailed scenarios about wanting to preview changes before applying them, leading to an extended back-and-forth about whether Git should be more interactive by default. The thread also touched on related topics like triangular workflows, the `git switch` and `git restore` commands, and whether better alternatives like Magit or Fugitive solve the problem or just shift it elsewhere.

## Q&A Session (24 Comments - 118 Upvotes)
This cluster contains direct questions posed to felipec and his responses covering a wide range of topics. When asked about his biggest regret, felipec replied: "I don't regret anything. The past cannot be changed, and the only time where we can do something is the present." On the Vim versus Emacs debate, he firmly sided with Vim: "Vim all the way. My fingers are way too used to it. I can't use anything else." He shared his setup of zsh and vim on Arch Linux with no IDE, explained how he got started with Git (about 4 years of use before contributing), advised newcomers to subscribe to the Git mailing list, and revealed that nobody has ever paid him to work on Git — all contributions were done in his free time. He also addressed the master versus main branch naming debate, code review preferences (favoring email patches over pull requests), and how Junio Hamano tracks bugs and features through the mailing list rather than dedicated tools.

## Deleted/Unknown (4 Comments - 60 Upvotes)
Four comments were removed by moderators or their authors before the data was archived, leaving only the metadata and upvote counts visible. The most notable was a top-level comment with 52 upvotes whose original content is no longer accessible. Three other deleted comments had much lower scores (6, 1, and 1 upvotes). Without the original text, their topics cannot be determined, though their placement in the thread suggests they were either questions, answers, or discussion contributions that were later removed.

## Humor/Off-topic (6 Comments - 52 Upvotes)
A small but lively thread emerged when a user asked "What's porcelain?" and another realized the Git terminology is a toilet metaphor: "I may have just realised that it's all a toilet metaphor." The conversation playfully continued with jadkik94 asking "In this context, the code would be shit? :D" and CoolioDood responding "In my experience it usually is haha." dotancohen pointed out that these metaphors are used extensively in the official Git Book, which he recommends for learning despite not being concise. The humor provided a light break from the heavier technical discussions while still being about Git's terminology.

## Technical Git Workflows (29 Comments - 51 Upvotes)
Several comments covered practical Git workflow questions. felipec discussed force pushing, explaining that it is safe on personal feature branches but dangerous on long-lived shared branches like master. He shared his alias setup using gitk and git-smartlist to visualize upstream changes. The thread touched on code review practices, with felipec strongly preferring email-based patches over GitHub pull requests, citing Linus Torvalds' criticism that "the pull requests are just pure garbage." There was also discussion about bare repositories, which felipec said are not meant for everyday work but for specific use cases like shared infrastructure. paul_h shared links about Subversion merge tracking limitations, and the group discussed Git's object model and what features might be missing compared to systems like Mercurial.

## Thanks/Appreciation (5 Comments - 22 Upvotes)
A handful of comments expressed gratitude for felipec's work. One user noted that the git-reintegrate tool "was unknown to me but solved a problem that my team has struggled with for a long time." Another simply wrote: "Thank you for your contributions to the tool I use everyday!" felipec responded with "You are welcome!" to several appreciative comments. These messages highlighted the real-world impact of his open-source contributions, with users discovering his tools and finding them genuinely useful in their daily development work.

(Total: 121 Comments - 451 Upvotes)

## Sentiment Analysis
Roughly 34% of comments were positive, 48% neutral, and 18% negative. The discussion was overwhelmingly constructive, with most users either asking thoughtful questions, sharing appreciation, or engaging in detailed technical debate. Even the disagreements, such as the extended back-and-forth about `git pull`, remained civil and technical in nature.

## Engagement Metrics
- **Total comments analyzed:** 121
- **Total upvotes across analyzed comments:** 451
- **Average upvotes per comment:** 3.7
- **Most upvoted comment:** u/felipec's "Vim all the way. My fingers are way too used to it. I can't use anything else." (17 upvotes)
- **Top contributing user:** felipec (the OP), who authored the post and the majority of answers, with multiple highly-upvoted responses

## Keywords
The discussion centered around: git, porcelain, UI, user interface, git pull, fetch, merge, rebase, felipec, Vim, workflows, triangular, master/main, patches, mailing list, email, force push, bare repositories, Git User Survey, switch, restore, completion, open source, contributions, regret, GUI, GitKraken, GitHub, GitLab, Gerrit, pull requests, code review, staging area, fast-forward, conflicts, feature branches, TBD, gitflow, Mercurial, Bazaar, CVS, Subversion, ClearCase, Monotone, Perforce, Linus Torvalds, Junio Hamano

# TOP COMMENTS

Each entry below is the verbatim text of the top comment in that upvote range, copied exactly as it appears on Reddit.

## 50+ Upvotes

u/[deleted]
"[deleted]" (52 Upvotes) - https://www.reddit.com/r/git/comments/kl8ld4/ive_been_a_git_developer_since_2009_ama/gh7g5p7/

## 20+ Upvotes

u/dotancohen
"First off, thank you for your work.

Everybody acknowledges Git as the most versatile, professional version control software for large projects with many devs. But a near-universal criticism of Git is the porcelain. **Do you have any insight as to why no better porcelain is being developed?** Or might you consider e.g. Magit or Fugitive as a better porcelain so nothing is being done in Git itself?" (22 Upvotes) - https://www.reddit.com/r/git/comments/kl8ld4/ive_been_a_git_developer_since_2009_ama/gh7nav5/

## 10+ Upvotes

u/felipec
"> Do you have any insight as to why no better porcelain is being developed?

I believe it's a deep issue with the culture of the development team.

Most of the people developing git have been using git for many years, decades even. So any inconsistency in the UI is already part of their muscle memory.

Recently I’ve been talking about the curse of knowledge; the better you know something, the less you remember about how hard it was to learn. I think git developers who are already experts in git don't see it in the same way most users do; most don't see any big problem with the UI.

I do see a big problem, and I've been involved in the Git User Surveys made in the past, in which all of them the UI is always mentioned as the big area of improvement.

I've tried to improve the UI in different areas, most importantly I've tried to change "git pull", and even introduced a "git update" command. But it feels like fighting an iceberg because first I need to convince developers who don't see any issue that there's an issue, then I need to convince them that my solution is better than other solutions, then that my solution is implemented correctly and it's not missing anything (e.g. configurations, tests, or documentation), then address any suggestions for improvement which sometimes lead to disagreements, and friction, then it gets forgotten.

I do think there's too much resistance to change in the UI, and no company (e.g. Google or Facebook) is paying any developer to try to improve it.

> Or might you consider e.g. Magit or Fugitive as a better porcelain so nothing is being done in Git itself?

I have been considering another porcelain myself since I think improving the current UI at this point is next to impossible (although I'm still trying)." (19 Upvotes) - https://www.reddit.com/r/git/comments/kl8ld4/ive_been_a_git_developer_since_2009_ama/gh7xlf8/

# ORIGINAL POST

"I've been a Git developer since 2009. AMA.

I've contributed to git since 2009, mostly small patches here and there, like the introduction of the `@` shorthand.

However, I've done some big stuff too, like [git-remote-hg](https://github.com/felipec/git-remote-hg), a bidirectional bridge between Git and Mercurial. Also [git-remote-bzr](https://github.com/felipec/git-remote-bzr).

I've also contributed a lot to the bash completion, and I'm the one that created the zsh completion.

Additionally, I have many separate tools, like [git-smartlist](https://github.com/felipec/git-smartlist), [git-reintegrate](https://github.com/felipec/git-reintegrate), [git-related](https://github.com/felipec/git-related).

I was just featured in the last [Git Rev News](https://git.github.io/rev_news/2020/12/26/edition-70/), so I thought; why not create an AMA?

Ask me anything."