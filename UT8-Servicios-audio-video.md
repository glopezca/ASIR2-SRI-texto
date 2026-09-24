# 🎧📺⚡ Unidad de Trabajo 8 · SERVICIOS DE AUDIO Y VÍDEO ⚡🎧

> 🧭 **ANTES DE EMPEZAR · VOCABULARIO TÉCNICO**
>
> Las siglas, abreviaturas y conceptos técnicos que van a aparecer en esta unidad se presentan aquí antes de su desarrollo. La explicación local de cada tema podrá ampliar estas definiciones cuando sea necesario.
>
> **UT** — Unidad de Trabajo: unidad didáctica del módulo profesional.
> **RA** — Resultado de Aprendizaje: capacidad que el alumnado debe demostrar al finalizar un bloque curricular.
> **CFGS** — Ciclo Formativo de Grado Superior.
> **ASIR** — Administración de Sistemas Informáticos en Red.
> **SRI** — Servicios de Red e Internet.
> **NIC** — Network Interface Controller/Card, interfaz que conecta un equipo a una red.
> **WSL2** — Windows Subsystem for Linux 2: tecnología de Windows que ejecuta un entorno Linux mediante una máquina virtual ligera.
> **CLI** — Interfaz de línea de comandos, es decir, administración mediante órdenes escritas.
> **CONTENEDOR** — Instancia aislada de una imagen que comparte el núcleo del sistema anfitrión.
> **IP** — Protocolo de Internet, responsable del direccionamiento y encaminamiento de paquetes.
> **FFmpeg** — Conjunto de herramientas para procesar, convertir, capturar y transmitir audio y vídeo.
> **RTMP** — Real-Time Messaging Protocol, protocolo usado en determinados flujos de ingestión de audio y vídeo en directo.
> **HLS** — HTTP Live Streaming, sistema de distribución de audio y vídeo segmentado mediante HTTP.
> **HTTP** — Protocolo de transferencia de hipertexto utilizado principalmente por la Web.
> **MP3** — Formato de audio comprimido basado en MPEG Audio Layer III.
> **AAC** — Advanced Audio Coding, códec de audio comprimido.
> **MP4** — Formato contenedor multimedia definido en MPEG-4 Part 14.
> **MKV** — Matroska Video, formato contenedor multimedia abierto.
> **OBS** — Open Broadcaster Software, aplicación para captura, mezcla y emisión audiovisual.
> **Docker** — Plataforma de contenerización para construir, distribuir y ejecutar aplicaciones aisladas en contenedores.
> **Docker Compose** — Herramienta de Docker para definir y ejecutar aplicaciones multicontenedor mediante un archivo declarativo.
> **Git** — Sistema distribuido de control de versiones.
> **FPS** — Frames Per Second, número de imágenes de vídeo mostradas por segundo.
> **VOD** — Video on Demand, vídeo reproducido bajo demanda.
> **RTP** — Real-time Transport Protocol, protocolo para transportar medios en tiempo real.
> **SIP** — Session Initiation Protocol, protocolo de señalización para establecer y terminar sesiones multimedia.
> **PCM** — Pulse Code Modulation, representación digital de una señal de audio mediante muestras.
> **HEVC** — High Efficiency Video Coding, estándar de compresión de vídeo también conocido como H.265.
> **VP9** — Códec de vídeo desarrollado por Google.
> **AV1** — Códec de vídeo moderno y abierto diseñado para alta eficiencia de compresión.
> **WAV** — Formato de archivo de audio que suele contener audio PCM.
> **WAV/PCM** — WAV es un formato/contenedor de archivo; PCM es una representación digital de audio.
> **JPEG** — Formato de imagen comprimida ampliamente usado en fotografía.
> **PNG** — Formato de imagen comprimida sin pérdida, adecuado para gráficos y transparencia.
> **AVIF** — Formato de imagen basado en el códec AV1.
> **SVG** — Scalable Vector Graphics, formato vectorial basado en XML.
> **TCP** — Protocolo de transporte orientado a conexión que proporciona entrega fiable y ordenada.
> **URL** — Localizador uniforme de recursos: URI que además proporciona su ubicación mediante un esquema.
> **HTTP/HTTPS** — HTTP es el protocolo web; HTTPS es HTTP protegido mediante TLS.
> **HTTPS** — HTTP protegido mediante TLS.
> **RTSP** — Real Time Streaming Protocol, protocolo de control de sesiones de streaming.
> **GitHub** — Servicio de alojamiento y colaboración basado en repositorios Git.
> **DNS** — Sistema de nombres de dominio: servicio distribuido que relaciona nombres con direcciones IP y otros datos.
> **TLS** — Protocolo criptográfico que proporciona confidencialidad, integridad y autenticación mediante certificados.
> **CDN** — Content Delivery Network, red distribuida de servidores que acerca contenidos a los usuarios.
> **RTMP/HLS** — RTMP puede utilizarse para ingestión de directo; HLS distribuye segmentos mediante HTTP.
> **GET** — Método HTTP usado normalmente para solicitar una representación de un recurso.
> **SSH** — Protocolo seguro de administración remota y transporte de otros servicios.
> **BIND9** — Rama 9 de BIND, implementación de servidor DNS usada habitualmente en Linux.
> **FTP** — Protocolo de transferencia de archivos que separa un canal de control de los canales de datos.
> **SMTP** — Simple Mail Transfer Protocol, protocolo principal para transportar correo entre agentes de correo.
> **IMAP** — Internet Message Access Protocol, protocolo para acceder y gestionar mensajes que permanecen en el servidor.
> **MIME** — Multipurpose Internet Mail Extensions, mecanismo para describir tipos de contenido y adjuntos en mensajes.
> **SFTP** — Protocolo de transferencia de archivos que funciona como subsistema de SSH; no es FTP cifrado.
> **MX** — Registro DNS que identifica los servidores que reciben correo.
> **UDP** — Protocolo de transporte sin conexión, ligero y sin garantía de entrega.
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

### RA7 y RA8 · Servicios de audio y vídeo.

> **SERVICIOS DE RED E INTERNET · CFGS ASIR · Material docente integral · 2026**
>
> Material autónomo actualizado para el perfil profesional de Técnico Superior en Administración de Sistemas Informáticos en Red. Laboratorio de referencia: **Cisco Packet Tracer**, **WSL2 + Ubuntu 26.04** y **VirtualBox + Ubuntu 26.04 Server**.
>
> ### 🎯 Resultados de aprendizaje trabajados
>
> **RA7.** Administra servicios de audio identificando las necesidades de distribución y adaptando los formatos.
>
> **RA8.** Administra servicios de vídeo identificando las necesidades de distribución y adaptando los formatos.
>
> La UT8 se divide conceptualmente en los servicios de audio y de vídeo para mantener la correspondencia curricular.

---

> 🎯 **MISIÓN DE LA UT**
>
> Comprender cómo se distribuyen contenidos audiovisuales por una red y ser
> capaz de **identificar formatos, elegir códecs, desplegar servicios de
> streaming, configurar clientes y diagnosticar problemas de reproducción y
> transmisión**.
>
> El laboratorio se construirá progresivamente:
>
> ```text
> fichero multimedia
>       ↓
> códec / contenedor
>       ↓
> servidor
>       ↓
> protocolo de distribución
>       ↓
> red
>       ↓
> cliente
>       ↓
> reproducción
> ```

---

# 📚 1. Estructura de la unidad

La estructura de referencia para esta unidad gira alrededor de:

```text
8.1  Introducción
8.2  Formatos multimedia
8.3  Herramientas de reproducción multimedia
8.4  Streaming
8.5  Distribución y suscripción de audio y vídeo
8.6  Tecnología de Voz IP (VoIP)
8.7  Servicios de videoconferencia
8.8  Prácticas resueltas
8.9  Prácticas propuestas
8.10 Resumen
8.11 Test de repaso
8.12 Comprueba tu aprendizaje
```

La organización coincide con índices publicados para el módulo que incluyen
formatos multimedia, reproducción, streaming, distribución/suscripción,
VoIP, videoconferencia y bloques finales de prácticas, resumen y evaluación.


> 🔄 **Actualización tecnológica**
>
> El contenido conceptual se conserva, pero las prácticas se trasladan a
> tecnologías actuales:
>
> - 🐧 **VirtualBox + Ubuntu 26.04 Server**
> - 🐧 **WSL2 + Ubuntu 26.04**
> - 🎧 **Icecast** para streaming de audio
> - 🎬 **FFmpeg** para codificación y pruebas
> - 📺 **Nginx + RTMP** como laboratorio de vídeo en directo
> - 🌐 **HLS** para distribución HTTP de vídeo
> - ▶️ **VLC** como cliente multimedia
> - 🖧 **Cisco Packet Tracer** para representar la infraestructura de red.
>
> La elección de estas herramientas es una actualización práctica del
> contenido, no una reproducción literal de una implementación histórica.

---

# 🧭 2. Mapa de la unidad

```text
                           🎧📺 MULTIMEDIA
                                  │
          ┌───────────────────────┼───────────────────────┐
          │                       │                       │
        AUDIO                   VÍDEO                  TIEMPO REAL
          │                       │                       │
       códec                   códec                  streaming
          │                       │                       │
      contenedor             contenedor                 │
          │                       │                ┌─────┴─────┐
          │                       │                │           │
       MP3/Ogg/AAC          MP4/WebM/MKV          HLS        RTMP
          │                       │                │           │
          └───────────────┬───────┘                │           │
                          ▼                        ▼           ▼
                       CLIENTE                  navegador    OBS/FFmpeg
                          │
                          ▼
                         VLC
        🧪 I Packet Tracer · II WSL2 · III VirtualBox · IV Docker Compose
```

---


> 🧪 **LOS CUATRO ENTORNOS DE PRÁCTICAS**
>
> **I · Cisco Packet Tracer** — simulación de red y protocolos.  
> **II · WSL2 + Ubuntu 26.04** — herramientas, clientes y diagnóstico.  
> **III · VirtualBox + Ubuntu 26.04 Server** — administración de servidores completos.  
> **IV · Docker Compose** — infraestructura reproducible y multicontenedor.


# 🎯 3. Objetivos

Al terminar esta UT deberás poder:

- Explicar qué es un servicio multimedia.
- Diferenciar **formato**, **códec** y **contenedor**.
- Explicar el muestreo y la cuantificación del audio digital.
- Interpretar frecuencia de muestreo, profundidad de bits y bitrate.
- Identificar formatos habituales de audio.
- Identificar formatos de imagen.
- Identificar formatos y códecs de vídeo.
- Explicar resolución, FPS, bitrate y relación de aspecto.
- Utilizar herramientas de reproducción multimedia.
- Explicar qué es streaming.
- Diferenciar descarga progresiva y streaming en tiempo real.
- Diferenciar unicast y multicast conceptualmente.
- Comprender streaming bajo HTTP.
- Comprender RTMP y HLS.
- Instalar y configurar un servidor de audio.
- Utilizar Icecast.
- Publicar un stream de audio.
- Utilizar VLC como cliente.
- Utilizar FFmpeg para generar streams.
- Crear un flujo de vídeo de laboratorio.
- Comprender la arquitectura de un servidor RTMP.
- Generar HLS.
- Comprender podcast y vodcast.
- Explicar VoIP.
- Explicar RTP, SIP y señalización.
- Comprender la arquitectura básica de videoconferencia.
- Diagnosticar problemas de bitrate, red, códec, puertos y reproducción.
- Documentar un servicio multimedia reproducible.

---

> 🧭 **ANTES DE EMPEZAR · Señal digital**
>
> Para representar audio digital debemos convertir una señal continua en muestras discretas. Los conceptos de **frecuencia de muestreo, profundidad de bits y bitrate** permiten cuantificar qué información estamos conservando y cuánto ancho de banda/almacenamiento necesitamos.

# 🎵 4. Audio digital

Una señal de audio analógica es continua.

Para procesarla digitalmente se realiza, de forma simplificada:

```text
SEÑAL ANALÓGICA
       │
       ▼
   MUESTREO
       │
       ▼
 CUANTIFICACIÓN
       │
       ▼
   CODIFICACIÓN
       │
       ▼
 AUDIO DIGITAL
```

---

# 📐 5. Frecuencia de muestreo

La frecuencia de muestreo indica cuántas muestras se toman por segundo.

Se expresa en:

```text
Hz
kHz
```

Ejemplo:

```text
44.100 Hz
```

significa:

```text
44.100 muestras / segundo
```

Un audio:

```text
44,1 kHz
```

contiene 44.100 muestras por segundo y canal.

---

# 🔢 6. Profundidad de bits

La profundidad de bits determina cuántos niveles de amplitud pueden
representarse.

Ejemplo:

```text
8 bits  → 256 niveles
16 bits → 65.536 niveles
24 bits → 16.777.216 niveles
```

La relación es:

```text
niveles = 2^bits
```

---

# 📦 7. Bitrate de audio PCM

Para PCM sin compresión:

```text
bitrate =
frecuencia_muestreo × bits_por_muestra × canales
```

Ejemplo:

```text
44.100 × 16 × 2
```

resultado:

```text
1.411.200 bit/s
```

o aproximadamente:

```text
1.411,2 kbit/s
```

Esto explica por qué un formato PCM ocupa mucho más que un audio comprimido.

---

> 🧭 **ANTES DE EMPEZAR · Códec**
>
> Un códec es el mecanismo que codifica y/o decodifica contenido audiovisual. No debe confundirse con el contenedor: el códec describe cómo se representa el flujo y el contenedor cómo se empaquetan uno o varios flujos junto con metadatos.

> 🧭 **PREPARACIÓN DIDÁCTICA**
>
> 🧭 **ANTES DE EMPEZAR · TRES CAPAS QUE NO DEBES CONFUNDIR**
> 
> Antes de trabajar con FFmpeg, separa tres conceptos: **códec** (cómo se codifica), **contenedor** (cómo se empaquetan las pistas) y **protocolo de distribución** (cómo llegan los datos al cliente). Confundirlos produce muchos errores de configuración.

# 🧠 8. Códec

Un **códec** es un algoritmo o conjunto de algoritmos para codificar y
decodificar contenido.

```text
CODIFICADOR
     │
     ▼
audio/vídeo comprimido
     │
     ▼
DECODIFICADOR
     │
     ▼
reproducción
```

Ejemplos:

```text
Audio:
MP3
AAC
Opus
Vorbis

Vídeo:
H.264/AVC
H.265/HEVC
VP9
AV1
```

> ⚠️ No confundas códec con contenedor.

---

# 📦 9. Contenedor

El contenedor organiza uno o varios flujos multimedia y metadatos.

Por ejemplo:

```text
┌─────────────────────────────┐
│           MP4               │
│                             │
│  vídeo → H.264              │
│  audio → AAC                │
│  metadatos                  │
└─────────────────────────────┘
```

Otro ejemplo:

```text
┌─────────────────────────────┐
│           MKV               │
│                             │
│  vídeo → AV1                │
│  audio → Opus               │
│  subtítulos                 │
└─────────────────────────────┘
```

---

# 🧩 10. Códec ≠ contenedor ≠ formato

Una forma útil de recordarlo:

```text
CONTENEDOR
    │
    ├── vídeo → CÓDEC
    ├── audio → CÓDEC
    ├── subtítulos
    └── metadatos
```

Ejemplo:

```text
pelicula.mkv
    │
    ├── vídeo: H.264
    ├── audio: AAC
    └── subtítulos: SRT
```

La extensión:

```text
.mkv
```

no nos dice por sí sola qué códecs contiene.

---

# 🎧 11. Formatos de audio

| Formato/códec | Tipo | Característica |
|---|---|---|
| WAV/PCM | Sin compresión habitual | Gran tamaño |
| FLAC | Sin pérdida | Reduce tamaño sin perder información |
| MP3 | Con pérdida | Muy extendido |
| AAC | Con pérdida | Muy utilizado en distribución |
| Ogg Vorbis | Con pérdida | Formato abierto |
| Opus | Con pérdida | Voz, música y comunicaciones |
| ALAC | Sin pérdida | Audio lossless |

---

# 🎬 12. Formatos de vídeo

| Contenedor | Ejemplo de vídeo | Uso |
|---|---|---|
| MP4 | H.264/H.265 | Distribución general |
| WebM | VP9/AV1 | Web |
| MKV | múltiples códecs | Contenedor flexible |
| MOV | H.264/HEVC, etc. | Ecosistema multimedia |
| MPEG-TS | MPEG/H.264/H.265 | Transporte/broadcast |

---

# 🖼️ 13. Formatos de imagen

La imagen también forma parte del ecosistema multimedia.

```text
JPEG
PNG
GIF
WebP
AVIF
SVG
```

### Mapa rápido

```text
JPEG  → fotografías
PNG   → transparencia / gráficos
WebP  → web
AVIF  → alta eficiencia
SVG   → vectorial
```

---

# 📐 14. Vídeo: resolución

La resolución indica normalmente:

```text
ancho × alto
```

Ejemplos:

```text
1280 × 720
1920 × 1080
3840 × 2160
```

Con frecuencia:

```text
720p  → 1280×720
1080p → 1920×1080
2160p → 3840×2160
```

---

# 🎞️ 15. FPS

FPS significa:

```text
Frames Per Second
```

Ejemplos:

```text
24 fps
25 fps
30 fps
50 fps
60 fps
```

A mayor FPS:

```text
más imágenes por segundo
→ potencialmente más fluidez
→ potencialmente más datos/procesamiento
```

---

# 📊 16. Bitrate de vídeo
### 📊 Conceptos audiovisuales que no deben confundirse

| Concepto | Responde a | Ejemplo |
|---|---|---|
| Códec | ¿Cómo se codifica el flujo? | H.264, AV1, Opus |
| Contenedor | ¿Cómo se empaquetan los flujos? | MP4, Matroska, WebM |
| Resolución | ¿Cuántos píxeles tiene cada imagen? | 1920×1080 |
| FPS | ¿Cuántas imágenes por segundo? | 25 fps |
| Bitrate | ¿Cuántos bits/s se transmiten? | 4 Mb/s |
| Latencia | ¿Cuánto tarda en llegar/procesarse? | 2 s |



El bitrate indica la cantidad de bits utilizados por unidad de tiempo.

Ejemplo:

```text
4 Mbit/s
```

significa aproximadamente:

```text
4 millones de bits por segundo
```

El bitrate afecta directamente:

```text
calidad
tamaño
ancho de banda
```

Pero la calidad no depende únicamente del bitrate.

También depende de:

```text
códec
resolución
FPS
contenido
perfil
preset
escena
```

---

# 📐 17. Relación de aspecto

Ejemplos:

```text
4:3
16:9
21:9
```

Para:

```text
1920×1080
```

tenemos:

```text
1920 / 1080 = 16 / 9
```

---


---

# 🗂️ Antes de las prácticas · localizar la configuración multimedia

En multimedia hay que separar **fichero de medios, proceso de codificación y servidor de distribución**. Localizar el fichero correcto antes de editar evita modificar una configuración que no está siendo utilizada.

### Icecast

```text
/etc/icecast2/               → configuración del servidor
/etc/icecast2/icecast.xml    → configuración principal
/var/log/icecast2/           → logs, según instalación
```

### Nginx + RTMP

```text
/etc/nginx/nginx.conf        → configuración principal
/etc/nginx/conf.d/           → fragmentos adicionales, si se utilizan
/var/log/nginx/              → logs
```

Comandos:
```bash
sudo icecast2 -c /etc/icecast2/icecast.xml -b
sudo nginx -t
sudo nginx -T | less
sudo ss -lntup
```

### 🖥️ Webmin

La administración multimedia depende de los módulos disponibles. La CLI sigue siendo la referencia: localiza el fichero, valida la configuración y comprueba los puertos antes de utilizar cualquier interfaz gráfica.



> 👨‍🏫 **Criterio de corrección de las prácticas**
>
> La solución de referencia no se reduce a una configuración final. Se valoran el proceso, la capacidad para localizar ficheros, validar la sintaxis, comprobar puertos y conectividad, interpretar logs y justificar técnicamente cada decisión. Cuando el ejercicio admita varias soluciones, cualquier solución equivalente y correctamente justificada es válida.
# 🧪 18. PRÁCTICA 8.1 — Inspección multimedia
> 🧭 **PREPARACIÓN DE LA PRÁCTICA**
>
> **1 · Sitúate.** Lee primero el objetivo y localiza en la unidad el concepto que estamos llevando a la práctica. No empieces copiando comandos: primero debes poder explicar qué componente estamos construyendo y para qué sirve.
>
> **2 · Prepara el entorno.** Comprueba si esta práctica utiliza **Entorno I · Packet Tracer**, **Entorno II · WSL2**, **Entorno III · VirtualBox + Ubuntu 26.04 Server** o **Entorno IV · Docker Compose**. Verifica conectividad, nombres, interfaces y estado de los servicios antes de modificar nada.
>
> **3 · Predice.** Antes de ejecutar un comando importante, escribe qué esperas que ocurra. Por ejemplo: «después de `ss -lnt`, espero encontrar el servicio escuchando en TCP/80». Esta pequeña predicción convierte la práctica en una investigación y no en una receta.
>
> **4 · Construye paso a paso.** Cada número debe dejar el sistema en un estado ligeramente más completo que el anterior. Después de cada bloque, realiza una comprobación corta. Si el paso 4 depende del 3, no avances hasta que el 3 funcione.
>
> **5 · Diagnostica si falla.** No empieces reiniciando. Sigue esta secuencia: **estado → configuración → logs → puertos → red → prueba desde el cliente**. Conserva las órdenes utilizadas y la evidencia del fallo.
>
> **6 · Demuestra.** La práctica termina cuando puedes demostrar el resultado con una evidencia: captura, salida de comando, conexión desde cliente, fichero de configuración o tráfico observado.
>
> **7 · Explica.** Cierra con una breve explicación técnica: qué has configurado, qué protocolo interviene, qué puerto utiliza, cómo se verifica y qué error sería el primero que investigarías si dejara de funcionar.




