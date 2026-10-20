---
name: decupagem
description: Decupa vídeo falado cru — corta silêncios, respirações, tomadas repetidas e erros — antes da edição. Use quando o usuário pedir pra decupar, cortar pausas, tirar silêncio, limpar a gravação ou "deixar o vídeo picotado/corrido".
---

# Decupagem

Primeira etapa de qualquer edição. Entra o vídeo cru, sai o vídeo só com a fala boa.
Não precisa de nenhuma API: só FFmpeg e Python.

## Passo 1 — cortar os silêncios (automático)

Rode o script desta pasta:

```
python cortar_silencios.py "caminho/do/video.mp4"
```

| Situação | Ajuste |
|---|---|
| Vídeo de YouTube | padrão (`--pausa 0.35`) |
| Criativo / reels (ritmo rápido) | `--pausa 0.2 --respiro 0.05` |
| Sala com barulho (ar-condicionado, rua) | `--limite -30` |
| Cortou a primeira sílaba das frases | aumente `--respiro` pra `0.12` |

Mostre ao usuário: duração antes × depois e quantos trechos ficaram.

## Passo 2 — tirar tomadas repetidas e erros (com a transcrição)

1. Transcreva o vídeo decupado palavra por palavra, com o tempo de cada palavra
   (`npx hyperframes transcribe` ou o whisper que estiver instalado).
2. Procure:
   - **Frase repetida:** o usuário errou e falou de novo. Fica a ÚLTIMA versão completa.
   - **Frase abandonada:** começou e parou no meio ("então o… não, pera").
   - **Instrução pra edição:** "corta isso", "abre nota… fecha nota", "de novo". Corta, mas
     guarde o que estava dentro da nota: é pedido de animação pra etapa de edição.
3. Mostre a lista do que vai cortar (tempo + texto) e **espere o OK** antes de cortar.
   Corte de conteúdo é decisão do usuário, não sua.
4. Corte com FFmpeg (trim/atrim + concat, 30 ms de fade no áudio em cada corte).

## Regras

- Nunca corte o meio de uma palavra. Sempre corte no silêncio entre palavras.
- O arquivo original não é tocado. A saída é `<nome>_decupado.mp4`.
- Se a transcrição tiver trecho incompreensível, pergunte em vez de chutar.
- No fim: "Quer que eu já passe pra edição com o pack?"
