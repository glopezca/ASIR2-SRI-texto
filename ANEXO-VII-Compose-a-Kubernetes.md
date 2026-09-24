# ☸️ ANEXO VII · Migración guiada de Docker Compose a Kubernetes

> **Nivel:** CFGS ASIR · Servicios de Red e Internet  
> **Punto de partida:** Docker Compose del Anexo VI  
> **Objetivo:** aprender a trasladar una infraestructura multicontenedor a Kubernetes sin tratar la conversión automática como una traducción mecánica.

## 0. Por qué existe este anexo

Docker Compose y Kubernetes resuelven problemas relacionados, pero no describen exactamente el mismo nivel de infraestructura. Compose es especialmente cómodo para definir y ejecutar una aplicación multicontenedor en un entorno local o de laboratorio. Kubernetes es una plataforma de orquestación que mantiene un estado deseado sobre un clúster y utiliza objetos como Pods, Deployments y Services.

La idea fundamental es esta:

```text
Docker Compose                         Kubernetes
─────────────────                      ─────────────────────
services:                              Deployment / StatefulSet / Job
container                              container dentro de un Pod
ports                                  Service / Ingress / port-forward
networks                               red del clúster + Services + DNS
volumes                                Volume / PersistentVolume / PVC
environment                            env / ConfigMap / Secret
healthcheck                            probes
depends_on                             readiness + controladores + aplicación
compose.yaml                           manifests YAML / Helm / Kustomize
```

Antes de leer la tabla conviene conocer cuatro términos que aparecerán continuamente: **YAML** es un formato textual de datos estructurados muy utilizado para configuración; **Helm** empaqueta aplicaciones Kubernetes mediante *charts*; **Kustomize** permite personalizar manifiestos Kubernetes; un **Service** es un objeto que proporciona un punto de acceso estable a Pods.

La tabla **no significa que exista una equivalencia uno a uno**. Es un mapa mental para iniciar la migración.

---


> 🏭 **ANALOGÍA · UNA FÁBRICA CON SUPERVISIÓN CONTINUA**
>
> En una fábrica no basta con encender una máquina una vez: hay que mantener el número de puestos de trabajo deseado, sustituir una máquina averiada y mantener una organización estable. Kubernetes introduce precisamente esa idea de **estado deseado** y supervisión continua. Esta analogía será útil durante toda la migración desde Compose.

# 1. Antes de empezar: ¿qué es Kubernetes?

## 1.1. El problema que intenta resolver

Imagina que con Docker Compose tenemos cinco servicios en un ordenador. Sabemos cómo arrancarlos, conectarlos y detenerlos. Ahora supongamos que necesitamos varias máquinas, réplicas de los servicios, recuperación automática, actualizaciones progresivas, descubrimiento de servicios y una forma declarativa de describir el estado que queremos mantener.

Ahí aparece Kubernetes.

Kubernetes es una plataforma de código abierto para gestionar cargas de trabajo y servicios contenerizados. Su modelo es declarativo: describimos el estado deseado y los componentes del sistema trabajan para acercar el estado real a ese estado deseado.

> 🧭 **Antes de continuar**
>
> **Clúster** significa el conjunto de recursos Kubernetes que se administran como una unidad. Un **nodo (Node)** es una máquina física o virtual que puede ejecutar Pods. El **plano de control (control plane)** contiene los componentes que mantienen el estado del clúster. La **API de Kubernetes** es la interfaz mediante la que usuarios, herramientas y componentes consultan o modifican ese estado.

## 1.2. El Pod

Un **Pod** es la unidad de computación desplegable más pequeña que Kubernetes crea y gestiona. Un Pod puede contener uno o varios contenedores que comparten determinados recursos, especialmente la red y los volúmenes que se monten en común.

No debemos pensar «un Pod = un contenedor» como una regla absoluta. En la mayoría de las aplicaciones sencillas habrá un contenedor principal por Pod, pero Kubernetes permite añadir contenedores estrechamente relacionados.

```text
┌────────────────────── POD ──────────────────────┐
│                                                 │
│   contenedor principal      contenedor auxiliar │
│          │                         │            │
│          └──────── red compartida ─┘            │
│                                                 │
└─────────────────────────────────────────────────┘
```

## 1.3. Deployment

