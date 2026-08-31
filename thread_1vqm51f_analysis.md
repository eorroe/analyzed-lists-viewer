# REDDIT POST ANALYSIS

A review posted by u/maxwell321 in r/LocalLLaMA got 474 upvotes and sparked 110 comments. The author tested Qwen 3.8 27B against classic arcade game recreations like Galaga and found it dramatically outperformed its predecessor, Qwen 3.6 27B, especially when set to high thinking modes. "Qwen 3.8 thinks a LOT, but it draws out those tiny details and absolutely nails it after the fact," the author wrote, noting the model captured animations, sound effects, and even the fighter capture mechanic that previous versions missed. The post also compares Qwen 3.8 to Claude Sonnet 5 and Opus 5, concluding that with the right prompting harness, Qwen 3.8 can reach Opus-level results while running locally on consumer hardware. The author predicts that 4B models will match Qwen 3.8 27B within a year, and that sparse Mixture-of-Experts variants like Qwen 3.8 35B A3B will further close the gap to proprietary models.

# REDDIT COMMENTS ANALYSIS

[Arcade Demo Hype vs Real Work] (15 Comments - 325 Upvotes)
Many commenters argued that building arcade game clones is more of a parlor trick than a real test of model capability. "Is it just me or do all these post with 'it can make a flappy bird' it can make space invaders' giving a false bias of capability?" asked u/Koakie, noting that these demos look flashy but don't prove a model can handle unique, original work. Others agreed that while these tests look impressive, they mostly measure how well a model memorized common tutorials rather than its true problem-solving ability.

[Model Quality & Benchmarking] (5 Comments - 6 Upvotes)
A smaller cluster debated what actually counts as a good benchmark for model intelligence. u/Good-Penalty-4838 argued the game recreation test is still valuable because it checks whether a model can reconstruct complex systems from internal knowledge. Others pointed out that benchmarks are often gamed, and that one-shot demos give a misleading picture of how a model will perform on real production tasks.

[Harness & Tooling Setup] (35 Comments - 108 Upvotes)
The largest conversation thread revolved around which coding harness, agent framework, and local serving setup works best with Qwen 3.8. Users shared experiences with OpenCode, Hermes Agent, Pi, maki.sh, and VS Code Copilot, discussing trade-offs between speed, context usage, and reliability. "I use opencode and i am pretty happy with it, codex also works well" wrote u/wgaca2, while u/noiserr recommended OpenCode for coding and Hermes Agent for higher-level tasks. Several users noted that MLX quantization caused issues and that GGUF or original weights performed better.

[Comparisons to Sonnet/Opus] (22 Comments - 120 Upvotes)
Many comments compared Qwen 3.8 directly to Claude Sonnet 5 and Opus 5. u/Repulsive_Initial308 distilled the post to "tldr: opus at home," while u/Bill_Salmons joked "tldr: RTX 3050 = Pro 6000 at home." Others agreed Qwen 3.8 sits between Sonnet and Opus in raw intelligence but trails on world knowledge. u/goldcakes noted "The pure agentic intelligence is somewhere between Sonnet and Opus 4.6 IMO. The world knowledge is obviously a lot less." Several users were skeptical, with d4mations flatly stating "No, it doesn't come close to Sonnet."

[Technical Deep Dives & Code] (5 Comments - 32 Upvotes)
Some commenters dug into the nitty-gritty of implementation details. u/bick_nyers described a specific threading and event pattern in their codebase where the model consistently tried to "shoehorn things in" rather than respecting existing architecture. Others discussed how Qwen struggles with negative instructions and how reinforcement learning can produce novel solutions. u/AD7GD observed that a shocking amount of software engineering is just remaking the same old things, so arcade demos are not entirely without merit.

[General Support & Reactions] (20 Comments - 59 Upvotes)
The rest of the thread was filled with users sharing their own experiences with Qwen 3.8, praising the review, and expressing excitement about future developments. "Agreed it feels like a big step up at this size," wrote u/tarpdetarp. u/daaain noted that getting models like Opus to write helper scripts on their own is "delightful." Many users thanked the author for the detailed write-up and said they planned to test Qwen 3.8 themselves. A few complained about images making the post laggy.

