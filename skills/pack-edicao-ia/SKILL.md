---
name: pack-edicao-ia
description: Edita vídeo de YouTube, criativo (vertical) e VSL com HyperFrames usando o Pack de Edição IA — 27 animações prontas em pt-BR (uma em 3D) (prova de resultado, texto, transições, criativo) e 34 efeitos sonoros gerados por código. Use quando o usuário pedir pra editar um vídeo, colocar animações, motion, legenda, transição ou efeito sonoro num vídeo, ou montar criativo com o pack.
---

# Pack de Edição IA

Você é o editor. O usuário é o diretor. Ele fala o que quer; você monta a edição em HyperFrames
usando as peças deste pack e só inventa animação nova quando nenhuma peça serve.

A pasta do pack tem esta estrutura (`PACK` = onde ela está):

```
PACK/
  compositions/   27 animações (.html), cada uma com variáveis
  assets/sfx/     38 efeitos sonoros (.wav) + gerar_sons.py
  assets/brand.css  cores e fontes de TODAS as animações (mude aqui a identidade)
  assets/fonts/  assets/vendor/gsap.min.js
  index.html  exemplos/reel-vertical.html   exemplos de montagem (horizontal e 9:16)
  renders/       prévias em MP4 e overlays em WebM com transparência
```

---

## O fluxo — sempre nesta ordem

### 1. Preparar o projeto
- Se o vídeo do usuário ainda não está num projeto HyperFrames: `npx hyperframes init meu-video --video caminho/do/video.mp4`
  (isso já transcreve com whisper e gera `transcript.json` com o tempo de cada palavra).
- Copie `PACK/compositions` e `PACK/assets` pra dentro do projeto (mantendo os nomes das pastas).
- Se o vídeo tem muita pausa e erro, decupe antes (cortar silêncio > 0,1 s, tomadas repetidas e
  falas de instrução tipo "abre nota / fecha nota"). Mostre a duração antes × depois.

### 2. Transcrever com atenção
É a transcrição que sincroniza tudo. Animação entrando fora do tempo = transcrição ruim → refaça.
Use os tempos de palavra do `transcript.json`, nunca chute tempo.

### 3. Mapa de edição — ANTES de renderizar
Leia a transcrição e devolva ao usuário uma tabela, cena a cena:

| Tempo | O que ele fala | Peça do pack | Variáveis | Som |
|---|---|---|---|---|

Só renderize depois que ele aprovar ou corrigir o mapa. É aqui que ele dirige.

### 4. Montar
Cada peça entra no `index.html` assim:

```html
<div class="clip" id="venda-1" data-composition-id="02-notificacao-venda"
     data-composition-src="compositions/02-notificacao-venda.html"
     data-start="12.40" data-duration="4" data-width="1920" data-height="1080" data-track-index="2"
     data-variable-values='{"valor":"R$ 47,00","detalhe":"Pix · Guia Completo"}'></div>
```

- **`data-composition-id` = exatamente o nome do arquivo sem `.html`.** Se for diferente, a peça
  some no render (sem erro nenhum). Usando a mesma peça 2 vezes, repita o mesmo `data-composition-id`
  — o HyperFrames numera sozinho. O que muda entre os usos é o `id` (ex.: `venda-1`, `venda-2`).
- `data-start` = tempo da palavra no transcript (a animação começa 0,1 s ANTES da palavra).
- `data-duration` = a duração da peça (tabela abaixo). Encurtar corta o final dela.
- Vídeo do usuário no track 0, peças de tela cheia no 1, overlays no 2, transições no 3.
- Formato: peça 1920×1080 em vídeo horizontal, peça 1080×1920 em criativo vertical. Não misture.

### 5. Autocrítica antes de entregar
1. `npx hyperframes check` e corrija todo erro.
2. `npx hyperframes snapshot` nos momentos de cada peça e olhe as imagens.
3. Dê nota de 1 a 10 pra cada cena em: sincronia com a fala, legibilidade no celular, poluição visual, ritmo.
4. Escreva os 3 piores problemas, corrija, repita até tudo ≥ 8.
5. Renderize (`npx hyperframes render`) e entregue com 1 linha do que mudou.

