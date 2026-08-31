# REDDIT POST ANALYSIS

An image-only meme posted on r/LocalLLaMA titled "…and I'm not afraid of losing my social credits" struck a chord with the local LLM community, earning 1,337 upvotes and sparking 352 comments. The post pokes fun at Qwen3.8-27B's tendency to generate extremely long reasoning traces by default, humorously comparing it to China's social credit system. Authored by u/JLeonsarmiento, the thread quickly became the most substantive discussion in the sub's recent history, evolving from a simple joke into a deep dive on reasoning-effort tuning, hardware setups, agent harness strategies, and direct model comparisons. The overwhelming community consensus is that Qwen3.8-27B is remarkably capable at xhigh reasoning but frequently overthinks trivial tasks, and the main fix is to tune reasoning_effort down or cap reasoning tokens explicitly.

# REDDIT COMMENTS ANALYSIS

Reasoning Effort & Overthinking (127 Comments - 1,357 Upvotes)
This is by far the dominant thread in the discussion, where users debate Qwen3.8's default xhigh reasoning mode and its habit of generating massive thinking traces even for simple tasks. The core frustration is that the model overthinks to the point of dysfunction, spending thousands of tokens debating semantics like whether "mind-blowing" is one or two words, or re-reading context it already has in its window. The community's shared prescription is to tune reasoning_effort to low or medium, or cap reasoning tokens via --reasoning-budget 16384. As one user bluntly put it, "read the manual bozo. switch reasoning effort to low," while another counters, "I very much prefer correct answers to immediate bullshit."

Humor & Meme Reactions (44 Comments - 607 Upvotes)
A highly-upvoted vein of jokes about Qwen3.8's verbose thinking behavior and the post's "social credit" meme framing. The standout anecdote describes the model spending 300 tokens debating whether "mind-blowing" is one or two words, then producing a 499-word story: "It even said multiple times right at the start that I probably just meant around 500 words (let's aim for 480-520), but it wasn't going to let that stop it." The post's title also triggered a wave of China-related humor, including "-100 social credits. Glory to LLaMa.CCP" and "Straight to the gulag."

Hardware, Quants & Inference Speed (37 Comments - 98 Upvotes)
Users share real-world hardware configurations and measured token speeds, from a 12GB RTX 4070 getting roughly 9 tok/s to a 5090 on native Linux hitting 190 tok/s with 268K context. Common advice includes using IQ4_XS or Q4_K_M quants, Q8 KV cache offload, MTP 3 draft tokens, and avoiding Q2_K_XL for serious work. A frequent retort to overthinking complaints is, "It doesn't overthink, you just have a slow ass graphics card."

Harness, Frameworks & Tooling (35 Comments - 370 Upvotes)
Deep discussion of agent harnesses including OpenCode, DeepSeek Harness, Pi, Hermes Agent, and Cline, and how each handles long reasoning traces. Users highlight a recurring problem where Qwen3.8 "re-reads" context verbatim via tool calls even when the information is already in its window: "Kat-Coder loves to do that: 'Let me read the relevant code: [50 lines from context]. Ah I see!'" Context-engineering hacks are shared, including intentionally repeating key instructions to boost attention weight and using graph-based knowledge representations to reduce token noise.

Model Comparisons & Capabilities (42 Comments - 612 Upvotes)
Direct comparisons of Qwen3.8-27B against Qwen3.6, DeepSeek V4 Flash, Claude Opus/Sonnet, and Gemma dominate this cluster. Enthusiasts claim "Xhigh has been opus-tier for me. It's fixed mistakes and one-shot tasks that opus got wrong or failed" and "Qwen 3.8 27B gives me consistently better results than Deepseek V4 flash." Detractors note Q3.8 "took 2x long" vs 3.6 for marginal gains. A central insight: "There's no free lunch, the fact that we are able to get such amazing performance out of a 27B model is because it reasons a lot."

Tips, Q&A & General Discussion (65 Comments - 102 Upvotes)
Practical configuration tips like "Unpopular opinion: Set the Temperature to 0.7... and suddenly, it no longer spends billions of tokens on the thinking process," onboarding questions from new users asking "What kind of pc so you need to run this," and meta-commentary about the subreddit: "This sub used to be full of really interesting technical posts and insightful writeups on local model use. Now it's this garbage; a meme image with no post explaining their experience. This shit is going to take over if people don't push back a little." Off-topic political tangents about social credit also land here.

