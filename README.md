# 🌐 Servicios de Red e Internet · ASIR

> 🧭 **ANTES DE EMPEZAR · VOCABULARIO TÉCNICO**
>
> Las siglas, abreviaturas y conceptos técnicos que van a aparecer en esta unidad se presentan aquí antes de su desarrollo. La explicación local de cada tema podrá ampliar estas definiciones cuando sea necesario.
>
> **UT** — Unidad de Trabajo: unidad didáctica del módulo profesional.
> **RA** — Resultado de Aprendizaje: capacidad que el alumnado debe demostrar al finalizar un bloque curricular.
> **CFGS** — Ciclo Formativo de Grado Superior.
> **ASIR** — Administración de Sistemas Informáticos en Red.
> **SRI** — Servicios de Red e Internet.
> **Docker** — Plataforma de contenerización para construir, distribuir y ejecutar aplicaciones aisladas en contenedores.
> **Git** — Sistema distribuido de control de versiones.
> **GitHub** — Servicio de alojamiento y colaboración basado en repositorios Git.
> **Codespaces** — Entornos de desarrollo alojados en GitHub que proporcionan un espacio de trabajo remoto.
> **URI** — Identificador uniforme de recursos: sintaxis general para identificar un recurso.
> **IP** — Protocolo de Internet, responsable del direccionamiento y encaminamiento de paquetes.
> **TCP** — Protocolo de transporte orientado a conexión que proporciona entrega fiable y ordenada.
> **TCP/IP** — Familia de protocolos de Internet en la que IP proporciona direccionamiento y TCP es uno de los protocolos de transporte.
> **IPv6** — Versión 6 del Protocolo de Internet, con direcciones de 128 bits.
> **CIDR** — Enrutamiento entre dominios sin clases: notación que expresa una red mediante dirección y longitud de prefijo, por ejemplo /24.
> **UDP** — Protocolo de transporte sin conexión, ligero y sin garantía de entrega.
> **NAT** — Traducción de direcciones de red: modificación de direcciones IP al atravesar un dispositivo intermedio.
> **NAT/PAT** — Combinación de NAT y PAT, habitual cuando varias direcciones privadas comparten una dirección pública.
> **PAT** — Traducción de direcciones mediante puertos: permite multiplexar conexiones privadas sobre una dirección pública.
> **DHCP** — Protocolo de configuración dinámica de host: entrega automáticamente parámetros de red a los clientes.
> **DORA** — Secuencia Discover, Offer, Request y Acknowledgement usada habitualmente para obtener una concesión IPv4 mediante DHCP.
> **DNS** — Sistema de nombres de dominio: servicio distribuido que relaciona nombres con direcciones IP y otros datos.
> **BIND** — Berkeley Internet Name Domain, implementación de servidor DNS.
> **BIND9** — Rama 9 de BIND, implementación de servidor DNS usada habitualmente en Linux.
> **FTP** — Protocolo de transferencia de archivos que separa un canal de control de los canales de datos.
> **FTPS** — FTP protegido mediante TLS.
> **TFTP** — Protocolo muy sencillo de transferencia de archivos basado en UDP.
> **SFTP** — Protocolo de transferencia de archivos que funciona como subsistema de SSH; no es FTP cifrado.
> **SCP** — Secure Copy: copia de archivos sobre SSH.
> **HTTP** — Protocolo de transferencia de hipertexto utilizado principalmente por la Web.
> **WWW** — World Wide Web, sistema de recursos enlazados accesibles principalmente mediante HTTP.
> **URI/URL** — URI identifica un recurso; URL es un URI que además proporciona una forma de localizarlo.
> **URL** — Localizador uniforme de recursos: URI que además proporciona su ubicación mediante un esquema.
> **MIME** — Multipurpose Internet Mail Extensions, mecanismo para describir tipos de contenido y adjuntos en mensajes.
> **HTTPS** — HTTP protegido mediante TLS.
> **TLS** — Protocolo criptográfico que proporciona confidencialidad, integridad y autenticación mediante certificados.
> **MUA** — Mail User Agent, programa con el que el usuario compone, envía y lee correo.
> **MTA** — Mail Transfer Agent, componente que transporta correo entre servidores.
> **SMTP** — Simple Mail Transfer Protocol, protocolo principal para transportar correo entre agentes de correo.
> **ESMTP** — Extended SMTP, conjunto de extensiones que amplían SMTP.
> **IMAP** — Internet Message Access Protocol, protocolo para acceder y gestionar mensajes que permanecen en el servidor.
> **POP3** — Post Office Protocol version 3, protocolo para recuperar mensajes del buzón.
> **XMPP** — Extensible Messaging and Presence Protocol, protocolo abierto para mensajería y presencia.
> **IRC** — Internet Relay Chat, protocolo de conversación textual en tiempo real mediante canales.
> **NNTP** — Network News Transfer Protocol, protocolo para intercambio y consulta de artículos de grupos de noticias.
> **VOD** — Video on Demand, vídeo reproducido bajo demanda.
> **FFmpeg** — Conjunto de herramientas para procesar, convertir, capturar y transmitir audio y vídeo.
> **RTMP** — Real-Time Messaging Protocol, protocolo usado en determinados flujos de ingestión de audio y vídeo en directo.
> **HLS** — HTTP Live Streaming, sistema de distribución de audio y vídeo segmentado mediante HTTP.
> **WSL2** — Windows Subsystem for Linux 2: tecnología de Windows que ejecuta un entorno Linux mediante una máquina virtual ligera.
> **Docker Compose** — Herramienta de Docker para definir y ejecutar aplicaciones multicontenedor mediante un archivo declarativo.
> **VLAN** — Red de área local virtual que permite separar lógicamente redes sobre infraestructura compartida.
> **YAML** — Formato de representación de datos estructurados, muy usado en configuración.
> **YAML/JSON** — YAML y JSON son formatos de representación de datos estructurados usados frecuentemente en configuración.
> **JSON** — Formato textual para representar datos estructurados mediante objetos y listas.
> **Kubernetes** — Plataforma de orquestación de contenedores que automatiza despliegue, escalado y operación.
> **VS Code** — Visual Studio Code, editor de código extensible con terminal y herramientas de desarrollo.
> **RFC** — Request for Comments: documento técnico que especifica o describe protocolos, estándares o prácticas de Internet.
> **VM** — Máquina virtual: ordenador software aislado que ejecuta un sistema operativo invitado.
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

