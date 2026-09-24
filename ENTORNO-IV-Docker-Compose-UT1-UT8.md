# 🧱 ENTORNO IV · Infraestructura de las UT1–UT8 con Docker Compose

> 🧭 **ANTES DE EMPEZAR · VOCABULARIO TÉCNICO**
>
> Las siglas, abreviaturas y conceptos técnicos que van a aparecer en esta unidad se presentan aquí antes de su desarrollo. La explicación local de cada tema podrá ampliar estas definiciones cuando sea necesario.
>
> **UT** — Unidad de Trabajo: unidad didáctica del módulo profesional.
> **CFGS** — Ciclo Formativo de Grado Superior.
> **ASIR** — Administración de Sistemas Informáticos en Red.
> **Docker** — Plataforma de contenerización para construir, distribuir y ejecutar aplicaciones aisladas en contenedores.
> **Docker Compose** — Herramienta de Docker para definir y ejecutar aplicaciones multicontenedor mediante un archivo declarativo.
> **DNS** — Sistema de nombres de dominio: servicio distribuido que relaciona nombres con direcciones IP y otros datos.
> **TCP** — Protocolo de transporte orientado a conexión que proporciona entrega fiable y ordenada.
> **TCP/IP** — Familia de protocolos de Internet en la que IP proporciona direccionamiento y TCP es uno de los protocolos de transporte.
> **IP** — Protocolo de Internet, responsable del direccionamiento y encaminamiento de paquetes.
> **CONTENEDOR** — Instancia aislada de una imagen que comparte el núcleo del sistema anfitrión.
> **DHCP** — Protocolo de configuración dinámica de host: entrega automáticamente parámetros de red a los clientes.
> **LAN** — Red de área local.
> **SFTP** — Protocolo de transferencia de archivos que funciona como subsistema de SSH; no es FTP cifrado.
> **SSH** — Protocolo seguro de administración remota y transporte de otros servicios.
> **SSH/SFTP** — SSH es el protocolo seguro de transporte; SFTP es un subsistema de transferencia de archivos que funciona sobre SSH.
> **HOST** — Equipo o sistema anfitrión en el que se ejecuta un servicio, contenedor o máquina virtual.
> **HTTP** — Protocolo de transferencia de hipertexto utilizado principalmente por la Web.
> **MUA** — Mail User Agent, programa con el que el usuario compone, envía y lee correo.
> **MTA** — Mail Transfer Agent, componente que transporta correo entre servidores.
> **SMTP** — Simple Mail Transfer Protocol, protocolo principal para transportar correo entre agentes de correo.
> **IMAP** — Internet Message Access Protocol, protocolo para acceder y gestionar mensajes que permanecen en el servidor.
> **XMPP** — Extensible Messaging and Presence Protocol, protocolo abierto para mensajería y presencia.
> **IRC** — Internet Relay Chat, protocolo de conversación textual en tiempo real mediante canales.
> **FFmpeg** — Conjunto de herramientas para procesar, convertir, capturar y transmitir audio y vídeo.
> **RTMP** — Real-Time Messaging Protocol, protocolo usado en determinados flujos de ingestión de audio y vídeo en directo.
> **HLS** — HTTP Live Streaming, sistema de distribución de audio y vídeo segmentado mediante HTTP.
> **CMD** — Instrucción de Dockerfile que define el comando predeterminado del contenedor.
> **WSL2** — Windows Subsystem for Linux 2: tecnología de Windows que ejecuta un entorno Linux mediante una máquina virtual ligera.
>
> **Criterio didáctico:** no se presupone que conocer una sigla equivalga a comprender el concepto. Primero se identifica qué significa y qué función desempeña; después se emplea en comandos, configuraciones y prácticas.

