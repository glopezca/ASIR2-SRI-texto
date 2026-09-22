# 🐳 ANEXO II · Docker, Docker Compose y Kubernetes con WSL2

> **Entorno de trabajo:** Windows 11 + WSL2 + Ubuntu 26.04 + Docker Desktop + Visual Studio Code  
> **Nivel:** CFGS ASIR · Servicios en Red e Internet  
> **Propósito:** aprender a crear, ejecutar, inspeccionar, conectar, publicar, diagnosticar y orquestar servicios de red mediante contenedores.

---

## 🎯 0. Qué vamos a aprender

Al terminar este anexo deberás poder:

- explicar qué problema resuelve la contenerización;
- diferenciar **imagen, contenedor, volumen, red, servicio y registro**;
- instalar y comprobar Docker Desktop con backend WSL2;
- trabajar con Docker desde la terminal Linux y desde Docker Desktop;
- crear y administrar contenedores;
- entrar mediante **shell** en un contenedor y ejecutar comandos;
- entender la diferencia entre **puerto del proceso, puerto del contenedor y puerto publicado en el host**;
- crear redes Docker y hacer que los contenedores se encuentren por nombre;
- trabajar con volúmenes y bind mounts;
- construir imágenes mediante `Dockerfile`;
- definir infraestructuras multicontenedor mediante **Docker Compose**;
- comprender `ports`, `expose`, `volumes`, `networks`, `depends_on` y `healthcheck`;
- acceder a los servicios y a sus shells desde Compose;
- diagnosticar problemas de procesos, puertos, DNS y conectividad;
- comprender los conceptos de **cluster, node, Pod, Deployment y Service** en Kubernetes;
- crear, inspeccionar, conectar y eliminar Pods;
- utilizar `kubectl exec`, `kubectl logs` y `kubectl port-forward`;
- desplegar aplicaciones mediante manifiestos YAML;
- distinguir Docker Compose, Docker Swarm y Kubernetes;
- utilizar una colección de comandos de referencia durante las UT.

La filosofía será siempre:

```text
CONCEPTO
   ↓
COMANDO / CONFIGURACIÓN
   ↓
EXPERIMENTO
   ↓
OBSERVACIÓN
   ↓
DIAGNÓSTICO
   ↓
APLICACIÓN A SRI
```

---

# 🧭 1. La idea fundamental: infraestructura como software

En una infraestructura tradicional podemos tener:

```text
Servidor físico
 ├── sistema operativo
 ├── servidor web
 ├── DNS
 ├── correo
 └── otros servicios
```

La contenerización permite describir gran parte de esa infraestructura mediante código y ficheros reproducibles:

```text
compose.yaml
Dockerfile
config/
└── nginx.conf
```

y obtener:

```text
                    INFRAESTRUCTURA
                           │
                           ▼
                    docker compose up
                           │
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
       DNS/Web          correo          mensajería
       contenedor      contenedor       contenedor
```

Esto resulta especialmente interesante en ASIR porque transforma la administración de sistemas en una actividad parcialmente **declarativa, reproducible y versionable**.

---

# 🐳 2. ¿Qué es Docker?

Docker es una plataforma para desarrollar, distribuir y ejecutar aplicaciones mediante contenedores.

La idea esencial:

```text
APLICACIÓN
   +
DEPENDENCIAS
   +
CONFIGURACIÓN
   ↓
 IMAGEN
   ↓
CONTENEDOR
```

Una **imagen** es un artefacto inmutable que contiene el sistema de ficheros y metadatos necesarios para crear contenedores.

Un **contenedor** es una instancia ejecutable de una imagen.

No confundas:

```text
imagen       → plantilla
contenedor   → instancia en ejecución
```

Una imagen puede dar lugar a muchos contenedores:

```text
              nginx:latest
                   │
          ┌────────┼────────┐
          ▼        ▼        ▼
       web-01    web-02   web-03
```

---

# 🧱 3. Contenedor frente a máquina virtual

Una máquina virtual suele incluir un sistema operativo invitado completo:

```text
┌──────────── VM ────────────┐
│ Aplicación                │
│ Bibliotecas               │
│ Sistema operativo         │
│ Kernel virtualizado       │
└────────────────────────────┘
```

Un contenedor comparte el kernel del sistema operativo del entorno de ejecución:

```text
┌──────────── CONTENEDOR ────┐
│ Aplicación                │
│ Bibliotecas               │
│ Sistema de ficheros       │
└────────────────────────────┘
              │
              ▼
        kernel / runtime
```

Esto no significa que un contenedor sea simplemente un proceso normal sin aislamiento. Docker utiliza mecanismos de aislamiento y control de recursos proporcionados por el sistema operativo y el runtime.

### Regla mental

> Una VM virtualiza una máquina; un contenedor empaqueta y aísla un proceso y su entorno de ejecución.

---

# 🧩 4. Conceptos fundamentales de Docker

## 4.1 Imagen

```bash
docker image ls
```

## 4.2 Contenedor

```bash
docker ps
docker ps -a
```

## 4.3 Registro

Un **registry** almacena imágenes. Docker Hub es el registro público más conocido.

```text
Dockerfile
    ↓
docker build
    ↓
imagen
    ↓
docker push
    ↓
Registry
    ↓
docker pull
```

## 4.4 Volumen

Persistencia gestionada por Docker:

```text
contenedor
    │
    ▼
 volumen
    │
    ▼
datos persistentes
```

## 4.5 Red

Permite conectar contenedores y proporcionar resolución de nombres entre ellos.

## 4.6 Puerto

Un proceso dentro de un contenedor puede escuchar en un puerto, pero eso **no implica automáticamente** que sea accesible desde el host.

---

# 🪟 5. Entorno de trabajo: Windows + WSL2 + Docker Desktop

Para este material utilizaremos:

```text
┌────────────────────────────── Windows 11 ──────────────────────────────┐
│                                                                        │
│  Visual Studio Code                 Docker Desktop                     │
│       │                                  │                             │
│       │ WSL extension                    │ Docker Engine               │
│       ▼                                  │ Docker Compose               │
│  ┌──────────── WSL2 ────────────┐        │ Kubernetes (opcional)       │
│  │ Ubuntu 26.04                 │◄───────┘                             │
│  │                              │                                      │
│  │ código + Git + terminal      │                                      │
│  └──────────────────────────────┘                                      │
└────────────────────────────────────────────────────────────────────────┘
```

Docker Desktop puede utilizar WSL2 como backend en Windows y proporciona Docker Engine, CLI y Compose. La integración WSL permite ejecutar `docker` desde la distribución Linux integrada. [Documentación oficial: Docker Desktop + WSL2](https://docs.docker.com/desktop/features/wsl/)

## ⚠️ Una decisión importante: dónde guardar los proyectos

Para este curso trabajaremos preferentemente dentro del sistema de ficheros Linux de WSL2:

```text
/home/alumno/proyectos/
```

y no:

```text
/mnt/c/Users/alumno/proyectos/
```

En proyectos con muchos ficheros, trabajar en el sistema de archivos de WSL2 proporciona un mejor rendimiento de E/S. [Docker: desarrollo con WSL2](https://docs.docker.com/desktop/features/wsl/use-wsl/)

---

# 🛠️ 6. Instalación y comprobación

## 6.1 Comprobar WSL

Desde PowerShell:

```powershell
wsl --version
wsl --status
wsl --list --verbose
```

La distribución utilizada deberá aparecer con versión `2`.

## 6.2 Instalar Docker Desktop

Instala Docker Desktop para Windows y selecciona el backend WSL2 cuando corresponda.

Después:

```text
Docker Desktop
   ↓
Settings
   ↓
General
   ↓
Use WSL 2 based engine
```

Y:

```text
Settings
   ↓
Resources
   ↓
WSL Integration
   ↓
Ubuntu
   ✓
```

[Instalación oficial de Docker Desktop para Windows](https://docs.docker.com/desktop/setup/install/windows-install/)

## 6.3 Comprobar desde Ubuntu

```bash
docker version
docker info
docker compose version
```

Prueba:

```bash
docker run --rm hello-world
```

Si aparece el mensaje de bienvenida, tenemos una primera prueba funcional.

---

# 🖥️ 7. Docker Desktop y línea de comandos

Docker Desktop ofrece una interfaz gráfica para inspeccionar y administrar recursos.

La terminal es fundamental porque:

- es reproducible;
- permite automatizar;
- permite documentar procedimientos;
- funciona en servidores;
- es esencial para CI/CD;
- facilita el diagnóstico.

Usaremos ambas:

```text
Docker Desktop
     ↕
docker CLI
     ↕
Docker Engine
```

La GUI no sustituye a la CLI.

### Correspondencias habituales

| Terminal | Docker Desktop |
|---|---|
| `docker ps` | Containers |
| `docker image ls` | Images |
| `docker logs` | Logs |
| `docker inspect` | Inspect |
| `docker volume ls` | Volumes |
| `docker network ls` | Networks |

---

# 🐋 8. Primer contenedor: Nginx

Utilizaremos **Nginx como servidor web de referencia**.

No porque Apache sea inferior: ambos son servidores web maduros y ambos disponen de imágenes oficiales.

La elección es didáctica. Nginx permite pasar con facilidad de HTTP básico a:

- servidor de contenido estático;
- reverse proxy;
- proxy TCP/UDP;
- balanceo;
- TLS;
- redes de contenedores.

Esto resulta especialmente útil en SRI.

[Documentación oficial de Nginx](https://nginx.org/en/docs/)
[Docker Official Image de Nginx](https://hub.docker.com/_/nginx)
[Documentación oficial de Apache HTTP Server](https://httpd.apache.org/docs/)

---

## 8.1 Ejecutar Nginx

```bash
docker run -d --name web nginx
```

Comprobar:

```bash
docker ps
```

Todavía no podremos acceder desde el navegador mediante `localhost:8080`, porque no hemos publicado ningún puerto.

---

# 🔌 9. Puertos: una distinción fundamental

Hay que distinguir:

```text
1. Puerto donde escucha el proceso
2. Puerto del contenedor
3. Puerto publicado en el host
```

Por ejemplo:

```text
                 HOST
            TCP/8080
                │
                │ -p 8080:80
                ▼
        ┌─────────────────┐
        │   CONTENEDOR    │
        │                 │
        │    Nginx        │
        │    TCP/80       │
        └─────────────────┘
```

La opción:

```bash
-p 8080:80
```

significa:

```text
HOST:8080 → CONTENEDOR:80
```

No al revés.

---

# 🚪 10. Publicar un puerto

Eliminar el contenedor anterior:

```bash
docker rm -f web
```

Crear uno nuevo:

```bash
docker run -d \
  --name web \
  -p 8080:80 \
  nginx
```

Comprobar:

```bash
docker ps
docker port web
```

Probar:

```bash
curl http://localhost:8080
```

También:

```text
http://localhost:8080
```

desde el navegador.

## 10.1 Bind específico

Podemos limitar la publicación a localhost:

```bash
docker run -d \
  --name web \
  -p 127.0.0.1:8080:80 \
  nginx
```

Ahora el servicio no queda publicado directamente en todas las interfaces del host.

---

# 📦 11. `EXPOSE` no publica un puerto

En un `Dockerfile` podemos encontrar:

```dockerfile
EXPOSE 80
```

Esto documenta que el contenedor utiliza ese puerto, pero **no equivale a publicar el puerto en el host**.

Para publicar necesitamos, por ejemplo:

```bash
docker run -p 8080:80 nginx
```

---

# 🐚 12. Entrar mediante shell en un contenedor

Este apartado es esencial para ASIR.

```bash
docker exec -it web bash
```

Si la imagen no dispone de Bash:

```bash
docker exec -it web sh
```

Descomposición:

```text
docker
  └── exec
       ├── -i  → stdin interactivo
       ├── -t  → terminal
       ├── web → contenedor
       └── sh  → proceso que queremos ejecutar
```

Una vez dentro:

```bash
hostname
ps
ls -la
cat /etc/os-release
```

Salir:

```bash
exit
```

## 12.1 Ejecutar un único comando

No hace falta abrir una shell:

```bash
docker exec web hostname
docker exec web ls -la /etc/nginx
docker exec web nginx -t
```

## 12.2 `exec` frente a `attach`

```bash
docker exec -it web sh
```

ejecuta **un proceso nuevo** dentro del contenedor.

```bash
docker attach web
```

se conecta al proceso principal del contenedor.

Para administración y diagnóstico normal, `exec` suele ser la opción adecuada.

---

# 📜 13. Logs

```bash
docker logs web
```

Seguirlos:

```bash
docker logs -f web
```

Últimas líneas:

```bash
docker logs --tail 50 web
```

Desde el punto de vista de administración:

```text
servicio no responde
       ↓
docker ps
       ↓
docker logs
       ↓
docker inspect
       ↓
docker exec
```

---

# 🔎 14. Inspección

```bash
docker inspect web
```

Es especialmente útil para consultar:

- IP;
- redes;
- mounts;
- variables;
- configuración;
- estado;
- puertos.

Filtrar con Go templates:

```bash
docker inspect -f '{{.NetworkSettings.IPAddress}}' web
```

En redes modernas, para consultar la IP de una red concreta puede ser más útil:

```bash
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' web
```

---

# 📁 15. Copiar archivos

Host → contenedor:

```bash
docker cp index.html web:/usr/share/nginx/html/
```

Contenedor → host:

```bash
docker cp web:/etc/nginx/nginx.conf .
```

---

# 💾 16. Volúmenes y bind mounts

## 16.1 Volumen gestionado por Docker

```bash
docker volume create datos-web
docker volume ls
docker volume inspect datos-web
```

Usarlo:

```bash
docker run -d \
  --name web \
  -v datos-web:/usr/share/nginx/html \
  nginx
```

## 16.2 Bind mount

```bash
mkdir -p ~/sri/docker/web
echo '<h1>Hola ASIR</h1>' > ~/sri/docker/web/index.html
```

```bash
docker run -d \
  --name web \
  -p 8080:80 \
  -v ~/sri/docker/web:/usr/share/nginx/html:ro \
  nginx
```

Aquí:

```text
~/sri/docker/web
        │
        │ bind mount
        ▼
/usr/share/nginx/html
```

El modificador `:ro` hace que el montaje sea de solo lectura para el contenedor.

---

# 🌐 17. Redes Docker

Ver redes:

```bash
docker network ls
```

Crear:

```bash
docker network create red-sri
```

Inspeccionar:

```bash
docker network inspect red-sri
```

Crear un servidor:

```bash
docker run -d \
  --name web \
  --network red-sri \
  nginx
```

Crear un cliente:

```bash
docker run --rm -it \
  --network red-sri \
  alpine sh
```

Dentro del cliente:

```sh
wget -qO- http://web
```

La comunicación funciona aunque **no hayamos publicado el puerto 80 con `-p`**.

Esta distinción es fundamental:

```text
-p
 ↓
publicación hacia el host

network
 ↓
comunicación entre contenedores
```

---

# 🧭 18. DNS interno de Docker

En una red Docker definida por el usuario, los contenedores pueden localizarse por nombre.

```text
cliente
   │
   │ http://web
   ▼
DNS Docker
   │
   ▼
IP de web
```

Podemos comprobarlo:

```bash
docker exec cliente getent hosts web
```

o desde un contenedor temporal:

```bash
docker run --rm \
  --network red-sri \
  alpine getent hosts web
```

Esto constituye un puente directo con los contenidos de DNS de SRI.

---

# 🏗️ 19. Dockerfile

Un `Dockerfile` describe cómo construir una imagen.

Ejemplo:

```dockerfile
FROM nginx:alpine

COPY index.html /usr/share/nginx/html/index.html
```

Construcción:

```bash
docker build -t asir-web:1.0 .
```

Comprobar:

```bash
docker image ls
```

Ejecutar:

```bash
docker run -d \
  --name asir-web \
  -p 8080:80 \
  asir-web:1.0
```

La cadena conceptual es:

```text
Dockerfile
    ↓
docker build
    ↓
imagen
    ↓
docker run
    ↓
contenedor
```

---

# 🐙 20. Docker Compose: pasar de contenedores a infraestructura

Cuando tenemos varios servicios, ejecutar manualmente decenas de comandos deja de ser cómodo.

Compose permite describir la aplicación en un fichero:

```yaml
services:
  web:
    image: nginx
    ports:
      - "8080:80"

  cliente:
    image: alpine
```

y levantarla:

```bash
docker compose up -d
```

---

# 📄 21. `compose.yaml`

La especificación moderna de Compose no necesita una línea:

```yaml
version: "3"
```

Para nuestros ejemplos utilizaremos:

```yaml
services:
  web:
    image: nginx
```

La especificación actual integra los antiguos formatos Compose 2.x y 3.x.

[Compose Specification](https://docs.docker.com/reference/compose-file/)

---

# 🔌 22. `ports` en Docker Compose

```yaml
services:
  web:
    image: nginx
    ports:
      - "8080:80"
```

Interpretación:

```text
HOST                  CONTENEDOR
8080       ─────────► 80
```

Acceso:

```text
http://localhost:8080
```

Comprobar:

```bash
docker compose ps
```

y:

```bash
docker compose port web 80
```

---

# 🧩 23. `expose` frente a `ports`

Ejemplo:

```yaml
services:
  web:
    image: nginx
    expose:
      - "80"
```

`expose` no publica automáticamente el puerto en el host.

En cambio:

```yaml
ports:
  - "8080:80"
```

sí crea una publicación.

### Regla práctica

```text
ports
  → acceso desde fuera del entorno de red del servicio

expose
  → documentación/visibilidad del puerto para comunicación de servicios
```

No debe entenderse `expose` como un mecanismo de NAT equivalente a `ports`.

---

# 🔗 24. Comunicación entre servicios Compose

Ejemplo:

```yaml
services:

  web:
    image: nginx

  cliente:
    image: alpine
    command: ["sh", "-c", "sleep infinity"]
```

Levantar:

```bash
docker compose up -d
```

Entrar en cliente:

```bash
docker compose exec cliente sh
```

Probar:

```sh
wget -qO- http://web
```

El nombre:

```text
web
```

es el nombre DNS del servicio dentro de la red Compose.

No debemos utilizar la IP del contenedor en la configuración de la aplicación salvo que exista una razón concreta.

---

# 🐚 25. Shell mediante Docker Compose

```bash
docker compose exec web sh
```

Ejecutar comandos:

```bash
docker compose exec web nginx -t
docker compose exec web hostname
docker compose exec web ss -lnt
```

Comparación:

```bash
docker exec -it nombre-contenedor sh
```

frente a:

```bash
docker compose exec nombre-servicio sh
```

Compose permite trabajar con el **servicio**, sin tener que memorizar el nombre dinámico del contenedor.

---

# ⚠️ 26. `docker compose exec` frente a `docker compose run`

No son equivalentes.

### `exec`

Ejecuta un comando en un contenedor que ya está ejecutándose:

```bash
docker compose exec web sh
```

### `run`

Crea un contenedor puntual para ejecutar un comando:

```bash
docker compose run web sh
```

Por defecto, `run` no publica los puertos del servicio. Si los necesitamos:

```bash
docker compose run --service-ports web sh
```

---

# 🗃️ 27. Volúmenes en Compose

```yaml
services:
  web:
    image: nginx
    volumes:
      - ./web:/usr/share/nginx/html:ro
```

La relación:

```text
proyecto/
└── web/
    └── index.html
          │
          ▼
/usr/share/nginx/html
```

permite editar desde VS Code y observar el resultado inmediatamente.

---

# 🌐 28. Redes en Compose

Podemos declarar explícitamente:

```yaml
services:

  web:
    image: nginx
    networks:
      - frontend

  app:
    image: alpine
    networks:
      - frontend

networks:
  frontend:
```

Los servicios comparten la red:

```text
        frontend
       /        \
      /          \
    web          app
```

Si necesitamos varias redes:

```yaml
services:

  proxy:
    image: nginx
    networks:
      - frontend
      - backend

  app:
    image: alpine
    networks:
      - backend

networks:
  frontend:
  backend:
```

Esto permite introducir segmentación lógica:

```text
Internet
   │
   ▼
 proxy
  / \
 /   \
frontend backend
       │
       ▼
      app
```

---

# ❤️ 29. `depends_on` y `healthcheck`

No debemos confundir:

```yaml
depends_on:
```

con:

> "el servicio ya está preparado para recibir peticiones".

Podemos comprobar la salud de un servicio:

```yaml
services:

  web:
    image: nginx
    healthcheck:
      test: ["CMD", "nginx", "-t"]
      interval: 30s
      timeout: 5s
      retries: 3
```

El concepto:

```text
contenedor arrancado
       ≠
servicio preparado
```

es fundamental.

---

# 🧪 30. Proyecto Compose completo de iniciación

```yaml
services:

  web:
    image: nginx:alpine
    ports:
      - "8080:80"
    volumes:
      - ./html:/usr/share/nginx/html:ro
    networks:
      - frontend

  cliente:
    image: alpine
    command: ["sh", "-c", "sleep infinity"]
    networks:
      - frontend

networks:
  frontend:
```

Preparar:

```bash
mkdir -p docker-lab/html
cd docker-lab
echo '<h1>Laboratorio ASIR</h1>' > html/index.html
```

Levantar:

```bash
docker compose up -d
```

Comprobar:

```bash
docker compose ps
```

Acceder:

```text
http://localhost:8080
```

Entrar en el cliente:

```bash
docker compose exec cliente sh
```

Desde el cliente:

```sh
wget -qO- http://web
```

Salir:

```sh
exit
```

Logs:

```bash
docker compose logs -f web
```

Detener y eliminar:

```bash
docker compose down
```

---

# 🛠️ 31. Diagnóstico sistemático de Docker

Cuando algo falla, no debemos comenzar modificando cosas al azar.

## Paso 1: ¿existe?

```bash
docker ps -a
```

## Paso 2: ¿está ejecutándose?

```bash
docker ps
```

## Paso 3: ¿qué dicen los logs?

```bash
docker logs nombre
```

## Paso 4: ¿cómo está configurado?

```bash
docker inspect nombre
```

## Paso 5: ¿qué puertos publica?

```bash
docker port nombre
```

## Paso 6: ¿está escuchando?

```bash
docker exec nombre ss -lnt
```

## Paso 7: ¿está en la red adecuada?

```bash
docker network inspect red
```

## Paso 8: ¿resuelve el nombre?

```bash
docker exec cliente getent hosts web
```

## Paso 9: ¿responde?

```bash
docker exec cliente wget -qO- http://web
```

---

# 🧰 32. Navaja suiza de Docker

## Contenedores

```bash
docker run
docker create
docker start
docker stop
docker restart
docker pause
docker unpause
docker kill
docker rm
docker rename
docker update
docker wait
```

## Consulta

```bash
docker ps
docker ps -a
docker inspect
docker stats
docker top
docker port
docker logs
docker events
```

## Imágenes

```bash
docker image ls
docker image inspect
docker image rm
docker image prune
docker pull
docker push
docker tag
docker history
```

## Construcción

```bash
docker build
docker buildx build
```

## Redes

```bash
docker network ls
docker network create
docker network inspect
docker network connect
docker network disconnect
docker network rm
docker network prune
```

## Volúmenes

```bash
docker volume ls
docker volume create
docker volume inspect
docker volume rm
docker volume prune
```

## Sistema

```bash
docker info
docker version
docker system df
docker system prune
docker system events
```

## Contextos

```bash
docker context ls
docker context show
docker context inspect
docker context use
```

> ⚠️ `docker system prune` puede eliminar recursos que todavía necesites. No debe ejecutarse como una solución genérica a cualquier problema.

---

# 🐙 33. Navaja suiza de Docker Compose

```bash
docker compose up
docker compose down
docker compose start
docker compose stop
docker compose restart
docker compose ps
docker compose logs
docker compose exec
docker compose run
docker compose build
docker compose pull
docker compose push
docker compose config
docker compose cp
docker compose images
docker compose volumes
docker compose top
docker compose events
docker compose watch
```

Comandos imprescindibles:

```bash
docker compose up -d
docker compose ps
docker compose logs -f
docker compose exec servicio sh
docker compose config
docker compose down
```

Antes de levantar una infraestructura compleja:

```bash
docker compose config
```

es una excelente comprobación de la configuración resultante.

---

# ☸️ 34. De los contenedores a la orquestación

Hasta ahora:

```text
Docker
  └── contenedores
```

Con varios servicios:

```text
Docker Compose
  └── aplicación multicontenedor
```

Si necesitamos gestionar cargas de trabajo distribuidas entre múltiples máquinas:

```text
orquestación
     │
     ├── Docker Swarm
     │
     └── Kubernetes
```

---

# 🐝 35. Docker Swarm: introducción

Swarm permite agrupar Docker Engines en un cluster.

```text
              SWARM
                │
        ┌───────┴───────┐
        │               │
    manager           worker
        │               │
      tareas          tareas
```

Inicializar:

```bash
docker swarm init
```

Consultar:

```bash
docker node ls
```

Crear un servicio:

```bash
docker service create \
  --name web \
  --publish published=8080,target=80 \
  --replicas 3 \
  nginx
```

Consultar:

```bash
docker service ls
docker service ps web
```

Escalar:

```bash
docker service scale web=5
```

Eliminar:

```bash
docker service rm web
```

Swarm es útil para comprender el concepto de cluster Docker, pero en este curso el camino principal será Docker Compose y, como introducción a orquestación, Kubernetes.

---

# ☸️ 36. Kubernetes: modelo mental

Kubernetes introduce una jerarquía diferente:

```text
CLUSTER
│
├── CONTROL PLANE
│
└── NODES
    │
    ├── Pod
    │   └── Container
    │
    └── Pod
        ├── Container
        └── Container
```

## Cluster

Conjunto de recursos Kubernetes gestionados conjuntamente.

## Node

Máquina que ejecuta cargas de trabajo.

## Pod

Unidad desplegable mínima de Kubernetes.

Un Pod puede contener uno o varios contenedores que comparten red y almacenamiento.

```text
┌──────────── POD ────────────┐
│                             │
│  container A    container B │
│       │               │     │
│       └─────┬─────────┘     │
│             │               │
│        localhost            │
│                             │
└─────────────────────────────┘
```

Los contenedores de un mismo Pod comparten la red del Pod.

---

# 🧪 37. Kubernetes local

Para los ejercicios podemos utilizar un Kubernetes local proporcionado por Docker Desktop o Minikube.

Docker Desktop incorpora Kubernetes y permite activar el entorno desde su configuración. La alternativa Minikube proporciona un cluster Kubernetes local apropiado para aprendizaje.

El objetivo no es convertir este anexo en un curso completo de Kubernetes, sino proporcionar una base sólida para comprender Pods, Services, Deployments, puertos y administración mediante `kubectl`.

---

# 🏃 38. Crear un Pod

```bash
kubectl run nginx --image=nginx
```

Consultar:

```bash
kubectl get pods
```

Más información:

```bash
kubectl get pods -o wide
```

Detalles:

```bash
kubectl describe pod nginx
```

---

# 🐚 39. Entrar en un Pod

```bash
kubectl exec -it nginx -- /bin/bash
```

Si Bash no existe:

```bash
kubectl exec -it nginx -- /bin/sh
```

Ejecutar un único comando:

```bash
kubectl exec nginx -- hostname
```

Con varios contenedores:

```bash
kubectl exec -it nginx -c nombre-contenedor -- /bin/sh
```

La forma conceptual es muy parecida a Docker:

```text
Docker:
docker exec -it contenedor sh

Kubernetes:
kubectl exec -it pod -- sh
```

Pero no debemos concluir que un Pod sea simplemente "un contenedor Kubernetes".

---

# 📜 40. Logs de un Pod

```bash
kubectl logs nginx
```

Seguir:

```bash
kubectl logs -f nginx
```

Si existen varios contenedores:

```bash
kubectl logs nginx -c nombre-contenedor
```

Logs de la ejecución anterior:

```bash
kubectl logs nginx --previous
```

---

# 🗑️ 41. Eliminar un Pod

```bash
kubectl delete pod nginx
```

Comprobar:

```bash
kubectl get pods
```

Una idea fundamental:

```text
Pod creado directamente
        │
        └── delete
             ↓
          desaparece
```

Pero:

```text
Deployment
    │
    └── Pod
         │
         └── delete
              ↓
        Deployment detecta
        que falta una réplica
              ↓
        crea otro Pod
```

---

# 🚀 42. Deployment

Crear:

```bash
kubectl create deployment web --image=nginx
```

Consultar:

```bash
kubectl get deployments
kubectl get pods
```

Describir:

```bash
kubectl describe deployment web
```

Escalar:

```bash
kubectl scale deployment web --replicas=3
```

Actualizar imagen:

```bash
kubectl set image deployment/web nginx=nginx:alpine
```

Comprobar el rollout:

```bash
kubectl rollout status deployment/web
kubectl rollout history deployment/web
```

Deshacer:

```bash
kubectl rollout undo deployment/web
```

---

# 🔌 43. Puertos en Kubernetes

Hay que distinguir varios niveles.

```text
HOST
 │
 │ port-forward
 ▼
Service
 │
 │ port
 ▼
targetPort
 │
 ▼
Pod
 │
 ▼
Container
```

Conceptos habituales:

```text
containerPort
targetPort
port
nodePort
```

No son sinónimos.

---

# 🔗 44. Service

Crear un Service:

```bash
kubectl expose deployment web \
  --port=80 \
  --target-port=80
```

Consultar:

```bash
kubectl get services
kubectl describe service web
```

Conceptualmente:

```text
Service :80
     │
     │ selector
     ▼
Pods :80
```

El Service proporciona un punto de acceso estable aunque los Pods puedan cambiar.

---

# 🚪 45. `kubectl port-forward`

Acceso temporal desde nuestra máquina:

```bash
kubectl port-forward pod/nginx 8080:80
```

Ahora:

```text
localhost:8080
       │
       ▼
    Pod:80
```

También podemos hacerlo sobre un Service:

```bash
kubectl port-forward service/web 8080:80
```

o sobre un Deployment:

```bash
kubectl port-forward deployment/web 8080:80
```

El *port-forward* es especialmente útil para laboratorios y diagnóstico. La sesión termina cuando finaliza el recurso seleccionado.

---

# 🏷️ 46. Namespaces y labels

Namespaces:

```bash
kubectl get namespaces
kubectl create namespace sri
kubectl get pods -n sri
```

Labels:

```bash
kubectl label pod nginx app=web
```

Consultar:

```bash
kubectl get pods -l app=web
```

Los selectors de los Services utilizan labels para determinar qué Pods constituyen sus backends.

---

# 📄 47. Kubernetes declarativo con YAML

Crear recursos mediante comandos es útil para aprender.

Para infraestructura reproducible utilizaremos manifiestos.

Ejemplo:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web
spec:
  replicas: 2
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
        - name: nginx
          image: nginx:alpine
          ports:
            - containerPort: 80
```

Aplicar:

```bash
kubectl apply -f deployment.yaml
```

Consultar:

```bash
kubectl get -f deployment.yaml
```

Ver diferencias:

```bash
kubectl diff -f deployment.yaml
```

Eliminar:

```bash
kubectl delete -f deployment.yaml
```

---

# 🔍 48. Diagnóstico Kubernetes

Metodología:

```text
❌ El servicio no funciona
        │
        ├── kubectl get pods
        │
        ├── kubectl describe pod
        │
        ├── kubectl logs
        │
        ├── kubectl get svc
        │
        ├── kubectl describe svc
        │
        ├── kubectl get endpoints
        │
        ├── kubectl get events
        │
        └── kubectl exec
```

Comandos:

```bash
kubectl get pods
kubectl get pods -o wide
kubectl describe pod nombre
kubectl logs nombre
kubectl get services
kubectl describe service nombre
kubectl get endpoints
kubectl get events --sort-by=.lastTimestamp
```

Consulta de recursos:

```bash
kubectl explain pod
kubectl explain deployment.spec
kubectl explain service.spec
```

Métricas, si Metrics Server está disponible:

```bash
kubectl top nodes
kubectl top pods
```

---

# 🧠 49. Docker, Compose, Swarm y Kubernetes

No debemos mezclarlos.

```text
Docker
│
├── imágenes
├── contenedores
├── redes
└── volúmenes
        │
        ▼
Docker Compose
│
└── aplicación multicontenedor
        │
        ├── laboratorio local
        ├── desarrollo
        └── infraestructura reproducible


Docker Swarm
│
└── cluster de Docker Engines


Kubernetes
│
└── plataforma de orquestación
    ├── Cluster
    ├── Nodes
    ├── Pods
    ├── Deployments
    └── Services
```

Tabla de referencia:

| Concepto | Docker | Compose | Kubernetes |
|---|---|---|---|
| Unidad de ejecución | Contenedor | Servicio/contenedor | Pod |
| Red | Network | Network Compose | Red del cluster |
| DNS | nombres de contenedor | nombres de servicio | Services/DNS |
| Shell | `docker exec` | `docker compose exec` | `kubectl exec` |
| Logs | `docker logs` | `docker compose logs` | `kubectl logs` |
| Publicación | `-p` | `ports` | Service / port-forward |
| Persistencia | Volume | `volumes` | Volumes/PV/PVC |
| Escalado | manual | réplicas/Compose según escenario | Deployment/replicas |
| Declaración | Dockerfile/CLI | `compose.yaml` | manifiestos YAML |

---

# 🧑‍💻 50. Visual Studio Code como centro de trabajo

La integración WSL de VS Code permite que la interfaz gráfica se ejecute en Windows mientras código, terminal y herramientas trabajan en Linux.

Abrir el proyecto desde WSL:

```bash
cd ~/sri/docker-lab
code .
```

La ventana de trabajo será:

```text
┌────────────────┬────────────────────────────────┐
│ 📁 EXPLORADOR  │                                │
│                │          📝 EDITOR             │
│ compose.yaml   │                                │
│ Dockerfile     │      compose.yaml              │
│ nginx.conf     │      Dockerfile                │
│ html/          │      nginx.conf                │
│                │                                │
├────────────────┴────────────────────────────────┤
│ 🐧 TERMINAL WSL2                                │
│ $ docker compose up -d                          │
│ $ docker compose ps                             │
│ $ docker compose logs -f                        │
└─────────────────────────────────────────────────┘
```

Microsoft documenta este flujo mediante la extensión WSL de VS Code. [VS Code + WSL](https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-vscode)

---

# 🧪 51. Laboratorio integrador: Nginx + cliente

Objetivo:

```text
Windows
   │
localhost:8080
   │
   ▼
Nginx
   │
   │ red frontend
   ▼
cliente Alpine
```

`compose.yaml`:

```yaml
services:

  web:
    image: nginx:alpine
    ports:
      - "8080:80"
    volumes:
      - ./html:/usr/share/nginx/html:ro
    networks:
      - frontend

  cliente:
    image: alpine
    command: ["sh", "-c", "sleep infinity"]
    networks:
      - frontend

networks:
  frontend:
```

Levantar:

```bash
docker compose up -d
```

Comprobar:

```bash
docker compose ps
```

Desde el host:

```bash
curl http://localhost:8080
```

Desde el cliente:

```bash
docker compose exec cliente wget -qO- http://web
```

Entrar en Nginx:

```bash
docker compose exec web sh
```

Comprobar puerto:

```bash
docker compose exec web ss -lnt
```

Consultar DNS:

```bash
docker compose exec cliente getent hosts web
```

Logs:

```bash
docker compose logs -f web
```

Finalizar:

```bash
docker compose down
```

---

# 🧪 52. Laboratorio de troubleshooting

Provoca deliberadamente un error modificando:

```yaml
ports:
  - "8080:81"
```

Nginx sigue escuchando en:

```text
80/tcp
```

pero publicamos:

```text
8080 → 81
```

Diagnóstico:

```bash
docker compose ps
docker compose port web 80
docker compose exec web ss -lnt
docker compose logs web
```

El objetivo no es memorizar comandos, sino aprender a formular hipótesis:

```text
¿Está ejecutándose?
        ↓
¿Está escuchando?
        ↓
¿Está publicado?
        ↓
¿El puerto coincide?
        ↓
¿Resuelve DNS?
        ↓
¿Responde la aplicación?
```

---

# 🧰 53. Chuleta rápida de Kubernetes

## Cluster

```bash
kubectl version
kubectl cluster-info
kubectl get nodes
kubectl get namespaces
kubectl api-resources
kubectl api-versions
```

## Contextos

```bash
kubectl config get-contexts
kubectl config current-context
kubectl config use-context NOMBRE
kubectl config view
```

## Pods

```bash
kubectl get pods
kubectl get pods -o wide
kubectl get pods -A
kubectl describe pod POD
kubectl delete pod POD
kubectl run POD --image=IMAGEN
```

## Shell / comandos

```bash
kubectl exec POD -- comando
kubectl exec -it POD -- /bin/sh
kubectl exec -it POD -c CONTENEDOR -- /bin/sh
```

## Logs

```bash
kubectl logs POD
kubectl logs -f POD
kubectl logs POD -c CONTENEDOR
kubectl logs POD --previous
```

## Copia

```bash
kubectl cp POD:/ruta/fichero ./fichero
kubectl cp ./fichero POD:/ruta/fichero
```

## Deployments

```bash
kubectl create deployment web --image=nginx
kubectl get deployments
kubectl describe deployment web
kubectl scale deployment web --replicas=3
kubectl set image deployment/web nginx=nginx:alpine
kubectl rollout status deployment/web
kubectl rollout history deployment/web
kubectl rollout undo deployment/web
```

## Services

```bash
kubectl expose deployment web --port=80 --target-port=80
kubectl get services
kubectl describe service web
```

## Port forwarding

```bash
kubectl port-forward pod/POD 8080:80
kubectl port-forward service/SERVICE 8080:80
kubectl port-forward deployment/DEPLOYMENT 8080:80
```

## YAML

```bash
kubectl apply -f fichero.yaml
kubectl get -f fichero.yaml
kubectl diff -f fichero.yaml
kubectl delete -f fichero.yaml
```

## Diagnóstico

```bash
kubectl describe
kubectl get events
kubectl get endpoints
kubectl top pods
kubectl top nodes
kubectl explain
kubectl debug
```

---

# 📚 54. Documentación oficial abierta

Utiliza la documentación oficial como referencia primaria.

## Docker

- [Docker Docs](https://docs.docker.com/)
- [Docker CLI reference](https://docs.docker.com/reference/cli/docker/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Compose Specification](https://docs.docker.com/reference/compose-file/)
- [Dockerfile reference](https://docs.docker.com/reference/dockerfile/)
- [Docker networking](https://docs.docker.com/engine/network/)
- [Docker volumes](https://docs.docker.com/engine/storage/volumes/)
- [Docker Desktop](https://docs.docker.com/desktop/)
- [Docker Desktop + WSL2](https://docs.docker.com/desktop/features/wsl/)
- [Docker Compose installation](https://docs.docker.com/compose/install/)

## Nginx

- [Nginx Documentation](https://nginx.org/en/docs/)
- [Nginx Beginner's Guide](https://nginx.org/en/docs/beginners_guide.html)
- [Nginx Docker Official Image](https://hub.docker.com/_/nginx)

## Kubernetes

- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [Kubernetes Concepts](https://kubernetes.io/docs/concepts/)
- [kubectl](https://kubernetes.io/docs/reference/kubectl/)
- [kubectl Quick Reference](https://kubernetes.io/docs/reference/kubectl/quick-reference/)
- [kubectl commands](https://kubernetes.io/docs/reference/kubectl/generated/)
- [Pods](https://kubernetes.io/docs/concepts/workloads/pods/)
- [Services](https://kubernetes.io/docs/concepts/services-networking/service/)
- [Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
- [kubectl exec](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_exec/)
- [kubectl port-forward](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_port-forward/)

## Microsoft / WSL / VS Code

- [WSL documentation](https://learn.microsoft.com/windows/wsl/)
- [VS Code + WSL](https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-vscode)
- [Docker + WSL2](https://docs.docker.com/desktop/features/wsl/use-wsl/)

---

# 📝 55. Autoevaluación

## Preguntas

1. ¿Qué diferencia existe entre una imagen y un contenedor?
2. ¿Por qué un contenedor no equivale a una máquina virtual?
3. ¿Qué función desempeña Docker Engine?
4. ¿Qué diferencia existe entre `docker exec` y `docker attach`?
5. ¿Qué significa `-p 8080:80`?
6. ¿Por qué `EXPOSE 80` no equivale a publicar el puerto?
7. ¿Necesitan dos contenedores de una misma red Docker publicar sus puertos en el host para comunicarse?
8. ¿Qué función proporciona el DNS interno de Docker?
9. ¿Qué diferencia existe entre un volumen y un bind mount?
10. ¿Qué problema resuelve Docker Compose?
11. ¿Qué diferencia existe entre `docker compose exec` y `docker compose run`?
12. ¿Qué diferencia existe entre `ports` y `expose`?
13. ¿Por qué podemos utilizar `http://web` dentro de una aplicación Compose?
14. ¿Qué problema intenta resolver un `healthcheck`?
15. ¿Qué diferencia fundamental existe entre un Pod y un contenedor?
16. ¿Cómo entrarías en un Pod mediante una shell?
17. ¿Cómo consultarías los logs de un Pod?
18. ¿Cómo publicarías temporalmente el puerto 80 de un Pod en el puerto 8080 de tu máquina?
19. ¿Qué función desempeña un Deployment?
20. ¿Qué diferencia conceptual existe entre un Service y un Pod?
21. ¿Qué diferencia existe entre Docker Compose y Kubernetes?
22. ¿Qué utilidad tiene `kubectl describe`?
23. ¿Por qué es preferible utilizar nombres de servicio frente a IPs efímeras en Compose?
24. ¿Qué procedimiento seguirías para diagnosticar que `localhost:8080` no responde?

---

# ✅ 56. Respuestas de la autoevaluación

1. **Imagen:** plantilla inmutable para crear contenedores. **Contenedor:** instancia ejecutable de una imagen.
2. Una VM virtualiza una máquina y normalmente incorpora un sistema operativo invitado; el contenedor utiliza mecanismos de aislamiento sobre el kernel del entorno.
3. Ejecuta y administra los objetos de Docker: imágenes, contenedores, redes, volúmenes, etc.
4. `exec` ejecuta un nuevo proceso dentro del contenedor; `attach` conecta la terminal al proceso principal existente.
5. Publica el puerto 80 del contenedor como puerto 8080 del host.
6. `EXPOSE` documenta el puerto utilizado por la imagen; no crea por sí solo una publicación hacia el host.
7. No. Pueden comunicarse mediante una red Docker sin publicar el puerto en el host.
8. Permite resolver nombres de contenedores/servicios dentro de las redes correspondientes.
9. El volumen está gestionado por Docker; el bind mount enlaza directamente una ruta del host con una ruta del contenedor.
10. Permite describir y administrar una aplicación multicontenedor de forma declarativa.
11. `exec` trabaja sobre un contenedor existente y en ejecución; `run` crea un contenedor puntual para ejecutar un comando.
12. `ports` publica puertos hacia el host; `expose` no realiza esa publicación.
13. Porque Compose proporciona resolución DNS basada en los nombres de servicio dentro de su red.
14. Permite expresar si un servicio está realmente operativo, no sólo si el contenedor está ejecutándose.
15. Un Pod es una unidad de ejecución de Kubernetes que puede contener uno o varios contenedores relacionados.
16. `kubectl exec -it POD -- /bin/sh` o `/bin/bash` si está disponible.
17. `kubectl logs POD`.
18. `kubectl port-forward pod/POD 8080:80`.
19. Mantiene el estado deseado de un conjunto de Pods, incluyendo su número de réplicas y actualizaciones.
20. El Pod ejecuta la carga; el Service proporciona un punto de acceso estable y selecciona los Pods que constituyen sus backends.
21. Compose describe aplicaciones multicontenedor, habitualmente en un entorno local; Kubernetes proporciona una plataforma de orquestación de clusters con objetos como Pods, Deployments y Services.
22. Proporciona información detallada sobre un recurso y sus eventos/estado.
23. Las IPs de contenedor pueden cambiar; los nombres de servicio proporcionan una referencia estable mediante DNS.
24. Comprobaría, en orden: `docker compose ps`, logs, publicación mediante `docker compose port`, escucha interna con `ss`, configuración con `docker compose config` y, finalmente, conectividad mediante `curl`/`wget`.

---

# 🏁 57. Qué debe quedar en tu modelo mental

Si sólo recuerdas una secuencia de este anexo, que sea ésta:

```text
                  🐳 DOCKER
                     │
              ┌──────┴──────┐
              │             │
           IMAGEN       CONTENEDOR
                            │
              ┌─────────────┼─────────────┐
              │             │             │
             RED         PUERTOS       VOLUMEN
              │             │             │
              └─────────────┼─────────────┘
                            │
                     🐙 COMPOSE
                            │
                  varios servicios
                            │
                            ▼
                     ORQUESTACIÓN
                       /       \
                 Swarm       Kubernetes
                               │
                    ┌──────────┼──────────┐
                    │          │          │
                  Cluster     Node       Pod
                                          │
                                      Container
                                          │
                                       Service
```

Y, sobre todo:

> **No memorices Docker como una colección de comandos. Aprende a interpretar la relación entre procesos, imágenes, contenedores, redes, puertos, almacenamiento y servicios. Los comandos son las herramientas que permiten observar y modificar ese modelo.**

---

## 📌 Fuentes oficiales consultadas para esta versión

Esta versión se ha contrastado con la documentación oficial actual de Docker, Kubernetes, Nginx y Microsoft. Entre otros aspectos, se han verificado el backend WSL2 de Docker Desktop, Compose, publicación de puertos, acceso mediante `exec`, redes, Pods, `kubectl`, `port-forward` y el flujo VS Code + WSL2.