## Material docente integral · `ASIR2-SRI-texto` · 

Material autónomo de estudio, laboratorio y evaluación para el módulo profesional **0375 · Servicios de red e Internet** del **CFGS Técnico Superior en Administración de Sistemas Informáticos en Red (ASIR)**.

La versión  supone un cambio de alcance: el repositorio deja de ser una colección de apuntes complementarios y se plantea como **material docente integral**, con fundamentos, administración de servicios, prácticas, diagnóstico, autoevaluación, resultados de aprendizaje, Docker, GitHub, Codespaces, bibliografía y materiales para el profesor.

---

# 🎯 1. Propósito

El objetivo es formar al alumnado para que pueda enfrentarse a un servicio de red como un técnico superior:

```text
NECESIDAD
   ↓
REQUISITOS
   ↓
ARQUITECTURA
   ↓
PROTOCOLO
   ↓
IMPLEMENTACIÓN
   ↓
CONFIGURACIÓN
   ↓
SEGURIDAD
   ↓
PRUEBAS
   ↓
MONITORIZACIÓN
   ↓
DIAGNÓSTICO
   ↓
DOCUMENTACIÓN
```

No se pretende que el alumnado memorice comandos. Se pretende que comprenda **qué servicio está desplegando, qué protocolos intervienen, qué puertos utiliza, cómo se comunica, cómo se protege y cómo se demuestra que funciona**.

