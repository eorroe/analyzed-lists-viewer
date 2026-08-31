import json
from collections import defaultdict

with open('data/1vqyo7y/flat.json') as f:
    comments = json.load(f)

real_comments = [c for c in comments if c['author'] != '[deleted]']

# Manual cluster assignments based on content analysis
# I'll assign cluster IDs and then summarize
cluster_map = {
    0: "Pro-IDE Advocates",
    1: "Text Editor/Terminal Purists", 
    2: "Hybrid/Context-Dependent Users",
    3: "Build Process & Compilation Control",
    4: "Performance, Resources & Bloat",
    5: "Education, Learning & Personal History"
}

# Assign each comment index to cluster
assignments = [
    0,   # 1. SoggyStress7785 - uses IDE to browse, compiles terminal (hybrid? actually leans pro-IDE for browsing) -> actually hybrid
    1,   # 2. EpochVanquisher - reply, passes flags easily -> hybrid/pro
    0,   # 3. burlingk - control over build process -> build process
    0,   # 4. EpochVanquisher - build process easy either way -> build process
    1,   # 5. lovelacedeconstruct - LSP, script -> text editor
    1,   # 6. EpochVanquisher - not sure what extra step -> text editor
    0,   # 7. Woshiwuja - cmake -> build process
    1,   # 8. lovelacedeconstruct - without cmake -> text editor
    1,   # 9. GhostVlvin - compile by hand in terminal, left jetbrains -> text editor
    3,   # 10. LordRybec - control over build process, learning each IDE -> build process
    4,   # 11. SoggyStress7785 - slower than terminal -> performance
    1,   # 12. neppo95 - not slower, hard to setup -> text editor/pro? actually defending IDE -> pro-IDE
    1,   # 13. scientist6092 - move to vim -> text editor
    1,   # 14. SoggyStress7785 - learning vim wasted -> text editor
    1,   # 15. scientist6092 - vim all the time -> text editor
    2,   # 16. txdsl - neovim/gcc/gdb, used various IDEs, nothing as seamless -> hybrid
    1,   # 17. scientist6092 - vim best for low level -> text editor
    4,   # 18. Reggie-Rectangle - vim response time, electron apps slow -> performance
    2,   # 19. txdsl - vscode not slow, m4 max -> hybrid
    1,   # 20. Hopeful_Rabbit_3729 - dude this reply -> text editor (reply to anti-vim? actually reply to txdsl vscode comment? parent is p49nkn7 which is anti-vim) -> text editor
    0,   # 21. ScallionSmooth5925 - don't like magic tools, don't know what happened -> pro-IDE (wants control/understanding)
    0,   # 22. Disastrous-Team-6431 - visual debugger, git colors -> pro-IDE
    3,   # 23. Loud_Anywhere8622 - misunderstanding, compilation steps obfuscated -> build process
    0,   # 24. ScallionSmooth5925 - syntax highlighting not IDE feature -> pro-IDE (text editors can do it)
    0,   # 25. Bloodshoot111 - settings menu clear, especially Clion -> pro-IDE
    5,   # 26. Loud_Anywhere8622 - bad IDE at college, CodeBlock -> education
    0,   # 27. Bloodshoot111 - CodeBlock at university -> education (but defending IDE) -> pro-IDE
    3,   # 28. neppo95 - build tools correctly, point is NOT see steps -> build process
    3,   # 29. Loud_Anywhere8622 - depends on what you're trying to achieve -> build process
    3,   # 30. neppo95 - verify compilation steps at setup -> build process
    3,   # 31. Loud_Anywhere8622 - IDE cool when you know how -> build process/hybrid -> build process
    0,   # 32. neppo95 - recommend clion/msvc -> pro-IDE
    0,   # 33. Disastrous-Team-6431 - CLion uses cmake -> pro-IDE
    0,   # 34. Xavier_OM - IDE calls cmake/make -> pro-IDE
    3,   # 35. max123246 - bad advice, nul-terminated strings -> off topic/build? actually off-topic -> build process (since it's about C details)
    0,   # 36. Vollink - stdio.h dependent on zero terminator -> build process/off topic -> build process
    0,   # 37. max123246 - avoid standard library -> build process
    3,   # 38. LordRybec - write() over printf, protocols required by tooling -> build process
    0,   # 39. neppo95 - why not use tool that speeds up work? -> pro-IDE
    1,   # 40. meepykittkitt69lmao - vim is all I need offensive -> text editor
    1,   # 41. zenthial - neovim/emacs customization better than IDEs -> text editor
    1,   # 42. LordRybec - IDEs not universally better -> text editor
    2,   # 43. My124thRedditAccount - emacs weird, basic features -> hybrid
    1,   # 44. LordRybec - nano/vim/emacs do it better -> text editor
    1,   # 45. LordRybec - emacs bloated -> text editor
    2,   # 46. dotNetromancer - file nav and git integration just as well -> hybrid
    1,   # 47. zenthial - binding files to hotkeys, magit -> text editor
    2,   # 48. LordRybec - used emacs for 3 months, now vim -> hybrid
    1,   # 49. Equal_Kale - xemacs customizations -> text editor
    1,   # 50. Reggie-Rectangle - slower in clion/vscode, vim shortcuts -> text editor
    1,   # 51. LordRybec - IDEs get in my way, auto-features -> text editor
    1,   # 52. LordRybec - faster without IDEs -> text editor
    1,   # 53. LordRybec - IDEs slow me down -> text editor
    1,   # 54. neppo95 - how so? -> text editor (question in anti-IDE thread? actually reply to LordRybec anti-IDE) -> text editor
    1,   # 55. LordRybec - type faster than autocomplete -> text editor
    2,   # 56. symbiatch - turn it off, wrongly working IDE -> hybrid
    1,   # 57. LordRybec - fewer IDEs allow disabling -> text editor
    1,   # 58. neppo95 - doubt you type faster -> text editor
    1,   # 59. LordRybec - accused of lying -> text editor
    1,   # 60. neppo95 - no better for every case -> text editor
    1,   # 61. LordRybec - you accused me -> text editor
    1,   # 62. neppo95 - sure buddy -> text editor
    2,   # 63. Big_Series4766 - small projects, vim -> hybrid
    2,   # 64. Candid_Zebra1297 - rawness of black and white -> hybrid (likes terminal but acknowledges IDE power)
    1,   # 65. Rough_Employee1254 - vi is all I need -> text editor
    1,   # 66. dmc_2930 - vim yes, pure vi sadistic -> text editor
    2,   # 67. flyingron - make and emacs, sometimes xcode/vs -> hybrid
    2,   # 68. Rough_Employee1254 - respect for emacs -> hybrid
    2,   # 69. flyingron - emacs build mode -> hybrid
    1,   # 70. stvpidcvnt111111 - ed is standard editor -> text editor
    2,   # 71. LordRybec - edlin in dos -> hybrid
    1,   # 72. lovelacedeconstruct - Larp -> text editor (insult)
    2,   # 73. MagicalPizza21 - insults better left unsaid -> neutral/hybrid
    2,   # 74. Sergey5588 - nvim with clangd, gdb -> hybrid
    1,   # 75. Ultimate_Sigma_Boy67 - you're a real chad -> text editor
    1,   # 76. Muffindrake - burned by GUIs -> text editor
    2,   # 77. LordRybec - wish I could upvote, MSVS pain -> hybrid
    2,   # 78. StrangelyEroticSoda - linux notepad, would install vscode -> hybrid
    1,   # 79. Ultimate_Sigma_Boy67 - kate or kwrite? -> text editor
    2,   # 80. LordRybec - used to use kate -> hybrid
    2,   # 81. StrangelyEroticSoda - mousepad -> hybrid
    0,   # 82. chakie2 - all in with CLion -> pro-IDE
    5,   # 83. GenericFoodService - no IDE looks/behaves how I'd like -> education/preference
    0,   # 84. MagicalPizza21 - IDE for visual layout and debugger -> pro-IDE
    2,   # 85. EnderPSO - emacs for school, vim for work, IDE at home -> hybrid
    2,   # 86. honkai-yuri-fan - gcc on windows, know where stuff is -> hybrid
    1,   # 87. LordRybec - MSYS2, MSVS bloated, know where things are -> text editor
    0,   # 88. Glorwyn - IDE to highlight typos, look through files -> pro-IDE
    2,   # 89. maep - one workflow everywhere, SSH, gdb visual mode -> hybrid
    2,   # 90. LordRybec - vim on target systems -> hybrid
    3,   # 91. qrzychu69 - renaming function requires IDE/LSP -> build process
    5,   # 92. Royal-Ninja - professor demanded no IDE -> education
    2,   # 93. LordRybec - discouraged from IDE first 4 semesters -> hybrid
    1,   # 94. kun1z - IDEs large, clunky, use Notepad++ -> text editor
    1,   # 95. LordRybec - vim with auto-anything disabled -> text editor
    1,   # 96. Easy-Nothing-6735 - vim for everything to save RAM -> text editor
    2,   # 97. akmark - emacs, LSP gives IDE features -> hybrid
    2,   # 98. rupturefunk - IDE for debugging, basic editor for rest -> hybrid
    1,   # 99. LordRybec - debugging without debugger, not enough to use IDE -> text editor
    2,   # 100. tobdomo - vscode as editor, build tools, external debugger -> hybrid
    2,   # 101. unbrand - Qt Creator -> hybrid
    1,   # 102. Stemt - IDE too slow, use vim -> text editor
    2,   # 103. LordRybec - creating new project annoying -> hybrid
    2,   # 104. tastygames_official - many languages, notepad++ or code oss -> hybrid
    2,   # 105. ape_rei - professional, windows c#, neovim/clangd for personal -> hybrid
    2,   # 106. FedUp233 - no IDE when started, separate editor and command line -> hybrid
    2,   # 107. eeriera - vim, IDE sounds like relearning -> hybrid
    2,   # 108. FewDevice2218 - Linux is IDE -> hybrid
    4,   # 109. Cash1942 - IDE+cmake slow, sublime faster -> performance
    4,   # 110. Unfair-Ocelot-2363 - IDE's are bloat -> performance
    2,   # 111. TheTrueXenose - neovim, IDEA felt less good -> hybrid
    2,   # 112. GhostVlvin - IDE good for 1 language, use nvim -> hybrid
    2,   # 113. anhadsa - nvim does it, decent lsp client -> hybrid
    0,   # 114. greg-spears - IDE assists with coding, popup function def -> pro-IDE
    2,   # 115. nimzobogo - Emacs + Eglot/LSP -> hybrid
    2,   # 116. alexcleac - discussion still going while AI discussion -> hybrid
    2,   # 117. Deathisfatal - many languages, powerful text editor -> hybrid
    2,   # 118. Realistic-Stress4547 - learned neovim before programming -> hybrid
    2,   # 119. fdwr - Alt+Tab adds up -> hybrid
    0,   # 120. West-Mycologist-6490 - Clion 90% of time -> pro-IDE
    2,   # 121. NoSpite4410 - emacs is my IDE -> hybrid
    0,   # 122. BlockOfDiamond - Xcode for OSX -> pro-IDE
    0,   # 123. BuyerImpressive4325 - Clion checks for bad code -> pro-IDE
    1,   # 124. Reggie-Rectangle - vim churn code fast -> text editor
    3,   # 125. mikeblas - how do you debug in vim? -> build process
    2,   # 126. Reggie-Rectangle - LazyVim, LLDB/GDB -> hybrid
    3,   # 127. mikeblas - assume they run gdb -> build process
    3,   # 128. HashDefTrueFalse - gdb/lldb directly -> build process
    1,   # 129. Reggie-Rectangle - no tree viewer not a slight -> text editor
    3,   # 130. HashDefTrueFalse - ranger for filesystem -> build process/hybrid -> build process
    3,   # 131. Ultimate_Sigma_Boy67 - normal debuggers, lldb/gdb -> build process
    3,   # 132. honkai-yuri-fan - never learned debug, printf billion -> build process
    3,   # 133. mikeblas - something you might want to work on -> build process
    3,   # 134. rupturefunk - like a caveman -> build process
    2,   # 135. gwenbeth - docker kills IDE debugger, use emacs -> hybrid
    2,   # 136. Different_Panda_000 - vi then Visual Studio -> hybrid
    2,   # 137. Pale_Bee_7638 - emacs everything, ~1GB RAM -> hybrid
    2,   # 138. 4iqdsk - text editors do everything, one editor -> hybrid
    2,   # 139. Vollink - holy war, vi keybindings -> hybrid
    2,   # 140. sirflatpipe - full IDEs clunky -> hybrid
    0,   # 141. BigTortuga - CLion to remove friction -> pro-IDE
    2,   # 142. FederalProfessor7836 - AI, editor for spot checking -> hybrid
    2,   # 143. W0x3r - Nano for simple, VSCodium for big -> hybrid
    2,   # 144. gswdh - AI don't look at code -> hybrid
    1,   # 145. Ultimate_Sigma_Boy67 - clown emoji -> text editor
    2,   # 146. gswdh - wind up on here -> hybrid
]

assert len(assignments) == 146, f"Expected 146 assignments, got {len(assignments)}"

clusters = defaultdict(list)
for i, c in enumerate(real_comments):
    clusters[assignments[i]].append(c)

for cid, clist in sorted(clusters.items()):
    print(f"Cluster {cid} ({cluster_map[cid]}): {len(clist)} comments, {sum(c['score'] for c in clist)} upvotes")

print(f"Total: {sum(len(v) for v in clusters.values())} comments, {sum(sum(c['score'] for c in v) for v in clusters.values())} upvotes")
