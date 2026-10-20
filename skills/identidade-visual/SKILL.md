---
name: identidade-visual
description: Deixa o Pack de Edição IA com a cara do usuário — cores, fontes e estilo — a partir de prints do canal, thumbs, logo ou de uma descrição. Use quando o usuário pedir pra personalizar o pack, trocar cor/fonte das animações, "deixar com a minha identidade" ou quando for a primeira vez que ele usa o pack.
---

# Identidade visual do pack

Todas as 22 animações leem as cores e as fontes de UM arquivo: `assets/brand.css`.
Mudou ali, mudou em tudo. Esta skill preenche esse arquivo com a identidade do usuário.

## 1. Coletar
Peça UMA destas coisas (a que ele tiver mais fácil):
- 3 a 5 thumbs ou prints do canal/perfil, ou
- o logo, ou
- o link do canal (abra e olhe as thumbs), ou
- uma descrição ("preto, amarelo e branco, fonte bem grossa").

## 2. Extrair
Das imagens, tire:
| Variável no brand.css | O que é |
|---|---|
| `--pk-acento` | a cor de destaque mais forte da marca (a que aparece no texto destacado das thumbs) |
| `--pk-fundo` | o fundo escuro dominante |
| `--pk-verde` | mantenha verde pra resultado/dinheiro, a não ser que a marca já use outra cor pra isso |
| `--pk-fonte` | a fonte dos títulos (se for uma fonte paga ou desconhecida, sugira a gratuita mais parecida) |

Mostre a proposta numa tabela com as cores em hexadecimal e **espere o OK**.

## 3. Aplicar
1. Edite só `assets/brand.css`.
2. Fonte nova: baixe o `.woff2` (Google Fonts ou `npm i @fontsource/<nome>`), coloque em
   `assets/fonts/` e adicione o `@font-face` no topo do brand.css. Fonte que não está em arquivo
   NÃO aparece no render.
3. Renderize 3 peças de amostra pra ele ver: `01-contador-faturamento`, `08-lower-third`, `18-gancho-topo`.
4. Ajuste até ele aprovar.

## Regras
- Contraste: texto sempre legível no celular. Se o acento for claro (amarelo, verde-limão),
  texto em cima dele é preto.
- Cor com função fixa: verde = resultado, vermelho/laranja = prejuízo/alerta. Não troque isso
  pela cor da marca, ou o número bom passa a parecer ruim.
- Salve a identidade aprovada nos **Aprendizados** da skill `pack-edicao-ia`.