---

# 🧭 2. Entorno curricular

El material está contextualizado en el módulo **0375 · Servicios de red e Internet** del ciclo de ASIR.

La regulación actual del título se articula sobre el Real Decreto 1629/2009, modificado por el Real Decreto 500/2024, y la nueva ordenación de Formación Profesional del Real Decreto 659/2023. En Castilla y León, la ficha oficial del título recoge además el **Decreto 24/2024** y la **Orden EDU/1287/2024** como referencias curriculares autonómicas.

El currículo de Castilla y León asigna actualmente **198 horas** al módulo 0375 en segundo curso. La distribución concreta de UT, instrumentos de evaluación y prácticas corresponde a la programación didáctica del centro.

## Resultados de aprendizaje

| RA | Resultado de aprendizaje | UT principal |
|---|---|---|
| **RA1** | Administra servicios de resolución de nombres, analizándolos y garantizando la seguridad del servicio. | **UT3** |
| **RA2** | Administra servicios de configuración automática, identificándolos y verificando la correcta asignación de los parámetros. | **UT2** |
| **RA3** | Administra servidores Web aplicando criterios de configuración y asegurando el funcionamiento del servicio. | **UT5** |
| **RA4** | Administra servicios de transferencia de archivos asegurando y limitando el acceso a la información. | **UT4** |
| **RA5** | Administra servidores de correo electrónico, aplicando criterios de configuración y garantizando la seguridad del servicio. | **UT6** |
| **RA6** | Administra servicios de mensajería instantánea, noticias y listas de distribución, verificando y asegurando el acceso de los usuarios. | **UT7** |
| **RA7** | Administra servicios de audio identificando las necesidades de distribución y adaptando los formatos. | **UT8 · audio** |
| **RA8** | Administra servicios de vídeo identificando las necesidades de distribución y adaptando los formatos. | **UT8 · vídeo** |

**UT1** constituye la base transversal de TCP/IP necesaria para interpretar todos los resultados posteriores.

---

# 📚 3. Unidades de trabajo

## [🌐 UT1 · Conceptos básicos de TCP/IP](UT1-Conceptos-basicos-TCP-IP.md)

Fundamentos de:

- arquitectura TCP/IP;
- IP e IPv6;
- subredes y CIDR;
- TCP y UDP;
- puertos;
- routing;
- NAT/PAT;
- virtualización;
- modelo cliente/servidor;
- diagnóstico de conectividad.

**Función:** prerrequisito transversal de las UT2–UT8.

## [📡 UT2 · Servicio DHCP](UT2-Servicio-DHCP.md)

**RA2.** Configuración automática de parámetros de red.

Incluye DORA, concesiones, reservas, opciones, relay, DHCPv6, Kea, alta disponibilidad y seguridad.

## [🌐 UT3 · Servicio DNS](UT3-Servicio-DNS.md)

**RA1.** Resolución de nombres.

Incluye arquitectura jerárquica, zonas, registros, resolución directa/inversa, BIND9, delegación, transferencias, DNS dinámico y seguridad.

## [📂 UT4 · Servicios de transferencia de ficheros](UT4-Servicios-transferencia-ficheros.md)

**RA4.** Transferencia de archivos.

Incluye FTP, FTPS, TFTP, SFTP, SCP, autenticación, permisos, modos activo/pasivo, NAT, firewall y diagnóstico.

## [🌍 UT5 · Servidores Web (HTTP)](UT5-Servidores-Web-HTTP.md)

**RA3.** Administración de servidores Web.

Incluye WWW, URI/URL, HTTP, MIME, Apache, Nginx, Virtual Hosts, proxy inverso, HTTPS, TLS, autenticación, logs y diagnóstico.

## [✉️ UT6 · Servicios de correo electrónico](UT6-Servicios-correo-electronico.md)

**RA5.** Administración de servidores de correo.

