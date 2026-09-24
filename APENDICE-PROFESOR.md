# 👨‍🏫 APÉNDICE · Materiales para el profesor

> 🧭 **ANTES DE EMPEZAR · VOCABULARIO TÉCNICO**
>
> Las siglas, abreviaturas y conceptos técnicos que van a aparecer en esta unidad se presentan aquí antes de su desarrollo. La explicación local de cada tema podrá ampliar estas definiciones cuando sea necesario.
>
> **UT** — Unidad de Trabajo: unidad didáctica del módulo profesional.
> **RA** — Resultado de Aprendizaje: capacidad que el alumnado debe demostrar al finalizar un bloque curricular.
> **CFGS** — Ciclo Formativo de Grado Superior.
> **ASIR** — Administración de Sistemas Informáticos en Red.
> **SRI** — Servicios de Red e Internet.
> **IP** — Protocolo de Internet, responsable del direccionamiento y encaminamiento de paquetes.
> **PAT** — Traducción de direcciones mediante puertos: permite multiplexar conexiones privadas sobre una dirección pública.
> **WSL2** — Windows Subsystem for Linux 2: tecnología de Windows que ejecuta un entorno Linux mediante una máquina virtual ligera.
> **TCP** — Protocolo de transporte orientado a conexión que proporciona entrega fiable y ordenada.
> **TCP/IP** — Familia de protocolos de Internet en la que IP proporciona direccionamiento y TCP es uno de los protocolos de transporte.
> **DNS** — Sistema de nombres de dominio: servicio distribuido que relaciona nombres con direcciones IP y otros datos.
> **UDP** — Protocolo de transporte sin conexión, ligero y sin garantía de entrega.
> **MAC** — Dirección de control de acceso al medio asociada a una interfaz de red.
> **NAT** — Traducción de direcciones de red: modificación de direcciones IP al atravesar un dispositivo intermedio.
> **IPv6** — Versión 6 del Protocolo de Internet, con direcciones de 128 bits.
> **DHCP** — Protocolo de configuración dinámica de host: entrega automáticamente parámetros de red a los clientes.
> **DORA** — Secuencia Discover, Offer, Request y Acknowledgement usada habitualmente para obtener una concesión IPv4 mediante DHCP.
> **MX** — Registro DNS que identifica los servidores que reciben correo.
> **AAAA** — Registro DNS que asocia un nombre con una dirección IPv6.
> **PTR** — Registro usado en resolución DNS inversa, de dirección IP a nombre.
> **SCP** — Secure Copy: copia de archivos sobre SSH.
> **SSH** — Protocolo seguro de administración remota y transporte de otros servicios.
> **SFTP** — Protocolo de transferencia de archivos que funciona como subsistema de SSH; no es FTP cifrado.
> **FTP** — Protocolo de transferencia de archivos que separa un canal de control de los canales de datos.
> **TFTP** — Protocolo muy sencillo de transferencia de archivos basado en UDP.
> **TLS** — Protocolo criptográfico que proporciona confidencialidad, integridad y autenticación mediante certificados.
> **HTTP** — Protocolo de transferencia de hipertexto utilizado principalmente por la Web.
> **URL** — Localizador uniforme de recursos: URI que además proporciona su ubicación mediante un esquema.
> **SMTP** — Simple Mail Transfer Protocol, protocolo principal para transportar correo entre agentes de correo.
> **IMAP** — Internet Message Access Protocol, protocolo para acceder y gestionar mensajes que permanecen en el servidor.
> **ARP** — Protocolo que relaciona una dirección IPv4 con una dirección de enlace en una red local.
> **TXT** — Registro DNS que contiene información textual estructurada, como determinadas políticas de correo.
> **CNAME** — Registro DNS que define un alias de un nombre canónico.
> **XMPP** — Extensible Messaging and Presence Protocol, protocolo abierto para mensajería y presencia.
> **SNMP** — Simple Network Management Protocol, protocolo de supervisión y administración de dispositivos de red.
> **NNTP** — Network News Transfer Protocol, protocolo para intercambio y consulta de artículos de grupos de noticias.
> **BIND9** — Rama 9 de BIND, implementación de servidor DNS usada habitualmente en Linux.
> **HLS** — HTTP Live Streaming, sistema de distribución de audio y vídeo segmentado mediante HTTP.
> **SSH/SFTP** — SSH es el protocolo seguro de transporte; SFTP es un subsistema de transferencia de archivos que funciona sobre SSH.
> **HTTPS** — HTTP protegido mediante TLS.
> **MTA** — Mail Transfer Agent, componente que transporta correo entre servidores.
> **FFmpeg** — Conjunto de herramientas para procesar, convertir, capturar y transmitir audio y vídeo.
> **URI** — Identificador uniforme de recursos: sintaxis general para identificar un recurso.
> **Git** — Sistema distribuido de control de versiones.
> **Docker** — Plataforma de contenerización para construir, distribuir y ejecutar aplicaciones aisladas en contenedores.
> **Docker Compose** — Herramienta de Docker para definir y ejecutar aplicaciones multicontenedor mediante un archivo declarativo.
> **NAT/PAT** — Combinación de NAT y PAT, habitual cuando varias direcciones privadas comparten una dirección pública.
> **FTPS** — FTP protegido mediante TLS.
> **SFTP/SCP** — SFTP proporciona operaciones de transferencia sobre SSH; SCP realiza copias de archivos sobre SSH.
> **WWW** — World Wide Web, sistema de recursos enlazados accesibles principalmente mediante HTTP.
> **URI/URL** — URI identifica un recurso; URL es un URI que además proporciona una forma de localizarlo.
> **MIME** — Multipurpose Internet Mail Extensions, mecanismo para describir tipos de contenido y adjuntos en mensajes.
> **POP3** — Post Office Protocol version 3, protocolo para recuperar mensajes del buzón.
> **MTA/MUA/MRA** — MTA transporta correo; MUA es el cliente de usuario; MRA es un agente de recuperación de correo.
> **MUA** — Mail User Agent, programa con el que el usuario compone, envía y lee correo.
> **IRC** — Internet Relay Chat, protocolo de conversación textual en tiempo real mediante canales.
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

