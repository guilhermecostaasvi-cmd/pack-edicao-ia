# 01 · Instalação (Windows e Mac)

Faz uma vez só. Leva uns 10 minutos.

## O que você precisa

| Item | Pra quê |
|---|---|
| **App desktop do Claude** (plano Pro ou maior) | é quem edita. Use a **aba Code** |
| **Node.js 22 ou mais novo** | roda o HyperFrames, o motor das animações |
| **FFmpeg** | junta os quadros e gera o MP4 |
| **Python 3** (opcional) | só pra skill de decupagem e pra gerar sons novos |

---

## 🪟 Windows

Abra o **PowerShell** e rode **um comando por vez** (copie, cole, Enter, espere terminar):

```
winget install OpenJS.NodeJS.LTS
```
```
winget install Gyan.FFmpeg
```
```
winget install Python.Python.3.12
```

**Feche e abra o PowerShell de novo.** Depois confira:

```
node -v
```
```
ffmpeg -version
```

✔ O `node -v` tem que mostrar **v22** ou mais. O `ffmpeg -version` tem que responder sem erro.

### As 3 travas do Windows (e como passar)

| O que aparece | Por quê | O que fazer |
|---|---|---|
| Erro com `&&` | o PowerShell do Windows não aceita `&&` | rode um comando por vez |
| `node` / `ffmpeg` / `claude` "não é reconhecido" | o terminal ainda não viu a instalação | feche e abra o PowerShell |
| O Claude não consegue digitar no terminal por você | o Windows bloqueia controle de tela no terminal | rode os comandos de instalação você mesmo |

---

## 🍎 Mac

No Terminal:

```
brew install node ffmpeg python
```

---

## Instalar o motor (HyperFrames) no Claude

Na **aba Code** do app do Claude, na caixa de mensagem, um de cada vez:

```
/plugin marketplace add heygen-com/hyperframes
```
```
/plugin install hyperframes@hyperframes
```

✔ Deu certo se o comando `/hyperframes` aparecer quando você digita `/`.

**Teste de fumaça** (pra ter certeza que renderiza):

> Usando /hyperframes, cria uma intro de 5 segundos com o texto "TESTE" entrando, fundo escuro.

Se voltou um MP4 que abre e toca, está tudo pronto. O render demora mesmo: ele grava quadro a quadro.

---

## Instalar as skills deste pack

Copie as pastas de `skills/` deste repositório pra pasta de skills do Claude:

| Sistema | Pasta |
|---|---|
| Windows | `C:\Users\SEU_USUARIO\.claude\skills\` |
| Mac | `~/.claude/skills/` |

Fica assim:
```
.claude/skills/
  pack-edicao-ia/SKILL.md
  decupagem/SKILL.md  (+ cortar_silencios.py)
  criativo-vertical/SKILL.md
  identidade-visual/SKILL.md
```

Ou peça pro próprio Claude, na aba Code, com esta pasta aberta:

> Copia as pastas de dentro de `skills/` pra minha pasta de skills do Claude.

Reinicie o Claude depois. ✔ As skills aparecem quando você digita `/`.

➡️ Próximo: [02 · Como usar](02-como-usar.md)