Un **Deployment** gestiona un conjunto de Pods que ejecutan una aplicación. Entre otras cosas, permite expresar cuántas réplicas queremos y controlar actualizaciones progresivas.

En una aplicación web stateless, el patrón habitual será:

```text
Deployment
    │
    ├── Pod web
    ├── Pod web
    └── Pod web
```

Si un Pod desaparece, el Deployment puede provocar que se cree otro para recuperar el número deseado de réplicas.

## 1.4. Service

Un **Service** proporciona un punto de acceso estable para un conjunto de Pods. Esto es necesario porque los Pods son recursos efímeros: pueden desaparecer y ser sustituidos por otros con otras direcciones IP.

```text
cliente
   │
   ▼
Service: web
   │
   ├── Pod web-1
   ├── Pod web-2
   └── Pod web-3
```

El cliente no necesita conocer las IP efímeras de los Pods.

## 1.5. Namespace

Un **Namespace** es un ámbito lógico para organizar recursos dentro de un clúster. Para las primeras prácticas podemos trabajar en `default`, pero conviene conocer el concepto desde el principio porque permite separar proyectos y recursos.

## 1.6. ConfigMap y Secret

Un **ConfigMap** almacena configuración no confidencial. Un **Secret** está pensado para datos sensibles como contraseñas, tokens o claves.

> ⚠️ Un Secret no debe interpretarse como «una contraseña mágicamente cifrada en todo momento». Su protección depende también de la configuración del clúster, del control de acceso y del almacenamiento subyacente. No se deben subir credenciales reales al repositorio.

## 1.7. Volúmenes y almacenamiento persistente

En Compose solemos declarar:

```yaml
volumes:
  datos:
```

En Kubernetes el almacenamiento se modela con recursos y volúmenes. Para almacenamiento persistente aparecen **PersistentVolume (PV)** y **PersistentVolumeClaim (PVC)**. Un PVC expresa la necesidad de almacenamiento que una carga de trabajo quiere utilizar.

## 1.8. kubectl

`kubectl` es la herramienta principal de línea de comandos para comunicarse con la API de Kubernetes.

```bash
kubectl version
kubectl cluster-info
kubectl get nodes
kubectl get pods
```

Antes de ejecutar órdenes debemos saber **a qué clúster y contexto estamos conectados**:

```bash
kubectl config get-contexts
kubectl config current-context
```

Un error de contexto puede hacer que trabajemos en otro clúster distinto del que creíamos.

---

# 2. Preparar un Kubernetes de laboratorio

Hay varias formas de disponer de un clúster de aprendizaje. Entre las habituales se encuentran Kubernetes integrado en una distribución de escritorio, Minikube o Kind. La elección depende de la máquina y del entorno del centro.

La condición imprescindible es que `kubectl` esté configurado para hablar con un clúster accesible.

Comprueba:

```bash
kubectl version
kubectl cluster-info
kubectl get nodes -o wide
```

El resultado de `kubectl get nodes` debe mostrar al menos un nodo en estado `Ready` para poder desplegar cargas de trabajo.

> 🧪 **Primera prueba antes de migrar Compose**
>
> No empieces por convertir `compose.yaml`. Primero demuestra que Kubernetes funciona independientemente del proyecto:
>
> ```bash
> kubectl create deployment prueba --image=nginx:alpine
> kubectl get deployment
> kubectl get pods -o wide
> kubectl delete deployment prueba
> ```
>
> Si esta prueba falla, el problema está en Kubernetes o en el acceso al clúster, no en Compose.

---

# 3. Inventariar el Compose antes de migrarlo

Nunca conviene empezar la migración ejecutando una herramienta automática sin entender el fichero de origen.

Supongamos:

```yaml
services:
  web:
    image: nginx:alpine
    ports:
      - "8080:80"
    networks:
      - frontend

  app:
    image: python:3-alpine
    command: ["python", "-m", "http.server", "8000", "--bind", "0.0.0.0"]
    expose:
      - "8000"
    networks:
      - frontend

networks:
  frontend:
```

Antes de convertirlo, responde:

1. ¿Cuántos servicios existen?
2. ¿Qué imagen utiliza cada servicio?
3. ¿Qué comando inicia cada contenedor?
4. ¿Qué puertos escucha realmente cada proceso?
5. ¿Qué puertos se publican hacia el host?
6. ¿Qué servicios necesitan comunicarse entre sí?
7. ¿Qué datos deben sobrevivir a la sustitución del contenedor?
8. ¿Qué variables de entorno existen?
9. ¿Hay comprobaciones de salud?
10. ¿Qué dependencias son reales y cuáles son solo un orden de arranque?