> **Material docente integral · CFGS ASIR · Servicios de Red e Internet**

Este apéndice contiene instrumentos de evaluación y propuestas de laboratorio alineados con las ocho UT y con los resultados de aprendizaje del módulo.

## 1. 🎯 Criterios de uso

Las pruebas tipo test están diseñadas como instrumentos de comprobación, no como sustituto de la evaluación práctica. Cada UT contiene **3 preguntas**, con **una única respuesta válida**. La posición de la respuesta correcta se distribuye deliberadamente para evitar patrones previsibles.

Las actividades prácticas están diseñadas para una duración máxima de **1 h 45 min** y se pueden ejecutar en VirtualBox + Ubuntu 26.04 Server, WSL2 o, cuando proceda, Cisco Packet Tracer.

---

# 2. 📝 Banco de test por UT

## UT1 · TCP/IP

**1. ¿Qué función corresponde principalmente a la capa de transporte?**

A. Resolver nombres DNS.
B. Proporcionar comunicación extremo a extremo mediante protocolos como TCP y UDP.
C. Asignar direcciones MAC.
D. Determinar exclusivamente la ruta IP.

**2. ¿Qué describe mejor una ruta por defecto?**

A. Una ruta utilizada cuando no existe una ruta más específica para el destino.
B. Una ruta que siempre apunta al servidor DNS.
C. Una ruta que sólo funciona con UDP.
D. Una ruta utilizada únicamente para tráfico multicast.

**3. ¿Qué hace PAT en un escenario típico de NAT?**

A. Convierte nombres DNS en direcciones IPv6.
B. Sustituye TCP por UDP.
C. Permite multiplexar conexiones mediante diferentes puertos usando una dirección pública compartida.
D. Elimina la necesidad de encaminamiento.

## UT2 · DHCP

**4. ¿Cuál es el orden habitual del proceso DORA?**

A. Discover → Offer → Request → Acknowledge.
B. Discover → Request → Offer → Acknowledge.
C. Offer → Discover → Acknowledge → Request.
D. Request → Offer → Discover → Acknowledge.