(Total: 350 Comments - 3,146 Upvotes)

# TOP COMMENTS

Each entry below is the verbatim text of the top comment in that upvote range, copied exactly as it appears on Reddit. No summarization, paraphrasing, or layman's-terms rewriting is applied to TOP COMMENTS.

## 500+ Upvotes

u/RevolutionaryGold325
"`reasoning_effort=\"xhigh\",  # xhigh by default; supported levels are xhigh, medium, and low`" (521 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vqgt0x/and_im_not_afraid_of_losing_my_social_credits/p45g3jy/

## 200+ Upvotes

u/TinyFluffyRabbit
"There's no free lunch, the fact that we are able to get such amazing performance out of a 27B model is because it reasons a lot" (230 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vqgt0x/and_im_not_afraid_of_losing_my_social_credits/p45lrga/

## 100+ Upvotes

u/bankinu
"How do you solve this problem -

"Let me read (some file already read)"

And then it proceeds to print contents of a large part of the file it read using decode tokens. I haven't seen previous Qwen or any other model do this.

Reducing to medium or low didn't solve this." (186 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vqgt0x/and_im_not_afraid_of_losing_my_social_credits/p45mosd/

## 70+ Upvotes

u/Hefty_Wolverine_553
"You don't even need this imo, just set it to low or medium reasoning effort and let it do its thing." (76 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vqgt0x/and_im_not_afraid_of_losing_my_social_credits/p45j6yj/

## 60+ Upvotes

u/Blues520
"Yes it's a trade off between intelligence and speed. The good thing is that we can tune it as we require.

Need for speed? Use less reasoning.
Need to find nasty bug? Use more reasoning.

It doesn't have to be only configured once, we can change it as our needs require." (63 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vqgt0x/and_im_not_afraid_of_losing_my_social_credits/p463ln5/

## 50+ Upvotes

u/michaelsoft__binbows
"kinda funny this mirrors our own operation as well. like the context window is just your short term buffer of your brain, not some notebook on your desk or whatever. Re-read something, yeah it's getting blitted out into the context window too.

the fact that we can fully control the context window is so powerful and we're like only scratching the surface of what we can do." (53 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vqgt0x/and_im_not_afraid_of_losing_my_social_credits/p45pbni/

## 40+ Upvotes

u/parepeg
"Exactly, reasoning-budget messes unaturally with the model whereas low, medium, xhigh are built into qwen and designed for it." (49 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vqgt0x/and_im_not_afraid_of_losing_my_social_credits/p45k827/

## 30+ Upvotes

u/Borkato
"I mean……

IS mind-blowing one or two words? 🤔" (39 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vqgt0x/and_im_not_afraid_of_losing_my_social_credits/p462pzx/

## 20+ Upvotes

u/FoxiPanda
"I didn't like all their wishy-washy settings, so I made it explicit. It seems to work really quite well.

Their settings don't map to a specific number of tokens, but instead:

- xhigh: Adds an instruction to think carefully, validate assumptions, consider alternatives, and prioritize correctness.
- medium: Accepted, but adds no special instruction.
- low: Adds an instruction to keep reasoning brief and move directly toward the conclusion.

I find the 16384 value works well for my stuff, but you know, you do you :)" (27 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vqgt0x/and_im_not_afraid_of_losing_my_social_credits/p45kjsb/

## 10+ Upvotes

u/TedDallas
"Let Qwen 3.8 cook.

Medium reasoning and 1.0 temp is working nicely for me with UD-Q3_K_XL. I'm hosting with Llama server and using the OpenCode harness.

It thinks a lot. But it is not looping and is getting the job done. I am impressed and am doing stuff with it that I would normally do with Claude Code. Anthropic and OpenAI should be sweating bullets." (19 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vqgt0x/and_im_not_afraid_of_losing_my_social_credits/p45rbhv/

# ORIGINAL POST

"…and I'm not afraid of losing my social credits."
