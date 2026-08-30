# REDDIT POST ANALYSIS

This post from u/chiribe in r/LocalLLaMA shares their personal experience running the Qwen 3.8 27B model on modest hardware—specifically an RTX 5060 Ti with 16GB of VRAM paired with an Intel N100 CPU. After pushing over 1 million tokens through the model using agentic coding workflows over a weekend, they published their exact llama.cpp configuration that achieved a 73,728-token context window. The post is written in Spanish and tagged as a Tutorial | Guide, with a gallery of screenshots showing their setup. The community responded enthusiastically to this practical, real-world configuration guide, sparking extensive discussion about quantization, speculative decoding, and hardware optimization for local LLM inference. The most frequently discussed topics centered on llama.cpp configuration parameters, KV cache quantization, MTP speculative decoding, context window size, and VRAM management. Users shared their own configs, debated sampling temperatures, and compared results across different GPUs including RTX 5060 Ti, 4090, 3090, AMD 6800, and 7900 XTX.

# REDDIT COMMENTS ANALYSIS

Praise and Enthusiasm (31 Comments - 574 Upvotes)
The largest cluster by far is made up of people thanking the author and celebrating the post as exactly the kind of practical content they want to see after new model releases. Comments like "Folks, this is the type of thread I want to see after release of any new models. Thanks u/chiribe" and "Awesome write up! Super interesting" show genuine excitement. Many users called the post "impressive," "goated," and "amazing," with several noting they have similar 16GB VRAM setups and finally feel like they have a working reference.

Configuration Deep Dive (64 Comments - 289 Upvotes)
This is the most technically dense cluster, where users dissect every parameter in the shared config file and offer their own refinements. The discussion centers on MTP (Multi-Token Prediction), ngram-mod speculative decoding, KV cache quantization choices (q4_1 vs q8_0), sampling temperatures, and batch sizes. Users like u/pmttyji suggested combining ngram with MTP, while u/ea_man shared their complete AMD 6800 config. There was significant back-and-forth about whether temperature 0.65 is correct for Qwen 3.8 thinking mode, with multiple users pointing out that the official recommendation is temperature 1.0. u/chiribe actively engaged in this cluster, updating their config based on feedback and reporting that enabling ngram-mod alongside MTP boosted speed to ~46 t/s on JavaScript generation.

Questions and Curiosity (29 Comments - 39 Upvotes)
A steady stream of newcomers asking how the setup works, how to replicate it, and whether it will work on their specific hardware. Questions ranged from "How did you come up with this setup? Trials and errors?" to "Will this work on weird dual GPU setups?" and "How do you turn on agentic coding or tool calls in Llama.cpp?" Many users with 5090s, 4090s, and other GPUs asked if the config translates directly, while others wondered about specific flags like "patched llama.cpp" and the difference between various quantization formats.

Hardware and Compatibility (28 Comments - 55 Upvotes)
This cluster focuses on the physical hardware and operating system choices behind the setup. Users discussed their own GPU and CPU combinations, with several sharing that they run similar hardware (RTX 5060 Ti, 4090, 3090, 7900 XTX) and confirming the config works or asking for tweaks. There was notable debate about Windows versus Linux for local AI, with u/Ammargok stating that "Windows is really bad for local ai" due to VRAM usage differences. Others shared experiences with Mac M-series chips, noting that MTP behaves differently on Apple Silicon due to unified memory constraints.

Skepticism and Pushback (3 Comments - 9 Upvotes)
A small but vocal cluster of users questioning the validity and practicality of the shared configuration. u/AvidCyclist250 delivered a lengthy technical critique, arguing that the math doesn't add up for running a 27B dense model with 73k context and MTP draft cache on 16GB VRAM, pointing out that "A 27B dense model with about 12.5gb plus a 73k KV cache plus your MTP draft cache requires over 17GB of VRAM" and that "Setting fit = off doesn't magically make 17gb fit into a 16GB GPU." u/sensitivecrocodile tested the exact settings and reported only 19 t/s compared to 38 t/s with IQ3_XXS, calling it a waste of time. u/electrified_ice sparked a minor flame war by asking "Why are you using llama cpp?" which drew downvotes and defensive responses.