Esta lista convierte la migración en un problema de arquitectura y no en un simple cambio de sintaxis.

---


> 🏢 **ANALOGÍA · DE UN PLANO ÚNICO A UN PROYECTO DE INSTALACIONES**
>
> En Compose podemos describir una aplicación multicontenedor en un solo documento. En Kubernetes el mismo problema se divide en varios objetos especializados: uno describe cómo ejecutar la carga de trabajo y otro cómo ofrecerle una dirección estable dentro de la red. No es una traducción palabra por palabra; es una adaptación del diseño a otro modelo de administración.

# 4. Traducir `services` a recursos Kubernetes

## 4.1. No existe un recurso `service` equivalente al `services:` de Compose

Esta es una de las confusiones más importantes.

En Compose:

```yaml
services:
  web:
```

`services` agrupa los contenedores que forman la aplicación.

En Kubernetes, el recurso llamado **Service** es otra cosa: proporciona acceso de red estable a Pods.

Por eso, una entrada Compose como `web:` normalmente se convierte en **al menos**:

```text
Deployment
   +
Service
```

---

# 5. Primera migración manual: Nginx

## 5.1. Compose de partida

```yaml
services:
  web:
    image: nginx:alpine
    ports:
      - "8080:80"
```

Ejecutar en Compose:

```bash
docker compose up -d
docker compose ps
curl http://localhost:8080
```

## 5.2. Deployment

Creamos `web-deployment.yaml`:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web
spec:
  replicas: 1
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
        - name: web
          image: nginx:alpine
          ports:
            - containerPort: 80
```

Aplicar:

```bash
kubectl apply -f web-deployment.yaml
kubectl get deployment web
kubectl get pods -l app=web
```

## 5.3. Service

Creamos `web-service.yaml`:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: web
spec:
  selector:
    app: web
  ports:
    - port: 80
      targetPort: 80
  type: ClusterIP
```

Aplicar:

```bash
kubectl apply -f web-service.yaml
kubectl get service web
```

Ahora `web` es un nombre DNS utilizable **dentro del clúster**.

## 5.4. ¿Y el `8080:80` de Compose?

No lo debemos traducir automáticamente a `ClusterIP` con `8080` porque son conceptos distintos.

Para una prueba local podemos utilizar:

```bash
kubectl port-forward service/web 8080:80
```

Y, en otra terminal:

```bash
curl http://localhost:8080
```

El `port-forward` es un mecanismo temporal de acceso desde nuestra máquina; no convierte el Service en una publicación permanente equivalente a `ports:` de Compose.

---

# 6. Escalar: de un contenedor a varias réplicas

Compose:

```bash
docker compose up -d --scale web=3
```

Kubernetes:

```bash
kubectl scale deployment web --replicas=3
kubectl get pods -l app=web -o wide
```

La diferencia conceptual es importante:

```text
Compose                         Kubernetes
────────                       ──────────
3 contenedores                 3 Pods gestionados
                                 ▲
                                 │
                             Deployment
```

No administramos manualmente los nombres de los Pods. Trabajamos con el estado deseado.

---

# 7. Traducir redes Compose

En Compose es habitual:

```yaml
networks:
  frontend:
```

y:

```yaml
services:
  web:
    networks: [frontend]
  app:
    networks: [frontend]
```

Los servicios pueden localizarse por nombre dentro de la red de Compose.

En Kubernetes la red funciona de otra forma. Los Pods tienen direcciones IP propias y los Services proporcionan nombres y puntos de acceso estables.

Por tanto, la traducción conceptual es:

```text
Compose network
       ↓
red del clúster + Service + DNS interno
```

Para acceder desde `web` a `app`, normalmente utilizaremos:

```text
http://app:8000
```

si existe un Service llamado `app` que expone el puerto correspondiente.

> 🧠 **Idea clave**
>
> En Compose solemos pensar «servicio → nombre DNS del servicio». En Kubernetes debemos añadir una capa: «Deployment/Pods → Service → nombre DNS estable».

---


