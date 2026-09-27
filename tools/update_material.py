#!/usr/bin/env python3
"""Actualizador y quality gate de ASIR2-SRI-texto."""
from __future__ import annotations
import argparse
import datetime as dt
import pathlib
import re
import subprocess
import sys
import zipfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
COMMON = 'PREPARACIÓN COMÚN DE LAS PRÁCTICAS'
ENVIRONMENTS = ['Entorno I','Entorno II','Entorno III','Entorno IV']
BAD_LITERAL = ['example.com','example.es','asir.test','ProxyPass /rtmp rtmp://','disable_plaintext_auth = no']
REQUIRED = [
    'README.md','VERSION','CITATION.cff','LICENSE.md','NOTICE.md','CHANGELOG.md',
    'ANEXO-XII-Plantillas-Entregables.md','ANEXO-XIII-Matriz-Curricular.md',
    'ANEXO-XIV-Recursos-Abiertos.md','ANEXO-XV-Guia-Laboratorio-Reproducible.md',
    'ANEXO-XVI-Auditoria-Obsolescencia.md','ANEXO-XVII-Algoritmo-Actualizacion.md',
    'INFORME-REVISION-FUENTES-v6.5.1.md','INDICE-ALFABETICO.md',
]


def read(path: pathlib.Path) -> str:
    return path.read_text(encoding='utf-8')


def version() -> str:
    return read(ROOT / 'VERSION').strip()


def markdown_files():
    return sorted(ROOT.rglob('*.md'))


def bash_blocks(text: str):
    return re.findall(r'```(?:bash|sh|shell)\n(.*?)```', text, flags=re.S | re.I)


def validate_bash(text: str, name: str):
    errors = []
    for i, block in enumerate(bash_blocks(text), 1):
        # No ejecutamos comandos; bash -n solo comprueba sintaxis. Fragmentos con plantillas se omiten.
        if re.search(r'<[^>]+>|\$\{[^}]+\}', block) or not block.strip():
            continue
        proc = subprocess.run(['bash','-n'], input=block, text=True, capture_output=True)
        if proc.returncode:
            errors.append(f'{name}: bloque bash {i} inválido: {proc.stderr.strip()}')
    return errors


def check(verbose=True):
    errors = []
    notices = []
    v = version()
    if not re.fullmatch(r'\d+\.\d+\.\d+', v):
        errors.append(f'VERSION inválida: {v!r}')
    errors.extend(f'Falta {x}' for x in REQUIRED if not (ROOT / x).exists())

    rd = read(ROOT/'README.md') if (ROOT/'README.md').exists() else ''
    if f'v{v}' not in rd:
        errors.append('README no contiene la versión canónica')
    cff = read(ROOT/'CITATION.cff') if (ROOT/'CITATION.cff').exists() else ''
    if f'version: "{v}"' not in cff:
        errors.append('CITATION.cff no coincide con VERSION')
    lic = read(ROOT/'LICENSE.md') if (ROOT/'LICENSE.md').exists() else ''
    for needle in ['Germán López Castro','github.com/glopezca/ASIR2-SRI-texto','CC BY-SA 4.0']:
        if needle not in lic:
            errors.append(f'LICENSE.md: falta {needle}')
    report = ROOT / f'INFORME-PRUEBAS-v{v}.md'
    if not report.exists():
        errors.append(f'Falta informe de pruebas de la versión {v}')

    ut_files = sorted(ROOT.glob('UT*.md'))
    if len(ut_files) != 8:
        errors.append(f'Se esperaban 8 UT y hay {len(ut_files)}')
    for p in ut_files:
        s = read(p)
        if s.count(COMMON) != 1:
            errors.append(f'{p.name}: preparación común != 1')
        for req in ['## 📘 Glosario esencial de la UT','## 🧩 Banco de ejercicios propuestos','## 🔗 Recursos oficiales y ampliación','## 🧪']:
            if req not in s:
                errors.append(f'{p.name}: falta {req}')
        blocks = re.findall(r'^> 🔎 \*\*PISTAS ESPECÍFICAS.*?\n(?:(?:>.*|>?)\n)+', s, re.M)
        norm = [re.sub(r'\s+', ' ', b.strip()) for b in blocks]
        if len(norm) != len(set(norm)):
            errors.append(f'{p.name}: hay pistas específicas idénticas')
        test = s.lower().find('test de repaso')
        sol = min([i for i in [s.lower().find('solucionario del test'), s.lower().find('respuestas del test')] if i >= 0], default=-1)
        if test >= 0 and sol >= 0 and test > sol:
            errors.append(f'{p.name}: test aparece después del solucionario')
        if s.count('```') % 2:
            errors.append(f'{p.name}: fences de código desbalanceados')
        for bad in BAD_LITERAL:
            if bad in s:
                errors.append(f'{p.name}: aparece patrón técnico no permitido: {bad}')
        if re.search(r'(?m)^\s*(?:sudo\s+)?apt-key\b', s):
            errors.append(f'{p.name}: receta apt-key detectada')
        for env in ENVIRONMENTS:
            if env not in s:
                errors.append(f'{p.name}: falta {env}')
        errors.extend(validate_bash(s, p.name))

    for asset in ['img/captura-roundcube-didactica.png','img/captura-sympa-didactica.png']:
        if not (ROOT / asset).exists():
            errors.append(f'Falta recurso gráfico {asset}')

    for p in markdown_files():
        s = read(p)
        for target in re.findall(r'!?(?:\[[^]]*\])\(([^)#\s]+)(?:#[^)]+)?\)', s):
            if target.startswith(('http://','https://','mailto:')):
                continue
            if not (p.parent/target).exists() and not (ROOT/target).exists():
                errors.append(f'{p.relative_to(ROOT)}: enlace local roto {target}')

    if verbose:
        print('QUALITY GATE')
        print(f'Versión: {v}')
        print(f'UT: {len(ut_files)}')
        print(f'Informe: {report.name}')
        if errors:
            print('FAIL')
            for e in errors:
                print(' -', e)
        else:
            print('PASS: todos los controles superados')
        for n in notices:
            print('NOTICE:', n)
    return not errors


