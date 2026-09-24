# 📖 ANEXO VIII · Glosario técnico completo

> **Cómo utilizar este anexo**
>
> Este glosario reúne los términos técnicos, siglas, abreviaturas, protocolos, tecnologías y objetos de infraestructura utilizados en la guía. Está ordenado alfabéticamente. La explicación contextual de un término sigue apareciendo en la unidad donde se introduce; este anexo sirve como referencia acumulativa.

## S

| Término | Explicación |
|---|---|
| **`systemd`** | sistema de inicio y gestor de servicios habitual en Linux; `systemctl` permite consultar y administrar esos servicios. |
## A

| Término | Explicación |
|---|---|
| **AAAA** | Registro DNS que asocia un nombre con una dirección IPv6. |
| **AAC** | Advanced Audio Coding, códec de audio comprimido. |
| **ACK** | Acknowledgement: confirmación; en DHCP forma parte de DORA y en TCP se utiliza para confirmar recepción de segmentos. |
| **ACK (DHCPACK)** | Mensaje DHCP mediante el que el servidor confirma al cliente la concesión de los parámetros de red. |
| **ACL** | Lista de control de acceso que determina quién puede realizar una operación. |
| **ACME** | Automated Certificate Management Environment, protocolo para automatizar la obtención y renovación de certificados. |
| **ALG** | Application Layer Gateway: función que adapta o inspecciona protocolos de aplicación al atravesar un intermediario. |
| **ANY** | Tipo de consulta DNS que históricamente solicitaba información amplia sobre un nombre; su uso operativo está desaconsejado en muchos escenarios. |
| **Apache** | Servidor web HTTP de código abierto ampliamente utilizado. |
| **Apache HTTP Server** | Servidor web de código abierto del proyecto Apache. |
| **API** | Interfaz de programación de aplicaciones: conjunto de operaciones mediante las que un programa puede comunicarse con otro sistema. |
| **API Server** | Servidor de la API de Kubernetes: componente del plano de control que recibe y procesa solicitudes contra la API del clúster. |
| **Archivo de configuración** | fichero que contiene los parámetros con los que un servicio determina su comportamiento. |
| **ARP** | Address Resolution Protocol: protocolo que relaciona una dirección IPv4 con una dirección de enlace en una red local. |
| **ARP/NDP** | ARP resuelve direcciones IPv4 en una red local; NDP realiza funciones equivalentes de descubrimiento y resolución en IPv6. |
| **ASCII** | American Standard Code for Information Interchange, codificación histórica de caracteres. |
| **ASIR** | Administración de Sistemas Informáticos en Red. |
| **AUTH** | Mecanismo de autenticación utilizado por protocolos como SMTP para identificar al usuario. |
| **AV1** | Códec de vídeo moderno y abierto diseñado para alta eficiencia de compresión. |
| **AVIF** | Formato de imagen basado en el códec AV1. |
| **AXFR** | Transferencia completa de una zona DNS entre servidores. |
## B

| Término | Explicación |
|---|---|
| **BD** | Base de datos. |
| **BIND** | Berkeley Internet Name Domain, implementación de servidor DNS. |
| **Bind mount** | Montaje que hace visible en un contenedor una ruta concreta del sistema de archivos del host. |
| **BIND9** | Rama 9 de BIND, implementación de servidor DNS usada habitualmente en Linux. |
| **Bitrate** | Tasa de bits: cantidad de bits transmitidos o procesados por unidad de tiempo. |
| **Broadcast o difusión** | envío dirigido a todos los equipos de un dominio de difusión. |
## C

