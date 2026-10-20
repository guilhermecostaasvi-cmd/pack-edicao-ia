"""
Gera todos os efeitos sonoros do pack por código (síntese pura, sem
nenhum arquivo de terceiro). Rodar:  python gerar_sons.py
Precisa de: numpy, scipy  ->  pip install numpy scipy

Como cada som é matemática, ele é 100% seu: pode usar em vídeo, criativo,
VSL e anúncio sem risco de direito autoral.
"""
import os
import numpy as np
from scipy import signal
from scipy.io import wavfile

SR = 48000
OUT = os.path.dirname(os.path.abspath(__file__))
rng = np.random.default_rng(7)  # semente fixa = sempre o mesmo som


# ---------------------------------------------------------------- utilidades
def t(dur):
    return np.arange(int(SR * dur)) / SR


def ruido(dur, cor="branco"):
    n = rng.standard_normal(int(SR * dur))
    if cor == "rosa":
        b, a = [0.049922035, -0.095993537, 0.050612699, -0.004408786], [1, -2.494956002, 2.017265875, -0.522189400]
        n = signal.lfilter(b, a, n)
    return n / (np.max(np.abs(n)) + 1e-9)


def env_ad(n, ataque, decaimento, curva=4.0):
    """Envelope ataque/decaimento exponencial (em segundos)."""
    a = int(SR * ataque)
    e = np.ones(n)
    if a > 0:
        e[:a] = np.linspace(0, 1, a) ** 2
    x = np.arange(n - a) / SR
    e[a:] = np.exp(-curva * x / max(decaimento, 1e-4))
    return e


def bandpass_varrendo(x, f0, f1, q=1.2, passos=64):
    """Filtro passa-banda que varre de f0 a f1 (o 'whoosh')."""
    n = len(x)
    out = np.zeros(n)
    bloco = n // passos + 1
    zi = None
    for i in range(passos):
        ini, fim = i * bloco, min((i + 1) * bloco, n)
        if ini >= n:
            break
        fr = f0 * (f1 / f0) ** (i / (passos - 1))
        lo, hi = max(fr / (1 + 1 / q), 20), min(fr * (1 + 1 / q), SR / 2 - 100)
        sos = signal.butter(2, [lo, hi], btype="band", fs=SR, output="sos")
        if zi is None:
            zi = signal.sosfilt_zi(sos) * 0
        y, zi = signal.sosfilt(sos, x[ini:fim], zi=zi)
        out[ini:fim] = y
    return out


def passa(x, f, tipo="low", ordem=4):
    sos = signal.butter(ordem, f, btype=tipo, fs=SR, output="sos")
    return signal.sosfilt(sos, x)


def reverb(x, tempo=1.2, mix=0.25):
    ir_n = int(SR * tempo)
    ir = rng.standard_normal(ir_n) * np.exp(-6.0 * np.arange(ir_n) / ir_n)
    ir = passa(ir, 6000)
    ir /= np.sqrt(np.sum(ir ** 2))
    molhado = np.zeros(len(x) + ir_n)
    conv = signal.fftconvolve(x, ir)[: len(x) + ir_n]
    molhado[: len(conv)] = conv
    seco = np.concatenate([x, np.zeros(ir_n)])
    return (1 - mix) * seco + mix * molhado


def seno_varrendo(dur, f0, f1, forma="exp"):
    tt = t(dur)
    if forma == "exp":
        f = f0 * (f1 / f0) ** (tt / dur)
    else:
        f = np.linspace(f0, f1, len(tt))
    fase = 2 * np.pi * np.cumsum(f) / SR
    return np.sin(fase)


