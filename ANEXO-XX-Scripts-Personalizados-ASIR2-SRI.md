# Anexo XX · Scripts personalizados de ASIR2-SRI

## 1. Propósito y criterio de integración

El repositorio complementario **ASIR2-SRI** mantiene un directorio `scripts/` destinado a **utilidades y automatización**. Este anexo no pretende convertir el material en un catálogo genérico de Git: parte de varios recursos concretos del directorio y explica cómo integrarlos de forma útil en un puesto Linux/WSL y en PowerShell.

Fuente de los scripts:

`https://github.com/glopezca/ASIR2-SRI/tree/main/scripts`

El repositorio identifica `scripts/` como espacio de utilidades y automatización. Antes de instalar o automatizar cualquier script hay que leerlo y comprobar qué modifica. La automatización debe ser el último paso, no el primero.

> **Idea guía:** un script puede vivir en `~/scripts` y estar disponible como cualquier otro comando, pero eso no significa que deba ejecutarse automáticamente al iniciar una sesión. Son dos decisiones distintas: **hacerlo accesible** y **hacerlo persistente**.

---

## 2. El modelo mental: tres piezas diferentes

Para integrar correctamente los recursos conviene separar tres conceptos:

```text
                 ~/scripts/
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
       apt.sh     prompt.sh   otros scripts
          │          │
          │          └── modifica el entorno de la shell
          │              → debe cargarse en la shell padre
          │
          └── se ejecuta como programa
              → basta con encontrarlo en PATH

                     │
                     ▼
            persistencia de sesión
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
      .profile /             $PROFILE
       .bashrc              PowerShell
```

Esto permite entender una diferencia especialmente importante:

- **Un programa ejecutable** (`apt.sh`) puede localizarse mediante `PATH` y ejecutarse como comando.
- **Una función, alias o configuración de prompt** necesita modificar el entorno de la shell actual; por ello normalmente debe **cargarse** (*source* / *dot-sourcing*) en esa shell.
- **La persistencia** se consigue haciendo que esa configuración se vuelva a cargar al iniciar una nueva sesión.

---

# 3. `apt.sh`: convertir un script en un comando del sistema

## 3.1. ¿Para qué sirve `apt.sh`?

`apt.sh` es un ejemplo de script de automatización para las tareas habituales relacionadas con **APT**, el sistema de gestión de paquetes de Debian/Ubuntu.

Pedagógicamente interesa porque permite pasar de una secuencia repetitiva de comandos a una herramienta propia:

```text
apt update
apt upgrade / install ...
        ↓
     apt.sh
        ↓
   una orden reutilizable
```

El objetivo no es ocultar `apt`, sino **encapsular una operación repetitiva** y aprender cómo un administrador convierte varios comandos en una herramienta ejecutable.

> ⚠️ Antes de utilizar el script hay que abrirlo y comprobar exactamente qué operaciones APT realiza. Un script que contiene `sudo apt ...` puede instalar, actualizar o eliminar software y, por tanto, tiene efectos sobre el sistema.

Consulta el contenido real de la versión disponible:

```bash
less ~/scripts/apt.sh
```

o:

```bash
sed -n '1,240p' ~/scripts/apt.sh
```

---

## 3.2. Instalar los scripts en `~/scripts`

Proponemos una ubicación sencilla y común para el laboratorio:

```text
/home/alumno/scripts/
```

que se expresa en Bash como:

```bash
~/scripts/
```

Por ejemplo, si hemos descargado el repositorio:

```bash
mkdir -p ~/scripts
cp ASIR2-SRI/scripts/apt.sh ~/scripts/
```

También podemos trabajar directamente con el directorio versionado, pero separar los scripts que queremos utilizar de forma cotidiana facilita el ejercicio y permite que `~/scripts` sea nuestra carpeta personal de herramientas.

Comprobar:

```bash
ls -la ~/scripts
```

---