(Total: 102 Comments - 650 Upvotes)

# TOP COMMENTS

## 100+ Upvotes
u/Koakie
"Is it just me or do all these post with "it can make a flappy bird" it can make space invaders" giving a false bias of competence of ai?

It can make it, because it has reference of what flappy bird should look like. I can make space invaders, including the "insert a coin" screen because the the sample data is out there.

During the lawsuit of suno ai, they asked "make a disco song with these lyrics" and then used the exact lyrics of daddy cool. Suno 9 out of 10 just spit out an exact copy of Boni M - Daddy Cool to prove that it's just copying shit.

I don't want to use AI to make an exact copy of pacman. I want to make the next pacman. Same with comfyui i can prompt a lot of stuff that looks the same as what's already out there (corporate logos, etc) but I find it a lot harder to make new shit" (235 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vqm51f/long_review_qwen_38_27b_is_very_good_at_tapping/p46od4d/

## 10+ Upvotes
u/Repulsive_Initial308
"tldr: opus at home" (69 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vqm51f/long_review_qwen_38_27b_is_very_good_at_tapping/p46j99p/

# ORIGINAL POST

"Long Review: Qwen 3.8 27B is VERY good at tapping into it's real-world knowledge. It's "overthinking" brings it to Sonnet level performance with the potential for Opus level results."

"Hi all! I finally just got around to testing out Qwen 3.8 27b. I'm using Unsloth's UD-Q8\_K\_XL quant as a sit-in replacement to Qwen 3.6 27b, same quant size. Wow -- this thing isn't messing around.

I have many baseline test prompts to gauge the 'intelligence' and usability of the model, but a go-to one is asking it to do a 1:1 recreation of classic arcade games (like Galaga, Donkey Kong, Pac-Man, etc). I do this to see what little details it gets correct.

I've tested this process on pretty much every model I could fit on my machine. In total, I have 3x 3090's and 1 Tesla P40 at my disposal, with 128gb of system memory. I've also tested on frontier models both in the webUI and across multiple harnesses.

I've been using Qwen 3.6 primarily, and occasionally switching to Deepseek V4 Flash. Now I'm starting to feel like the ladder is not longer necessary.

Originally in these games/tests, Qwen 3.6 would get the basics down (maybe a few fancy effects and animations) but it always felt about 75% there. It rarely posed technical issues, but little features and tiny details were either missing or 'half-ass' implemented. I had no problem further instructing it to add these and doing some 'hand-holding' for it. Overall though Qwen 3.6 super comparable to other models in it's weight class, but ultimately the precision was the best in the frontier models' results. With extra prompting and multi-shot planning phases (via a custom harness I have with prompts to kinda prompt it to think about the little details, then injecting key elements into a fresh session's prompt) I've managed to milk out smaller details that the model clearly had in it's internal knowledge, but forgot about it entirely for the relevant prompt.

  
Qwen 3.8 thinks a LOT, but it draws out those tiny details and absolutely nails it after the fact. It makes it worth the wait and context usage, and it helps close the gap between local and proprietary models a LOT.

Here's an example:

Prompt: "Create a single page html + tailwind css + javascript recreation of Galaga, 1:1 to the original arcade game"

Qwen 3.6 27B's 'Galaga' clone:

https://preview.redd.it/4nx5c98gyujh1.png?width=874&format=png&auto=webp&s=5984272dff7636b68f968f22da57f5b827860065

This 'Galaga' clone ended up pretty much being a space invaders clone instead. Enemies didn't shoot back or swoop down or do anything special, until I did additional prompting. It was a decent look but it wasn't anything remotely faithful to the original game.

Qwen 3.8 27B wiped the floor with this one:

https://preview.redd.it/yae6n9753vjh1.png?width=992&format=png&auto=webp&s=2d461ab4483a101533a62cdeaef547543d0f23c8

Rather than strictly using SVG polygons to design the enemies, Qwen 3.8 used a pixel bitmap type deal (is that the right word?) that constructed the sprite dynamically:

https://preview.redd.it/gen91i2i3vjh1.png?width=1398&format=png&auto=webp&s=b565315ab7aa8e2b51d082ec887b9ae389e47fcf

Which is pretty cool. There also seems to be a CRT-like filter and effects on the screen, including a power-on simulation on the screen. Not only that, but they were ANIMATED. Each sprite switched between two states (the first line and second line, as you see in the code above). It also managed to nail the small gameplay details like the characters swooping down, enemies shooting at you. I was VERY surprised to find that Qwen 3.8 managed to remember and implement the was the fighter capture system. In Galaga, there's a special enemy that can capture your ship and use it against you, but by shooting the enemy you can get it back and have two ships on the screen at once. Qwen 3.8 managed to remember and implement this. The only issue is that instead of a beam coming down to capture you, the special enemy just ran into you to capture you. Regardless, it was impressive that it remembered this and implemented it in a way -- one small correction in a follow-up prompt, or a more precise starting prompt would have fixed it.

It also implemented SOUND EFFECTS too, which Qwen 3.6 didn't even bother. It also had idle screens and screens that were shown when the page was open and not on screen:

https://preview.redd.it/yxybaki84vjh1.png?width=626&format=png&auto=webp&s=202da21c84c3bf08ee119a7980411d16dc2bd7e9

As if it were an actual arcade cabinet running the game, even with an 'Insert Coin' simulation. 

As you can see though, the sprites (and sound effects) weren't 1:1 with Namco's Galaga, but much closer and more tasteful than Qwen 3.6.

Here's where I'm at though, and where it brings me back to the post's title. Qwen 3.8 thinks a LOT. Luckily my machine is able to handle it due to high token throughput, but anyone that needs to offload layers will probably we waiting a while.

Here's my main issue though with this testing:

Qwen 3.6's Galaga clone took 8 seconds of thinking.

Qwen 3.8 (xHigh)'s Galaga clone took 15 minutes of thinking.

It may have been worth it to just tell it to manually implement these things with follow-up prompts. I believe if I took the time to hand-hold it and guide it to make the capture system, sound effects, etc. It probably would have been 5 minutes total (or 8-10 minutes total, assuming I had to wait longer for more thinking tokens, re-generation of code, and more debugging).

I tried the :low and :medium settings and got these results:

  
Qwen 3.8 27b (low):

https://preview.redd.it/viwdd4dukvjh1.png?width=940&format=png&auto=webp&s=53bba90e2b8cad440ae514f2dd810eeef0f3d9bc

Playability wise, it's very comparable to Qwen 3.6. It does have some sound effects though! Characters swoop down but don't shoot or abduct/capture the player. 3 seconds of thinking total.

  
Qwen 3.8 27b (medium):

https://preview.redd.it/dfuxe5w6nvjh1.png?width=962&format=png&auto=webp&s=42476d436bab01c986844400979aa8fcc2f81c21

I found that despite thinking being 3 minutes long, most of the thinking content was actually drafting out the code blocks and labeling them, it only reconsidered and rewrote a chunk once or twice. By the time it came to output the actual response, the MTP had gotten extremely fast (91 tk/s vs 62 tk/s starting rate). Quality wise, I think this is a really happy medium and am surprised that it isn't the default. The reasoning was much better to wait for, and it delivered like 90% of the result that xHigh delivered. True 8-bit characters are back (with two animation frames again), sound effects, proper swooping and shooting. It forgot about the abduction/capturing system, but with one quick follow-up prompt and 2 more minutes of thinking, it managed to implement it without hassle.

More impressively, since the textures were in a text bitmap type format, I wanted to see how well it would implement the original game's graphics based on a reference picture.

https://preview.redd.it/njhdw63sovjh1.png?width=770&format=png&auto=webp&s=f9fdc94d9034d4a5fb49c7e3edd7fa20a0857719

I provided the picture above, and was pretty impressed when it implemented the textures pretty faithfully except for the player's ship (everything still has an off-brand look though), and also gave them animations!

https://preview.redd.it/yxc4dt1uqvjh1.png?width=792&format=png&auto=webp&s=09390db28c583f595276d16d0cb551d4d047d56d

After regenerating prompt to give it another chance, it managed to get the ship closer to the original but a couple other sprites were off. I'm going to settle on it "mostly" gets it right. In medium mode. I'm going to give it the benefit of the doubt and assume that a follow-up prompt or two can eliminate the ones that are pretty off. :xHigh didn't have this problem but had the same quality. I didn't think that it would improve really, as reasoning doesn't really help understanding of image contents.

https://preview.redd.it/j8c7ni4ttvjh1.png?width=92&format=png&auto=webp&s=15881cf5d6640cc0ec5cf0a7a512ee7c26fc1d0d

I put Claude Sonnet 5 through the same test:

https://preview.redd.it/f5lc8f0xjvjh1.png?width=866&format=png&auto=webp&s=f48723828168b67e75e266d53a87b5d225232fca

Sonnet's was about on-par with Qwen 3.8 27b xHigh, though the sprites themselves didn't have animations like Qwen 3.8 xHigh's and Opus's results. Sonnet took 3 minutes total. When prompted to reference the actual namco images, I noticed it was using a 'zoom' tool to get a better / closer look at sprites, resulting in a little bit better accuracy:

https://preview.redd.it/c06snqct1wjh1.png?width=804&format=png&auto=webp&s=c331d06e8834f08608fe883e34e9815ef1b826e9

Testing with Clade Opus 5 on High effort, it managed to unsurprisingly beat everything else (in my opinion) though also taking 15 minutes of thinking (roughly, the first 10 minutes got interrupted by my 5 hour limit cooldown, and proceeded to take 5 more minutes after i resumed it):

https://preview.redd.it/2btvmjr0uvjh1.png?width=684&format=png&auto=webp&s=716ce3671e335c08f28ed7c5ea4b3ca9346e8b2d

Better animations (enemies swirl in in formations, very faithful to the original game), better sound effects, much more stylistic accuracy, the whole nine yards. It even had challenge rounds!

When asked to implement the sprites from the image. Instead of analyzing the image directly, it actually build and ran a python script to extract the exact pixel grid from the reference image, resulting in 1:1 replicas:

https://preview.redd.it/8s8ogiy1zvjh1.png?width=718&format=png&auto=webp&s=0bacca9c09a013cac4696f70ae8d7febfb70c9fe

This blew me away, so I wanted to see if Qwen could do the same or similar when prompted properly.

Prompt:  
"Here are proper Galaga sprites, replace your designs with these ones. Since you have trouble making pixel art, we can leverage Python to get you information as needed. Give me a python script to run that will give you the data needed from the image."

It then provided me with the Python script to run on my machine and pass the image into, and it requested that I paste the output to it. It successfully pulled it off!

https://preview.redd.it/v62f6guw6wjh1.png?width=812&format=png&auto=webp&s=2118ed373dad179f3605c4f346a5167073a90988

This convinces me that with the proper harness (or system prompt + tools), Qwen 3.8 27b can reach Opus levels of performance.

We're at a point where the reasoning in these local models are so strong, it's able to produce the same end result as frontier models. It's only a matter of time (thinking tokens) and the ability to prompt it properly. Harnesses are super important and can practically eliminate the ladder. 

I think we're about to enter a speed race and optimization race now. Instead of competing for the best knowledge, model providers might start looking into "how can I do this but faster or with less VRAM?". I'm really convinced that we have a LOOOONG way to go before model weights are completely optimal for the size/performance ratio. Models clearly have this knowledge available to them, it's just a matter of tapping into it. I'm predicting that as soon as one year from now, 4b models will be on-par with Qwen 3.8 27b.

This gets me excited for future Qwen models now too. Qwen 3.8 35b A3B will be game changer as it will probably get close to this level of precision but take a fraction of the time due to only 3b active parameters. A Qwen 3.8 122b A10B would be the nail in the coffin for proprietary models as it offers much more real world knowledge, faster speed, and comparable reasoning skills to a dense model. Qwen 3.8 27b is going to be an open-weight KING for a while.

Thank you for reading!"