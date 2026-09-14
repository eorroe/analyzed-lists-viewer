# REDDIT POST ANALYSIS

The Reddit post titled "Google dropped a 68-page prompt engineering guide, here's what's most interesting" was created by u/dancleary544 and earned 2891 upvotes. The post shares a summary of Google's 68-page prompt engineering whitepaper, highlighting key best practices such as providing high-quality examples, keeping prompts simple and verb-driven, being specific about output formats, and using positive instructions over constraints. The author emphasizes techniques like few-shot prompting, experimenting with input and output formats, and continually testing prompts across different model versions. The post sparked a lively discussion with 106 total comments, where community members debated everything from the credibility of the guide to the very definition of prompt engineering.

# REDDIT COMMENTS ANALYSIS

[Self-Promotion & Blog/Ad Concerns] (22 Comments - 402 Upvotes)
A large portion of the discussion centered on whether the post was disguised self-promotion. Many commenters pointed out that the external links led back to the OP's own blog rather than official Google domains, with u/thirteenth_mang noting that "Dan Cleary -> dancleary544" matches the article author to the username. Others defended the OP, with u/Chefseiler sarcastically asking "Oh how dare them to try to direct views to their blog after digging through a 68 page document and summarizing it for the benefit of all." u/avadreams called it "low effort, sneaky BS way of trying to build up DA, LLA and remarketing lists."

[Kaggle = Google Domain Clarification] (7 Comments - 9 Upvotes)
Several commenters clarified that Kaggle is owned by Google, countering the claim that the links were not to Google domains. u/exgeo stated simply "Google owns Kaggle," and u/codenamelegendary added that "The top link Kaggle is a google owned company. The rest are not." This cluster focused on factual corrections about the domain ownership rather than broader criticism.

[Resources & Helpful Links] (2 Comments - 202 Upvotes)
A small cluster where commenters shared or sought out direct resources. u/LinkFrost provided the actual whitepaper link, writing "Here's a link to the whitepaper" with a Google Drive URL, while u/stonedoubt shared a link to a cognitive-prompt-architecture repository. These comments aimed to cut through the debate and give people direct access to materials.

[Prompt Engineering Technique Discussion] (14 Comments - 66 Upvotes)
A core group of technically-minded commenters debated the actual prompt engineering techniques mentioned in the post. u/doctordaedalus shared a practical use of chain-of-thought prompting, while u/funbike discussed how "n-shot is more effective that many people realize" and warned that "1-shot causes overfitting." u/Blaze344 noted that persona prompting is "the biggest scam that made prompt engineering seem like a joke," emphasizing that measurable techniques like few-shot prompting have real benefits while persona-based methods are mostly aesthetic.

[Skepticism & Subreddit Culture] (25 Comments - 124 Upvotes)
This was the largest thematic cluster, filled with cynicism about both the guide and the state of the subreddit. u/But-I-Am-a-Robot expressed confusion at the negativity, asking "Why does anybody need a guide to prompt engineering? You might as well publish a guide on speaking English." u/jeremiah256 observed that "Over time, it's common for a subreddit that began as a helpful forum to grow less supportive." u/Civil_Sir_4154 boiled prompt engineering down to basics: "Learn proper grammar and English without all the modern slang, and how to explain something in proper detail and you can make an LLM do pretty much anything." u/DataScienceNutcase called the guide "fake" and said it "sounds like a typical influencer trying to pimp their bullshit."

[Humor & Light-hearted Comments] (8 Comments - 90 Upvotes)
Several commenters used humor to cope with or comment on the thread. u/-C4354R- sarcastically thanked the OP for "stopping reddit to become another bs social media." u/Agent_User_io joked about getting "a degree certificate for the prompt engineering," and u/BarbellPhilosophy369 quipped that the report "Should've been a 69-page report (niceeee)." These comments added levity to a contentious thread.

[Questions & Clarifications] (9 Comments - 15 Upvotes)
A handful of commenters sought clarification on specific points from the post. u/asyd0 asked "guys could someone explain to me why it shouldn't be used with reasoning models?" regarding chain-of-thought prompting. u/Sweaty_Ganache3247 wondered about "the ideal prompt for the image" and noted that adding more things can confuse models. u/yeswearecoding asked "Which tools use to: Track versions, configurations, and performance metrics?" These questions showed genuine curiosity about the practical application of the techniques.

[Thanks & Appreciation] (4 Comments - 12 Upvotes)
A small but positive cluster of users who appreciated the summary. u/reverentjest wrote "Thanks. I just finished reading this today, so I guess this was a good post read summary." u/BrilliantDesigner518 said "I will no doubt be training my agents on it soon," and u/Uvelha simply wrote "Thanks a lot."