Instala FFmpeg:

```bash
sudo apt update
sudo apt install ffmpeg
```

Consulta un fichero:

```bash
ffprobe video.mp4
```

También:

```bash
ffprobe -v error \
  -show_entries stream=index,codec_name,codec_type,width,height,r_frame_rate,bit_rate \
  video.mp4
```

Identifica:

```text
contenedor
códec de vídeo
códec de audio
resolución
FPS
bitrate
```

---


### 🧭 Guía de resolución y comprobación

Esta práctica se considera resuelta cuando puedes **explicar y demostrar** el resultado, no solo cuando el comando termina sin errores. Sigue siempre esta secuencia:

1. **Identifica el estado inicial.** Anota interfaces, direcciones, rutas y servicios que ya estaban activos.
2. **Aplica el cambio mínimo.** No modifiques varias cosas a la vez: si algo falla, necesitas saber qué cambio lo provocó.
3. **Valida inmediatamente.** Comprueba la sintaxis o el estado del servicio antes de probar desde el cliente.
4. **Prueba desde el punto de vista del usuario.** Una configuración correcta debe producir el comportamiento esperado desde el cliente, no solo desde el servidor.
5. **Observa evidencias.** Conserva la salida de comandos, logs, capturas de tráfico y capturas de pantalla que demuestren el resultado.

**Comandos de referencia para esta práctica:**

- `ip addr`
- `ip route`
- `ss -lntup`
- `journalctl -b --no-pager`
- `ping <destino>`

> 💡 **Si algo falla:** no empieces reiniciando. Compara primero **estado → configuración → logs → puertos → red → cliente**. Un reinicio puede ocultar la causa y hacer más difícil aprender de la incidencia.

### 🧪 Rúbrica de evaluación

| Criterio | Puntos | Evidencia esperada |
|---|---:|---|
| Comprensión del objetivo y del protocolo | 2 | Explica qué servicio/protocolo está utilizando y por qué. |
| Preparación y configuración | 2 | Ficheros, comandos o topología correctamente preparados. |
| Verificación funcional | 2 | Demuestra el resultado desde un cliente o herramienta adecuada. |
| Diagnóstico y razonamiento | 2 | Utiliza evidencias para justificar la solución. |
| Documentación técnica | 1 | Incluye comandos, configuraciones y capturas relevantes. |
| Seguridad y buenas prácticas | 1 | Aplica permisos, exposición de puertos y credenciales con criterio. |
| **Total** | **10** | **Superación recomendada: ≥ 5 puntos y práctica funcional.** |


# 🧪 19. PRÁCTICA 8.2 — Comparar contenedores
> 🧭 **PREPARACIÓN DE LA PRÁCTICA**
>
> **1 · Sitúate.** Lee primero el objetivo y localiza en la unidad el concepto que estamos llevando a la práctica. No empieces copiando comandos: primero debes poder explicar qué componente estamos construyendo y para qué sirve.
>
> **2 · Prepara el entorno.** Comprueba si esta práctica utiliza **Entorno I · Packet Tracer**, **Entorno II · WSL2**, **Entorno III · VirtualBox + Ubuntu 26.04 Server** o **Entorno IV · Docker Compose**. Verifica conectividad, nombres, interfaces y estado de los servicios antes de modificar nada.
>
> **3 · Predice.** Antes de ejecutar un comando importante, escribe qué esperas que ocurra. Por ejemplo: «después de `ss -lnt`, espero encontrar el servicio escuchando en TCP/80». Esta pequeña predicción convierte la práctica en una investigación y no en una receta.
>
> **4 · Construye paso a paso.** Cada número debe dejar el sistema en un estado ligeramente más completo que el anterior. Después de cada bloque, realiza una comprobación corta. Si el paso 4 depende del 3, no avances hasta que el 3 funcione.
>
> **5 · Diagnostica si falla.** No empieces reiniciando. Sigue esta secuencia: **estado → configuración → logs → puertos → red → prueba desde el cliente**. Conserva las órdenes utilizadas y la evidencia del fallo.
>
> **6 · Demuestra.** La práctica termina cuando puedes demostrar el resultado con una evidencia: captura, salida de comando, conexión desde cliente, fichero de configuración o tráfico observado.
>
> **7 · Explica.** Cierra con una breve explicación técnica: qué has configurado, qué protocolo interviene, qué puerto utiliza, cómo se verifica y qué error sería el primero que investigarías si dejara de funcionar.




Utiliza un mismo contenido y genera:

```text
video.mp4
video.mkv
video.webm
```

Comprueba:

```bash
ffprobe video.mp4
ffprobe video.mkv
ffprobe video.webm
```

Responde:

> ¿Cambiar la extensión cambia necesariamente el códec?

---


### 🧭 Guía de resolución y comprobación

Esta práctica se considera resuelta cuando puedes **explicar y demostrar** el resultado, no solo cuando el comando termina sin errores. Sigue siempre esta secuencia:

1. **Identifica el estado inicial.** Anota interfaces, direcciones, rutas y servicios que ya estaban activos.
2. **Aplica el cambio mínimo.** No modifiques varias cosas a la vez: si algo falla, necesitas saber qué cambio lo provocó.
3. **Valida inmediatamente.** Comprueba la sintaxis o el estado del servicio antes de probar desde el cliente.
4. **Prueba desde el punto de vista del usuario.** Una configuración correcta debe producir el comportamiento esperado desde el cliente, no solo desde el servidor.
5. **Observa evidencias.** Conserva la salida de comandos, logs, capturas de tráfico y capturas de pantalla que demuestren el resultado.

**Comandos de referencia para esta práctica:**

- `ip addr`
- `ip route`
- `ss -lntup`
- `journalctl -b --no-pager`
- `ping <destino>`

> 💡 **Si algo falla:** no empieces reiniciando. Compara primero **estado → configuración → logs → puertos → red → cliente**. Un reinicio puede ocultar la causa y hacer más difícil aprender de la incidencia.

### 🧪 Rúbrica de evaluación

| Criterio | Puntos | Evidencia esperada |
|---|---:|---|
| Comprensión del objetivo y del protocolo | 2 | Explica qué servicio/protocolo está utilizando y por qué. |
| Preparación y configuración | 2 | Ficheros, comandos o topología correctamente preparados. |
| Verificación funcional | 2 | Demuestra el resultado desde un cliente o herramienta adecuada. |
| Diagnóstico y razonamiento | 2 | Utiliza evidencias para justificar la solución. |
| Documentación técnica | 1 | Incluye comandos, configuraciones y capturas relevantes. |
| Seguridad y buenas prácticas | 1 | Aplica permisos, exposición de puertos y credenciales con criterio. |
| **Total** | **10** | **Superación recomendada: ≥ 5 puntos y práctica funcional.** |


# ▶️ 20. Herramientas de reproducción

En el laboratorio utilizaremos principalmente:

```text
VLC
ffplay
navegador web
```

VLC resulta especialmente útil porque permite reproducir:

```text
archivos
URLs
streams
listas
```

---

# 🧪 21. PRÁCTICA 8.3 — VLC
> 🧭 **PREPARACIÓN DE LA PRÁCTICA**
>
> **1 · Sitúate.** Lee primero el objetivo y localiza en la unidad el concepto que estamos llevando a la práctica. No empieces copiando comandos: primero debes poder explicar qué componente estamos construyendo y para qué sirve.
>
> **2 · Prepara el entorno.** Comprueba si esta práctica utiliza **Entorno I · Packet Tracer**, **Entorno II · WSL2**, **Entorno III · VirtualBox + Ubuntu 26.04 Server** o **Entorno IV · Docker Compose**. Verifica conectividad, nombres, interfaces y estado de los servicios antes de modificar nada.
>
> **3 · Predice.** Antes de ejecutar un comando importante, escribe qué esperas que ocurra. Por ejemplo: «después de `ss -lnt`, espero encontrar el servicio escuchando en TCP/80». Esta pequeña predicción convierte la práctica en una investigación y no en una receta.
>
> **4 · Construye paso a paso.** Cada número debe dejar el sistema en un estado ligeramente más completo que el anterior. Después de cada bloque, realiza una comprobación corta. Si el paso 4 depende del 3, no avances hasta que el 3 funcione.
>
> **5 · Diagnostica si falla.** No empieces reiniciando. Sigue esta secuencia: **estado → configuración → logs → puertos → red → prueba desde el cliente**. Conserva las órdenes utilizadas y la evidencia del fallo.
>
> **6 · Demuestra.** La práctica termina cuando puedes demostrar el resultado con una evidencia: captura, salida de comando, conexión desde cliente, fichero de configuración o tráfico observado.
>
> **7 · Explica.** Cierra con una breve explicación técnica: qué has configurado, qué protocolo interviene, qué puerto utiliza, cómo se verifica y qué error sería el primero que investigarías si dejara de funcionar.




Instala VLC en el cliente que corresponda.

Desde terminal:

```bash
vlc video.mp4
```

Prueba después:

```text
Media → Open Network Stream
```

Introduce una URL HTTP de prueba.

### Objetivo

Distinguir:

```text
fichero local
      ≠
recurso remoto
      ≠
stream en directo
```

---

> 🧭 **ANTES DE EMPEZAR · Streaming**
>
> Streaming no significa simplemente «descargar un archivo lentamente». El cliente comienza a reproducir mientras los datos siguen llegando. Esto introduce conceptos nuevos: **buffer, latencia, bitrate sostenido y adaptación a las condiciones de red**.

> 🧭 **PREPARACIÓN DIDÁCTICA**
>
> 🧭 **ANTES DE EMPEZAR · TRANSMISIÓN FRENTE A DESCARGA**
> 
> En una descarga tradicional, el archivo completo es el objeto principal. En streaming, el cliente empieza a reproducir mientras siguen llegando datos. Esta diferencia introduce búfer, latencia, bitrate y tolerancia a pérdidas.


### 🧭 Guía de resolución y comprobación

Esta práctica se considera resuelta cuando puedes **explicar y demostrar** el resultado, no solo cuando el comando termina sin errores. Sigue siempre esta secuencia:

1. **Identifica el estado inicial.** Anota interfaces, direcciones, rutas y servicios que ya estaban activos.
2. **Aplica el cambio mínimo.** No modifiques varias cosas a la vez: si algo falla, necesitas saber qué cambio lo provocó.
3. **Valida inmediatamente.** Comprueba la sintaxis o el estado del servicio antes de probar desde el cliente.
4. **Prueba desde el punto de vista del usuario.** Una configuración correcta debe producir el comportamiento esperado desde el cliente, no solo desde el servidor.
5. **Observa evidencias.** Conserva la salida de comandos, logs, capturas de tráfico y capturas de pantalla que demuestren el resultado.

**Comandos de referencia para esta práctica:**

- `ip addr`
- `ip route`
- `ss -lntup`
- `journalctl -b --no-pager`
- `ping <destino>`

> 💡 **Si algo falla:** no empieces reiniciando. Compara primero **estado → configuración → logs → puertos → red → cliente**. Un reinicio puede ocultar la causa y hacer más difícil aprender de la incidencia.

### 🧪 Rúbrica de evaluación

| Criterio | Puntos | Evidencia esperada |
|---|---:|---|
| Comprensión del objetivo y del protocolo | 2 | Explica qué servicio/protocolo está utilizando y por qué. |
| Preparación y configuración | 2 | Ficheros, comandos o topología correctamente preparados. |
| Verificación funcional | 2 | Demuestra el resultado desde un cliente o herramienta adecuada. |
| Diagnóstico y razonamiento | 2 | Utiliza evidencias para justificar la solución. |
| Documentación técnica | 1 | Incluye comandos, configuraciones y capturas relevantes. |
| Seguridad y buenas prácticas | 1 | Aplica permisos, exposición de puertos y credenciales con criterio. |
| **Total** | **10** | **Superación recomendada: ≥ 5 puntos y práctica funcional.** |


# 🌊 22. ¿Qué es streaming?

Streaming es una técnica de distribución en la que el contenido puede comenzar
a reproducirse mientras se recibe.

```text
SERVIDOR
   │
   │ datos
   ▼
CLIENTE
   │
   ├──► búfer
   │
   └──► reproducción
```

No es necesario esperar a disponer de todo el contenido.

---

# 📥 23. Descarga frente a streaming

## Descarga tradicional

```text
SERVIDOR
   │
   ▼
████████████████████
        │
        ▼
     fichero
        │
        ▼
   reproducción
```

## Streaming

```text
SERVIDOR
   │
   ▼
███
 │
 ▼
reproduce
 │
 ▼
████
 │
 ▼
sigue reproduciendo
```

---

# 🧠 24. Búfer

El cliente mantiene una cantidad de datos temporalmente.

```text
          RED
           │
           ▼
      ┌──────────┐
      │  BÚFER   │
      └────┬─────┘
           │
           ▼
      REPRODUCTOR
```

Si la tasa de llegada es inferior a la tasa necesaria de reproducción:

```text
búfer ↓↓↓
     ↓
  buffering
```

---

# 📊 25. Condición básica de streaming

De forma simplificada:

```text
tasa de recepción ≥ tasa de reproducción
```

Si:

```text
vídeo = 5 Mbit/s
red efectiva = 2 Mbit/s
```

el cliente terminará quedándose sin datos.

Pero una red con suficiente ancho de banda tampoco garantiza una reproducción
perfecta.

También importan:

```text
latencia
jitter
pérdidas
CPU
decodificación
búfer
servidor
```

---

# 🔄 26. Streaming bajo demanda y directo

## VOD

```text
Video On Demand
```

El usuario solicita contenido almacenado.

```text
película
curso
grabación
vídeo educativo
```

## Live

Contenido generado en directo:

```text
cámara
  ↓
codificador
  ↓
servidor
  ↓
clientes
```

---

# 🌐 27. Arquitectura de streaming

```text
              FUENTE
                │
                ▼
          CODIFICADOR
                │
                ▼
         SERVIDOR MEDIA
                │
       ┌────────┼────────┐
       │        │        │
      C1       C2       C3
       │        │        │
       ▼        ▼        ▼
     VLC      navegador  móvil
```

---

# 🧱 28. Componentes

Un sistema puede contener:

```text
1. Fuente
2. Capturadora
3. Codificador
4. Servidor
5. Red
6. Cliente
7. Reproductor
```

Ejemplo:

```text
Micrófono
   │
   ▼
FFmpeg / IceS
   │
   ▼
Icecast
   │
   ▼
VLC
```

---

# 📡 29. Protocolos multimedia

Dependiendo de la arquitectura podemos encontrar:

```text
HTTP/HTTPS
HLS
RTMP
RTP
RTSP
WebRTC
SIP
```

No todos cumplen la misma función.

```text
HTTP/HLS → distribución
RTMP     → ingest / streaming
RTP      → transporte multimedia en tiempo real
RTSP     → control de sesiones multimedia
SIP      → señalización VoIP
WebRTC   → comunicación multimedia interactiva
```

---

> 🧭 **ANTES DE EMPEZAR · Icecast**
>
> Icecast es un servidor de streaming de audio. Utilizaremos el concepto de **mountpoint** para identificar el flujo publicado y conectaremos un origen de audio con clientes que consumen ese flujo.

> 🧭 **PREPARACIÓN DIDÁCTICA**
>
> 🧭 **ANTES DE EMPEZAR · SERVIDOR DE AUDIO EN DIRECTO**
> 
> Icecast no genera el audio: recibe un flujo producido por una fuente y lo distribuye a clientes. La separación fuente → servidor → oyentes será la clave para entender el laboratorio.

# 🎧 30. Icecast

Icecast es un servidor orientado a streaming, especialmente habitual en
radio por Internet.

Arquitectura:

```text
FUENTE
  │
  │ stream
  ▼
┌──────────────┐
│   ICECAST    │
│              │
│ /radio.ogg   │
│ /radio.mp3   │
└──────┬───────┘
       │
   ┌───┼───┐
   ▼   ▼   ▼
  C1  C2  C3
```

Icecast utiliza **mountpoints** para identificar streams independientes. Un
mismo servidor puede alojar varios streams. 

---

# 🔌 31. Icecast y mountpoints

Ejemplo:

```text
/radio.mp3
```

o:

```text
/radio.ogg
```

Cada mountpoint identifica un stream.

```text
Icecast
   │
   ├── /rock.mp3
   ├── /jazz.ogg
   └── /classical.ogg
```

La documentación de Icecast describe los mountpoints como identificadores
únicos de cada broadcast/stream y permite configurar parámetros específicos
por mountpoint. 

---

# 🧪 32. PRÁCTICA 8.4 — Instalar Icecast
> 🧭 **PREPARACIÓN DE LA PRÁCTICA**
>
> **1 · Sitúate.** Lee primero el objetivo y localiza en la unidad el concepto que estamos llevando a la práctica. No empieces copiando comandos: primero debes poder explicar qué componente estamos construyendo y para qué sirve.
>
> **2 · Prepara el entorno.** Comprueba si esta práctica utiliza **Entorno I · Packet Tracer**, **Entorno II · WSL2**, **Entorno III · VirtualBox + Ubuntu 26.04 Server** o **Entorno IV · Docker Compose**. Verifica conectividad, nombres, interfaces y estado de los servicios antes de modificar nada.
>
> **3 · Predice.** Antes de ejecutar un comando importante, escribe qué esperas que ocurra. Por ejemplo: «después de `ss -lnt`, espero encontrar el servicio escuchando en TCP/80». Esta pequeña predicción convierte la práctica en una investigación y no en una receta.
>
> **4 · Construye paso a paso.** Cada número debe dejar el sistema en un estado ligeramente más completo que el anterior. Después de cada bloque, realiza una comprobación corta. Si el paso 4 depende del 3, no avances hasta que el 3 funcione.
>
> **5 · Diagnostica si falla.** No empieces reiniciando. Sigue esta secuencia: **estado → configuración → logs → puertos → red → prueba desde el cliente**. Conserva las órdenes utilizadas y la evidencia del fallo.
>
> **6 · Demuestra.** La práctica termina cuando puedes demostrar el resultado con una evidencia: captura, salida de comando, conexión desde cliente, fichero de configuración o tráfico observado.
>
> **7 · Explica.** Cierra con una breve explicación técnica: qué has configurado, qué protocolo interviene, qué puerto utiliza, cómo se verifica y qué error sería el primero que investigarías si dejara de funcionar.




En **VirtualBox + Ubuntu 26.04 Server**:

```bash
sudo apt update
sudo apt install icecast2
```

Comprueba:

```bash
systemctl status icecast2
```

Y:

```bash
ss -ltnp | grep 8000
```

> ℹ️ La disponibilidad exacta del paquete y los nombres de servicio pueden
> variar según la distribución/repositorio. Comprueba siempre:
>
> ```bash
> apt policy icecast2
> ```

---


### 🧭 Guía de resolución y comprobación

Esta práctica se considera resuelta cuando puedes **explicar y demostrar** el resultado, no solo cuando el comando termina sin errores. Sigue siempre esta secuencia:

1. **Identifica el estado inicial.** Anota interfaces, direcciones, rutas y servicios que ya estaban activos.
2. **Aplica el cambio mínimo.** No modifiques varias cosas a la vez: si algo falla, necesitas saber qué cambio lo provocó.
3. **Valida inmediatamente.** Comprueba la sintaxis o el estado del servicio antes de probar desde el cliente.
4. **Prueba desde el punto de vista del usuario.** Una configuración correcta debe producir el comportamiento esperado desde el cliente, no solo desde el servidor.
5. **Observa evidencias.** Conserva la salida de comandos, logs, capturas de tráfico y capturas de pantalla que demuestren el resultado.

**Comandos de referencia para esta práctica:**

- `ffprobe <fichero>`
- `ss -lntup`
- `sudo nginx -t`
- `sudo systemctl status icecast2 nginx`
- `curl -I http://<stream-host>/`

> 💡 **Si algo falla:** no empieces reiniciando. Compara primero **estado → configuración → logs → puertos → red → cliente**. Un reinicio puede ocultar la causa y hacer más difícil aprender de la incidencia.

### 🧪 Rúbrica de evaluación

| Criterio | Puntos | Evidencia esperada |
|---|---:|---|
| Comprensión del objetivo y del protocolo | 2 | Explica qué servicio/protocolo está utilizando y por qué. |
| Preparación y configuración | 2 | Ficheros, comandos o topología correctamente preparados. |
| Verificación funcional | 2 | Demuestra el resultado desde un cliente o herramienta adecuada. |
| Diagnóstico y razonamiento | 2 | Utiliza evidencias para justificar la solución. |
| Documentación técnica | 1 | Incluye comandos, configuraciones y capturas relevantes. |
| Seguridad y buenas prácticas | 1 | Aplica permisos, exposición de puertos y credenciales con criterio. |
| **Total** | **10** | **Superación recomendada: ≥ 5 puntos y práctica funcional.** |


# ⚙️ 33. Configuración de Icecast

El fichero habitual es:

```text
/etc/icecast2/icecast.xml
```

Parámetros importantes:

```text
listen socket
source password
relay password
admin credentials
mountpoints
limits
logging
```

La documentación de Icecast organiza la configuración en límites,
autenticación, relays, mountpoints, rutas, logging y seguridad.


---