Incluye arquitectura MUA/MTA/MRA, SMTP/ESMTP, IMAP, POP3, MIME, Postfix, Dovecot, autenticación, TLS, spam, seguridad y diagnóstico.

## [💬 UT7 · Mensajería, noticias y listas de distribución](UT7-Servicios-mensajeria-noticias-listas-distribucion.md)

**RA6.** Mensajería instantánea, noticias y listas de distribución.

Incluye XMPP, presencia, clientes y servidores, IRC, listas de distribución, Mailman, NNTP, grupos de noticias y troubleshooting.

## [🎧📺 UT8 · Servicios de audio y vídeo](UT8-Servicios-audio-video.md)

**RA7 + RA8.** Audio y vídeo.

Incluye formatos, códecs, contenedores, bitrate, streaming, VOD, directo, FFmpeg, Icecast, RTMP, Nginx, HLS, podcast, VoIP y videoconferencia.

---

# 🧪 4. Laboratorio tecnológico

La guía utiliza **cuatro entornos de prácticas complementarios**. Los cuatro forman parte de un único laboratorio de SRI y aparecen relacionados desde el comienzo de la guía. Cada uno responde a una pregunta diferente y prepara el siguiente nivel de trabajo.

```text
                         🧪 LABORATORIO SRI
                                │
        ┌───────────────────────┼──────────────────────────────┐
        │                       │                              │
        ├── 🧪 ENTORNO I       ├── 🐧 ENTORNO II              ├── 🖥️ ENTORNO III
        │   Cisco Packet       │   WSL2 + Ubuntu              │   VirtualBox +
        │   Tracer             │   26.04                      │   Ubuntu 26.04 Server
        │                      │                              │
        └──────────────────────┴──────────────────────────────┴── 🐳 ENTORNO IV
                                                                   Docker Compose
                                                                   │
                                                                   ▼
                                                            🌐 SERVICIOS SRI
```

> 🧭 **Cómo leer el esquema**
>
> Los cuatro entornos no compiten entre sí. **Entorno I** permite visualizar el comportamiento de la red; **Entorno II** facilita la observación y el diagnóstico desde Linux; **Entorno III** reproduce la administración de servidores reales; **Entorno IV** convierte la infraestructura en código reproducible. Una misma actividad puede comenzar en I y terminar en IV, utilizando II y III cuando sean necesarios para comprender o validar el servicio.

### 🧪 Entorno I · Cisco Packet Tracer

Para topologías, routing, VLAN, DHCP, relay y experimentación de red. Es especialmente útil cuando queremos concentrarnos en el comportamiento de la red sin que la instalación de los servicios distraiga del concepto que estamos estudiando.

### 🐧 Entorno II · WSL2 + Ubuntu 26.04

Para herramientas Linux, clientes, scripts, análisis de tráfico y pruebas rápidas. Es nuestro **banco de trabajo**: ligero, inmediato y adecuado para repetir comandos muchas veces.

### 🖥️ Entorno III · VirtualBox + Ubuntu 26.04 Server

Para servidores completos y prácticas que requieren control de interfaces, servicios, `systemd`, firewall, DNS, DHCP, Web, correo y comportamiento de red independiente.

### 🐳 Entorno IV · Docker Compose

Para convertir una arquitectura de servicios en infraestructura reproducible. Permite trabajar con imágenes, contenedores, redes, puertos, volúmenes, DNS interno, dependencias y varios servicios coordinados mediante un único fichero `compose.yaml`.

### 📊 Los cuatro entornos, de un vistazo

| Entorno | Plataforma | Función principal | Pregunta didáctica |
|---|---|---|---|
| **I** | Cisco Packet Tracer | Simular topologías y protocolos | **¿Cómo se comporta la red?** |
| **II** | WSL2 + Ubuntu 26.04 | Ejecutar herramientas y clientes Linux | **¿Qué está ocurriendo realmente?** |
| **III** | VirtualBox + Ubuntu 26.04 Server | Administrar servidores completos | **¿Cómo se configura y mantiene?** |
| **IV** | Docker Compose | Reproducir infraestructura multicontenedor | **¿Cómo lo convierto en infraestructura reproducible?** |