Alternative Approaches (6 Comments - 20 Upvotes)
Users suggesting different tools, frameworks, or quant formats that might work better for similar hardware. u/SOC_FreeDiver shared their testing results showing that spec-draft-p-min 0.85 actually slows things down despite higher acceptance rates, and that ubatch 1024 trades context size for prefill speed. u/Danmoreng recommended an alternative config achieving ~60 t/s with IQ3_XXS and 80k context. u/bobaburger shared a detailed comparison showing 35 tps with q8_0 KV cache and 150k context using -nkvo to offload KV cache to RAM, versus 59.8 tps with q4_0 KV cache and 73k context. Others mentioned trying NVFP4 on RTX 50-series cards or using vLLM/SGLang instead of llama.cpp.

(Total: 161 Comments - 986 Upvotes)

# TOP COMMENTS

## 300+ Upvotes

u/pmttyji
"Folks, this is the type of thread I want to see after release of any new models. Thanks u/chiribe" (350 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vqrt86/after_pushing_1m_tokens_through_qwen_38_27b_here/p47qwuh/

## 100+ Upvotes

u/dsdt
"i was gonna say how the f? then i saw 

* **Model:** `Qwen3.8-27B-UD-Q3_K_XL.gguf`
* **KV Cache Quant:** `q4_1` for main context, `q5_1` for MTP draft context

thanks for sharing your numbers.

" (100 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vqrt86/after_pushing_1m_tokens_through_qwen_38_27b_here/p47oc06/

## 40+ Upvotes

u/Equivalent_Bit_461
"Impressive but I don't trust a q3, I'll stick to my q6 offloaded moes.

Fellow 16gb vramlet here as well, tho I have 8 times the ram..." (45 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vqrt86/after_pushing_1m_tokens_through_qwen_38_27b_here/p47pkgv/

u/pmttyji
"u/chiribe Did you try with ngram together with MTP?

    spec-type = draft-mtp
    spec-draft-n-max = 2
    spec-ngram-mod-n-match = 24
    spec-ngram-mod-n-min = 48
    spec-ngram-mod-n-max = 64" (40 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vqrt86/after_pushing_1m_tokens_through_qwen_38_27b_here/p47rnlu/

## 10+ Upvotes

u/johnzadok
"Why did you use a different sampling parameters than the one official doc suggests at https://huggingface.co/Qwen/Qwen3.8-27B:

> We recommend using the following sets of sampling parameters for generation:
```
    Thinking Mode: temperature=1.0, top_p=0.95, top_k=20, min_p=0.0, presence_penalty=0.0, repetition_penalty=1.0
    Instruct (or non-thinking) mode: temperature=0.7, top_p=0.80, top_k=20, min_p=0.0, presence_penalty=1.5, repetition_penalty=1.0
```" (26 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vqrt86/after_pushing_1m_tokens_through_qwen_38_27b_here/p48c645/

u/chiribe
"Not really an option with my setup, weak CPU, PCIe 3.0 x4, and single-channel DDR5 RAM. I know there were syntax errors, but fortunately the automated tests and linter caught them and the model fixed them on its own." (26 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vqrt86/after_pushing_1m_tokens_through_qwen_38_27b_here/p47qsq1/

u/chiribe
"I'm actually not super familiar with how n-gram works under the hood here, so I'll read up on it and test it out with your parameters. Thanks!" (25 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vqrt86/after_pushing_1m_tokens_through_qwen_38_27b_here/p47snty/

u/dsdt
"It seemed impossible with 70k context window with a 5060ti, since I have two and maximum I can get is 100k with q8 kv cache." (17 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vqrt86/after_pushing_1m_tokens_through_qwen_38_27b_here/p49l50y/

u/ea_man
"Here's mine for 16GB on AMD 6800:

    # https://huggingface.co/vmarcelo/Qwen3.8-27B-MIX_GGUF
    # Vulkan max context:86784 with MTP n=2 speed TG 39.91t/s
    # ctx patched: 86784, unpatched mainline llama.cp: 78080
    # ROCm:  max ctx 84480, unpatched 31488, speed TG 40.58
    
    
    # 1. Set Environment Variables
    export LD_LIBRARY_PATH="/home/eaman/llama/bin_vulkan" 
    
    # 2. Run the Server
    /home/eaman/llama/bin_vulkan/llama-server  --device vulkan0 \
     -m /home/eaman/.lmstudio/models/vmarcelo/Qwen3.8-27B-IQ4-MIX.gguf \
    --host 0.0.0.0  -fa on --load-mode none --jinja --no-log-timestamps \
    -ctk q5_1 -ctv q5_1 \
    --temp 0.8 --top-k 20 --top-p 0.95 --min-p 0.0 \
    --presence-penalty 0.0 --repeat-penalty 1.0 \
    -b 1024 -ub 128 --fit-target 30 \
            --spec-type draft-mtp,ngram-mod --spec-draft-p-min 0.82 --spec-draft-n-max 2 \
            --cache-type-k-draft q4_0 --cache-type-v-draft q4_0 \
            --spec-ngram-mod-n-match 24 --spec-ngram-mod-n-min 8 --spec-ngram-mod-n-max 32 \
    --reasoning on --chat-template-kwargs '{"reasoning_effort":"medium"}' --chat-template-kwargs '{"preserve_thinking":true}' --reasoning-budget 14000 --reasoning-budget-message " -- Reasoning budget exceeded, proceed to final answer." \
    --ctx-checkpoints 96 --cache-ram 6000 -np 1 -ngl 99 -lv 3 --no-warmup  

Note: this is for 16GB with desktop in software rendering, headless should give some ~70MB more vRAM for ctx." (17 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vqrt86/after_pushing_1m_tokens_through_qwen_38_27b_here/p4838ri/

u/LetsGoBrandon4256
"> cross-checking my configs with ChatGPT and Claude.

OP asked catGPT and Claude. In other words, the clanker hallucinated the sampler params. 

This is the actual recommended sampler config from Qwen's huggingface page.

> We recommend using the following sets of sampling parameters for generation:

> Thinking Mode: temperature=1.0, top_p=0.95, top_k=20, min_p=0.0, presence_penalty=0.0, repetition_penalty=1.0 

> Instruct (or non-thinking) mode: temperature=0.7, top_p=0.80, top_k=20, min_p=0.0, presence_penalty=1.5, repetition_penalty=1.0

Unsloth's model page reference the same values. I have no idea where OP got that "Official / Recommended" from" (17 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vqrt86/after_pushing_1m_tokens_through_qwen_38_27b_here/p49011i/

u/chiribe
"Update on this: I hadn't enabled ngram-mod properly earlier. With it running alongside MTP, speed jumped to ~46 t/s on JavaScript generation (+6-8 t/s gain). Appreciate the advice! I'll edit the main post shortly to reflect all the optimizations from the comments." (15 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vqrt86/after_pushing_1m_tokens_through_qwen_38_27b_here/p49pebi/

u/Craftkorb
"There are agents that integrate with LSP to tighten the compile-and-fix loop. Opencode is one of them, but you have to enable it in the config" (13 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vqrt86/after_pushing_1m_tokens_through_qwen_38_27b_here/p482rel/

u/Constandinoskalifo
"Curious about why such a low temperature? Is there a reason you deviated from the official one?" (13 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vqrt86/after_pushing_1m_tokens_through_qwen_38_27b_here/p47w72u/

u/AvidCyclist250
"I know Qwen 27B isn't a moe model. Which also makes your claims impossible or at least weird as fuck. All 27B parameters are active during prompt ingestion. Changing your system prompt to switch "sub-agents" invalidates the llama.cpp prefix cache. Re-running tens of thousands of tokens of project history through a 27B dense model at a crippled ubatch size of 512 does not take a few seconds either. The only way is is realistic is if your context is actually tiny and nowhere near 73k

And there is a reason llama.cpp offloads to CPU. A 27B dense model with about 12.5gb plus a 73k KV cache plus your MTP draft cache (which you weirdly set to a higher precision of q5_1) requires over 17GB of VRAM. Setting fit = off doesn't magically make 17gb fit into a 16GB GPU even if headless. It just means you haven't crashed yet because at least from what I can tell your wiping script keeps you far below the 73k limit.

Just looking at the math. And the agentic buzzwords for a sequential Python loop. You neutered the model with top-k = 15, wrong temp, and shit quants and medium reasing, and your VRAM math is weird. the official recs aren't what you say they are.

image 1: 30% context with 15,358 MiB out of 16,311 MiB used 

image 2: asking for Node.js/Cheerio script, and you got C# .NET 

image 3: threads = 3 and threads-batch = 4. but core 1 is 100% loaded and the others are idle. why is the hostname of your terminal j1900 if you have a n100?" (13 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vqrt86/after_pushing_1m_tokens_through_qwen_38_27b_here/p4970rz/

u/lood9phee2Ri
"ngram tends to help with "iterative refinement" conversational tasks since it drafts based on previous. Like "make a html page saying blah", "okay now make the text blue".  I'm just using `--spec-type ngram-simple,draft-mtp --spec-draft-n-max 3`" (10 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vqrt86/after_pushing_1m_tokens_through_qwen_38_27b_here/p48c1iy/

u/YearnMar10
"Official temperature recommendation is 1 for thinking " (10 Upvotes) - https://www.reddit.com/r/LocalLLaMA/comments/1vqrt86/after_pushing_1m_tokens_through_qwen_38_27b_here/p47x4un/

# ORIGINAL POST

"Dando seguimiento a mi post anterior sobre cómo tengo montado mi servidor de presupuesto (Intel N100 + RTX 5060 Ti 16GB), varios me preguntaron por una mirada más profunda a mi configuración real de inferencia y al desempeño agentic en el mundo real.

Como muchos de ustedes, estaba refrescando la página esperando descargar Qwen 3.8 27B apenas salió. Después de pasar todo el fin de semana estresándolo con flujos de trabajo de codificación agentic, logré correr un proyecto completo y grande casi todo de forma autónoma (más de 1M de tokens procesados en total, solo 3 prompts).

Aquí va un resumen rápido de la configuración base antes de meternos en los detalles del config y del workflow.

### Specs y parámetros rápidos

* **Modelo:** `Qwen3.8-27B-UD-Q3_K_XL.gguf`
* **Hardware:** RTX 5060 Ti (16GB VRAM) + Intel N100 (4C/4T, 16GB RAM)
* **Ventana de contexto:** **73,728 (73k de contexto)** corriendo tranqui en 16GB de VRAM.
* **Cuantización de KV Cache:** `q4_1` para el contexto principal
* **Decodificación especulativa:** MTP nativa activada (`spec-type = draft-mtp`, `n-max = 2`)
* **Sampling:** `temp = 0.65`, `top_p = 0.95`, `top_k = 20`, `min_p = 0.05`

---

### El experimento: armar una API completa con 3 prompts

En vez de correr benchmarks sintéticos, metí esta configuración por una cadena real de ingeniería de software: construyendo una **REST API** no oficial y un **servidor MCP** para un foro vBulletin heredado.

1. **Prompt 1 (Arquitectura del sitio y análisis):** Pedí al modelo que mapee el sitio objetivo. Generó una especificación en Markdown impecable de ~1,500 líneas que cubría análisis estructural, nodos HTML rescatables, payloads JSON esperados, selección de stack, lógica de paginación, autenticación de sesión y endpoints de búsqueda—mucho más a fondo de lo que yo habría escrito a mano.
2. **Prompt 2 (Arquitectura de desarrollo):** Usando la spec como única fuente de verdad, diseñó un plan de implementación modular de NestJS dividido en 9 fases de ejecución:
* *Fase 1:* Estructura inicial del proyecto
* *Fase 2:* Modelos de dominio
* *Fase 3:* Scraping core (HTTP + limitación de tasa + reintentos)
* *Fase 4:* Parsers de HTML (`cheerio`)
* *Fase 5:* Capa de caché
* *Fase 6:* Servicios de aplicación + REST API
* *Fase 7:* Autenticación (sesiones con cookies)
* *Fase 8:* Servidor MCP *(entrega principal)*
* *Fase 9:* Fortalecimiento, documentación y entrega


3. **Prompt 3 (Ejecución autónoma agentic):** La prueba de verdad. Le pedí a **OpenCode** (usando Qwen 3.8 27B) que actuara estrictamente como orquestador, creando sub-agentes para cada fase de tareas. Corrió de forma autónoma por **~2 horas**. Cuando se acercaron los límites de contexto, OpenCode resumió su estado y siguió construyendo. Escribió tests unitarios, aplicó linting y entregó código 100% funcional—solo necesitando un arreglo automatizado menor cuando le di un payload de HTML crudo con un caso extremo.

---

### El archivo de configuración `llama.cpp` 

Aquí está mi archivo exacto de configuración de enrutador `--models-preset` . Fíjate cómo `fit = off` se usa en el perfil de 27B junto con `ctx-size = 73728` (73k) y `q4_1` para cuantizar la KV cache, con el objetivo de maximizar la asignación de VRAM mientras se mantiene el rendimiento nativo de MTP.

```ini
# ==============================================================================
# LLAMA.CPP — CONFIGURACIÓN DE INFERENCIA (modo router / --models-preset)
# ==============================================================================
#
# Objetivo de hardware:
#   GPU: 16 GB VRAM (RTX 5060 Ti)
#   CPU: Intel N100, 4C/4T (Debian Headless)

# ------------------------------------------------------------------------------
# GLOBAL / LÍNEA BASE
# ------------------------------------------------------------------------------
[*]

# --- HILOS DE CPU -----------------------------------------------------------
# Reserva 1 core para SO/servicios durante el decode.
# Usa los 4 threads durante ráfagas de prefill del prompt.
threads             = 3
threads-batch       = 4

# --- SERVIDOR / CONCURRENCIA ---------------------------------------------------
# Un solo slot; desactivado continuous batching para máximo rendimiento por usuario.
parallel            = 1
cont-batching       = 0

# --- GPU / AJUSTE DE VRAM ---------------------------------------------------------
flash-attn          = on
fit                 = on

# Holgura de seguridad para el límite físico de VRAM (MiB).
# Ponlo bajo (128) porque el sistema es headless (100% VRAM disponible para inferencia).
# NOTA: Si usas caches KV draft de MTP, ojo con la asignación doble de VRAM. 
# Sube a 128-256 si te topas con OOMs.
fit-target          = 128

# --- CONTEXTO & CACHÉ ------------------------------------------------------
ctx-size            = 65536
context-shift       = 1

# Desactiva checkpoints de contexto (evita problemas de reprocesamiento en arquitecturas híbridas)
ctx-checkpoints     = 0

# RAM Prompt Cache (2 GiB)
cache-ram           = 2048

# --- KV CACHE GLOBAL --------------------------------------------------------
cache-type-k        = q5_1
cache-type-v        = q5_1

# --- PREFILL / BATCHING -----------------------------------------------------
batch-size          = 2048
ubatch-size         = 1024

# --- SAMPLING POR DEFECTO (Códigos / Precisión) ----------------------------------
temp                = 0.5
top-p               = 0.95
top-k               = 20
min-p               = 0.05
repeat-penalty      = 1.0

# ------------------------------------------------------------------------------
# QWEN 3.8 27B — PERFIL DE RAZONAMIENTO & CODIFICACIÓN PESADA
# ------------------------------------------------------------------------------
[qwen3.8-27b]
model               = /opt/llama-infrastructure/models/Qwen3.8-27B-UD-Q3_K_XL.gguf

# Desactiva "fit" para evitar que capas se carguen en la CPU por un error de cálculo automático
fit                 = off
ctx-size            = 73728
context-shift       = 1

# MTP nativa del modelo (Decodificación especulativa)
spec-type           = ngram-mod,draft-mtp
spec-draft-n-max    = 2

# Cuantización de KV (q4_1 nos permite meter contexto de 73k en 16GB de VRAM)
cache-type-k        = q4_1
cache-type-v        = q4_1

# Parámetros de presupuesto de pensamiento / razonamiento
chat-template-kwargs = {"preserve_thinking": true, "reasoning_effort":"medium"}
reasoning-budget    = 5000

# Batches más chicos para evitar picos de VRAM durante prefills masivos
batch-size          = 1024
ubatch-size         = 512

# Ajustes oficiales / recomendados del sampler de cuantización
temp                = 0.65
top-p               = 0.95
top-k               = 15
min-p               = 0.05

```"
