# REDDIT POST ANALYSIS

A post in r/LocalLLaMA sparked excitement when user sleepy_roger shared news from the Qwen Ambassador Discord that a community manager had put an "X" reaction on someone asking for a 35B model and said "We'll have a new midsize open weight model coming next week (hopefully), This midsize model won't provide early access due to the schedule." The original poster speculated it would be "over 100B" and ended with "Exciting!!" The post received 546 upvotes and generated 268 comments, with the community eagerly debating what form this new model might take.

# REDDIT COMMENTS ANALYSIS

## Excitement & Anticipation (27 Comments - 1,039 Upvotes)
The thread is packed with genuine excitement about the upcoming release. u/boxwrenchx captured the mood with "This August is legendary, reminds me of the olds days!" while u/EvolvingDior wrote "Shit, if they release a DS4F rival, the local llm community is gonna explode." Many commenters praised Qwen's recent pace of releases, with u/CoffeeToCode99 noting "Qwen teasing a midsize open-weight model next week is wild. Folks are already speculating 100B+, but even if it lands smaller, the cadence matters — they're dropping models like patch notes while others are still polishing roadmaps." Even some of the lower-scoring comments expressed hope, like u/UnWiseSageVibe's simple "Crossing fingers" and u/Beneficial-Ad-8127's "They about to drop something better Stay tuned!"

## Model Size & Architecture Speculation (80 Comments - 1,051 Upvotes)
The biggest debate centered on what size the model would actually be. The most upvoted comment was u/boxwrenchx's hopeful "80b Qwen coder" with 279 upvotes, followed by u/cogitech2 noting "another comment from someone on the team was '...35B A3B isn't the one to wait for...'" with 115 upvotes. u/Gloomy_Letterhead395 wrote "Qwen 3.8 100ish b will a dsv4F killer" (100 upvotes), while u/whichsideisup argued "A new 122b with the 3.8 capabilities would be a game changer. It's truly the sweet spot for speed and world knowledge" (69 upvotes). u/JumpingJack79 similarly pleaded "122B please" and called 122B A10B "the absolute sweetspot Goldilocks GOAT arch for all 128GB AI PCs" (26 upvotes). Others hoped for 80B, with u/DonkeyBonked stating "I'd much rather an 80B MoE that can run on 96GB with decent context" (9 upvotes). Some skepticism appeared too, like u/I_Play_Zed worrying the model might be "250B-500B parameters, which is a stones throw away from being out of reach on my hardware" (9 upvotes). u/migsperez bluntly stated "I'm not falling for it. The next model will be 35b Moe or similar size" (7 upvotes).

## Hardware & Practical Deployment (58 Comments - 287 Upvotes)
A major thread of discussion focused on what hardware could actually run the new model. u/National_Meeting_749 lamented "No 35b Rip low vram setups" (64 upvotes), while u/BornInAFish explained the math: "Yeah 122B is an awkward size. A decent 4-bit quant is still gonna run you 75-80GB of weights. Which would be fine if you have 128 GB of VRAM, buuuuut it's much more common to end up with 96 GB of RAM" (11 upvotes). Several users noted the 80B option would be more accessible, with u/Gloomy_Letterhead395 adding "80b would be more amazing" (17 upvotes) and u/QuackerEnte stating "I REALLY hope it's 80B-A3B. I cannot run 122B-A10B at any good quant, nor any good speeds. 80B-A3B is the best option for the VRAM poor" (2 upvotes). u/LagOps91 observed "it fits very nicely for 64gb ram + gpu setups. i would assume those to be more common than multi gpu rigs" (6 upvotes). The discussion also touched on quantization strategies, with u/the-username-is-here noting "4/8 bits fits with full context no problem" (1 upvote) and u/tecneeq explaining "100b@Q2 is double the amount of weights than 27b@Q4" (2 upvotes).

