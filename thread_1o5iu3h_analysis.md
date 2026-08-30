# REDDIT POST ANALYSIS

A discussion sparked in the r/git community after news broke that Git developers are potentially planning to release Git 3.0 by the end of next year. The post, shared by u/Jordi_Mon_Companys, links to a Phoronix article about the upcoming release talk and has earned 314 upvotes. The news centers on a major version change that would introduce breaking changes, mandatory Rust in the build process, and a shift away from SHA1 hashes. Since the post went up on October 13, 2025, it has drawn 77 comments — though 6 were later deleted or removed — with the community splitting into several lively debates about versioning, security, Rust adoption, and even the name "git" itself.

# REDDIT COMMENTS ANALYSIS

Humor, Memes & Lighthearted Reactions (19 Comments - 157 Upvotes)
The largest group of comments treated the news with playful banter, inside jokes, and meme-style replies. The top comment in the entire thread — with 94 upvotes from u/gregdonald — joked about putting the release on a calendar: "Fourteen months from now, a thing is probably going to happen." That comment spawned a small cascade of replies, including u/gregdonald's own follow-up sharing a fake upgrade bash script, and a "RemindMeBot" automatically posting a reminder for one year later. Other lighthearted remarks ranged from references to "Tech Tips" and Les Misérables ("Do you hear the people sing?!") to jokes about Linus Torvalds being the "big new feature in Git 3.0." One particularly vivid comment from u/PartBanyanTree compared git to the character Rimmer from Red Dwarf — grumpy, difficult, and yet somehow lovable. The humor thread also absorbed a brief side conversation about merge conflicts, where u/Saltillokid11 quipped "git ai fix my conflict" and others suggested non-AI alternatives like mergiraf.org.

Concerns About Breaking Changes & Versioning (7 Comments - 138 Upvotes)
A smaller but highly upvoted cluster focused on the risks of a major version bump. u/efalk voiced a common worry with 47 upvotes: "Major version # changes makes me nervous. What's 3.0 going to have, and more importantly, what's it going to break?" The discussion was bolstered by u/elephantdingo, who explained with 48 upvotes that "Part of purpose of the discussion is indeed to give a heads up to the wider community that a breaking version change is coming in the not-distant future." Another user linked directly to Git's official BreakingChanges documentation, while u/i860 compared the situation to the Python 3 transition, warning it could "cost the general industry 100s of millions of dollars in wasted time." The cluster also included practical concerns about object databases and filesystem changes, with u/FingerAmazing5176 noting that "Git itself is fine but 3rd party support is slow on the uptake."

Rebase Discussions (6 Comments - 14 Upvotes)
A focused technical thread debated whether changing git's default pull behavior to rebase would cause problems. u/Guvante warned that if someone has their own fork set as origin, rebasing could "rebasing the real branch on top of their changes." u/RevRagnarok pushed back with 5 upvotes, arguing that "pull --rebase does _nothing_ that can affect any other user in a detrimental way" and that the real concern is only when you rewrite history others have already seen. The conversation included detailed back-and-forth about branching, conflict resolution, and whether rebase truly changes anything behind the scenes, with most participants agreeing the fear of rebase is overblown for everyday use.

SHA1/SHA256 & Hash Security (9 Comments - 48 Upvotes)
Several comments dug into the security implications of moving away from SHA1. u/emaxor asked whether the new hash would actually stop exploits, suggesting collisions would only produce "junk bytes, not malware." u/carsncode corrected this with 25 upvotes, explaining that "they don't have to choose, they'd use both" — an attacker could combine regular malware with junk bytes to create a collision intentionally. u/PurepointDog pointed out that "There are feasible attacks based on collisions," while u/huntermatthews noted that regulated industries like government, banking, and medical have already mandated dropping SHA1. The discussion touched on the broader frustration that this conversation has been ongoing for years, with u/Moscato359 simply commenting "So tired... so, so tired."