> 🧩 **ANTES DE EMPEZAR · CONCEPTOS BASE**
>
> **Protocolo** — conjunto de reglas que define cómo se comunican dos o más sistemas.
> **Cliente** — programa o equipo que inicia una petición de un servicio.
> **Servidor** — programa o equipo que ofrece un servicio y atiende peticiones.
> **Servicio de red** — aplicación o proceso que ofrece una función accesible mediante la red, normalmente a través de uno o varios puertos.
> **Proceso** — instancia en ejecución de un programa dentro de un sistema operativo.
> **Demonio (daemon)** — proceso que permanece ejecutándose en segundo plano para prestar un servicio; en Linux es habitual que esté gestionado por `systemd`.
> **Puerto** — número lógico asociado a un servicio de transporte; permite distinguir varias comunicaciones que utilizan la misma dirección IP.
> **Socket** — extremo de comunicación que combina, según el contexto, una dirección IP, un puerto y un protocolo de transporte.
> **Interfaz de red** — componente físico o virtual mediante el que un sistema se conecta a una red.
> **Dirección IP** — identificador lógico de una interfaz dentro de una red IP.
> **Subred** — porción de un espacio de direccionamiento IP que comparte un prefijo común.
> **Puerta de enlace predeterminada** — equipo al que un host entrega el tráfico destinado a redes que no conoce directamente.
> **Encaminamiento (routing)** — proceso de decidir por qué camino debe avanzar un paquete para alcanzar su destino.
> **Tabla de encaminamiento** — conjunto de rutas que utiliza un sistema para decidir dónde enviar los paquetes.
> **Broadcast o difusión** — envío dirigido a todos los equipos de un dominio de difusión.
> **Unicast** — comunicación dirigida de un emisor a un receptor concreto.
> **Multicast** — comunicación dirigida a un grupo de receptores que se han suscrito al grupo.
> **Resolución de nombres** — proceso mediante el cual un sistema obtiene información asociada a un nombre, por ejemplo una dirección IP mediante DNS.
> **Caché** — almacenamiento temporal de resultados para poder reutilizarlos sin repetir inmediatamente una consulta o cálculo.
> **Archivo de configuración** — fichero que contiene parámetros con los que un programa determina cómo debe funcionar.
> **Validación** — comprobación de que una configuración tiene una sintaxis y una estructura aceptables antes de aplicarla.
> **Estado** — situación actual de un proceso, servicio, interfaz o recurso; conocerlo es esencial para diagnosticar una incidencia.
> **Registro (log)** — anotación generada por un programa o sistema para dejar constancia de eventos, errores y operaciones.
>
> Estos conceptos son el vocabulario común sobre el que se construyen las prácticas. Cuando una unidad introduzca un concepto especializado —por ejemplo, una zona DNS, una concesión DHCP, un virtual host, un contenedor o un Pod— se explicará de nuevo antes de utilizarlo operativamente.

