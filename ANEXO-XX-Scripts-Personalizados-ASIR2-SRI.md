# Anexo XX · Scripts personalizados de ASIR2-SRI

## 1. Propósito

El repositorio complementario **ASIR2-SRI** mantiene un directorio `scripts/` destinado a **utilidades y automatización**. La fuente viva es:

`https://github.com/glopezca/ASIR2-SRI/tree/main/scripts`

Este anexo integra esos recursos en `ASIR2-SRI-texto` sin duplicar innecesariamente su código. El repositorio de scripts es la **fuente de verdad**; este documento explica cómo localizar, revisar, ejecutar e integrar los scripts en PowerShell y Bash.

> **Criterio de seguridad:** no se debe ejecutar un script simplemente porque proceda de GitHub. Primero se inspecciona, se entiende su finalidad, se prueban sus efectos y solo después se automatiza.

## 2. Localizar y revisar los scripts

Clonar el repositorio:

```bash
git clone https://github.com/glopezca/ASIR2-SRI.git
cd ASIR2-SRI
```

Inventariar ficheros:

```bash
find scripts -maxdepth 2 -type f -print | sort
```

En PowerShell:

```powershell
Get-ChildItem .\scripts -Recurse -File | Select-Object FullName
```

Revisar antes de ejecutar:

```bash
sed -n '1,240p' scripts/NOMBRE_DEL_SCRIPT.sh
```

```powershell
Get-Content .\scripts\NOMBRE_DEL_SCRIPT.ps1
```

Para cada script hay que poder contestar:

1. ¿Qué tarea automatiza?
2. ¿Qué parámetros recibe?
3. ¿Qué ficheros modifica?
4. ¿Qué servicios o procesos afecta?
5. ¿Necesita privilegios?
6. ¿Realiza conexiones de red?
7. ¿Es idempotente?
8. ¿Cómo se verifica el resultado?
9. ¿Cómo se revierte el cambio?

El README del repositorio describe `scripts/` como espacio de **utilidades y automatización**; este anexo evita inventar un catálogo estático de nombres que pueda quedar obsoleto. El inventario real debe obtenerse del directorio actual.

## 3. Bash: ejecución y permisos

Primera prueba, sin cambiar permisos:

```bash
bash scripts/NOMBRE_DEL_SCRIPT.sh
```

Comprobar el *shebang*:

```bash
head -n 1 scripts/NOMBRE_DEL_SCRIPT.sh
```

Si ya se ha revisado el contenido y se quiere ejecutar directamente:

```bash
chmod +x scripts/NOMBRE_DEL_SCRIPT.sh
./scripts/NOMBRE_DEL_SCRIPT.sh
```

Una organización limpia separa los scripts versionados de las personalizaciones del usuario:

```text
$HOME/
├── ASIR2-SRI/
│   └── scripts/       ← código versionado
├── bin/               ← herramientas personales seleccionadas
└── .profile
```

## 4. `.profile` frente a `.bashrc`

Regla práctica:

```text
.profile → variables de entorno y PATH
.bashrc  → aliases y funciones de la sesión interactiva
```

No se debe copiar el mismo bloque a ambos ficheros sin necesidad.

### Añadir `$HOME/bin` al PATH

En `.profile`:

```bash
if [ -d "$HOME/bin" ]; then
    case ":$PATH:" in
        *:"$HOME/bin":*) ;;
        *) PATH="$HOME/bin:$PATH" ;;
    esac
fi
export PATH
```

Recargar:

```bash
source ~/.profile
```

Comprobar:

```bash
echo "$PATH"
command -v NOMBRE_DEL_SCRIPT.sh
```

### Cargar funciones o aliases

Si un script está diseñado para definir funciones o aliases, puede cargarse en `.bashrc`:

```bash
if [ -f "$HOME/ASIR2-SRI/scripts/NOMBRE_DEL_SCRIPT.sh" ]; then
    source "$HOME/ASIR2-SRI/scripts/NOMBRE_DEL_SCRIPT.sh"
fi
```

**No** se debe hacer esto con un script que tenga efectos secundarios importantes al ser cargado. En ese caso se mantiene como comando explícito.

## 5. PowerShell: Execution Policy

Comprobar la política actual:

```powershell
Get-ExecutionPolicy
Get-ExecutionPolicy -List
```

Para un laboratorio de usuario, cuando la política corporativa lo permita, la opción habitual es:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Después:

```powershell
Get-ExecutionPolicy -List
```

### Qué no hacer

No se debe enseñar como solución permanente:

```powershell
Set-ExecutionPolicy Unrestricted
```

o ejecutar sistemáticamente con:

```powershell
-ExecutionPolicy Bypass
```

Si `MachinePolicy` o `UserPolicy` está definido por directiva de grupo, esa política puede tener prioridad y no debe intentarse eludir.

## 6. Scripts descargados: `Unblock-File`

Windows puede marcar los ficheros procedentes de Internet con información de zona. Comprobar:

```powershell
Get-Item .\scripts\NOMBRE_DEL_SCRIPT.ps1 -Stream Zone.Identifier -ErrorAction SilentlyContinue
```

Después de revisar el contenido y confirmar su procedencia:

```powershell
Unblock-File -Path .\scripts\NOMBRE_DEL_SCRIPT.ps1
```

