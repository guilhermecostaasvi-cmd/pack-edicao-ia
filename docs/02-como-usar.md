# 02 · Como usar — 3 jeitos

Escolha pelo que você quer agora.

| Jeito | Precisa instalar? | Você consegue |
|---|---|---|
| **A · Arrastar pro seu editor** | nada | usar as animações como estão |
| **B · Pedir uma animação** | [instalação](01-instalacao.md) | qualquer animação com o seu texto, valor e cor |
| **C · Editar o vídeo inteiro** | instalação + skills | o Claude edita o vídeo do começo ao fim |

---

## A · Arrastar pro seu editor (CapCut, Premiere, DaVinci)

1. Abra a pasta `renders/`.
2. Os arquivos **`.webm`** têm **fundo transparente**: arraste por cima do seu vídeo.
3. As transições (15, 16, 17): coloque o **meio** da transição exatamente em cima do corte.

> ⚠️ O texto e o valor ficam os de exemplo ("Venda aprovada R$ 97,00"). Pra mudar, use o jeito B.
> No Premiere, se o `.webm` não abrir, peça no jeito B a versão `--format mov`.

---

## B · Pedir uma animação com o seu texto

Abra **esta pasta** na aba Code do Claude e peça em português. Exemplos:

> Usa o pack e me gera a notificação de venda com **R$ 47,00**, detalhe "Pix · Mentoria", em vídeo transparente.

> Gera o contador de faturamento indo até **R$ 25.000**, legenda "lucro da semana".

> Me faz o checklist "Os 4 filtros do radar" com os itens: Dias no ar, Anúncios ativos, Tipo de entregável, Ticket.

> Faz o selo de oferta de **R$ 197** por **R$ 47** em vertical, transparente.

O Claude troca as variáveis, renderiza e te entrega o arquivo em `renders/`.

**Por baixo dos panos** (se quiser rodar você mesmo):

```
npx hyperframes render -c compositions/02-notificacao-venda.html --format webm --variables "{\"valor\":\"R$ 47,00\"}"
```

---

## C · Editar o vídeo inteiro

1. Coloque o vídeo cru dentro desta pasta.
2. Peça:

> Usando a skill **decupagem**, decupa o `meu-video.mp4`.

> Agora, usando a skill **pack-edicao-ia**, edita o vídeo decupado. Antes de renderizar, me mostra o **mapa de edição**.

3. O Claude devolve uma tabela: em que segundo entra cada animação, com que texto, com que som.
   **É aqui que você dirige.** Corrija o que quiser antes de deixar ele renderizar.
4. Recebeu o vídeo, achou algo errado? Fala do jeito que falaria pra um editor:
   > O logo entrou meio segundo atrasado. Tira o círculo do minuto 2. Legenda menor.
5. No fim, sempre:
   > Salva o que você aprendeu nessa edição na skill.

Da segunda edição em diante, ele já começa no seu padrão.

### Pra criativo de anúncio

> Usando a skill **criativo-vertical**, transforma esse vídeo em 3 criativos de 30 segundos com 2 ganchos diferentes cada.

### Primeira vez? Faça isso antes

> Usando a skill **identidade-visual**, deixa o pack com a minha cara. Aqui estão 3 thumbs do meu canal.

Senão o seu vídeo fica igual ao de todo mundo que baixou o pack.

➡️ Próximo: [03 · Prompts prontos](03-prompts-prontos.md)
