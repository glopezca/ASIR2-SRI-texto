# Changelog · v6.5.8a

## Cambios principales

### Anexo XX · Scripts personalizados

- Integración documental del directorio `scripts/` del repositorio complementario `ASIR2-SRI`.
- Explicación del flujo profesional: localizar → inspeccionar → probar → integrar → automatizar.
- Ejecución y permisos de scripts Bash.
- Diferenciación entre `.profile` y `.bashrc`.
- Integración mediante `$HOME/bin` y `PATH`.
- Explicación de `ExecutionPolicy`, `RemoteSigned`, ámbitos y precedencia en PowerShell.
- Uso de `Unblock-File` para scripts descargados, después de revisar su contenido.
- Uso de `$PROFILE`, `Get-Help`, `Get-Command` y *dot-sourcing*.
- Reglas para evitar que el perfil ejecute código con efectos secundarios no deseados.
- El anexo enlaza la fuente viva y evita duplicar un catálogo de scripts que pueda quedar obsoleto.

### Anexo XXI · Utilidades TUI

- Nueva chuleta de herramientas de terminal para administración local y remota.
- Procesos: `btop`, `htop`, `pstree`.
- Servicios y logs: `systemctl`, `journalctl`, `lnav`.
- Árboles y ficheros: `broot`, `mc`, `ncdu`.
- Red: `nmtui` y relación con Netplan.
- Contenedores: `lazydocker` y equivalentes Docker CLI/Compose.
- Salud del sistema: `nmon` y comandos equivalentes.
- Administración remota mediante SSH, `tmux` y `byobu`.
- Secuencia de diagnóstico TUI conectada con la metodología de las UT.
- Ejemplos aplicados a Mordor, Gondor, Rohan, Lothlorien y Rivendel.

### Navegación y mantenimiento

- README e índice general actualizados a v6.5.8a.
- Anexo XIX renombrado a la versión 6.5.8a.
- Referencias de arquitectura de las UT actualizadas a v6.5.8a.
- Se mantiene WSL como denominación canónica.