| Término | Explicación |
|---|---|
| **CA** | Autoridad de certificación que emite y firma certificados digitales. |
| **Caché** | almacenamiento temporal de resultados para poder reutilizarlos sin repetir inmediatamente una consulta o cálculo. |
| **CDN** | Content Delivery Network, red distribuida de servidores que acerca contenidos a los usuarios. |
| **Certificado digital** | credencial criptográfica que vincula una identidad con una clave pública y que puede estar firmada por una autoridad de certificación. |
| **CFGS** | Ciclo Formativo de Grado Superior. |
| **CIDR** | Enrutamiento entre dominios sin clases: notación que expresa una red mediante dirección y longitud de prefijo, por ejemplo /24. |
| **CLI** | Interfaz de línea de comandos, es decir, administración mediante órdenes escritas. |
| **Cliente** | programa o equipo que inicia una petición de un servicio. |
| **CNAME** | Registro DNS que define un alias de un nombre canónico. |
| **Codespace** | entorno de desarrollo remoto proporcionado por GitHub para trabajar con un repositorio. |
| **Commit** | instantánea registrada por Git que conserva un conjunto concreto de cambios. |
| **Compose project** | Conjunto de servicios, redes y volúmenes gestionados conjuntamente por Docker Compose. |
| **Concesión DHCP** | asignación temporal de una dirección IP y otros parámetros de red a un cliente. |
| **ConfigMap** | Objeto de Kubernetes destinado a almacenar datos de configuración no confidenciales que pueden consumir los Pods. |
| **Consulta iterativa** | consulta en la que el servidor responde con la mejor información que conoce, pudiendo remitir al consultante hacia otro servidor. |
| **Consulta recursiva** | consulta en la que el servidor consultado asume la tarea de obtener una respuesta completa para el cliente, si tiene habilitada la recursión. |
| **Container runtime** | Componente que ejecuta contenedores en un nodo de Kubernetes. |
| **Contenedor** | Instancia aislada de una imagen que comparte el núcleo del sistema anfitrión. |
| **Contenedor multimedia** | formato de archivo que agrupa una o varias pistas de audio, vídeo, subtítulos o metadatos. |
| **Controller** | Componente de Kubernetes que observa el estado del clúster y actúa para acercarlo al estado deseado. |
| **CPU** | Central Processing Unit: unidad de procesamiento principal de un sistema. |
| **CronJob** | Recurso de Kubernetes que crea Jobs siguiendo una planificación temporal. |
| **CSRF** | Cross-Site Request Forgery, ataque que induce al navegador de una víctima a realizar una acción no deseada. |
| **CSS** | Cascading Style Sheets, lenguaje de hojas de estilo para definir la presentación de documentos web. |
| **Códec** | algoritmo que codifica y decodifica audio, vídeo u otro tipo de datos; un códec no es lo mismo que un contenedor multimedia. |
## D

| Término | Explicación |
|---|---|
| **DaemonSet** | Recurso de Kubernetes que asegura la ejecución de un Pod en los nodos que cumplen sus criterios. |
| **DELETE** | Método HTTP usado normalmente para solicitar la eliminación de un recurso. |
| **Demonio (daemon)** | proceso que permanece ejecutándose en segundo plano para prestar un servicio; en Linux es habitual que esté gestionado por `systemd`. |
| **DHCP** | Protocolo de configuración dinámica de host: entrega automáticamente parámetros de red a los clientes. |
| **DHCPACK** | Mensaje DHCP que confirma una concesión y sus parámetros. |
| **DHCPDISCOVER** | Mensaje DHCP con el que un cliente busca servidores disponibles. |
| **DHCPNAK** | Mensaje DHCP que rechaza una solicitud o indica que la concesión solicitada no es válida. |
| **DHCPOFFER** | Mensaje DHCP con el que un servidor ofrece parámetros de configuración. |
| **DHCPREQUEST** | Mensaje DHCP con el que un cliente solicita una oferta o confirma una concesión. |
| **Digest** | Identificador criptográfico de una imagen o contenido que permite referirse a una versión concreta. |
| **Dirección IP** | identificador lógico de una interfaz dentro de una red IP. |
| **DKIM** | DomainKeys Identified Mail, mecanismo que firma criptográficamente mensajes para facilitar su validación. |
| **DMARC** | Domain-based Message Authentication, Reporting and Conformance, política que relaciona autenticación del mensaje con el dominio del remitente y define acciones y reportes. |
| **DNS** | Sistema de nombres de dominio: servicio distribuido que relaciona nombres con direcciones IP y otros datos. |
| **DNSKEY** | Registro DNSSEC que publica una clave criptográfica. |
| **DNSSEC** | Extensiones de seguridad de DNS que permiten validar criptográficamente respuestas y datos DNS. |
| **Docker** | Plataforma de contenerización para construir, distribuir y ejecutar aplicaciones aisladas en contenedores. |
| **Docker Compose** | Herramienta de Docker para definir y ejecutar aplicaciones multicontenedor mediante un archivo declarativo. |
| **Dockerfile** | Archivo de instrucciones utilizado para construir una imagen de Docker. |
| **DORA** | Secuencia Discover, Offer, Request y Acknowledgement usada habitualmente para obtener una concesión IPv4 mediante DHCP. |
| **DS** | Registro DNSSEC que enlaza una clave de una zona hija con la cadena de confianza de la zona padre. |
## E

