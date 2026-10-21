---
name: explicativo-3d
description: Cria animações explicativas em 3D (órgão, peça, produto, funil) que giram, são cortadas no meio e mostram cada região com cor e etiqueta. Use quando pedirem "animação 3D", "mostra por dentro", "corta no meio", "explica as partes de", "vídeo explicativo com modelo 3D".
---

# Explicativo 3D

Gera uma cena 3D de verdade (three.js dentro do HyperFrames). O modelo gira, uma lâmina de luz
corta no meio, a metade da frente sai e cada região acende com cor + etiqueta + linha.
Template: `compositions/23-explicativo-3d.html`. Exemplo pronto: coração com 4 câmaras.

## Fluxo

1. **Entenda o pedido** — o que vai ser mostrado, quais regiões, em que ordem e o texto curto de cada
   uma (nome + uma linha de "pra que serve"). Máximo 6 regiões por cena; mais que isso, faça 2 cenas.
2. **Arrume o modelo .glb** (veja "De onde tirar o modelo"). O modelo PRECISA ter as regiões como
   peças separadas, com nome. Modelo de peça única não dá pra colorir por região.
3. **Descubra o nome das peças** — rode no terminal:
   `node -e "const fs=require('fs');const b=fs.readFileSync(process.argv[1]);const j=JSON.parse(b.slice(20,20+b.readUInt32LE(12)).toString());console.log(j.nodes.map(n=>n.name).join('\n'))" modelo.glb`
4. **Monte as variáveis** do template:
   - `modelo`: caminho do .glb (coloque em `assets/modelos/`)
   - `regioes`: JSON com `parte` (começo do nome da peça), `nome`, `info`, `cor`
   - `pecas_claras`: peças pra deixar em cor clara (válvulas, parafusos, detalhes)
   - `eixo_corte`: `frente` (separa frente e trás) ou `lado` (esquerda e direita)
   - `titulo`, `subtitulo`, `cor_base`, `fundo`
5. **Confira antes de renderizar** — tire snapshot nos tempos 1 s, 3 s, 5,5 s e no fim
   (`npx hyperframes snapshot`). Veja se cada etiqueta aponta pra peça certa e se nenhuma
   etiqueta cobre o modelo ou o título.
6. **Renderize** em `-q draft -f 24` pra testar. 3D é lento no computador sem placa de vídeo boa
   (vários segundos por quadro). O final em qualidade alta só depois de aprovado.

## Tempos do template (14 s)

| Tempo | O que acontece |
|---|---|
| 0–2,6 s | modelo gira e assenta, título entra |
| 2,6–3,4 s | lâmina de luz desce e corta |
| 3,3–4,9 s | metade da frente sai, câmera aproxima |
| 5,0 s em diante | uma região a cada 1,15 s: acende, etiqueta entra com "pop" |

Pra mudar o ritmo, mexa em `T_CORTE`, `T_ABRE`, `T_REG` e `PASSO` no script e nos `data-start`
dos `<audio>` (um pop por região).

## De onde tirar o modelo (grátis)

| Fonte | Bom pra | Licença | Observação |
|---|---|---|---|
| **Z-Anatomy** (github.com/Z-Anatomy) | anatomia humana inteira, peça por peça | CC BY-SA 4.0 (+ BodyParts3D, CC BY-SA 2.1 JP) | use `exportar_glb.py` desta pasta. Crédito dos dois na descrição |
| **BodyParts3D** (lifesciencedb.jp) | anatomia, base do Z-Anatomy | CC BY-SA | arquivos .obj separados por estrutura |
| **NIH 3D** (3d.nih.gov) | órgãos, proteínas, vírus, células | varia, muitos domínio público | confira a licença de cada modelo |
| **Smithsonian 3D** (3d.si.edu) | fósseis, objetos, animais | CC0 nos de "Open Access" | |
| **Sketchfab** (filtro "Downloadable" + licença CC) | quase tudo | CC BY na maioria | escolha modelo com peças separadas |
| **Poly Haven** (polyhaven.com) | objetos realistas | CC0 | |
| **IA: TRELLIS.2, Hunyuan3D, Meshy, Tripo** | criar um objeto que não existe | varia | sai em peça ÚNICA: serve pra girar e mostrar, não pra pintar região |
| **Montar em código (three.js)** | funil, engrenagem, camadas, gráfico 3D | seu | o Claude monta com caixas, cilindros e esferas. Bom pro nicho de marketing |

### Z-Anatomy em 3 comandos

```bash
pip install bpy                                   # Blender sem abrir o Blender (~400 MB)
# baixe Z-Anatomy.zip de github.com/Z-Anatomy/Models-of-human-anatomy e descompacte
python exportar_glb.py Startup.blend - --listar heart          # procura as peças
python exportar_glb.py Startup.blend coracao.glb --colecao Heart
```

Os nomes no Z-Anatomy estão em inglês (Right atrium, Left ventricle...). As etiquetas da cena
você escreve em português no campo `nome`.

## Regras

- **Nunca invente anatomia nem função.** O texto do `info` vem do que o usuário pediu ou de fonte
  confiável. Se não tiver certeza, pergunte.
- **Cores com sentido:** em coração, lado direito azul (sangue sem oxigênio) e esquerdo vermelho.
  Em produto/funil, use as cores da marca.
- **Crédito do modelo** sempre na descrição do vídeo quando a licença pedir (CC BY, CC BY-SA).
- Etiquetas no máximo 2 linhas, nome com até 3 palavras.
- Tudo determinístico: nada de `Math.random()` ou `Date.now()`. Toda animação sai de `render(t)`.
- Se o modelo vier gigante ou minúsculo, não mexa no .glb: o template já centraliza e ajusta o tamanho.
- three.js vem em `assets/vendor/three/three-pack.min.js` (sem internet, com GLTFLoader).

## Aprendizados

(adicione aqui o que o usuário corrigir)