**5. ¿Qué diferencia una reserva DHCP de una concesión dinámica ordinaria?**

A. Una reserva impide utilizar DNS.
B. Una reserva asocia de forma estable determinados parámetros, normalmente una IP, con un cliente identificado.
C. Una reserva sólo funciona con IPv6.
D. Una reserva sustituye al gateway.

**6. ¿Para qué sirve un DHCP relay?**

A. Para cifrar DHCP.
B. Para sustituir el servidor DNS.
C. Para almacenar las concesiones en una base de datos.
D. Para permitir que solicitudes DHCP atraviesen segmentos de red donde el broadcast no puede llegar directamente al servidor.

## UT3 · DNS

**7. ¿Qué registro se utiliza habitualmente para asociar un nombre con una dirección IP?**

A. MX
B. AAAA
C. A
D. PTR

**8. ¿Qué caracteriza a un servidor DNS autoritativo?**

A. Siempre reenvía todas las consultas a Google.
B. Posee información autoritativa sobre una o más zonas.
C. Sólo puede resolver direcciones IPv6.
D. No puede responder consultas recursivas.

**9. ¿Qué comando es especialmente apropiado para comprobar registros DNS y observar respuestas detalladas?**

A. `dig`
B. `scp`
C. `sshd`
D. `ip link set`

## UT4 · Transferencia de ficheros

**10. ¿Cuál es la característica fundamental de SFTP?**

A. Es FTP con UDP.
B. Es un protocolo independiente basado en SSH.
C. Es FTP sin autenticación.
D. Es TFTP sobre TLS.

**11. En FTP tradicional, ¿qué puerto TCP se utiliza normalmente para el canal de control?**

A. 20
B. 22
C. 25
D. 21

**12. ¿Por qué el modo pasivo de FTP es especialmente relevante cuando existen firewalls o NAT?**

A. Porque elimina TCP.
B. Porque utiliza exclusivamente el puerto 21 para todo.
C. Porque permite que el cliente inicie también la conexión de datos, facilitando determinados escenarios atravesando firewalls/NAT.
D. Porque convierte FTP en SFTP.

## UT5 · HTTP

**13. ¿Qué función desempeña un Virtual Host?**

A. Permite servir diferentes sitios o configuraciones desde una misma infraestructura web según criterios como nombre, dirección o puerto.
B. Sustituye siempre al DNS.
C. Convierte HTTP en FTP.
D. Impide utilizar TLS.

**14. ¿Qué herramienta es adecuada para realizar una prueba HTTP desde una terminal?**

A. `dig`
B. `curl`
C. `scp`
D. `ip neigh flush`

**15. ¿Qué diferencia fundamental existe entre `proxy_pass` de Nginx y un servidor web que entrega directamente un fichero estático?**

A. `proxy_pass` permite reenviar la petición a otro servicio backend.
B. `proxy_pass` sólo funciona con FTP.
C. Un servidor estático no utiliza HTTP.
D. `proxy_pass` desactiva DNS.

## UT6 · Correo electrónico

**16. ¿Cuál es la función principal de SMTP?**

A. Leer exclusivamente mensajes mediante IMAP.
B. Transferir mensajes de correo entre agentes y servidores de correo.
C. Resolver nombres de dominio.
D. Cifrar discos.

**17. ¿Qué protocolo está orientado principalmente al acceso remoto a un buzón manteniendo los mensajes en el servidor?**

A. IMAP
B. TFTP
C. DNS
D. ARP

**18. ¿Qué registro DNS se utiliza para indicar servidores de correo de un dominio?**

A. TXT exclusivamente
B. PTR
C. MX
D. CNAME exclusivamente

## UT7 · Mensajería, noticias y listas

**19. ¿Qué protocolo está asociado históricamente con la mensajería instantánea extensible y la presencia?**

A. XMPP
B. FTP
C. SMTP
D. SNMP

**20. ¿Qué caracteriza a una lista de distribución?**

A. Cada mensaje sólo puede tener un destinatario.
B. Permite distribuir mensajes a un conjunto de suscriptores según las reglas configuradas.
C. Sustituye necesariamente a DNS.
D. Utiliza exclusivamente UDP.