| Término | Explicación |
|---|---|
| **Encaminamiento (routing)** | proceso de decidir por qué camino debe avanzar un paquete para alcanzar su destino. |
| **EndpointSlice** | Objeto de Kubernetes que representa de forma escalable los endpoints que pertenecen a un Service. |
| **EOL** | End of Life: momento a partir del cual un producto deja de recibir soporte normal del fabricante. |
| **Estado** | situación actual de un proceso, servicio, interfaz o recurso; conocerlo es esencial para diagnosticar una incidencia. |
## F

| Término | Explicación |
|---|---|
| **FFmpeg** | Conjunto de herramientas para procesar, convertir, capturar y transmitir audio y vídeo. |
| **FPS** | Frames Per Second: número de imágenes de vídeo mostradas o procesadas por segundo. |
| **FQDN** | Nombre de dominio completamente cualificado, que identifica un nombre dentro de toda la jerarquía DNS. |
| **FROM** | Instrucción de Dockerfile que selecciona la imagen base. |
| **FTP** | Protocolo de transferencia de archivos que separa un canal de control de los canales de datos. |
| **FTP/TFTP** | FTP es un protocolo completo de transferencia de archivos; TFTP es una versión mínima basada en UDP. |
| **FTPS** | FTP protegido mediante TLS. |
| **FW** | Firewall o cortafuegos: sistema que filtra tráfico según reglas. |
| **FXP** | Mecanismo de transferencia directa entre dos servidores FTP coordinada por un cliente. |
## G

| Término | Explicación |
|---|---|
| **GET** | Método HTTP usado normalmente para solicitar una representación de un recurso. |
| **GET/POST** | Métodos HTTP utilizados, respectivamente, para solicitar recursos y enviar datos a un recurso. |
| **Git** | Sistema distribuido de control de versiones. |
| **GitHub** | Servicio de alojamiento y colaboración basado en repositorios Git. |
| **GUI** | Interfaz gráfica de usuario, es decir, administración mediante ventanas, menús y controles visuales. |
## H

| Término | Explicación |
|---|---|
| **HEAD** | Referencia de Git que identifica el commit actual de la línea de trabajo seleccionada. |
| **Healthcheck** | Comprobación definida para determinar si un servicio o contenedor responde según las condiciones esperadas. |
| **Helm** | Herramienta de empaquetado y gestión de aplicaciones Kubernetes mediante charts. |
| **HEVC** | High Efficiency Video Coding, estándar de compresión de vídeo también conocido como H.265. |
| **HLS** | HTTP Live Streaming, sistema de distribución de audio y vídeo segmentado mediante HTTP. |
| **Host** | Equipo o sistema anfitrión en el que se ejecuta un servicio, contenedor o máquina virtual. |
| **HTML** | HyperText Markup Language, lenguaje de marcado para estructurar documentos web. |
| **HTTP** | Protocolo de transferencia de hipertexto utilizado principalmente por la Web. |
| **HTTP/HTTPS** | HTTP es el protocolo web; HTTPS es HTTP protegido mediante TLS. |
| **HTTPS** | HTTP protegido mediante TLS. |
## I

| Término | Explicación |
|---|---|
| **IANA** | Internet Assigned Numbers Authority, organismo que coordina parámetros, espacios de nombres y números de Internet. |
| **Icecast** | Servidor de streaming de audio utilizado para distribuir flujos de audio a clientes compatibles. |
| **ICMP** | Internet Control Message Protocol: protocolo de control y diagnóstico de IP; herramientas como `ping` utilizan mensajes ICMP. |
| **ICQ** | Servicio histórico de mensajería instantánea. |
| **ID** | Identificador utilizado para distinguir un objeto de otros. |
| **IIS** | Internet Information Services, servidor web de Microsoft para Windows. |
| **IM** | Instant Messaging o mensajería instantánea. |
| **Imagen de contenedor** | plantilla inmutable a partir de la cual se crean contenedores. |
| **IMAP** | Internet Message Access Protocol, protocolo para acceder y gestionar mensajes que permanecen en el servidor. |
| **IMAPS** | IMAP protegido mediante TLS. |
| **Ingress** | Recurso de Kubernetes que describe reglas de entrada HTTP/HTTPS hacia Services; normalmente requiere un controlador de Ingress. |
| **INN** | InterNetNews, implementación de servidor de noticias NNTP. |
| **Interfaz de red** | componente físico o virtual mediante el que un sistema se conecta a una red. |
| **IOS** | Cisco Internetwork Operating System, sistema operativo de muchos equipos de red Cisco. |
| **IP** | Protocolo de Internet, responsable del direccionamiento y encaminamiento de paquetes. |
| **IPv4** | Versión 4 del Protocolo de Internet, con direcciones de 32 bits. |
| **IPv6** | Versión 6 del Protocolo de Internet, con direcciones de 128 bits. |
| **IRC** | Internet Relay Chat, protocolo de conversación textual en tiempo real mediante canales. |
| **ISC** | Internet Systems Consortium, organización que desarrolla software de infraestructura de Internet como BIND y Kea. |
| **IXFR** | Transferencia incremental de una zona DNS, limitada a los cambios. |
## J