## 3.3. El `shebang`: quién debe interpretar el script

Primero debemos mirar la primera línea:

```bash
head -n 1 ~/scripts/apt.sh
```

Por ejemplo:

```bash
#!/usr/bin/env bash
```

o:

```bash
#!/bin/bash
```

Esta línea, denominada **shebang**, indica qué intérprete debe utilizar el sistema cuando el fichero se ejecuta directamente.

### Sin permiso de ejecución

Podemos invocarlo explícitamente con el intérprete:

```bash
bash ~/scripts/apt.sh
```

Aquí somos nosotros quienes decimos: «ejecútalo con Bash».

### Con permiso de ejecución

Una vez revisado el script:

```bash
chmod +x ~/scripts/apt.sh
```

podemos ejecutarlo directamente:

```bash
~/scripts/apt.sh
```

En este segundo caso, el sistema utiliza el **shebang** para seleccionar el intérprete.

### ¿Por qué importa `chmod +x`?

Porque queremos que `apt.sh` sea tratado como **programa ejecutable**, no como un fichero de texto que debemos pasar manualmente a `bash`.

La diferencia conceptual es:

```text
bash apt.sh
   │
   └── el administrador elige Bash

./apt.sh
   │
   └── el fichero indica su intérprete mediante el shebang
```

Esto también hace visible una buena práctica: **no utilizar `chmod +x` a ciegas**. Primero se inspecciona el contenido y el shebang; después se concede el permiso que necesita.

Comprobar permisos:

```bash
ls -l ~/scripts/apt.sh
```

Deberíamos ver una `x` entre los permisos del propietario/grupo/otros según el `chmod` aplicado.

---

# 4. Hacer `~/scripts` accesible mediante `PATH`

Aunque `apt.sh` sea ejecutable, todavía tendríamos que escribir:

```bash
~/scripts/apt.sh
```

Queremos poder escribir simplemente:

```bash
apt.sh
```

Para ello añadimos la carpeta al `PATH`.

## 4.1. Prueba temporal

Antes de modificar ningún fichero de configuración, probamos:

```bash
export PATH="$HOME/scripts:$PATH"
```

Comprobar:

```bash
echo "$PATH"
command -v apt.sh
```

Si todo está correcto:

```bash
apt.sh
```

> **Nota:** es preferible utilizar `$HOME/scripts` en la asignación de `PATH` frente a escribir literalmente `~/scripts`. Así evitamos depender de la expansión de `~` en contextos donde no se produce.

---

## 4.2. Hacerlo persistente con `.profile`

La variable `PATH` es una **variable de entorno**. Para que la modificación sobreviva al cierre de la terminal debemos establecerla en un fichero de inicio de la shell.

En Ubuntu, una opción apropiada para esta configuración general es `~/.profile`.

Editar:

```bash
nano ~/.profile
```

Añadir:

**Importante:** usa `$HOME/scripts` en la configuración del `PATH`. La versión que se recomienda copiar es:

```bash
# Scripts personales
if [ -d "$HOME/scripts" ]; then
    case ":$PATH:" in
        *:"$HOME/scripts":*) ;;
        *) PATH="$HOME/scripts:$PATH" ;;
    esac
fi
export PATH
```

Recargar sin cerrar la terminal:

```bash
source ~/.profile
```

Comprobar:

```bash
command -v apt.sh
```

Abrir una terminal nueva y repetir la prueba. Esta segunda comprobación es importante: demuestra que la configuración es realmente **persistente**.

---

## 4.3. `.profile` o `.bashrc`: ¿dónde lo ponemos?

No conviene añadir indiscriminadamente el mismo bloque a ambos ficheros.

Como regla práctica:

| Fichero | Uso recomendado |
|---|---|
| `~/.profile` | variables de entorno como `PATH` y configuración de inicio de sesión |
| `~/.bashrc` | aliases, funciones y comportamiento específico de Bash interactivo |

