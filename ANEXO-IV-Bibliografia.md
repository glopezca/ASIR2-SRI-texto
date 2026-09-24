# 📚 ANEXO IV · Bibliografía y documentación técnica abierta

> 🧭 **ANTES DE EMPEZAR · VOCABULARIO TÉCNICO**
>
> Las siglas, abreviaturas y conceptos técnicos que van a aparecer en esta unidad se presentan aquí antes de su desarrollo. La explicación local de cada tema podrá ampliar estas definiciones cuando sea necesario.
>
> **CFGS** — Ciclo Formativo de Grado Superior.
> **ASIR** — Administración de Sistemas Informáticos en Red.
> **HTTP** — Protocolo de transferencia de hipertexto utilizado principalmente por la Web.
> **TCP** — Protocolo de transporte orientado a conexión que proporciona entrega fiable y ordenada.
> **TCP/IP** — Familia de protocolos de Internet en la que IP proporciona direccionamiento y TCP es uno de los protocolos de transporte.
> **IP** — Protocolo de Internet, responsable del direccionamiento y encaminamiento de paquetes.
> **RFC** — Request for Comments: documento técnico que especifica o describe protocolos, estándares o prácticas de Internet.
> **IETF** — Internet Engineering Task Force, comunidad que desarrolla estándares de Internet.
> **IPv6** — Versión 6 del Protocolo de Internet, con direcciones de 128 bits.
> **UDP** — Protocolo de transporte sin conexión, ligero y sin garantía de entrega.
> **DHCP** — Protocolo de configuración dinámica de host: entrega automáticamente parámetros de red a los clientes.
> **ISC** — Internet Systems Consortium, organización que desarrolla software de infraestructura de Internet como BIND y Kea.
> **DNS** — Sistema de nombres de dominio: servicio distribuido que relaciona nombres con direcciones IP y otros datos.
> **BIND** — Berkeley Internet Name Domain, implementación de servidor DNS.
> **IANA** — Internet Assigned Numbers Authority, organismo que coordina parámetros, espacios de nombres y números de Internet.
> **DNSSEC** — Extensiones de seguridad de DNS que permiten validar criptográficamente respuestas y datos DNS.
> **FTP** — Protocolo de transferencia de archivos que separa un canal de control de los canales de datos.
> **FTP/TLS** — FTP protegido mediante TLS, normalmente denominado FTPS.
> **TLS** — Protocolo criptográfico que proporciona confidencialidad, integridad y autenticación mediante certificados.
> **TFTP** — Protocolo muy sencillo de transferencia de archivos basado en UDP.
> **SMTP** — Simple Mail Transfer Protocol, protocolo principal para transportar correo entre agentes de correo.
> **MIME** — Multipurpose Internet Mail Extensions, mecanismo para describir tipos de contenido y adjuntos en mensajes.
> **XMPP** — Extensible Messaging and Presence Protocol, protocolo abierto para mensajería y presencia.
> **NNTP** — Network News Transfer Protocol, protocolo para intercambio y consulta de artículos de grupos de noticias.
> **FFmpeg** — Conjunto de herramientas para procesar, convertir, capturar y transmitir audio y vídeo.
> **HLS** — HTTP Live Streaming, sistema de distribución de audio y vídeo segmentado mediante HTTP.
> **RTP** — Real-time Transport Protocol, protocolo para transportar medios en tiempo real.
> **Docker** — Plataforma de contenerización para construir, distribuir y ejecutar aplicaciones aisladas en contenedores.
> **CLI** — Interfaz de línea de comandos, es decir, administración mediante órdenes escritas.
> **WSL** — Windows Subsystem for Linux, plataforma de Windows para ejecutar entornos Linux.
> **WSL2** — Windows Subsystem for Linux 2: tecnología de Windows que ejecuta un entorno Linux mediante una máquina virtual ligera.
> **Kubernetes** — Plataforma de orquestación de contenedores que automatiza despliegue, escalado y operación.
> **Git** — Sistema distribuido de control de versiones.
> **GitHub** — Servicio de alojamiento y colaboración basado en repositorios Git.
> **Codespaces** — Entornos de desarrollo alojados en GitHub que proporcionan un espacio de trabajo remoto.
> **VS Code** — Visual Studio Code, editor de código extensible con terminal y herramientas de desarrollo.
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

