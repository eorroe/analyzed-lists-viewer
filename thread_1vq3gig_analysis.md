# REDDIT POST ANALYSIS

The post titled "Qwen 3.8 distillations" was shared in the r/LocalLLaMA subreddit by u/jacek2023, where it received 512 upvotes and sparked 131 comments. The post links to an X (formerly Twitter) status about Qwen 3.8 distillations, with the author noting "Not tested by me in any way :)". The discussion that followed centered heavily on whether it is appropriate for third-party creators to use the official "Qwen 3.8" name for their own distilled models, with many commenters arguing that the name is misleading and could confuse users into thinking these are official Alibaba releases. Alongside the naming debate, the thread also touched on skepticism about limited benchmark reporting, security concerns around GGUF files, and a lengthy technical discussion about what actually counts as "distillation" versus fine-tuning.

# REDDIT COMMENTS ANALYSIS

Naming and Branding Concerns (26 Comments - 1098 Upvotes)
The largest group of comments focused on the model's name, with many users feeling that calling it "Qwen 3.8" is misleading because it is not an official Qwen release. u/Barni275 wrote: "Dear guys, you do a great job, I use your models for a while. But please, rename this one. This name misleads and confuses." Others pointed out potential legal issues, with u/daniel-sousa-me stating: "Qwen is a registered trademark." u/shiny_monkee added: "They should just rename it, just a slight tweak to the name. Feels silly to use the official names, and it's unnecessarily confusing." Some commenters suspected the naming was a deliberate tactic to drive downloads, with u/darkwalker247 suggesting it was done "to trick people into downloading it and get more downloads on the model."

Benchmarks and Suspicion (3 Comments - 166 Upvotes)
A smaller but vocal group expressed skepticism about the model's quality based on the limited evidence provided. u/Velocita84 wrote: "Only 2 shitty benchmarks reported in the model card, totally nothing fishy going on here." u/the_TIGEEER speculated that "it's just one guy who has a lotta money and was able ot run the big Qwen, and they distilled the data into the 9B models" or alternatively suggested "Or it's a Trojan horse." u/Tall_Abrocoma_3533 shared an image comparing the 4B model to Qwen 3.5 and wrote: "I wouldn't necessarily believe this... this is all the 'proof' that it's better then 3.5."

Trojan and Security Concerns (18 Comments - 188 Upvotes)
Several comments explored whether GGUF model files could contain malicious code. u/Borkato asked: "Wait can ggufs have Trojans 🫪" which sparked a thread of jokes and serious discussion. u/maddeninglemon quipped: "Amazing_model.gguf.exe" and u/Borkato followed up with: "Omg finally!! I've been waiting for Qwen-Opus-0.01B-AGI.exe to run on my CPU!!" Others provided more technical context, with u/beneath_steel_sky explaining: "Not trojans in the traditional sense... but they can be trained to be malicious under specific circumstances" and u/Refefer adding: "trust-remote-code baby." u/Due-Memory-6957 shared real-world vulnerability links, noting: "Yeah, last time it happened it was fixed fairly quickly, but still, be careful with what you download."

Distillation Technical Discussion (30 Comments - 201 Upvotes)
A lengthy technical thread debated whether the models were actually "distilled" or simply fine-tuned. u/BitterProfessional7p argued: "Then it's just a finetune from another model but not a distillation. For distillation you teach the small model with the token probabilities distribution from the big model for each predicted token." u/RG_Fusion pushed back, saying: "You don't need to share logits. A distillation can be anything that trains a model's weights to behave like a more intelligent model." u/toothpastespiders commented: "Props to you for holding strong on the terminology. It's annoying that distillation has become another one of those terms that can mean multiple things in informal discussions." Others noted practical applications, with u/No-Refrigerator-1672 explaining: "Of course it can, distillation is universal, you can even apply it to Gemma."

Model Usage and Testing (23 Comments - 83 Upvotes)
Many users shared practical experiences or asked about running the models. u/pmttyji compiled links to the HuggingFace repositories: "Nice find u/jacek2023\n\nFor lazy hands:\n\n* https://huggingface.co/empero-ai/Qwen3.8-27B-Ridge-GGUF\n* https://huggingface.co/empero-ai/Qwen3.8-9B-GGUF\n* https://huggingface.co/empero-ai/Qwen3.8-4B-GGUF\n* https://huggingface.co/empero-ai/Qwen3.8-2B-GGUF\n\nEven this creator didn't release 35B." u/the_TIGEEER shared a personal use case: "This would be perfect for my Yu-Gi-Oh self-learning project, where I need small models to do SFT weight updates on them!" u/insraq posted their own renamed version: "I made a heretic version of 2B model for my own testing... (I decide to use a more descriptive and appropriate naming)."

