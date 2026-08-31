# REDDIT POST ANALYSIS

The original post in r/C_Programming, titled "Why do you use/don't use an IDE?" and written by user AxeForge, describes a personal journey from using a basic text editor and command line to switching to CLion as a C game engine project grew in size. The author specifically highlights that a "visual debugger" and "easy refactoring that's C/C++ specific" became essential for managing larger codebases, along with appreciating that everything is "setup out of the box." The post invites the community to share their own reasons for choosing or avoiding IDEs, sparking a broad discussion about tooling philosophy, workflow preferences, and the tradeoffs between lightweight editors and full-featured development environments.

# REDDIT COMMENTS ANALYSIS

[Pro-IDE Advocates] (23 Comments - 190 Upvotes)
This group pushes back against the idea that text editors are always superior, arguing that modern IDEs provide genuine productivity gains through integrated debugging, smart code navigation, and project-wide refactoring that are hard to replicate in a plain editor. Users point out that tools like CLion catch mistakes automatically - for example, one commenter notes that "If you use like clion or smth it makes it so that if you forget to make something a const or smth that shows up as a warning." Another highlights that "IDE does sooooo many things to assist me with coding" including instant function-definition popups, while others emphasize that IDEs lower the barrier for newcomers and keep everything in one place.

[Text Editor/Terminal Purists] (46 Comments - 123 Upvotes)
This is the largest cluster and the most vocal camp, insisting that lightweight editors like Vim, Emacs, and Neovim are faster, more customizable, and ultimately more powerful than any IDE for experienced developers. Commenters celebrate the raw speed and portability of terminal-based tools, with one praising "the sub millisecond response time that VIM has" and another stating "vim for everything to save RAM and fingers." Many argue that modern text editors paired with LSP servers like clangd provide most IDE benefits without the bloat, and several express frustration that IDEs get in their way with unwanted auto-completion and rigid workflows.

[Hybrid/Context-Dependent Users] (53 Comments - 107 Upvotes)
This pragmatic cluster takes a "best tool for the job" stance, using IDEs for certain languages or large projects while relying on terminal tools for others. One developer describes using CLion 90% of the time but switching to Visual Studio for Windows-specific driver work, while another uses VSCode for embedded development because of its plugin ecosystem and WSL support. Several note that their choice depends on project size, platform constraints, or whether they need to work remotely over SSH, making flexibility the core philosophy rather than loyalty to one category of tool.

[Build Process & Compilation Control] (17 Comments - 38 Upvotes)
A substantial technical thread focuses on how IDEs abstract away the build process, with some users valuing that convenience and others wanting explicit control over compiler flags, linker steps, and debugging commands. One commenter explains that "the big thing is control over the build process" and warns that IDEs can hide important details, while another counters that modern tools like CLion still use the exact command-line invocations you would run manually. The discussion also covers debugging workflows, with terminal purists describing how they use gdb and lldb directly - one admits "I just add 1 billion printf()s until I figure out where the bug is" - while others defend visual debuggers as essential for complex systems.

[Performance, Resources & Bloat] (4 Comments - -6 Upvotes)
A smaller but passionate cluster complains that IDEs are slow, resource-hungry, and built on unreliable foundations. One user gripes about Electron-based editors: "Do you really need to ship a container with a full fekin chromium instance just to run VSCode?" while another simply states "IDE's are bloat." These comments tend to be emotionally charged and focus on RAM usage, startup time, and the frustration of GUI crashes or forced workflows that ignore user preferences.

[Education, Learning & Personal History] (3 Comments - 7 Upvotes)
Several commenters trace their tooling preferences back to formative experiences such as college courses that banned IDEs, early exposure to Unix philosophy, or years of muscle memory built with specific editors. One explains that "A professor in my third semester at college demanded we didn't use an IDE and I never got fully used to using one again afterwords," while another notes that switching tools later in life feels like relearning everything from scratch. These anecdotes highlight how deeply ingrained editor habits become and why the choice often has less to do with objective feature comparisons and more with years of accumulated workflow.

**Sentiment Analysis:** Across all 146 comments, the overall sentiment breaks down as 26.0% Positive, 55.5% Neutral, and 18.5% Negative. The discussion is largely neutral and constructive, with most users calmly explaining their preferences, though a few exchanges become heated - particularly when users accuse each other of lying about typing speed or call opposing viewpoints "larp" and "sadistic."

**Engagement Metrics:** The thread contains 146 real comments (excluding 1 deleted comment) with a combined total of 459 upvotes, averaging 3.14 upvotes per comment. The most upvoted comment is from u/SoggyStress7785 with 57 upvotes. The top contributing users by comment count are: u/LordRybec (22 comments), u/neppo95 (9 comments), u/Reggie-Rectangle (5 comments), u/Loud_Anywhere8622 (4 comments), u/Ultimate_Sigma_Boy67 (4 comments).

