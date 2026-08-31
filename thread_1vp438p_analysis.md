# REDDIT POST ANALYSIS

On August 15, 2025, u/MikeNonect shared a surprising milestone in r/LocalLLaMA: a local Qwen3.8-27B model running on a Framework Desktop with 128GB RAM successfully generated a working Super Mario clone as a single HTML page in one shot. The post earned 629 upvotes and sparked 148 comments. Mike noted the Q8 GGUF quant runs slowly but handles overnight batches well, and asked the community for tips on improving speed without losing accuracy. To dodge copyright issues, he later asked the model to remake the game with a circus theme instead, making it "technically no longer a one-shot." The discussion quickly grew into a broader debate about whether this feat is genuinely impressive or just a model regurgitating training data.

# REDDIT COMMENTS ANALYSIS

Gaming Hype & Future Predictions (33 Comments - 519 Upvotes)
This cluster is all about where AI-generated games go next. People joked about one-shotting GTA 6, GTA 7, Elder Scrolls, Fallout, and Giana Sisters, showing how excited the community is about AI eventually building full AAA titles. u/Infinite100p wrote: "You'll be able to one shot GTA 6 before it comes out circa 2046." The tone is playful and optimistic, with many users sharing their own benchmarks and wishlists for future AI milestones.

Skepticism & Training Data Critique (17 Comments - 199 Upvotes)
A large group pushed back on the hype, arguing the Mario clone is not a true measure of intelligence because similar code likely exists in the training data. u/falconandeagle wrote: "There is nothing beastly about this. It's in the training data. These prompts for benchmarking are just embarassing." u/mechkbfan added: "Once the authors see what's popular they'll train their next models around it. Do something different for a change." Others mentioned the "pelican on a bicycle" test and car-wash benchmarks, saying these viral demos get fixed in the next training run.

Questions About Prompts, Tools & Hardware (27 Comments - 126 Upvotes)
Many commenters asked practical questions about how the demo was built. u/AnyNameFreeGiveIt asked: "Knowing Nintendo I would not host that on Github lol. What was the prompt?" u/nsartem asked about the agent harness: "And what agent harness did you use? Pi? Opencode?" Mike answered that he used "Plain vanilla OpenCode" and shared the exact prompt. Others asked about GPU specs, context window size, and whether MTP was enabled.

Speed, Performance & Quantization (3 Comments - 13 Upvotes)
A small but focused cluster discussed the trade-offs between model size, quantization, and inference speed. u/MikeNonect mentioned running on Q8 GGUF with roughly 7 tokens per second and a slow prefill stage. u/edsonmedina asked about MTP, and Mike confirmed he hadn't tried it yet. One user noted that dropping to Q4_K_M or adjusting context size could help speed on smaller hardware.

Technical & Philosophical Discussion (16 Comments - 56 Upvotes)
This group debated whether a single developer or model could realistically build a complex game from scratch. u/masterlafontaine argued: "There is no way. It's like expecting a great developer to build an OS alone." The thread branched into discussions about Brooks's Law, Linux history, Terry Davis, and whether 10,000 years of solo development is a fair comparison. Others brought up DeepSeek's +900k context window as a potential game-changer.

Humor & Off-Topic Banter (14 Comments - 57 Upvotes)
A lighthearted cluster with inside jokes and tangents. u/hIXhnWUmMvw asked: "All named Peter Palantir that will be flocking around on some axons?" u/FrogsJumpFromPussy replied: "I'm Peter Palantir look at me / No I'm Peter Palantir look at me." u/-dysangel- and u/masterlafontaine had a playful pedantry battle about what counts as an OS. u/tvall_ critiqued a mushroom placement with "Mushrooms in the wrong ? Block. Fail."

Agreement & Enthusiasm (3 Comments - 6 Upvotes)
A small cluster of genuinely impressed reactions. u/jloverich wrote: "I beat the game!" u/rookan said: "great game! I love flying monsters on 2nd stage." u/IrisColt quipped: "*The circus is saved!*"

Miscellaneous (27 Comments - 141 Upvotes)
Comments that didn't fit neatly into other categories, including nitpicks, deleted/removed posts, and single-word replies. Some users shared links to related projects like aaabench, while others complained the post felt like an ad or critiqued specific game details. u/entsnack wrote: "for your github repo bro, and I could do this with a Qwen from 3 years ago so you need to up your prompting game."

(Total: 140 Comments - 1,117 Upvotes)

# TOP COMMENTS

Each entry below is the verbatim text of the top comment in that upvote range, copied exactly as it appears on Reddit. No summarization, paraphrasing, or layman's-terms rewriting is applied to TOP COMMENTS.

## 200+ Upvotes

u/Infinite100p
"You'll be able to one shot GTA 6 before it comes out circa 2046." (222 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vp438p/if_you_would_have_told_me_half_a_year_ago_that_a/p3uh73x/

## 100+ Upvotes

u/falconandeagle
"There is nothing beastly about this. It's in the training data. These prompts for benchmarking are just embarassing " (102 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vp438p/if_you_would_have_told_me_half_a_year_ago_that_a/p3upt2j/

## 90+ Upvotes

u/Thin_Pollution8843
"In a year you will be able to one shot gta vice city. Call me nuts if you want." (97 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vp438p/if_you_would_have_told_me_half_a_year_ago_that_a/p3ugy44/

## 40+ Upvotes

u/mechkbfan
"This is it to me. And there's likely heaps of example projects online to copy off 

Basically when people are like "it drew a Pelican on a bike really well", or "it did the car wash prompt perfectly", I don't know why they're surprised.

(Edit: Pelican was a bad example. It seems it's been proven to not be the case)
Once the authors see what's popular they'll train their next models around it

Do something different for a change. I'm sure it'll still do decently but it'll expose it's weaknesses a bit more" (47 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vp438p/if_you_would_have_told_me_half_a_year_ago_that_a/p3utj17/

## 30+ Upvotes

u/No_Lingonberry1201
"YOU'RE NUTS! Absolutely cashews, maybe even walnuts!" (36 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vp438p/if_you_would_have_told_me_half_a_year_ago_that_a/p3v1l28/

## 20+ Upvotes

u/OttoRenner
"GTAI" (25 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vp438p/if_you_would_have_told_me_half_a_year_ago_that_a/p3utmzr/

## 10+ Upvotes

u/MikeNonect
"It was, on purpose, very succinct: "Create a Super Mario clone in JavaScript as a single HTML page. Make the game engaging and the graphics as beautiful as possible."

I'm getting around 7t/s on the Framework,which is reasonable, but the prefill is slow." (17 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vp438p/if_you_would_have_told_me_half_a_year_ago_that_a/p3ui88p/

# ORIGINAL POST

"If you would have told me half a year ago that a local model running in my office would be able to one-shot a Super Mario clone, I would have called you nuts. Qwen3.8-27B is a different beast.

Running the Q8 GGUF on my Framework Desktop is not fast, but it's extremely smart for overnight batches and background jobs. Can't wait to play around with MTP and other quants.

Have any of you found ways to improve speed while keeping accuracy?

https://mikeveerman.github.io/qwen38-27b-mario

Edit: to avoid copyright issues and to see how creative it would get, I asked Qwen3.8 to make it circus-themed instead of Mario-themed. It's technically no longer a one-shot."