> 🚪 **ANALOGÍA · PUERTAS INTERIORES Y PUERTA PRINCIPAL**
>
> `expose` se parece a indicar que un edificio tiene una puerta interior que otros departamentos pueden utilizar; `ports` se parece a abrir una puerta que conecta el edificio con el exterior. En Kubernetes, esa idea se reparte entre los Services y los distintos mecanismos de exposición.

# 8. Traducir `ports` y `expose`

## `expose` en Compose

`expose` documenta o deja disponible un puerto para la comunicación entre servicios sin publicarlo directamente en el host.

En Kubernetes el concepto habitual será un `containerPort` acompañado, cuando haga falta acceso estable, de un Service.

## `ports` en Compose

```yaml
ports:
  - "8080:80"
```

significa que el host publica `8080` y lo dirige al puerto `80` del contenedor.

En Kubernetes hay varias formas de exposición:

| Necesidad | Mecanismo habitual |
|---|---|
| Acceso interno al clúster | `ClusterIP` |
| Prueba temporal desde el equipo | `kubectl port-forward` |
| Publicación mediante puerto del nodo | `NodePort` |
| Integración con un balanceador externo | `LoadBalancer` |
| Entrada HTTP/HTTPS basada en reglas | `Ingress` + controlador |

No debemos escoger `NodePort` simplemente porque se parece visualmente a `ports`. La elección depende de la arquitectura y del entorno.

---

# 9. Traducir volúmenes

Compose:

```yaml
services:
  db:
    volumes:
      - datos:/var/lib/mysql

volumes:
  datos:
```

En Kubernetes debemos decidir qué tipo de persistencia necesitamos.

Para una práctica sencilla podemos utilizar un volumen gestionado por el entorno. Para almacenamiento persistente independiente del ciclo de vida del Pod aparecen PV y PVC.

Ejemplo de PVC:

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: datos
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
```

Y el Pod/Deployment puede montarlo:

```yaml
volumes:
  - name: datos
    persistentVolumeClaim:
      claimName: datos
```

El alumno debe comprobar qué **StorageClass** ofrece su clúster antes de asumir que cualquier configuración de almacenamiento funcionará.

---

# 10. Traducir variables de entorno

Compose:

```yaml
environment:
  APP_MODE: production
  DB_HOST: db
```

Puede trasladarse inicialmente a:

```yaml
env:
  - name: APP_MODE
    value: production
  - name: DB_HOST
    value: db
```

Pero cuando una configuración debe separarse del manifiesto de la aplicación conviene estudiar ConfigMap y Secret.

ConfigMap:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  APP_MODE: production
  DB_HOST: db
```

Y después:

```yaml
envFrom:
  - configMapRef:
      name: app-config
```

Para una contraseña:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: db-secret
type: Opaque
stringData:
  DB_PASSWORD: cambia-esta-clave-en-el-laboratorio
```

En un repositorio real no debemos almacenar credenciales reales en texto plano.

---

# 11. Traducir `healthcheck`

Compose puede contener:

```yaml
healthcheck:
  test: ["CMD", "curl", "-f", "http://localhost/health"]
  interval: 30s
  timeout: 5s
  retries: 3
```

Kubernetes separa las comprobaciones según su finalidad. Las tres ideas fundamentales son:

- **startup probe:** determina si la aplicación ha terminado de arrancar;
- **readiness probe:** determina si está preparada para recibir tráfico;
- **liveness probe:** ayuda a detectar una aplicación que ha quedado bloqueada o no responde correctamente.

Ejemplo:

```yaml
readinessProbe:
  httpGet:
    path: /health
    port: 80
  initialDelaySeconds: 5
  periodSeconds: 10

livenessProbe:
  httpGet:
    path: /health
    port: 80
  periodSeconds: 20
```

No se debe copiar una prueba de Compose sin entender qué significa «saludable» para esa aplicación.

---

# 12. Traducir `depends_on`

Compose permite expresar dependencias de arranque:

```yaml
depends_on:
  - db