| Término | Explicación |
|---|---|
| **JID** | Jabber ID, identificador de usuario XMPP, normalmente usuario@dominio/recurso. |
| **Job** | Recurso de Kubernetes que ejecuta una tarea hasta que se completa satisfactoriamente. |
| **JPEG** | Formato de imagen comprimida ampliamente usado en fotografía. |
| **JS** | JavaScript, lenguaje de programación usado ampliamente en aplicaciones web. |
| **JSON** | Formato textual para representar datos estructurados mediante objetos y listas. |
## K

| Término | Explicación |
|---|---|
| **KEA** | Servidor DHCP desarrollado por Internet Systems Consortium como alternativa moderna al servidor DHCP clásico de ISC. |
| **Kea** | Implementación moderna de servicios DHCP desarrollada por Internet Systems Consortium. |
| **Kubelet** | Agente que se ejecuta en cada nodo de Kubernetes y se encarga de que los contenedores de los Pods asignados funcionen según su especificación. |
| **Kustomize** | Herramienta de personalización de manifiestos Kubernetes sin necesidad de copiar y modificar cada archivo. |
## L

| Término | Explicación |
|---|---|
| **Label** | Par clave-valor que identifica o clasifica objetos de Kubernetes y permite seleccionarlos. |
| **LAN** | Red de área local. |
| **LEASE** | Concesión temporal de parámetros de red entregada por DHCP. |
| **Lease** | Concesión temporal de un recurso, especialmente de una dirección IP asignada mediante DHCP. |
| **LIST** | Comando FTP que solicita un listado de archivos. |
| **LISTSERV** | Sistema de gestión de listas de distribución de correo. |
## M

| Término | Explicación |
|---|---|
| **MAC** | Dirección de control de acceso al medio asociada a una interfaz de red. |
| **Manifest** | Archivo declarativo, normalmente YAML o JSON, que describe el estado deseado de uno o varios objetos de infraestructura. |
| **MDA** | Mail Delivery Agent, componente que entrega el mensaje al buzón del destinatario. |
| **MIME** | Multipurpose Internet Mail Extensions, mecanismo para describir tipos de contenido y adjuntos en mensajes. |
| **MKV** | Matroska Video, formato contenedor multimedia abierto. |
| **MP3** | Formato de audio comprimido basado en MPEG Audio Layer III. |
| **MP4** | Formato contenedor multimedia definido en MPEG-4 Part 14. |
| **MSA** | Mail Submission Agent, componente que recibe mensajes enviados por clientes para su posterior transporte. |
| **MSN/MSNP** | MSN Messenger fue un servicio histórico de mensajería; MSNP fue su protocolo de comunicación. |
| **MTA** | Mail Transfer Agent, componente que transporta correo entre servidores. |
| **MTU** | Unidad máxima de transmisión: tamaño máximo de una trama o paquete que puede transportarse sin fragmentación en un enlace concreto. |
| **MUA** | Mail User Agent, programa con el que el usuario compone, envía y lee correo. |
| **Multicast** | comunicación dirigida a un grupo de receptores que se han suscrito al grupo. |
| **MX** | Registro DNS que identifica los servidores que reciben correo. |
## N