### 6. Aprender
Toda correção que o usuário fizer ("o logo entrou atrasado", "menos texto", "essa cor não") vira
uma linha na seção **Aprendizados** no fim deste arquivo. Na próxima edição você já começa por ela.
No fim de cada edição pergunte: "Quer que eu salve o que aprendi nessa edição na skill?"

---

## As 27 peças

**Prova de resultado** (é o que mais segura quem roda tráfego)

| Arquivo | Formato | Duração | Quando usar | Variáveis principais |
|---|---|---|---|---|
| `01-contador-faturamento` | 16:9 tela cheia | 5 s | ele fala um valor ganho | `valor`, `prefixo`, `legenda`, `centavos` |
| `02-notificacao-venda` | 16:9 overlay | 4 s | "vendeu", "caiu venda", prova de venda | `titulo`, `valor`, `detalhe`, `app`, `lado` |
| `03-cascata-vendas` | 9:16 tela cheia | 6 s | abertura de criativo, "acordei com isso" | `valor_venda`, `produto`, `rotulo_total` |
| `04-roi-destaque` | 16:9 tela cheia | 4,5 s | investido × retorno, ROI | `investido`, `retorno`, `rotulo`, `titulo` |
| `05-grafico-crescimento` | 16:9 tela cheia | 6 s | evolução por dia/semana | `titulo`, `valores` (1,2,3), `rotulos` |
| `06-circulo-destaque` | 16:9 overlay | 3,5 s | apontar um número num print | `x`, `y`, `largura`, `altura`, `texto`, `cor` |
| `07-zoom-no-print` | 16:9 tela cheia | 5 s | mostrar print de gerenciador/dashboard | `imagem`, `foco_x`, `foco_y`, `zoom` |

**Texto**

| Arquivo | Formato | Duração | Quando usar | Variáveis principais |
|---|---|---|---|---|
| `08-lower-third` | 16:9 overlay | 5 s | primeira vez que ele aparece | `nome`, `arroba`, `etiqueta`, `cor` |
| `09-inscreva-se` | 16:9 overlay | 5 s | pedido de inscrição/sininho | `canal`, `inscritos`, `foto` |
| `10-palavra-destaque` | 16:9 overlay | 4 s | frase-tese, frase de virada | `frase`, `destaque`, `posicao` |
| `11-legenda-karaoke` | 16:9 overlay | 5 s (ajuste) | legenda palavra por palavra | `texto`, `palavras_por_tela`, `velocidade` |
| `12-titulo-capitulo` | 16:9 tela cheia | 3,5 s | começo de cada etapa/bloco | `numero`, `titulo`, `subtitulo` |
| `13-headline-impacto` | 16:9 overlay | 2,8 s | frase curta de impacto | `linha1`, `linha2`, `escurecer` |
| `14-checklist` | 16:9 tela cheia | 5,5 s | método nomeado ("os 4 filtros") | `titulo`, `itens` (separados por \|) |

**Transição** (overlay transparente — coloque o MEIO em cima do corte)

| Arquivo | Duração | Meio (cobre a tela) | Quando usar |
|---|---|---|---|
| `15-transicao-flash` | 0,9 s | 0,40 s | virada de assunto, revelação |
| `16-transicao-cortina` | 0,95 s | 0,45 s | troca de etapa/bloco (`cor1`, `direcao`) |
| `17-transicao-glitch` | 0,7 s | 0,30 s | erro, "deu ruim", antes × depois |
| `27-transicao-obturador` | 0,95 s | 0,40–0,46 s (preto total) | "foto", print, prova, flash de câmera (`laminas`, `flash`) |

Ex.: corte em 20,00 s com cortina → `data-start="19.55"`.

**Criativo vertical 9:16**

| Arquivo | Formato | Duração | Quando usar | Variáveis principais |
|---|---|---|---|---|
| `18-gancho-topo` | overlay | 4 s | os 3 primeiros segundos | `texto`, `destaque`, `duracao_tela` |
| `19-barra-progresso` | overlay | o vídeo todo | retenção em reels/criativo | `duracao` (igual ao data-duration), `cor` |
| `20-selo-oferta` | overlay | 4,5 s | preço de/por | `preco_de`, `preco_por`, `chamada`, `rodape` |
| `21-antes-depois` | tela cheia | 5 s | comparação com divisória | `numero_antes/depois`, `imagem_antes/depois` |
| `22-me-chama-na-dm` | overlay | 5 s | CTA de palavra-chave na DM | `arroba`, `palavra`, `chamada` |
**Efeitos especiais 16:9**

