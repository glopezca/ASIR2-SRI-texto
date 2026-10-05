# Informe de integración · v6.5.8a

## Alcance

La v6.5.8a amplía la v6.5.7 mediante dos anexos orientados a la operación profesional del laboratorio:

1. **Anexo XX · Scripts personalizados de ASIR2-SRI**.
2. **Anexo XXI · Chuleta de utilidades TUI para administración de sistemas**.

## Anexo XX

La fuente original mantiene un directorio `scripts/` descrito por el propio repositorio como espacio de utilidades y automatización. La integración no copia indiscriminadamente su contenido: enlaza la fuente viva y documenta el procedimiento para inventariar, revisar, ejecutar y mantener los scripts.

Se cubren:

- Bash, permisos y ejecución.
- `.profile` y `.bashrc`.
- `PATH` y `$HOME/bin`.
- PowerShell `ExecutionPolicy`.
- `RemoteSigned` en `CurrentUser`.
- `Unblock-File`.
- `$PROFILE`.
- *dot-sourcing* frente a ejecución con `&`.
- actualización mediante Git.
- seguridad e idempotencia.

La documentación oficial de Microsoft confirma la existencia y función de `$PROFILE`, así como la precedencia de las políticas `MachinePolicy`, `UserPolicy`, `Process`, `CurrentUser` y `LocalMachine`. La documentación oficial de Bash explica el uso de `.profile` en shells de login y `.bashrc` en shells interactivos no-login.

## Anexo XXI

Se añade una chuleta TUI transversal para:

- procesos y consumo: `btop`, `htop`, `pstree`;
- servicios y logs: `systemctl`, `journalctl`, `lnav`;
- directorios y ficheros: `broot`, `mc`, `ncdu`;
- red: `nmtui`, `ip`, `ss`;
- contenedores: `lazydocker`, Docker CLI y Compose;
- salud del sistema: `nmon`;
- administración remota: SSH, `tmux`, `byobu`.

Se relacionan las herramientas con la metodología de diagnóstico de las UT y con el ecosistema Tierra Media.

## No regresión

- Se mantienen las tres plataformas principales: Packet Tracer, WSL y VirtualBox.
- Se mantienen las cinco VMs: Mordor, Gondor, Rohan, Lothlorien y Rivendel.
- Se mantiene Lothlorien como servidor principal y Rivendel como auxiliar.
- Se mantiene la continuidad de las ocho UT.
- El Anexo XIX continúa siendo la referencia arquitectónica común.

## Criterio de actualización

Los scripts externos se consideran una **fuente viva**. Si cambia su contenido, este anexo no necesita duplicar automáticamente el código: el alumno debe volver a inventariar y revisar la versión actual antes de incorporarla a su perfil.
