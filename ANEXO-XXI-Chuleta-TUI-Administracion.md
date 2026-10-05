# Anexo XXI · Chuleta de utilidades TUI para administración de sistemas

## 1. Qué es una TUI

Una **TUI (Terminal User Interface)** es una interfaz interactiva que funciona dentro de una terminal. Combina la eficiencia de la línea de comandos con una presentación dinámica basada en menús, paneles, tablas, árboles o indicadores.

Es especialmente útil en servidores donde no existe entorno gráfico o donde una administración remota mediante SSH resulta más eficiente que abrir una interfaz gráfica.

### Mapa mental

```text
                      TERMINAL
                          │
          ┌───────────────┼────────────────┐
          ▼               ▼                ▼
       comando           TUI          sesión remota
          │               │                │
          │        ┌──────┼──────┐         │
          │        ▼      ▼      ▼         │
          │     procesos discos red    SSH + TUI
          │        │      │      │         │
          └────────┴──────┴──────┴─────────┘
                         │
                         ▼
                    DIAGNÓSTICO
```

Una TUI no sustituye a las herramientas clásicas. Normalmente es una **capa visual sobre información que también puede consultarse mediante comandos**.

---

# 2. Tabla rápida

| Necesidad | Herramienta | Función principal | Local | SSH/remoto |
|---|---|---|---:|---:|
| Procesos y CPU/RAM | `btop` | Monitor interactivo del sistema | ✓ | ✓ |
| Procesos | `htop` | Procesos, señales y consumo | ✓ | ✓ |
| Salud global | `nmon` | CPU, memoria, disco, red y procesos | ✓ | ✓ |
| Árbol de directorios | `broot` | Navegación y búsqueda en árbol | ✓ | ✓ |
| Ficheros | `mc` | Gestor de ficheros de dos paneles | ✓ | ✓ |
| Uso de disco | `ncdu` | Analizador interactivo de espacio | ✓ | ✓ |
| Red | `nmtui` | Configuración de NetworkManager | ✓ | ✓* |
| Logs | `lnav` | Visualización y filtrado de logs | ✓ | ✓ |
| Contenedores Docker | `lazydocker` | Gestión/observación interactiva | ✓ | ✓ |
| Multiplexación | `tmux` | Mantener sesiones persistentes | ✓ | ✓ |
| Multiplexación sencilla | `byobu` | Interfaz sobre tmux/screen | ✓ | ✓ |

`*` En remoto, `nmtui` debe utilizarse con especial cuidado: cambiar la red de la propia interfaz SSH puede cortar la sesión.

---

# 3. Procesos: `btop` y `htop`

## 3.1. `btop`

Es una de las mejores opciones para una visión general interactiva:

```bash
btop
```

Permite observar, entre otros datos:

- CPU por núcleo;
- memoria y swap;
- procesos;
- consumo de red;
- discos;
- carga del sistema.

### Uso didáctico

Antes de iniciar un servicio:

```bash
btop
```

Después se observa cómo cambia el consumo al ejecutar una operación concreta.

### Relación con los comandos clásicos

```bash
ps aux
uptime
free -h
ip -s link
```

La TUI facilita la observación; los comandos permiten documentar resultados de forma reproducible.

---

## 3.2. `htop`

```bash
htop
```

Es especialmente útil para aprender la relación entre:

```text
proceso → PID → consumo → usuario → comando
```

Operaciones habituales dependen de la configuración y versión, pero suelen incluir:

- búsqueda de procesos;
- ordenación por CPU/RAM;
- selección de procesos;
- envío de señales;
- visualización jerárquica.

### Equivalentes CLI

```bash
ps aux --sort=-%cpu | head
ps aux --sort=-%mem | head
pgrep -a NOMBRE
kill PID
```

---

# 4. Árbol de procesos

Cuando se necesita comprender quién ha lanzado a quién:

```bash
pstree -ap
```

Ejemplo conceptual:

```text
systemd
 ├─ sshd
 │   └─ sshd
 │       └─ bash
 │           └─ btop
 ├─ systemd-resolved
 └─ docker
     ├─ containerd
     └─ dockerd
```

