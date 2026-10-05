# Informe de integración · v6.5.8b

La v6.5.8b es una revisión de precisión de la v6.5.8. No cambia la arquitectura del laboratorio ni las UT; corrige el enfoque pedagógico del Anexo XX.

## Corrección principal

La versión anterior trataba los scripts de forma demasiado genérica. La nueva versión parte de los recursos concretos solicitados:

1. `apt.sh` como ejemplo de **programa ejecutable**.
2. Scripts de prompt Linux y PowerShell como ejemplos de **configuración que debe cargarse en la shell actual**.
3. `bat`/`batcat` como herramienta complementaria y alias persistente.
4. Git queda después como **generalización** para versionar los recursos sin mezclar el código con la configuración personal.

## Decisiones pedagógicas

- `PATH` se configura con `$HOME/scripts`, evitando depender de la expansión de `~`.
- La persistencia del `PATH` se sitúa en `.profile`.
- El comportamiento interactivo de Bash, como prompt y aliases, se sitúa en `.bashrc`.
- El prompt de PowerShell se integra mediante `$PROFILE`.
- Se explica por qué ejecutar un script de prompt como proceso hijo no equivale a `source`/dot-sourcing.
- `chmod +x` se vincula explícitamente con la ejecución directa y el `shebang`.
- `batcat` se integra mediante alias y no mediante sustitución del binario del sistema.
- Se mantiene una secuencia profesional: **inspeccionar → probar → integrar → persistir → verificar → revertir**.

## Continuidad

Se conservan la arquitectura Tierra Media, las cinco VMs, los tres entornos principales, Docker Compose como extensión y los anexos XX/XXI de la v6.5.8.

## 6. v6.5.8b · Reorganización de TUI

La revisión detectó que `systemctl` aparecía en una chuleta cuyo objeto es explicar TUIs. Se corrige la clasificación: `systemctl` y `journalctl` se consolidan en el Anexo XVIII como herramientas CLI de administración de `systemd`.

El Anexo XXI queda dedicado a interfaces de terminal interactivas y utilidades de observación/administración: `btop`, `htop`, `glances`, `nmon`, `iftop`, `bandwhich`, `nmtui`, `lazydocker`, `ctop`, `k9s`, `broot`, `mc`, `ncdu`, `lnav`, `lazygit`, `tmux` y `byobu`.

Se añaden ejemplos y pro tips y se incorporan cuatro infografías originales en castellano, inspiradas únicamente en la estructura divulgativa del material visual aportado por el usuario.