def estereo(x, pan_ini=0.0, pan_fim=0.0, largura=0.0):
    """Pan de -1 (esq) a 1 (dir), com movimento e um pouco de largura."""
    p = np.linspace(pan_ini, pan_fim, len(x))
    ang = (p + 1) * np.pi / 4
    esq, dir_ = x * np.cos(ang), x * np.sin(ang)
    if largura > 0:
        d = int(SR * 0.012 * largura)
        dir_ = np.concatenate([np.zeros(d), dir_])[: len(x)] * 0.85 + dir_ * 0.15
    return np.stack([esq, dir_], axis=1)


def salvar(nome, x, pico_db=-1.0, rms_db=-18.0):
    if x.ndim == 1:
        x = estereo(x)
    # micro fade nas pontas pra nunca dar estalo
    f = min(int(SR * 0.004), len(x) // 4)
    rampa = np.linspace(0, 1, f)[:, None]
    x[:f] *= rampa
    x[-f:] *= rampa[::-1]
    pico = np.max(np.abs(x)) + 1e-9
    x = x / pico * (10 ** (pico_db / 20))
    if rms_db is not None:
        # nivela o volume percebido: todos os sons ficam na mesma altura
        ativo = np.abs(x).max(axis=1) > 0.02
        rms = np.sqrt(np.mean(x[ativo] ** 2)) if ativo.any() else 1
        ganho = min(10 ** (rms_db / 20) / rms, 1.0)  # nunca passa do pico
        x = x * ganho
    wavfile.write(os.path.join(OUT, nome + ".wav"), SR, (x * 32767).astype(np.int16))
    print(f"  {nome}.wav  ({len(x)/SR:.2f}s)")


def silencio(dur):
    return np.zeros(int(SR * dur))


def cola(*partes):
    return np.concatenate(partes)


def soma(*sinais):
    n = max(len(s) for s in sinais)
    out = np.zeros(n)
    for s in sinais:
        out[: len(s)] += s
    return out


def sino(f, dur, parciais=((1, 1.0), (2.76, 0.5), (5.4, 0.25), (8.9, 0.12)), decai=0.8):
    tt = t(dur)
    s = np.zeros(len(tt))
    for mult, amp in parciais:
        s += amp * np.sin(2 * np.pi * f * mult * tt) * np.exp(-tt * (3 + mult) / decai)
    return s


# ------------------------------------------------------------------- WHOOSH
def whooshes():
    print("WHOOSH")
    d = 0.55
    x = bandpass_varrendo(ruido(d, "rosa"), 300, 4500, q=1.5) * env_ad(int(SR * d), 0.22, 0.33, 3)
    salvar("whoosh-curto", estereo(x, -0.7, 0.7, 0.5))

    d = 1.1
    x = bandpass_varrendo(ruido(d, "rosa"), 180, 6000, q=1.3) * env_ad(int(SR * d), 0.6, 0.5, 3)
    salvar("whoosh-longo", estereo(x, -0.9, 0.9, 0.7))

    d = 0.8
    x = bandpass_varrendo(ruido(d, "rosa"), 90, 900, q=1.1) * env_ad(int(SR * d), 0.3, 0.5, 3)
    x += 0.5 * seno_varrendo(d, 70, 45) * env_ad(int(SR * d), 0.25, 0.5, 4)
    salvar("whoosh-grave", estereo(x, 0.6, -0.6, 0.6))

    d = 0.35
    x = bandpass_varrendo(ruido(d), 2500, 9000, q=2.0) * env_ad(int(SR * d), 0.1, 0.25, 4)
    salvar("swoosh-agudo", estereo(x, -0.8, 0.8, 0.3))

    d = 0.45
    x = bandpass_varrendo(ruido(d, "rosa"), 5000, 400, q=1.4) * env_ad(int(SR * d), 0.05, 0.4, 4)
    salvar("whoosh-saida", estereo(x, 0.8, -0.8, 0.5))


# ------------------------------------------------------------------ IMPACTO
def impactos():
    print("IMPACTO")
    d = 1.6
    boom = seno_varrendo(d, 110, 32) * env_ad(int(SR * d), 0.002, 1.2, 3.5)
    clique = passa(ruido(0.03), 2500) * env_ad(int(SR * 0.03), 0.0005, 0.03, 6)
    x = soma(boom, 0.6 * clique)
    salvar("impacto-grave", np.tanh(1.8 * x))

    d = 0.35
    corpo = seno_varrendo(d, 180, 55) * env_ad(int(SR * d), 0.001, 0.22, 5)
    ataque = passa(ruido(0.05), 4000, "low") * env_ad(int(SR * 0.05), 0.0005, 0.05, 6)
    salvar("impacto-seco", np.tanh(2.2 * soma(corpo, 0.7 * ataque)))

    d = 2.4
    boom = seno_varrendo(d, 90, 28) * env_ad(int(SR * d), 0.002, 1.8, 3)
    corpo = passa(ruido(d, "rosa"), 900) * env_ad(int(SR * d), 0.003, 0.9, 5)
    x = soma(boom, 0.5 * corpo)
    x = reverb(np.tanh(1.5 * x), 1.8, 0.35)
    salvar("hit-cinematico", estereo(x, 0, 0, 0.8))

    d = 0.5
    pele = seno_varrendo(d, 160, 70) * env_ad(int(SR * d), 0.001, 0.3, 5)
    esteira = passa(passa(ruido(d), 1800, "high"), 7000) * env_ad(int(SR * d), 0.001, 0.15, 6)
    salvar("batida-tambor", soma(pele, 0.22 * esteira))

    d = 0.9
    x = soma(seno_varrendo(d, 140, 40) * env_ad(int(SR * d), 0.001, 0.6, 4),
             0.6 * passa(ruido(d), 3000) * env_ad(int(SR * d), 0.001, 0.12, 6))
    salvar("slam-texto", reverb(np.tanh(2 * x), 0.6, 0.15))


# -------------------------------------------------------------------- RISER
def risers():
    print("RISER")
    for dur, nome in ((2.0, "riser-2s"), (4.0, "riser-4s")):
        n = int(SR * dur)
        sw = bandpass_varrendo(ruido(dur, "rosa"), 200, 9000, q=1.6)
        tom = sum(seno_varrendo(dur, 110 * k, 880 * k) / k for k in (1, 2, 3))
        env = np.linspace(0, 1, n) ** 2.4
        x = (sw * 0.8 + tom * 0.35) * env
        x *= 1 + 0.25 * np.sin(2 * np.pi * np.cumsum(np.linspace(4, 18, n)) / SR)  # tremolo acelerando
        salvar(nome, estereo(x, -0.3, 0.3, 0.8), rms_db=None)

    d = 1.6
    x = passa(passa(ruido(d, "rosa"), 600, "high"), 9000) * (np.linspace(0, 1, int(SR * d)) ** 3)
    salvar("reverso-swell", estereo(x, 0, 0, 1.0), rms_db=None)


# ---------------------------------------------------------------- POP/CLIQUE
def pops():
    print("POP / CLIQUE")
    d = 0.12
    salvar("pop", seno_varrendo(d, 900, 300) * env_ad(int(SR * d), 0.001, 0.08, 5))

    d = 0.18
    x = seno_varrendo(d, 300, 1400) * env_ad(int(SR * d), 0.002, 0.14, 4)
    salvar("pop-bolha", x)

    d = 0.04
    x = signal.sosfilt(signal.butter(2, [1500, 5000], btype="band", fs=SR, output="sos"), ruido(d)) * env_ad(int(SR * d), 0.0003, 0.015, 7)
    x = soma(x, 0.6 * np.sin(2 * np.pi * 2100 * t(d)) * env_ad(int(SR * d), 0.0003, 0.012, 7))
    salvar("clique-mouse", x)

    d = 0.06
    x = soma(signal.sosfilt(signal.butter(2, [900, 4500], btype="band", fs=SR, output="sos"), ruido(d)) * env_ad(int(SR * d), 0.0003, 0.025, 7),
             0.5 * np.sin(2 * np.pi * 180 * t(d)) * env_ad(int(SR * d), 0.0005, 0.04, 6))
    salvar("tecla", x)

    d = 0.05
    salvar("tick", np.sin(2 * np.pi * 2400 * t(d)) * env_ad(int(SR * d), 0.0003, 0.03, 7))

    # digitando: sequência de teclas com timing humano (deterministico)
    partes = []
    for i in range(14):
        dd = 0.06
        k = soma(signal.sosfilt(signal.butter(2, [800 + (i % 4) * 200, 4500], btype="band", fs=SR, output="sos"), ruido(dd)) * env_ad(int(SR * dd), 0.0003, 0.025, 7),
                 0.35 * np.sin(2 * np.pi * (160 + (i % 3) * 25) * t(dd)) * env_ad(int(SR * dd), 0.0005, 0.04, 6))
        partes += [k * (0.7 + 0.3 * ((i * 7) % 5) / 4), silencio(0.05 + ((i * 13) % 7) * 0.018)]
    salvar("digitando", cola(*partes))


# -------------------------------------------------------------------- VENDA
def vendas():
    print("VENDA")
    # cha-ching: batida de caixa + dois sinos + moedas
    caixa = seno_varrendo(0.12, 400, 120) * env_ad(int(SR * 0.12), 0.001, 0.08, 5)
    s1 = sino(1568, 1.4)
    s2 = sino(2093, 1.4)
    moedas = np.zeros(int(SR * 1.2))
    for i in range(9):
        ini = int(SR * (0.02 + i * 0.045 + (i % 3) * 0.012))
        m = sino(3000 + (i * 397) % 1600, 0.25, ((1, 1), (2.4, 0.4)), 0.15) * (0.6 - i * 0.04)
        moedas[ini: ini + len(m)] += m[: len(moedas) - ini]
    x = soma(caixa, cola(silencio(0.08), 0.8 * s1), cola(silencio(0.2), 0.9 * s2), cola(silencio(0.25), 0.5 * moedas))
    salvar("cha-ching", estereo(reverb(x, 0.8, 0.18), 0, 0, 0.6))

    salvar("moeda", sino(2600, 0.6, ((1, 1), (2.4, 0.5), (4.1, 0.2)), 0.35))

    # notificação de venda: dois tons subindo, limpo (estilo app de pagamento genérico)
    a = sino(1318.5, 0.5, ((1, 1), (2, 0.2)), 0.5)
    b = sino(1760, 0.8, ((1, 1), (2, 0.2)), 0.6)
    salvar("notificacao-venda", reverb(soma(a, cola(silencio(0.11), b)), 0.5, 0.12))

    # ding de sucesso: arpejo maior
    notas = [1046.5, 1318.5, 1568, 2093]
    x = soma(*[cola(silencio(i * 0.07), sino(f, 0.9, ((1, 1), (2, 0.25), (3, 0.08)), 0.5) * (0.9 - i * 0.1)) for i, f in enumerate(notas)])
    salvar("sucesso", reverb(x, 0.7, 0.18))

    # varias vendas seguidas (pra cascata de notificações)
    partes = []
    for i in range(5):
        partes.append(cola(silencio(i * 0.38), soma(sino(1318.5, 0.4, ((1, 1), (2, .2)), .4), cola(silencio(0.09), sino(1760, 0.5, ((1, 1), (2, .2)), .5)))))
    salvar("vendas-em-sequencia", reverb(soma(*partes), 0.5, 0.12))


# ------------------------------------------------------------------- GLITCH
def glitches():
    print("GLITCH")
    d = 0.5
    n = int(SR * d)
    x = np.zeros(n)
    pos = 0
    i = 0
    while pos < n:
        tam = int(SR * (0.015 + ((i * 17) % 9) * 0.006))
        f = 200 + ((i * 331) % 2400)
        seg = signal.square(2 * np.pi * f * t(tam / SR)) * (0.4 + ((i * 7) % 5) / 8)
        if i % 3 == 0:
            seg = ruido(tam / SR)
        x[pos: pos + tam] = seg[: n - pos]
        pos += tam + int(SR * 0.004 * (i % 2))
        i += 1
    x = np.round(x * 8) / 8  # bitcrush
    salvar("glitch-digital", estereo(x, -0.4, 0.4, 0.4), -3)

    d = 0.7
    x = passa(ruido(d), 7000) * (0.5 + 0.5 * signal.square(2 * np.pi * 23 * t(d)))
    salvar("estatica", estereo(x * env_ad(int(SR * d), 0.01, 0.6, 3), 0, 0, 1.0), -4)

    # stutter: um mesmo pedaço repetido acelerando
    pedaco = seno_varrendo(0.06, 600, 200) * env_ad(int(SR * 0.06), 0.001, 0.05, 4)
    partes = []
    for i in range(10):
        partes += [pedaco, silencio(max(0.005, 0.07 - i * 0.007))]
    salvar("stutter", cola(*partes), -3)

    d = 0.35
    x = signal.sawtooth(2 * np.pi * 110 * t(d)) * env_ad(int(SR * d), 0.005, 0.3, 3)
    x += 0.6 * signal.sawtooth(2 * np.pi * 116 * t(d)) * env_ad(int(SR * d), 0.005, 0.3, 3)
    salvar("erro-buzz", passa(x, 2500), -3)


# ---------------------------------------------------------------- UI / ZOOM
def ui():
    print("UI / TRANSIÇÃO")
    d = 0.25
    x = bandpass_varrendo(ruido(d), 1500, 5000, q=2.5) * env_ad(int(SR * d), 0.03, 0.2, 4)
    salvar("swipe", estereo(x, 0.7, -0.7, 0.3))

    d = 0.08
    salvar("toggle", soma(seno_varrendo(d, 700, 1100) * env_ad(int(SR * d), 0.001, 0.06, 5),
                          0.3 * passa(ruido(d), 3000, "high") * env_ad(int(SR * d), 0.0005, 0.02, 7)))

    d = 0.6
    x = soma(seno_varrendo(d, 220, 1200) * env_ad(int(SR * d), 0.3, 0.3, 3),
             0.6 * bandpass_varrendo(ruido(d, "rosa"), 400, 6000) * env_ad(int(SR * d), 0.3, 0.3, 3))
    salvar("zoom-in", estereo(x, 0, 0, 0.6))

    d = 0.6
    x = soma(seno_varrendo(d, 1200, 220) * env_ad(int(SR * d), 0.02, 0.5, 3),
             0.6 * bandpass_varrendo(ruido(d, "rosa"), 6000, 400) * env_ad(int(SR * d), 0.02, 0.5, 3))
    salvar("zoom-out", estereo(x, 0, 0, 0.6))

    d = 1.2
    brilho = sum(np.sin(2 * np.pi * f * t(d)) for f in (2637, 3136, 3951, 5274)) / 4
    x = brilho * env_ad(int(SR * d), 0.01, 1.0, 4) + 0.4 * passa(ruido(d), 6000, "high") * env_ad(int(SR * d), 0.005, 0.3, 5)
    salvar("flash-brilho", estereo(reverb(x, 0.9, 0.3), 0, 0, 1.0), -3)

    # check de sucesso: tique duplo + tom
    x = soma(sino(1760, 0.5, ((1, 1), (2, .15)), .35), cola(silencio(0.09), sino(2349, 0.6, ((1, 1), (2, .15)), .4)))
    salvar("check", x)


if __name__ == "__main__":
    whooshes()
    impactos()
    risers()
    pops()
    vendas()
    glitches()
    ui()
    print("pronto.")