Esto es particularmente útil para explicar que **un servicio no es simplemente un proceso aislado**: puede existir una cadena de procesos y dependencias.

---

# 5. Servicios: `systemctl` + observación interactiva

`systemctl` no es una TUI, pero es la herramienta base para administrar servicios en sistemas `systemd`.

```bash
systemctl status ssh
systemctl is-active ssh
systemctl is-enabled ssh
```

Acciones:

```bash
sudo systemctl start SERVICIO
sudo systemctl stop SERVICIO
sudo systemctl restart SERVICIO
sudo systemctl reload SERVICIO
sudo systemctl enable SERVICIO
sudo systemctl disable SERVICIO
```

### Diagnóstico

```bash
systemctl status SERVICIO --no-pager
journalctl -u SERVICIO -b --no-pager
```

Para una visualización interactiva de logs:

```bash
journalctl -u SERVICIO -f
```

O con `lnav` cuando se trabaja con ficheros de log compatibles.

### Idea clave

```text
systemctl → controla el servicio
journalctl → explica qué ha ocurrido
btop/htop → muestra el proceso
ss → muestra los sockets
curl/dig/nc → prueba el servicio desde el exterior
```

Esta secuencia es excelente para diagnóstico en SRI.

---

# 6. Logs: `lnav`

`lnav` es un visor interactivo de logs desde terminal.

Ejemplo:

```bash
lnav /var/log/
```

Para un servicio concreto puede ser más apropiado utilizar directamente `journalctl` si el servicio registra mediante `systemd-journald`:

```bash
journalctl -u nginx
journalctl -u bind9
journalctl -u ssh
```

### Principio de diagnóstico

No basta con mirar el mensaje de error. Hay que relacionarlo con:

```text
estado del servicio
       ↓
proceso
       ↓
puerto
       ↓
configuración
       ↓
log
       ↓
prueba desde cliente
```

---

# 7. Árboles y navegación de directorios: `broot`

`broot` permite explorar árboles de directorios de forma interactiva.

```bash
broot
```

Es útil para comprender estructuras como:

```text
/etc
├── bind
├── nginx
├── ssh
├── systemd
└── netplan
```

En SRI resulta especialmente útil para localizar rápidamente dónde viven las configuraciones.

### Alternativa universal

Si `broot` no está instalado:

```bash
tree -L 2 /etc
find /etc -maxdepth 2 -type f | sort
```

---

# 8. Gestor de ficheros: `mc`

`mc` (Midnight Commander) proporciona dos paneles de navegación:

```bash
mc
```

Es útil para:

- copiar/mover ficheros;
- comparar ubicaciones;
- explorar `/etc`;
- trabajar con ficheros remotos cuando se combina con mecanismos de acceso adecuados;
- realizar operaciones sin abandonar la terminal.

### Precaución

`mc` hace que operaciones destructivas sean cómodas. La facilidad de uso no elimina la necesidad de revisar destino y permisos antes de confirmar.

---

# 9. Uso de disco: `ncdu`

Para localizar qué está ocupando espacio:

```bash
ncdu /
```

En un servidor es habitual empezar por:

```bash
ncdu /var
ncdu /home
```

Antes de eliminar nada, identificar:

```text
qué ocupa espacio → por qué → si es necesario → si puede limpiarse
```

### Equivalentes

```bash
df -h
sudo du -xh /var | sort -h | tail
```

---

# 10. Red: `nmtui`

`nmtui` es una TUI de NetworkManager:

```bash
sudo nmtui
```

Permite gestionar conexiones, direcciones IP, gateways y DNS cuando NetworkManager es el gestor de red del sistema.

> **Importante para este laboratorio:** Ubuntu Server puede utilizar Netplan con `systemd-networkd` en lugar de NetworkManager. En ese caso, `nmtui` no es la herramienta principal.

Para nuestro laboratorio, la referencia conceptual sigue siendo:

```text
Netplan → backend de red → interfaces/rutas reales
```

Comprobaciones:

```bash
ip addr
ip route
resolvectl status
```