---

# 🧪 5. Entornos de prácticas

Los cuatro entornos aparecen a lo largo de las UT. No es necesario utilizarlos todos en todas las actividades: se selecciona el entorno que mejor responde al objetivo didáctico de cada ejercicio.

| Entorno | Aplicación habitual |
|---|---|
| **I · Packet Tracer** | Redes, direccionamiento, routing, DHCP y servicios simulables |
| **II · WSL2** | Clientes, diagnóstico, `curl`, `dig`, `ss`, `tcpdump`, scripts y análisis |
| **III · VirtualBox** | Instalación y administración real de servidores |
| **IV · Docker Compose** | Despliegues reproducibles y arquitecturas multicontenedor |

## [🐳 Entorno IV · Docker Compose para UT1–UT8](ENTORNO-IV-Docker-Compose-UT1-UT8.md)

El cuarto entorno permite desplegar, de forma reproducible, las infraestructuras de las UT mediante contenedores y Docker Compose. **Complementa los otros tres entornos; no los sustituye.**

# 📚 6. Anexos

## [🧰 Anexo I · Visual Studio Code + WSL2](ANEXO-I-VSCode-WSL2.md)

Herramienta común de edición y administración:

- Explorador;
- editor;
- terminal WSL2;
- YAML/JSON/Markdown;
- validación de configuraciones;
- Git;
- diagnóstico.

## [🐳 Anexo II · Docker, Docker Compose y Kubernetes](ANEXO-II-Docker-WSL2.md)

Guía completa de:

- Docker Desktop;
- WSL2;
- imágenes y contenedores;
- shell;
- logs;
- redes;
- DNS;
- puertos;
- volúmenes;
- Dockerfile;
- Compose;
- Swarm;
- Kubernetes;
- Pods;
- Deployments;
- Services;
- `kubectl exec`;
- `port-forward`;
- troubleshooting.

## [🐙 Anexo III · Git, GitHub, Codespaces y VS Code](ANEXO-III-Git-GitHub-Codespaces.md)

Flujo completo desde Git local hasta GitHub y Codespaces.

## [📚 Anexo IV · Bibliografía y documentación abierta](ANEXO-IV-Bibliografia.md)

Bibliografía temática y enlaces a documentación oficial de:

- normativa;
- RFC;
- Ubuntu;
- BIND;
- Kea;
- OpenSSH;
- Apache;
- Nginx;
- Postfix;
- Dovecot;
- XMPP;
- Icecast;
- FFmpeg;
- Docker;
- Kubernetes;
- Git/GitHub;
- VS Code;
- WSL2;
- VirtualBox;
- Packet Tracer;
- Wireshark.

## [🛡️ Anexo V · Seguridad, observabilidad y pruebas](ANEXO-V-Seguridad-Observabilidad-Pruebas.md)

Método transversal para diseñar pruebas, observar servicios, introducir incidencias deliberadas y documentar la resolución.

---

# 👨‍🏫 6. Material para el profesor

## [Apéndice · Evaluación y prácticas](APENDICE-PROFESOR.md)

Incluye:

- 3 preguntas tipo test por UT;
- una sola respuesta correcta;
- distribución variable de las posiciones correctas;
- solucionario al final;
- prácticas evaluables de hasta 1 h 45 min;
- proyecto integrador;
- rúbrica común;
- lista de comprobación docente.

Las preguntas del apéndice son **reformulaciones y ampliaciones docentes**, no una reproducción literal de los bancos de preguntas del material de referencia.

---

# 🧭 7. Secuencia didáctica