# 🔐 34. Contraseñas de Icecast

Debes diferenciar:

```text
source password
relay password
admin password
```

No utilices:

```text
1234
admin
password
```

aunque sea un laboratorio.

Utiliza credenciales de laboratorio claramente identificadas y no las
publiques en GitHub.

---

# 🧪 35. PRÁCTICA 8.5 — Configurar Icecast
> 🧭 **PREPARACIÓN DE LA PRÁCTICA**
>
> **1 · Sitúate.** Lee primero el objetivo y localiza en la unidad el concepto que estamos llevando a la práctica. No empieces copiando comandos: primero debes poder explicar qué componente estamos construyendo y para qué sirve.
>
> **2 · Prepara el entorno.** Comprueba si esta práctica utiliza **Entorno I · Packet Tracer**, **Entorno II · WSL2**, **Entorno III · VirtualBox + Ubuntu 26.04 Server** o **Entorno IV · Docker Compose**. Verifica conectividad, nombres, interfaces y estado de los servicios antes de modificar nada.
>
> **3 · Predice.** Antes de ejecutar un comando importante, escribe qué esperas que ocurra. Por ejemplo: «después de `ss -lnt`, espero encontrar el servicio escuchando en TCP/80». Esta pequeña predicción convierte la práctica en una investigación y no en una receta.
>
> **4 · Construye paso a paso.** Cada número debe dejar el sistema en un estado ligeramente más completo que el anterior. Después de cada bloque, realiza una comprobación corta. Si el paso 4 depende del 3, no avances hasta que el 3 funcione.
>
> **5 · Diagnostica si falla.** No empieces reiniciando. Sigue esta secuencia: **estado → configuración → logs → puertos → red → prueba desde el cliente**. Conserva las órdenes utilizadas y la evidencia del fallo.
>
> **6 · Demuestra.** La práctica termina cuando puedes demostrar el resultado con una evidencia: captura, salida de comando, conexión desde cliente, fichero de configuración o tráfico observado.
>
> **7 · Explica.** Cierra con una breve explicación técnica: qué has configurado, qué protocolo interviene, qué puerto utiliza, cómo se verifica y qué error sería el primero que investigarías si dejara de funcionar.




Configura:

```text
Servidor:
radio.asir.test

Puerto:
8000

Mount:
radio.mp3
```

Comprueba desde WSL2:

```bash
curl -I http://radio.asir.test:8000/
```

Y:

```bash
curl -s http://radio.asir.test:8000/status-json.xsl
```

Si la instalación proporciona ese endpoint, úsalo para estudiar el estado
del servidor.

---


### 🧭 Guía de resolución y comprobación

Esta práctica se considera resuelta cuando puedes **explicar y demostrar** el resultado, no solo cuando el comando termina sin errores. Sigue siempre esta secuencia:

1. **Identifica el estado inicial.** Anota interfaces, direcciones, rutas y servicios que ya estaban activos.
2. **Aplica el cambio mínimo.** No modifiques varias cosas a la vez: si algo falla, necesitas saber qué cambio lo provocó.
3. **Valida inmediatamente.** Comprueba la sintaxis o el estado del servicio antes de probar desde el cliente.
4. **Prueba desde el punto de vista del usuario.** Una configuración correcta debe producir el comportamiento esperado desde el cliente, no solo desde el servidor.
5. **Observa evidencias.** Conserva la salida de comandos, logs, capturas de tráfico y capturas de pantalla que demuestren el resultado.

**Comandos de referencia para esta práctica:**

- `ffprobe <fichero>`
- `ss -lntup`
- `sudo nginx -t`
- `sudo systemctl status icecast2 nginx`
- `curl -I http://<stream-host>/`

> 💡 **Si algo falla:** no empieces reiniciando. Compara primero **estado → configuración → logs → puertos → red → cliente**. Un reinicio puede ocultar la causa y hacer más difícil aprender de la incidencia.

### 🧪 Rúbrica de evaluación

| Criterio | Puntos | Evidencia esperada |
|---|---:|---|
| Comprensión del objetivo y del protocolo | 2 | Explica qué servicio/protocolo está utilizando y por qué. |
| Preparación y configuración | 2 | Ficheros, comandos o topología correctamente preparados. |
| Verificación funcional | 2 | Demuestra el resultado desde un cliente o herramienta adecuada. |
| Diagnóstico y razonamiento | 2 | Utiliza evidencias para justificar la solución. |
| Documentación técnica | 1 | Incluye comandos, configuraciones y capturas relevantes. |
| Seguridad y buenas prácticas | 1 | Aplica permisos, exposición de puertos y credenciales con criterio. |
| **Total** | **10** | **Superación recomendada: ≥ 5 puntos y práctica funcional.** |


# 🎙️ 36. Generar audio con FFmpeg

Puedes utilizar un fichero local:

```bash
ffmpeg \
  -re \
  -i audio.mp3 \
  -c:a libmp3lame \
  -b:a 128k \
  -f mp3 \
  icecast://source:CONTRASEÑA_SOURCE@radio.asir.test:8000/radio.mp3
```

La sintaxis concreta de publicación depende de cómo esté configurado el
servidor y de la autenticación requerida.

---

# 🧪 37. PRÁCTICA 8.6 — Publicar un stream de audio
> 🧭 **PREPARACIÓN DE LA PRÁCTICA**
>
> **1 · Sitúate.** Lee primero el objetivo y localiza en la unidad el concepto que estamos llevando a la práctica. No empieces copiando comandos: primero debes poder explicar qué componente estamos construyendo y para qué sirve.
>
> **2 · Prepara el entorno.** Comprueba si esta práctica utiliza **Entorno I · Packet Tracer**, **Entorno II · WSL2**, **Entorno III · VirtualBox + Ubuntu 26.04 Server** o **Entorno IV · Docker Compose**. Verifica conectividad, nombres, interfaces y estado de los servicios antes de modificar nada.
>
> **3 · Predice.** Antes de ejecutar un comando importante, escribe qué esperas que ocurra. Por ejemplo: «después de `ss -lnt`, espero encontrar el servicio escuchando en TCP/80». Esta pequeña predicción convierte la práctica en una investigación y no en una receta.
>
> **4 · Construye paso a paso.** Cada número debe dejar el sistema en un estado ligeramente más completo que el anterior. Después de cada bloque, realiza una comprobación corta. Si el paso 4 depende del 3, no avances hasta que el 3 funcione.
>
> **5 · Diagnostica si falla.** No empieces reiniciando. Sigue esta secuencia: **estado → configuración → logs → puertos → red → prueba desde el cliente**. Conserva las órdenes utilizadas y la evidencia del fallo.
>
> **6 · Demuestra.** La práctica termina cuando puedes demostrar el resultado con una evidencia: captura, salida de comando, conexión desde cliente, fichero de configuración o tráfico observado.
>
> **7 · Explica.** Cierra con una breve explicación técnica: qué has configurado, qué protocolo interviene, qué puerto utiliza, cómo se verifica y qué error sería el primero que investigarías si dejara de funcionar.




Objetivo:

```text
audio.mp3
   │
   ▼
FFmpeg
   │
   ▼
Icecast
   │
   ▼
VLC
```

Comprueba desde el cliente:

```text
http://radio.asir.test:8000/radio.mp3
```

En VLC:

```text
Media
  ↓
Open Network Stream
  ↓
URL
```

---


### 🧭 Guía de resolución y comprobación

Esta práctica se considera resuelta cuando puedes **explicar y demostrar** el resultado, no solo cuando el comando termina sin errores. Sigue siempre esta secuencia:

1. **Identifica el estado inicial.** Anota interfaces, direcciones, rutas y servicios que ya estaban activos.
2. **Aplica el cambio mínimo.** No modifiques varias cosas a la vez: si algo falla, necesitas saber qué cambio lo provocó.
3. **Valida inmediatamente.** Comprueba la sintaxis o el estado del servicio antes de probar desde el cliente.
4. **Prueba desde el punto de vista del usuario.** Una configuración correcta debe producir el comportamiento esperado desde el cliente, no solo desde el servidor.
5. **Observa evidencias.** Conserva la salida de comandos, logs, capturas de tráfico y capturas de pantalla que demuestren el resultado.

**Comandos de referencia para esta práctica:**

- `ffprobe <fichero>`
- `ss -lntup`
- `sudo nginx -t`
- `sudo systemctl status icecast2 nginx`
- `curl -I http://<stream-host>/`

> 💡 **Si algo falla:** no empieces reiniciando. Compara primero **estado → configuración → logs → puertos → red → cliente**. Un reinicio puede ocultar la causa y hacer más difícil aprender de la incidencia.

### 🧪 Rúbrica de evaluación

| Criterio | Puntos | Evidencia esperada |
|---|---:|---|
| Comprensión del objetivo y del protocolo | 2 | Explica qué servicio/protocolo está utilizando y por qué. |
| Preparación y configuración | 2 | Ficheros, comandos o topología correctamente preparados. |
| Verificación funcional | 2 | Demuestra el resultado desde un cliente o herramienta adecuada. |
| Diagnóstico y razonamiento | 2 | Utiliza evidencias para justificar la solución. |
| Documentación técnica | 1 | Incluye comandos, configuraciones y capturas relevantes. |
| Seguridad y buenas prácticas | 1 | Aplica permisos, exposición de puertos y credenciales con criterio. |
| **Total** | **10** | **Superación recomendada: ≥ 5 puntos y práctica funcional.** |


# 🔍 38. Diagnóstico de Icecast

Comprueba:

```bash
systemctl status icecast2
```

Puerto:

```bash
ss -ltnp | grep 8000
```

Conectividad:

```bash
nc -vz radio.asir.test 8000
```

HTTP:

```bash
curl -I http://radio.asir.test:8000/
```

Logs:

```bash
journalctl -u icecast2
```

---

# 🧪 39. PRÁCTICA 8.7 — Provocar un fallo
> 🧭 **PREPARACIÓN DE LA PRÁCTICA**
>
> **1 · Sitúate.** Lee primero el objetivo y localiza en la unidad el concepto que estamos llevando a la práctica. No empieces copiando comandos: primero debes poder explicar qué componente estamos construyendo y para qué sirve.
>
> **2 · Prepara el entorno.** Comprueba si esta práctica utiliza **Entorno I · Packet Tracer**, **Entorno II · WSL2**, **Entorno III · VirtualBox + Ubuntu 26.04 Server** o **Entorno IV · Docker Compose**. Verifica conectividad, nombres, interfaces y estado de los servicios antes de modificar nada.
>
> **3 · Predice.** Antes de ejecutar un comando importante, escribe qué esperas que ocurra. Por ejemplo: «después de `ss -lnt`, espero encontrar el servicio escuchando en TCP/80». Esta pequeña predicción convierte la práctica en una investigación y no en una receta.
>
> **4 · Construye paso a paso.** Cada número debe dejar el sistema en un estado ligeramente más completo que el anterior. Después de cada bloque, realiza una comprobación corta. Si el paso 4 depende del 3, no avances hasta que el 3 funcione.
>
> **5 · Diagnostica si falla.** No empieces reiniciando. Sigue esta secuencia: **estado → configuración → logs → puertos → red → prueba desde el cliente**. Conserva las órdenes utilizadas y la evidencia del fallo.
>
> **6 · Demuestra.** La práctica termina cuando puedes demostrar el resultado con una evidencia: captura, salida de comando, conexión desde cliente, fichero de configuración o tráfico observado.
>
> **7 · Explica.** Cierra con una breve explicación técnica: qué has configurado, qué protocolo interviene, qué puerto utiliza, cómo se verifica y qué error sería el primero que investigarías si dejara de funcionar.




Cambia temporalmente:

```text
puerto
mountpoint
contraseña
```

Observa qué ocurre.

Diagnóstico:

```text
DNS
 ↓
TCP
 ↓
Icecast
 ↓
autenticación
 ↓
mountpoint
 ↓
cliente
```

Documenta:

```text
síntoma
causa
evidencia
corrección
```

---


### 🧭 Guía de resolución y comprobación

Esta práctica se considera resuelta cuando puedes **explicar y demostrar** el resultado, no solo cuando el comando termina sin errores. Sigue siempre esta secuencia:

1. **Identifica el estado inicial.** Anota interfaces, direcciones, rutas y servicios que ya estaban activos.
2. **Aplica el cambio mínimo.** No modifiques varias cosas a la vez: si algo falla, necesitas saber qué cambio lo provocó.
3. **Valida inmediatamente.** Comprueba la sintaxis o el estado del servicio antes de probar desde el cliente.
4. **Prueba desde el punto de vista del usuario.** Una configuración correcta debe producir el comportamiento esperado desde el cliente, no solo desde el servidor.
5. **Observa evidencias.** Conserva la salida de comandos, logs, capturas de tráfico y capturas de pantalla que demuestren el resultado.

**Comandos de referencia para esta práctica:**

- `ip addr`
- `ip route`
- `ss -lntup`
- `journalctl -b --no-pager`
- `ping <destino>`

> 💡 **Si algo falla:** no empieces reiniciando. Compara primero **estado → configuración → logs → puertos → red → cliente**. Un reinicio puede ocultar la causa y hacer más difícil aprender de la incidencia.

### 🧪 Rúbrica de evaluación

| Criterio | Puntos | Evidencia esperada |
|---|---:|---|
| Comprensión del objetivo y del protocolo | 2 | Explica qué servicio/protocolo está utilizando y por qué. |
| Preparación y configuración | 2 | Ficheros, comandos o topología correctamente preparados. |
| Verificación funcional | 2 | Demuestra el resultado desde un cliente o herramienta adecuada. |
| Diagnóstico y razonamiento | 2 | Utiliza evidencias para justificar la solución. |
| Documentación técnica | 1 | Incluye comandos, configuraciones y capturas relevantes. |
| Seguridad y buenas prácticas | 1 | Aplica permisos, exposición de puertos y credenciales con criterio. |
| **Total** | **10** | **Superación recomendada: ≥ 5 puntos y práctica funcional.** |


# 🎙️ 40. Podcast

Un podcast es una forma de distribución y suscripción de contenidos
audiovisuales, habitualmente mediante feeds.

Arquitectura conceptual:

```text
CREADOR
   │
   ▼
audio.mp3
   │
   ▼
SERVIDOR WEB
   │
   ├── archivo
   └── feed RSS
          │
          ▼
        CLIENTE
```

El feed permite descubrir y suscribirse a nuevos episodios.

---

# 📡 41. RSS y podcast

Conceptualmente:

```text
<rss>
   <channel>
      <title>ASIR Radio</title>

      <item>
         <title>UT8 · Streaming</title>
         <enclosure ... />
      </item>
   </channel>
</rss>
```

El elemento `enclosure` permite asociar el recurso multimedia.

---

# 🧪 42. PRÁCTICA 8.8 — Mini-podcast
> 🧭 **PREPARACIÓN DE LA PRÁCTICA**
>
> **1 · Sitúate.** Lee primero el objetivo y localiza en la unidad el concepto que estamos llevando a la práctica. No empieces copiando comandos: primero debes poder explicar qué componente estamos construyendo y para qué sirve.
>
> **2 · Prepara el entorno.** Comprueba si esta práctica utiliza **Entorno I · Packet Tracer**, **Entorno II · WSL2**, **Entorno III · VirtualBox + Ubuntu 26.04 Server** o **Entorno IV · Docker Compose**. Verifica conectividad, nombres, interfaces y estado de los servicios antes de modificar nada.
>
> **3 · Predice.** Antes de ejecutar un comando importante, escribe qué esperas que ocurra. Por ejemplo: «después de `ss -lnt`, espero encontrar el servicio escuchando en TCP/80». Esta pequeña predicción convierte la práctica en una investigación y no en una receta.
>
> **4 · Construye paso a paso.** Cada número debe dejar el sistema en un estado ligeramente más completo que el anterior. Después de cada bloque, realiza una comprobación corta. Si el paso 4 depende del 3, no avances hasta que el 3 funcione.
>
> **5 · Diagnostica si falla.** No empieces reiniciando. Sigue esta secuencia: **estado → configuración → logs → puertos → red → prueba desde el cliente**. Conserva las órdenes utilizadas y la evidencia del fallo.
>
> **6 · Demuestra.** La práctica termina cuando puedes demostrar el resultado con una evidencia: captura, salida de comando, conexión desde cliente, fichero de configuración o tráfico observado.
>
> **7 · Explica.** Cierra con una breve explicación técnica: qué has configurado, qué protocolo interviene, qué puerto utiliza, cómo se verifica y qué error sería el primero que investigarías si dejara de funcionar.




Crea:

```text
podcast/
├── feed.xml
├── episodio01.mp3
└── episodio02.mp3
```

Sirve el directorio mediante Nginx:

```bash
sudo apt install nginx
```

Comprueba:

```text
http://podcast.asir.test/feed.xml
```

### Reto

Añade un tercer episodio sin modificar los anteriores.

---


### 🧭 Guía de resolución y comprobación

Esta práctica se considera resuelta cuando puedes **explicar y demostrar** el resultado, no solo cuando el comando termina sin errores. Sigue siempre esta secuencia:

1. **Identifica el estado inicial.** Anota interfaces, direcciones, rutas y servicios que ya estaban activos.
2. **Aplica el cambio mínimo.** No modifiques varias cosas a la vez: si algo falla, necesitas saber qué cambio lo provocó.
3. **Valida inmediatamente.** Comprueba la sintaxis o el estado del servicio antes de probar desde el cliente.
4. **Prueba desde el punto de vista del usuario.** Una configuración correcta debe producir el comportamiento esperado desde el cliente, no solo desde el servidor.
5. **Observa evidencias.** Conserva la salida de comandos, logs, capturas de tráfico y capturas de pantalla que demuestren el resultado.

**Comandos de referencia para esta práctica:**

- `ip addr`
- `ip route`
- `ss -lntup`
- `journalctl -b --no-pager`
- `ping <destino>`

> 💡 **Si algo falla:** no empieces reiniciando. Compara primero **estado → configuración → logs → puertos → red → cliente**. Un reinicio puede ocultar la causa y hacer más difícil aprender de la incidencia.

### 🧪 Rúbrica de evaluación

| Criterio | Puntos | Evidencia esperada |
|---|---:|---|
| Comprensión del objetivo y del protocolo | 2 | Explica qué servicio/protocolo está utilizando y por qué. |
| Preparación y configuración | 2 | Ficheros, comandos o topología correctamente preparados. |
| Verificación funcional | 2 | Demuestra el resultado desde un cliente o herramienta adecuada. |
| Diagnóstico y razonamiento | 2 | Utiliza evidencias para justificar la solución. |
| Documentación técnica | 1 | Incluye comandos, configuraciones y capturas relevantes. |
| Seguridad y buenas prácticas | 1 | Aplica permisos, exposición de puertos y credenciales con criterio. |
| **Total** | **10** | **Superación recomendada: ≥ 5 puntos y práctica funcional.** |


# 📺 43. Vídeo bajo demanda

Para VOD podemos utilizar un servidor web:

```text
Nginx
   │
   ├── video01.mp4
   ├── video02.mp4
   └── video03.mp4
```

El cliente solicita:

```text
https://video.asir.test/video01.mp4
```

Esto no convierte automáticamente Nginx en un servidor de streaming
especializado.

---

# 🎬 44. Streaming HTTP y HLS

HLS utiliza:

```text
playlist .m3u8
+
segmentos
```

Conceptualmente:

```text
stream.m3u8
   │
   ├── segment001.ts
   ├── segment002.ts
   ├── segment003.ts
   └── ...
```

El cliente solicita los segmentos sucesivamente.

---

> 🧭 **PREPARACIÓN DIDÁCTICA**
>
> 🧭 **ANTES DE EMPEZAR · VÍDEO SEGMENTADO**
> 
> HLS transforma el vídeo en segmentos y utiliza HTTP para distribuirlos. No es lo mismo que enviar un flujo continuo por RTMP: cada arquitectura tiene objetivos y propiedades diferentes.

# 🌐 45. HLS

Arquitectura:

```text
          CODIFICADOR
               │
               ▼
        ┌──────────────┐
        │   SERVIDOR   │
        │               │
        │ stream.m3u8   │
        │ segment*.ts   │
        └──────┬────────┘
               │ HTTP
               ▼
             CLIENTE
```

HLS permite distribuir vídeo utilizando HTTP y playlists `.m3u8`. Nginx
dispone además de un módulo HLS específico para determinados escenarios de
ficheros multimedia. 

---

> 🧭 **ANTES DE EMPEZAR · RTMP**
>
> RTMP es un protocolo de ingestión/transporte de vídeo que históricamente ha sido muy utilizado para enviar un flujo desde un codificador hacia un servidor. En esta guía lo utilizaremos como pieza de entrada de una arquitectura que después puede generar HLS.

# 📡 46. RTMP

RTMP es un protocolo de streaming utilizado históricamente y todavía muy
presente en flujos de **ingest** hacia servidores multimedia.

Arquitectura típica:

```text
OBS / FFmpeg
     │
     │ RTMP
     ▼
RTMP SERVER
     │
     ├──► HLS
     └──► otros destinos
```

El módulo `nginx-rtmp-module` proporciona soporte para RTMP y puede generar
HLS/DASH según la configuración. 

---

# ⚠️ 47. RTMP no es HLS

No son lo mismo:

```text
RTMP
│
└── protocolo de ingest / distribución

HLS
│
└── distribución mediante HTTP + playlist/segmentos
```

Una arquitectura puede utilizar ambos:

```text
FFmpeg
  │
  │ RTMP
  ▼
Nginx RTMP
  │
  │ HLS
  ▼
navegador
```

