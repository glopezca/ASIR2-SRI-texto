# Informe de pruebas · v6.5.8a

## Pruebas estructurales

- [x] README en v6.5.8a.
- [x] Índice general enlaza Anexos XX y XXI.
- [x] Anexo XIX actualizado a v6.5.8a.
- [x] Referencias de arquitectura de las UT actualizadas.
- [x] WSL utilizado como denominación canónica en los documentos activos.
- [x] Anexo XX presente.
- [x] Anexo XXI presente.
- [x] Changelog v6.5.8a presente.
- [x] Informe de integración v6.5.8a presente.

## Pruebas de contenido

- [x] PowerShell: `Get-ExecutionPolicy -List`.
- [x] PowerShell: `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`.
- [x] PowerShell: `$PROFILE` y creación del perfil.
- [x] PowerShell: `Unblock-File`.
- [x] Bash: `.profile` y `.bashrc`.
- [x] Bash: `PATH` y `$HOME/bin`.
- [x] TUI de procesos.
- [x] TUI/CLI de servicios y logs.
- [x] TUI de directorios y discos.
- [x] Red y precauciones con `nmtui`.
- [x] Contenedores Docker.
- [x] SSH + `tmux`/`byobu`.
- [x] Aplicación a Tierra Media.

## Validación de enlaces y sintaxis

La validación automática debe comprobar, como mínimo:

```bash
python3 tests/validate_material.py
```

y un chequeo de enlaces Markdown internos desde la raíz del repositorio.

## Límite de esta prueba

No se afirma que cada herramienta TUI haya sido ejecutada en una máquina real durante esta generación. La validación de ejecución (`btop`, `lazydocker`, `nmtui`, etc.) debe realizarse en el laboratorio con las versiones concretas instaladas.