```text
UT1 · TCP/IP
       │
       ▼
UT2 · DHCP ───────────────► RA2
       │
       ▼
UT3 · DNS ────────────────► RA1
       │
       ▼
UT4 · Transferencia ──────► RA4
       │
       ▼
UT5 · Web ────────────────► RA3
       │
       ▼
UT6 · Correo ─────────────► RA5
       │
       ▼
UT7 · Mensajería ─────────► RA6
       │
       ▼
UT8 · Audio/Vídeo ────────► RA7 + RA8
       │
       ▼
Anexos tecnológicos
       │
       ├── VS Code + WSL2
       ├── Docker + Compose + Kubernetes
       ├── Git + GitHub + Codespaces
       └── seguridad + observabilidad
```

---

# 🔬 8. Método común de todas las prácticas

Todas las prácticas deben seguir, en la medida de lo posible:

```text
1. Analizar requisitos
2. Diseñar la solución
3. Instalar
4. Configurar
5. Validar sintaxis
6. Arrancar
7. Comprobar puertos
8. Probar desde un cliente
9. Analizar logs
10. Diagnosticar fallos
11. Aplicar seguridad
12. Documentar
```

El alumno debe entregar **evidencias**, no sólo afirmar que una práctica funciona.

---

# ⚠️ 9. Estado de las pruebas técnicas

La  incluye revisión estática y coherencia de los ejemplos. Cuando una práctica depende de un daemon, una VM, Docker Desktop, una red virtual específica o GitHub Codespaces, la ejecución final debe realizarse en el entorno indicado.

En particular, el entorno de generación de este paquete **no dispone de Docker Engine ni de un Codespace ejecutable**, por lo que no se presenta como ejecutada una validación extremo a extremo que no haya sido posible realizar.

Esto es deliberado: en administración de sistemas, **una configuración que no se ha probado no debe presentarse como probada**.

---

# 📜 10. Normativa y fuentes curriculares

La versión  se ha actualizado tomando como referencia la normativa vigente y, para Castilla y León, la información oficial publicada para el título de ASIR.

- Portal oficial de FP de Castilla y León: https://www.educa.jcyl.es/fp/
- Ficha oficial de ASIR: https://www.educa.jcyl.es/fp/es/catalogo-titulos-fp-castilla-leon/catalogo-titulos-grado-superior/administracion-sistemas-informaticos-red
- Real Decreto 1629/2009: https://www.boe.es/buscar/doc.php?id=BOE-A-2009-18355
- Real Decreto 500/2024: https://www.boe.es/buscar/doc.php?id=BOE-A-2024-10685
- Real Decreto 659/2023: https://www.boe.es/buscar/act.php?id=BOE-A-2023-16889
- Orden EFD/659/2024: https://www.boe.es/eli/es/o/2024/06/25/efd659

---

# 🧑‍🎓 11. Cómo utilizar este material

### Primera pasada

Leer la UT y construir el modelo conceptual.

### Segunda pasada

Repetir las prácticas en el laboratorio.

### Tercera pasada

Introducir fallos deliberados y aplicar troubleshooting.

### Cuarta pasada

Recrear la infraestructura mediante Docker Compose cuando la UT lo permita.

### Quinta pasada

Versionar la solución con Git y trabajar desde GitHub/Codespaces.

### Sexta pasada

Resolver una práctica evaluable sin seguir paso a paso la receta.

El objetivo final es pasar de:

> «Sé ejecutar estos comandos»

A:

> **«Sé diseñar, desplegar, verificar, proteger, diagnosticar y documentar este servicio».**

---

# 🏁 12. Principio rector

```text
        ┌───────────────────────────────┐
        │       ADMINISTRAR SRI         │
        ├───────────────────────────────┤
        │ Comprender                    │
        │ Diseñar                       │
        │ Implementar                   │
        │ Verificar                     │
        │ Diagnosticar                  │
        │ Proteger                      │
        │ Documentar                    │
        └───────────────────────────────┘
```

**La herramienta cambia. El método profesional permanece.**