---

# 🧪 48. PRÁCTICA 8.9 — Nginx RTMP
> 🧭 **PREPARACIÓN DE LA PRÁCTICA**
>
> **1 · Sitúate.** Lee primero el objetivo y localiza en la unidad el concepto que estamos llevando a la práctica. No empieces copiando comandos: primero debes poder explicar qué componente estamos construyendo y para qué sirve.
>
> **2 · Prepara el entorno.** Comprueba si esta práctica utiliza **Entorno I · Packet Tracer**, **Entorno II · WSL2**, **Entorno III · VirtualBox + Ubuntu 26.04 Server** o **Entorno IV · Docker Compose**. Verifica conectividad, nombres, interfaces y estado de los servicios antes de modificar nada.
>
> **3 · Predice.** Antes de ejecutar un comando importante, escribe qué esperas que ocurra. Por ejemplo: «después de `ss -lnt`, espero encontrar el servicio escuchando en TCP/80». Esta pequeña predicción convierte la práctica en una investigación y no en una receta.
>
> **4 · Construye paso a paso.** Cada número debe dejar el sistema en un estado ligeramente más completo que el anterior. Después de cada bloque, realiza una comprobación corta. Si el paso 4 depende del 3, no avances hasta que el 3 funcione.
>
> **5 · Diagnostica si falla.** No empieces reiniciando. Sigue esta secuencia: **estado → configuración → logs → puertos → red → prueba desde el cliente**. Conserva las órdenes utilizadas y la evidencia del fallo.
>
> **6 · Demuestra.** La práctica termina cuando puedes demostrar el resultado con una evidencia: captura, salida de comando, conexión desde cliente, fichero de configuración o tráfico observado.
>
> **7 · Explica.** Cierra con una breve explicación técnica: qué has configurado, qué protocolo interviene, qué puerto utiliza, cómo se verifica y qué error sería el primero que investigarías si dejara de funcionar.




El módulo RTMP no está integrado necesariamente de la misma forma en todas
las instalaciones de Nginx.

Primero comprueba:

```bash
nginx -V 2>&1
```

y:

```bash
apt search nginx | grep rtmp
```

Si existe un paquete/módulo compatible en tu repositorio:

```bash
sudo apt install libnginx-mod-rtmp
```

Después comprueba que Nginx reconoce el módulo y valida la configuración:

```bash
sudo nginx -t
```

> ⚠️ No asumas que cualquier paquete denominado `nginx` incluye RTMP.

---


### 🧭 Guía de resolución y comprobación

Esta práctica se considera resuelta cuando puedes **explicar y demostrar** el resultado, no solo cuando el comando termina sin errores. Sigue siempre esta secuencia:

1. **Identifica el estado inicial.** Anota interfaces, direcciones, rutas y servicios que ya estaban activos.
2. **Aplica el cambio mínimo.** No modifiques varias cosas a la vez: si algo falla, necesitas saber qué cambio lo provocó.
3. **Valida inmediatamente.** Comprueba la sintaxis o el estado del servicio antes de probar desde el cliente.
4. **Prueba desde el punto de vista del usuario.** Una configuración correcta debe producir el comportamiento esperado desde el cliente, no solo desde el servidor.
5. **Observa evidencias.** Conserva la salida de comandos, logs, capturas de tráfico y capturas de pantalla que demuestren el resultado.

**Comandos de referencia para esta práctica:**

- `ss -lntp | grep -E ":80|:443"`
- `curl -I http://<host>`
- `sudo apache2ctl configtest / sudo nginx -t`
- `sudo apache2ctl -S / sudo nginx -T`
- `journalctl -u apache2 -u nginx --no-pager`

> 💡 **Si algo falla:** no empieces reiniciando. Compara primero **estado → configuración → logs → puertos → red → cliente**. Un reinicio puede ocultar la causa y hacer más difícil aprender de la incidencia.

### 🧪 Rúbrica de evaluación

| Criterio | Puntos | Evidencia esperada |
|---|---:|---|
| Comprensión del objetivo y del protocolo | 2 | Explica qué servicio/protocolo está utilizando y por qué. |
| Preparación y configuración | 2 | Ficheros, comandos o topología correctamente preparados. |
| Verificación funcional | 2 | Demuestra el resultado desde un cliente o herramienta adecuada. |
| Diagnóstico y razonamiento | 2 | Utiliza evidencias para justificar la solución. |
| Documentación técnica | 1 | Incluye comandos, configuraciones y capturas relevantes. |
| Seguridad y buenas prácticas | 1 | Aplica permisos, exposición de puertos y credenciales con criterio. |
| **Total** | **10** | **Superación recomendada: ≥ 5 puntos y práctica funcional.** |


# ⚙️ 49. Arquitectura Nginx + RTMP + HLS

Ejemplo conceptual:

```nginx
rtmp {
    server {
        listen 1935;

        application live {
            live on;

            hls on;
            hls_path /var/www/hls;
            hls_fragment 3s;
            hls_playlist_length 12s;
        }
    }
}
```

El esquema anterior pertenece al modelo habitual del módulo
`nginx-rtmp-module`: una aplicación `live`, entrada RTMP y generación HLS.


> 🔐 Para producción deben añadirse controles de publicación, autenticación,
> límites, TLS en la distribución HTTP y una política de acceso adecuada.

---

# 🧪 50. PRÁCTICA 8.10 — Publicar RTMP con FFmpeg
> 🧭 **PREPARACIÓN DE LA PRÁCTICA**
>
> **1 · Sitúate.** Lee primero el objetivo y localiza en la unidad el concepto que estamos llevando a la práctica. No empieces copiando comandos: primero debes poder explicar qué componente estamos construyendo y para qué sirve.
>
> **2 · Prepara el entorno.** Comprueba si esta práctica utiliza **Entorno I · Packet Tracer**, **Entorno II · WSL2**, **Entorno III · VirtualBox + Ubuntu 26.04 Server** o **Entorno IV · Docker Compose**. Verifica conectividad, nombres, interfaces y estado de los servicios antes de modificar nada.
>
> **3 · Predice.** Antes de ejecutar un comando importante, escribe qué esperas que ocurra. Por ejemplo: «después de `ss -lnt`, espero encontrar el servicio escuchando en TCP/80». Esta pequeña predicción convierte la práctica en una investigación y no en una receta.
>
> **4 · Construye paso a paso.** Cada número debe dejar el sistema en un estado ligeramente más completo que el anterior. Después de cada bloque, realiza una comprobación corta. Si el paso 4 depende del 3, no avances hasta que el 3 funcione.
>
> **5 · Diagnostica si falla.** No empieces reiniciando. Sigue esta secuencia: **estado → configuración → logs → puertos → red → prueba desde el cliente**. Conserva las órdenes utilizadas y la evidencia del fallo.
>
> **6 · Demuestra.** La práctica termina cuando puedes demostrar el resultado con una evidencia: captura, salida de comando, conexión desde cliente, fichero de configuración o tráfico observado.
>
> **7 · Explica.** Cierra con una breve explicación técnica: qué has configurado, qué protocolo interviene, qué puerto utiliza, cómo se verifica y qué error sería el primero que investigarías si dejara de funcionar.




Una vez disponible el servidor RTMP:

```bash
ffmpeg \
  -re \
  -stream_loop -1 \
  -i video.mp4 \
  -c:v libx264 \
  -preset veryfast \
  -c:a aac \
  -b:a 128k \
  -f flv \
  rtmp://video.asir.test/live/ut8
```

Arquitectura:

```text
video.mp4
   │
   ▼
 FFmpeg
   │
 RTMP
   │
   ▼
Nginx RTMP
   │
   ▼
 HLS
```

---


### 🧭 Guía de resolución y comprobación

Esta práctica se considera resuelta cuando puedes **explicar y demostrar** el resultado, no solo cuando el comando termina sin errores. Sigue siempre esta secuencia:

1. **Identifica el estado inicial.** Anota interfaces, direcciones, rutas y servicios que ya estaban activos.
2. **Aplica el cambio mínimo.** No modifiques varias cosas a la vez: si algo falla, necesitas saber qué cambio lo provocó.
3. **Valida inmediatamente.** Comprueba la sintaxis o el estado del servicio antes de probar desde el cliente.
4. **Prueba desde el punto de vista del usuario.** Una configuración correcta debe producir el comportamiento esperado desde el cliente, no solo desde el servidor.
5. **Observa evidencias.** Conserva la salida de comandos, logs, capturas de tráfico y capturas de pantalla que demuestren el resultado.

**Comandos de referencia para esta práctica:**

- `ffprobe <fichero>`
- `ss -lntup`
- `sudo nginx -t`
- `sudo systemctl status icecast2 nginx`
- `curl -I http://<stream-host>/`

> 💡 **Si algo falla:** no empieces reiniciando. Compara primero **estado → configuración → logs → puertos → red → cliente**. Un reinicio puede ocultar la causa y hacer más difícil aprender de la incidencia.

### 🧪 Rúbrica de evaluación

| Criterio | Puntos | Evidencia esperada |
|---|---:|---|
| Comprensión del objetivo y del protocolo | 2 | Explica qué servicio/protocolo está utilizando y por qué. |
| Preparación y configuración | 2 | Ficheros, comandos o topología correctamente preparados. |
| Verificación funcional | 2 | Demuestra el resultado desde un cliente o herramienta adecuada. |
| Diagnóstico y razonamiento | 2 | Utiliza evidencias para justificar la solución. |
| Documentación técnica | 1 | Incluye comandos, configuraciones y capturas relevantes. |
| Seguridad y buenas prácticas | 1 | Aplica permisos, exposición de puertos y credenciales con criterio. |
| **Total** | **10** | **Superación recomendada: ≥ 5 puntos y práctica funcional.** |


# 🌐 51. Servir HLS

Si el servidor genera:

```text
/var/www/hls/ut8.m3u8
```

Nginx debe servirlo mediante HTTP.

Ejemplo conceptual:

```nginx
location /hls {
    root /var/www;

    types {
        application/vnd.apple.mpegurl m3u8;
        video/mp2t ts;
    }

    add_header Cache-Control no-cache;
    add_header Access-Control-Allow-Origin *;
}
```

Comprueba:

```bash
curl -I http://video.asir.test/hls/ut8.m3u8
```

---

# 🧪 52. PRÁCTICA 8.11 — Reproducir HLS
> 🧭 **PREPARACIÓN DE LA PRÁCTICA**
>
> **1 · Sitúate.** Lee primero el objetivo y localiza en la unidad el concepto que estamos llevando a la práctica. No empieces copiando comandos: primero debes poder explicar qué componente estamos construyendo y para qué sirve.
>
> **2 · Prepara el entorno.** Comprueba si esta práctica utiliza **Entorno I · Packet Tracer**, **Entorno II · WSL2**, **Entorno III · VirtualBox + Ubuntu 26.04 Server** o **Entorno IV · Docker Compose**. Verifica conectividad, nombres, interfaces y estado de los servicios antes de modificar nada.
>
> **3 · Predice.** Antes de ejecutar un comando importante, escribe qué esperas que ocurra. Por ejemplo: «después de `ss -lnt`, espero encontrar el servicio escuchando en TCP/80». Esta pequeña predicción convierte la práctica en una investigación y no en una receta.
>
> **4 · Construye paso a paso.** Cada número debe dejar el sistema en un estado ligeramente más completo que el anterior. Después de cada bloque, realiza una comprobación corta. Si el paso 4 depende del 3, no avances hasta que el 3 funcione.
>
> **5 · Diagnostica si falla.** No empieces reiniciando. Sigue esta secuencia: **estado → configuración → logs → puertos → red → prueba desde el cliente**. Conserva las órdenes utilizadas y la evidencia del fallo.
>
> **6 · Demuestra.** La práctica termina cuando puedes demostrar el resultado con una evidencia: captura, salida de comando, conexión desde cliente, fichero de configuración o tráfico observado.
>
> **7 · Explica.** Cierra con una breve explicación técnica: qué has configurado, qué protocolo interviene, qué puerto utiliza, cómo se verifica y qué error sería el primero que investigarías si dejara de funcionar.




Desde VLC:

```text
Media
  ↓
Open Network Stream
  ↓
http://video.asir.test/hls/ut8.m3u8
```

Analiza:

```text
playlist
segmentos
latencia
buffer
```

---


### 🧭 Guía de resolución y comprobación

Esta práctica se considera resuelta cuando puedes **explicar y demostrar** el resultado, no solo cuando el comando termina sin errores. Sigue siempre esta secuencia:

1. **Identifica el estado inicial.** Anota interfaces, direcciones, rutas y servicios que ya estaban activos.
2. **Aplica el cambio mínimo.** No modifiques varias cosas a la vez: si algo falla, necesitas saber qué cambio lo provocó.
3. **Valida inmediatamente.** Comprueba la sintaxis o el estado del servicio antes de probar desde el cliente.
4. **Prueba desde el punto de vista del usuario.** Una configuración correcta debe producir el comportamiento esperado desde el cliente, no solo desde el servidor.
5. **Observa evidencias.** Conserva la salida de comandos, logs, capturas de tráfico y capturas de pantalla que demuestren el resultado.

**Comandos de referencia para esta práctica:**

- `ip addr`
- `ip route`
- `ss -lntup`
- `journalctl -b --no-pager`
- `ping <destino>`

> 💡 **Si algo falla:** no empieces reiniciando. Compara primero **estado → configuración → logs → puertos → red → cliente**. Un reinicio puede ocultar la causa y hacer más difícil aprender de la incidencia.

### 🧪 Rúbrica de evaluación

| Criterio | Puntos | Evidencia esperada |
|---|---:|---|
| Comprensión del objetivo y del protocolo | 2 | Explica qué servicio/protocolo está utilizando y por qué. |
| Preparación y configuración | 2 | Ficheros, comandos o topología correctamente preparados. |
| Verificación funcional | 2 | Demuestra el resultado desde un cliente o herramienta adecuada. |
| Diagnóstico y razonamiento | 2 | Utiliza evidencias para justificar la solución. |
| Documentación técnica | 1 | Incluye comandos, configuraciones y capturas relevantes. |
| Seguridad y buenas prácticas | 1 | Aplica permisos, exposición de puertos y credenciales con criterio. |
| **Total** | **10** | **Superación recomendada: ≥ 5 puntos y práctica funcional.** |


# 📊 53. Latencia

En directo existe un compromiso:

```text
más búfer
   ↓
más estabilidad
   ↓
más latencia
```

Mientras:

```text
menos búfer
   ↓
menos latencia
   ↓
más sensibilidad a problemas de red
```

Conceptualmente:

```text
          estabilidad
              ▲
              │
              │
              │
              └──────────────► latencia
```

No existe un valor universalmente óptimo.

---

# 🧪 54. PRÁCTICA 8.12 — Medir comportamiento
> 🧭 **PREPARACIÓN DE LA PRÁCTICA**
>
> **1 · Sitúate.** Lee primero el objetivo y localiza en la unidad el concepto que estamos llevando a la práctica. No empieces copiando comandos: primero debes poder explicar qué componente estamos construyendo y para qué sirve.
>
> **2 · Prepara el entorno.** Comprueba si esta práctica utiliza **Entorno I · Packet Tracer**, **Entorno II · WSL2**, **Entorno III · VirtualBox + Ubuntu 26.04 Server** o **Entorno IV · Docker Compose**. Verifica conectividad, nombres, interfaces y estado de los servicios antes de modificar nada.
>
> **3 · Predice.** Antes de ejecutar un comando importante, escribe qué esperas que ocurra. Por ejemplo: «después de `ss -lnt`, espero encontrar el servicio escuchando en TCP/80». Esta pequeña predicción convierte la práctica en una investigación y no en una receta.
>
> **4 · Construye paso a paso.** Cada número debe dejar el sistema en un estado ligeramente más completo que el anterior. Después de cada bloque, realiza una comprobación corta. Si el paso 4 depende del 3, no avances hasta que el 3 funcione.
>
> **5 · Diagnostica si falla.** No empieces reiniciando. Sigue esta secuencia: **estado → configuración → logs → puertos → red → prueba desde el cliente**. Conserva las órdenes utilizadas y la evidencia del fallo.
>
> **6 · Demuestra.** La práctica termina cuando puedes demostrar el resultado con una evidencia: captura, salida de comando, conexión desde cliente, fichero de configuración o tráfico observado.
>
> **7 · Explica.** Cierra con una breve explicación técnica: qué has configurado, qué protocolo interviene, qué puerto utiliza, cómo se verifica y qué error sería el primero que investigarías si dejara de funcionar.




Realiza una transmisión:

```text
FFmpeg → RTMP → Nginx → HLS → VLC
```

Registra:

```text
resolución
FPS
bitrate
latencia aproximada
CPU
uso de red
```

Después cambia:

```text
720p → 1080p
```

y compara.

---


### 🧭 Guía de resolución y comprobación

Esta práctica se considera resuelta cuando puedes **explicar y demostrar** el resultado, no solo cuando el comando termina sin errores. Sigue siempre esta secuencia:

1. **Identifica el estado inicial.** Anota interfaces, direcciones, rutas y servicios que ya estaban activos.
2. **Aplica el cambio mínimo.** No modifiques varias cosas a la vez: si algo falla, necesitas saber qué cambio lo provocó.
3. **Valida inmediatamente.** Comprueba la sintaxis o el estado del servicio antes de probar desde el cliente.
4. **Prueba desde el punto de vista del usuario.** Una configuración correcta debe producir el comportamiento esperado desde el cliente, no solo desde el servidor.
5. **Observa evidencias.** Conserva la salida de comandos, logs, capturas de tráfico y capturas de pantalla que demuestren el resultado.

**Comandos de referencia para esta práctica:**

- `ip addr`
- `ip route`
- `ss -lntup`
- `journalctl -b --no-pager`
- `ping <destino>`

> 💡 **Si algo falla:** no empieces reiniciando. Compara primero **estado → configuración → logs → puertos → red → cliente**. Un reinicio puede ocultar la causa y hacer más difícil aprender de la incidencia.

### 🧪 Rúbrica de evaluación

| Criterio | Puntos | Evidencia esperada |
|---|---:|---|
| Comprensión del objetivo y del protocolo | 2 | Explica qué servicio/protocolo está utilizando y por qué. |
| Preparación y configuración | 2 | Ficheros, comandos o topología correctamente preparados. |
| Verificación funcional | 2 | Demuestra el resultado desde un cliente o herramienta adecuada. |
| Diagnóstico y razonamiento | 2 | Utiliza evidencias para justificar la solución. |
| Documentación técnica | 1 | Incluye comandos, configuraciones y capturas relevantes. |
| Seguridad y buenas prácticas | 1 | Aplica permisos, exposición de puertos y credenciales con criterio. |
| **Total** | **10** | **Superación recomendada: ≥ 5 puntos y práctica funcional.** |


# 🧠 55. Calidad y bitrate

Un aumento de bitrate puede mejorar la calidad:

```text
2 Mbit/s
      ↓
5 Mbit/s
```

pero también:

```text
más tráfico
más almacenamiento
más requisitos de red
```

La calidad depende de la eficiencia del códec.

Por eso no es correcto afirmar:

> «más bitrate siempre significa mejor experiencia».

---

# 🧪 56. PRÁCTICA 8.13 — Comparar códecs
> 🧭 **PREPARACIÓN DE LA PRÁCTICA**
>
> **1 · Sitúate.** Lee primero el objetivo y localiza en la unidad el concepto que estamos llevando a la práctica. No empieces copiando comandos: primero debes poder explicar qué componente estamos construyendo y para qué sirve.
>
> **2 · Prepara el entorno.** Comprueba si esta práctica utiliza **Entorno I · Packet Tracer**, **Entorno II · WSL2**, **Entorno III · VirtualBox + Ubuntu 26.04 Server** o **Entorno IV · Docker Compose**. Verifica conectividad, nombres, interfaces y estado de los servicios antes de modificar nada.
>
> **3 · Predice.** Antes de ejecutar un comando importante, escribe qué esperas que ocurra. Por ejemplo: «después de `ss -lnt`, espero encontrar el servicio escuchando en TCP/80». Esta pequeña predicción convierte la práctica en una investigación y no en una receta.
>
> **4 · Construye paso a paso.** Cada número debe dejar el sistema en un estado ligeramente más completo que el anterior. Después de cada bloque, realiza una comprobación corta. Si el paso 4 depende del 3, no avances hasta que el 3 funcione.
>
> **5 · Diagnostica si falla.** No empieces reiniciando. Sigue esta secuencia: **estado → configuración → logs → puertos → red → prueba desde el cliente**. Conserva las órdenes utilizadas y la evidencia del fallo.
>
> **6 · Demuestra.** La práctica termina cuando puedes demostrar el resultado con una evidencia: captura, salida de comando, conexión desde cliente, fichero de configuración o tráfico observado.
>
> **7 · Explica.** Cierra con una breve explicación técnica: qué has configurado, qué protocolo interviene, qué puerto utiliza, cómo se verifica y qué error sería el primero que investigarías si dejara de funcionar.




Genera versiones de un mismo vídeo utilizando un tamaño objetivo comparable.

Por ejemplo:

```text
H.264
VP9
AV1
```

Compara:

```text
tamaño
bitrate
tiempo de codificación
CPU
calidad visual
compatibilidad
```

> 💡 La práctica es experimental: no existe una única respuesta válida para
> todos los equipos y contenidos.

---


### 🧭 Guía de resolución y comprobación

Esta práctica se considera resuelta cuando puedes **explicar y demostrar** el resultado, no solo cuando el comando termina sin errores. Sigue siempre esta secuencia:

1. **Identifica el estado inicial.** Anota interfaces, direcciones, rutas y servicios que ya estaban activos.
2. **Aplica el cambio mínimo.** No modifiques varias cosas a la vez: si algo falla, necesitas saber qué cambio lo provocó.
3. **Valida inmediatamente.** Comprueba la sintaxis o el estado del servicio antes de probar desde el cliente.
4. **Prueba desde el punto de vista del usuario.** Una configuración correcta debe producir el comportamiento esperado desde el cliente, no solo desde el servidor.
5. **Observa evidencias.** Conserva la salida de comandos, logs, capturas de tráfico y capturas de pantalla que demuestren el resultado.

**Comandos de referencia para esta práctica:**

- `ip addr`
- `ip route`
- `ss -lntup`
- `journalctl -b --no-pager`
- `ping <destino>`

> 💡 **Si algo falla:** no empieces reiniciando. Compara primero **estado → configuración → logs → puertos → red → cliente**. Un reinicio puede ocultar la causa y hacer más difícil aprender de la incidencia.

### 🧪 Rúbrica de evaluación

| Criterio | Puntos | Evidencia esperada |
|---|---:|---|
| Comprensión del objetivo y del protocolo | 2 | Explica qué servicio/protocolo está utilizando y por qué. |
| Preparación y configuración | 2 | Ficheros, comandos o topología correctamente preparados. |
| Verificación funcional | 2 | Demuestra el resultado desde un cliente o herramienta adecuada. |
| Diagnóstico y razonamiento | 2 | Utiliza evidencias para justificar la solución. |
| Documentación técnica | 1 | Incluye comandos, configuraciones y capturas relevantes. |
| Seguridad y buenas prácticas | 1 | Aplica permisos, exposición de puertos y credenciales con criterio. |
| **Total** | **10** | **Superación recomendada: ≥ 5 puntos y práctica funcional.** |


# 🧮 57. Estimar ancho de banda

Si tenemos:

```text
bitrate = 4 Mbit/s
clientes = 20
```

aproximación:

```text
4 × 20 = 80 Mbit/s
```

Sin contar overhead ni otros consumos.

Con:

```text
100 clientes
```

serían aproximadamente:

```text
400 Mbit/s
```

Esto explica por qué un servicio multimedia escala de forma diferente a una
web con ficheros pequeños.

---

# 🧪 58. PRÁCTICA 8.14 — Capacidad del servidor
> 🧭 **PREPARACIÓN DE LA PRÁCTICA**
>
> **1 · Sitúate.** Lee primero el objetivo y localiza en la unidad el concepto que estamos llevando a la práctica. No empieces copiando comandos: primero debes poder explicar qué componente estamos construyendo y para qué sirve.
>
> **2 · Prepara el entorno.** Comprueba si esta práctica utiliza **Entorno I · Packet Tracer**, **Entorno II · WSL2**, **Entorno III · VirtualBox + Ubuntu 26.04 Server** o **Entorno IV · Docker Compose**. Verifica conectividad, nombres, interfaces y estado de los servicios antes de modificar nada.
>
> **3 · Predice.** Antes de ejecutar un comando importante, escribe qué esperas que ocurra. Por ejemplo: «después de `ss -lnt`, espero encontrar el servicio escuchando en TCP/80». Esta pequeña predicción convierte la práctica en una investigación y no en una receta.
>
> **4 · Construye paso a paso.** Cada número debe dejar el sistema en un estado ligeramente más completo que el anterior. Después de cada bloque, realiza una comprobación corta. Si el paso 4 depende del 3, no avances hasta que el 3 funcione.
>
> **5 · Diagnostica si falla.** No empieces reiniciando. Sigue esta secuencia: **estado → configuración → logs → puertos → red → prueba desde el cliente**. Conserva las órdenes utilizadas y la evidencia del fallo.
>
> **6 · Demuestra.** La práctica termina cuando puedes demostrar el resultado con una evidencia: captura, salida de comando, conexión desde cliente, fichero de configuración o tráfico observado.
>
> **7 · Explica.** Cierra con una breve explicación técnica: qué has configurado, qué protocolo interviene, qué puerto utiliza, cómo se verifica y qué error sería el primero que investigarías si dejara de funcionar.




Calcula el ancho de banda necesario para:

```text
100 clientes
5 Mbit/s por cliente
```

Después repite:

```text
500 clientes
5 Mbit/s
```

Y:

```text
1000 clientes
5 Mbit/s
```

Analiza:

```text
NIC
switch
router
servidor
CPU
CDN
```

---


### 🧭 Guía de resolución y comprobación

Esta práctica se considera resuelta cuando puedes **explicar y demostrar** el resultado, no solo cuando el comando termina sin errores. Sigue siempre esta secuencia:

1. **Identifica el estado inicial.** Anota interfaces, direcciones, rutas y servicios que ya estaban activos.
2. **Aplica el cambio mínimo.** No modifiques varias cosas a la vez: si algo falla, necesitas saber qué cambio lo provocó.
3. **Valida inmediatamente.** Comprueba la sintaxis o el estado del servicio antes de probar desde el cliente.
4. **Prueba desde el punto de vista del usuario.** Una configuración correcta debe producir el comportamiento esperado desde el cliente, no solo desde el servidor.
5. **Observa evidencias.** Conserva la salida de comandos, logs, capturas de tráfico y capturas de pantalla que demuestren el resultado.

**Comandos de referencia para esta práctica:**

- `ip addr`
- `ip route`
- `ss -lntup`
- `journalctl -b --no-pager`
- `ping <destino>`

> 💡 **Si algo falla:** no empieces reiniciando. Compara primero **estado → configuración → logs → puertos → red → cliente**. Un reinicio puede ocultar la causa y hacer más difícil aprender de la incidencia.

### 🧪 Rúbrica de evaluación

| Criterio | Puntos | Evidencia esperada |
|---|---:|---|
| Comprensión del objetivo y del protocolo | 2 | Explica qué servicio/protocolo está utilizando y por qué. |
| Preparación y configuración | 2 | Ficheros, comandos o topología correctamente preparados. |
| Verificación funcional | 2 | Demuestra el resultado desde un cliente o herramienta adecuada. |
| Diagnóstico y razonamiento | 2 | Utiliza evidencias para justificar la solución. |
| Documentación técnica | 1 | Incluye comandos, configuraciones y capturas relevantes. |
| Seguridad y buenas prácticas | 1 | Aplica permisos, exposición de puertos y credenciales con criterio. |
| **Total** | **10** | **Superación recomendada: ≥ 5 puntos y práctica funcional.** |


# 📡 59. Unicast y multicast

## Unicast

Cada cliente recibe su flujo:

```text
       ┌── C1
       │
SERVER ├── C2
       │
       └── C3
```

El servidor puede tener que enviar varias copias.

## Multicast

Conceptualmente:

```text
SERVER
   │
   ▼
MULTICAST
 ┌─┼─┐
 ▼ ▼ ▼
C1 C2 C3
```

La red puede replicar el tráfico donde sea necesario.

---

# ⚠️ 60. Multicast en Internet

Multicast no equivale automáticamente a:

```text
«streaming eficiente en Internet»
```

Su disponibilidad depende de:

```text
red
routers
protocolos
operador
arquitectura
```

Para el laboratorio se estudiará principalmente como concepto.

---

> 🧭 **ANTES DE EMPEZAR · VoIP**
>
> VoIP transporta comunicaciones de voz mediante redes IP. Separaremos señalización —por ejemplo, SIP— de transporte del medio —por ejemplo, RTP— para entender por qué una llamada puede establecerse correctamente y, aun así, presentar problemas de audio.

# 🎙️ 61. VoIP

VoIP significa:

```text
Voice over IP
```

Consiste en transportar comunicaciones de voz sobre redes IP.

Arquitectura simplificada:

```text
TELÉFONO
   │
   ▼
RED IP
   │
   ▼
SISTEMA VoIP
   │
   ▼
OTRO TELÉFONO
```

---

# 📞 62. Telefonía tradicional frente a VoIP

| Aspecto | Telefonía tradicional | VoIP |
|---|---|---|
| Transporte | Redes telefónicas | IP |
| Señalización | Tecnologías PSTN/RTC | SIP u otras |
| Media | Circuito/red telefónica | RTP normalmente |
| Infraestructura | Red específica | Infraestructura IP |
| Integración | Más específica | Alta integración con datos |

---

> 🧭 **PREPARACIÓN DIDÁCTICA**
>
> 🧭 **ANTES DE EMPEZAR · SEÑALIZACIÓN FRENTE A MEDIA**
> 
> En VoIP debemos separar la señalización, que establece y controla la sesión, del transporte de audio/vídeo. SIP y RTP cumplen funciones diferentes.

# 📡 63. SIP

SIP se utiliza para señalización.

Permite operaciones conceptuales como:

```text
REGISTER
INVITE
RINGING
200 OK
ACK
BYE
```

Ejemplo:

```text
A ── INVITE ──► B
A ◄─ 180 ───── B
A ◄─ 200 ───── B
A ── ACK ─────► B
       │
       ▼
      RTP
       │
       ▼
      VOZ
```

---

# 🎧 64. RTP

RTP se utiliza para transportar medios en tiempo real.

```text
SIP
 │
 └── establece/controla sesión

RTP
 │
 └── transporta audio/vídeo
```

No deben confundirse:

```text
SIP ≠ RTP
```

---

# ⏱️ 65. Jitter

El jitter es la variación del tiempo de llegada de paquetes.

Ejemplo ideal:

```text
10 ms
10 ms
10 ms
10 ms
```

Con jitter:

```text
10 ms
18 ms
7 ms
25 ms
12 ms
```

El receptor puede utilizar un:

```text
jitter buffer
```

para suavizar esas variaciones.

---

# 🧪 66. PRÁCTICA 8.15 — Analizar RTP
> 🧭 **PREPARACIÓN DE LA PRÁCTICA**
>
> **1 · Sitúate.** Lee primero el objetivo y localiza en la unidad el concepto que estamos llevando a la práctica. No empieces copiando comandos: primero debes poder explicar qué componente estamos construyendo y para qué sirve.
>
> **2 · Prepara el entorno.** Comprueba si esta práctica utiliza **Entorno I · Packet Tracer**, **Entorno II · WSL2**, **Entorno III · VirtualBox + Ubuntu 26.04 Server** o **Entorno IV · Docker Compose**. Verifica conectividad, nombres, interfaces y estado de los servicios antes de modificar nada.
>
> **3 · Predice.** Antes de ejecutar un comando importante, escribe qué esperas que ocurra. Por ejemplo: «después de `ss -lnt`, espero encontrar el servicio escuchando en TCP/80». Esta pequeña predicción convierte la práctica en una investigación y no en una receta.
>
> **4 · Construye paso a paso.** Cada número debe dejar el sistema en un estado ligeramente más completo que el anterior. Después de cada bloque, realiza una comprobación corta. Si el paso 4 depende del 3, no avances hasta que el 3 funcione.
>
> **5 · Diagnostica si falla.** No empieces reiniciando. Sigue esta secuencia: **estado → configuración → logs → puertos → red → prueba desde el cliente**. Conserva las órdenes utilizadas y la evidencia del fallo.
>
> **6 · Demuestra.** La práctica termina cuando puedes demostrar el resultado con una evidencia: captura, salida de comando, conexión desde cliente, fichero de configuración o tráfico observado.
>
> **7 · Explica.** Cierra con una breve explicación técnica: qué has configurado, qué protocolo interviene, qué puerto utiliza, cómo se verifica y qué error sería el primero que investigarías si dejara de funcionar.




Con una captura autorizada de laboratorio:

```text
Wireshark
```

Filtra:

```text
rtp
```

Observa:

```text
Sequence Number
Timestamp
SSRC
Payload Type
```

Relaciona:

```text
paquete
   ↓
secuencia
   ↓
jitter
   ↓
calidad percibida
```

---

> 🧭 **ANTES DE EMPEZAR · Videoconferencia y WebRTC**
>
> Una videoconferencia combina señalización, negociación de capacidades, transporte de medios y mecanismos para atravesar redes intermedias. WebRTC reúne buena parte de estas funciones en un ecosistema pensado para comunicación en tiempo real entre navegadores y aplicaciones.


### 🧭 Guía de resolución y comprobación

Esta práctica se considera resuelta cuando puedes **explicar y demostrar** el resultado, no solo cuando el comando termina sin errores. Sigue siempre esta secuencia:

1. **Identifica el estado inicial.** Anota interfaces, direcciones, rutas y servicios que ya estaban activos.
2. **Aplica el cambio mínimo.** No modifiques varias cosas a la vez: si algo falla, necesitas saber qué cambio lo provocó.
3. **Valida inmediatamente.** Comprueba la sintaxis o el estado del servicio antes de probar desde el cliente.
4. **Prueba desde el punto de vista del usuario.** Una configuración correcta debe producir el comportamiento esperado desde el cliente, no solo desde el servidor.
5. **Observa evidencias.** Conserva la salida de comandos, logs, capturas de tráfico y capturas de pantalla que demuestren el resultado.

**Comandos de referencia para esta práctica:**

- `ip addr`
- `ip route`
- `ss -lntup`
- `journalctl -b --no-pager`
- `ping <destino>`

> 💡 **Si algo falla:** no empieces reiniciando. Compara primero **estado → configuración → logs → puertos → red → cliente**. Un reinicio puede ocultar la causa y hacer más difícil aprender de la incidencia.

### 🧪 Rúbrica de evaluación

| Criterio | Puntos | Evidencia esperada |
|---|---:|---|
| Comprensión del objetivo y del protocolo | 2 | Explica qué servicio/protocolo está utilizando y por qué. |
| Preparación y configuración | 2 | Ficheros, comandos o topología correctamente preparados. |
| Verificación funcional | 2 | Demuestra el resultado desde un cliente o herramienta adecuada. |
| Diagnóstico y razonamiento | 2 | Utiliza evidencias para justificar la solución. |
| Documentación técnica | 1 | Incluye comandos, configuraciones y capturas relevantes. |
| Seguridad y buenas prácticas | 1 | Aplica permisos, exposición de puertos y credenciales con criterio. |
| **Total** | **10** | **Superación recomendada: ≥ 5 puntos y práctica funcional.** |


# 🎥 67. Videoconferencia

Una videoconferencia añade:

```text
audio
+
vídeo
+
señalización
+
sincronización
+
control
```

Arquitectura:

```text
Cámara ──┐
         ├──► cliente ───► red ───► cliente
Micrófono┘
```

---

# 🌐 68. WebRTC

WebRTC permite comunicación multimedia interactiva desde aplicaciones
compatibles, especialmente navegadores.

Conceptualmente:

```text
NAVEGADOR A
    │
    │ señalización
    ▼
SERVIDOR
    │
    │ establecimiento
    ▼
NAVEGADOR B
    │
    └──── audio/vídeo ────►
```

En escenarios reales intervienen mecanismos de establecimiento de conectividad
y servidores auxiliares cuando es necesario.

---

# 🧪 69. PRÁCTICA 8.16 — Videoconferencia
> 🧭 **PREPARACIÓN DE LA PRÁCTICA**
>
> **1 · Sitúate.** Lee primero el objetivo y localiza en la unidad el concepto que estamos llevando a la práctica. No empieces copiando comandos: primero debes poder explicar qué componente estamos construyendo y para qué sirve.
>
> **2 · Prepara el entorno.** Comprueba si esta práctica utiliza **Entorno I · Packet Tracer**, **Entorno II · WSL2**, **Entorno III · VirtualBox + Ubuntu 26.04 Server** o **Entorno IV · Docker Compose**. Verifica conectividad, nombres, interfaces y estado de los servicios antes de modificar nada.
>
> **3 · Predice.** Antes de ejecutar un comando importante, escribe qué esperas que ocurra. Por ejemplo: «después de `ss -lnt`, espero encontrar el servicio escuchando en TCP/80». Esta pequeña predicción convierte la práctica en una investigación y no en una receta.
>
> **4 · Construye paso a paso.** Cada número debe dejar el sistema en un estado ligeramente más completo que el anterior. Después de cada bloque, realiza una comprobación corta. Si el paso 4 depende del 3, no avances hasta que el 3 funcione.
>
> **5 · Diagnostica si falla.** No empieces reiniciando. Sigue esta secuencia: **estado → configuración → logs → puertos → red → prueba desde el cliente**. Conserva las órdenes utilizadas y la evidencia del fallo.
>
> **6 · Demuestra.** La práctica termina cuando puedes demostrar el resultado con una evidencia: captura, salida de comando, conexión desde cliente, fichero de configuración o tráfico observado.
>
> **7 · Explica.** Cierra con una breve explicación técnica: qué has configurado, qué protocolo interviene, qué puerto utiliza, cómo se verifica y qué error sería el primero que investigarías si dejara de funcionar.




Utiliza una herramienta de videoconferencia autorizada por el centro.

Identifica:

```text
micrófono
cámara
codec
resolución
FPS
bitrate
latencia
jitter
```

Después documenta:

```text
cliente
servidor
señalización
medios
red
```

---


### 🧭 Guía de resolución y comprobación

Esta práctica se considera resuelta cuando puedes **explicar y demostrar** el resultado, no solo cuando el comando termina sin errores. Sigue siempre esta secuencia:

1. **Identifica el estado inicial.** Anota interfaces, direcciones, rutas y servicios que ya estaban activos.
2. **Aplica el cambio mínimo.** No modifiques varias cosas a la vez: si algo falla, necesitas saber qué cambio lo provocó.
3. **Valida inmediatamente.** Comprueba la sintaxis o el estado del servicio antes de probar desde el cliente.
4. **Prueba desde el punto de vista del usuario.** Una configuración correcta debe producir el comportamiento esperado desde el cliente, no solo desde el servidor.
5. **Observa evidencias.** Conserva la salida de comandos, logs, capturas de tráfico y capturas de pantalla que demuestren el resultado.

**Comandos de referencia para esta práctica:**

- `ffprobe <fichero>`
- `ss -lntup`
- `sudo nginx -t`
- `sudo systemctl status icecast2 nginx`
- `curl -I http://<stream-host>/`

> 💡 **Si algo falla:** no empieces reiniciando. Compara primero **estado → configuración → logs → puertos → red → cliente**. Un reinicio puede ocultar la causa y hacer más difícil aprender de la incidencia.

### 🧪 Rúbrica de evaluación

| Criterio | Puntos | Evidencia esperada |
|---|---:|---|
| Comprensión del objetivo y del protocolo | 2 | Explica qué servicio/protocolo está utilizando y por qué. |
| Preparación y configuración | 2 | Ficheros, comandos o topología correctamente preparados. |
| Verificación funcional | 2 | Demuestra el resultado desde un cliente o herramienta adecuada. |
| Diagnóstico y razonamiento | 2 | Utiliza evidencias para justificar la solución. |
| Documentación técnica | 1 | Incluye comandos, configuraciones y capturas relevantes. |
| Seguridad y buenas prácticas | 1 | Aplica permisos, exposición de puertos y credenciales con criterio. |
| **Total** | **10** | **Superación recomendada: ≥ 5 puntos y práctica funcional.** |


# 🧪 70. PRÁCTICA 8.17 — Red degradada
> 🧭 **PREPARACIÓN DE LA PRÁCTICA**
>
> **1 · Sitúate.** Lee primero el objetivo y localiza en la unidad el concepto que estamos llevando a la práctica. No empieces copiando comandos: primero debes poder explicar qué componente estamos construyendo y para qué sirve.
>
> **2 · Prepara el entorno.** Comprueba si esta práctica utiliza **Entorno I · Packet Tracer**, **Entorno II · WSL2**, **Entorno III · VirtualBox + Ubuntu 26.04 Server** o **Entorno IV · Docker Compose**. Verifica conectividad, nombres, interfaces y estado de los servicios antes de modificar nada.
>
> **3 · Predice.** Antes de ejecutar un comando importante, escribe qué esperas que ocurra. Por ejemplo: «después de `ss -lnt`, espero encontrar el servicio escuchando en TCP/80». Esta pequeña predicción convierte la práctica en una investigación y no en una receta.
>
> **4 · Construye paso a paso.** Cada número debe dejar el sistema en un estado ligeramente más completo que el anterior. Después de cada bloque, realiza una comprobación corta. Si el paso 4 depende del 3, no avances hasta que el 3 funcione.
>
> **5 · Diagnostica si falla.** No empieces reiniciando. Sigue esta secuencia: **estado → configuración → logs → puertos → red → prueba desde el cliente**. Conserva las órdenes utilizadas y la evidencia del fallo.
>
> **6 · Demuestra.** La práctica termina cuando puedes demostrar el resultado con una evidencia: captura, salida de comando, conexión desde cliente, fichero de configuración o tráfico observado.
>
> **7 · Explica.** Cierra con una breve explicación técnica: qué has configurado, qué protocolo interviene, qué puerto utiliza, cómo se verifica y qué error sería el primero que investigarías si dejara de funcionar.




Simula o provoca en un entorno controlado:

```text
latencia
pérdidas
ancho de banda limitado
```

Observa:

```text
audio
vídeo
buffering
pixelación
saltos
desincronización
```

### Objetivo

Relacionar:

```text
problema de red
      ↓
efecto multimedia
```

---


### 🧭 Guía de resolución y comprobación

Esta práctica se considera resuelta cuando puedes **explicar y demostrar** el resultado, no solo cuando el comando termina sin errores. Sigue siempre esta secuencia:

1. **Identifica el estado inicial.** Anota interfaces, direcciones, rutas y servicios que ya estaban activos.
2. **Aplica el cambio mínimo.** No modifiques varias cosas a la vez: si algo falla, necesitas saber qué cambio lo provocó.
3. **Valida inmediatamente.** Comprueba la sintaxis o el estado del servicio antes de probar desde el cliente.
4. **Prueba desde el punto de vista del usuario.** Una configuración correcta debe producir el comportamiento esperado desde el cliente, no solo desde el servidor.
5. **Observa evidencias.** Conserva la salida de comandos, logs, capturas de tráfico y capturas de pantalla que demuestren el resultado.

**Comandos de referencia para esta práctica:**

- `ip addr`
- `ip route`
- `ss -lntup`
- `journalctl -b --no-pager`
- `ping <destino>`

> 💡 **Si algo falla:** no empieces reiniciando. Compara primero **estado → configuración → logs → puertos → red → cliente**. Un reinicio puede ocultar la causa y hacer más difícil aprender de la incidencia.

### 🧪 Rúbrica de evaluación

| Criterio | Puntos | Evidencia esperada |
|---|---:|---|
| Comprensión del objetivo y del protocolo | 2 | Explica qué servicio/protocolo está utilizando y por qué. |
| Preparación y configuración | 2 | Ficheros, comandos o topología correctamente preparados. |
| Verificación funcional | 2 | Demuestra el resultado desde un cliente o herramienta adecuada. |
| Diagnóstico y razonamiento | 2 | Utiliza evidencias para justificar la solución. |
| Documentación técnica | 1 | Incluye comandos, configuraciones y capturas relevantes. |
| Seguridad y buenas prácticas | 1 | Aplica permisos, exposición de puertos y credenciales con criterio. |
| **Total** | **10** | **Superación recomendada: ≥ 5 puntos y práctica funcional.** |


# 🔍 71. Diagnóstico sistemático

Cuando un vídeo no reproduce:

```text
                 ❌ VÍDEO NO FUNCIONA
                          │
                          ▼
                    ¿DNS resuelve?
                     /          \
                   NO            SÍ
                   │              │
                  DNS             ▼
                           ¿TCP conecta?
                            /         \
                          NO           SÍ
                          │             │
                       firewall         ▼
                                 ¿HTTP/RTMP/HLS?
                                  /           \
                                NO             SÍ
                                │               │
                             servidor           ▼
                                           ¿Códec?
                                            /   \
                                          NO     SÍ
                                          │       │
                                      transcodificar
                                                  ▼
                                             ¿bitrate?
                                              /   \
                                            NO     SÍ
                                            │       │
                                          red      ▼
                                                 cliente
```

---

# 🩺 72. Herramientas de diagnóstico

## DNS

```bash
dig video.asir.test
```

## TCP

```bash
nc -vz video.asir.test 1935
nc -vz video.asir.test 80
```

## HTTP

```bash
curl -I http://video.asir.test/
```

## Puertos

```bash
ss -ltnp
```

## Logs

```bash
journalctl -u nginx
journalctl -u icecast2
```

## Captura

```bash
sudo tcpdump -ni any
```

## Multimedia

```bash
ffprobe video.mp4
```

---

# 🧪 73. PRÁCTICA 8.18 — Diagnóstico completo
> 🧭 **PREPARACIÓN DE LA PRÁCTICA**
>
> **1 · Sitúate.** Lee primero el objetivo y localiza en la unidad el concepto que estamos llevando a la práctica. No empieces copiando comandos: primero debes poder explicar qué componente estamos construyendo y para qué sirve.
>
> **2 · Prepara el entorno.** Comprueba si esta práctica utiliza **Entorno I · Packet Tracer**, **Entorno II · WSL2**, **Entorno III · VirtualBox + Ubuntu 26.04 Server** o **Entorno IV · Docker Compose**. Verifica conectividad, nombres, interfaces y estado de los servicios antes de modificar nada.
>
> **3 · Predice.** Antes de ejecutar un comando importante, escribe qué esperas que ocurra. Por ejemplo: «después de `ss -lnt`, espero encontrar el servicio escuchando en TCP/80». Esta pequeña predicción convierte la práctica en una investigación y no en una receta.
>
> **4 · Construye paso a paso.** Cada número debe dejar el sistema en un estado ligeramente más completo que el anterior. Después de cada bloque, realiza una comprobación corta. Si el paso 4 depende del 3, no avances hasta que el 3 funcione.
>
> **5 · Diagnostica si falla.** No empieces reiniciando. Sigue esta secuencia: **estado → configuración → logs → puertos → red → prueba desde el cliente**. Conserva las órdenes utilizadas y la evidencia del fallo.
>
> **6 · Demuestra.** La práctica termina cuando puedes demostrar el resultado con una evidencia: captura, salida de comando, conexión desde cliente, fichero de configuración o tráfico observado.
>
> **7 · Explica.** Cierra con una breve explicación técnica: qué has configurado, qué protocolo interviene, qué puerto utiliza, cómo se verifica y qué error sería el primero que investigarías si dejara de funcionar.




Síntoma:

> VLC no reproduce el directo.

Realiza obligatoriamente:

```text
1. dig
2. ping
3. nc
4. ss
5. systemctl
6. logs
7. curl
8. ffprobe
9. captura
```

No soluciones el problema «a ciegas».

Para cada paso:

```text
PRUEBA
  ↓
RESULTADO
  ↓
HIPÓTESIS
  ↓
SIGUIENTE PRUEBA
```

---


### 🧭 Guía de resolución y comprobación

Esta práctica se considera resuelta cuando puedes **explicar y demostrar** el resultado, no solo cuando el comando termina sin errores. Sigue siempre esta secuencia:

1. **Identifica el estado inicial.** Anota interfaces, direcciones, rutas y servicios que ya estaban activos.
2. **Aplica el cambio mínimo.** No modifiques varias cosas a la vez: si algo falla, necesitas saber qué cambio lo provocó.
3. **Valida inmediatamente.** Comprueba la sintaxis o el estado del servicio antes de probar desde el cliente.
4. **Prueba desde el punto de vista del usuario.** Una configuración correcta debe producir el comportamiento esperado desde el cliente, no solo desde el servidor.
5. **Observa evidencias.** Conserva la salida de comandos, logs, capturas de tráfico y capturas de pantalla que demuestren el resultado.

**Comandos de referencia para esta práctica:**

- `ip addr`
- `ip route`
- `ss -lntup`
- `journalctl -b --no-pager`
- `ping <destino>`

> 💡 **Si algo falla:** no empieces reiniciando. Compara primero **estado → configuración → logs → puertos → red → cliente**. Un reinicio puede ocultar la causa y hacer más difícil aprender de la incidencia.

### 🧪 Rúbrica de evaluación

| Criterio | Puntos | Evidencia esperada |
|---|---:|---|
| Comprensión del objetivo y del protocolo | 2 | Explica qué servicio/protocolo está utilizando y por qué. |
| Preparación y configuración | 2 | Ficheros, comandos o topología correctamente preparados. |
| Verificación funcional | 2 | Demuestra el resultado desde un cliente o herramienta adecuada. |
| Diagnóstico y razonamiento | 2 | Utiliza evidencias para justificar la solución. |
| Documentación técnica | 1 | Incluye comandos, configuraciones y capturas relevantes. |
| Seguridad y buenas prácticas | 1 | Aplica permisos, exposición de puertos y credenciales con criterio. |
| **Total** | **10** | **Superación recomendada: ≥ 5 puntos y práctica funcional.** |


# 🔐 74. Seguridad multimedia

Un servidor multimedia puede ser abusado.

Riesgos:

```text
stream no autorizado
consumo masivo de ancho de banda
credenciales expuestas
contenido no autorizado
abuso del servidor
denegación de servicio
```

Medidas:

```text
☑ autenticación
☑ límites
☑ firewall
☑ TLS cuando proceda
☑ control de publicación
☑ logs
☑ monitorización
☑ actualización
```

---

# 🛡️ 75. No publicar secretos

Nunca subas al repositorio:

```text
stream keys
passwords
private keys
tokens
credenciales
```

Utiliza:

```text
.env
variables de entorno
secret managers
ficheros fuera de Git
```

y:

```gitignore
.env
*.key
*.pem
secrets/
```

---

# 🧪 76. PRÁCTICA 8.19 — Git seguro
> 🧭 **PREPARACIÓN DE LA PRÁCTICA**
>
> **1 · Sitúate.** Lee primero el objetivo y localiza en la unidad el concepto que estamos llevando a la práctica. No empieces copiando comandos: primero debes poder explicar qué componente estamos construyendo y para qué sirve.
>
> **2 · Prepara el entorno.** Comprueba si esta práctica utiliza **Entorno I · Packet Tracer**, **Entorno II · WSL2**, **Entorno III · VirtualBox + Ubuntu 26.04 Server** o **Entorno IV · Docker Compose**. Verifica conectividad, nombres, interfaces y estado de los servicios antes de modificar nada.
>
> **3 · Predice.** Antes de ejecutar un comando importante, escribe qué esperas que ocurra. Por ejemplo: «después de `ss -lnt`, espero encontrar el servicio escuchando en TCP/80». Esta pequeña predicción convierte la práctica en una investigación y no en una receta.
>
> **4 · Construye paso a paso.** Cada número debe dejar el sistema en un estado ligeramente más completo que el anterior. Después de cada bloque, realiza una comprobación corta. Si el paso 4 depende del 3, no avances hasta que el 3 funcione.
>
> **5 · Diagnostica si falla.** No empieces reiniciando. Sigue esta secuencia: **estado → configuración → logs → puertos → red → prueba desde el cliente**. Conserva las órdenes utilizadas y la evidencia del fallo.
>
> **6 · Demuestra.** La práctica termina cuando puedes demostrar el resultado con una evidencia: captura, salida de comando, conexión desde cliente, fichero de configuración o tráfico observado.
>
> **7 · Explica.** Cierra con una breve explicación técnica: qué has configurado, qué protocolo interviene, qué puerto utiliza, cómo se verifica y qué error sería el primero que investigarías si dejara de funcionar.




Crea:

```text
.env.example
```

Ejemplo:

```text
ICECAST_SOURCE_PASSWORD=CAMBIAR
RTMP_STREAM_KEY=CAMBIAR
```

Pero nunca:

```text
.env
```

con las credenciales reales.

---


### 🧭 Guía de resolución y comprobación

Esta práctica se considera resuelta cuando puedes **explicar y demostrar** el resultado, no solo cuando el comando termina sin errores. Sigue siempre esta secuencia:

1. **Identifica el estado inicial.** Anota interfaces, direcciones, rutas y servicios que ya estaban activos.
2. **Aplica el cambio mínimo.** No modifiques varias cosas a la vez: si algo falla, necesitas saber qué cambio lo provocó.
3. **Valida inmediatamente.** Comprueba la sintaxis o el estado del servicio antes de probar desde el cliente.
4. **Prueba desde el punto de vista del usuario.** Una configuración correcta debe producir el comportamiento esperado desde el cliente, no solo desde el servidor.
5. **Observa evidencias.** Conserva la salida de comandos, logs, capturas de tráfico y capturas de pantalla que demuestren el resultado.

**Comandos de referencia para esta práctica:**

- `ip addr`
- `ip route`
- `ss -lntup`
- `journalctl -b --no-pager`
- `ping <destino>`

> 💡 **Si algo falla:** no empieces reiniciando. Compara primero **estado → configuración → logs → puertos → red → cliente**. Un reinicio puede ocultar la causa y hacer más difícil aprender de la incidencia.

### 🧪 Rúbrica de evaluación

| Criterio | Puntos | Evidencia esperada |
|---|---:|---|
| Comprensión del objetivo y del protocolo | 2 | Explica qué servicio/protocolo está utilizando y por qué. |
| Preparación y configuración | 2 | Ficheros, comandos o topología correctamente preparados. |
| Verificación funcional | 2 | Demuestra el resultado desde un cliente o herramienta adecuada. |
| Diagnóstico y razonamiento | 2 | Utiliza evidencias para justificar la solución. |
| Documentación técnica | 1 | Incluye comandos, configuraciones y capturas relevantes. |
| Seguridad y buenas prácticas | 1 | Aplica permisos, exposición de puertos y credenciales con criterio. |
| **Total** | **10** | **Superación recomendada: ≥ 5 puntos y práctica funcional.** |


# 📊 77. Comparativa de tecnologías

| Tecnología | Función | Uso principal en la UT |
|---|---|---|
| Icecast | Servidor audio | ⭐ Laboratorio |
| FFmpeg | Codificación/transcodificación | ⭐ Laboratorio |
| VLC | Cliente/reproductor | ⭐ Laboratorio |
| Nginx | HTTP | ⭐ Laboratorio |
| nginx-rtmp-module | RTMP/HLS | ⭐ Laboratorio |
| HLS | Distribución HTTP | ⭐ Laboratorio |
| RTMP | Ingest/directo | ⭐ Laboratorio |
| RTP | Transporte multimedia tiempo real | Conceptual/análisis |
| SIP | Señalización VoIP | Conceptual |
| WebRTC | Multimedia interactiva | Videoconferencia |

---

# 🧪 78. PRÁCTICA 8.20 — Proyecto integrado
> 🧭 **PREPARACIÓN DE LA PRÁCTICA**
>
> **1 · Sitúate.** Lee primero el objetivo y localiza en la unidad el concepto que estamos llevando a la práctica. No empieces copiando comandos: primero debes poder explicar qué componente estamos construyendo y para qué sirve.
>
> **2 · Prepara el entorno.** Comprueba si esta práctica utiliza **Entorno I · Packet Tracer**, **Entorno II · WSL2**, **Entorno III · VirtualBox + Ubuntu 26.04 Server** o **Entorno IV · Docker Compose**. Verifica conectividad, nombres, interfaces y estado de los servicios antes de modificar nada.
>
> **3 · Predice.** Antes de ejecutar un comando importante, escribe qué esperas que ocurra. Por ejemplo: «después de `ss -lnt`, espero encontrar el servicio escuchando en TCP/80». Esta pequeña predicción convierte la práctica en una investigación y no en una receta.
>
> **4 · Construye paso a paso.** Cada número debe dejar el sistema en un estado ligeramente más completo que el anterior. Después de cada bloque, realiza una comprobación corta. Si el paso 4 depende del 3, no avances hasta que el 3 funcione.
>
> **5 · Diagnostica si falla.** No empieces reiniciando. Sigue esta secuencia: **estado → configuración → logs → puertos → red → prueba desde el cliente**. Conserva las órdenes utilizadas y la evidencia del fallo.
>
> **6 · Demuestra.** La práctica termina cuando puedes demostrar el resultado con una evidencia: captura, salida de comando, conexión desde cliente, fichero de configuración o tráfico observado.
>
> **7 · Explica.** Cierra con una breve explicación técnica: qué has configurado, qué protocolo interviene, qué puerto utiliza, cómo se verifica y qué error sería el primero que investigarías si dejara de funcionar.




Construye:

```text
                    DNS
                     │
          ┌──────────┴──────────┐
          │                     │
      radio.asir.test       video.asir.test
          │                     │
          ▼                     ▼
       Icecast              Nginx/RTMP
          │                     │
          │                     ▼
          │                    HLS
          │                     │
          ▼                     ▼
         VLC                  VLC/Web
```

### Audio

```text
FFmpeg → Icecast → VLC
```

### Vídeo

```text
FFmpeg → RTMP → Nginx → HLS → VLC
```

---


### 🧭 Guía de resolución y comprobación

Esta práctica se considera resuelta cuando puedes **explicar y demostrar** el resultado, no solo cuando el comando termina sin errores. Sigue siempre esta secuencia:

1. **Identifica el estado inicial.** Anota interfaces, direcciones, rutas y servicios que ya estaban activos.
2. **Aplica el cambio mínimo.** No modifiques varias cosas a la vez: si algo falla, necesitas saber qué cambio lo provocó.
3. **Valida inmediatamente.** Comprueba la sintaxis o el estado del servicio antes de probar desde el cliente.
4. **Prueba desde el punto de vista del usuario.** Una configuración correcta debe producir el comportamiento esperado desde el cliente, no solo desde el servidor.
5. **Observa evidencias.** Conserva la salida de comandos, logs, capturas de tráfico y capturas de pantalla que demuestren el resultado.

**Comandos de referencia para esta práctica:**

- `ip addr`
- `ip route`
- `ss -lntup`
- `journalctl -b --no-pager`
- `ping <destino>`

> 💡 **Si algo falla:** no empieces reiniciando. Compara primero **estado → configuración → logs → puertos → red → cliente**. Un reinicio puede ocultar la causa y hacer más difícil aprender de la incidencia.

### 🧪 Rúbrica de evaluación

| Criterio | Puntos | Evidencia esperada |
|---|---:|---|
| Comprensión del objetivo y del protocolo | 2 | Explica qué servicio/protocolo está utilizando y por qué. |
| Preparación y configuración | 2 | Ficheros, comandos o topología correctamente preparados. |
| Verificación funcional | 2 | Demuestra el resultado desde un cliente o herramienta adecuada. |
| Diagnóstico y razonamiento | 2 | Utiliza evidencias para justificar la solución. |
| Documentación técnica | 1 | Incluye comandos, configuraciones y capturas relevantes. |
| Seguridad y buenas prácticas | 1 | Aplica permisos, exposición de puertos y credenciales con criterio. |
| **Total** | **10** | **Superación recomendada: ≥ 5 puntos y práctica funcional.** |


# 🏆 79. Reto profesional

## «La radio funciona, el vídeo no»

Dispones de:

```text
radio.asir.test
video.asir.test
```

Radio:

```text
✔ DNS
✔ TCP/8000
✔ Icecast
✔ VLC
```

Vídeo:

```text
✔ DNS
✔ TCP/1935
❌ VLC
```

Debes determinar si el fallo está en:

```text
RTMP
Nginx
FFmpeg
HLS
HTTP
playlist
segmentos
codec
cliente
```

### Evidencias obligatorias

```bash
dig
ss
nc
systemctl
journalctl
curl
ffprobe
tcpdump
```

---

# 🏆 80. Reto profesional 2 — Escalabilidad

Una empresa quiere distribuir:

```text
vídeo 1080p
8 Mbit/s
500 usuarios simultáneos
```

Calcula el tráfico aproximado necesario.

Después analiza:

```text
servidor
NIC
switch
router
firewall
Internet
CDN
```

Explica qué elementos se convierten en posibles cuellos de botella.

---

# 🧠 81. Errores conceptuales frecuentes

### ❌ «MP4 es un códec»

No.

```text
MP4 = contenedor
```

### ❌ «H.264 es un formato contenedor»

No.

```text
H.264 = códec de vídeo
```

### ❌ «RTMP y HLS son lo mismo»

No.

```text
RTMP → protocolo
HLS  → mecanismo de distribución HTTP mediante playlist/segmentos
```

### ❌ «Más bitrate siempre es mejor»

No necesariamente.

### ❌ «Si hay ping, el streaming funciona»

No.

`ping` no demuestra:

```text
puerto
servicio
protocolo
codec
buffer
```

---

# 🧪 82. Práctica de integración con Packet Tracer
> 🧭 **PREPARACIÓN DE LA PRÁCTICA**
>
> **1 · Sitúate.** Lee primero el objetivo y localiza en la unidad el concepto que estamos llevando a la práctica. No empieces copiando comandos: primero debes poder explicar qué componente estamos construyendo y para qué sirve.
>
> **2 · Prepara el entorno.** Comprueba si esta práctica utiliza **Entorno I · Packet Tracer**, **Entorno II · WSL2**, **Entorno III · VirtualBox + Ubuntu 26.04 Server** o **Entorno IV · Docker Compose**. Verifica conectividad, nombres, interfaces y estado de los servicios antes de modificar nada.
>
> **3 · Predice.** Antes de ejecutar un comando importante, escribe qué esperas que ocurra. Por ejemplo: «después de `ss -lnt`, espero encontrar el servicio escuchando en TCP/80». Esta pequeña predicción convierte la práctica en una investigación y no en una receta.
>
> **4 · Construye paso a paso.** Cada número debe dejar el sistema en un estado ligeramente más completo que el anterior. Después de cada bloque, realiza una comprobación corta. Si el paso 4 depende del 3, no avances hasta que el 3 funcione.
>
> **5 · Diagnostica si falla.** No empieces reiniciando. Sigue esta secuencia: **estado → configuración → logs → puertos → red → prueba desde el cliente**. Conserva las órdenes utilizadas y la evidencia del fallo.
>
> **6 · Demuestra.** La práctica termina cuando puedes demostrar el resultado con una evidencia: captura, salida de comando, conexión desde cliente, fichero de configuración o tráfico observado.
>
> **7 · Explica.** Cierra con una breve explicación técnica: qué has configurado, qué protocolo interviene, qué puerto utiliza, cómo se verifica y qué error sería el primero que investigarías si dejara de funcionar.




Packet Tracer no sustituye a Icecast, Nginx RTMP o FFmpeg.

Su función aquí es representar:

```text
cliente
   │
switch
   │
router
   │
servidor
```

y estudiar:

```text
IP
TCP
puertos
rutas
```

La implementación multimedia real se realiza en:

```text
VirtualBox + Ubuntu 26.04 Server
```

---


### 🧭 Guía de resolución y comprobación

Esta práctica se considera resuelta cuando puedes **explicar y demostrar** el resultado, no solo cuando el comando termina sin errores. Sigue siempre esta secuencia:

1. **Identifica el estado inicial.** Anota interfaces, direcciones, rutas y servicios que ya estaban activos.
2. **Aplica el cambio mínimo.** No modifiques varias cosas a la vez: si algo falla, necesitas saber qué cambio lo provocó.
3. **Valida inmediatamente.** Comprueba la sintaxis o el estado del servicio antes de probar desde el cliente.
4. **Prueba desde el punto de vista del usuario.** Una configuración correcta debe producir el comportamiento esperado desde el cliente, no solo desde el servidor.
5. **Observa evidencias.** Conserva la salida de comandos, logs, capturas de tráfico y capturas de pantalla que demuestren el resultado.

**Comandos de referencia para esta práctica:**

- `show ip interface brief`
- `show ip route`
- `show running-config`
- `ping <destino>`
- `traceroute <destino>`

> 💡 **Si algo falla:** no empieces reiniciando. Compara primero **estado → configuración → logs → puertos → red → cliente**. Un reinicio puede ocultar la causa y hacer más difícil aprender de la incidencia.

### 🧪 Rúbrica de evaluación

| Criterio | Puntos | Evidencia esperada |
|---|---:|---|
| Comprensión del objetivo y del protocolo | 2 | Explica qué servicio/protocolo está utilizando y por qué. |
| Preparación y configuración | 2 | Ficheros, comandos o topología correctamente preparados. |
| Verificación funcional | 2 | Demuestra el resultado desde un cliente o herramienta adecuada. |
| Diagnóstico y razonamiento | 2 | Utiliza evidencias para justificar la solución. |
| Documentación técnica | 1 | Incluye comandos, configuraciones y capturas relevantes. |
| Seguridad y buenas prácticas | 1 | Aplica permisos, exposición de puertos y credenciales con criterio. |
| **Total** | **10** | **Superación recomendada: ≥ 5 puntos y práctica funcional.** |


# 🧪 83. Topología Packet Tracer
### 🧭 Guía de resolución y comprobación

**Puntos a conseguir:** dejar el sistema en el estado solicitado, poder explicar qué protocolo interviene, comprobarlo desde un cliente y aportar evidencias reproducibles.

1. **Preparar** el entorno y registrar el estado inicial.
2. **Construir** solo el siguiente elemento necesario.
3. **Validar** sintaxis y servicio.
4. **Probar** desde el cliente.
5. **Observar** puertos, logs y tráfico cuando proceda.
6. **Documentar** configuración, comandos y capturas.


#### Solución de referencia

La evidencia mínima es `show ip interface brief`, `show ip route`, la configuración relevante y una prueba extremo a extremo. En Packet Tracer, utiliza Simulation Mode cuando necesites demostrar el recorrido de los paquetes y no solo el resultado del `ping`.


### 📸 Evidencias y capturas

Incluye, cuando aporte información, una captura de la topología, del fichero o interfaz configurada, del estado del servicio y de la prueba final. Cada captura debe llevar una frase que explique **qué demuestra**; una imagen sin interpretación no constituye una evidencia técnica suficiente.

### 🧪 Rúbrica de evaluación

| Criterio | Puntos |
|---|---:|
| Comprensión del servicio/protocolo | 2 |
| Configuración y proceso | 2 |
| Funcionamiento demostrado | 2 |
| Diagnóstico y razonamiento | 2 |
| Documentación y evidencias | 1 |
| Seguridad y buenas prácticas | 1 |
| **Total** | **10** |


```text
                  ROUTER
                 /      \
                /        \
              SW1        SERVER
             /   \
           PC1   PC2
```

Configura:

```text
192.168.100.0/24
```

Comprueba:

```text
ping
```

Después relaciona:

```text
IP
 ↓
TCP
 ↓
puerto
 ↓
servicio multimedia
```

---

# 🐧 84. WSL2 como estación de análisis

WSL2 proporciona herramientas especialmente útiles:

```bash
sudo apt update
sudo apt install \
  ffmpeg \
  vlc \
  dnsutils \
  netcat-openbsd \
  tcpdump \
  curl
```

Herramientas:

```text
ffprobe → metadatos multimedia
ffmpeg  → conversión/codificación
curl    → HTTP
nc      → TCP
dig     → DNS
tcpdump → captura
```

---

# 🖥️ 85. VirtualBox + Ubuntu 26.04 Server

Servidor recomendado:

```text
hostname:
media.asir.test
```

Servicios:

```text
DNS
Icecast
Nginx
RTMP
HLS
```

Red:

```text
192.168.100.10
```

Arquitectura:

```text
                 media.asir.test
                       │
          ┌────────────┼────────────┐
          │            │            │
       :8000         :80         :1935
       Icecast       HTTP        RTMP
          │            │            │
          │            │            ▼
          │            │          HLS
          │            │            │
          └────────────┴────────────┘
                       │
                      VLC
```

---

# 🧪 86. PRÁCTICA 8.21 — Monitorización
> 🧭 **PREPARACIÓN DE LA PRÁCTICA**
>
> **1 · Sitúate.** Lee primero el objetivo y localiza en la unidad el concepto que estamos llevando a la práctica. No empieces copiando comandos: primero debes poder explicar qué componente estamos construyendo y para qué sirve.
>
> **2 · Prepara el entorno.** Comprueba si esta práctica utiliza **Entorno I · Packet Tracer**, **Entorno II · WSL2**, **Entorno III · VirtualBox + Ubuntu 26.04 Server** o **Entorno IV · Docker Compose**. Verifica conectividad, nombres, interfaces y estado de los servicios antes de modificar nada.
>
> **3 · Predice.** Antes de ejecutar un comando importante, escribe qué esperas que ocurra. Por ejemplo: «después de `ss -lnt`, espero encontrar el servicio escuchando en TCP/80». Esta pequeña predicción convierte la práctica en una investigación y no en una receta.
>
> **4 · Construye paso a paso.** Cada número debe dejar el sistema en un estado ligeramente más completo que el anterior. Después de cada bloque, realiza una comprobación corta. Si el paso 4 depende del 3, no avances hasta que el 3 funcione.
>
> **5 · Diagnostica si falla.** No empieces reiniciando. Sigue esta secuencia: **estado → configuración → logs → puertos → red → prueba desde el cliente**. Conserva las órdenes utilizadas y la evidencia del fallo.
>
> **6 · Demuestra.** La práctica termina cuando puedes demostrar el resultado con una evidencia: captura, salida de comando, conexión desde cliente, fichero de configuración o tráfico observado.
>
> **7 · Explica.** Cierra con una breve explicación técnica: qué has configurado, qué protocolo interviene, qué puerto utiliza, cómo se verifica y qué error sería el primero que investigarías si dejara de funcionar.




Comprueba:

```bash
sudo ss -ltnp
```

Filtra:

```bash
sudo ss -ltnp | grep -E ':80|:8000|:1935'
```

CPU:

```bash
top
```

Memoria:

```bash
free -h
```

Red:

```bash
ip -s link
```

Procesos:

```bash
ps aux | grep -E 'ffmpeg|nginx|icecast'
```

---


### 🧭 Guía de resolución y comprobación

Esta práctica se considera resuelta cuando puedes **explicar y demostrar** el resultado, no solo cuando el comando termina sin errores. Sigue siempre esta secuencia:

1. **Identifica el estado inicial.** Anota interfaces, direcciones, rutas y servicios que ya estaban activos.
2. **Aplica el cambio mínimo.** No modifiques varias cosas a la vez: si algo falla, necesitas saber qué cambio lo provocó.
3. **Valida inmediatamente.** Comprueba la sintaxis o el estado del servicio antes de probar desde el cliente.
4. **Prueba desde el punto de vista del usuario.** Una configuración correcta debe producir el comportamiento esperado desde el cliente, no solo desde el servidor.
5. **Observa evidencias.** Conserva la salida de comandos, logs, capturas de tráfico y capturas de pantalla que demuestren el resultado.

**Comandos de referencia para esta práctica:**

- `ip addr`
- `ip route`
- `ss -lntup`
- `journalctl -b --no-pager`
- `ping <destino>`

> 💡 **Si algo falla:** no empieces reiniciando. Compara primero **estado → configuración → logs → puertos → red → cliente**. Un reinicio puede ocultar la causa y hacer más difícil aprender de la incidencia.

### 🧪 Rúbrica de evaluación

| Criterio | Puntos | Evidencia esperada |
|---|---:|---|
| Comprensión del objetivo y del protocolo | 2 | Explica qué servicio/protocolo está utilizando y por qué. |
| Preparación y configuración | 2 | Ficheros, comandos o topología correctamente preparados. |
| Verificación funcional | 2 | Demuestra el resultado desde un cliente o herramienta adecuada. |
| Diagnóstico y razonamiento | 2 | Utiliza evidencias para justificar la solución. |
| Documentación técnica | 1 | Incluye comandos, configuraciones y capturas relevantes. |
| Seguridad y buenas prácticas | 1 | Aplica permisos, exposición de puertos y credenciales con criterio. |
| **Total** | **10** | **Superación recomendada: ≥ 5 puntos y práctica funcional.** |


# 📈 87. Monitorización multimedia

Una infraestructura multimedia debe observar:

```text
CPU
RAM
red
conexiones
bitrate
clientes
latencia
errores
```

En Icecast interesa especialmente:

```text
sources
listeners
mountpoints
```

En Nginx/RTMP:

```text
publish
play
streams
conexiones
errores
```

---

# 🧪 88. PRÁCTICA 8.22 — Captura de tráfico
> 🧭 **PREPARACIÓN DE LA PRÁCTICA**
>
> **1 · Sitúate.** Lee primero el objetivo y localiza en la unidad el concepto que estamos llevando a la práctica. No empieces copiando comandos: primero debes poder explicar qué componente estamos construyendo y para qué sirve.
>
> **2 · Prepara el entorno.** Comprueba si esta práctica utiliza **Entorno I · Packet Tracer**, **Entorno II · WSL2**, **Entorno III · VirtualBox + Ubuntu 26.04 Server** o **Entorno IV · Docker Compose**. Verifica conectividad, nombres, interfaces y estado de los servicios antes de modificar nada.
>
> **3 · Predice.** Antes de ejecutar un comando importante, escribe qué esperas que ocurra. Por ejemplo: «después de `ss -lnt`, espero encontrar el servicio escuchando en TCP/80». Esta pequeña predicción convierte la práctica en una investigación y no en una receta.
>
> **4 · Construye paso a paso.** Cada número debe dejar el sistema en un estado ligeramente más completo que el anterior. Después de cada bloque, realiza una comprobación corta. Si el paso 4 depende del 3, no avances hasta que el 3 funcione.
>
> **5 · Diagnostica si falla.** No empieces reiniciando. Sigue esta secuencia: **estado → configuración → logs → puertos → red → prueba desde el cliente**. Conserva las órdenes utilizadas y la evidencia del fallo.
>
> **6 · Demuestra.** La práctica termina cuando puedes demostrar el resultado con una evidencia: captura, salida de comando, conexión desde cliente, fichero de configuración o tráfico observado.
>
> **7 · Explica.** Cierra con una breve explicación técnica: qué has configurado, qué protocolo interviene, qué puerto utiliza, cómo se verifica y qué error sería el primero que investigarías si dejara de funcionar.




Audio Icecast:

```bash
sudo tcpdump -ni any port 8000
```

RTMP:

```bash
sudo tcpdump -ni any port 1935
```

HTTP/HLS:

```bash
sudo tcpdump -ni any port 80
```

Relaciona:

```text
puerto
protocolo
flujo
cliente
servidor
```

---


### 🧭 Guía de resolución y comprobación

Esta práctica se considera resuelta cuando puedes **explicar y demostrar** el resultado, no solo cuando el comando termina sin errores. Sigue siempre esta secuencia:

1. **Identifica el estado inicial.** Anota interfaces, direcciones, rutas y servicios que ya estaban activos.
2. **Aplica el cambio mínimo.** No modifiques varias cosas a la vez: si algo falla, necesitas saber qué cambio lo provocó.
3. **Valida inmediatamente.** Comprueba la sintaxis o el estado del servicio antes de probar desde el cliente.
4. **Prueba desde el punto de vista del usuario.** Una configuración correcta debe producir el comportamiento esperado desde el cliente, no solo desde el servidor.
5. **Observa evidencias.** Conserva la salida de comandos, logs, capturas de tráfico y capturas de pantalla que demuestren el resultado.

**Comandos de referencia para esta práctica:**

- `ip addr`
- `ip route`
- `ss -lntup`
- `journalctl -b --no-pager`
- `ping <destino>`

> 💡 **Si algo falla:** no empieces reiniciando. Compara primero **estado → configuración → logs → puertos → red → cliente**. Un reinicio puede ocultar la causa y hacer más difícil aprender de la incidencia.

### 🧪 Rúbrica de evaluación

| Criterio | Puntos | Evidencia esperada |
|---|---:|---|
| Comprensión del objetivo y del protocolo | 2 | Explica qué servicio/protocolo está utilizando y por qué. |
| Preparación y configuración | 2 | Ficheros, comandos o topología correctamente preparados. |
| Verificación funcional | 2 | Demuestra el resultado desde un cliente o herramienta adecuada. |
| Diagnóstico y razonamiento | 2 | Utiliza evidencias para justificar la solución. |
| Documentación técnica | 1 | Incluye comandos, configuraciones y capturas relevantes. |
| Seguridad y buenas prácticas | 1 | Aplica permisos, exposición de puertos y credenciales con criterio. |
| **Total** | **10** | **Superación recomendada: ≥ 5 puntos y práctica funcional.** |


# 🔬 89. ¿Qué ocurre cuando reproducimos?

Ejemplo HLS:

```text
1. DNS
      ↓
2. TCP
      ↓
3. HTTP GET playlist.m3u8
      ↓
4. servidor responde
      ↓
5. cliente solicita segmento
      ↓
6. servidor responde
      ↓
7. cliente almacena en búfer
      ↓
8. decodifica
      ↓
9. reproduce
      ↓
10. solicita siguiente segmento
```

---

# 🧪 90. PRÁCTICA 8.23 — Analizar HLS
> 🧭 **PREPARACIÓN DE LA PRÁCTICA**
>
> **1 · Sitúate.** Lee primero el objetivo y localiza en la unidad el concepto que estamos llevando a la práctica. No empieces copiando comandos: primero debes poder explicar qué componente estamos construyendo y para qué sirve.
>
> **2 · Prepara el entorno.** Comprueba si esta práctica utiliza **Entorno I · Packet Tracer**, **Entorno II · WSL2**, **Entorno III · VirtualBox + Ubuntu 26.04 Server** o **Entorno IV · Docker Compose**. Verifica conectividad, nombres, interfaces y estado de los servicios antes de modificar nada.
>
> **3 · Predice.** Antes de ejecutar un comando importante, escribe qué esperas que ocurra. Por ejemplo: «después de `ss -lnt`, espero encontrar el servicio escuchando en TCP/80». Esta pequeña predicción convierte la práctica en una investigación y no en una receta.
>
> **4 · Construye paso a paso.** Cada número debe dejar el sistema en un estado ligeramente más completo que el anterior. Después de cada bloque, realiza una comprobación corta. Si el paso 4 depende del 3, no avances hasta que el 3 funcione.
>
> **5 · Diagnostica si falla.** No empieces reiniciando. Sigue esta secuencia: **estado → configuración → logs → puertos → red → prueba desde el cliente**. Conserva las órdenes utilizadas y la evidencia del fallo.
>
> **6 · Demuestra.** La práctica termina cuando puedes demostrar el resultado con una evidencia: captura, salida de comando, conexión desde cliente, fichero de configuración o tráfico observado.
>
> **7 · Explica.** Cierra con una breve explicación técnica: qué has configurado, qué protocolo interviene, qué puerto utiliza, cómo se verifica y qué error sería el primero que investigarías si dejara de funcionar.




Captura:

```text
tcp.port == 80
```

Busca:

```text
.m3u8
```

Después:

```text
.ts
```

o los segmentos utilizados por la implementación.

Explica:

```text
playlist
   ↓
segmento 1
   ↓
segmento 2
   ↓
segmento 3
```

---


### 🧭 Guía de resolución y comprobación

Esta práctica se considera resuelta cuando puedes **explicar y demostrar** el resultado, no solo cuando el comando termina sin errores. Sigue siempre esta secuencia:

1. **Identifica el estado inicial.** Anota interfaces, direcciones, rutas y servicios que ya estaban activos.
2. **Aplica el cambio mínimo.** No modifiques varias cosas a la vez: si algo falla, necesitas saber qué cambio lo provocó.
3. **Valida inmediatamente.** Comprueba la sintaxis o el estado del servicio antes de probar desde el cliente.
4. **Prueba desde el punto de vista del usuario.** Una configuración correcta debe producir el comportamiento esperado desde el cliente, no solo desde el servidor.
5. **Observa evidencias.** Conserva la salida de comandos, logs, capturas de tráfico y capturas de pantalla que demuestren el resultado.

**Comandos de referencia para esta práctica:**

- `ip addr`
- `ip route`
- `ss -lntup`
- `journalctl -b --no-pager`
- `ping <destino>`

> 💡 **Si algo falla:** no empieces reiniciando. Compara primero **estado → configuración → logs → puertos → red → cliente**. Un reinicio puede ocultar la causa y hacer más difícil aprender de la incidencia.

### 🧪 Rúbrica de evaluación

| Criterio | Puntos | Evidencia esperada |
|---|---:|---|
| Comprensión del objetivo y del protocolo | 2 | Explica qué servicio/protocolo está utilizando y por qué. |
| Preparación y configuración | 2 | Ficheros, comandos o topología correctamente preparados. |
| Verificación funcional | 2 | Demuestra el resultado desde un cliente o herramienta adecuada. |
| Diagnóstico y razonamiento | 2 | Utiliza evidencias para justificar la solución. |
| Documentación técnica | 1 | Incluye comandos, configuraciones y capturas relevantes. |
| Seguridad y buenas prácticas | 1 | Aplica permisos, exposición de puertos y credenciales con criterio. |
| **Total** | **10** | **Superación recomendada: ≥ 5 puntos y práctica funcional.** |


# 🔧 91. Transcodificación

Puede ser necesario convertir:

```text
entrada
   ↓
FFmpeg
   ↓
salida
```

Ejemplo:

```bash
ffmpeg \
  -i entrada.mkv \
  -c:v libx264 \
  -c:a aac \
  salida.mp4
```

No confundas:

```text
transcodificación
```

con:

```text
cambio de contenedor sin recodificar
```

---

# 🧪 92. PRÁCTICA 8.24 — Remux frente a transcodificación
> 🧭 **PREPARACIÓN DE LA PRÁCTICA**
>
> **1 · Sitúate.** Lee primero el objetivo y localiza en la unidad el concepto que estamos llevando a la práctica. No empieces copiando comandos: primero debes poder explicar qué componente estamos construyendo y para qué sirve.
>
> **2 · Prepara el entorno.** Comprueba si esta práctica utiliza **Entorno I · Packet Tracer**, **Entorno II · WSL2**, **Entorno III · VirtualBox + Ubuntu 26.04 Server** o **Entorno IV · Docker Compose**. Verifica conectividad, nombres, interfaces y estado de los servicios antes de modificar nada.
>
> **3 · Predice.** Antes de ejecutar un comando importante, escribe qué esperas que ocurra. Por ejemplo: «después de `ss -lnt`, espero encontrar el servicio escuchando en TCP/80». Esta pequeña predicción convierte la práctica en una investigación y no en una receta.
>
> **4 · Construye paso a paso.** Cada número debe dejar el sistema en un estado ligeramente más completo que el anterior. Después de cada bloque, realiza una comprobación corta. Si el paso 4 depende del 3, no avances hasta que el 3 funcione.
>
> **5 · Diagnostica si falla.** No empieces reiniciando. Sigue esta secuencia: **estado → configuración → logs → puertos → red → prueba desde el cliente**. Conserva las órdenes utilizadas y la evidencia del fallo.
>
> **6 · Demuestra.** La práctica termina cuando puedes demostrar el resultado con una evidencia: captura, salida de comando, conexión desde cliente, fichero de configuración o tráfico observado.
>
> **7 · Explica.** Cierra con una breve explicación técnica: qué has configurado, qué protocolo interviene, qué puerto utiliza, cómo se verifica y qué error sería el primero que investigarías si dejara de funcionar.




### Remux

```bash
ffmpeg -i entrada.mkv -c copy salida.mp4
```

### Transcodificación

```bash
ffmpeg \
  -i entrada.mkv \
  -c:v libx264 \
  -c:a aac \
  salida.mp4
```

Compara:

```text
CPU
tiempo
tamaño
calidad
```

---


### 🧭 Guía de resolución y comprobación

Esta práctica se considera resuelta cuando puedes **explicar y demostrar** el resultado, no solo cuando el comando termina sin errores. Sigue siempre esta secuencia:

1. **Identifica el estado inicial.** Anota interfaces, direcciones, rutas y servicios que ya estaban activos.
2. **Aplica el cambio mínimo.** No modifiques varias cosas a la vez: si algo falla, necesitas saber qué cambio lo provocó.
3. **Valida inmediatamente.** Comprueba la sintaxis o el estado del servicio antes de probar desde el cliente.
4. **Prueba desde el punto de vista del usuario.** Una configuración correcta debe producir el comportamiento esperado desde el cliente, no solo desde el servidor.
5. **Observa evidencias.** Conserva la salida de comandos, logs, capturas de tráfico y capturas de pantalla que demuestren el resultado.

**Comandos de referencia para esta práctica:**

- `ip addr`
- `ip route`
- `ss -lntup`
- `journalctl -b --no-pager`
- `ping <destino>`

