# 🧰 Extras — skills de outros criadores

Skills open source de vídeo pro Claude, de outros autores, que combinam com o Pack.
Copiadas aqui com a licença original (todas **MIT**), pra você baixar tudo num lugar só.
**O crédito é de quem criou** — cada pasta mantém o `LICENSE` e o `README` original.

| Pasta | O que faz | Autor · original | Funciona em |
|---|---|---|---|
| [`cut-video`](cut-video) | Decupagem pesada: corta silêncio, "é…", "tipo", começo errado e repetição, com corte na fronteira exata da palavra | Louise de Sadeleer · [louisedesadeleer/cut-video](https://github.com/louisedesadeleer/cut-video) | feito pro Mac. No Windows, peça pro Claude tirar o `-hwaccel videotoolbox` dos comandos |
| [`clipify`](clipify) | Acha os melhores momentos de um vídeo longo, corta, passa pra 9:16 e coloca legenda palavra por palavra | Louise de Sadeleer · [louisedesadeleer/clipify](https://github.com/louisedesadeleer/clipify) | idem |
| [`add-zooms`](add-zooms) | Coloca zoom de impacto nas palavras fortes e "Ken Burns" nas frases importantes de um vídeo falado | Louise de Sadeleer · [louisedesadeleer/add-zooms](https://github.com/louisedesadeleer/add-zooms) | idem |
| [`freecut`](freecut) | Edita o vídeo inteiro conversando: transcreve, corta, faz color grade, legenda e se autoavalia em cada corte. Sem nenhuma chave paga | Moh4696 (fork do video-use da Browser Use) · [Moh4696/freecut](https://github.com/Moh4696/freecut) | Mac, Windows, Linux |
| [`motion-graphics`](motion-graphics) | 6 skills: b-roll animado sincronizado com a fala, separar pessoa do fundo, explainers, efeitos sonoros no ritmo | Bart · [Barty-Bart/motion-graphics](https://github.com/Barty-Bart/motion-graphics) | Mac, Windows, Linux |

## Como instalar uma delas

Copie a pasta pra pasta de skills do Claude (`C:\Users\SEU_USUARIO\.claude\skills\` no Windows,
`~/.claude/skills/` no Mac) e reinicie o Claude. No `motion-graphics`, copie as pastas de dentro
de `motion-graphics/skills/`.

Ou peça na aba Code, com este repositório aberto:

> Instala a skill `extras/clipify` pra mim e adapta os comandos pro Windows se precisar.

Leia o `README.md` de cada uma: algumas instalam dependências (Whisper, Montreal Forced Aligner)
na primeira vez.

## Qual usar com o Pack

| Você quer | Use |
|---|---|
| Decupar rápido, sem instalar nada a mais | `skills/decupagem` (do Pack) |
| Decupagem mais fina, cortando "é…" e muleta | `extras/cut-video` |
| Edição completa com autocorreção | `extras/freecut` + animações do Pack |
| Cortes pra reels a partir de vídeo longo | `extras/clipify` ou `skills/criativo-vertical` |
| Mais energia em vídeo de cabeça falante | `extras/add-zooms` |

> Versões copiadas em 20/10/2026. Pra pegar atualizações, use o link original de cada uma.
