# NOTICE

Este pack contém trabalhos derivados de blocos e componentes do registro do **HyperFrames**
(https://github.com/heygen-com/hyperframes), © HeyGen, distribuídos sob a
**Apache License, Version 2.0** (https://www.apache.org/licenses/LICENSE-2.0).

Os arquivos em `compositions/` foram reescritos e adaptados (textos em português, valores em R$,
identidade visual própria, sons). O cabeçalho de cada arquivo indica o bloco de origem:

| Arquivo | Origem no catálogo HyperFrames |
|---|---|
| 01-contador-faturamento | apple-money-count |
| 02-notificacao-venda | native-notification-pop |
| 03-cascata-vendas | notification-cascade |
| 04-roi-destaque | mk-progress-stat |
| 05-grafico-crescimento | mk-line-graph |
| 06-circulo-destaque | hw-callout-circle, hw-arrow |
| 07-zoom-no-print | ui-focus-zoom, yt-feather-highlight |
| 08-lower-third | lt-color-block, lt-bold-block |
| 09-inscreva-se | yt-lower-third, press-ripple |
| 10-palavra-destaque | mk-callout-highlight, marker-highlight |
| 11-legenda-karaoke | caption-highlight, caption-pill-karaoke |
| 12-titulo-capitulo | titlecard-lockup, line-swap |
| 13-headline-impacto | headline-slam, beat-accent |
| 14-checklist | mk-specs-list, marker-checklist-card, success-check |
| 15-transicao-flash | flash-through-white, editorial-flash-overlay |
| 16-transicao-cortina | directional-wipe, chromatic-aberration-wipe |
| 17-transicao-glitch | glitch, rgb-glitch-text, scan-band |
| 18-gancho-topo | headline-slam, spring-pop, outline-draw |
| 19-barra-progresso | separator, conic-progress-ring |
| 20-selo-oferta | strikethrough-replace, spring-pop, number-wheel |
| 21-antes-depois | comparison-split, before-after-wipe |
| 22-me-chama-na-dm | instagram-follow, message-thread-reveal |
| 23-explicativo-3d | product-turntable (estrutura de render seek-safe com three.js) |

Outros componentes de terceiros:
- `assets/vendor/gsap.min.js` — GSAP 3.14.2, GreenSock/Webflow, licença padrão "no charge" (https://gsap.com/standard-license).
- `assets/vendor/three/three-pack.min.js` — three.js r184 (MIT, © three.js authors) com GLTFLoader e RoomEnvironment, empacotados num arquivo só. Licença em `assets/vendor/three/LICENSE`.
- `assets/modelos/coracao.glb` — derivado do Z-Anatomy (https://github.com/Z-Anatomy/Models-of-human-anatomy), © Z-Anatomy, que por sua vez deriva do BodyParts3D © The Database Center for Life Science (CC BY-SA 2.1 Japão); **CC BY-SA 4.0** (https://creativecommons.org/licenses/by-sa/4.0/). Alterações: só as peças do coração e grandes vasos, convertidas de .blend para .glb, sem materiais. Este arquivo derivado segue sob a mesma licença CC BY-SA 4.0. Veja `assets/modelos/LICENCA-MODELOS.md`.
- `assets/fonts/` — Poppins e JetBrains Mono (SIL OFL 1.1, arquivos de licença inclusos); Caveat (SIL OFL 1.1).

Os efeitos sonoros em `assets/sfx/` são sintetizados pelo script `gerar_sons.py` incluso e não
contêm gravações de terceiros.

## Extras de terceiros (`extras/`)

Cópias sem modificação, sob a licença MIT de cada autor (o `LICENSE` original está em cada pasta):

| Pasta | Origem | Versão (commit) |
|---|---|---|
| extras/cut-video | github.com/louisedesadeleer/cut-video — © 2026 Louise de Sadeleer | a5a87a6 |
| extras/clipify | github.com/louisedesadeleer/clipify — © 2026 Louise de Sadeleer | 5f6b75e |
| extras/add-zooms | github.com/louisedesadeleer/add-zooms — © 2026 Louise de Sadeleer | 34db910 |
| extras/freecut | github.com/Moh4696/freecut — © 2026 Browser Use | f1d4334 |
| extras/motion-graphics | github.com/Barty-Bart/motion-graphics (pasta skills/) — © 2026 Bart | 3d83d98 |
| extras/threejs-skills | github.com/cloudai-x/threejs-skills — © 2026 CloudAI-X | 0e18186 |
