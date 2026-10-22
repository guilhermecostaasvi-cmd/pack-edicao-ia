# 07 · Biblioteca de estilos: 10 jeitos de fazer vídeo com o Claude

Cada estilo tem uma **prévia pronta** no catálogo oficial do HyperFrames (abra o link e veja a animação) e um **prompt pronto** pra colar na aba Code, com a pasta do pack aberta.
Troque o que está entre `[colchetes]`. Os números são sempre os seus, reais.

| # | Estilo | Tipo | Prévia pronta |
|---|---|---|---|
| 1 | Produto 3D girando | 3D | [product-turntable](https://hyperframes.heygen.com/catalog/blocks/product-turntable) |
| 2 | Funil em camadas 3D | 3D | [exploded-stack](https://hyperframes.heygen.com/catalog/blocks/exploded-stack) |
| 3 | Título 3D cromado ou dourado | 3D | [extruded-logo](https://hyperframes.heygen.com/catalog/blocks/extruded-logo) |
| 4 | Objeto de vidro na frente do título | 3D | [glass-hero](https://hyperframes.heygen.com/catalog/blocks/glass-hero) |
| 5 | iPhone e MacBook 3D com a sua tela | 3D | [vfx-iphone-device](https://hyperframes.heygen.com/catalog/blocks/vfx-iphone-device) |
| 6 | Gráfico estilo jornal | Dados | [data-chart](https://hyperframes.heygen.com/catalog/blocks/data-chart) |
| 7 | Mapa-múndi animado | Dados | [world-map](https://hyperframes.heygen.com/catalog/blocks/world-map) |
| 8 | Diagrama desenhado à mão | 2D | [hw-pipeline](https://hyperframes.heygen.com/catalog/blocks/hw-pipeline) |
| 9 | IA operando a tela | 2D | [agent-cursor](https://hyperframes.heygen.com/catalog/components/agent-cursor) |
| 10 | Palavra que trava e vira manchete | Tipografia | [ticker-takeover](https://hyperframes.heygen.com/catalog/components/ticker-takeover) |

Também tem o **3D explicativo** do próprio pack (animação 23, o coração cortado): veja [06 · Animações 3D](06-animacoes-3d.md).

## 1 · Produto 3D girando

**Pra quê:** Mostrar o produto (ou a capa do infoproduto) girando num pedestal de estúdio.  
**Prévia pronta:** https://hyperframes.heygen.com/catalog/blocks/product-turntable

```
Instala o bloco product-turntable do catálogo do HyperFrames (npx hyperframes add product-turntable).
Adapta pra mostrar o meu produto: [nome do produto], com a frase "[benefício em 4 palavras]" no rótulo e a legenda "[preço ou chamada]".
Cor do rótulo: [cor da marca]. Se eu tiver um modelo 3D (.glb), usa ele: [caminho do arquivo].
Me mostra um snapshot antes de renderizar.
```

## 2 · Funil em camadas 3D

**Pra quê:** Explicar um processo em etapas: as camadas se separam com uma etiqueta em cada uma.  
**Prévia pronta:** https://hyperframes.heygen.com/catalog/blocks/exploded-stack

```
Instala o bloco exploded-stack (npx hyperframes add exploded-stack).
Transforma num funil de vendas com 4 camadas, de cima pra baixo: [Anúncio], [Página], [Checkout], [Upsell].
Título: "[como uma venda acontece]". Cor de destaque: [cor da marca], fundo escuro.
Tudo em português. Me mostra um snapshot antes de renderizar.
```

## 3 · Título 3D cromado ou dourado

**Pra quê:** Abertura de vídeo ou revelação de nome: letras 3D com brilho passando.  
**Prévia pronta:** https://hyperframes.heygen.com/catalog/blocks/extruded-logo

```
Instala o bloco extruded-logo (npx hyperframes add extruded-logo).
Texto em 3D: "[PALAVRA, até 8 letras, sem acento]". Frase de baixo: "[subtítulo]".
Acabamento: [dourado ou cromado]. Fundo: [cor].
Me mostra um snapshot antes de renderizar.
```

## 4 · Objeto de vidro na frente do título

**Pra quê:** Tela de capítulo com cara de comercial: um objeto de vidro gira e distorce a frase atrás.  
**Prévia pronta:** https://hyperframes.heygen.com/catalog/blocks/glass-hero

```
Instala o bloco glass-hero (npx hyperframes add glass-hero).
Frase atrás do vidro: "[frase curta de impacto]". Cores da marca do assets/brand.css.
Me mostra um snapshot antes de renderizar.
```

## 5 · iPhone e MacBook 3D com a sua tela

**Pra quê:** Mostrar página de vendas, app ou painel dentro de um celular/notebook 3D girando.  
**Prévia pronta:** https://hyperframes.heygen.com/catalog/blocks/vfx-iphone-device

```
Instala o bloco vfx-iphone-device (npx hyperframes add vfx-iphone-device).
Coloca na tela do iPhone o print [print-da-pagina.png] e na tela do MacBook o print [print-do-painel.png].
Mantém o movimento de câmera de review de produto. Me mostra um snapshot antes de renderizar.
```

## 6 · Gráfico estilo jornal

**Pra quê:** Mostrar resultado com número de verdade: barras + linha entrando em sequência.  
**Prévia pronta:** https://hyperframes.heygen.com/catalog/blocks/data-chart

```
Instala o bloco data-chart (npx hyperframes add data-chart).
Troca os dados pelos meus: meses [jan a jun], faturamento em R$ [valores reais], conversão em % [valores reais].
Título: "[título]". Tudo em português, R$ e vírgula decimal. NÃO invente nenhum número.
Me mostra um snapshot antes de renderizar.
```

## 7 · Mapa-múndi animado

**Pra quê:** Vender na gringa: mostrar os países onde você vende ou onde está o público.  
**Prévia pronta:** https://hyperframes.heygen.com/catalog/blocks/world-map

```
Instala o bloco world-map (npx hyperframes add world-map).
Troca os dados pelos países onde eu vendo: [lista de países e números reais].
Título: "[título]". Legenda e textos em português. NÃO invente nenhum número.
Me mostra um snapshot antes de renderizar.
```

## 8 · Diagrama desenhado à mão

**Pra quê:** Explicar um método em 3 a 5 passos com caixas e setas que se desenham sozinhas.  
**Prévia pronta:** https://hyperframes.heygen.com/catalog/blocks/hw-pipeline

```
Instala o bloco hw-pipeline (npx hyperframes add hw-pipeline).
Os passos são: [passo 1], [passo 2], [passo 3]. Fundo transparente, pra eu colocar por cima do meu vídeo.
Me mostra um snapshot antes de renderizar.
```

## 9 · IA operando a tela

**Pra quê:** Demonstrar automação: um cursor com o nome da IA clica e narra cada passo em cima do seu print.  
**Prévia pronta:** https://hyperframes.heygen.com/catalog/components/agent-cursor

```
Instala o componente agent-cursor (npx hyperframes add agent-cursor).
Monta uma cena com o print [print.png] de fundo e o cursor "Claude" fazendo estes passos: [passo 1], [passo 2], [passo 3], [resultado].
Clica nos lugares certos do print (me mostra onde antes). Me mostra um snapshot antes de renderizar.
```

## 10 · Palavra que trava e vira manchete

**Pra quê:** Gancho de abertura: palavras rolando como caça-níquel até travar na palavra-chave do vídeo.  
**Prévia pronta:** https://hyperframes.heygen.com/catalog/components/ticker-takeover

```
Instala o componente ticker-takeover (npx hyperframes add ticker-takeover).
Palavras que rolam: [criativo, oferta, página, público]. Palavra final: "[escala]".
Cor de destaque: [cor da marca]. Me mostra um snapshot antes de renderizar.
```

---

> Dica: antes de renderizar qualquer estilo 3D, peça sempre o snapshot. Render 3D é lento em computador sem placa de vídeo boa.

➡️ Voltar pro [README](../README.md)
