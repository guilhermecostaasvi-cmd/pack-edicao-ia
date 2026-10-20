"""
Corta os silêncios de um vídeo falado (decupagem automática), sem nenhuma API paga.
Só precisa do FFmpeg instalado e de Python 3.

Uso:
    python cortar_silencios.py meu-video.mp4
    python cortar_silencios.py meu-video.mp4 --limite -35 --pausa 0.35 --respiro 0.08

Saída: meu-video_decupado.mp4 (na mesma pasta) + meu-video_cortes.json (o que foi cortado)

--limite   volume (dB) abaixo do qual conta como silêncio. Sala barulhenta: -30. Sala silenciosa: -40.
--pausa    pausa mínima (s) pra cortar. 0.35 = ritmo de YouTube. 0.2 = ritmo de criativo/reels.
--respiro  quanto de folga (s) fica antes e depois de cada fala, pra não comer a primeira sílaba.
"""
import argparse
import json
import os
import re
import subprocess
import sys


def duracao(arquivo):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", arquivo],
        capture_output=True, text=True, check=True,
    ).stdout.strip()
    return float(out)


def achar_silencios(arquivo, limite, pausa):
    proc = subprocess.run(
        ["ffmpeg", "-hide_banner", "-i", arquivo, "-af", f"silencedetect=noise={limite}dB:d={pausa}", "-f", "null", "-"],
        capture_output=True, text=True,
    )
    inicios = [float(x) for x in re.findall(r"silence_start: (-?[\d.]+)", proc.stderr)]
    fins = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", proc.stderr)]
    return list(zip(inicios, fins + [None] * (len(inicios) - len(fins))))


def trechos_de_fala(total, silencios, respiro):
    trechos, cursor = [], 0.0
    for ini, fim in silencios:
        ini = max(0.0, ini)
        fim = total if fim is None else fim
        if ini - cursor > 0.05:
            trechos.append((max(0.0, cursor - respiro), min(total, ini + respiro)))
        cursor = fim
    if total - cursor > 0.05:
        trechos.append((max(0.0, cursor - respiro), total))
    # junta trechos que se encostaram por causa do respiro
    juntos = []
    for a, b in trechos:
        if juntos and a <= juntos[-1][1]:
            juntos[-1] = (juntos[-1][0], max(juntos[-1][1], b))
        else:
            juntos.append((a, b))
    return juntos


def montar(arquivo, trechos, saida):
    partes, rotulos = [], []
    for i, (a, b) in enumerate(trechos):
        partes.append(f"[0:v]trim=start={a:.3f}:end={b:.3f},setpts=PTS-STARTPTS[v{i}];")
        # 30 ms de fade em cada corte: nunca dá estalo no áudio
        fade = min(0.03, (b - a) / 3)
        partes.append(
            f"[0:a]atrim=start={a:.3f}:end={b:.3f},asetpts=PTS-STARTPTS,"
            f"afade=t=in:d={fade:.3f},afade=t=out:st={max(0, b - a - fade):.3f}:d={fade:.3f}[a{i}];"
        )
        rotulos.append(f"[v{i}][a{i}]")
    filtro = "".join(partes) + "".join(rotulos) + f"concat=n={len(trechos)}:v=1:a=1[v][a]"
    script = saida + ".filtro.txt"
    with open(script, "w", encoding="utf-8") as f:
        f.write(filtro)
    try:
        subprocess.run(
            ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", arquivo, "-filter_complex_script", script,
             "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-crf", "18", "-preset", "medium", "-c:a", "aac", "-b:a", "192k", saida],
            check=True,
        )
    finally:
        os.remove(script)


def main():
    p = argparse.ArgumentParser(description="Corta os silêncios de um vídeo falado.")
    p.add_argument("video")
    p.add_argument("--limite", type=float, default=-35.0)
    p.add_argument("--pausa", type=float, default=0.35)
    p.add_argument("--respiro", type=float, default=0.08)
    a = p.parse_args()

    if not os.path.exists(a.video):
        sys.exit(f"Arquivo não encontrado: {a.video}")
    total = duracao(a.video)
    silencios = achar_silencios(a.video, a.limite, a.pausa)
    trechos = trechos_de_fala(total, silencios, a.respiro)
    if not trechos:
        sys.exit("Não achei fala nenhuma. Tente um --limite mais alto (ex.: -30).")

    base, _ = os.path.splitext(a.video)
    saida = base + "_decupado.mp4"
    montar(a.video, trechos, saida)

    novo = sum(b - a_ for a_, b in trechos)
    with open(base + "_cortes.json", "w", encoding="utf-8") as f:
        json.dump({"original_s": round(total, 2), "decupado_s": round(novo, 2), "trechos_mantidos": [[round(x, 3), round(y, 3)] for x, y in trechos]}, f, indent=2)
    print(f"Antes: {total:.1f}s  ·  Depois: {novo:.1f}s  ·  Cortou {total - novo:.1f}s ({(1 - novo / total) * 100:.0f}%) em {len(trechos)} trechos")
    print(f"Arquivo: {saida}")


if __name__ == "__main__":
    main()