Humor and Off-topic (26 Comments - 137 Upvotes)
The thread included many lighthearted comments and inside jokes. u/Borkato made multiple quips including: "Q0 answer" and "Omg finally!! I've been waiting for Qwen-Opus-0.01B-AGI.exe to run on my CPU!!" u/jacek2023 joked: "I volunteer you" in response to "please someone test" and later posted a humorous identity test where a model incorrectly claimed: "I am **Qwen3.5**, the latest large language model developed by Tongyi Lab." u/Tall_Abrocoma_3533 clarified: "It's a distill, not a real new model." u/RemindMeBot also appeared, sending reminders to users who requested follow-ups.

(Total: 126 Comments - 1873 Upvotes)

# TOP COMMENTS

Each entry below is the verbatim text of the top comment in that upvote range, copied exactly as it appears on Reddit. No summarization, paraphrasing, or layman's-terms rewriting is applied to TOP COMMENTS.

## 300+ Upvotes

u/Chromix_
"https://preview.redd.it/spyhj0exzrjh1.png?width=267&format=png&auto=webp&s=ef2ee0fb05044998039b344c8be070e9b8cb76f1

Still, it seems to do something - if not benchmaxxed.  
The names will certainly clash though - should not name it *exactly* like the official model" (339 Upvotes) - https://reddit.com/r/LocalLLaMA/comments/1vq3gig/qwen_38_distillations/p42gvbf/

## 100+ Upvotes

u/Barni275
"Dear guys, you do a great job, I use your models for a while. But please, rename this one. This name misleads and confuses." (164 Upvotes) - https://reddit.com/r/LocalLLaMA/comments/1vq3gig/qwen_38_distillations/p42gv57/

## 90+ Upvotes

u/shy_monkee
"Are they allowed legally to call it that? Since it's not the real Qwen3.8-9B?" (154 Upvotes) - https://reddit.com/r/LocalLLaMA/comments/1vq3gig/qwen_38_distillations/p42ew1q/

## 80+ Upvotes

u/Velocita84
"Only 2 shitty benchmarks reported in the model card, totally nothing fishy going on here" (136 Upvotes) - https://reddit.com/r/LocalLLaMA/comments/1vq3gig/qwen_38_distillations/p42gxq6/

## 70+ Upvotes

u/shy_monkee
"They should just rename it, just a slight tweak to the name. Feels silly to use the official names, and it's unnecessarily confusing." (120 Upvotes) - https://reddit.com/r/LocalLLaMA/comments/1vq3gig/qwen_38_distillations/p42fjci/

## 60+ Upvotes

u/--Spaci--
"Why are they posing it as the official model name? " (85 Upvotes) - https://reddit.com/r/LocalLLaMA/comments/1vq3gig/qwen_38_distillations/p42ik4q/

## 50+ Upvotes

u/Icy-Degree6161
"Yep cannot deny the idea that the whole point was to "take" the names." (85 Upvotes) - https://reddit.com/r/LocalLLaMA/comments/1vq3gig/qwen_38_distillations/p42tdbh/

## 40+ Upvotes

u/darkwalker247
"to trick people into downloading it and get more downloads on the model, i would guess" (67 Upvotes) - https://reddit.com/r/LocalLLaMA/comments/1vq3gig/qwen_38_distillations/p4312ce/

## 30+ Upvotes

u/the_TIGEEER
"I think it's just one guy who has a lotta money and was able ot run the big Qwen, and they distilled the data into the 9B models with the 3.5 architecture, and they didn't have time to run the benchmarks. Or it's a Trojan horse. Either one is possible 🤷‍♀️ " (56 Upvotes) - https://reddit.com/r/LocalLLaMA/comments/1vq3gig/qwen_38_distillations/p42lcq6/

## 20+ Upvotes

u/maddeninglemon
"Amazing\\_model.gguf.exe" (45 Upvotes) - https://reddit.com/r/LocalLLaMA/comments/1vq3gig/qwen_38_distillations/p43kc03/

## 10+ Upvotes

u/tarruda
"Funny how third parties just straight up use official model names for their distill, misleading people into thinking it was trained by Alibaba." (44 Upvotes) - https://reddit.com/r/LocalLLaMA/comments/1vq3gig/qwen_38_distillations/p42o3t6/

# ORIGINAL POST

"Qwen 3.8 distillations

https://x.com/i/status/2088993948983246906

Not tested by me in any way :)"
