---
name: criativo-vertical
description: Transforma uma gravação (vídeo de YouTube, live, aula ou UGC) em vários criativos verticais 9:16 pra anúncio e reels, com gancho no topo, legenda palavra por palavra, barra de progresso e CTA. Use quando o usuário pedir criativos, variações de gancho, cortes pra reels/anúncio ou "transformar esse vídeo em criativo".
---

# Criativo vertical

Uma gravação vira munição pra teste. Esta skill usa as peças 18 a 22 e a 11 do Pack de Edição IA
(veja a skill `pack-edicao-ia` pra lista completa e o jeito de montar).

## O fluxo

### 1. Achar os ganchos
Leia a transcrição inteira e marque de **3 a 5 trechos de 15 a 45 s** que funcionam sozinhos.
Um bom trecho:
- Começa com uma frase que para a rolagem: número, contradição, "ninguém te conta", dor direta.
- Tem começo, meio e fim sem depender do resto do vídeo.
- Termina numa conclusão ou numa promessa.

Mostre a lista ao usuário (tempo, primeira frase, por que é gancho) e espere ele escolher.

### 2. Recortar e verticalizar
- Corte cada trecho com FFmpeg.
- Vídeo horizontal → vertical: rosto no centro (crop 9:16 centrado no rosto) ou, se tiver tela
  importante, o vídeo em cima e o fundo desfocado embaixo.
- Rode a skill `decupagem` com `--pausa 0.2` (ritmo de criativo é mais rápido que o de YouTube).

### 3. Montar cada criativo (1080×1920)
| Camada | Peça do pack | Quando |
|---|---|---|
| Gancho no topo | `18-gancho-topo` | 0 a ~3,5 s. Texto = a frase que para a rolagem, curta |
| Legenda | `11-legenda-karaoke` | o vídeo todo, com os tempos da transcrição, 2 a 3 palavras por tela |
| Barra de progresso | `19-barra-progresso` | o vídeo todo (`duracao` = duração do criativo) |
| Prova | `02`, `03`, `21` | só se o usuário tiver o número/print real |
| Oferta | `20-selo-oferta` | só com preço real |
| CTA | `22-me-chama-na-dm` | últimos 4 a 5 s |

### 4. Variações de gancho
Pro MESMO corpo, gere 2 ou 3 versões trocando só o texto do `18-gancho-topo` e o primeiro
segundo. É assim que se testa gancho sem gravar de novo. Nomeie os arquivos:
`criativo-01-gancho-A.mp4`, `criativo-01-gancho-B.mp4`…

## Regras de criativo
- Zona segura: nada importante nos 220 px de cima nem nos 380 px de baixo.
- Os 2 primeiros segundos decidem tudo: algo tem que se mexer na tela já no quadro 1.
- Legenda sempre ligada: a maioria assiste sem som.
- **Nenhuma promessa ou número que o usuário não informou.** Anúncio com promessa falsa
  derruba a conta e é propaganda enganosa.
- Entregue uma tabela final: arquivo · gancho usado · duração.