En Ubuntu, `.profile` suele encargarse de la configuración del entorno y puede cargar `.bashrc` para una sesión Bash interactiva. Por ello, para `PATH` es suficiente con una configuración bien hecha en `.profile`.

---

# 5. Scripts de prompt en Linux

Los scripts relacionados con el **prompt** son diferentes de `apt.sh`.

Un prompt puede utilizar, entre otros mecanismos:

- `PS1`;
- `PROMPT_COMMAND`;
- funciones Bash;
- variables de entorno;
- información dinámica como usuario, host, directorio, rama Git o estado de salida.

Por eso no debemos tratarlos como un simple ejecutable.

## 5.1. Colocarlos en `~/scripts`

Por ejemplo:

```bash
cp ASIR2-SRI/scripts/NOMBRE_PROMPT.sh ~/scripts/
```

Si además queremos poder ejecutarlo directamente como programa, y su shebang lo permite:

```bash
chmod +x ~/scripts/NOMBRE_PROMPT.sh
```

**Matiz importante:** para `source ~/scripts/NOMBRE_PROMPT.sh` el permiso `+x` no es necesario, porque no estamos ejecutando el fichero como programa; lo estamos cargando desde Bash. Se puede mantener por coherencia si el mismo script también admite ejecución directa, pero no debe confundirse una cosa con la otra.

Comprobar:

```bash
head -n 5 ~/scripts/NOMBRE_PROMPT.sh
```

La extensión `.sh` no es lo que determina cómo se integra. Lo importante es **qué hace el script**.

---

## 5.2. Ejecutarlo no siempre significa cambiar el prompt

Esta es una de las ideas pedagógicas fundamentales del anexo.

Si hacemos:

```bash
~/scripts/NOMBRE_PROMPT.sh
```

el script se ejecuta en un proceso de shell separado. Si dentro modifica:

```bash
PS1='...'
```

esa modificación puede desaparecer cuando termina el proceso.

Para que una función, variable o configuración definida por el script quede en la **shell actual**, normalmente debemos cargarlo:

```bash
source ~/scripts/NOMBRE_PROMPT.sh
```

o equivalentemente:

```bash
. ~/scripts/NOMBRE_PROMPT.sh
```

Esto se denomina **sourcear** el script.

> **Regla:** `apt.sh` normalmente se ejecuta; un script que define el prompt normalmente se **carga**.

---

## 5.3. Hacer persistente el prompt Linux

Si hemos comprobado que el script funciona:

```bash
source ~/scripts/NOMBRE_PROMPT.sh
```

podemos integrarlo en `~/.bashrc`.

```bash
if [ -f "$HOME/scripts/NOMBRE_PROMPT.sh" ]; then
    source "$HOME/scripts/NOMBRE_PROMPT.sh"
fi
```

Después:

```bash
source ~/.bashrc
```

Y finalmente debemos abrir una **nueva terminal** para comprobar que el cambio se carga automáticamente.

### ¿Por qué `.bashrc`?

Porque el prompt es una característica de la **shell interactiva Bash**. No es necesario cargarlo en `.profile` si únicamente afecta al funcionamiento interactivo de Bash.

---

# 6. Scripts de prompt en PowerShell

PowerShell utiliza un mecanismo diferente. El prompt se puede personalizar mediante una función denominada `prompt` y el perfil de PowerShell proporciona el punto de carga persistente.

## 6.1. Colocar el script

Por ejemplo:

```powershell
New-Item -ItemType Directory -Path "$HOME\scripts" -Force | Out-Null
Copy-Item .\scripts\NOMBRE_PROMPT.ps1 "$HOME\scripts\"
```

Comprobar:

```powershell
Get-Content "$HOME\scripts\NOMBRE_PROMPT.ps1"
```

---

## 6.2. Execution Policy

Antes de ejecutar un `.ps1` debemos conocer la política efectiva:

```powershell
Get-ExecutionPolicy -List
```

En un equipo personal/laboratorio, y solo si las políticas superiores lo permiten, puede utilizarse para el ámbito del usuario:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

No se debe presentar `Unrestricted` o `Bypass` como solución habitual. Si existe una política establecida por `MachinePolicy` o `UserPolicy`, esa política tiene prioridad.

Si el archivo ha sido marcado como procedente de Internet y ya hemos revisado su contenido y procedencia:

```powershell
Unblock-File "$HOME\scripts\NOMBRE_PROMPT.ps1"
```

---

## 6.3. El perfil `$PROFILE`

Localizar el perfil:

```powershell
$PROFILE
```

Comprobar si existe:

```powershell
Test-Path $PROFILE
```

Crear el directorio y el fichero si es necesario:

```powershell
New-Item -ItemType Directory -Path (Split-Path $PROFILE) -Force | Out-Null
New-Item -ItemType File -Path $PROFILE -Force | Out-Null
```

Abrirlo:

```powershell
notepad $PROFILE
```

---

## 6.4. Cargar el prompt de forma persistente

Si el script está diseñado para definir una función `prompt`, lo adecuado es **dot-sourcearlo**:

```powershell
. "$HOME\scripts\NOMBRE_PROMPT.ps1"
```

El punto inicial es significativo: carga el script en el ámbito de la sesión actual.

En `$PROFILE` podemos proteger la carga:

```powershell
if (Test-Path "$HOME\scripts\NOMBRE_PROMPT.ps1") {
    . "$HOME\scripts\NOMBRE_PROMPT.ps1"
}
```

Después de guardar:

```powershell
. $PROFILE
```

Abrir una nueva sesión de PowerShell y comprobar que el prompt continúa funcionando.

### Diferencia esencial

```powershell
& "$HOME\scripts\NOMBRE_PROMPT.ps1"
```

Ejecuta el script como comando.

```powershell
. "$HOME\scripts\NOMBRE_PROMPT.ps1"
```

Carga sus definiciones en la sesión actual.

Para un script cuyo objetivo es **definir/modificar el prompt**, normalmente necesitamos la segunda opción.

---

# 7. Ayuda adicional: `bat` / `batcat`

Otro recurso interesante para personalizar el puesto es **bat**, una alternativa enriquecida a `cat` que añade resaltado de sintaxis, números de línea y otras funciones de lectura.

En Debian/Ubuntu el ejecutable puede instalarse con el nombre de paquete `bat` pero exponerse como `batcat`.

Instalación:

```bash
sudo apt update
sudo apt install bat
```

Comprobar:

```bash
command -v batcat
batcat --version
```

---

## 7.1. No sustituir `cat` directamente: crear un alias

La forma pedagógicamente más limpia de experimentar es crear un **alias de usuario**, no reemplazar el binario del sistema.

Probar primero en la sesión actual:

```bash
alias cat='batcat'
```

Ahora:

```bash
cat /etc/hosts
```

utilizará `batcat`.

Comprobar el alias:

```bash
type cat
```

---

## 7.2. Hacer persistente el alias

Como es un comportamiento específico de una sesión interactiva Bash, podemos colocarlo en `~/.bashrc`:

```bash
alias cat='batcat'
```

Recargar:

```bash
source ~/.bashrc
```

Y comprobar:

```bash
type cat
cat /etc/hosts
```

### ¿Qué hemos aprendido?

```text
cat original
     │
     ▼
 alias cat='batcat'
     │
     ▼
 misma orden escrita por el usuario
     │
     ▼
 herramienta enriquecida
```

El binario `cat` **no se ha sustituido**. Solo hemos cambiado la resolución del comando en nuestra shell.

> **Buena práctica:** si necesitamos el comportamiento original sin eliminar el alias, podemos utilizar una ruta explícita al binario o retirar temporalmente el alias con `unalias cat`.