### Advertencia remota

Nunca se debe modificar la interfaz de la sesión SSH sin haber previsto cómo recuperar la conectividad. En una VM local el riesgo es menor; en un servidor remoto puede dejar al administrador sin acceso.

---

# 11. Contenedores: `lazydocker`

`lazydocker` ofrece una interfaz interactiva para observar y administrar Docker.

```bash
lazydocker
```

Permite visualizar de forma integrada:

```text
containers
   ├── estado
   ├── logs
   ├── CPU/RAM
   └── reinicio/parada

images
volumes
networks
```

### Equivalentes Docker CLI

```bash
docker ps
docker stats
docker logs CONTENEDOR
docker inspect CONTENEDOR
docker network ls
docker volume ls
```

### Relación con Docker Compose

Desde el directorio del proyecto:

```bash
docker compose ps
docker compose logs -f
docker compose up -d
docker compose down
```

La TUI no sustituye a Compose: facilita la observación y operación del despliegue.

---

# 12. Salud del sistema: `nmon`

`nmon` ofrece una vista interactiva de múltiples subsistemas:

```bash
nmon
```

Puede utilizarse para observar:

- CPU;
- memoria;
- discos;
- red;
- procesos;
- carga.

### Alternativas

```bash
uptime
free -h
vmstat 1
iostat
ip -s link
```

La elección depende de lo que se quiera demostrar.

---

# 13. Sesiones remotas: SSH + TUI

La arquitectura más habitual es:

```text
┌───────────────┐       SSH        ┌──────────────────┐
│ PC del técnico│ ───────────────> │ Servidor Ubuntu  │
│               │                  │                  │
│ terminal      │                  │ btop             │
│               │                  │ htop             │
│               │                  │ ncdu             │
│               │                  │ mc               │
│               │                  │ lazydocker       │
└───────────────┘                  └──────────────────┘
```

Conexión:

```bash
ssh usuario@servidor
```

Y, una vez dentro:

```bash
btop
```

También puede ejecutarse directamente:

```bash
ssh -t usuario@servidor btop
```

No todas las TUI funcionan correctamente en una ejecución remota de una sola orden; cuando la interfaz necesita una terminal completa, `ssh -t` ayuda a proporcionar un pseudo-terminal.

---

# 14. `tmux`: la herramienta imprescindible para administración remota

En una conexión SSH, si se cierra la sesión se puede perder el proceso interactivo. `tmux` permite mantener una sesión en el servidor:

```bash
tmux new -s sri
```

Dentro:

```bash
btop
```

Desconectar sin detenerla:

```text
Ctrl+b  d
```

Volver:

```bash
tmux attach -t sri
```

Listar sesiones:

```bash
tmux ls
```

### Esquema

```text
SSH
 │
 ▼
tmux
 ├── ventana 0 → btop
 ├── ventana 1 → journalctl
 └── ventana 2 → shell / pruebas
```

Esto resulta especialmente útil al administrar las VMs de Tierra Media.

---

# 15. `byobu`

`byobu` ofrece una interfaz más amigable sobre multiplexores de terminal:

```bash
byobu
```

Es una alternativa didáctica a aprender inicialmente toda la sintaxis de `tmux`.

En un servidor de prácticas puede utilizarse para mantener varias vistas simultáneas:

```text
ventana 1 → red
ventana 2 → servicio
ventana 3 → logs
ventana 4 → pruebas
```

---

# 16. Aplicación a Tierra Media

Las TUI deben encajar en la arquitectura del laboratorio, no crear una arquitectura paralela.

```text
                         MORDOR
                  router + servicios base
                         │
          ┌──────────────┼──────────────┐
          │              │              │
       GONDOR          ROHAN        LOTHLORIEN
       cliente         cliente      servicios
          │              │              │
          └──────────────┼──────────────┘
                         │
                      RIVENDEL
                       auxiliar
```

Ejemplos:

### Diagnosticar Lothlorien

```bash
ssh usuario@192.168.20.192
```

Después:

```bash
btop
systemctl status bind9
ss -lntup
journalctl -u bind9 -b
```