def new_report(newv: str):
    p = ROOT / f'INFORME-PRUEBAS-v{newv}.md'
    if not p.exists():
        p.write_text(
            f'# Informe de pruebas · ASIR2-SRI-texto · v{newv}\n\n'
            '## Estado\n\n'
            'Release preparada; completar el resultado real de los gates A/B/C/D.\n\n'
            '## Gates\n\n'
            '- A · editorial/estructural\n'
            '- B · didáctico/pedagógico\n'
            '- C · sintaxis/configuración\n'
            '- D · ejecución cuando exista infraestructura disponible\n\n'
            '> No se marca como ejecutada ninguna prueba que no se haya ejecutado realmente.\n',
            encoding='utf-8')


def bump(newv: str, dry=False):
    if not re.fullmatch(r'\d+\.\d+', newv):
        raise SystemExit('Versión esperada MAJOR.MINOR')
    old = version()
    if dry:
        print(f'dry-run: {old} -> {newv}')
        return
    if newv == old:
        raise SystemExit('La nueva versión debe ser distinta de la actual')
    (ROOT/'VERSION').write_text(newv+'\n', encoding='utf-8')
    for name in ['README.md','CHANGELOG.md']:
        p = ROOT/name
        s = read(p).replace(f'v{old}', f'v{newv}').replace(f'Versión {old}', f'Versión {newv}')
        p.write_text(s, encoding='utf-8')
    p = ROOT/'CITATION.cff'
    s = read(p)
    s = re.sub(r'^version: ".*"$', f'version: "{newv}"', s, flags=re.M)
    s = re.sub(r'^date-released: .*$', f'date-released: {dt.date.today().isoformat()}', s, flags=re.M)
    p.write_text(s, encoding='utf-8')
    p = ROOT/'CHANGELOG.md'
    s = read(p)
    if not re.search(rf'^## v{re.escape(newv)}', s, re.M):
        p.write_text(f'## v{newv} · nueva iteración\n\n- Revisar fuentes, calidad, prácticas y pruebas.\n\n'+s, encoding='utf-8')
    new_report(newv)
    print(f'bump: {old} -> {newv}')


def package():
    if not check(verbose=True):
        raise SystemExit('No se empaqueta: el quality gate ha fallado.')
    v = version()
    out = ROOT.parent / f'ASIR2-SRI-texto-v{v}.zip'
    if out.exists():
        out.unlink()
    with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as z:
        for p in sorted(ROOT.rglob('*')):
            if p.is_file() and '__pycache__' not in p.parts and not p.name.endswith('.zip'):
                z.write(p, p.relative_to(ROOT.parent))
    print(f'ZIP: {out}')
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    ap.add_argument('--bump')
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--package', action='store_true')
    ns = ap.parse_args()
    ok = True
    if ns.bump:
        bump(ns.bump, ns.dry_run)
    if ns.check:
        ok = check()
    if ns.package:
        package()
    if not (ns.bump or ns.check or ns.package):
        ap.print_help()
        return 2
    return 0 if ok else 1

if __name__ == '__main__':
    sys.exit(main())