| Arquivo | Formato | Duração | Quando usar | Variáveis principais |
|---|---|---|---|---|
| `24-vidro-liquido` | overlay | 5 s | notificação estilo iOS 26: resultado, venda, mensagem. Montada no HyperFrames, desfoca o vídeo de trás de verdade | `app`, `titulo`, `texto`, `icone`, `posicao`, `tema` |
| `25-particulas` | overlay | 4,6 s | número grande ou virada que se monta com partículas | `texto` (até ~14 letras), `subtexto`, `cor`, `saida` |
| `26-jornal` | overlay | 4 s | manchete de jornal girando: prova social, resultado de aluno, notícia | `jornal`, `data`, `manchete`, `linha_fina`, `imagem` |
| `23-explicativo-3d` | tela cheia | 14 s | modelo 3D gira, é cortado e etiqueta as regiões (veja a skill `explicativo-3d`) | `modelo`, `regioes`, `titulo`, `eixo_corte` |

---

## Os 38 sons (`assets/sfx/`, todos nivelados no mesmo volume)

| Grupo | Arquivos | Use em |
|---|---|---|
| Whoosh | `whoosh-curto` `whoosh-longo` `whoosh-grave` `swoosh-agudo` `whoosh-saida` | elemento entrando/saindo, troca de cena |
| Impacto | `impacto-grave` `impacto-seco` `hit-cinematico` `batida-tambor` `slam-texto` | número/frase que bate na tela |
| Riser | `riser-2s` `riser-4s` `reverso-swell` | tensão antes de revelar um número (termina no hit) |
| Pop/clique | `pop` `pop-bolha` `clique-mouse` `tecla` `tick` `digitando` | ícone aparecendo, clique, digitação |
| Venda | `cha-ching` `moeda` `notificacao-venda` `sucesso` `vendas-em-sequencia` | prova de venda, resultado |
| Glitch | `glitch-digital` `estatica` `stutter` `erro-buzz` | erro, prejuízo, "antes" |
| UI | `swipe` `toggle` `zoom-in` `zoom-out` `flash-brilho` `check` | interface, zoom, item marcado |
| Especiais | `obturador` `papel-giro` `brilho-particulas` `vidro-tilin` | câmera/foto, jornal girando, partículas, vidro |

Som avulso no `index.html`:
`<audio data-start="31.2" data-duration="0.55" src="assets/sfx/whoosh-curto.wav" data-volume="0.5"></audio>`

- `data-duration` = duração real do arquivo (no máximo).
- Sons de efeito entre 0,3 e 0,7 de volume. A voz do usuário é sempre a coisa mais alta.
- No máximo 1 som a cada 1,5 s fora de montagem rápida. Som em tudo cansa.

---

## Regras que nunca quebram

1. **Nenhum número inventado.** Valor, ROI, vendas: só o que o usuário disse ou o que está no print dele.
   Os valores padrão das peças são exemplo — troque sempre. Preço "de" do selo tem que ser real.
2. **Proibido o visual padrão de IA:** texto centralizado entrando com fade em tudo, fonte do sistema,
   gradiente roxo, emoji decorativo, tela poluída. Uma ideia por vez na tela.
3. **Identidade:** cores e fontes vêm de `assets/brand.css`. Pra mudar o visual, mude lá, não peça por peça.
4. **Seek-safe:** nada de `Math.random()`, `Date.now()`, `tl.call()` ou `<audio>` criado por JavaScript —
   o render pula de quadro em quadro e isso quebra. Use `tl.set()` e `<audio>` escrito no HTML,
   sempre com `id` (áudio sem `id` pode sair mudo).
5. **Zona segura no vertical:** nada importante nos 220 px de cima nem nos 380 px de baixo (interface do app).
6. **Overlay pra outro editor:** se o usuário edita no CapCut/Premiere, renderize a peça sozinha com
   `npx hyperframes render -c compositions/<peça>.html --format webm` (transparente) ou `--format mov`.

---

## Aprendizados

<!-- O Claude adiciona aqui, uma linha por correção do usuário, com a data. Ex.:
- 2026-10-21 · logo/elemento entra 0,1 s antes da palavra, não junto
- 2026-10-21 · legenda karaokê: máximo 3 palavras por tela no vertical
-->