### Investigar espacio en disco

```bash
ssh usuario@192.168.20.192
ncdu /var
```

### Observar contenedores

En el servidor donde se ejecuta Docker:

```bash
ssh usuario@SERVIDOR
lazydocker
```

### Mantener una sesión de administración

```bash
ssh usuario@SERVIDOR
tmux new -s mantenimiento
```

---

# 17. Secuencia TUI para diagnóstico profesional

Cuando aparece una incidencia, no se debe abrir herramientas al azar.

```text
1. ¿Está vivo el sistema?
       ↓
   uptime / btop
       ↓
2. ¿Existe el proceso?
       ↓
   htop / pstree
       ↓
3. ¿Está activo el servicio?
       ↓
   systemctl status
       ↓
4. ¿Qué dice el log?
       ↓
   journalctl / lnav
       ↓
5. ¿Está escuchando?
       ↓
   ss -lntup
       ↓
6. ¿Hay conectividad?
       ↓
   ip route / ping / tracepath
       ↓
7. ¿Responde la aplicación?
       ↓
   curl / dig / nc / cliente específico
```

Esta secuencia conecta las TUI con la metodología de diagnóstico de las UT.

---

# 18. Instalación recomendada en Ubuntu

No todas las herramientas forman parte de una instalación mínima. Comprobar primero:

```bash
command -v btop htop nmon mc ncdu tmux byobu lnav nmtui
```

Instalar únicamente lo necesario y comprobar qué paquete proporciona cada herramienta:

```bash
apt-cache policy btop
apt-cache policy htop
apt-cache policy mc
apt-cache policy ncdu
apt-cache policy tmux
```

Después:

```bash
sudo apt update
sudo apt install btop htop mc ncdu tmux byobu lnav nmon
```

`broot` y `lazydocker` pueden requerir procedimientos de instalación específicos según la versión de Ubuntu y el método de distribución elegido. En un entorno docente se debe preferir el método documentado oficialmente por el proyecto y registrar la versión instalada.

---

# 19. Buenas prácticas

1. **No instalar herramientas porque sí.** Cada herramienta debe responder a una necesidad.
2. **No usar TUI como sustituto de conocimiento CLI.** El alumno debe saber qué información está viendo.
3. **No administrar remotamente una red sin una vía de recuperación.**
4. **Usar `tmux`/`byobu` para operaciones largas por SSH.**
5. **Documentar comandos reproducibles.** Una captura de `btop` no sustituye a una evidencia textual cuando se necesita reproducibilidad.
6. **Evitar privilegios innecesarios.** Usar `sudo` solo cuando la operación lo requiera.
7. **Comprobar la versión de la herramienta.** Las teclas y opciones pueden cambiar entre versiones.

---

# 20. Chuleta final

```text
PROCESOS       btop                 htop
ÁRBOL PROCESOS pstree -ap
SERVICIOS      systemctl status X
LOGS           journalctl -u X -b
LOGS TUI       lnav
ÁRBOL FICHEROS broot
FICHEROS       mc
DISCO          ncdu /
RED            nmtui / ip / ss
CONTENEDORES   lazydocker / docker ps
SALUD          nmon / btop
REMOTO         ssh usuario@host
PERSISTENCIA   tmux / byobu
```

### Regla de oro

> **La TUI mejora la observabilidad y la ergonomía; la CLI aporta reproducibilidad y automatización. Un administrador ASIR debe saber utilizar ambas.**


## 21. Fuentes y documentación de referencia

Para cada herramienta se recomienda consultar la documentación de la versión instalada (`man`, `--help` y documentación oficial). Como referencias generales:

- Ubuntu Server Documentation: `https://documentation.ubuntu.com/server/`
- systemd: `https://systemd.io/`
- tmux: `https://github.com/tmux/tmux`
- btop: `https://github.com/aristocratos/btop`
- Midnight Commander: `https://midnight-commander.org/`
- ncdu: `https://dev.yorhel.nl/ncdu`
- lazydocker: `https://github.com/jesseduffield/lazydocker`