```

En Kubernetes no debemos traducir esto literalmente como «arranca A antes que B». Kubernetes trabaja con recursos que convergen hacia un estado deseado.

Si `web` necesita que `db` esté realmente disponible, debemos expresar esa condición de forma adecuada, por ejemplo mediante:

- Service estable para `db`;
- readiness del servicio de base de datos;
- reintentos de conexión en la aplicación;
- probes;
- inicialización de esquema mediante Jobs o mecanismos específicos de la aplicación.

> 🧠 **Analogía**
>
> `depends_on` se parece a decir «abre primero la puerta de la cocina». Kubernetes necesita una descripción más profesional: «el restaurante puede aceptar clientes cuando la cocina está realmente operativa». El orden de creación de procesos no demuestra que la aplicación esté lista.

---

# 13. Convertir automáticamente con Kompose

Kubernetes proporciona documentación específica para traducir ficheros Docker Compose mediante **Kompose**. La herramienta puede generar manifiestos Kubernetes a partir de un Compose existente.

Ejemplo:

```bash
kompose convert
```

A continuación inspeccionamos los archivos generados y los aplicamos:

```bash
kubectl apply -f .
```

> ⚠️ **Kompose no es un botón mágico de migración.**
>
> Una conversión automática puede ser muy útil como punto de partida, pero hay que revisar redes, puertos, almacenamiento, seguridad, probes, configuración y comportamiento de la aplicación. La propia documentación de Kubernetes muestra advertencias para determinadas claves de Compose que no tienen una equivalencia directa.

Procedimiento profesional:

```text
compose.yaml
    │
    ▼
kompose convert
    │
    ▼
manifiestos generados
    │
    ▼
REVISIÓN HUMANA
    │
    ├── redes
    ├── puertos
    ├── almacenamiento
    ├── configuración
    ├── secretos
    ├── probes
    ├── seguridad
    └── escalado
    │
    ▼
kubectl apply
    │
    ▼
PRUEBAS
```

---

# 14. Migración guiada de una arquitectura de dos servicios

Partimos de:

```yaml
services:
  proxy:
    image: nginx:alpine
    ports:
      - "8080:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
    networks: [frontend, backend]

  app:
    image: python:3-alpine
    command: ["python", "-m", "http.server", "8000", "--bind", "0.0.0.0"]
    expose:
      - "8000"
    networks: [backend]

networks:
  frontend:
  backend:
```

## Paso 1 · Mantener las imágenes

No cambiamos inicialmente las imágenes. La primera migración debe reducir variables:

```text
nginx:alpine → nginx:alpine
python:3-alpine → python:3-alpine
```

## Paso 2 · Crear Deployment de `app`

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: app
  template:
    metadata:
      labels:
        app: app
    spec:
      containers:
        - name: app
          image: python:3-alpine
          command: ["python", "-m", "http.server", "8000", "--bind", "0.0.0.0"]
          ports:
            - containerPort: 8000
```

## Paso 3 · Crear Service de `app`

```yaml
apiVersion: v1
kind: Service
metadata:
  name: app
spec:
  selector:
    app: app
  ports:
    - port: 8000
      targetPort: 8000
```

## Paso 4 · Crear Deployment de `proxy`

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: proxy
spec:
  replicas: 1
  selector:
    matchLabels:
      app: proxy
  template:
    metadata:
      labels:
        app: proxy
    spec:
      containers:
        - name: proxy
          image: nginx:alpine
          ports:
            - containerPort: 80
```

La configuración de Nginx debe apuntar al Service `app`, no a la IP de un Pod:

```nginx
location / {
    proxy_pass http://app:8000;
}
```

## Paso 5 · Crear Service de `proxy`

```yaml
apiVersion: v1
kind: Service
metadata:
  name: proxy
spec:
  selector:
    app: proxy
  ports:
    - port: 80
      targetPort: 80
```

## Paso 6 · Probar desde el interior

Creamos un Pod temporal con herramientas:

```bash
kubectl run cliente --rm -it --image=curlimages/curl -- sh
```

Dentro:

```sh
curl http://proxy
curl http://app:8000
```

Salimos con `exit`.

## Paso 7 · Probar desde el host

En otra terminal:

```bash
kubectl port-forward service/proxy 8080:80
```

Y probamos:

```bash
curl http://localhost:8080
```

## Paso 8 · Diagnosticar

```bash
kubectl get pods -o wide
kubectl get services
kubectl get endpointslices
kubectl describe deployment proxy
kubectl describe service proxy
kubectl logs deployment/proxy
```

Si `proxy` no puede llegar a `app`, seguimos esta secuencia:

```text
¿app está Running?
      ↓
¿app tiene Service?
      ↓