| Término | Explicación |
|---|---|
| **Namespace** | Ámbito lógico dentro de un clúster de Kubernetes que permite organizar recursos. |
| **NAT** | Traducción de direcciones de red: modificación de direcciones IP al atravesar un dispositivo intermedio. |
| **NAT/PAT** | Combinación de NAT y PAT, habitual cuando varias direcciones privadas comparten una dirección pública. |
| **NDP** | Neighbor Discovery Protocol: conjunto de mecanismos de IPv6 para descubrimiento de vecinos, resolución de direcciones y autoconfiguración. |
| **Nginx** | Servidor web y proxy de alto rendimiento utilizado también como proxy inverso y para determinadas funciones de streaming. |
| **NIC** | Network Interface Controller/Card, interfaz que conecta un equipo a una red. |
| **NNTP** | Network News Transfer Protocol, protocolo para intercambio y consulta de artículos de grupos de noticias. |
| **NNTPS** | NNTP protegido mediante TLS. |
| **Node** | Máquina física o virtual que forma parte de un clúster de Kubernetes y ejecuta Pods. |
| **NS** | Registro DNS que identifica servidores autoritativos de una zona. |
| **NSEC/NSEC3** | Mecanismos DNSSEC que permiten demostrar de forma autenticada que determinados nombres o tipos de registros no existen. |
| **NXDOMAIN** | Respuesta DNS que indica que el nombre consultado no existe. |
## O

| Término | Explicación |
|---|---|
| **OBS** | Open Broadcaster Software, aplicación para captura, mezcla y emisión audiovisual. |
| **OPTIONS** | Método HTTP utilizado para consultar capacidades o métodos permitidos. |
| **Orquestación** | automatización de la ejecución, escalado, recuperación y coordinación de múltiples cargas de trabajo o contenedores. |
| **OSI** | Modelo de referencia que organiza las funciones de comunicación de red en siete capas. |
## P

| Término | Explicación |
|---|---|
| **PASS** | Comando de determinados protocolos, como FTP, utilizado para proporcionar la contraseña durante la autenticación. |
| **PASV** | Modo pasivo de FTP, en el que el servidor anuncia un puerto para el canal de datos. |
| **PAT** | Traducción de direcciones mediante puertos: permite multiplexar conexiones privadas sobre una dirección pública. |
| **PATCH** | Método HTTP usado normalmente para aplicar modificaciones parciales a un recurso. |
| **PCM** | Pulse-Code Modulation: representación digital de una señal de audio mediante muestras codificadas. |
| **PersistentVolume** | Recurso de Kubernetes que representa almacenamiento persistente disponible para las cargas de trabajo. |
| **PersistentVolumeClaim** | Solicitud de almacenamiento persistente realizada por una carga de trabajo de Kubernetes. |
| **PHP** | Lenguaje de programación de propósito general utilizado con frecuencia en aplicaciones web del lado del servidor. |
| **PNG** | Formato de imagen comprimida sin pérdida, adecuado para gráficos y transparencia. |
| **Pod** | unidad mínima desplegable de Kubernetes; contiene uno o varios contenedores que comparten determinados recursos. |
| **Podcast** | Contenido de audio o vídeo distribuido como episodios que pueden descargarse o reproducirse bajo demanda. |
| **POOL** | Conjunto de direcciones disponibles para asignación dinámica. |
| **POP3** | Post Office Protocol version 3, protocolo para recuperar mensajes del buzón. |
| **POP3S** | POP3 sobre TLS: recuperación de correo mediante una conexión protegida. |
| **Port mapping** | Correspondencia entre un puerto publicado en el host y un puerto del servicio dentro del contenedor. |
| **Port-forward** | Reenvío temporal de un puerto local hacia un recurso de Kubernetes, por ejemplo un Pod o un Service. |
| **POST** | Método HTTP usado normalmente para enviar datos al servidor para crear o procesar un recurso. |
| **POSTFIX** | Agente de transferencia de correo Postfix. |
| **Proceso** | instancia en ejecución de un programa dentro de un sistema operativo. |
| **Prosody** | Servidor XMPP de código abierto escrito en Lua. |
| **Protocolo** | conjunto de reglas que define cómo se comunican dos o más sistemas. |
| **PROXY** | Servidor intermediario que recibe peticiones de un cliente y las reenvía a otro servicio. |
| **Proxy** | Intermediario que recibe solicitudes y las reenvía a otro servicio; puede ser directo o inverso. |
| **PTR** | Registro usado en resolución DNS inversa, de dirección IP a nombre. |
| **Puerta de enlace predeterminada** | equipo al que un host entrega el tráfico destinado a redes que no conoce directamente. |
| **Puerto** | número lógico asociado a un servicio de transporte; permite distinguir varias comunicaciones que utilizan la misma dirección IP. |
| **PUT** | Método HTTP usado normalmente para crear o reemplazar la representación de un recurso en una URI determinada. |
| **PWD** | Comando FTP que muestra el directorio de trabajo actual. |
## Q

