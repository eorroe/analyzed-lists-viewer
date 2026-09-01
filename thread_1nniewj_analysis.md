# REDDIT POST ANALYSIS

A software engineer named u/Zandercat_ posted in r/git asking for help with an upcoming presentation to their boss about why their department should adopt version control using Git and Azure DevOps. The original post is from an "antiquated" software engineering department that currently doesn't use version control at all, and the poster is worried that speaking only in technical terms about branching, collaboration, and pull requests won't convince management or a review board. They specifically asked for hard statistics, research results, or "business speak" to back up the case, noting that the topic seems so obvious in software development that published papers are hard to find. The post received 205 upvotes and sparked 168 real comments, with the community overwhelmingly reacting with disbelief that any software team still operates without version control in 2025.

# REDDIT COMMENTS ANALYSIS

Business Value & ROI (37 Comments - 151 Upvotes)
The largest group of commenters focused on translating technical benefits into business language that managers actually care about. They emphasized framing Git as a tool for accountability, risk reduction, cost savings, and disaster recovery rather than as a developer convenience. u/pseudometapseudo received the most upvotes in the thread by explaining that version control provides a "paper trail" and reversibility, which are things management values. Other commenters suggested using terms like "compliance," "security," "standard," and "reproducible" to land the message. Several noted that the business case comes down to saving time and money, with one commenter suggesting a simple calculation: estimate how many hours developers currently waste manually sharing and reconciling changes, then multiply by their hourly rate to show the cost of staying without version control. Many in this cluster agreed that Git is decades-old, established technology used by 99% of software teams, so adopting it is about catching up to modern standards, not experimenting with something new.

Version Control Necessity (18 Comments - 268 Upvotes)
This highly upvoted cluster expressed strong disbelief that any software engineering department in 2025 could operate without version control, treating it as an absolute basic requirement rather than a decision that needs approval. Commenters compared it to a carpenter needing a hammer or a sanitation worker needing gloves — things that simply come with the job. u/Professional_Mix2418 wrote "Why do you even need to pitch it to your boss!? Its version control and management. Can't you as an engineering team make such decisions yourselves? Seems a very bad position to be in." Others noted that version control has existed since the 1970s with systems like SCCS, making the current situation roughly 50 years behind. Many in this cluster suggested that if the company doesn't already recognize this as essential, it may be a sign of deeper organizational problems, with some commenters bluntly advising the original poster to consider looking for another job.

Practical Implementation Advice (45 Comments - 156 Upvotes)
This cluster provided concrete suggestions for how to actually implement and present the case for version control. Commenters recommended starting with the hosting and budget conversation since paid services like Azure DevOps or GitHub Enterprise require financial approval, while noting that basic Git is free and can even run on a local network drive with no cloud costs. Several suggested using visual tools like GitHub Desktop or Atlassian SourceTree for demonstrations to make the concept accessible to non-technical people. Others recommended focusing on automation benefits: automated testing, continuous integration, and safer deployments. One commenter advised using a simple problem-solution-next steps format for the presentation, with real examples of past incidents where lack of version control caused problems. Many also suggested demonstrating Git directly during the presentation by showing side-by-side comparisons of current manual workflows versus what Git enables.

Humor & Off-topic (3 Comments - 71 Upvotes)
A small but highly upvoted cluster of humorous comments that mostly mocked the absurdity of the original situation through exaggeration. u/dashingThroughSnow12 joked that "once OP gets approval for version control, the next step is approval for text editors." Others contributed to the bit by referencing outdated technology like toggle switches on mainframes, TECO line editors, and Visual SourceSafe nightmares. u/chuckmilam posted a fake Windows filename representing manual version control chaos: "C:\users\bob\helloworld.html.v_1.2.4.5_DEC_2024 (13).txt". These comments lightened the tone while reinforcing the main point that version control is an obvious, decades-old standard.

Personal Experience & Anecdotes (28 Comments - 172 Upvotes)
Many commenters shared personal stories about working with or without version control to illustrate the business impact. One described a company merger where they discovered over 8 different versions of the same source code in the field, with no one knowing which was the real version, and another piece of software that kept reintroducing old bugs because previous fixes weren't in the current deployed version. Another shared a story about code that was supposedly "on Dave's old machine" after Dave left the company, and that machine couldn't be found. Others described current or former workplaces where developers shared files via FTP, email attachments, or a single person who collected updates manually, calling these situations "nightmares." A common theme was that source control acts as insurance for the business: if a developer leaves, their laptop dies, or a customer reports a critical bug, the company isn't crippled.

Questions & Clarifications (27 Comments - 239 Upvotes)
This cluster contained direct questions to the original poster about their current workflow, pushback on assumptions in the post, and requests for more details. Several asked "How are you doing this today?" and "What do you mean, text editor?" expressing genuine confusion about how a software team functions without any version control. Others questioned whether the poster had confused Git with a programming language, or whether management really needed to approve basic development tools. A few commenters asked for specifics about the team size, current file-sharing process, and whether they had experienced actual disasters from the lack of version control, noting that concrete examples would strengthen the business case. Some also clarified that Git itself is free and open source, while hosting services like Azure DevOps or GitHub may have costs.