**Top Keywords & Phrases:** The most frequently discussed terms in this thread include: "ides", "emacs", "code", "editor", "features", "project", "faster", "never", "visual", "projects", "text", "where", "terminal", "without", "always". These keywords reflect the community's focus on editor choice, build control, and the specific tools that define modern C development workflows.

(Total: 146 Comments - 459 Upvotes)
The sum of all comment counts above equals 146, which is the total number of real comments analyzed.

# TOP COMMENTS

Each entry below is the verbatim text of the top comment in that upvote range, copied exactly as it appears on Reddit. No summarization, paraphrasing, or layman's-terms rewriting is applied to TOP COMMENTS.

## 10+ Upvotes

u/SoggyStress7785
"I use IDE to browse code but I compile with the terminal." (57 Upvotes) - https://www.reddit.com/r/C_Programming/comments/1vqyo7y/why_do_you_usedont_use_an_ide/p49c8qf/

u/ScallionSmooth5925
"I don't like magic tools because then I don't know what exacly happened when I pressed the button " (53 Upvotes) - https://www.reddit.com/r/C_Programming/comments/1vqyo7y/why_do_you_usedont_use_an_ide/p4994md/

u/txdsl
"I’m revisiting C/C++ for grad school. Using neovim / gcc / gdb on Mac for most of my study.

Ive used various ides (vs, eclipse, IntelliJ) over my career but nothing has felt as seamless and out of my way as vim." (26 Upvotes) - https://www.reddit.com/r/C_Programming/comments/1vqyo7y/why_do_you_usedont_use_an_ide/p49dhrk/

u/Loud_Anywhere8622
"you're misunderstooding the point. He is not reffering to the visual that provide an IDE (aka text coloration nor repertories tree representation) but the compilation steps, which are far more obfusquated via IDE tool. Compilation flag, linker or assembly instructions for example, are not explicitly explain on most IDE tool, even diging through them." (22 Upvotes) - https://www.reddit.com/r/C_Programming/comments/1vqyo7y/why_do_you_usedont_use_an_ide/p49twvs/

u/zenthial
"Not really the case for most neovim/emacs users. IDEs still have not caught up to the level of customization that neovim/emacs users get. Any time I try to use a fancy new IDE (Zed, Cursor), they still struggle behind. Vim motions, git integration, file navigation are all worse in modern IDEs than emacs and nvim." (22 Upvotes) - https://www.reddit.com/r/C_Programming/comments/1vqyo7y/why_do_you_usedont_use_an_ide/p49m9aj/

u/neppo95
"Why wouldn't I use a tool that speeds up my work? I honestly don't get people that don't use them, unless it is for example VS Code fully set up, which technically isn't an IDE but can be setup as one." (21 Upvotes) - https://www.reddit.com/r/C_Programming/comments/1vqyo7y/why_do_you_usedont_use_an_ide/p49b9xr/

u/ScallionSmooth5925
"Exactly. I don't consider syntax highlighting and git integration an ide feature because basic text editors can do it." (18 Upvotes) - https://www.reddit.com/r/C_Programming/comments/1vqyo7y/why_do_you_usedont_use_an_ide/p4a0ebt/

u/dmc_2930
"Vim, yes. Pure vi? Sadistic!" (16 Upvotes) - https://www.reddit.com/r/C_Programming/comments/1vqyo7y/why_do_you_usedont_use_an_ide/p49hq0y/

u/EpochVanquisher
"I do the same and I think a lot of other people do. One of the nice things about this is how easy it is to pass different command-line flags to the program you’re running, or interact with it in other ways. " (14 Upvotes) - https://www.reddit.com/r/C_Programming/comments/1vqyo7y/why_do_you_usedont_use_an_ide/p4a9wlq/

u/Rough_Employee1254
"vi is all I need..." (13 Upvotes) - https://www.reddit.com/r/C_Programming/comments/1vqyo7y/why_do_you_usedont_use_an_ide/p49amdb/

u/Sergey5588
"too much for me ig, i have just nvim with clangd and tree plugin, and i use gdb for debugging" (11 Upvotes) - https://www.reddit.com/r/C_Programming/comments/1vqyo7y/why_do_you_usedont_use_an_ide/p49924u/

u/LordRybec
"Exactly.  People who think that IDEs are universally better than Vim or Emacs are people who don't actually know anything about Vim or Emacs.  (I don't even like Emacs, but I'd still use it over most modern IDEs.)" (10 Upvotes) - https://www.reddit.com/r/C_Programming/comments/1vqyo7y/why_do_you_usedont_use_an_ide/p4c12do/

# ORIGINAL POST

Title: "Why do you use/don't use an IDE?"

"I've tried using a text editor with just the command line and for the most part isn't wasn't so bad until my game engine got big enough. Then I switched to Clion because it just handles so much more for big projects. Biggest thing is a visual debugger and easy refactoring that's C/C++ specific. Not to mention everything is setup out of the box.

I'm curious about other's reasons for using or not using an IDE."