| Término | Explicación |
|---|---|
| **QUIC** | Protocolo de transporte moderno sobre UDP con seguridad y multiplexación. |
| **QUIT** | Comando de salida de sesiones de protocolos como FTP o IRC. |
## R

| Término | Explicación |
|---|---|
| **RA** | Resultado de Aprendizaje: capacidad que el alumnado debe demostrar al finalizar un bloque curricular. |
| **Rama (branch)** | línea de desarrollo independiente dentro de un repositorio Git. |
| **Red Docker** | red virtual administrada por Docker que permite conectar contenedores y, según su configuración, publicar servicios hacia el host. |
| **Registro (log)** | anotación generada por un programa o sistema para dejar constancia de eventos, errores y operaciones. |
| **Registro DNS** | entrada de una zona DNS que asocia un nombre con un dato, como una dirección IP, un servidor de correo o un alias. |
| **Registry** | Servicio que almacena y distribuye imágenes de contenedores. |
| **RELAY** | Agente que reenvía mensajes DHCP entre redes distintas. |
| **Relay agent** | Agente intermediario que reenvía mensajes DHCP entre clientes y servidores cuando no comparten directamente el mismo dominio de difusión. |
| **Remoto (remote)** | referencia a un repositorio Git externo con el que se intercambian commits mediante `fetch`, `pull` o `push`. |
| **ReplicaSet** | Recurso de Kubernetes que mantiene un número determinado de réplicas de un Pod. |
| **Resolución de nombres** | proceso mediante el cual un sistema obtiene información asociada a un nombre, por ejemplo una dirección IP mediante DNS. |
| **Resolver o resolvedor** | componente que realiza consultas DNS en nombre de una aplicación o de un usuario y obtiene la respuesta siguiendo el proceso de resolución. |
| **RETR** | Comando FTP que solicita la descarga de un archivo. |
| **REVERSE** | Proxy inverso: intermediario situado delante de servidores de origen y que recibe peticiones de los clientes. |
| **RFC** | Request for Comments: documento técnico que especifica o describe protocolos, estándares o prácticas de Internet. |
| **Rolling update** | Actualización progresiva de una carga de trabajo, sustituyendo réplicas gradualmente para reducir la interrupción del servicio. |
| **ROOT** | Servidores raíz de DNS, punto superior de la jerarquía de nombres. |
| **Roundcube** | cliente de correo web que accede al buzón mediante IMAP y puede enviar mensajes mediante SMTP. |
| **Router** | Dispositivo o proceso que toma decisiones de encaminamiento entre redes. |
| **RR** | Resource Record o registro de recursos DNS: unidad básica de información de una zona. |
| **RRSIG** | Registro DNSSEC que contiene una firma digital asociada a otros registros. |
| **RTMP** | Real-Time Messaging Protocol, protocolo usado en determinados flujos de ingestión de audio y vídeo en directo. |
| **RTMP/HLS** | RTMP puede utilizarse para ingestión de directo; HLS distribuye segmentos mediante HTTP. |
| **RTP** | Real-time Transport Protocol, protocolo para transportar medios en tiempo real. |
| **RTSP** | Real Time Streaming Protocol: protocolo de control utilizado en determinados sistemas de streaming de medios. |
## S