Other (10 Comments - 19 Upvotes)
A small cluster of comments that didn't fit cleanly into the other categories, including brief agreements, deleted or anonymized posts, and miscellaneous suggestions. Some commenters mentioned specific resources like the Google State of DevOps report, DORA metrics, or Joel Spolsky's "12 steps for better software" as evidence-backed references. A few suggested using AI tools to rewrite the presentation in executive-friendly language. Others made quick jokes or one-line observations without expanding into the main discussion themes.

(Total: 168 Comments - 1076 Upvotes)

# TOP COMMENTS

## 200+ Upvotes

u/pseudometapseudo
"I think you can make the case by "translating" the benefits of git into things management cares about:
- version control means accountability, since it's clear who is responsible for any change
- it's basically the equivalent of a paper trail of every change, something management usually values
- it makes things reversible, so changes in product requirements can be dealt with much more easily
- git is not a fancy new thing, but a decades old, established solution used by 99% of software engineering teams. You are not doing experiments but catching up to modern standards." (236 Upvotes) - https://www.reddit.com/r/git/comments/1nniewj/presenting_git_to_my_boss_struggling_to_talk/nfkq0p7/

## 100+ Upvotes

u/Professional_Mix2418
"Why do you even need to pitch it to your boss!? Its version control and management. Can't you as an engineering team make such decisions yourselves? Seems a very bad position to be in." (108 Upvotes) - https://www.reddit.com/r/git/comments/1nniewj/presenting_git_to_my_boss_struggling_to_talk/nfko1ca/

## 80+ Upvotes

u/ps_cubensis
"Went into this thread assuming it was another "how do I convince my company to switch from X to Git?". But then realized that is is the question is about having a version control system at all 😳
Isn't this the same as being a carpenter and needing to pitch the need of a hammer in you daily work?" (89 Upvotes) - https://www.reddit.com/r/git/comments/1nniewj/presenting_git_to_my_boss_struggling_to_talk/nfkqnwr/

## 50+ Upvotes

u/dashingThroughSnow12
"Look, once OP gets approval for version control, the next step is approval for text editors." (53 Upvotes) - https://www.reddit.com/r/git/comments/1nniewj/presenting_git_to_my_boss_struggling_to_talk/nfkrwmk/

## 40+ Upvotes

u/Dan_Linder71
"☝️☝️ Hey OP, this is the "business speak" you're looking for ☝️☝️

But more to the discussion others are having, if you replace 'git' with 'Python' or 'C' or whatever language you use, does management have the same oversight and input on it? 

Just using git is normally a programming and development team decision and management accepts it as part of their preferred work environment.  

The business type decisions that you should keep management involved in are the financial and legal responsibilities it might bring up. Probably not many legal challenges adding a get workflow to your team, but adding a subscription cost to have a get repository with vendor support might be a legal requirement as well as additional financial burden to company. You could save a lot of the financial costs by using the unlicensed community version of gitlab or GitHub and host them on your own servers either in the cloud or on premise, that then requires a couple on your team being proficient in troubleshooting and recovering that server. Should it have issues. There are benefits to having a vendor supported subscription model for something as critical as your git repository server." (42 Upvotes) - https://www.reddit.com/r/git/comments/1nniewj/presenting_git_to_my_boss_struggling_to_talk/nfkyd9z/

## 30+ Upvotes

u/Ayjayz
"Don't even mention it to your boss. All the engineers should just start using git. He really doesn't have to know how you guys are doing your job, any more than he needs to know which text editor you're using." (30 Upvotes) - https://www.reddit.com/r/git/comments/1nniewj/presenting_git_to_my_boss_struggling_to_talk/nfkozed/

## 20+ Upvotes

u/chuckmilam
"C:\users\bob\helloworld.html.v_1.2.4.5_DEC_2024 (13).txt" (28 Upvotes) - https://www.reddit.com/r/git/comments/1nniewj/presenting_git_to_my_boss_struggling_to_talk/nfl3vcj/

## 10+ Upvotes

u/anonymous-red-it
"With your traditional process.

Estimate the time it would take for you to share your changes with the entire team

Estimate the time it would take to resolve a conflicting change across the team

Estimate the time it would take to review a single change 

Scale that up to one month and compare that to the amount of time it would take if everyone was using control.

Time is money, that should be plenty of justification from a business perspective.

Do a simple demonstration of each of those things to prove it's not just talk." (16 Upvotes) - https://www.reddit.com/r/git/comments/1nniewj/presenting_git_to_my_boss_struggling_to_talk/nfku5ii/

# ORIGINAL POST

"Hi all. At the end of this  week I'll be giving a short presentation about why I think we, as a software engineering department, should be using version control. Namely Git and Azure Devops as our remote repo.

l've so far drafted why it would make sense in terms of the development process such as branching, collaboration, history and pull requests, but I'm worried that I am only speaking to the development angle and not in terms of business talk. Things like hard stats, or research results seem to be quite hard to find to back up my intuition. Even if he agrees with me, I suspect it will need to be brought forward to a review board and the tech speak may be a bit hard to land on people who dont understand as much.

I have had a look around and perhaps it is such a given that software development is better with a version control system that there a few reasons to prove this with papers drawing upon the same conclusion?

I really want to make sure I hit this out of the park as the department is an antiquated one and I suspect there will be resistance to a "new" idea. It has the potential to improve our development experience and I think would look fantastic in interviews, should I want to leave later down the line.

Has anyone had a similar pitch go successfully? Or any resources that may help my case"