**21. ¿Qué protocolo se asocia con los servicios de noticias Usenet?**

A. DHCP
B. HTTP
C. NNTP
D. IMAP

## UT8 · Audio y vídeo

**22. ¿Qué diferencia básica existe entre un códec y un contenedor multimedia?**

A. Son exactamente lo mismo.
B. El códec define la compresión/codificación; el contenedor organiza uno o varios flujos y metadatos.
C. El contenedor sólo existe para audio.
D. El códec sólo define la dirección IP.

**23. ¿Qué componente es apropiado para servir audio mediante streaming en un laboratorio SRI?**

A. Icecast
B. BIND9
C. Kea DHCP
D. Postfix

**24. ¿Qué ventaja fundamental aporta HLS?**

A. Elimina la necesidad de cualquier servidor HTTP.
B. Permite distribuir vídeo mediante HTTP utilizando una playlist y segmentos.
C. Sólo funciona sobre FTP.
D. Sustituye a los códecs.

---

# 3. ✅ Solucionario del test

| Pregunta | Respuesta | UT |
|---:|:---:|:---:|
| 1 | **B** | UT1 |
| 2 | **A** | UT1 |
| 3 | **C** | UT1 |
| 4 | **A** | UT2 |
| 5 | **B** | UT2 |
| 6 | **D** | UT2 |
| 7 | **C** | UT3 |
| 8 | **B** | UT3 |
| 9 | **A** | UT3 |
| 10 | **B** | UT4 |
| 11 | **D** | UT4 |
| 12 | **C** | UT4 |
| 13 | **A** | UT5 |
| 14 | **B** | UT5 |
| 15 | **A** | UT5 |
| 16 | **B** | UT6 |
| 17 | **A** | UT6 |
| 18 | **C** | UT6 |
| 19 | **A** | UT7 |
| 20 | **B** | UT7 |
| 21 | **C** | UT7 |
| 22 | **B** | UT8 |
| 23 | **A** | UT8 |
| 24 | **B** | UT8 |

La distribución de respuestas evita utilizar una única posición como patrón de corrección.

---

# 4. 🧪 Prácticas evaluables de máximo 1 h 45 min

## PE01 · TCP/IP y diagnóstico

**Entorno:** VirtualBox + Ubuntu 26.04 Server + cliente Linux.

### Enunciado

Configura una red privada entre dos máquinas. El servidor debe tener una dirección estática y el cliente debe poder alcanzarlo. Documenta direccionamiento, rutas y puertos abiertos.

### Evidencias

```bash
ip addr
ip route
ss -lntup
ping -c 4 SERVIDOR
```

**Duración:** 1 h 30 min.

## PE02 · DHCP con Kea

**Entorno:** VirtualBox + Ubuntu Server.

Instala Kea DHCP, configura una subred de laboratorio, un pool y una reserva. Valida la configuración antes de reiniciar el servicio y demuestra una concesión correcta.

**Duración:** 1 h 45 min.

## PE03 · DNS con BIND9

Crea una zona directa e inversa. Añade registros `A`, `AAAA` y `MX`. Comprueba la resolución con `dig` y documenta el resultado.

**Duración:** 1 h 45 min.

## PE04 · Transferencia segura

Configura SSH/SFTP. Crea un usuario limitado y demuestra una transferencia de fichero. Comprueba permisos y registra las pruebas.

**Duración:** 1 h 30 min.

## PE05 · Dos sitios web

Configura Apache o Nginx con dos sitios virtuales y acceso HTTPS de laboratorio. Analiza los logs y demuestra mediante `curl` qué sitio responde a cada nombre.

**Duración:** 1 h 45 min.

## PE06 · Correo en laboratorio

Configura un MTA y un servicio de acceso al buzón en una red privada. Demuestra SMTP y acceso al buzón. Comprueba que el servidor no funciona como relay abierto.

**Duración:** 1 h 45 min.

## PE07 · Mensajería instantánea

Despliega un servidor XMPP de laboratorio, crea dos cuentas y demuestra una sesión entre dos clientes. Documenta autenticación y puertos.

**Duración:** 1 h 30 min.

## PE08 · Streaming de audio