| Término | Explicación |
|---|---|
| **Sampling rate** | Frecuencia de muestreo: número de muestras por segundo utilizadas para representar una señal digital. |
| **SCP** | Secure Copy: copia de archivos sobre SSH. |
| **Secret** | Objeto de Kubernetes destinado a almacenar pequeñas cantidades de datos sensibles, como credenciales o tokens. |
| **Selector** | Criterio utilizado para seleccionar objetos que poseen determinadas labels. |
| **SERVFAIL** | Respuesta DNS que indica que el servidor no pudo completar correctamente la resolución. |
| **ServiceAccount** | Identidad que un Pod puede utilizar para autenticarse frente a la API de Kubernetes. |
| **Servicio de red** | aplicación o proceso que ofrece una función accesible mediante la red, normalmente a través de uno o varios puertos. |
| **Servidor** | programa o equipo que ofrece un servicio y atiende peticiones. |
| **Servidor autoritativo** | servidor que posee la información oficial de una zona DNS y puede responder con autoridad sobre ella. |
| **SFTP** | Protocolo de transferencia de archivos que funciona como subsistema de SSH; no es FTP cifrado. |
| **SFTP/SCP** | SFTP proporciona operaciones de transferencia sobre SSH; SCP realiza copias de archivos sobre SSH. |
| **SIP** | Session Initiation Protocol: protocolo utilizado para establecer, modificar y finalizar sesiones de comunicación, especialmente en VoIP. |
| **SMTP** | Simple Mail Transfer Protocol, protocolo principal para transportar correo entre agentes de correo. |
| **SMTPS** | SMTP establecido directamente sobre TLS. |
| **SNI** | Server Name Indication, extensión de TLS que indica el nombre del servicio solicitado durante el establecimiento seguro. |
| **SO** | Sistema operativo. |
| **SOA** | Registro DNS de autoridad de una zona que incluye información de temporización y control. |
| **SOAP** | Simple Object Access Protocol: protocolo de intercambio de mensajes estructurados basado en XML; no debe confundirse con los protocolos principales de SRI estudiados en esta guía. |
| **Socket** | extremo de comunicación que combina, según el contexto, una dirección IP, un puerto y un protocolo de transporte. |
| **SPF** | Sender Policy Framework, mecanismo que publica mediante DNS qué servidores están autorizados a enviar correo para un dominio. |
| **SPF/DKIM** | SPF publica remitentes autorizados mediante DNS; DKIM firma mensajes para facilitar su verificación. |
| **SRI** | Servicios de Red e Internet. |
| **SRV** | Registro DNS que publica la ubicación de un servicio mediante prioridad, peso, puerto y destino. |
| **SSH** | Protocolo seguro de administración remota y transporte de otros servicios. |
| **SSH/SFTP** | SSH es el protocolo seguro de transporte; SFTP es un subsistema de transferencia de archivos que funciona sobre SSH. |
| **SSL** | Familia histórica de protocolos de seguridad antecesora de TLS; hoy se considera obsoleta. |
| **Staging area** | área intermedia de Git donde se seleccionan los cambios que formarán el próximo commit. |
| **Stanza** | Unidad estructural de comunicación de XMPP, como `message`, `presence` o `iq`. |
| **STARTTLS** | Mecanismo que permite pasar una conexión inicialmente no cifrada a una sesión protegida mediante TLS. |
| **StartTLS** | Mecanismo mediante el que una conexión inicialmente no cifrada solicita cambiar a una conexión protegida mediante TLS. |
| **StatefulSet** | Recurso de Kubernetes pensado para aplicaciones con identidad estable y, habitualmente, almacenamiento persistente asociado a cada réplica. |
| **STOR** | Comando FTP que solicita la subida de un archivo. |
| **Streaming** | distribución de contenido de forma que el receptor puede comenzar a consumirlo mientras continúa recibiendo datos. |
| **Subred** | porción de un espacio de direccionamiento IP que comparte un prefijo común. |
| **SVG** | Scalable Vector Graphics, formato vectorial basado en XML. |
| **Sympa** | gestor de listas de distribución que proporciona funciones de suscripción, moderación, administración y distribución de mensajes. |
| **SYN** | Synchronization: bandera TCP utilizada durante el establecimiento de una conexión para sincronizar números de secuencia. |
| **`systemd`** | sistema de inicio y gestor de servicios habitual en Linux; `systemctl` permite consultar y administrar esos servicios. |
## T

| Término | Explicación |
|---|---|
| **Tabla de encaminamiento** | conjunto de rutas que utiliza un sistema para decidir dónde enviar los paquetes. |
| **TCP** | Protocolo de transporte orientado a conexión que proporciona entrega fiable y ordenada. |
| **TCP/IP** | Familia de protocolos de Internet en la que IP proporciona direccionamiento y TCP es uno de los protocolos de transporte. |
| **TFTP** | Protocolo muy sencillo de transferencia de archivos basado en UDP. |
| **TLD** | Top-Level Domain: dominio de nivel superior de la jerarquía DNS. |
| **TLS** | Protocolo criptográfico que proporciona confidencialidad, integridad y autenticación mediante certificados. |
| **TSIG** | Mecanismo de autenticación mediante una clave compartida para proteger operaciones DNS concretas. |
| **TTL** | Tiempo de vida de un dato o registro almacenado en caché. |
| **TXT** | Registro DNS que contiene información textual estructurada, como determinadas políticas de correo. |
## U

