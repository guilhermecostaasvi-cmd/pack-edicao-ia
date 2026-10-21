# 06 · Animações 3D explicativas

"Claude, faz uma animação de um coração, parte no meio e mostra as regiões."
Dá pra fazer, de graça, com o que já vem no pack.

<p align="center"><img src="img/preview-3d.gif" width="640" alt="Coração 3D cortado com as regiões etiquetadas" /></p>

## O que vem pronto

| O quê | Onde |
|---|---|
| Template 3D: gira, corta no meio e etiqueta cada região | `compositions/23-explicativo-3d.html` |
| Coração com as 4 câmaras, válvulas e vasos, peça por peça | `assets/modelos/coracao.glb` |
| Skill que ensina o Claude a montar qualquer cena dessas | `skills/explicativo-3d/` |
| Script pra tirar qualquer órgão do atlas Z-Anatomy | `skills/explicativo-3d/exportar_glb.py` |
| 13 skills de three.js (o motor 3D), da CloudAI-X | `extras/threejs-skills/` |

## Prompts prontos

**Usar o coração que já vem:**
```
Usando a skill explicativo-3d, faz a cena do coração com estas regiões, nesta ordem:
ventrículo esquerdo, aorta, átrio direito. Texto de cada uma: [...]. Título: [...].
Me mostra os snapshots antes de renderizar.
```

**Outro órgão (do atlas grátis Z-Anatomy):**
```
Usando a skill explicativo-3d, baixa o Z-Anatomy, exporta o [rim / cérebro / pulmão]
com o exportar_glb.py e monta a cena cortando de [frente / lado].
Regiões: [...]. Coloca o crédito do modelo no fim pra eu pôr na descrição.
```

**Do nicho (sem modelo nenhum, o Claude monta em código):**
```
Usando a skill explicativo-3d, monta em three.js um funil de vendas 3D com 4 camadas
(anúncio, página, checkout, upsell). Ele gira, abre as camadas e mostra a taxa de
conversão de cada uma: [números reais].
```

## Quanto custa

| Caminho | Custo |
|---|---|
| Template + coração do pack | R$ 0 |
| Z-Anatomy, BodyParts3D, NIH 3D, Smithsonian, Poly Haven | R$ 0 (respeite a licença de cada um) |
| Sketchfab com licença CC | R$ 0, com crédito ao autor |
| Gerar o objeto com IA (TRELLIS.2, Hunyuan3D, Meshy, Tripo) | grátis com limite ou alguns créditos. Sai em peça única: gira bonito, mas não dá pra pintar região |
| Blender + Blender MCP (o Claude mexendo no Blender) | R$ 0. Só se quiser render cinematográfico; é bem mais pesado |

## O que esperar

- **Render 3D é lento** em computador sem placa de vídeo boa: alguns segundos por quadro.
  Teste com `-q draft -f 24` e só faça o final depois de aprovar os snapshots.
- **O modelo precisa ter as peças separadas** pra cada região ganhar cor. Os do Z-Anatomy já vêm assim.
- **Crédito na descrição** quando a licença pede. Pro coração do pack:
  `Modelo 3D: BodyParts3D, The Database Center for Life Science (CC BY-SA 2.1 JP) · Z-Anatomy (CC BY-SA 4.0)`
- **Conteúdo de saúde:** confira o texto das etiquetas. O Claude não deve inventar função de órgão.

## Ferramentas pra ir além (só o link)

| Ferramenta | Pra quê | Licença |
|---|---|---|
| [ahujasid/blender-mcp](https://github.com/ahujasid/blender-mcp) | o Claude controla o Blender: modela, ilumina e renderiza | MIT |
| [Z-Anatomy](https://github.com/Z-Anatomy/Models-of-human-anatomy) | atlas 3D completo do corpo humano | CC BY-SA 4.0 |
| [microsoft/TRELLIS.2](https://github.com/microsoft/TRELLIS.2) | imagem → modelo 3D, roda na sua máquina com GPU | MIT |
| [Hunyuan3D](https://github.com/Tencent-Hunyuan) | imagem/texto → modelo 3D | licença própria da Tencent |
| Bloco `exploded-stack` do HyperFrames | camadas que se separam com etiqueta (arquitetura, funil) | Apache-2.0 · `npx hyperframes add exploded-stack` |
| Bloco `product-turntable` do HyperFrames | produto girando num pedestal, aceita .glb | Apache-2.0 · `npx hyperframes add product-turntable` |

➡️ Voltar pro [README](../README.md)
