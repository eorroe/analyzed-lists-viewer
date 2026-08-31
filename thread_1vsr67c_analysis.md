# REDDIT POST ANALYSIS

The post "Introducing Qwen3.8-27B Dynamic v3 Unsloth GGUFs" by u/danielhanchen announces a new release of compressed AI model files (GGUFs) for the Qwen3.8-27B model. The key claim is that these new files deliver "10% higher accuracy for the same size" thanks to Unsloth's Dynamic v3.0 technology, and the team also released 1-bit quantized versions that supposedly retain 77% accuracy while running on just 8GB of RAM. The author clarifies that an earlier update to these files was not because anything was broken, but rather to make them "EVEN BETTER," and shares links to a detailed blog post, the Hugging Face model repository, and an upcoming Unsloth Desktop update.

# REDDIT COMMENTS ANALYSIS

MTP Confusion and Clarification (47 Comments - 366 Upvotes)
A large portion of the discussion centered on confusion about whether the MTP (multimodal prediction/thinking) component was removed from the model files. The Unsloth team clarified that MTP was only removed from smaller quantizations under UD-Q2-K_XL to save around 500MB of space, while larger quants like UD-Q3_K_XL and Q4_K_XL still include it. However, the messaging was inconsistent at first, leading to confusion. u/NovaXeros wrote, "I'm a bit confused now then - are you saying the UD quants no longer have MTP even though the HF page still makes mention of MTP training?" and u/BigPoppaK78 noted, "So, if MTP was removed, why am I still seeing draft acceptance rates in the llama.cpp logs?" The team later clarified that MTP is still present in most quants and only stripped from the very smallest ones.

Hardware and Performance (41 Comments - 346 Upvotes)
Many users discussed their experiences running these models on various hardware configurations, with a focus on VRAM and RAM limitations. Users with 8GB, 16GB, and 32GB of VRAM shared their experiences, noting that 16GB VRAM is "living on the edge" for 4-bit quantizations. u/CatiStyle wrote, "16G VRAM is like living on the edge, 4-bit run but no space for context (cut thinking answer short), and 3-bit is less smart." Others shared tips like removing the vision projection file (mmproj) to free up memory, and several users on Macs, RTX cards, and older GPUs chimed in with their performance numbers and context window limitations.

Praise and Support (36 Comments - 813 Upvotes)
The community responded with a wave of gratitude toward the Unsloth team for releasing these optimized model files. Many users praised the work as "incredible" and "awesome," with u/Jorlen's comment earning the most upvotes in the thread by simply saying, "Just want to say, thank you Unsloth team for these great quants. Your hard work is appreciated!" Several users highlighted how Unsloth's quants make running advanced AI models accessible on consumer hardware, and the team received recognition for sharing their imatrix calibration files openly with the community.

Benchmarks and Comparisons (31 Comments - 330 Upvotes)
Users frequently asked for more detailed benchmarks and comparisons with previous versions of the quants, other quantization methods, and competing projects like AtomicChat and Byteshape. u/Chromix_ requested, "Can you also add a line for the previous Qwen 3.8 27B UD 2.0 quants to the graph, so that it's easier to see how what most of us now have on disk compares to the latest and greatest?" Others asked about comparisons with NVFP4 builds, INT8 quants, and whether the accuracy improvements hold up in real-world agentic tasks. Some users shared their own A/B testing results, with u/jonaddb noting they "couldn't tell them apart perplexity gap well inside the error bars" when comparing Unsloth's quants to AtomicChat's on a single RTX 3090.

Questions and Clarifications (30 Comments - 56 Upvotes)
A significant number of comments were straightforward questions about the release, the technology, or how to use the models. Users asked whether the models work with llama.cpp and Ollama, what the "Ba, By, At" labels on the benchmark charts mean, whether the release is an update from the preview version, and how the 1-bit quantization compares to other options. u/Ryan4456 asked, "What does this mean in laymans terms for us simpler folk?" reflecting a desire for more accessible explanations of the technical improvements. Several users also asked about file naming conventions and whether they needed to redownload existing models.

Feature Requests (26 Comments - 107 Upvotes)
The community made numerous requests for Unsloth to apply their Dynamic v3.0 quantization to other models, including Qwen3.6, Qwen3.5, DeepSeek V4 Flash, Gemma 4, and Muse Glimmer 30B. u/Leflakk asked, "Will you also do DSV4 flash 0731?" and u/Choice_Celery9481 inquired about plans for Gemma4 with UDv3. Users also requested MLX support for Apple Silicon, mobile-friendly versions, a web interface for Unsloth Desktop, and local server options. Some asked about backporting the technology to older model versions, with u/LargelyInnocuous asking, "can this be backported to qwen3.6 and 3.5?"

Bug Reports and Issues (21 Comments - 84 Upvotes)
Several users reported technical issues they encountered while trying to use the new models. u/BigPoppaK78 experienced "partial kv cache reprocessing" with Qwen 3.8 templates, and u/RevolutionaryPick241 reported the model "keeps stopping itself while reasoning" with UD v3, forcing a revert to v2. u/Oleszykyt discovered a bug in Unsloth Desktop where the estimated VRAM capacity didn't update when using KV cache quantization, and u/therealgmx encountered a "peg-native format" error with llama.cpp. u/DevelopmentBorn3978 also noted broken links on the Unsloth documentation page for Qwen3.8.