---

# 8. Integración recomendada del puesto Linux

Una configuración sencilla y mantenible podría quedar así:

```text
$HOME/
├── scripts/
│   ├── apt.sh
│   ├── <script-prompt-linux>.sh
│   └── ...
├── .profile       → PATH=$HOME/scripts:$PATH
└── .bashrc        → prompt + aliases
```

### `~/.profile`

```bash
# Scripts personales
if [ -d "$HOME/scripts" ]; then
    case ":$PATH:" in
        *:"$HOME/scripts":*) ;;
        *) PATH="$HOME/scripts:$PATH" ;;
    esac
fi
export PATH
```

### `~/.bashrc`

```bash
# Prompt personalizado
if [ -f "$HOME/scripts/NOMBRE_PROMPT.sh" ]; then
    source "$HOME/scripts/NOMBRE_PROMPT.sh"
fi

# cat enriquecido con bat
if command -v batcat >/dev/null 2>&1; then
    alias cat='batcat'
fi
```

La comprobación `command -v batcat` evita introducir un alias roto si `bat` no está instalado.

---

# 9. Integración recomendada en PowerShell

```text
$HOME\
└── scripts\
    └── <script-prompt>.ps1

$PROFILE
└── carga el script de prompt
```

En `$PROFILE`:

```powershell
if (Test-Path "$HOME\scripts\NOMBRE_PROMPT.ps1") {
    . "$HOME\scripts\NOMBRE_PROMPT.ps1"
}
```

Este modelo mantiene separados:

- el **script versionado**;
- el **perfil personal**;
- la decisión de cargarlo automáticamente.

Los perfiles de PowerShell están diseñados precisamente para personalizar el entorno de una sesión y se consultan mediante `$PROFILE`.

---

# 10. Git: generalización y mantenimiento de la solución

Una vez comprendido el caso concreto de `apt.sh`, los prompts y `batcat`, podemos generalizar el modelo con Git.

El repositorio original debe ser la **fuente versionada** de los scripts:

```text
repositorio Git
      │
      └── scripts/
             │
             ├── apt.sh
             ├── prompt Linux
             └── prompt PowerShell

                 ↓ instalación/selección

          $HOME/scripts/
                 │
        ┌────────┴────────┐
        ▼                 ▼
     .profile          .bashrc / $PROFILE
```

Clonar:

```bash
git clone https://github.com/glopezca/ASIR2-SRI.git
```

Actualizar:

```bash
git pull --ff-only
```

Antes de adoptar cambios:

```bash
git diff
```

La idea importante es que **Git versiona el recurso; el perfil decide cómo se integra en cada máquina**.

No conviene modificar el script del repositorio para introducir preferencias personales que pertenecen al usuario. Es mejor mantenerlas en `.profile`, `.bashrc` o `$PROFILE`.

---

# 11. Aplicación al laboratorio Tierra Media

Los scripts son una capa de automatización transversal a los tres entornos:

```text
                 TIERRA MEDIA
                      │
       ┌──────────────┼──────────────┐
       ▼              ▼              ▼
 Packet Tracer       WSL         VirtualBox
                                  │
                           Mordor · Gondor
                           Rohan · Lothlorien
                           Rivendel
```

Ejemplos pedagógicos:

- En **WSL**, `apt.sh` puede servir para automatizar la preparación de herramientas del alumno.
- En una VM Ubuntu, los scripts de prompt pueden mostrar de forma visible usuario, host, directorio o contexto Git.
- En **Mordor**, antes de automatizar tareas de administración, el alumno debe saber ejecutar manualmente `ip`, `ss`, `systemctl`, `journalctl`, `nft` y las herramientas propias de cada servicio.
- Un alias como `cat → batcat` mejora la lectura de configuraciones, pero **no sustituye** el conocimiento de `cat`, `less`, `grep`, `sed` y `awk`.