[Low-Effort & General Reactions] (3 Comments - 8 Upvotes)
Some comments were extremely brief, offering minimal engagement. u/MonkeyWithIt noted the paper "was February but it appeared in April," u/Super-Researcher6544 wrote "Interesting," and u/PrestigiousTale2759 simply wrote "Mark."

[Off-Topic/Spam] (1 Comments - 1 Upvotes)
u/EmbarrassedAd5111 posted what appears to be a spam link, writing "Mine is a great sequel" followed by an unrelated URL. This was the only clearly off-topic comment in the thread.

[Deleted/Removed/AutoModerator] (11 Comments - 39 Upvotes)
Eleven comments were deleted, removed, or posted by AutoModerator. These included accounts that were later deleted, removed comments, and automated moderator messages about account age requirements.

(Total: 106 Comments - 968 Upvotes)
The sum of all X Comments values above equals 106, which is the total number of comments analyzed. Every comment fetched has been assigned to exactly one cluster.

# TOP COMMENTS

Each entry below is the verbatim text of the top comment in that upvote range, copied exactly as it appears on Reddit. No summarization, paraphrasing, or layman's-terms rewriting is applied to TOP COMMENTS.

## 100++ Upvotes

u/LinkFrost
"Here’s a link to the whitepaper https://drive.google.com/file/d/1AbaBYbEa_EbPelsT40-vj64L-2IwUJHy/view" (199 Upvotes) - https://www.reddit.com/r/PromptEngineering/comments/1kggmh0/google_dropped_a_68page_prompt_engineering_guide/mqzkml4/

## 70++ Upvotes

u/-C4354R-
"Thanks for stopping reddit to become another bs social media. Very appreciated." (73 Upvotes) - https://www.reddit.com/r/PromptEngineering/comments/1kggmh0/google_dropped_a_68page_prompt_engineering_guide/mqzs3nz/

## 20++ Upvotes

u/[deleted]
"[deleted]" (27 Upvotes) - https://www.reddit.com/r/PromptEngineering/comments/1kggmh0/google_dropped_a_68page_prompt_engineering_guide/mr0fzyo/

## 10++ Upvotes

u/spellbound_app
"Kaggle is a Google domain, but the others just seem like backlink bait" (17 Upvotes) - https://www.reddit.com/r/PromptEngineering/comments/1kggmh0/google_dropped_a_68page_prompt_engineering_guide/mqyqzar/

# ORIGINAL POST

"Google dropped a 68-page prompt engineering guide, here's what's most interesting

Read through Google's  [68-page paper](https://www.kaggle.com/whitepaper-prompt-engineering) about prompt engineering. It's a solid combination of being beginner friendly, while also going deeper int some more complex areas. 

There are a ton of best practices spread throughout the paper, but here's what I found to be most interesting. (If you want more info, full down down available [here](https://www.prompthub.us/blog/googles-prompt-engineering-best-practices#best-practices).)

* **Provide high-quality examples**: One-shot or [few-shot prompting](https://www.prompthub.us/blog/the-few-shot-prompting-guide#:~:text=outputs%20from%20LLMs.-,What%20is%20few%20shot%20prompting?,sentiment%20of%20the%20movie%20review.) teaches the model exactly what format, style, and scope you expect. Adding edge cases can boost performance, but you’ll need to watch for overfitting!
* **Start simple**: Nothing beats concise, clear, verb-driven prompts. Reduce ambiguity → get better outputs

* **Be specific about the output**: Explicitly state the desired structure, length, and style (e.g., “Return a three-sentence summary in bullet points”).

* **Use positive instructions over constraints**: “Do this” >“Don’t do that.” Reserve hard constraints for safety or strict formats. 

* **Use variables**: Parameterize dynamic values (names, dates, thresholds) with placeholders for reusable prompts.

* **Experiment with input formats & writing styles**: Try tables, bullet lists, or JSON schemas—different formats can focus the model’s attention.

* **Continually test**: Re-run your prompts whenever you switch models or new versions drop; As we saw with GPT-4.1, new models may handle prompts differently!

* **Experiment with output formats**: Beyond plain text, ask for JSON, CSV, or markdown. Structured outputs are easier to consume programmatically and reduce post-processing overhead .

* **Collaborate with your team**: Working with your team makes the prompt engineering process easier. 

* **Chain-of-Thought best practices**: When using CoT, keep your “Let’s think step by step…” prompts simple, and don't use it when prompting reasoning models
* **Document prompt iterations**: Track versions, configurations, and performance metrics."
