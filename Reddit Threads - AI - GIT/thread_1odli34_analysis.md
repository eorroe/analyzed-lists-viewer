# REDDIT POST ANALYSIS

A user going by u/Basic_Abroad_1845 asked the r/git community for advice on convincing their non-technical team to adopt git for version control. The team currently manages files by appending version numbers like "spreadsheet_v1" and "spreadsheet_v2," which the poster described as frustrating and error-prone. They wanted to start using git for config files, text files, and even Microsoft Office documents like .docx and .xlsx files, with a plan to build a simple GUI and eventually a background script that automatically commits changes. The poster noted that no one on their team codes or has ever used git before, so the main challenge was avoiding overwhelm while introducing a brand-new workflow. In an edit, they added that the team already uses SharePoint but not its built-in version control features, so they were considering using git just for config files while standardizing SharePoint for documents instead.

# REDDIT COMMENTS ANALYSIS

SharePoint / Office 365 / Cloud Tools Recommended (24 Comments - 199 Upvotes)
The largest and most upvoted cluster argued that the team should stick with tools already built for Office documents rather than forcing git onto non-technical users. Many pointed out that SharePoint, OneDrive, Google Drive, and Office 365 already have automatic version history, change tracking, and collaboration features that work out of the box. u/exile_10 asked, "Surely SharePoint is the answer for common Office files?" and u/SwimmingDownstream highlighted that "SharePoint handles the versioning sharing, history and change tracking, permission handling for office files. You can have different folders as repos. it has a gui anyone can figure out." Several commenters noted that cloud tools sync automatically and require no training, making them far more practical for a team that does not code. Others suggested Google Docs, Dropbox, or Notion as alternatives, with the general sentiment being that the team should use the right tool for the job instead of introducing unnecessary complexity.

Git Is Not the Right Tool for Non-Developers (29 Comments - 195 Upvotes)
A closely sized cluster shared personal experience supporting the view that git is too technical for non-programmers, especially when combined with binary Office files. u/Guvante wrote, "Honestly having supported lots of people on git I don't think it is the right tool for non-programmers," and u/Aware-Sock123 joked that if anyone on the team figured out how to push a change, "they'll probably just commit new files with _v2 anyways lol." Commenters described how merge conflicts, command-line workflows, and abstract concepts like branches and commits become barriers for people who just want to edit a spreadsheet. Some noted past failures trying to introduce git to non-engineering teams, with u/elbiot remarking, "Lol I tried this at my job 15 years ago. Git is amazing for plain text files used in code bases but it's the wrong tool for MS Office documents. Looking back i was very naive." The consensus was that git carries a steep learning curve and that asking non-technical users to learn it for basic document versioning would likely create more frustration than value.

Binary Files and Merge Conflicts Are Problematic (24 Comments - 69 Upvotes)
This cluster focused on the technical reality that Office documents are not plain text and do not behave well in git. u/AKostur explained, "What's not clear is whether you're talking about programmers, or other folk. Last I checked, git isn't great for versioning binary blobs (which with things named 'spreadsheet*', I suspect are binary files)." Several commenters noted that .docx and .xlsx files are actually zip archives containing XML, so git cannot show meaningful diffs or merge changes the way it does with code. u/FalconDriver85 asked, "But would you trust Jen from accounting diffing a part of an Excel file reading and comparing XML?" Others shared painful experiences, like u/TimonAndPumbaAreDead saying, "We stored SSIS packages - which are xml - in git. It was hell." The cluster emphasized that without true text-based diffs, users lose most of git's benefits and are left with large binary blobs, ballooning repository size, and confusing merge conflicts that non-technical users cannot resolve.

Git Works Well for Plain Text / Personal Success Stories (8 Comments - 42 Upvotes)
A smaller but enthusiastic cluster shared positive experiences using git specifically for plain-text documents, config files, and writing projects. u/shoretel230 wrote, "The only place where I'll actually disagree is writers and law makers. Tracking large text changes would be great for those use cases," and u/DevMahasen, identifying as a novelist, said, "I can't live without Git, but yes it is hard to get my tribe to see the light. Once they do though, you can see light dawning across their face." u/SoldRIP added that "Any job that deals with large amounts of incrementally changing plain-text" benefits from git. These commenters agreed that git excels with true text files and suggested converting documents to formats like Markdown or Fountain for screenplays, but they did not argue it was suitable for the average Office user.

