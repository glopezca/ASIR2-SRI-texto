# Changelog · v6.5.8a

## Objetivo

Revisión de v6.5.8 centrada en corregir el enfoque del **Anexo XX · Scripts personalizados de ASIR2-SRI**.

## Cambios

- Replanteado el Anexo XX para partir de los scripts concretos solicitados: `apt.sh`, scripts de prompt para Linux y PowerShell y la ayuda `bat`/`batcat`.
- Explicado el objetivo de `apt.sh` y su modelo de integración como comando ejecutable.
- Añadida la instalación de los scripts en `~/scripts`.
- Explicada la incorporación persistente de `$HOME/scripts` al `PATH` mediante `~/.profile`.
- Explicado `chmod +x` y la relación entre permiso de ejecución y `shebang`.
- Diferenciado ejecutar un script de **cargarlo en la shell actual** mediante `source`/dot-sourcing.
- Explicada la persistencia de los prompts Linux mediante `~/.bashrc`.
- Explicada la persistencia de los prompts PowerShell mediante `$PROFILE`.
- Añadida la explicación de `Get-ExecutionPolicy`, `RemoteSigned` y `Unblock-File` sin convertir `Bypass`/`Unrestricted` en solución rutinaria.
- Añadida la instalación de `bat` y la variante `batcat` habitual en Debian/Ubuntu.
- Añadido el alias persistente `cat='batcat'`, explicando que no sustituye el binario del sistema.
- Conservado el material de Git, pero trasladado **después** del material concreto como generalización sobre versionado y personalización local.
- Actualizados README, índice, arquitectura e informes a v6.5.8a.