> **Regla pedagógica:** primero CLI y funcionamiento; después script; finalmente automatización persistente.

---

# 12. Práctica guiada: del script al entorno personal

### Nivel 1 · `apt.sh`

1. Localiza `apt.sh` en la fuente original.
2. Lee su contenido.
3. Identifica el shebang.
4. Explica qué operaciones APT realiza.
5. Copia el script a `~/scripts`.
6. Aplica `chmod +x`.
7. Añade `~/scripts` al `PATH` temporalmente.
8. Comprueba `command -v apt.sh`.
9. Ejecuta el script y registra el resultado.
10. Haz persistente el `PATH` en `.profile`.
11. Abre una nueva sesión y repite la prueba.

### Nivel 2 · Prompt Linux

1. Copia el script a `~/scripts`.
2. Lee su código.
3. Determina si define `PS1`, `PROMPT_COMMAND`, funciones u otras variables.
4. Prueba `source ~/scripts/NOMBRE_PROMPT.sh`.
5. Comprueba el efecto sobre la sesión actual.
6. Cárgalo desde `.bashrc`.
7. Abre una nueva terminal.
8. Explica por qué ejecutarlo con `./script.sh` no es equivalente a `source script.sh`.

### Nivel 3 · Prompt PowerShell

1. Copia el `.ps1` a `$HOME\scripts`.
2. Comprueba `Get-ExecutionPolicy -List`.
3. Revisa el script.
4. Prueba el *dot-sourcing*.
5. Integra la carga en `$PROFILE`.
6. Abre una nueva sesión.
7. Explica la diferencia entre `& script.ps1` y `. script.ps1`.

### Nivel 4 · `batcat`

1. Instala `bat`.
2. Comprueba `batcat`.
3. Crea temporalmente `alias cat='batcat'`.
4. Prueba con `/etc/hosts` y un fichero YAML.
5. Persiste el alias en `.bashrc`.
6. Ejecuta `type cat`.
7. Retira el alias con `unalias cat` y explica qué ha cambiado.

---

# 13. Checklist profesional

- [ ] He leído el script antes de ejecutarlo.
- [ ] Conozco su shebang.
- [ ] Sé si necesita privilegios.
- [ ] He usado `chmod +x` cuando corresponde.
- [ ] `~/scripts` está en `PATH` mediante `$HOME/scripts`.
- [ ] El `PATH` es persistente y no se duplica en cada sesión.
- [ ] Sé distinguir ejecutar un script de cargarlo en la shell actual.
- [ ] El prompt Linux se carga desde `.bashrc` cuando procede.
- [ ] El prompt PowerShell se carga desde `$PROFILE` cuando procede.
- [ ] No he usado `Unrestricted`/`Bypass` como solución rutinaria en PowerShell.
- [ ] `batcat` se integra mediante alias, no sustituyendo el binario del sistema.
- [ ] Sé deshacer cada personalización.
- [ ] Git mantiene la fuente versionada y el perfil mantiene la personalización local.

> **Idea final:** un administrador no memoriza solamente comandos. Aprende a convertir una herramienta en un recurso reutilizable, accesible, persistente y reversible sin perder de vista qué está haciendo realmente el sistema.

## Fuentes técnicas

- Repositorio de scripts de ASIR2-SRI: `https://github.com/glopezca/ASIR2-SRI/tree/main/scripts`
- Repositorio ASIR2-SRI: `https://github.com/glopezca/ASIR2-SRI`
- Microsoft Learn · perfiles de PowerShell: `https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_profiles`
- Microsoft Learn · políticas de ejecución: `https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_execution_policies`
- GNU Bash Reference Manual · Bash Startup Files: `https://www.gnu.org/software/bash/manual/html_node/Bash-Startup-Files.html`
- Debian/Ubuntu · paquete `bat` / ejecutable `batcat` (consultar el repositorio de paquetes de la distribución instalada).