¿el selector coincide con las labels?
      ↓
¿existe EndpointSlice?
      ↓
¿el puerto del Service coincide con targetPort?
      ↓
¿Nginx apunta al nombre correcto?
      ↓
¿la aplicación escucha en 0.0.0.0?
```

---

# 15. Trasladar las UT1–UT8

La migración de las ocho unidades debe entenderse como una progresión. No todos los servicios son igualmente apropiados para Kubernetes.

| UT | Compose | Kubernetes | Observación didáctica |
|---|---|---|---|
| **UT1** TCP/IP | toolbox de diagnóstico | Pod de herramientas + Services cuando proceda | Ideal para observar red y DNS del clúster; no sustituye Packet Tracer para routing físico/lógico. |
| **UT2** DHCP | laboratorio controlado | Pod/Deployment posible, pero limitado por la semántica de broadcast y la red del clúster | Mantener la práctica real de DHCP en VirtualBox/Packet Tracer. Kubernetes sirve para estudiar contenedorización, no para fingir una LAN convencional. |
| **UT3** DNS | BIND + cliente | Deployment/Service de BIND + cliente | Excelente para estudiar DNS interno y Service discovery; separar DNS de aplicación y DNS del clúster. |
| **UT4** FTP/SFTP | servidor + cliente | Deployment/Service | SFTP suele ser más sencillo de trasladar; FTP requiere especial cuidado con canal de datos, puertos pasivos y NAT. |
| **UT5** Web | Nginx/Apache + aplicación | Deployment + Service + opcional Ingress | Es el ejemplo ideal para comprender la migración. |
| **UT6** Correo | MTA/MDA/IMAP/Webmail | Varios Deployments/Services + almacenamiento persistente | Requiere almacenamiento, DNS, identidad, seguridad y persistencia; no es una migración trivial. |
| **UT7** Mensajería | XMPP/IRC/listas | Deployments/StatefulSets + Services + almacenamiento según servicio | Adecuado para estudiar Service discovery y persistencia, pero hay que revisar identidad y datos. |
| **UT8** Audio/vídeo | Icecast/RTMP/HLS | Deployments/Services + almacenamiento/Ingress según arquitectura | El streaming en tiempo real introduce requisitos de red, latencia y persistencia que deben probarse. |

## 15.1. Regla didáctica

No se debe decir «todo Compose se convierte a Kubernetes» sin matices.

La pregunta profesional es:

> **¿Qué parte de la arquitectura queremos conservar y qué parte debe cambiar al pasar de un entorno local multicontenedor a un sistema orquestado?**

---

# 16. Acceso a un Pod

Para listar Pods:

```bash
kubectl get pods
```

Para entrar:

```bash
kubectl exec -it NOMBRE_DEL_POD -- /bin/sh
```

Si la imagen incluye Bash:

```bash
kubectl exec -it NOMBRE_DEL_POD -- /bin/bash
```

Para salir:

```bash
exit
```

Si el Pod tiene varios contenedores:

```bash
kubectl exec -it NOMBRE_DEL_POD -c NOMBRE_CONTENEDOR -- /bin/sh
```

Para consultar logs:

```bash
kubectl logs NOMBRE_DEL_POD
```

Para copiar archivos:

```bash
kubectl cp NAMESPACE/NOMBRE_DEL_POD:/ruta/remota ./ruta-local
```

La operación `exec` es una herramienta de diagnóstico, no una sustitución de la administración declarativa. Los cambios manuales realizados dentro de un contenedor pueden desaparecer cuando el Pod sea reemplazado.

---

# 17. Borrar y volver a crear correctamente

En Kubernetes debemos distinguir entre borrar un Pod y borrar el recurso que lo gestiona.

```bash
kubectl delete pod NOMBRE_DEL_POD
```

Si existe un Deployment, probablemente aparecerá otro Pod para recuperar el estado deseado.

Para eliminar el Deployment:

```bash
kubectl delete deployment web
```

Y su Service:

```bash
kubectl delete service web
```

Esta diferencia es fundamental para entender la reconciliación de Kubernetes.

---

# 18. Actualizaciones y rollback

Con un Deployment podemos modificar la imagen:

```bash
kubectl set image deployment/web web=nginx:alpine
```

Consultar el rollout:

```bash
kubectl rollout status deployment/web
kubectl rollout history deployment/web
```

Si una actualización debe revertirse:

```bash
kubectl rollout undo deployment/web
```

La idea es equivalente a una actualización progresiva, pero Kubernetes incorpora un controlador que mantiene el estado deseado.

---

# 19. Diagnóstico sistemático después de la migración

Cuando algo falla, no empieces cambiando YAML al azar.

## Nivel 1 · Cluster

```bash
kubectl get nodes
kubectl get namespaces
```

## Nivel 2 · Workload

```bash
kubectl get deployments
kubectl get pods -o wide
```

## Nivel 3 · Estado del Pod

```bash
kubectl describe pod NOMBRE_DEL_POD
```

## Nivel 4 · Logs

```bash
kubectl logs NOMBRE_DEL_POD
```

## Nivel 5 · Service

```bash
kubectl get services
kubectl describe service NOMBRE
kubectl get endpointslices
```

## Nivel 6 · DNS

Desde un Pod de diagnóstico:

```bash
nslookup web
```

## Nivel 7 · Conectividad

```bash
curl http://web
```

## Nivel 8 · Eventos

```bash
kubectl get events --sort-by=.lastTimestamp
```

Este procedimiento reproduce la filosofía de diagnóstico aprendida en las UT: **estado → configuración → proceso → red → cliente → logs → evidencia**.

---

# 20. Ejercicio guiado: migrar la práctica Web de UT5

## Objetivo

Partir de la práctica Docker Compose de UT5 y obtener una versión Kubernetes que mantenga la misma funcionalidad observable.

## Fase A · Comprender

Antes de escribir YAML, dibuja:

```text
cliente
   │
   ▼
