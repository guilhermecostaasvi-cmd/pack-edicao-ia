# 04 · Problemas comuns

| Sintoma | Causa provável | Solução |
|---|---|---|
| `node`, `ffmpeg` ou `claude` "não é reconhecido" | terminal aberto antes da instalação | feche e abra o PowerShell |
| Erro com `&&` no Windows | PowerShell não aceita `&&` | um comando por vez |
| Render falha logo no começo | falta FFmpeg ou o Node é antigo | `node -v` (precisa 22+) e `ffmpeg -version` |
| Render muito lento | ele grava quadro a quadro, é normal | use `-q draft` pra testar e só o final em qualidade alta |
| **Animação some no vídeo final, sem erro** | o `data-composition-id` não é igual ao nome do arquivo | use o nome exato, ex.: `data-composition-id="02-notificacao-venda"` |
| Animação entra fora do tempo da fala | transcrição imprecisa | peça pra refazer a transcrição com atenção |
| Fonte saiu diferente no MP4 | fonte sem arquivo `.woff2` no projeto | coloque o arquivo em `assets/fonts/` (skill identidade-visual) |
| Som não toca dentro da animação | `<audio>` sem `id` | todo `<audio>` precisa de `id` |
| Animação "pula" ou fica diferente a cada render | `Math.random()`, `Date.now()` ou `tl.call()` no código | troque por valores fixos e `tl.set()` |
| Visual com "cara de IA" | faltou proibir o padrão | reforce: "nada de fade em tudo, nada de texto no meio sem motivo, pouco elemento" |
| `.webm` não abre no Premiere | o Premiere não lê WebM transparente | renderize com `--format mov` |
| Toda edição sai num padrão diferente | a skill não foi atualizada | rode o Prompt 5 no fim de cada edição |

---

## Skills e ferramentas que combinam com este pack

| Ferramenta | O que faz | Link |
|---|---|---|
| **HyperFrames** (obrigatório) | o motor: transforma HTML em vídeo | github.com/heygen-com/hyperframes |
| **video-use** | decupagem avançada com autocorreção em cada corte (usa ElevenLabs, pago) | github.com/browser-use/video-use |
| **freecut** | versão do video-use sem nenhuma chave paga | github.com/Moh4696/freecut |
| **Remotion skills** | outro motor de vídeo (React). Atenção: licença paga pra empresa acima de certo tamanho | github.com/remotion-dev/skills |

> As skills deste pack (`decupagem`, `pack-edicao-ia`, `criativo-vertical`, `identidade-visual`)
> não dependem de nenhuma chave de API.