Rust in Git (23 Comments - 65 Upvotes)
The largest thematic cluster revolved around Git's plan to require Rust as part of its build process in version 3.0. The debate was heated and personal. u/UnbeliebteMeinung stated bluntly with -34 upvotes: "I will never use git-rust. I hope there will be a git-free-rust alternative." Others pushed back, with u/0-R-I-0-N asking "Are you a contributor to the git source code and don't like writing rust or how does rust impact you as an end user? Rust is just a language." u/elephantdingo offered the pithy observation that "people least affected by change [are] most vocal about it happening" and later argued that since there is almost no Rust code in Git outside maybe contrib/, the opposition is likely "purely ideological." u/bigkahuna1uk asked for specifics, prompting a deeper dive into the Rust requirement. u/arjuna93 raised a legitimate technical concern, explaining that Rust is broken on OpenBSD ppc and Darwin ppc, meaning "I literally can't install anything which requires it." Others clarified that Rust compiles to machine code so end users don't need a Rust compiler, but u/Rimrul countered that you still need a working compiler target for cross-compilation, and platform-specific targets like powerpc-unknown-openbsd are tier 3 at best. The thread also included references to Git's official documentation stating Rust will be mandatory for the build process, and a reminder from u/y-c-c that the Rust push started with xdiff, Git's diff engine licensed under LGPL, which means downstream projects like libgit2 and Vim would also be affected.

Name & Identity Discussions (6 Comments - 8 Upvotes)
A smaller side conversation debated whether "git" is a good name. u/Bladders_ asked, "Can they just change the name? Git sounds awful and British English is a word to describe an unlikeable character." u/Jordi_Mon_Companys defended it, noting that Linus Torvalds likely used it as a self-deprecating description of himself, while u/ilestalleou confirmed it was named specifically because of that British-English definition. u/PartBanyanTree expanded the analogy into a long, humorous comparison of git to Rimmer from Red Dwarf — temperamental, demanding, and yet somehow essential to the crew.

General Questions & Off-topic (4 Comments - 16 Upvotes)
A handful of comments veered into unrelated or meta territory. u/git0ffmylawnm8 asked, "Who are the developers? I just want to talk like a calm and reasonable individual," which prompted brief replies identifying Linus Torvalds (with others noting Junio Hamano is the current maintainer) and a reference to "Tech Tips." u/elven_mage expressed a desire for "an equivalent to mercurial's evolve," a feature request that did not spark further discussion in this thread.

(Total: 74 Comments - 446 Upvotes)
The sum of all X Comments values above equals the total number of comments analyzed. Every comment fetched has been assigned to exactly one cluster.

# TOP COMMENTS

## 90+ Upvotes

u/gregdonald
"Fourteen months from now, a thing is probably going to happen."

Thanks for the heads-up! I'll put it on my calendar. (94 Upvotes) - https://www.reddit.com/r/git/comments/1o5iu3h/git_developers_talk_about_potentially_releasing/nj9kmx8/

## 40+ Upvotes

u/elephantdingo
Part of purpose of the discussion is indeed to give a heads up to the wider community that a breaking version change is coming in the not-distant future. (48 Upvotes) - https://www.reddit.com/r/git/comments/1o5iu3h/git_developers_talk_about_potentially_releasing/nj9t9k1/

## 20+ Upvotes

u/carsncode
That's not how exploits work, they don't have to choose, they'd use both. It would take regular malware, plus junk bytes to create the collision, which wouldn't "just happen to collide", it'd be done intentionally, which is the whole purpose of upgrading algorithms, so that intentional collisions are harder to produce. (25 Upvotes) - https://www.reddit.com/r/git/comments/1o5iu3h/git_developers_talk_about_potentially_releasing/nj9ywbv/

## 10+ Upvotes

u/gregdonald
I said I was putting it on my calendar!

I even wrote myself an upgrade script to fix all my repos:

    #!/bin/bash
    
    find "$HOME" -type d -name ".git" -prune 2>/dev/null | while IFS= read -r GIT_DIR; do
        ( cd "$(dirname "$GIT_DIR")" && echo "Upgrading $PWD..." && git upgrade-version 3.0 )
    done (19 Upvotes) - https://www.reddit.com/r/git/comments/1o5iu3h/git_developers_talk_about_potentially_releasing/nj9xkht/

# ORIGINAL POST

"Git Developers Talk About Potentially Releasing Git 3.0 By The End Of Next Year"
