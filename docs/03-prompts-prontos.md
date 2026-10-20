# 03 · Prompts prontos — a esteira completa

Uma gravação crua → vídeo editado + criativos. Cola na ordem, na aba Code, com esta pasta aberta.
O que está entre `[colchetes]` você troca.

---

## Prompt 1 · Decupagem

```
Usando a skill decupagem, decupa o vídeo [meu-video.mp4].
Ritmo de YouTube. Depois me mostra a duração antes e depois
e a lista de tomadas repetidas que você quer cortar. Não corta
conteúdo sem eu aprovar.
```

---

## Prompt 2 · Mapa de edição (você dirige aqui)

```
Usando a skill pack-edicao-ia, lê a transcrição do vídeo decupado
e me devolve o mapa de edição em tabela: tempo, o que eu falo,
qual peça do pack entra, com quais variáveis, e qual som.

Contexto do vídeo: [sobre o que é e pra quem].
Números reais que eu falo no vídeo: [ex.: R$ 25 mil de lucro na semana, ROI 3,2x].
NÃO invente nenhum número que eu não passei.

Regras de estilo:
- uma ideia por vez na tela, nada poluído
- nada de texto centralizado entrando com fade em tudo
- animação entra 0,1 s antes da palavra
- no máximo um som a cada 1,5 s

Não renderiza ainda. Só o mapa.
```

---

## Prompt 3 · Editar com excelência

```
Mapa aprovado [com estas mudanças: ...]. Agora edita com excelência
e faz refinamento:

1. Monta tudo no index.html seguindo o mapa.
2. Roda o check e corrige todo erro.
3. Tira snapshot de cada cena e dá nota de 1 a 10 em: sincronia com
   a fala, legibilidade no celular, poluição visual e ritmo.
4. Escreve os 3 piores problemas, corrige e repete até tudo ficar 8 ou mais.
5. Só então renderiza e me entrega.
```

---

## Prompt 4 · Criativos

```
Usando a skill criativo-vertical, acha os 3 melhores trechos desse
vídeo pra virar criativo de anúncio (15 a 45 s cada). Me mostra a
lista antes de cortar. Pra cada um, faz 2 variações de gancho.
```

---

## Prompt 5 · Aprender

```
Salva na skill pack-edicao-ia, na seção Aprendizados, tudo que eu
corrigi nessa edição, pra na próxima você já entregar no meu padrão.
Me mostra o que você adicionou.
```

---

## Dicas que fazem diferença

- **Use o modelo mais forte que o seu plano tiver** pra edição (Opus). Pra decupagem, um modelo
  mais rápido já resolve.
- **"Edita com excelência e faz refinamento"** no pedido melhora o resultado de verdade.
- **Proibir o padrão funciona melhor do que pedir "bonito".** Diga o que você NÃO quer.
- **Deixe notas pra edição na própria gravação:** fale "abre nota, aqui quero o contador indo até
  25 mil, fecha nota". Na decupagem o Claude corta a nota e usa o pedido na edição.
- **Referência de ritmo, não de design:** mande um vídeo que você gosta e peça pra analisar a
  velocidade dos cortes e a energia. Copiar o design deixa seu vídeo igual ao dos outros.

➡️ Próximo: [04 · Problemas comuns](04-problemas-comuns.md)
