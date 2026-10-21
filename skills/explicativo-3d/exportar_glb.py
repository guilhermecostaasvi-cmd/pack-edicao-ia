"""Exporta peças de um arquivo .blend para um .glb pronto pro template 23-explicativo-3d.

Feito pro Z-Anatomy (atlas de anatomia grátis, CC BY-SA 4.0), mas serve pra qualquer .blend.
Roda SEM abrir o Blender: precisa só do Python 3.13 e do pacote bpy (pip install bpy).

Exemplos:
  # todas as peças de uma coleção (ex.: "Heart", "Brain", "Kidney")
  python exportar_glb.py Startup.blend coracao.glb --colecao Heart

  # peças escolhidas pelo nome (começo do nome, separado por vírgula)
  python exportar_glb.py Startup.blend rim.glb --pecas "Kidney.r,Renal pelvis.r"

  # pra ver o que existe no arquivo
  python exportar_glb.py Startup.blend - --listar rim
"""
import argparse
import sys

import bpy

ap = argparse.ArgumentParser()
ap.add_argument("blend")
ap.add_argument("saida")
ap.add_argument("--colecao", default="")
ap.add_argument("--pecas", default="")
ap.add_argument("--listar", default="")
ap.add_argument("--min-vertices", type=int, default=20)
a = ap.parse_args(sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else sys.argv[1:])

bpy.ops.wm.open_mainfile(filepath=a.blend)

if a.listar:
    termo = a.listar.lower()
    for o in bpy.data.objects:
        if termo in o.name.lower() and o.type in ("MESH", "CURVE"):
            cols = ", ".join(c.name for c in o.users_collection)
            print(f"{o.type:5s} {o.name}  [{cols}]")
    sys.exit(0)

alvos = []
if a.colecao:
    col = bpy.data.collections.get(a.colecao)
    if not col:
        sys.exit(f"coleção '{a.colecao}' não existe. Use --listar pra procurar.")
    alvos += [o for o in col.all_objects if o.type in ("MESH", "CURVE")]
if a.pecas:
    for nome in [p.strip() for p in a.pecas.split(",") if p.strip()]:
        alvos += [o for o in bpy.data.objects if o.name.startswith(nome) and o.type in ("MESH", "CURVE")]
if not alvos:
    sys.exit("nenhuma peça encontrada. Passe --colecao ou --pecas.")

dg = bpy.context.evaluated_depsgraph_get()
cena = bpy.data.scenes.new("exportar")
bpy.context.window.scene = cena
vistos = set()
for o in alvos:
    if o.name in vistos:
        continue
    vistos.add(o.name)
    me = bpy.data.meshes.new_from_object(o.evaluated_get(dg), depsgraph=dg)
    if len(me.vertices) < a.min_vertices:
        continue  # pula marcadores e rótulos vazios do atlas
    me.transform(o.matrix_world)
    me.materials.clear()
    novo = bpy.data.objects.new(o.name, me)
    cena.collection.objects.link(novo)
    print("ok", o.name, len(me.vertices))

bpy.ops.export_scene.gltf(filepath=a.saida, export_format="GLB", use_active_scene=True,
                          export_materials="NONE", export_normals=True, export_yup=True)
print("salvo:", a.saida)