> 🧠 **CONCEPTOS QUE NO DEBEMOS DAR POR SUPUESTOS**
>
> **`systemd`** — sistema de inicio y gestor de servicios habitual en Linux; `systemctl` permite consultar y administrar esos servicios.
> **Archivo de configuración** — fichero que contiene los parámetros con los que un servicio determina su comportamiento.
> **Registro DNS** — entrada de una zona DNS que asocia un nombre con un dato, como una dirección IP, un servidor de correo o un alias.
> **Zona DNS** — parte de la jerarquía DNS administrada por un servidor autoritativo concreto.
> **Servidor autoritativo** — servidor que posee la información oficial de una zona DNS y puede responder con autoridad sobre ella.
> **Resolver o resolvedor** — componente que realiza consultas DNS en nombre de una aplicación o de un usuario y obtiene la respuesta siguiendo el proceso de resolución.
> **Consulta recursiva** — consulta en la que el servidor consultado asume la tarea de obtener una respuesta completa para el cliente, si tiene habilitada la recursión.
> **Consulta iterativa** — consulta en la que el servidor responde con la mejor información que conoce, pudiendo remitir al consultante hacia otro servidor.
> **Concesión DHCP** — asignación temporal de una dirección IP y otros parámetros de red a un cliente.
> **Imagen de contenedor** — plantilla inmutable a partir de la cual se crean contenedores.
> **Volumen** — almacenamiento gestionado que permite conservar datos independientemente del ciclo de vida de un contenedor.
> **Red Docker** — red virtual administrada por Docker que permite conectar contenedores y, según su configuración, publicar servicios hacia el host.
> **Orquestación** — automatización de la ejecución, escalado, recuperación y coordinación de múltiples cargas de trabajo o contenedores.
> **Pod** — unidad mínima desplegable de Kubernetes; contiene uno o varios contenedores que comparten determinados recursos.
> **Virtual host** — configuración que permite que un mismo servidor web atienda distintos sitios o nombres mediante configuraciones diferenciadas.
> **Certificado digital** — credencial criptográfica que vincula una identidad con una clave pública y que puede estar firmada por una autoridad de certificación.
> **Códec** — algoritmo que codifica y decodifica audio, vídeo u otro tipo de datos; un códec no es lo mismo que un contenedor multimedia.
> **Contenedor multimedia** — formato de archivo que agrupa una o varias pistas de audio, vídeo, subtítulos o metadatos.
> **Streaming** — distribución de contenido de forma que el receptor puede comenzar a consumirlo mientras continúa recibiendo datos.
> **Commit** — instantánea registrada por Git que conserva un conjunto concreto de cambios.
> **Staging area** — área intermedia de Git donde se seleccionan los cambios que formarán el próximo commit.
> **Rama (branch)** — línea de desarrollo independiente dentro de un repositorio Git.
> **Remoto (remote)** — referencia a un repositorio Git externo con el que se intercambian commits mediante `fetch`, `pull` o `push`.
> **Codespace** — entorno de desarrollo remoto proporcionado por GitHub para trabajar con un repositorio.
> **Webmin** — interfaz web de administración de sistemas que permite gestionar determinados servicios y parámetros de un sistema Linux.
> **Roundcube** — cliente de correo web que accede al buzón mediante IMAP y puede enviar mensajes mediante SMTP.
> **Sympa** — gestor de listas de distribución que proporciona funciones de suscripción, moderación, administración y distribución de mensajes.

> **Material docente integral · CFGS ASIR**

## 1. 🎯 Objetivos

Convertir los laboratorios en infraestructuras reproducibles y versionables, con especial atención a **redes, puertos, DNS interno, volúmenes, healthchecks y pruebas**.

## 2. 🧭 Patrón común

```text
compose.yaml
  ├── services
  ├── networks
  ├── volumes
  └── healthchecks
```

## 3. UT1 · TCP/IP

Para herramientas de diagnóstico puede utilizarse un contenedor de laboratorio:

```yaml
services:
  toolbox:
    image: nicolaka/netshoot:latest
    command: ["sleep", "infinity"]
```

```bash
docker compose up -d
docker compose exec toolbox ip addr
docker compose exec toolbox ip route
docker compose exec toolbox ss -lntup
docker compose down
```

Para prácticas de routing real se mantiene VirtualBox/Packet Tracer.

## 4. UT2 · DHCP

DHCP requiere cuidado con broadcast, interfaces y privilegios. Compose sirve para laboratorios controlados, pero las pruebas que necesitan una LAN real se realizarán en VirtualBox o Packet Tracer.

Kea debe validarse antes de iniciar:

```bash
kea-dhcp4 -t /etc/kea/kea-dhcp4.conf
```

## 5. UT3 · DNS

Arquitectura:

```text
DNS server ──┐
             ├── dnsnet ── client
```

Ejemplo conceptual:

```yaml
services:
  dns:
    image: ubuntu/bind9:latest
    ports:
      - "5353:53/udp"
      - "5353:53/tcp"
    networks: [dnsnet]

  client:
    image: alpine:latest
    command: ["sleep", "infinity"]
    networks: [dnsnet]

networks:
  dnsnet:
```

Prueba:

```bash
docker compose exec client nslookup ejemplo.test dns
```

## 6. UT4 · Transferencia

SFTP se basa en SSH. El laboratorio debe mantener el acceso limitado y no publicar credenciales reales.

```text
cliente ── SSH/SFTP ── servidor
```

Cuando se utilice una imagen de terceros, fijar una versión o digest para hacer reproducible la práctica.

## 7. UT5 · Web

```text
localhost:8080
      ↓
   Nginx
      ↓
   app:8000
```

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
    working_dir: /srv
    volumes:
      - ./app:/srv:ro
    expose: ["8000"]
    networks: [backend]

networks:
  frontend:
  backend:
```

## 8. UT6 · Correo

Arquitectura de referencia:

```text
MUA → Submission → MTA → SMTP → MTA → Mailbox → IMAP
```

El laboratorio debe ser privado y nunca convertirse en relay abierto.

## 9. UT7 · Mensajería

```text
           red-comunica
          /      |      \
       XMPP     IRC    cliente
```

Prosody, InspIRCd y herramientas equivalentes deben fijarse a versiones compatibles con la práctica.

## 10. UT8 · Multimedia

```text
FFmpeg → Icecast → VLC
FFmpeg → RTMP → Nginx → HLS → cliente
```

Separar siempre generación, codificación, distribución y reproducción.

## 11. 🔌 Regla de puertos

```text
¿Necesita acceso el host?
  ├─ sí → ports
  └─ no → red interna
```

Ejemplo:

```yaml
ports:
  - "8080:80"
```

significa **HOST 8080 → CONTENEDOR 80**.

## 12. ❤️ Healthcheck

```yaml
healthcheck:
  test: ["CMD", "wget", "--spider", "-q", "http://localhost/"]
  interval: 10s
  timeout: 3s
  retries: 5
```

Un contenedor ejecutándose no implica que la aplicación esté lista.

## 13. 🧪 Matriz de pruebas

| UT | Configuración | Arranque | Red | Funcionalidad | Diagnóstico |
|---|---|---|---|---|---|
| UT1 | ✓ | ✓ | ✓ | ✓ | ✓ |
| UT2 | ✓ | ✓ | depende del modo de red | ✓ | ✓ |
| UT3 | ✓ | ✓ | ✓ | `dig` | ✓ |
| UT4 | ✓ | ✓ | ✓ | transferencia | ✓ |
| UT5 | ✓ | ✓ | ✓ | HTTP | ✓ |
| UT6 | ✓ | ✓ | ✓ | SMTP/IMAP | ✓ |
| UT7 | ✓ | ✓ | ✓ | sesión | ✓ |
| UT8 | ✓ | ✓ | ✓ | streaming | ✓ |

## 14. ⚠️ Validación real

En el entorno de generación de esta  no existe Docker Engine ni un Codespace ejecutable. Por tanto, esta guía **no afirma haber ejecutado extremo a extremo** los ocho Compose. Antes de usar estos despliegues como evaluación práctica deben probarse en:

1. WSL2 + Docker Desktop;
2. un Codespace con Docker operativo;
3. VirtualBox para protocolos que requieren capacidades de red específicas.

## 15. 📚 Documentación oficial

- https://docs.docker.com/compose/
- https://docs.docker.com/reference/compose-file/
- https://docs.docker.com/engine/network/
- https://docs.docker.com/engine/storage/volumes/
- https://bind9.readthedocs.io/
- https://nginx.org/en/docs/
- https://www.openssh.com/manual.html
- https://www.postfix.org/documentation.html
- https://doc.dovecot.org/
- https://prosody.im/doc/
- https://icecast.org/docs/
- https://ffmpeg.org/documentation.html