Humor/Off-topic (18 Comments - 174 Upvotes)
The thread included several lighthearted and humorous comments. u/RazsterOxzine joked about model speeds being "almost as fast as Qwen3.8-27B-Cold-Fusion-GAIN-V1.1-NM-DAU-NEO-MAX-MTP-GGUF," which led to u/AvidCyclist250 confirming, "yes guys, i just checked. it's real." u/Thin_Pollution8843 quipped, "Jensen dreaming on how he will sell you rtx6080 with 12gb of vram," and u/RedditAtWork23 declared, "I will be naming all my children after unsloth." u/Long_comment_san reacted to the 1-bit quantization with "that 1 bit quant is scary lmao 😂," and u/P47R1CK_IA noted, "These quants do be quanting."

(Total: 250 Comments - 2276 Upvotes)

# SENTIMENT ANALYSIS

The overall tone of the discussion was mostly neutral, with about 70% of comments falling into that category. Roughly 16% of comments were positive, filled with gratitude and excitement about the new model releases. About 14% of comments were negative, mostly consisting of bug reports, frustration with hardware limitations, or confusion about the MTP removal messaging. The positive comments often came from users thanking the Unsloth team directly, while the negative comments tended to focus on technical issues or unmet expectations around documentation and compatibility.

# TOP COMMENTS

## 400+ Upvotes

u/Jorlen

"Just want to say, thank you Unsloth team for these great quants.  Your hard work is appreciated!" (431 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vsr67c/introducing_qwen3827b_dynamic_v3_unsloth_ggufs/p4nmwow/

## 100+ Upvotes

u/Chromix_

"That's very nice. Can you also add a line for the previous Qwen 3.8 27B UD 2.0 quants to the graph, so that it's easier (or possible at all) to see how what most of us now have on disk compares to the latest and greatest? KLD and/or top-1 would probably be sufficient, I assume you still have that data from the previous quants." (158 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vsr67c/introducing_qwen3827b_dynamic_v3_unsloth_ggufs/p4ncmc2/

## 80+ Upvotes

u/yoracale

"There will definitely be loss in quality compared to BF16 but less than before! Same size but more recovery of accuracy " (86 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vsr67c/introducing_qwen3827b_dynamic_v3_unsloth_ggufs/p4nbvir/

## 70+ Upvotes

u/yoracale

"Edit: 
Yes we removed MTP **for the small ones under UD-Q2-K_XL** after some feedback from folks. All big ones UD-Q3_K_XL, Q4_K_XL etc all have inbuilt MTP still. It doesn't always work anyways edit: we still uploaded MTP but as a SEPARATE component so you can still use it!!" (70 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vsr67c/introducing_qwen3827b_dynamic_v3_unsloth_ggufs/p4ni79n/

## 60+ Upvotes

u/Adventurous-Gold6413

"So we can now run IQ4XS on 16gb vram without mtp" (67 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vsr67c/introducing_qwen3827b_dynamic_v3_unsloth_ggufs/p4nfw2z/

## 50+ Upvotes

u/yoracale

"We can add a graph in our blog regarding the previous versions!" (59 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vsr67c/introducing_qwen3827b_dynamic_v3_unsloth_ggufs/p4ndc5a/

## 40+ Upvotes

u/CatiStyle

"16G VRAM is like living on the edge, 4-bit run but no space for context (cut thinking answer short), and 3-bit is less smart." (42 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vsr67c/introducing_qwen3827b_dynamic_v3_unsloth_ggufs/p4o1c4q/

## 30+ Upvotes

u/Leflakk

"Will you also do DSV4 flash 0731?" (33 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vsr67c/introducing_qwen3827b_dynamic_v3_unsloth_ggufs/p4njn3n/

## 20+ Upvotes

u/Jcsq6

"The MTP was only removed for quants under UD-Q2\_K\_XL according to the ud3 description." (27 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vsr67c/introducing_qwen3827b_dynamic_v3_unsloth_ggufs/p4oskdk/

## 10+ Upvotes

u/danielhanchen

"Oh so we removed MTP for models smaller than UD-Q2_K_XL since even 500mb is needed for lower end GPUs " (19 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vsr67c/introducing_qwen3827b_dynamic_v3_unsloth_ggufs/p4phfjw/

# ORIGINAL POST

"Hey everyone! We’re releasing new Qwen3.8-27B GGUFs with 10% higher accuracy for the same size. This uses a new version of Dynamic v3.0

Unsloth Dynamic V3 outperforms others by >10% on Div-300, KLD & more benchmarks.

We also release 1-bit quants that retain 77% accuracy. Run on 8GB RAM.

Some of you already saw we updated our quants a few hours ago. No, nothing was broken, nothing needed fixes (I don't know why people even said this since it's a complete fabricated story). This was purely an update to make them EVEN BETTER.

We do not train on the imatrix calibration dataset, and we do NOT use QAT or QAD. Everything is done through post-training quantization. Our imatrix file used is available for the community to test, evaluate, and use. We encourage researchers and developers to create variations and fine-tunes of Qwen3.8 using our Unsloth quants/imatrix. You can read our over fitting analysis as well.

Blog with all details and more benchmarks: https://unsloth.ai/docs/basics/dynamic-3.0-ggufs

GGUF: https://huggingface.co/unsloth/Qwen3.8-27B-GGUF

Enjoy! We also will be doing a new Unsloth Desktop update today: https://github.com/unslothai/unsloth

We had A LOT of updates and will be introducing auto compaction, allowing external APIs to do tool calling and more."