Questions About the Approach (6 Comments - 5 Upvotes)
A handful of commenters pushed back on the premise of the post by asking what problem the team was actually trying to solve. u/ImDevinC asked, "What actual problem are you trying to solve? Using spreadsheet_v* isn't a problem if things are working correctly. It may not be ideal, but it sounds like you're trying to shoehorn a solution for a non-problem." u/Frequent_Simple5264 echoed this with "What is the problem you are trying to solve?" and u/EspaaValorum suggested clarifying whether the goal was tracking changes, keeping old versions, or maintaining an audit trail. The underlying point was that the team should diagnose their actual pain points before choosing a tool, because git might be solving a problem that does not exist or could be solved more simply.

Practical Git Advice (2 Comments - 11 Upvotes)
A very small cluster offered concrete suggestions for making git work if the team still wanted to try it. u/KAJed recommended, "Start a local repo. Start versioning things correctly. Show the team the benefits with real examples from your own data. Push to public repo all can access. Profit!" u/Grouchy-Friend4235 suggested using Tortoise Git as a Windows Explorer-integrated GUI to reduce typing, noting that the team would still need to learn checkout, commit, push, pull, and possibly merge. This cluster acknowledged the difficulty but offered the most direct implementation path if the poster decided to proceed.

(Total: 93 Comments - 521 Upvotes)

# TOP COMMENTS

## 100+ Upvotes

u/exile_10
"Surely SharePoint is the answer for common Office files?" (138 Upvotes) - https://www.reddit.com/r/git/comments/1odli34/convincing_team_to_use_git/nkusyvh/

## 80+ Upvotes

u/Guvante
"Honestly having supported lots of people on git I don't think it is the right tool for non-programmers." (81 Upvotes) - https://www.reddit.com/r/git/comments/1odli34/convincing_team_to_use_git/nkuujg5/

## 50+ Upvotes

u/whattteva
"Yeah, git is great for regular text files, but it ain't great for things that aren't plain text like Office files." (47 Upvotes) - https://www.reddit.com/r/git/comments/1odli34/convincing_team_to_use_git/nkuyvi7/

## 20+ Upvotes

u/AKostur
"What's not clear is whether you're talking about programmers, or other folk.  Last I checked, git isn't great for versioning binary blobs (which with things named "spreadsheet*", I suspect are binary files).   You might wish to use some other document management system." (28 Upvotes) - https://www.reddit.com/r/git/comments/1odli34/convincing_team_to_use_git/nkusgt5/

## 10+ Upvotes

u/meowisaymiaou
"Git doesnt work well with binary data (spreadsheets, general computing documents). It was designed specifically for plain text docs.  Docx, xlsx are zip files, and would be miserable to use in git


Turn on versioning with office, so spreadsheet tracks all changes.


And make a course of truth location: someplace online, like SharePoint (which also versions). So that the latest is available readily, and old versions as needed.  


Document versioning is well established in the existing tools" (14 Upvotes) - https://www.reddit.com/r/git/comments/1odli34/convincing_team_to_use_git/nkuuknq/

u/DevMahasen
"Novelist here. I  can't live without Git, but yes it is hard to get my tribe to see the light. Once they do though, you can see light dawning across their face." (11 Upvotes) - https://www.reddit.com/r/git/comments/1odli34/convincing_team_to_use_git/nkwavuc/

u/KAJed
"Start a local repo. Start versioning things correctly. Show the team the benefits with real examples from your own data. Push to public repo all can access. Profit!" (10 Upvotes) - https://www.reddit.com/r/git/comments/1odli34/convincing_team_to_use_git/nkurlq3/

# ORIGINAL POST

"I have the opportunity to convince my team we should use got for version control. This would be used for configs, text files, docx, and xlsx documents. Our team doesn't code, and have never used git.

Currently our "version" control is naming things spreadsheet_v1, v2 etc, it sucks. How would you approach this? I want to show some basic workflow that uses minimal typing, maybe a gui and eventually I write a small app like a cronjob that just checks certain folders on someone's laptop and when changes are made, commit changes to a central git repo for various types of documents.

Appreciate any input, I'm a bit lost on how to not overwhelm the team here.

EDIT:
Thanks all for the input, it is all very helpful. We do use sharepoint today, but sub-optimally I suppose since we aren't using the built in version control and our team structure is all over the place. Seems like standardizing that might be a stronger option, and use git strictly for our config files. Thanks all!"