Para varios scripts revisados:

```powershell
Get-ChildItem .\scripts -Recurse -File -Filter *.ps1 | Unblock-File
```

> **Desbloquear no equivale a validar.** Es una operación de confianza sobre un fichero que ya ha sido revisado.

## 7. Ejecutar scripts PowerShell

```powershell
.\scripts\NOMBRE_DEL_SCRIPT.ps1
```

Con parámetros:

```powershell
.\scripts\NOMBRE_DEL_SCRIPT.ps1 -Parametro Valor
```

Consultar ayuda, si existe:

```powershell
Get-Help .\scripts\NOMBRE_DEL_SCRIPT.ps1 -Full
Get-Command .\scripts\NOMBRE_DEL_SCRIPT.ps1 -Syntax
```

## 8. Integración en `$PROFILE`

Localizar el perfil:

```powershell
$PROFILE
Test-Path $PROFILE
```

Crear directorio y fichero si no existen:

```powershell
New-Item -ItemType Directory -Path (Split-Path $PROFILE) -Force | Out-Null
New-Item -ItemType File -Path $PROFILE -Force | Out-Null
```

Abrirlo:

```powershell
notepad $PROFILE
```

Si el script define funciones y está diseñado para ser *dot-sourced*:

```powershell
. "$HOME\ASIR2-SRI\scripts\NOMBRE_DEL_SCRIPT.ps1"
```

Si es un programa que debe ejecutarse al iniciar sesión:

```powershell
if (Test-Path "$HOME\ASIR2-SRI\scripts\NOMBRE_DEL_SCRIPT.ps1") {
    & "$HOME\ASIR2-SRI\scripts\NOMBRE_DEL_SCRIPT.ps1"
}
```

La diferencia es importante:

```text
. .\script.ps1  → ejecuta en el ámbito actual; puede dejar funciones/variables
& .\script.ps1  → ejecuta como comando
```

No se debe *dot-sourcear* indiscriminadamente cualquier script.

## 9. Integración profesional

El perfil del usuario debe contener **la mínima integración posible**. El código permanece en Git.

```text
repositorio Git
     │
     ├── scripts/       → código versionado
     │
     └── documentación

perfil del usuario
     │
     ├── PATH
     ├── aliases
     └── funciones/cargas seleccionadas
```

Para actualizar:

```bash
git pull --ff-only
git diff
```

Y en PowerShell:

```powershell
git pull --ff-only
git diff
```

Nunca se deben guardar preferencias personales modificando directamente el código versionado si pueden vivir en el perfil.

## 10. Aplicación a Tierra Media

Los scripts son una **capa de automatización**, no un cuarto entorno de prácticas.

```text
              LABORATORIO TIERRA MEDIA
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
    Packet Tracer     WSL       VirtualBox
                                     │
                              Mordor · Gondor
                              Rohan · Lothlorien
                              Rivendel
```

Su función pedagógica es automatizar tareas repetitivas y obtener evidencias. Por ejemplo, ante un problema en Lothlorien, primero se formula una hipótesis y después se utiliza el script para recoger estado, procesos, configuración o logs si el script correspondiente lo proporciona.

## 11. Práctica propuesta

### Nivel 1 · Inventario

1. Clona `ASIR2-SRI`.
2. Enumera `scripts/`.
3. Clasifica los scripts por extensión.
4. Selecciona uno.
5. Explica su función a partir de su código/documentación.

### Nivel 2 · Ejecución controlada

1. Ejecuta el script manualmente.
2. Registra la salida.
3. Identifica cambios en procesos, servicios, ficheros o variables.
4. Determina si necesita privilegios.

### Nivel 3 · Integración

1. Decide si corresponde a un alias, función o comando.
2. Integra solo lo necesario en `$PROFILE`, `.bashrc` o `.profile`.
3. Abre una nueva sesión.
4. Demuestra el resultado.

### Nivel 4 · Auditoría

Documenta:

- función;
- permisos;
- dependencias;
- efectos secundarios;
- evidencia de ejecución;
- actualización;
- procedimiento de reversión.

## 12. Checklist

- [ ] He localizado el script en la fuente original.
- [ ] He leído su contenido/documentación.
- [ ] Sé qué permisos necesita.
- [ ] Lo he ejecutado manualmente antes de automatizarlo.
- [ ] He comprobado sus efectos.
- [ ] He elegido correctamente entre alias, función y comando.
- [ ] He utilizado el perfil apropiado.
- [ ] No he desactivado globalmente la seguridad de PowerShell.
- [ ] Sé actualizar el script.
- [ ] Sé deshacer la integración.

> **Idea clave:** automatizar no significa dejar de comprender. El script reduce trabajo repetitivo y aumenta la reproducibilidad; la explicación técnica sigue siendo responsabilidad del administrador ASIR.


## 13. Fuentes técnicas recomendadas

- Repositorio de scripts de ASIR2-SRI: `https://github.com/glopezca/ASIR2-SRI/tree/main/scripts`
- Microsoft Learn · perfiles de PowerShell: `https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_profiles`
- Microsoft Learn · políticas de ejecución: `https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_execution_policies`
- GNU Bash Reference Manual · startup files: `https://www.gnu.org/software/bash/manual/html_node/Bash-Startup-Files.html`