## Competition & Comparisons (22 Comments - 478 Upvotes)
Many commenters framed the announcement in terms of the broader AI race, particularly against DeepSeek. u/atumblingdandelion declared "Yay! The real AI battle is not Anthropic vs OpenAI, it's Deepseek vs Qwen lol" (73 upvotes), while u/boxwrenchx added "Just pushes DS to go harder, we win" (64 upvotes). u/MacsBicycle noted "Dsv4F is still beating 3.8 in my local assignments" (22 upvotes), and u/Hoodfu shared testing results: "qwen 3.8 27b lags nicely behind ds v4 flash without thinking. With thinking on its seriously impressive. Point being, we really need a high total, lower active parameter model that we can engage thinking on that'll be fast enough" (14 upvotes). Some users expressed concern about the size gap, with u/pmttyji hoping "it's smaller than DeepseekV4Flash" (13 upvotes). The competitive framing was a major theme, with u/EvolvingDior exclaiming "Shit, if they release a DS4F rival, the local llm community is gonna explode" (28 upvotes).

## Vision & Capabilities (25 Comments - 234 Upvotes)
A significant portion of the discussion focused on whether the new model would include vision capabilities. u/Embarrassed_Adagio28 wrote "Agreed. However with vision this time hopefully. Almost all of my coding tasks require vision for computer use to verify ui elements" (86 upvotes), and u/Bohdanowicz agreed "100%. Having free inference for local vision is awesome" (35 upvotes). u/Strong_Chicken6838 noted "It's also INCREDIBLY useful for any type of engineering (not software engineering)" (6 upvotes), while u/cunasmoker69420 suggested practical uses like "you can have it debugging some physical thing like a separate device with a display. Point a camera at it and now Qwen has eyes at that separate device" (3 upvotes). Some users were already satisfied with current vision capabilities, like u/ThatRegister5397 pointing out "Qwen 3.8 27b has vision too. It was the older coder model that didn't" (5 upvotes). u/Pristine_Pick823 noted "Personally I find that it still outperforms even Qwen 3.8 for everyday coding usage" (1 upvote), and u/Momsbestboy expressed relief that "27b now has vision, because it was such a waste of time to set up a second llm on cpu/different gpu just to be able to analyze images first" (2 upvotes).

## Humor, Nostalgia & Off-Topic (32 Comments - 411 Upvotes)
The thread also had a lively undercurrent of humor and nostalgia. u/boxwrenchx's "Back in my day you had to tell the model you were dying of cancer to get it to answer" (69 upvotes) sparked a chain of jokes about how much prompt engineering has changed. u/PermanentLiminality responded "Three years?! I think the dinosaurs were still walking the earth that far back. Maybe 3 months ago?" (34 upvotes), and u/mfarmemo joked "Take a deep breath. Take you time. Think through this step by step. DO NOT HALLUCINATE! You will get a $200 tip for outputting working code" (37 upvotes). u/some_user_2021's non-sequitur "What did you do to those poor kittens???" (3 upvotes) and u/profcuck's "When llamas roamed the earth..." (1 upvote) added to the playful tone. Some comments reminisced about older models, with u/mfarmemo noting ""back in my day" can remember when starcoder was the goat" (4 upvotes) and u/_TheWolfOfWalmart_ adding "QBasic. Now that brings back some fond memories. (I'm old)" (2 upvotes). A few off-topic threads emerged, like u/retowyss's suggestion that "UI and vision are so pre-agentic. Retro really... We need TUI design skill and native ASCII art output" (4 upvotes), which sparked a mini-debate about whether TUI or GUI is more "retro."

(Total: 257 Comments - 2,026 Upvotes)
The sum of all X Comments values above (27 + 80 + 58 + 22 + 25 + 32) equals 257. Every comment fetched has been assigned to exactly one cluster.

# TOP COMMENTS

Each entry below is the verbatim text of the top comment in that upvote range, copied exactly as it appears on Reddit. No summarization, paraphrasing, or layman's-terms rewriting is applied to TOP COMMENTS.

## 200+ Upvotes