proxy
   │
   ▼
app
```

Identifica:

- imagen del proxy;
- imagen de la aplicación;
- puerto del proxy;
- puerto de la aplicación;
- configuración del proxy;
- qué puerto debe quedar accesible desde el host;
- qué tráfico debe permanecer interno.

## Fase B · Convertir

Crea:

```text
k8s/
├── app-deployment.yaml
├── app-service.yaml
├── proxy-config.yaml
├── proxy-deployment.yaml
└── proxy-service.yaml
```

## Fase C · Aplicar

```bash
kubectl apply -f k8s/
```

## Fase D · Verificar

```bash
kubectl get deployments
kubectl get pods
kubectl get services
kubectl get endpointslices
```

## Fase E · Probar

```bash
kubectl port-forward service/proxy 8080:80
curl http://localhost:8080
```

## Fase F · Explicar

El alumno debe responder por escrito:

1. ¿Qué elemento de Kubernetes sustituye conceptualmente a cada servicio de Compose?
2. ¿Por qué existe un Service además del Deployment?
3. ¿Qué ocurre si eliminamos un Pod?
4. ¿Por qué Nginx debe utilizar `app` y no la IP del Pod?
5. ¿Qué diferencia existe entre `containerPort`, `targetPort` y el puerto local usado por `port-forward`?
6. ¿Qué información debería ir en un ConfigMap?
7. ¿Qué información debería ir en un Secret?

---

# 21. Ejercicio guiado: usar Kompose sin perder el control

1. Comprueba que Compose funciona:

```bash
docker compose up -d
docker compose ps
docker compose config
```

2. Guarda el Compose que has probado.

3. Ejecuta:

```bash
kompose convert
```

4. Abre todos los YAML generados.

5. Identifica qué recursos ha creado.

6. Busca especialmente:
   - puertos;
   - Services;
   - Deployments;
   - volúmenes;
   - variables de entorno;
   - claves ignoradas o no traducidas.

7. Aplica solo después de revisar:

```bash
kubectl apply -f .
```

8. Compara el resultado con la arquitectura original.

9. Documenta qué has tenido que corregir manualmente.

---

# 22. Qué no debe migrarse automáticamente

Hay características de Compose que no tienen una traducción directa o que requieren decisiones arquitectónicas:

- `depends_on` como simple orden de arranque;
- `network_mode` específico del host;
- montajes de rutas locales del host;
- acceso a dispositivos del host;
- privilegios elevados;
- redes especiales;
- puertos pasivos de FTP;
- servicios que esperan broadcast de una LAN física;
- almacenamiento local sin una estrategia de persistencia;
- configuraciones dependientes de una máquina concreta.

Cuando aparece uno de estos casos, la respuesta profesional no es buscar una traducción textual. Hay que rediseñar el mecanismo manteniendo el requisito funcional.

---

# 23. Kubernetes y Git

Una vez migrada una infraestructura, los manifiestos deben versionarse:

```text
k8s/
├── namespace.yaml
├── app-deployment.yaml
├── app-service.yaml
├── configmap.yaml
├── secret.example.yaml
└── README.md
```

Nunca debemos subir credenciales reales al repositorio.

El flujo profesional básico es:

```bash
git status
git add k8s/
git commit -m "Añadir despliegue Kubernetes de UT5"
git push
```

La infraestructura pasa así a ser código revisable y reproducible.

---

# 24. Checklist de migración

Antes de considerar terminada una migración:

- [ ] El clúster está operativo.
- [ ] `kubectl` utiliza el contexto correcto.
- [ ] Cada carga de trabajo tiene un recurso Kubernetes adecuado.
- [ ] Los Pods están `Running` o han alcanzado el estado esperado.
- [ ] Los Services tienen selectores correctos.
- [ ] Existen EndpointSlices cuando deben existir.
- [ ] Los puertos internos están documentados.
- [ ] La exposición externa responde al requisito real.
- [ ] La configuración no confidencial está separada mediante ConfigMap cuando procede.
- [ ] Las credenciales se gestionan como Secret o mediante un mecanismo externo apropiado.
- [ ] El almacenamiento persistente está diseñado y probado.
- [ ] Las probes representan condiciones reales de la aplicación.
- [ ] Los logs se pueden consultar.
- [ ] Se ha probado la pérdida y recreación de un Pod.
- [ ] Se ha probado una actualización.
- [ ] Se sabe hacer rollback.
- [ ] La configuración está versionada.
- [ ] La documentación explica las diferencias respecto de Compose.

---

# 25. Navaja suiza de la migración

## Compose

```bash
docker compose config
docker compose up -d
docker compose ps
docker compose logs -f
docker compose exec servicio sh
docker compose down
```

## Kubernetes

```bash
kubectl config current-context
kubectl get nodes
kubectl get namespaces
kubectl apply -f .
kubectl get deployments
kubectl get pods -o wide
kubectl get services
kubectl get endpointslices
kubectl describe pod POD
kubectl logs POD
kubectl exec -it POD -- sh
kubectl port-forward service/SERVICE 8080:80
kubectl rollout status deployment/DEPLOYMENT
kubectl rollout undo deployment/DEPLOYMENT
kubectl delete -f .
```

## Kompose

```bash
kompose convert
kompose convert -f compose.yaml
```

---

# 26. Criterio final

La migración termina cuando podemos demostrar que la aplicación funciona y explicar **por qué** funciona en Kubernetes.

El objetivo didáctico no es que el alumno aprenda a convertir YAML. Es que sea capaz de reconocer el cambio de modelo:

```text
Docker Compose
    │
    │  aplicación multicontenedor
    ▼