| Término | Explicación |
|---|---|
| **UDP** | Protocolo de transporte sin conexión, ligero y sin garantía de entrega. |
| **Unicast** | comunicación dirigida de un emisor a un receptor concreto. |
| **URI** | Identificador uniforme de recursos: sintaxis general para identificar un recurso. |
| **URI/URL** | URI identifica un recurso; URL es un URI que además proporciona una forma de localizarlo. |
| **URL** | Localizador uniforme de recursos: URI que además proporciona su ubicación mediante un esquema. |
| **USER** | Comando de determinados protocolos, como FTP, utilizado para indicar el nombre de usuario. |
| **UT** | Unidad de Trabajo: unidad didáctica del módulo profesional. |
## V

| Término | Explicación |
|---|---|
| **Validación** | comprobación de que una configuración tiene una sintaxis y una estructura aceptables antes de aplicarla. |
| **Virtual host** | configuración que permite que un mismo servidor web atienda distintos sitios o nombres mediante configuraciones diferenciadas. |
| **VirtualBox** | Hipervisor de virtualización utilizado en esta guía para ejecutar máquinas virtuales con Ubuntu Server. |
| **VLAN** | Virtual LAN: red de área local virtual que permite separar lógicamente dominios de red sobre infraestructura compartida. |
| **VLC** | VLC media player: reproductor multimedia de código abierto utilizado para reproducir y comprobar flujos de audio y vídeo. |
| **VM** | Máquina virtual: ordenador software aislado que ejecuta un sistema operativo invitado. |
| **VOD** | Video on Demand: distribución de vídeo bajo demanda. |
| **VoIP** | Voice over IP: transmisión de voz mediante redes basadas en IP. |
| **Volumen** | almacenamiento gestionado que permite conservar datos independientemente del ciclo de vida de un contenedor. |
| **VP9** | Códec de vídeo desarrollado por Google. |
## W

| Término | Explicación |
|---|---|
| **WAN** | Wide Area Network: red de área extensa que conecta redes separadas geográficamente. |
| **WAV** | Formato de archivo de audio que suele contener audio PCM. |
| **WAV/PCM** | WAV es un formato/contenedor de archivo; PCM es una representación digital de audio. |
| **Webmin** | interfaz web de administración de sistemas que permite gestionar determinados servicios y parámetros de un sistema Linux. |
| **WEBMIN** | Interfaz web de administración de sistemas Linux y Unix. |
| **WebRTC** | Tecnologías para comunicación en tiempo real de audio, vídeo y datos entre navegadores y otras aplicaciones compatibles. |
| **Wireshark** | Analizador gráfico de protocolos de red que permite capturar e inspeccionar tráfico. |
| **Workload** | Carga de trabajo que Kubernetes ejecuta y gestiona, por ejemplo mediante un Deployment, StatefulSet, Job o DaemonSet. |
| **WSL** | Windows Subsystem for Linux, plataforma de Windows para ejecutar entornos Linux. |
| **WSL2** | Windows Subsystem for Linux 2: tecnología de Windows que ejecuta un entorno Linux mediante una máquina virtual ligera. |
| **WWW** | World Wide Web: sistema de recursos enlazados accesibles principalmente mediante HTTP. |
## X

| Término | Explicación |
|---|---|
| **XEP** | XMPP Extension Protocol, especificación que define una extensión de XMPP. |
| **XML** | Extensible Markup Language, lenguaje de marcado para datos estructurados. |
| **XMPP** | Extensible Messaging and Presence Protocol, protocolo abierto para mensajería y presencia. |
| **XSS** | Cross-Site Scripting, vulnerabilidad que permite inyectar contenido ejecutable en páginas web servidas a otros usuarios. |
## Z

| Término | Explicación |
|---|---|
| **Zona DNS** | parte de la jerarquía DNS administrada por un servidor autoritativo concreto. |

## Referencias oficiales

- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [Kubernetes Concepts](https://kubernetes.io/docs/concepts/)
- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose Specification](https://docs.docker.com/reference/compose-file/)
- [Git Documentation](https://git-scm.com/docs)
- [GitHub Docs](https://docs.github.com/)
- [Visual Studio Code Documentation](https://code.visualstudio.com/docs)
- [Microsoft WSL Documentation](https://learn.microsoft.com/windows/wsl/)