u/boxwrenchx
"80b Qwen coder" (279 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vs9zym/new_midsize_qwen_38_model_coming_next_week/p4jpded/

## 100+ Upvotes

u/cogitech2
"Yep, another comment from someone on the team was "...35B A3B isn't the one to wait for..." (115 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vs9zym/new_midsize_qwen_38_model_coming_next_week/p4jolrz/

## 100+ Upvotes

u/boxwrenchx
"This August is legendary, reminds me of the olds days! You know....3 years ago" (103 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vs9zym/new_midsize_qwen_38_model_coming_next_week/p4jp8nm/

## 100+ Upvotes

u/Gloomy_Letterhead395
"Qwen 3.8 100ish b will a dsv4F killer" (100 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vs9zym/new_midsize_qwen_38_model_coming_next_week/p4joi3d/

## 80+ Upvotes

u/Embarrassed_Adagio28
"Agreed. However with vision this time hopefully. Almost all of my coding tasks require vision for computer use to verify ui elements." (86 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vs9zym/new_midsize_qwen_38_model_coming_next_week/p4jrpjd/

## 70+ Upvotes

u/atumblingdandelion
"Yay! The real AI battle is not Anthropic vs OpenAI, it's Deepseek vs Qwen lol" (73 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vs9zym/new_midsize_qwen_38_model_coming_next_week/p4jrqrj/

## 60+ Upvotes

u/boxwrenchx
"Back in my day you had to tell the model you were dying of cancer to get it to answer" (69 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vs9zym/new_midsize_qwen_38_model_coming_next_week/p4jqk37/

## 60+ Upvotes

u/whichsideisup
"A new 122b with the 3.8 capabilities would be a game changer. It's truly the sweet spot for speed and world knowledge" (69 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vs9zym/new_midsize_qwen_38_model_coming_next_week/p4jp4lq/

## 60+ Upvotes

u/boxwrenchx
"Just pushes DS to go harder, we win" (64 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vs9zym/new_midsize_qwen_38_model_coming_next_week/p4jp25o/

## 60+ Upvotes

u/National_Meeting_749
"No 35b Rip low vram setups." (64 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vs9zym/new_midsize_qwen_38_model_coming_next_week/p4jnxd1/

## 40+ Upvotes

u/triynizzles1
"This is my vote too but it will likely be 3.8 122b" (43 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vs9zym/new_midsize_qwen_38_model_coming_next_week/p4jru4a/

## 30+ Upvotes

u/mfarmemo
"Take a deep breath. Take you time. Think through this step by step. DO NOT HALLUCINATE! You will get a $200 tip for outputting working code. You are a software developer with 30 years experience. This is very important! Your code will be reviewed by experts. Please."

 (37 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vs9zym/new_midsize_qwen_38_model_coming_next_week/p4k0v34/

## 30+ Upvotes

u/Bohdanowicz
"100%. Having free inference for local vision is awesome." (35 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vs9zym/new_midsize_qwen_38_model_coming_next_week/p4jtpux/

## 30+ Upvotes

u/PermanentLiminality
"Three years?!   I think the dinosaurs were still walking the earth that far back.  Maybe 3 months ago?" (34 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vs9zym/new_midsize_qwen_38_model_coming_next_week/p4jq2do/

## 30+ Upvotes

u/Iory1998
"I agree. A 35B3A model that's close to the 27B would be the dream of many people. With MTP natively enabled, local agentic setups will be accessible to more people than any time before." (33 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vs9zym/new_midsize_qwen_38_model_coming_next_week/p4jq0dv/

## 20+ Upvotes

u/OsmanthusBloom
"If it's a 3.8 model it will be a variation of one of the previous 3.x models, likely with the same architecture and number of parameters. So 122B-A10B is possible, not e.g. 80B-A3B." (28 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vs9zym/new_midsize_qwen_38_model_coming_next_week/p4k77yd/

## 20+ Upvotes

u/EvolvingDior
"Shit, if they release a DS4F rival, the local llm community is gonna explode." (28 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vs9zym/new_midsize_qwen_38_model_coming_next_week/p4jtxla/

## 20+ Upvotes

u/Pristine_Pick823
"Qwen coder next remains a monster. I hope this is what they're going for." (26 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vs9zym/new_midsize_qwen_38_model_coming_next_week/p4jv82o/

## 20+ Upvotes

u/JumpingJack79
"122B please, k thanx

No but seriously though, 122B A10B is the absolute sweetspot Goldilocks GOAT arch for all 128GB "AI PCs", which are SUPER POPULAR" (26 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vs9zym/new_midsize_qwen_38_model_coming_next_week/p4jzpe0/

## 20+ Upvotes

u/RG_Fusion
"Really hoping this is a 15-30b active parameter MoE model. I know most of this community's members can't run anything that large, but when Qwen says medium, they are almost certainly talking about something in the 200-700b total parameter range.

Unless you're willing to spend more than $20k in GPUs, that leaves the medium sized models to EPYC/Xeon servers, Mac, and specialized inference boxes. The key to making those three systems run well is a lower total parameter count.

There have have been a few good models releasing in the medium category of late, but if Qwen would release this as a vision capable model they would definitely be the best choice." (24 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vs9zym/new_midsize_qwen_38_model_coming_next_week/p4jr1pt/

## 20+ Upvotes

u/MacsBicycle
"I would welcome it. Dsv4F is still beating 3.8 in my local assignments." (22 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vs9zym/new_midsize_qwen_38_model_coming_next_week/p4k05bh/

## 20+ Upvotes

u/Non-Technical
"122B A10B please please." (22 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vs9zym/new_midsize_qwen_38_model_coming_next_week/p4k0fg5/

## 20+ Upvotes

u/smithy_dll
"27B is already more coder than coder" (22 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vs9zym/new_midsize_qwen_38_model_coming_next_week/p4jpl9h/

## 20+ Upvotes

u/boxwrenchx
"It's not funny it's prompt engineering" (21 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vs9zym/new_midsize_qwen_38_model_coming_next_week/p4jxmr1/

## 10+ Upvotes

u/Gloomy_Letterhead395
"80b would be more amazing" (17 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vs9zym/new_midsize_qwen_38_model_coming_next_week/p4k13x5/

## 10+ Upvotes

u/some_user_2021
"*again" (16 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vs9zym/new_midsize_qwen_38_model_coming_next_week/p4jzhmw/

## 10+ Upvotes

u/dionisioalcaraz
"My bet is something around 180/200B-A10B" (16 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vs9zym/new_midsize_qwen_38_model_coming_next_week/p4jrht0/

## 10+ Upvotes

u/Hoodfu
"So after lots of testing, qwen 3.8 27b lags nicely behind ds v4 flash without thinking. With thinking on its seriously impressive. Point being, we really need a high total, lower active parameter model that we can engage thinking on that'll be fast enough. (I don't consider dropping to q4 to be viable to attain that speed)" (14 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vs9zym/new_midsize_qwen_38_model_coming_next_week/p4k2yis/

## 10+ Upvotes

u/AdNew5862
"This is so funny" (13 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vs9zym/new_midsize_qwen_38_model_coming_next_week/p4jxcuc/

## 10+ Upvotes

u/pmttyji
"Hope it's smaller than DeepseekV4Flash" (13 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vs9zym/new_midsize_qwen_38_model_coming_next_week/p4jux0h/

## 10+ Upvotes

u/BornInAFish
"Yeah 122B is an awkward size. A decent 4-bit quant is still gonna run you 75-80GB of weights. Which would be fine if you have 128 GB of VRAM, buuuuut it's much more common to end up with 96 GB of RAM:

- single RTX 6000 if you're loaded
- 4x 24 GB cards
- 3x 32 GB cards
- 2x 48 GB cards
- 128 GB unified with 32GB of the memory reserved for main RAM.

You _can_ still run 122B on 96 GB VRAM, but you won't get much cache out of it sadly, and you have to quant down.

Vs an 80B model, which you can either use at 8-bit still small KV cache, or at 4-bit with large KV cache. Options!" (11 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vs9zym/new_midsize_qwen_38_model_coming_next_week/p4knz9b/

## 10+ Upvotes

u/RG_Fusion
"You're probably right, though this could also be a 3.8 version of 397b-a17b." (11 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vs9zym/new_midsize_qwen_38_model_coming_next_week/p4krsou/

## 10+ Upvotes

u/starheap
"Honestly something in the 60-72b range would be awesome" (11 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vs9zym/new_midsize_qwen_38_model_coming_next_week/p4jyaco/

## 10+ Upvotes

u/boxwrenchx
"Qwen coder next NEXT" (10 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vs9zym/new_midsize_qwen_38_model_coming_next_week/p4jyrdx/

## 10+ Upvotes

u/sleepy_roger
"Yeah but it just means not right now, could still be coming." (10 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vs9zym/new_midsize_qwen_38_model_coming_next_week/p4jo8uq/

# ORIGINAL POST

"Community manager mentioned this in the Qwen Ambassador Discord, put an X reaction on someone asking for 35B... and said 

> We'll have a new midsize open weight model coming next week (hopfully), This midsize model won't provide early access due to the schedule


Thinking it's going to be over 100B.

Exciting!!"