La documentación oficial del proyecto es la referencia primaria. Las fuentes se agrupan por función didáctica y tecnológica.

## 1. 🧭 Normativa y currículo

- Ley Orgánica 3/2022: https://www.boe.es/buscar/act.php?id=BOE-A-2022-5089
- Real Decreto 659/2023: https://www.boe.es/buscar/act.php?id=BOE-A-2023-16889
- Real Decreto 1629/2009: https://www.boe.es/buscar/doc.php?id=BOE-A-2009-18355
- Real Decreto 500/2024: https://www.boe.es/buscar/doc.php?id=BOE-A-2024-10685
- Orden EFD/659/2024: https://www.boe.es/eli/es/o/2024/06/25/efd659
- Portal de ASIR de Castilla y León: https://www.educa.jcyl.es/fp/es/catalogo-titulos-fp-castilla-leon/catalogo-titulos-grado-superior/administracion-sistemas-informaticos-red

## 2. 🌐 TCP/IP y RFC

- IETF RFC Editor: https://www.rfc-editor.org/
- RFC 791 IP: https://www.rfc-editor.org/rfc/rfc791
- RFC 8200 IPv6: https://www.rfc-editor.org/rfc/rfc8200
- RFC 9293 TCP: https://www.rfc-editor.org/rfc/rfc9293
- RFC 768 UDP: https://www.rfc-editor.org/rfc/rfc768
- RFC 1918 direccionamiento privado: https://www.rfc-editor.org/rfc/rfc1918

## 3. 📡 DHCP

- Kea: https://kea.readthedocs.io/
- ISC: https://www.isc.org/kea/
- Ubuntu Server networking: https://documentation.ubuntu.com/server/how-to/networking/
- RFC 2131: https://www.rfc-editor.org/rfc/rfc2131
- RFC 8415: https://www.rfc-editor.org/rfc/rfc8415

## 4. 🌐 DNS

- BIND 9: https://bind9.readthedocs.io/
- ISC BIND: https://www.isc.org/bind/
- IANA: https://www.iana.org/domains
- RFC 1034: https://www.rfc-editor.org/rfc/rfc1034
- RFC 1035: https://www.rfc-editor.org/rfc/rfc1035
- RFC 4033 DNSSEC: https://www.rfc-editor.org/rfc/rfc4033

## 5. 📂 Transferencia

- vsftpd: https://security.appspot.com/vsftpd.html
- OpenSSH: https://www.openssh.com/
- OpenSSH manuals: https://www.openssh.com/manual.html
- RFC 959 FTP: https://www.rfc-editor.org/rfc/rfc959
- RFC 4217 FTP/TLS: https://www.rfc-editor.org/rfc/rfc4217
- RFC 1350 TFTP: https://www.rfc-editor.org/rfc/rfc1350

## 6. 🌍 Web

- HTTP Semantics: https://www.rfc-editor.org/rfc/rfc9110
- HTTP/1.1: https://www.rfc-editor.org/rfc/rfc9112
- HTTP/2: https://www.rfc-editor.org/rfc/rfc9113
- HTTP/3: https://www.rfc-editor.org/rfc/rfc9114
- MDN HTTP: https://developer.mozilla.org/docs/Web/HTTP
- Apache: https://httpd.apache.org/docs/
- Nginx: https://nginx.org/en/docs/
- OpenSSL: https://docs.openssl.org/
- Let's Encrypt: https://letsencrypt.org/docs/

## 7. ✉️ Correo

- Postfix: https://www.postfix.org/documentation.html
- Dovecot: https://doc.dovecot.org/
- RFC 5321 SMTP: https://www.rfc-editor.org/rfc/rfc5321
- RFC 5322: https://www.rfc-editor.org/rfc/rfc5322
- RFC 6409: https://www.rfc-editor.org/rfc/rfc6409
- RFC 8314: https://www.rfc-editor.org/rfc/rfc8314
- RFC 2045 MIME: https://www.rfc-editor.org/rfc/rfc2045

## 8. 💬 Mensajería