Kubernetes
    │
    ├── estado deseado
    ├── Pods
    ├── controladores
    ├── Services
    ├── DNS interno
    ├── almacenamiento
    ├── configuración
    ├── seguridad
    └── observabilidad
```

> **Principio rector:** primero comprender la arquitectura, después traducirla y finalmente automatizar la traducción. Una herramienta como Kompose puede ahorrar trabajo mecánico; no sustituye el criterio del administrador de sistemas.

## Documentación oficial

- Kubernetes: https://kubernetes.io/docs/
- Conceptos de Kubernetes: https://kubernetes.io/docs/concepts/
- Pods: https://kubernetes.io/docs/concepts/workloads/pods/
- Deployments: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
- Services: https://kubernetes.io/docs/concepts/services-networking/service/
- ConfigMaps: https://kubernetes.io/docs/concepts/configuration/configmap/
- Secrets: https://kubernetes.io/docs/concepts/configuration/secret/
- Volúmenes: https://kubernetes.io/docs/concepts/storage/volumes/
- `kubectl`: https://kubernetes.io/docs/concepts/overview/kubectl/
- Traducción de Compose a Kubernetes mediante Kompose: https://kubernetes.io/docs/tasks/configure-pod-container/translate-compose-kubernetes/
- Docker Compose: https://docs.docker.com/compose/