Instala Icecast y utiliza FFmpeg para producir un flujo de audio de laboratorio. Accede desde VLC, mide el bitrate y documenta el recorrido completo.

**Duración:** 1 h 45 min.

---

# 5. 🧩 Práctica integradora

## Proyecto · Servicios de red reproducibles

Construye una infraestructura que contenga como mínimo:

```text
                 ┌──────────────┐
                 │     DNS      │
                 └──────┬───────┘
                        │
          ┌─────────────┼─────────────┐
          ▼             ▼             ▼
       HTTP           SFTP          XMPP
          │             │             │
          └─────────────┼─────────────┘
                        ▼
                  cliente de pruebas
```

El proyecto debe incluir:

- diagrama de red;
- direccionamiento;
- puertos;
- configuración;
- pruebas;
- logs;
- medidas de seguridad;
- README técnico;
- repositorio Git;
- versión Docker Compose cuando el servicio lo permita.

**Duración recomendada:** varias sesiones. No utilizar como práctica de 1 h 45 min.

---

# 6. 📚 Sobre las preguntas de evaluación del material de referencia

El repositorio  utiliza el material de referencia para determinar **contenidos, objetivos y bloques de evaluación**, pero las preguntas de este apéndice están **reformuladas y ampliadas** para el currículo y las tecnologías actuales. No se reproduce aquí de forma literal un banco completo de preguntas del libro de referencia.

La cobertura de evaluación se mantiene mediante bloques equivalentes:

| UT | Contenidos evaluados |
|---|---|
| UT1 | arquitectura TCP/IP, IP/IPv6, subredes, transporte, puertos, NAT/PAT, routing y virtualización |
| UT2 | DHCP, DORA, concesiones, reservas, opciones, relay, DHCPv6 y seguridad |
| UT3 | DNS, zonas, registros, resolución, BIND9, delegación, transferencia de zona y seguridad |
| UT4 | FTP, FTPS, TFTP, SFTP/SCP, modos, autenticación, permisos y seguridad |
| UT5 | WWW, URI/URL, HTTP, MIME, servidores, proxies, Virtual Hosts, HTTPS y logs |
| UT6 | arquitectura de correo, SMTP, IMAP, POP3, MIME, MTA/MUA/MRA, TLS, spam y autenticación |
| UT7 | mensajería instantánea, XMPP, IRC, listas de distribución, NNTP, servidores y clientes |
| UT8 | formatos, códecs, contenedores, reproducción, streaming, podcast, VoIP y videoconferencia |

La adaptación evita trasladar preguntas dependientes de productos, versiones o interfaces que han quedado obsoletas y permite evaluar los conceptos mediante las plataformas actuales del laboratorio.

---

# 7. 🧾 Rúbrica común para prácticas

| Criterio | Peso orientativo |
|---|---:|
| Comprensión del problema | 15 % |
| Diseño de la solución | 15 % |
| Configuración correcta | 25 % |
| Pruebas y evidencias | 20 % |
| Diagnóstico | 10 % |
| Seguridad | 5 % |
| Documentación | 10 % |

La ponderación concreta debe adaptarse a la programación didáctica y a los criterios de evaluación del RA correspondiente.

---

# 8. 🧠 Lista de comprobación del profesor

Antes de utilizar una práctica:

- [ ] ¿La versión de Ubuntu está disponible?
- [ ] ¿El paquete/software sigue existiendo?
- [ ] ¿Los puertos son correctos?
- [ ] ¿La configuración se valida antes de reiniciar?
- [ ] ¿Existe una prueba funcional objetiva?
- [ ] ¿Hay una incidencia deliberada o supuesto de diagnóstico?
- [ ] ¿La práctica puede completarse en el tiempo previsto?
- [ ] ¿La evidencia entregada permite corregirla sin repetir el laboratorio?
- [ ] ¿Los secretos están fuera del repositorio?
- [ ] ¿La práctica está vinculada al RA y a sus criterios de evaluación?

---

# 9. 🏁 Principio metodológico

> **No evaluar sólo que el servicio funcione. Evaluar que el alumno sepa explicar por qué funciona, demostrarlo, detectar cuándo deja de funcionar y justificar cómo lo ha solucionado.**