> 💡 **Si algo falla:** no empieces reiniciando. Compara primero **estado → configuración → logs → puertos → red → cliente**. Un reinicio puede ocultar la causa y hacer más difícil aprender de la incidencia.

### 🧪 Rúbrica de evaluación

| Criterio | Puntos | Evidencia esperada |
|---|---:|---|
| Comprensión del objetivo y del protocolo | 2 | Explica qué servicio/protocolo está utilizando y por qué. |
| Preparación y configuración | 2 | Ficheros, comandos o topología correctamente preparados. |
| Verificación funcional | 2 | Demuestra el resultado desde un cliente o herramienta adecuada. |
| Diagnóstico y razonamiento | 2 | Utiliza evidencias para justificar la solución. |
| Documentación técnica | 1 | Incluye comandos, configuraciones y capturas relevantes. |
| Seguridad y buenas prácticas | 1 | Aplica permisos, exposición de puertos y credenciales con criterio. |
| **Total** | **10** | **Superación recomendada: ≥ 5 puntos y práctica funcional.** |


# 🧮 93. Almacenamiento

Para vídeo:

```text
tamaño ≈ bitrate × duración
```

Ejemplo:

```text
8 Mbit/s
1 hora
```

Aproximación:

```text
8.000.000 bit/s
× 3600 s
= 28.800.000.000 bits
```

Dividiendo entre 8:

```text
3.600.000.000 bytes
```

aproximadamente:

```text
3,6 GB
```

sin considerar audio adicional, contenedor y otros factores.

---

# 🧪 94. PRÁCTICA 8.25 — Planificar almacenamiento
> 🧭 **PREPARACIÓN DE LA PRÁCTICA**
>
> **1 · Sitúate.** Lee primero el objetivo y localiza en la unidad el concepto que estamos llevando a la práctica. No empieces copiando comandos: primero debes poder explicar qué componente estamos construyendo y para qué sirve.
>
> **2 · Prepara el entorno.** Comprueba si esta práctica utiliza **Entorno I · Packet Tracer**, **Entorno II · WSL2**, **Entorno III · VirtualBox + Ubuntu 26.04 Server** o **Entorno IV · Docker Compose**. Verifica conectividad, nombres, interfaces y estado de los servicios antes de modificar nada.
>
> **3 · Predice.** Antes de ejecutar un comando importante, escribe qué esperas que ocurra. Por ejemplo: «después de `ss -lnt`, espero encontrar el servicio escuchando en TCP/80». Esta pequeña predicción convierte la práctica en una investigación y no en una receta.
>
> **4 · Construye paso a paso.** Cada número debe dejar el sistema en un estado ligeramente más completo que el anterior. Después de cada bloque, realiza una comprobación corta. Si el paso 4 depende del 3, no avances hasta que el 3 funcione.
>
> **5 · Diagnostica si falla.** No empieces reiniciando. Sigue esta secuencia: **estado → configuración → logs → puertos → red → prueba desde el cliente**. Conserva las órdenes utilizadas y la evidencia del fallo.
>
> **6 · Demuestra.** La práctica termina cuando puedes demostrar el resultado con una evidencia: captura, salida de comando, conexión desde cliente, fichero de configuración o tráfico observado.
>
> **7 · Explica.** Cierra con una breve explicación técnica: qué has configurado, qué protocolo interviene, qué puerto utiliza, cómo se verifica y qué error sería el primero que investigarías si dejara de funcionar.




Calcula cuánto espacio necesitas para:

```text
10 vídeos
1 hora cada uno
8 Mbit/s
```

Después compara con:

```text
4 Mbit/s
```

y:

```text
12 Mbit/s
```

Explica la relación entre:

```text
calidad
bitrate
almacenamiento
ancho de banda
```

---


### 🧭 Guía de resolución y comprobación

Esta práctica se considera resuelta cuando puedes **explicar y demostrar** el resultado, no solo cuando el comando termina sin errores. Sigue siempre esta secuencia:

1. **Identifica el estado inicial.** Anota interfaces, direcciones, rutas y servicios que ya estaban activos.
2. **Aplica el cambio mínimo.** No modifiques varias cosas a la vez: si algo falla, necesitas saber qué cambio lo provocó.
3. **Valida inmediatamente.** Comprueba la sintaxis o el estado del servicio antes de probar desde el cliente.
4. **Prueba desde el punto de vista del usuario.** Una configuración correcta debe producir el comportamiento esperado desde el cliente, no solo desde el servidor.
5. **Observa evidencias.** Conserva la salida de comandos, logs, capturas de tráfico y capturas de pantalla que demuestren el resultado.

**Comandos de referencia para esta práctica:**

- `ip addr`
- `ip route`
- `ss -lntup`
- `journalctl -b --no-pager`
- `ping <destino>`

> 💡 **Si algo falla:** no empieces reiniciando. Compara primero **estado → configuración → logs → puertos → red → cliente**. Un reinicio puede ocultar la causa y hacer más difícil aprender de la incidencia.

### 🧪 Rúbrica de evaluación

| Criterio | Puntos | Evidencia esperada |
|---|---:|---|
| Comprensión del objetivo y del protocolo | 2 | Explica qué servicio/protocolo está utilizando y por qué. |
| Preparación y configuración | 2 | Ficheros, comandos o topología correctamente preparados. |
| Verificación funcional | 2 | Demuestra el resultado desde un cliente o herramienta adecuada. |
| Diagnóstico y razonamiento | 2 | Utiliza evidencias para justificar la solución. |
| Documentación técnica | 1 | Incluye comandos, configuraciones y capturas relevantes. |
| Seguridad y buenas prácticas | 1 | Aplica permisos, exposición de puertos y credenciales con criterio. |
| **Total** | **10** | **Superación recomendada: ≥ 5 puntos y práctica funcional.** |


# 🛡️ 95. Checklist de seguridad

```text
☐ firewall activo
☐ solo puertos necesarios
☐ contraseñas robustas
☐ stream keys protegidas
☐ publicación autenticada
☐ HTTPS para distribución cuando proceda
☐ logs
☐ monitorización
☐ límites de clientes
☐ límites de bitrate
☐ software actualizado
☐ backups
☐ contenido autorizado
```

---

# 📦 96. Estructura del repositorio GitHub

```text
ut8-audio-video/
│
├── README.md
├── 01-formatos-multimedia.md
├── 02-codecs-contenedores.md
├── 03-reproduccion.md
├── 04-streaming.md
├── 05-icecast.md
├── 06-hls.md
├── 07-rtmp.md
├── 08-voip.md
├── 09-videoconferencia.md
├── 10-diagnostico.md
│
├── scripts/
│   ├── media-info.sh
│   └── test-stream.sh
│
├── icecast/
│   └── README.md
│
├── nginx/
│   └── README.md
│
├── packet-tracer/
│   └── README.md
│
└── capturas/
```

---

# ⚠️ 97. Qué NO debe entrar en Git

```text
.env
*.key
*.pem
stream-key.txt
passwords.txt
credenciales/
```

Incluye:

```text
.env.example
```

pero no las credenciales reales.

---

# 🏁 98. Proyecto final

## «Campus Multimedia ASIR»

Construye una pequeña infraestructura multimedia:

```text
                       DNS
                        │
             ┌──────────┴──────────┐
             │                     │
          radio                  video
             │                     │
          Icecast               Nginx
             │                  RTMP/HLS
             │                     │
             └──────────┬──────────┘
                        │
                       VLC
```

Debe proporcionar:

### 🎧 Radio

```text
/radio.mp3
```

### 📺 Vídeo

```text
/hls/ut8.m3u8
```

### 🌐 Podcast

```text
/feed.xml
```

### 📞 VoIP

Documento técnico explicando:

```text
SIP
RTP
jitter
QoS
```

### 🎥 Videoconferencia

Documento técnico explicando:

```text
WebRTC
señalización
audio
vídeo
red
```

---

# 🧪 99. Entrega del proyecto
### 🧭 Guía de resolución y comprobación

**Puntos a conseguir:** dejar el sistema en el estado solicitado, poder explicar qué protocolo interviene, comprobarlo desde un cliente y aportar evidencias reproducibles.

1. **Preparar** el entorno y registrar el estado inicial.
2. **Construir** solo el siguiente elemento necesario.
3. **Validar** sintaxis y servicio.
4. **Probar** desde el cliente.
5. **Observar** puertos, logs y tráfico cuando proceda.
6. **Documentar** configuración, comandos y capturas.


#### Solución de referencia

La solución debe dejar un estado reproducible: topología o configuración documentada, comandos ejecutados, resultado esperado y resultado observado. Si el ejercicio pide una incidencia, documenta además **causa → evidencia → corrección → prueba de recuperación**.


### 📸 Evidencias y capturas

Incluye, cuando aporte información, una captura de la topología, del fichero o interfaz configurada, del estado del servicio y de la prueba final. Cada captura debe llevar una frase que explique **qué demuestra**; una imagen sin interpretación no constituye una evidencia técnica suficiente.

### 🧪 Rúbrica de evaluación

| Criterio | Puntos |
|---|---:|
| Comprensión del servicio/protocolo | 2 |
| Configuración y proceso | 2 |
| Funcionamiento demostrado | 2 |
| Diagnóstico y razonamiento | 2 |
| Documentación y evidencias | 1 |
| Seguridad y buenas prácticas | 1 |
| **Total** | **10** |


La documentación debe contener:

```text
1. Arquitectura
2. Direccionamiento
3. DNS
4. Instalación
5. Configuración
6. Pruebas
7. Capturas
8. Logs
9. Seguridad
10. Diagnóstico
11. Conclusiones
```

Cada prueba debe seguir:

```text
OBJETIVO
   ↓
CONFIGURACIÓN
   ↓
COMANDO
   ↓
RESULTADO
   ↓
EVIDENCIA
   ↓
CONCLUSIÓN
```

---

# 📚 100. Resumen

```text
                       MULTIMEDIA
                           │
           ┌───────────────┼────────────────┐
           │               │                │
         AUDIO            VÍDEO          TIEMPO REAL
           │               │                │
        códecs          códecs            RTP
           │               │                │
       Icecast        RTMP/HLS           SIP
           │               │                │
           └───────────────┼────────────────┘
                           │
                         CLIENTE
                           │
                          VLC
```

Ideas fundamentales:

1. El audio y el vídeo digitales son datos.
2. El muestreo convierte una señal continua en muestras discretas.
3. La profundidad de bits determina niveles de cuantificación.
4. El bitrate determina cantidad de datos por unidad de tiempo.
5. Un códec codifica/decodifica contenido.
6. Un contenedor agrupa flujos y metadatos.
7. MP4 no es un códec.
8. H.264 no es un contenedor.
9. Streaming permite reproducir mientras se reciben datos.
10. El búfer ayuda a absorber variaciones de red.
11. VOD y live tienen necesidades diferentes.
12. Icecast es especialmente adecuado para radio/streaming de audio.
13. Un mountpoint identifica un stream en Icecast.
14. FFmpeg permite inspeccionar, convertir y generar streams.
15. RTMP y HLS cumplen funciones diferentes.
16. RTMP puede utilizarse como entrada de un servidor multimedia.
17. HLS utiliza playlists y segmentos sobre HTTP.
18. VLC puede utilizarse como cliente multimedia.
19. SIP se utiliza para señalización VoIP.
20. RTP transporta medios en tiempo real.
21. Jitter es variación del tiempo de llegada.
22. Videoconferencia combina señalización y medios.
23. WebRTC está orientado a comunicación multimedia interactiva.
24. El ancho de banda debe dimensionarse según bitrate y número de clientes.
25. Los problemas multimedia deben diagnosticarse con evidencia.

---

# ❓ 101. Autoevaluación

1. ¿Qué es el muestreo de una señal de audio?
2. ¿Qué representa la profundidad de bits?
3. ¿Qué es un códec?
4. ¿Qué es un contenedor?
5. ¿Es MP4 un códec?
6. ¿Es H.264 un contenedor?
7. ¿Qué diferencia existe entre MP3 y WAV/PCM?
8. ¿Qué significa bitrate?
9. ¿Qué significa FPS?
10. ¿Qué es la resolución de un vídeo?
11. ¿Qué es streaming?
12. ¿Qué función realiza el búfer?
13. ¿Qué diferencia existe entre VOD y live?
14. ¿Qué componentes forman un sistema de streaming?
15. ¿Qué es Icecast?
16. ¿Qué es un mountpoint?
17. ¿Para qué sirve FFmpeg?
18. ¿Qué es RTMP?
19. ¿Qué es HLS?
20. ¿Qué diferencia existe entre RTMP y HLS?
21. ¿Qué es un podcast?
22. ¿Qué es VoIP?
23. ¿Qué función tiene SIP?
24. ¿Qué función tiene RTP?
25. ¿Qué es jitter?
26. ¿Qué problemas puede provocar una red con pérdidas?
27. ¿Qué comando permite inspeccionar un vídeo con FFmpeg?
28. ¿Qué comando permite comprobar si TCP/1935 está accesible?
29. ¿Qué herramienta permite reproducir un stream desde una URL?
30. ¿Por qué no debemos guardar una stream key en GitHub?

---

# ✅ 102. Respuestas de la autoevaluación

### 1.
El muestreo consiste en medir la amplitud de una señal a intervalos regulares.

### 2.
Indica cuántos bits se utilizan para representar cada muestra y, por tanto,
cuántos niveles de amplitud pueden representarse.

### 3.
Un códec es un mecanismo para codificar y decodificar audio o vídeo.

### 4.
Un contenedor organiza uno o varios flujos multimedia y metadatos.

### 5.
No. MP4 es un formato contenedor.

### 6.
No. H.264 es un códec de vídeo.

### 7.
WAV puede contener audio PCM sin compresión; MP3 utiliza compresión con
pérdida.

### 8.
Cantidad de bits transmitidos o utilizados por unidad de tiempo, normalmente
bit/s.

### 9.
Frames Per Second: número de imágenes de vídeo mostradas por segundo.

### 10.
Normalmente, el número de píxeles de ancho y alto del vídeo.

### 11.
Técnica de distribución que permite reproducir contenido mientras se recibe.

### 12.
Almacena temporalmente datos para compensar variaciones en la llegada de
datos.

### 13.
VOD distribuye contenido almacenado bajo demanda; live distribuye contenido
generado en directo.

### 14.
Fuente, codificador, servidor, red y cliente/reproductor, además de los
componentes auxiliares que requiera la arquitectura.

### 15.
Un servidor de streaming utilizado especialmente para distribución de audio.

### 16.
Un identificador de un stream dentro de Icecast.

### 17.
Permite inspeccionar, convertir, codificar, decodificar y procesar contenido
multimedia, además de participar en flujos de streaming.

### 18.
Un protocolo utilizado para streaming y especialmente habitual como mecanismo
de ingest hacia servidores multimedia.

### 19.
HTTP Live Streaming: mecanismo de distribución multimedia mediante playlists y
segmentos sobre HTTP.

### 20.
RTMP y HLS son tecnologías diferentes: RTMP se utiliza frecuentemente para
ingest/directo, mientras HLS distribuye mediante HTTP y segmentos.

### 21.
Sistema de distribución y suscripción de episodios multimedia mediante feeds.

### 22.
Voice over IP: transmisión de comunicaciones de voz sobre redes IP.

### 23.
SIP realiza señalización y establecimiento/control de sesiones multimedia.

### 24.
RTP transporta datos multimedia en tiempo real.

### 25.
Variación en el tiempo de llegada de los paquetes.

### 26.
Pérdidas pueden producir cortes, degradación, artefactos, pérdida de
sincronización o interrupciones.

### 27.
Por ejemplo:

```bash
ffprobe video.mp4
```

### 28.
Por ejemplo:

```bash
nc -vz servidor 1935
```

### 29.
VLC, mediante la opción de abrir un flujo de red.

### 30.
Porque una stream key es una credencial que permite publicar contenido en el
servidor. Si se expone, otra persona podría utilizarla.

---

# 📝 103. Test de repaso

### 1. ¿Qué es H.264?

a) Contenedor  
b) Códec de vídeo  
c) Protocolo DNS  
d) Servidor multimedia

### 2. ¿Qué es MP4?

a) Códec  
b) Contenedor  
c) Protocolo  
d) Servidor

### 3. ¿Qué herramienta utilizamos para inspeccionar streams multimedia?

a) dig  
b) ffprobe  
c) ssh  
d) nslookup

### 4. ¿Qué software utilizamos como servidor de audio?

a) Apache  
b) Icecast  
c) Dovecot  
d) BIND9

### 5. ¿Qué identifica un mountpoint de Icecast?

a) Una interfaz de red  
b) Un stream  
c) Un DNS  
d) Una ruta IP

### 6. ¿Qué protocolo se utiliza habitualmente para ingest hacia Nginx RTMP?

a) FTP  
b) RTMP  
c) SMTP  
d) IMAP

### 7. ¿Qué utiliza HLS?

a) FTP + ZIP  
b) HTTP + playlist/segmentos  
c) SMTP + MIME  
d) SSH + SFTP

### 8. ¿Qué herramienta puede reproducir una URL multimedia?

a) VLC  
b) dig  
c) ss  
d) tcpdump

### 9. ¿Qué protocolo se asocia principalmente con señalización VoIP?

a) RTP  
b) SIP  
c) HLS  
d) RTMP

### 10. ¿Qué protocolo transporta habitualmente los medios en VoIP?

a) RTP  
b) SIP  
c) DNS  
d) HTTP

### 11. ¿Qué es jitter?

a) Pérdida de resolución  
b) Variación del tiempo de llegada  
c) Compresión de vídeo  
d) Un códec

### 12. ¿Qué componente ayuda a absorber variaciones de red?

a) DNS  
b) búfer  
c) MX  
d) switch

### 13. ¿Qué significa VOD?

a) Video Over DNS  
b) Video On Demand  
c) Voice On Data  
d) Video Open Distribution

### 14. ¿Qué tecnología es especialmente adecuada para radio por Internet?

a) Icecast  
b) Dovecot  
c) Postfix  
d) BIND9

### 15. ¿Qué componente no debe confundirse con un códec?

a) contenedor  
b) bit  
c) FPS  
d) bitrate

---

# ✅ 104. Respuestas del test

| Nº | Respuesta |
|---:|:---:|
| 1 | **b** |
| 2 | **b** |
| 3 | **b** |
| 4 | **b** |
| 5 | **b** |
| 6 | **b** |
| 7 | **b** |
| 8 | **a** |
| 9 | **b** |
| 10 | **a** |
| 11 | **b** |
| 12 | **b** |
| 13 | **b** |
| 14 | **a** |
| 15 | **a** |

---


# 🧪 106. Secuencia recomendada de laboratorio
### 🧭 Guía de resolución y comprobación

**Puntos a conseguir:** dejar el sistema en el estado solicitado, poder explicar qué protocolo interviene, comprobarlo desde un cliente y aportar evidencias reproducibles.

1. **Preparar** el entorno y registrar el estado inicial.
2. **Construir** solo el siguiente elemento necesario.
3. **Validar** sintaxis y servicio.
4. **Probar** desde el cliente.
5. **Observar** puertos, logs y tráfico cuando proceda.
6. **Documentar** configuración, comandos y capturas.


#### Solución de referencia

La solución debe dejar un estado reproducible: topología o configuración documentada, comandos ejecutados, resultado esperado y resultado observado. Si el ejercicio pide una incidencia, documenta además **causa → evidencia → corrección → prueba de recuperación**.


### 📸 Evidencias y capturas

Incluye, cuando aporte información, una captura de la topología, del fichero o interfaz configurada, del estado del servicio y de la prueba final. Cada captura debe llevar una frase que explique **qué demuestra**; una imagen sin interpretación no constituye una evidencia técnica suficiente.

### 🧪 Rúbrica de evaluación

| Criterio | Puntos |
|---|---:|
| Comprensión del servicio/protocolo | 2 |
| Configuración y proceso | 2 |
| Funcionamiento demostrado | 2 |
| Diagnóstico y razonamiento | 2 |
| Documentación y evidencias | 1 |
| Seguridad y buenas prácticas | 1 |
| **Total** | **10** |


```text
UT3 · DNS
   │
   ▼
media.asir.test
   │
   ├──────────────────────┐
   ▼                      ▼
🎧 AUDIO                 📺 VÍDEO
   │                      │
   ▼                      ▼
FFmpeg                  FFmpeg
   │                      │
   ▼                      ▼
Icecast                  RTMP
   │                      │
   ▼                      ▼
VLC                     Nginx
                          │
                          ▼
                         HLS
                          │
                          ▼
                       VLC/Web
```

Después:

```text
                 MULTIMEDIA
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
      Podcast       VoIP    Videoconferencia
        │            │            │
       RSS          SIP          WebRTC
                     │
                    RTP
```

---

# 🏁 107. Resultado esperado

Al finalizar esta UT, el alumno debería ser capaz de enfrentarse a:

> **«Tengo un servidor Ubuntu, un fichero multimedia y varios clientes. Debo
> decidir qué códec y contenedor utilizar, publicar el contenido mediante el
> servicio adecuado, permitir que los clientes lo reproduzcan y diagnosticar
> cualquier fallo de red, servidor o formato.»**

El procedimiento profesional:

```text
REQUISITOS
    ↓
FORMATO
    ↓
CÓDEC
    ↓
BITRATE
    ↓
SERVIDOR
    ↓
PROTOCOLO
    ↓
DNS
    ↓
TCP/UDP
    ↓
CLIENTE
    ↓
BÚFER
    ↓
DECODIFICACIÓN
    ↓
REPRODUCCIÓN
    ↓
MONITORIZACIÓN
    ↓
DIAGNÓSTICO
```

---

