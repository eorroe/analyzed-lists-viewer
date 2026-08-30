# REDDIT POST ANALYSIS

A web developer named Haaldor posted in r/git saying they've tried learning Git six times but still don't see how it improves their workflow. They currently use two permanent branches (Main and Test) for a basic website, and whenever they make a change, they manually copy files to the server and compare them by content — sometimes 1-3 times per minute. They call this copying process a "commit." They also sometimes need separate server copies with partial files and permanent custom changes. They ask: "Am I missing the point somewhere?" and whether Git "simplifies the workflow at all, or is it adding more work but the safety it adds is worth additional work?"

# REDDIT COMMENTS ANALYSIS

## Core Correction: Git is Version Control, Not Deployment (9 Comments - 78 Upvotes)
Most commenters quickly pointed out that the original poster is mixing up version control with deployment. The top commenter, DanLynch, wrote: "This is not how Git is supposed to be used. Git is not a deployment system: it's not designed to take care of your servers and keeping them configured properly. It's a version control system for source code." Another noted, "If you understand that git is version control, then you're already done. What you need to learn next is CI/CD." Several people emphasized that Git is meant to track code changes over time, not to copy files to servers. One deleted commenter simply replied "Yes" to the question of whether the poster was misunderstanding Git. Others shared that they'd seen senior programmers who just copy folders and regretted it, and one person noted that "Using it will save time much more than you will spend in learning it."

## CI/CD and Deployment Tools (11 Comments - 39 Upvotes)
A large group of commenters suggested that what the poster actually needs is a CI/CD pipeline, not a better Git workflow. One wrote: "What you want is a CI / CD pipeline. You push to git, it builds your project in multiple variants (staging / prod) then it optionally deploys your files to your servers." Another added: "(which would be 'GitHub Actions' on GitHub)." People shared real examples: one uses Netlify to auto-deploy when code is pushed to main, another uses three branches with GitHub Actions triggering builds, and someone else explained that CI/CD ensures consistent builds across different developers' machines by using a controlled container. One person recommended the 12-factor app methodology at https://12factor.net/ for understanding environment configuration.

## Workflow and Branching Best Practices (14 Comments - 42 Upvotes)
This group dove into the details of how Git branches and environments should actually work. The second-highest commenter, Trigus_, explained that the problem is in the workflow: "You shouldn't adjust the written code to your environments (prod, dev, feature-x, etc.), but have a way to adjust the runtime behaviour (e.g. displaying different text) through things like environment variables." They suggested that the exact commits made on dev should eventually end up in the main branch. DanLynch shared his Android development workflow where Jenkins retrieves code from Git and compiles it, but the deployment steps don't involve Git at all. Others suggested using git worktree for multiple checkouts, Docker for containerized deployments, Apache virtual hosts instead of different branches for different servers, and mocking databases for local testing. One person shared a link to the Git Flow branching model at https://nvie.com/posts/a-successful-git-branching-model/. Another wrote a detailed step-by-step guide showing how to clone, branch, commit, and push in Git.

## OP Questions and Acknowledgments (4 Comments - 9 Upvotes)
The original poster, Haaldor, engaged actively in the thread with follow-up questions. They wrote: "That's... Fair, I guess. Still hard for me to wrap my head around, but to truly understand Git I need to understand that version control and deployment should be separate." They asked what the "professional" workflow looks like after pushing to main, and whether they should set up Git on the server to pull after every commit. They also noted: "Not gonna lie, since I started writing this post I felt more and more uneasy with what my workflow is" and later thanked a commenter: "Thanks for the answer! It gave me insight in what to read about more to learn the capabilities of Git and how it may fit into real development."

## Humor/Off-topic (1 Comment - 1 Upvote)
One commenter simply replied with a laughing emoji: "🤪"

## Redacted/Deleted and Low-Value Comments (8 Comments - 11 Upvotes)
Several comments in this thread were either deleted, removed, or contained minimal content. These included four deleted or removed comments, two comments that were mass-redacted with random text, and a few very short responses like "true" and "Good luck. I only use git a few times a day."

(Total: 47 Comments - 180 Upvotes)

# TOP COMMENTS

## 50+ Upvotes
u/DanLynch
"This is not how Git is supposed to be used. Git is not a deployment system: it's not designed to take care of your servers and keeping them configured properly. It's a version control system for source code.

Any time you find yourself wanting different files in different branches (and to keep them that way permanently), you are probably doing Git wrong. And if you rely on Git to copy files from your local workstation to your production server, you are definitely doing Git wrong." (52 Upvotes) - https://www.reddit.com/r/git/comments/1fxtni7/real_life_usage_of_git/lqp6so8/

## 10+ Upvotes
u/Trigus_
"I feel this warrants a longer answer, but the problem lies in your workflow. You shouldn't adjust the written code to your environments (prod, dev, feature-x, etc.), but have a way to adjust the runtime behaviour (e.g. displaying different text) through things like environment variables or arguments passed to the program.  
This means that the exact commits that you made on the dev or feature branch will eventually end up in the prod (main/master) branch (maybe in a squashed form)." (16 Upvotes) - https://www.reddit.com/r/git/comments/1fxtni7/real_life_usage_of_git/lqp8v1n/

# ORIGINAL POST

"I've been trying to learn Git for a long time and this is my 6th time trying to do a project using Git and Github to learn it... But honestly, I can't wrap my head around it.  
I really can see the pros of version control system like Git, but on the other hand, I just can't get rid of the feeling that additional hours of work needed to use it are not worth it over just... having multiple folders and backups.

I feel like I'm misunderstanding how Git works, taken how it's basically a world-wide standard. Based on following workflow that I'm used to, how is Git improving or simplifying/automating it?

Workflow I'm used to (let's make it a basic HTML + JS website with PHP backend, to make it simple):  
The project has 2 permanent branches - Main and Test.

* Main is version of website visible for everyone, it needs to be constantly working. Terminology here would be "production", if I'm not mistaken.
* Test is my testing environment, where I can test new features and do fixes before pushing the changes to Main as a new version.

Some of the files in branches need to be different - as the Test website should have at least different name and icon than the Main one.  
Whenever I make changes to the Main or Test branch I need that to be reflected on the website, so whenever I change something, I copy the files to the server. If I'm not mistaken, the terminology for it is "commit" - during bugfixing and feature testing I need to copy those files on average 1-3 times a minute.  
Copying files means comparing files by content (in my case, using TotalCommander's Compare by Content feature).

On top of that, sometimes I need to create new branches for website copy on different servers. Those copies only need part of the files from Main branch, but not all of them - and after creating such copy sometimes I need to add new custom changes on top of them, so they diverge from Main branch instantly. Those branches are not kept on my server, contrary to Main and Test versions.

In my eyes, this is the most basic usage of Git, but in my current workflow it seems to be much slower than just doing it by hand (and in some cases, impossible - like in different files for production and Test, or having updates automatically reflected at the website without manual updating the server). Am I missing the point somewhere?  
And, generally, in your opinion - is Git simplifying the workflow at all, or is it adding more work but the safety it adds is worth additional work?"