- Prosody: https://prosody.im/doc/
- XMPP Standards Foundation: https://xmpp.org/
- RFC 6120 XMPP: https://www.rfc-editor.org/rfc/rfc6120
- NNTP RFC 3977: https://www.rfc-editor.org/rfc/rfc3977
- Mailman 3: https://docs.mailman3.org/

## 9. 🎧 Multimedia

- FFmpeg: https://ffmpeg.org/documentation.html
- Icecast: https://icecast.org/docs/
- HLS RFC 8216: https://www.rfc-editor.org/rfc/rfc8216
- RTP RFC 3550: https://www.rfc-editor.org/rfc/rfc3550
- WebRTC: https://www.w3.org/TR/webrtc/

## 10. 🐳 Docker

- Docker Docs: https://docs.docker.com/
- CLI: https://docs.docker.com/reference/cli/docker/
- Dockerfile: https://docs.docker.com/reference/dockerfile/
- Compose: https://docs.docker.com/compose/
- Compose Specification: https://docs.docker.com/reference/compose-file/
- Networking: https://docs.docker.com/engine/network/
- Volumes: https://docs.docker.com/engine/storage/volumes/
- Docker Desktop: https://docs.docker.com/desktop/
- Docker + WSL2: https://docs.docker.com/desktop/features/wsl/

## 11. ☸️ Kubernetes

- Documentation: https://kubernetes.io/docs/
- Concepts: https://kubernetes.io/docs/concepts/
- Pods: https://kubernetes.io/docs/concepts/workloads/pods/
- Deployments: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
- Services: https://kubernetes.io/docs/concepts/services-networking/service/
- kubectl: https://kubernetes.io/docs/reference/kubectl/
- exec: https://kubernetes.io/docs/reference/kubectl/generated/kubectl_exec/
- port-forward: https://kubernetes.io/docs/reference/kubectl/generated/kubectl_port-forward/

## 12. 🐙 Git y GitHub

- Git: https://git-scm.com/doc
- GitHub Docs: https://docs.github.com/
- Git + GitHub: https://docs.github.com/en/get-started/using-git
- GitHub CLI: https://cli.github.com/manual/
- Codespaces: https://docs.github.com/en/codespaces
- Codespaces + VS Code: https://docs.github.com/en/codespaces/developing-in-a-codespace/using-github-codespaces-in-visual-studio-code

## 13. 🖥️ Linux y virtualización

- Ubuntu Server: https://documentation.ubuntu.com/server/
- Ubuntu packages: https://packages.ubuntu.com/
- systemd: https://systemd.io/
- VirtualBox: https://www.virtualbox.org/wiki/Documentation
- WSL: https://learn.microsoft.com/windows/wsl/
- VS Code: https://code.visualstudio.com/docs

## 14. 🧪 Redes y simulación

- Cisco Packet Tracer: https://www.netacad.com/courses/packet-tracer
- Wireshark: https://www.wireshark.org/docs/
- tcpdump: https://www.tcpdump.org/manpages/tcpdump.1.html

## 🖥️ Interfaces web de administración y correo

### Webmin

- Webmin — introducción: https://webmin.com/docs/intro/
- Instalación y acceso: https://webmin.com/download/
- Configuración de red: https://webmin.com/docs/modules/network-configuration/
- Webmin CLI: https://webmin.com/docs/reference/webmin-command-line/

### Roundcube

- Sitio oficial: https://roundcube.net/
- Capturas oficiales de la interfaz: https://roundcube.net/screens/
- Documentación y proyecto: https://roundcube.net/about/

### Sympa

- Sitio oficial: https://www.sympa.community/
- Manual: https://www.sympa.community/manual/
- Interfaz web para listmasters: https://www.sympa.community/manual/admin/web-interface.html
- Configuración de la interfaz web: https://www.sympa.community/gpldoc/man/sympa_config.5.html
- Integración con servidor HTTP: https://www.sympa.community/manual/install/configure-http-server.html

## 15. 📌 Criterio de actualización

Cuando una herramienta cambia, la documentación oficial tiene prioridad sobre tutoriales antiguos. En las prácticas se deben fijar versiones cuando la reproducibilidad sea relevante.
