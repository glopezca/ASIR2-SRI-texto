#!/usr/bin/env python3
"""Validador ligero del material docente."""
from pathlib import Path
import re, subprocess, sys
ROOT=Path(__file__).resolve().parents[1]
UT=sorted(ROOT.glob("UT*.md")); errors=[]
COMMON="PREPARACIÓN COMÚN DE LAS PRÁCTICAS"
for p in UT:
    s=p.read_text(encoding="utf-8")
    if s.count(COMMON)!=1: errors.append(f"{p.name}: preparación común")
    blocks=re.findall(r'^> 🔎 \*\*PISTAS ESPECÍFICAS.*?\n(?:(?:>.*|>?)\n)+',s,re.M)
    norm=[re.sub(r"\s+"," ",x.strip()) for x in blocks]
    if len(norm)!=len(set(norm)): errors.append(f"{p.name}: pistas clónicas")
    for bad in ["example.com","example.es","asir.test","cite","filecite","ProxyPass /rtmp rtmp://","disable_plaintext_auth = no"]:
        if bad in s: errors.append(f"{p.name}: patrón prohibido {bad}")
    if re.search(r'(?m)^\s*(?:sudo\s+)?apt-key\b',s): errors.append(f"{p.name}: receta apt-key")
    if s.count("```")%2: errors.append(f"{p.name}: fences desbalanceados")
    t=s.lower().find("test de repaso"); sol=min([i for i in [s.lower().find("solucionario del test"),s.lower().find("respuestas del test")] if i>=0],default=-1)
    if t>=0 and sol>=0 and t>sol: errors.append(f"{p.name}: orden test/solucionario")
    for h in ["Entorno I","Entorno II","Entorno III","Entorno IV","## 📘 Glosario esencial de la UT","## 🧩 Banco de ejercicios propuestos","## 🔗 Recursos oficiales y ampliación"]:
        if h not in s: errors.append(f"{p.name}: falta {h}")
    for i,b in enumerate(re.findall(r'```(?:bash|sh|shell)\n(.*?)```',s,re.S|re.I),1):
        if re.search(r'<[^>]+>|\$\{[^}]+\}',b) or not b.strip(): continue
        if subprocess.run(["bash","-n"],input=b,text=True,capture_output=True).returncode:
            errors.append(f"{p.name}: Bash {i} inválido")
for asset in ["img/captura-roundcube-didactica.png","img/captura-sympa-didactica.png"]:
    if not (ROOT/asset).exists(): errors.append(f"falta recurso gráfico {asset}")
if len(UT)!=8: errors.append("No hay exactamente 8 UT")
if errors:
    print("FAIL")
    for e in errors: print("-",e)
    sys.exit(1)
print("PASS: validator.py")
