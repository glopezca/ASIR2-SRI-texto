# 🌍⚡ Unidad de Trabajo 5 · SERVIDORES WEB Y PROTOCOLO DE TRANSFERENCIA DE HIPERTEXTO (HTTP) ⚡🌍

> 🧭 **ANTES DE EMPEZAR · VOCABULARIO TÉCNICO**
>
> Las siglas, abreviaturas y conceptos técnicos que van a aparecer en esta unidad se presentan aquí antes de su desarrollo. La explicación local de cada tema podrá ampliar estas definiciones cuando sea necesario.
>
> **UT** — Unidad de Trabajo: unidad didáctica del módulo profesional.
> **RA** — Resultado de Aprendizaje: capacidad que el alumnado debe demostrar al finalizar un bloque curricular.
> **CFGS** — Ciclo Formativo de Grado Superior.
> **ASIR** — Administración de Sistemas Informáticos en Red.
> **SRI** — Servicios de Red e Internet.
> **HTTP** — Protocolo de transferencia de hipertexto utilizado principalmente por la Web.
> **WSL2** — Windows Subsystem for Linux 2: tecnología de Windows que ejecuta un entorno Linux mediante una máquina virtual ligera.
> **CA** — Autoridad de certificación que emite y firma certificados digitales.
> **IIS** — Internet Information Services, servidor web de Microsoft para Windows.
> **CLI** — Interfaz de línea de comandos, es decir, administración mediante órdenes escritas.
> **IP** — Protocolo de Internet, responsable del direccionamiento y encaminamiento de paquetes.
> **HTTPS** — HTTP protegido mediante TLS.
> **PROXY** — Servidor intermediario que recibe peticiones de un cliente y las reenvía a otro servicio.
> **TCP** — Protocolo de transporte orientado a conexión que proporciona entrega fiable y ordenada.
> **TLS** — Protocolo criptográfico que proporciona confidencialidad, integridad y autenticación mediante certificados.
> **URI** — Identificador uniforme de recursos: sintaxis general para identificar un recurso.
> **Docker** — Plataforma de contenerización para construir, distribuir y ejecutar aplicaciones aisladas en contenedores.
> **Docker Compose** — Herramienta de Docker para definir y ejecutar aplicaciones multicontenedor mediante un archivo declarativo.
> **URL** — Localizador uniforme de recursos: URI que además proporciona su ubicación mediante un esquema.
> **MIME** — Multipurpose Internet Mail Extensions, mecanismo para describir tipos de contenido y adjuntos en mensajes.
> **DNS** — Sistema de nombres de dominio: servicio distribuido que relaciona nombres con direcciones IP y otros datos.
> **URI/URL** — URI identifica un recurso; URL es un URI que además proporciona una forma de localizarlo.
> **WWW** — World Wide Web, sistema de recursos enlazados accesibles principalmente mediante HTTP.
> **HTTP/HTTPS** — HTTP es el protocolo web; HTTPS es HTTP protegido mediante TLS.
> **HTML** — HyperText Markup Language, lenguaje de marcado para estructurar documentos web.
> **CSS** — Cascading Style Sheets, lenguaje de hojas de estilo para definir la presentación de documentos web.
> **JS** — JavaScript, lenguaje de programación usado ampliamente en aplicaciones web.
> **BD** — Base de datos.
> **PHP** — Lenguaje de programación de propósito general utilizado con frecuencia en aplicaciones web del lado del servidor.
> **REVERSE** — Proxy inverso: intermediario situado delante de servidores de origen y que recibe peticiones de los clientes.
> **GET** — Método HTTP usado normalmente para solicitar una representación de un recurso.
> **OPTIONS** — Método HTTP utilizado para consultar capacidades o métodos permitidos.
> **UDP** — Protocolo de transporte sin conexión, ligero y sin garantía de entrega.
> **POST** — Método HTTP usado normalmente para enviar datos al servidor para crear o procesar un recurso.
> **HEAD** — Referencia de Git que identifica el commit actual de la línea de trabajo seleccionada.
> **PUT** — Método HTTP usado normalmente para crear o reemplazar la representación de un recurso en una URI determinada.
> **PATCH** — Método HTTP usado normalmente para aplicar modificaciones parciales a un recurso.
> **DELETE** — Método HTTP usado normalmente para solicitar la eliminación de un recurso.
> **JSON** — Formato textual para representar datos estructurados mediante objetos y listas.
> **XSS** — Cross-Site Scripting, vulnerabilidad que permite inyectar contenido ejecutable en páginas web servidas a otros usuarios.
> **CSRF** — Cross-Site Request Forgery, ataque que induce al navegador de una víctima a realizar una acción no deseada.
> **QUIC** — Protocolo de transporte moderno sobre UDP con seguridad y multiplexación.
> **SSL** — Familia histórica de protocolos de seguridad antecesora de TLS; hoy se considera obsoleta.
> **VM** — Máquina virtual: ordenador software aislado que ejecuta un sistema operativo invitado.
> **ACL** — Lista de control de acceso que determina quién puede realizar una operación.
> **SNI** — Server Name Indication, extensión de TLS que indica el nombre del servicio solicitado durante el establecimiento seguro.
> **ACME** — Automated Certificate Management Environment, protocolo para automatizar la obtención y renovación de certificados.
> **FTP** — Protocolo de transferencia de archivos que separa un canal de control de los canales de datos.
> **DHCP** — Protocolo de configuración dinámica de host: entrega automáticamente parámetros de red a los clientes.
> **TFTP** — Protocolo muy sencillo de transferencia de archivos basado en UDP.
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

### RA3 · Administración de servidores Web.

> **SERVICIOS DE RED E INTERNET · CFGS ASIR · Material docente integral · 2026**
>
> Material autónomo actualizado para el perfil profesional de Técnico Superior en Administración de Sistemas Informáticos en Red. Laboratorio de referencia: **Cisco Packet Tracer**, **WSL2 + Ubuntu 26.04** y **VirtualBox + Ubuntu 26.04 Server**.
>
> ### 🎯 Resultado de aprendizaje trabajado
>
> **RA3.** Administra servidores Web aplicando criterios de configuración y asegurando el funcionamiento del servicio.

---

> 🎯 **MISIÓN DE LA UT**
>
> Comprender cómo funciona la Web desde la petición del navegador hasta
> la respuesta del servidor, y ser capaz de **instalar, configurar,
> publicar, asegurar, monitorizar y diagnosticar** un servicio web.
>
> El objetivo profesional es poder responder:
>
> **«Tengo que publicar una aplicación web. ¿Qué servidor utilizo, cómo
> lo configuro, cómo separo varios sitios, cómo lo protejo y cómo
> demuestro que funciona?»**

> ⚠️ **Actualización tecnológica**
>
> El enfoque práctico actual utiliza versiones y herramientas contemporáneas, manteniendo los conceptos fundamentales:
>
> - 🧪 **Cisco Packet Tracer** para la parte de red y servicios básicos.
> - 🐧 **WSL2 + Ubuntu 26.04** como cliente y entorno de pruebas.
> - 🖥️ **VirtualBox + Ubuntu 26.04 Server** como plataforma principal de servidor.
>
> La documentación actual de Ubuntu organiza la configuración de Apache mediante `apache2.conf`, `ports.conf`, `mods-*`, `conf-*` y `sites-*`.

------------------------------------------------------------------------

# 🧭 Mapa de la unidad

``` text
                         🌐 WEB
                           │
             ┌─────────────┼─────────────┐
             │             │             │
           HTTP          HTTPS         PROXY
             │             │             │
          TCP/80        TLS/443       🔀 caché
             │             │             │
             └──────┬──────┴──────┬──────┘
                    │             │
                 Apache          Nginx
                    │             │
              ┌─────┴─────┐      │
              │           │      │
          VirtualHost   módulos   │
              │           │       │
              └──────┬────┴───────┘
                     ▼
                 🗂️ SITIOS
                     │
             ┌───────┴────────┐
             │                │
          estático          aplicación
             │                │
             └───────┬────────┘
                     ▼
                🔐 SEGURIDAD
                     │
          TLS · permisos · logs
┌──────────────────────────────────────────────────────────────────────┐
│ 🧪 ENTORNOS · I Packet Tracer · II WSL2 · III VirtualBox · IV Compose │
└──────────────────────────────────────────────────────────────────────┘
```

------------------------------------------------------------------------

> 🧪 **LOS CUATRO ENTORNOS DE PRÁCTICAS**
>
> **I · Cisco Packet Tracer** — simulación de red y protocolos.  
> **II · WSL2 + Ubuntu 26.04** — herramientas, clientes y diagnóstico.  
> **III · VirtualBox + Ubuntu 26.04 Server** — administración de servidores completos.  
> **IV · Docker Compose** — infraestructura reproducible y multicontenedor.


# 🎯 0. Objetivos

Al finalizar esta unidad deberás ser capaz de:

-   Explicar qué es la Web y cómo se relaciona con Internet.
-   Identificar los principales componentes de una arquitectura web.
-   Diferenciar página web, sitio web y aplicación web.
-   Comprender el papel del navegador.
-   Diferenciar URI, URL y otros identificadores de recursos.
-   Explicar el funcionamiento básico de HTTP.
-   Interpretar una petición HTTP.
-   Interpretar una respuesta HTTP.
-   Conocer los principales métodos HTTP.
-   Interpretar códigos de estado.
-   Comprender cabeceras HTTP.
-   Explicar cookies, caché, compresión y redirecciones.
-   Comprender MIME y `Content-Type`.
-   Diferenciar HTTP y HTTPS.
-   Comprender TLS y certificados digitales.
-   Instalar y configurar Apache.
-   Comprender la arquitectura de configuración de Apache en Ubuntu.
-   Activar y desactivar módulos.
-   Crear sitios virtuales.
-   Configurar autenticación y control de acceso.
-   Configurar HTTPS en un laboratorio.
-   Analizar logs de acceso y errores.
-   Utilizar herramientas de diagnóstico HTTP.
-   Comprender el funcionamiento básico de un proxy web.
-   Comparar Apache y Nginx.
-   Diagnosticar problemas de conectividad, configuración, permisos y
    TLS.

------------------------------------------------------------------------

# 🚀 1. Introducción

La Web es uno de los servicios de red más utilizados.

Conceptualmente:

``` text
        🌐 INTERNET
             │
             │ HTTP / HTTPS
             ▼
       ┌─────────────┐
       │   SERVIDOR  │
       │     WEB     │
       └──────┬──────┘
              │
              ▼
         recurso web
```

Pero una página web aparentemente sencilla puede implicar:

``` text
DNS
 ↓
TCP
 ↓
TLS
 ↓
HTTP
 ↓
Servidor web
 ↓
Aplicación
 ↓
Base de datos
```

Por eso un administrador de sistemas debe entender tanto el protocolo
como la infraestructura que lo soporta.

------------------------------------------------------------------------

> 🧭 **ANTES DE EMPEZAR · Web y HTTP**
>
> La Web combina recursos identificados mediante URI/URL, clientes que realizan peticiones y servidores que devuelven respuestas. Más adelante formalizaremos este intercambio mediante HTTP.

# 🌍 2. WWW

**WWW --- World Wide Web** es un sistema distribuido de información
construido sobre Internet.

Sus elementos fundamentales incluyen:

``` text
🌐 recursos
🔗 enlaces
🧭 identificadores
📡 HTTP/HTTPS
🖥️ servidores
🌎 clientes
```

No debe confundirse:

``` text
Internet ≠ Web
```

Internet es la infraestructura y conjunto de redes interconectadas.

La Web es uno de los servicios que funciona sobre Internet.

------------------------------------------------------------------------

# 🏛️ 3. W3C y estándares Web

La Web se apoya en estándares.

El **W3C --- World Wide Web Consortium** ha desempeñado históricamente
un papel central en la estandarización de tecnologías Web.

Entre las tecnologías relacionadas encontramos:

``` text
HTML
CSS
DOM
HTTP
URI
```

Actualmente muchas especificaciones Web se desarrollan también en
colaboración con otros organismos y comunidades, por lo que no debe
interpretarse que «todo estándar Web» procede exclusivamente del W3C.

> 🧠 **Idea clave**
>
> Un administrador no necesita memorizar la organización que mantiene
> cada especificación, pero sí debe comprender que la interoperabilidad
> de la Web depende de estándares abiertos y protocolos bien definidos.

------------------------------------------------------------------------

# 🧩 4. Componentes y funcionamiento

Una arquitectura web básica:

``` text
┌──────────────┐
│   NAVEGADOR  │
└──────┬───────┘
       │
       │ HTTP/HTTPS
       ▼
┌──────────────┐
│ SERVIDOR WEB │
└──────┬───────┘
       │
       ├── HTML
       ├── CSS
       ├── JS
       ├── imágenes
       └── aplicación
```

En una aplicación dinámica:

``` text
NAVEGADOR
    │
    ▼
WEB SERVER
    │
    ▼
APLICACIÓN
    │
    ▼
BASE DE DATOS
```

------------------------------------------------------------------------

# 🧭 5. URIs y URLs

Una **URI --- Uniform Resource Identifier** identifica un recurso.

Una **URL --- Uniform Resource Locator** proporciona además información
para localizarlo mediante un mecanismo de acceso.

Ejemplo:

``` text
https://www.ejemplo.test:443/alumnos/ut5/index.html?grupo=asir#inicio
│      │                    │            │             │        │
│      │                    │            │             │        └─ fragmento
│      │                    │            │             └─ consulta
│      │                    │            └─ recurso
│      │                    └─ puerto
│      └─ autoridad/host
└─ esquema
```

La estructura conceptual ayuda a interpretar cualquier URL.

------------------------------------------------------------------------

> 🧭 **ANTES DE EMPEZAR · Página, sitio y aplicación web**
>
> Una página es un recurso concreto; un sitio agrupa recursos relacionados; una aplicación web añade lógica de aplicación y normalmente genera o procesa información dinámica. Esta distinción será importante al configurar servidores y proxies.

# 🏠 6. Páginas, sitios y aplicaciones

## Página web

Un recurso concreto:

``` text
/index.html
```

## Sitio web

Conjunto organizado de recursos:

``` text
www.ejemplo.test
├── index.html
├── css/
├── js/
├── img/
└── documentos/
```

## Aplicación web

Incluye lógica de aplicación:

``` text
Navegador
    │
    ▼
HTTP
    │
    ▼
Web server
    │
    ▼
Aplicación
    │
    ▼
BD
```

Ejemplos de tecnologías de aplicación:

``` text
PHP
Python
Node.js
Java
.NET
```

> ⚠️ **Servidor web ≠ aplicación web**
>
> Apache puede servir directamente contenido estático y actuar como
> parte de una arquitectura que entrega peticiones a una aplicación.

------------------------------------------------------------------------

# 🖥️ 7. Servidores web

Un servidor web:

-   escucha peticiones;
-   recibe solicitudes HTTP;
-   localiza o genera recursos;
-   devuelve respuestas;
-   registra actividad;
-   aplica políticas de acceso;
-   puede terminar TLS;
-   puede actuar como proxy o reverse proxy.

Ejemplos:

``` text
Apache HTTP Server
Nginx
Caddy
Microsoft IIS
```

En esta UT utilizaremos principalmente:

``` text
🪶 Apache 2.4
```

y compararemos conceptos con:

``` text
🚀 Nginx
```

------------------------------------------------------------------------

# 🌐 8. Clientes web

El cliente habitual es el navegador:

``` text
Firefox
Chrome
Edge
Safari
```

Pero también podemos utilizar:

``` bash
curl
wget
```

Esto es especialmente útil para administración.

Ejemplo:

``` bash
curl http://192.168.10.10/
```

Cabeceras:

``` bash
curl -I http://192.168.10.10/
```

Modo detallado:

``` bash
curl -v http://192.168.10.10/
```

HTTPS:

``` bash
curl -vk https://192.168.10.10/
```

> 🧠 Para administración de sistemas, `curl` es tan importante como el
> navegador.

------------------------------------------------------------------------

> 🧭 **ANTES DE EMPEZAR · Proxy directo y proxy inverso**
>
> Un proxy actúa como intermediario entre clientes y otros servicios. En un **proxy directo** el cliente utiliza el proxy para salir hacia otros destinos; en un **proxy inverso** los clientes acceden al proxy como punto de entrada hacia servidores internos.

# 🔀 9. Proxies web

Un proxy se sitúa entre cliente y servidor.

``` text
CLIENTE
   │
   ▼
┌────────┐
│ PROXY  │
└───┬────┘
    │
    ▼
SERVIDOR
```

Puede utilizarse para:

-   caché;
-   control de acceso;
-   filtrado;
-   registro;
-   salida común a Internet;
-   inspección, según configuración;
-   proxy inverso.

------------------------------------------------------------------------

> 🧭 **ANTES DE EMPEZAR · Proxy inverso**
>
> Un proxy inverso recibe peticiones de los clientes y las reenvía hacia uno o varios servidores internos. Permite separar el punto de entrada público de las aplicaciones y centralizar funciones como TLS, control de acceso o balanceo.

# 🔄 10. Proxy directo y reverse proxy

## Proxy directo

El cliente conoce el proxy:

``` text
CLIENTE
   │
   ▼
PROXY ───────► INTERNET
```

## Reverse proxy

El cliente cree comunicarse con el servicio final:

``` text
CLIENTE
   │
   ▼
REVERSE PROXY
   │
   ├────► APP 1
   ├────► APP 2
   └────► APP 3
```

Nginx y Apache pueden utilizarse en arquitecturas de reverse proxy.

------------------------------------------------------------------------

> 🧭 **ANTES DE EMPEZAR · HTTP**
>
> HTTP utiliza un modelo de **petición y respuesta**. El cliente solicita un recurso mediante una petición y el servidor devuelve una respuesta con código de estado, cabeceras y, cuando corresponde, un cuerpo. Esta estructura será la base para entender `curl`, navegadores, virtual hosts y APIs.

# 📡 11. HTTP
### 📊 Herramientas HTTP que utilizaremos

| Necesidad | Comando | Información útil |
|---|---|---|
| Petición básica | `curl http://host/` | Cuerpo de respuesta |
| Cabeceras | `curl -I http://host/` | Cabeceras de respuesta |
| Detalle de intercambio | `curl -v http://host/` | Conexión, petición y respuesta |
| Seguir redirecciones | `curl -L http://host/` | Cadena de `3xx` |
| Método concreto | `curl -X OPTIONS URL` | Método solicitado |
| Enviar datos | `curl -d 'a=b' URL` | Petición con cuerpo |
| TLS | `curl -vk https://host/` | Diagnóstico TLS en laboratorio |



**HTTP --- Hypertext Transfer Protocol** es un protocolo de aplicación
basado en un modelo petición/respuesta.

``` text
CLIENTE                         SERVIDOR

     ──────── HTTP REQUEST ─────────►
     ◄─────── HTTP RESPONSE ─────────
```

Ejemplo:

``` http
GET /index.html HTTP/1.1
Host: www.asir.test
Accept: text/html
```

Respuesta:

``` http
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 1234
```

------------------------------------------------------------------------

> 🧭 **PREPARACIÓN DIDÁCTICA**
>
> 🧭 **ANTES DE EMPEZAR · PROTOCOLO DE APLICACIÓN**
> 
> Ya conocemos TCP, UDP y puertos. Ahora subimos de nivel: HTTP define cómo un cliente formula una petición y cómo un servidor construye una respuesta. Piensa en HTTP como un formulario de solicitud y una respuesta estructurada, transportados por una conexión de red.

# 🔬 12. Funcionamiento básico de HTTP

Proceso simplificado:

``` text
1. Resolver nombre
       ↓
2. Conectar TCP
       ↓
3. [TLS si HTTPS]
       ↓
4. Enviar petición HTTP
       ↓
5. Procesar petición
       ↓
6. Generar respuesta
       ↓
7. Transferir contenido
```

Con HTTP/1.1 y versiones posteriores pueden existir conexiones
persistentes y otras optimizaciones.

------------------------------------------------------------------------

# 📨 13. Mensaje HTTP

Una petición HTTP contiene conceptualmente:

``` text
Línea inicial
Cabeceras
Línea vacía
Cuerpo opcional
```

Ejemplo:

``` http
GET /index.html HTTP/1.1
Host: www.asir.test
User-Agent: Mozilla/5.0
Accept: text/html
```

Respuesta:

``` http
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 512

<html>
...
</html>
```

------------------------------------------------------------------------

# 🔧 14. Métodos HTTP

  Método      Uso habitual
  ----------- --------------------------------------
  `GET`       Obtener recurso
  `HEAD`      Obtener cabeceras sin cuerpo
  `POST`      Enviar/procesar datos
  `PUT`       Crear/reemplazar recurso
  `PATCH`     Modificar parcialmente
  `DELETE`    Eliminar recurso
  `OPTIONS`   Consultar opciones
  `TRACE`     Diagnóstico; normalmente restringido

### GET

``` http
GET /index.html HTTP/1.1
```

### POST

``` http
POST /login HTTP/1.1
```

con datos en el cuerpo.

> ⚠️ No debe explicarse `POST` simplemente como «más seguro que GET».
>
> La seguridad depende del protocolo, transporte, aplicación, validación
> y control de acceso. HTTPS protege el transporte, no convierte
> automáticamente una aplicación en segura.

------------------------------------------------------------------------

# 📋 15. Cabeceras HTTP

Las cabeceras aportan metadatos.

Ejemplos:

``` text
Host
User-Agent
Accept
Accept-Encoding
Content-Type
Content-Length
Authorization
Cookie
Cache-Control
Location
Server
Set-Cookie
```

Ejemplo:

``` http
Host: www.asir.test
Accept: text/html
Accept-Encoding: gzip
```

------------------------------------------------------------------------

# 📦 16. Códigos de estado

Los códigos HTTP se agrupan:

``` text
1xx → información
2xx → éxito
3xx → redirección
4xx → error del cliente
5xx → error del servidor
```

Los más importantes:

    Código Significado
  -------- -----------------------
       200 OK
       201 Created
       204 No Content
       301 Moved Permanently
       302 Found
       304 Not Modified
       400 Bad Request
       401 Unauthorized
       403 Forbidden
       404 Not Found
       405 Method Not Allowed
       429 Too Many Requests
       500 Internal Server Error
       502 Bad Gateway
       503 Service Unavailable
       504 Gateway Timeout

> 🧠 Diferencia fundamental:
>
> **401** indica que falta autenticación válida.
>
> **403** indica que el servidor entiende la petición pero rechaza el
> acceso.

------------------------------------------------------------------------

# 🔁 17. Redirecciones

Una redirección puede indicar:

``` http
HTTP/1.1 301 Moved Permanently
Location: https://www.asir.test/
```

Es habitual utilizarla para:

``` text
HTTP → HTTPS
www → dominio canónico
URL antigua → URL nueva
```

Ejemplo Apache:

``` apache
Redirect permanent / https://www.asir.test/
```

------------------------------------------------------------------------

# 🗂️ 18. MIME y Content-Type

HTTP necesita indicar qué tipo de contenido se está entregando.

Ejemplos:

``` text
text/html
text/css
text/javascript
application/json
image/png
image/jpeg
application/pdf
application/zip
```

Ejemplo:

``` http
Content-Type: text/html; charset=UTF-8
```

El servidor utiliza su configuración MIME para relacionar extensiones y
tipos de contenido.

------------------------------------------------------------------------

# 🍪 19. Cookies

HTTP es fundamentalmente stateless: cada petición no tiene por qué
mantener estado de aplicación por sí misma.

Las cookies permiten asociar peticiones con información persistente del
lado del cliente.

Servidor:

``` http
Set-Cookie: sesion=abc123; Secure; HttpOnly
```

Cliente:

``` http
Cookie: sesion=abc123
```

### Atributos importantes

``` text
Secure
HttpOnly
SameSite
Domain
Path
Max-Age / Expires
```

> 🛡️ Una cookie con `HttpOnly` dificulta el acceso desde JavaScript,
> pero no sustituye otras medidas de seguridad frente a XSS, CSRF o
> secuestro de sesión.

------------------------------------------------------------------------

# 🧠 20. Caché

La caché reduce transferencias y latencia.

``` text
CLIENTE
   │
   │ petición
   ▼
CACHE
   │
   ├── HIT  → devuelve copia
   │
   └── MISS → consulta servidor
```

Cabeceras relacionadas:

``` text
Cache-Control
ETag
Last-Modified
Expires
If-None-Match
If-Modified-Since
```

Una respuesta:

``` http
304 Not Modified
```

permite al cliente reutilizar una representación almacenada cuando
corresponde.

------------------------------------------------------------------------

# 🗜️ 21. Compresión

Las respuestas pueden comprimirse para reducir el tráfico.

Cabecera típica:

``` http
Accept-Encoding: gzip, br
```

y respuesta:

``` http
Content-Encoding: gzip
```

La compresión puede reducir el tamaño de recursos textuales:

``` text
HTML
CSS
JavaScript
JSON
```

Pero hay que considerar:

-   consumo de CPU;
-   tamaño del recurso;
-   caché;
-   contenido ya comprimido.

------------------------------------------------------------------------

# 🔗 22. Conexiones persistentes

Abrir una conexión TCP tiene un coste.

Las conexiones persistentes permiten reutilizar una conexión para varias
peticiones.

``` text
TCP
 │
 ├── GET /
 ├── GET /style.css
 ├── GET /app.js
 └── GET /logo.png
```

HTTP/1.1 estableció las conexiones persistentes como comportamiento
normal, mientras que HTTP/2 y HTTP/3 introducen mecanismos más avanzados
de multiplexación y transporte.

------------------------------------------------------------------------

# ⚡ 23. HTTP/2 y HTTP/3

El estudio comienza con HTTP/1.x como base histórica y después relaciona sus conceptos con las versiones modernas de HTTP. En una infraestructura
actual conviene conocer la evolución.

``` text
HTTP/1.1
   │
   ▼
HTTP/2
   │
   ▼
HTTP/3
```

### HTTP/2

Introduce, entre otras características:

-   multiplexación;
-   compresión de cabeceras;
-   streams;
-   priorización.

### HTTP/3

Utiliza:

``` text
QUIC
 ↓
UDP
 ↓
HTTP/3
```

> 🧠 Esto no elimina la importancia de HTTP/1.1 para el aprendizaje:
> comprender petición/respuesta, cabeceras, códigos y métodos sigue
> siendo fundamental.

------------------------------------------------------------------------

# 🔐 24. Seguridad Web

Un servidor web debe proteger:

``` text
🔐 comunicación
👤 identidad
📂 recursos
🧩 aplicación
📜 logs
🖥️ sistema operativo
```

Amenazas habituales:

-   exposición accidental de ficheros;
-   permisos incorrectos;
-   credenciales transmitidas sin TLS;
-   vulnerabilidades de aplicación;
-   inyección;
-   XSS;
-   CSRF;
-   configuración insegura;
-   directorios publicados accidentalmente;
-   versiones vulnerables;
-   certificados incorrectos.

------------------------------------------------------------------------

# 🔒 25. HTTPS

HTTPS es HTTP transportado sobre TLS.

``` text
HTTP
  │
  ▼
 TLS 🔐
  │
  ▼
TCP
```

Tradicionalmente:

``` text
HTTP  → TCP/80
HTTPS → TCP/443
```

Con HTTP/3:

``` text
HTTP/3 → QUIC/UDP/443
```

------------------------------------------------------------------------

# 🧬 26. TLS

Durante el establecimiento de TLS se negocian parámetros criptográficos
y el servidor presenta un certificado.

Conceptualmente:

``` text
CLIENTE
   │
   │ ClientHello
   ▼
SERVIDOR
   │
   │ ServerHello + certificado
   ▼
CLIENTE
   │
   │ verifica certificado
   ▼
🔐 canal cifrado
```

El certificado permite vincular una identidad de servidor con una clave
pública mediante una infraestructura de confianza.

------------------------------------------------------------------------

# 📜 27. Certificados

Un certificado X.509 puede contener:

-   identidad del sujeto;
-   clave pública;
-   entidad emisora;
-   periodo de validez;
-   extensiones;
-   firma de la CA.

Un certificado de laboratorio puede ser autofirmado:

``` text
Servidor
   │
   └── firma su propio certificado
```

Pero los navegadores no lo consideran automáticamente confiable.

Para producción se utiliza una CA reconocida o una CA corporativa que
los clientes confíen explícitamente.

------------------------------------------------------------------------

> 🧭 **ANTES DE EMPEZAR · HTTPS y TLS**
>
> HTTPS es HTTP protegido mediante TLS. TLS aporta confidencialidad e integridad y permite autenticar al servidor mediante certificados. En el laboratorio utilizaremos certificados controlados y aprenderemos a distinguir un certificado válido de uno simplemente útil para hacer pruebas.

# 🧪 28. HTTPS de laboratorio
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


Para el laboratorio podemos utilizar certificados autofirmados.

``` text
/etc/ssl/
├── certs/
└── private/
```

Ejemplo:

``` bash
sudo openssl req -x509 -newkey rsa:2048 \
  -keyout /etc/ssl/private/asir.test.key \
  -out /etc/ssl/certs/asir.test.crt \
  -days 365 \
  -nodes
```

> ⚠️ Este certificado sirve para **laboratorio**.
>
> No debe utilizarse como modelo de emisión de certificados públicos.

------------------------------------------------------------------------

# 🪶 29. Apache en Ubuntu 26.04 Server

Instalación:

``` bash
sudo apt update
sudo apt install apache2
```

Comprobar:

``` bash
systemctl status apache2
```

Puerto:

``` bash
sudo ss -ltnp | grep -E ':80|:443'
```

Prueba:

``` bash
curl http://localhost/
```

Ubuntu documenta `apache2` como el servidor HTTP actual disponible
mediante APT. 

------------------------------------------------------------------------

# 🗂️ 30. Arquitectura de Apache en Ubuntu

La estructura principal:

``` text
/etc/apache2/
├── apache2.conf
├── ports.conf
├── mods-available/
├── mods-enabled/
├── conf-available/
├── conf-enabled/
├── sites-available/
└── sites-enabled/
```

La configuración está modularizada mediante enlaces simbólicos.

``` text
mods-available
      │
      │ a2enmod
      ▼
mods-enabled
```

y:

``` text
sites-available
      │
      │ a2ensite
      ▼
sites-enabled
```

Ubuntu documenta esta organización explícitamente. 

------------------------------------------------------------------------

# 🔧 31. Directivas fundamentales

En un VirtualHost:

``` apache
<VirtualHost *:80>
    ServerName www.asir.test
    ServerAlias asir.test

    DocumentRoot /srv/www/asir
</VirtualHost>
```

Las directivas principales:

``` text
Listen
ServerName
ServerAlias
DocumentRoot
DirectoryIndex
ErrorLog
CustomLog
<Directory>
```

------------------------------------------------------------------------

# 📁 32. DocumentRoot

El `DocumentRoot` indica dónde se encuentran los recursos publicados.

Ejemplo:

``` text
/srv/www/asir/
├── index.html
├── css/
├── js/
└── img/
```

Configuración:

``` apache
DocumentRoot /srv/www/asir
```

Ubuntu utiliza `/var/www/html` como DocumentRoot del sitio
predeterminado, aunque podemos crear estructuras propias como
`/srv/www/...`. 

------------------------------------------------------------------------


---

# 🗂️ Antes de las prácticas · localizar la configuración Web

Un servidor Web puede tener decenas de ficheros, pero el técnico necesita distinguir tres cosas: **configuración global, sitios publicados y logs**.

### Apache

```text
/etc/apache2/
├── apache2.conf             → configuración global
├── ports.conf               → puertos de escucha
├── sites-available/         → Virtual Hosts disponibles
├── sites-enabled/           → Virtual Hosts activados
├── mods-available/          → módulos disponibles
└── mods-enabled/            → módulos activados

/var/www/                    → contenido web habitual
/var/log/apache2/            → access.log y error.log
```

Comandos:
```bash
sudo apache2ctl configtest
sudo apache2ctl -S
sudo ss -lntp | grep -E ':80|:443'
```

### Nginx

```text
/etc/nginx/
├── nginx.conf               → configuración principal
├── sites-available/         → server blocks disponibles
└── sites-enabled/           → server blocks activados

/var/www/                    → contenido
/var/log/nginx/              → access.log y error.log
```

```bash
sudo nginx -t
sudo nginx -T
sudo ss -lntp | grep -E ':80|:443'
```

### 🖥️ Webmin

En Webmin, los módulos de **Servers → Apache Webserver** o **Servers → Nginx Webserver** permiten trabajar con parte de esta configuración. Localiza primero el Virtual Host/server block y después comprueba el fichero físico desde CLI.



> 👨‍🏫 **Criterio de corrección de las prácticas**
>
> La solución de referencia no se reduce a una configuración final. Se valoran el proceso, la capacidad para localizar ficheros, validar la sintaxis, comprobar puertos y conectividad, interpretar logs y justificar técnicamente cada decisión. Cuando el ejercicio admita varias soluciones, cualquier solución equivalente y correctamente justificada es válida.
# 🧪 33. PRÁCTICA 5.1 --- Explorar HTTP con curl
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




Desde WSL2:

``` bash
curl -I https://juandecolonia.jc
```

Después:

``` bash
curl -v https://juandecolonia.jc
```

Identifica:

``` text
versión HTTP
código de estado
Server
Content-Type
Content-Length
Location
Cache-Control
```

### Entrega

Captura una respuesta y explica cada cabecera relevante.

------------------------------------------------------------------------


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


# 🧪 34. PRÁCTICA 5.2 --- Analizar HTTP con Wireshark
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




En un laboratorio sin TLS:

``` bash
curl http://192.168.10.10/
```

Captura:

``` text
tcp.port == 80
```

Identifica:

``` text
GET
Host
User-Agent
HTTP/1.1 200 OK
Content-Type
```

### Pregunta

¿Por qué no podemos aplicar exactamente el mismo análisis al contenido
de HTTPS?

------------------------------------------------------------------------


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


# 🧪 35. PRÁCTICA 5.3 --- Instalación y configuración básica de Apache
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




Instala:

``` bash
sudo apt update
sudo apt install apache2
```

Comprueba:

``` bash
systemctl status apache2
```

Abre:

``` text
http://IP_DEL_SERVIDOR/
```

Comprueba:

``` bash
curl -I http://localhost/
```

Consulta:

``` bash
ls -la /var/www/html/
```

### Evidencias

``` text
✔ servicio activo
✔ puerto 80
✔ página inicial
✔ respuesta HTTP
```

------------------------------------------------------------------------


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


# 🧪 36. PRÁCTICA 5.4 --- Primera web
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

``` bash
sudo mkdir -p /srv/www/asir
```

Página:

``` bash
sudo nano /srv/www/asir/index.html
```

Contenido:

``` html
<!doctype html>
<html lang="es">
<head>
    <meta charset="utf-8">
    <title>ASIR · UT5</title>
</head>
<body>
    <h1>🌐 Servidor Web ASIR</h1>
    <p>Esta página procede de Apache.</p>
</body>
</html>
```

Configura un VirtualHost:

``` bash
sudo nano /etc/apache2/sites-available/asir.test.conf
```

``` apache
<VirtualHost *:80>
    ServerName asir.test
    DocumentRoot /srv/www/asir

    <Directory /srv/www/asir>
        Require all granted
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/asir_error.log
    CustomLog ${APACHE_LOG_DIR}/asir_access.log combined
</VirtualHost>
```

Activa:

``` bash
sudo a2ensite asir.test.conf
```

Desactiva, si procede:

``` bash
sudo a2dissite 000-default.conf
```

Comprueba:

``` bash
sudo apache2ctl configtest
```

Recarga:

``` bash
sudo systemctl reload apache2
```

------------------------------------------------------------------------


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


# 🧪 37. PRÁCTICA 5.5 --- DNS + VirtualHost
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




Utiliza la UT3.

Crea:

``` text
www.asir.test
```

y:

``` text
www.daw.test
```

Ambos deben resolver a:

``` text
192.168.10.10
```

Apache:

``` text
www.asir.test → /srv/www/asir
www.daw.test  → /srv/www/daw
```

Prueba:

``` bash
curl http://www.asir.test/
curl http://www.daw.test/
```

### Objetivo

Demostrar que:

``` text
DNS
 +
Host:
 +
VirtualHost
```

permiten servir sitios diferentes desde una misma IP.

Apache documenta los Virtual Hosts basados en nombre como una forma de
alojar varios sitios sobre una misma dirección IP.


------------------------------------------------------------------------


### 🧭 Guía de resolución y comprobación

Esta práctica se considera resuelta cuando puedes **explicar y demostrar** el resultado, no solo cuando el comando termina sin errores. Sigue siempre esta secuencia:

1. **Identifica el estado inicial.** Anota interfaces, direcciones, rutas y servicios que ya estaban activos.
2. **Aplica el cambio mínimo.** No modifiques varias cosas a la vez: si algo falla, necesitas saber qué cambio lo provocó.
3. **Valida inmediatamente.** Comprueba la sintaxis o el estado del servicio antes de probar desde el cliente.
4. **Prueba desde el punto de vista del usuario.** Una configuración correcta debe producir el comportamiento esperado desde el cliente, no solo desde el servidor.
5. **Observa evidencias.** Conserva la salida de comandos, logs, capturas de tráfico y capturas de pantalla que demuestren el resultado.

**Comandos de referencia para esta práctica:**

- `resolvectl status`
- `dig @<DNS> <nombre>`
- `sudo named-checkconf`
- `sudo named-checkzone <zona> <fichero>`
- `sudo journalctl -u bind9 --no-pager`

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


# 🧪 38. PRÁCTICA 5.6 --- Virtual Hosts y `Host`
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




Utiliza:

``` bash
curl -H 'Host: www.asir.test' http://192.168.10.10/
```

Después:

``` bash
curl -H 'Host: www.daw.test' http://192.168.10.10/
```

Observa cómo el mismo:

``` text
IP = 192.168.10.10
```

produce dos respuestas diferentes.

### Diagnóstico Apache

``` bash
sudo apachectl -S
```

Este comando permite inspeccionar cómo Apache interpreta los Virtual
Hosts. 

------------------------------------------------------------------------


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


# 🧪 39. PRÁCTICA 5.7 --- Módulos Apache
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




Lista módulos:

``` bash
apache2ctl -M
```

Lista módulos disponibles:

``` bash
ls /etc/apache2/mods-available/
```

Activa:

``` bash
sudo a2enmod rewrite
```

Comprueba:

``` bash
apache2ctl -M | grep rewrite
```

Desactiva:

``` bash
sudo a2dismod rewrite
```

Comprueba la configuración:

``` bash
sudo apache2ctl configtest
```

Ubuntu proporciona `a2enmod` y `a2dismod` para administrar módulos
dinámicos. 

------------------------------------------------------------------------


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


# 🧪 40. PRÁCTICA 5.8 --- Redirección HTTP → HTTPS
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

``` text
http://www.asir.test
       │
       │ 301
       ▼
https://www.asir.test
```

Apache:

``` apache
<VirtualHost *:80>
    ServerName www.asir.test
    Redirect permanent / https://www.asir.test/
</VirtualHost>
```

Comprueba:

``` bash
curl -I http://www.asir.test/
```

Debe aparecer un código de redirección y una cabecera:

``` text
Location:
```

------------------------------------------------------------------------


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


# 🧪 41. PRÁCTICA 5.9 --- HTTPS con certificado de laboratorio
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




Activa SSL:

``` bash
sudo a2enmod ssl
```

Activa el sitio SSL:

``` bash
sudo a2ensite default-ssl
```

Comprueba:

``` bash
sudo apache2ctl configtest
```

Reinicia/recarga:

``` bash
sudo systemctl reload apache2
```

Prueba:

``` bash
curl -k https://localhost/
```

El módulo `mod_ssl` proporciona HTTPS en Apache; Ubuntu documenta
también el VirtualHost SSL predeterminado. 

------------------------------------------------------------------------


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


# 🧪 42. PRÁCTICA 5.10 --- Certificado autofirmado personalizado
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




Genera:

``` bash
sudo openssl req -x509 -newkey rsa:2048 \
  -keyout /etc/ssl/private/asir.test.key \
  -out /etc/ssl/certs/asir.test.crt \
  -days 365 \
  -nodes
```

Configura:

``` apache
<VirtualHost *:443>
    ServerName asir.test
    DocumentRoot /srv/www/asir

    SSLEngine on
    SSLCertificateFile /etc/ssl/certs/asir.test.crt
    SSLCertificateKeyFile /etc/ssl/private/asir.test.key

    <Directory /srv/www/asir>
        Require all granted
    </Directory>
</VirtualHost>
```

Prueba:

``` bash
sudo apache2ctl configtest
sudo systemctl reload apache2
curl -k https://asir.test/
```

### Analiza el certificado

``` bash
openssl s_client -connect asir.test:443 -servername asir.test
```

------------------------------------------------------------------------


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


# 🧪 43. PRÁCTICA 5.11 --- Autenticación básica
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




Activa:

``` bash
sudo a2enmod auth_basic
```

Crea directorio:

``` bash
sudo mkdir -p /srv/www/privado
```

Crea fichero de contraseñas:

``` bash
sudo htpasswd -c /etc/apache2/.htpasswd alumno
```

Configura:

``` apache
<Directory /srv/www/privado>
    AuthType Basic
    AuthName "Zona ASIR"
    AuthUserFile /etc/apache2/.htpasswd
    Require valid-user
</Directory>
```

Comprueba:

``` bash
curl -u alumno:CONTRASEÑA http://asir.test/privado/
```

> ⚠️ Basic Authentication sin HTTPS no protege adecuadamente las
> credenciales frente a un observador de red. Utilízala en el
> laboratorio para comprender el mecanismo y combínala con HTTPS.

------------------------------------------------------------------------


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


# 🧪 44. PRÁCTICA 5.12 --- Control de acceso
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




Estudia:

``` apache
Require all granted
```

frente a:

``` apache
Require all denied
```

y:

``` apache
Require ip 192.168.10.0/24
```

Construye:

``` text
PUBLICO
  │
  └── acceso general

PRIVADO
  │
  └── solo 192.168.10.0/24
```

Prueba desde:

-   servidor;
-   WSL2;
-   otra VM.

------------------------------------------------------------------------


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


# 🧪 45. PRÁCTICA 5.13 --- Logs
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




Apache registra por defecto:

``` text
/var/log/apache2/access.log
/var/log/apache2/error.log
```

Ubuntu documenta `CustomLog` y `ErrorLog` para controlar estos
registros. 

Observa:

``` bash
sudo tail -f /var/log/apache2/access.log
```

En otra terminal:

``` bash
curl http://localhost/
```

Comprueba:

``` bash
sudo tail -f /var/log/apache2/error.log
```

### Analiza

-   IP origen;
-   fecha;
-   método;
-   URL;
-   código;
-   tamaño;
-   User-Agent.

------------------------------------------------------------------------


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


# 🧪 46. PRÁCTICA 5.14 --- Diagnóstico de errores HTTP
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




Provoca:

``` text
404
403
401
500
```

Para cada uno documenta:

``` text
Petición
   ↓
Código HTTP
   ↓
Log
   ↓
Causa
   ↓
Corrección
```

### Herramientas

``` bash
curl -I
curl -v
apachectl -S
apache2ctl -M
journalctl -u apache2
tail /var/log/apache2/*
```

------------------------------------------------------------------------


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


# 🧪 47. PRÁCTICA 5.15 --- Monitorización con `ss`, `curl` y `tcpdump`
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

``` bash
sudo ss -ltnp | grep apache
```

Captura:

``` bash
sudo tcpdump -ni any port 80
```

En otra terminal:

``` bash
curl http://localhost/
```

Observa:

``` text
TCP handshake
HTTP request
HTTP response
TCP close / reutilización
```

------------------------------------------------------------------------


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


# 🧪 48. PRÁCTICA 5.16 --- HTTP con Wireshark
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

``` text
tcp.port == 80
```

Busca:

``` text
GET
HTTP/1.1
Host
User-Agent
200 OK
Content-Type
```

Utiliza:

``` text
Follow → TCP Stream
```

### Después repite con HTTPS

Filtro:

``` text
tcp.port == 443
```

Compara:

``` text
HTTP
   → contenido visible

HTTPS
   → contenido HTTP protegido por TLS
```

------------------------------------------------------------------------


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


# 🧪 49. PRÁCTICA 5.17 --- Proxy web conceptual
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

``` text
WSL2
  │
  ▼
PROXY
  │
  ▼
WEB SERVER
```

Investiga y documenta:

-   proxy directo;
-   reverse proxy;
-   caché;
-   ACL;
-   logs.

Para la práctica principal puedes utilizar **Squid** como proxy
explícito:

``` bash
sudo apt install squid
```

> ⚠️ Squid es una tecnología complementaria al capítulo. El objetivo
> aquí es comprender el papel de un proxy, no convertir esta UT en una
> unidad de administración de Squid.

------------------------------------------------------------------------


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


# 🧪 50. PRÁCTICA 5.18 --- Reverse proxy con Nginx
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




Instala:

``` bash
sudo apt install nginx
```

Arquitectura:

``` text
CLIENTE
   │
   ▼
NGINX :80
   │
   ▼
APACHE :8080
```

Configura Apache para escuchar en:

``` text
8080
```

Y Nginx:

``` nginx
server {
    listen 80;
    server_name app.asir.test;

    location / {
        proxy_pass http://127.0.0.1:8080;
    }
}
```

Comprueba:

``` bash
curl -I http://app.asir.test/
```

### Objetivo

Distinguir:

``` text
servidor web
     ≠
reverse proxy
```

------------------------------------------------------------------------


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


# 🧪 51. PRÁCTICA 5.19 --- Apache + aplicación
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




Monta:

``` text
Navegador
    │
    ▼
Apache
    │
    ▼
Aplicación
    │
    ▼
Datos
```

Puedes utilizar una aplicación sencilla en Python:

``` bash
python3 -m http.server 9000
```

Apache/Nginx actuará como reverse proxy.

Comprueba:

``` text
Cliente → proxy → aplicación
```

### Reto

Añade una segunda aplicación:

``` text
/app1 → 127.0.0.1:9000
/app2 → 127.0.0.1:9001
```

------------------------------------------------------------------------


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


# 🧪 52. PRÁCTICA 5.20 --- Alojamiento virtual completo
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

``` text
                 DNS
                  │
        ┌─────────┴─────────┐
        │                   │
   www.asir.test       www.daw.test
        │                   │
        └─────────┬─────────┘
                  │
             192.168.10.10
                  │
                Apache
             ┌────┴────┐
             │         │
          /asir       /daw
```

Cada sitio debe tener:

``` text
index.html
CSS
favicon
logs independientes
```

Utiliza:

``` apache
ServerName
ServerAlias
DocumentRoot
CustomLog
ErrorLog
```

------------------------------------------------------------------------


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


# 🧪 53. PRÁCTICA 5.21 --- HTTPS para varios sitios
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

``` text
www.asir.test → HTTPS
www.daw.test  → HTTPS
```

Con:

``` text
SNI
```

Cada sitio tendrá un certificado apropiado.

``` text
CLIENTE
   │
   │ TLS ClientHello + SNI
   ▼
APACHE
   │
   ├── asir.test → certificado ASIR
   └── daw.test  → certificado DAW
```

Apache y OpenSSL actuales soportan Virtual Hosts basados en nombre con
SNI. La selección del VirtualHost SSL utiliza el nombre indicado durante
el handshake TLS cuando está disponible.


------------------------------------------------------------------------


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


# 🌍 54. PRÁCTICA 5.22 --- Certificado de confianza
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




Compara:

``` text
certificado autofirmado
```

con:

``` text
certificado emitido por una CA
```

Para una infraestructura pública actual, estudia ACME y Let's Encrypt.

Ubuntu documenta Certbot como cliente ACME recomendado para obtener
certificados de Let's Encrypt. 

Ejemplo conceptual:

Instala Certbot y el plugin de Apache:

``` bash
sudo apt install certbot python3-certbot-apache
```

Después:

``` bash
sudo certbot --apache -d www.ejemplo.es
```

> ⚠️ No ejecutes esta práctica contra un dominio público sin
> autorización. En laboratorio utiliza una CA propia o certificados de
> prueba.

------------------------------------------------------------------------

# 🧪 55. PRÁCTICA 5.23 --- Apache frente a Nginx
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




Instala ambos, pero evita conflictos de puerto.

Escenario:

``` text
Apache → 8080
Nginx  → 80
```

Compara:

  Característica                  Apache                             Nginx
  ------------------------------- ---------------------------------- ----------------------
  Modelo                          multiproceso/multihilo según MPM   orientado a eventos
  Virtual Hosts / server blocks   Sí                                 Sí
  Módulos                         Muy amplio                         Arquitectura modular
  Reverse proxy                   Sí                                 Sí
  Servir estático                 Sí                                 Sí
  HTTPS                           Sí                                 Sí
  Configuración Ubuntu            `/etc/apache2`                     `/etc/nginx`

### Reto

Explica qué servidor utilizarías en:

``` text
A. sitio estático
B. reverse proxy
C. aplicación PHP
D. infraestructura heterogénea
```

No existe una respuesta universal: debe justificarse según los
requisitos.

------------------------------------------------------------------------


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


# 🧪 56. PRÁCTICA 5.24 --- Seguridad de configuración
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




Realiza una auditoría:

``` text
☐ ¿Está activo HTTP?
☐ ¿Está activo HTTPS?
☐ ¿Hay redirección?
☐ ¿El certificado es válido?
☐ ¿Se expone información innecesaria?
☐ ¿Los permisos son correctos?
☐ ¿Hay directorios listables?
☐ ¿Se protegen zonas privadas?
☐ ¿Se registran accesos?
☐ ¿Se revisan errores?
☐ ¿Los módulos innecesarios están desactivados?
☐ ¿El software está actualizado?
```

------------------------------------------------------------------------


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


# 🔍 57. Diagnóstico sistemático

Cuando una web no funciona:

``` text
                   ❌ WEB NO FUNCIONA
                           │
                           ▼
                     ¿DNS resuelve?
                       /       \
                     NO         SÍ
                     │           │
                    DNS          ▼
                           ¿Conectividad?
                            /          \
                          NO            SÍ
                          │              │
                       routing           ▼
                                 ¿Puerto abierto?
                                  /          \
                                NO            SÍ
                                │              │
                            firewall           ▼
                                      ¿Apache activo?
                                       /         \
                                     NO           SÍ
                                     │             │
                                  systemd           ▼
                                             ¿VirtualHost?
                                              /       \
                                            NO         SÍ
                                            │           │
                                        Apachectl -S    ▼
                                                   ¿TLS?
                                                    /  \
                                                  NO    SÍ
                                                  │      │
                                               cert     logs
```

------------------------------------------------------------------------

# 🧰 58. Herramientas de diagnóstico

### DNS

``` bash
dig www.asir.test
```

### Conectividad

``` bash
ping 192.168.10.10
```

### Puertos

``` bash
nc -vz 192.168.10.10 80
nc -vz 192.168.10.10 443
```

### HTTP

``` bash
curl -I http://www.asir.test/
curl -v http://www.asir.test/
```

### TLS

``` bash
openssl s_client \
  -connect www.asir.test:443 \
  -servername www.asir.test
```

### Apache

``` bash
apache2ctl configtest
apachectl -S
apache2ctl -M
```

### Servicio

``` bash
systemctl status apache2
journalctl -u apache2
```

### Logs

``` bash
tail -f /var/log/apache2/access.log
tail -f /var/log/apache2/error.log
```

------------------------------------------------------------------------

# 🧪 59. Caso de diagnóstico integral
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


Un usuario indica:

> «`www.asir.test` no funciona.»

La resolución DNS:

``` bash
dig www.asir.test
```

devuelve:

``` text
192.168.10.10
```

Pero:

``` bash
curl http://www.asir.test/
```

devuelve:

``` text
503 Service Unavailable
```

Debes investigar:

``` text
1. DNS
2. TCP
3. Apache
4. VirtualHost
5. reverse proxy
6. aplicación
7. logs
```

### Evidencias mínimas

``` bash
dig
ss
curl -v
apachectl -S
systemctl status apache2
journalctl -u apache2
tail /var/log/apache2/error.log
```

------------------------------------------------------------------------

# 🧠 60. Arquitectura completa

Relaciona las UT anteriores:

``` text
                    🌐 CLIENTE
                         │
                         ▼
                       DNS
                         │
                         ▼
                   IP del servidor
                         │
                         ▼
                       TCP
                         │
                 ┌───────┴───────┐
                 │               │
               HTTP            HTTPS
                80               443
                 │               │
                 │              TLS
                 │               │
                 └───────┬───────┘
                         ▼
                     APACHE
                         │
               ┌─────────┼─────────┐
               │         │         │
            sitio 1    sitio 2   proxy
               │         │         │
               └─────────┴────┬────┘
                              │
                         aplicación
                              │
                              ▼
                              BD
```

------------------------------------------------------------------------

# 🧪 61. PRÁCTICA FINAL --- «Publica dos sitios seguros»
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




Construye en:

``` text
VirtualBox + Ubuntu 26.04 Server
```

con un cliente:

``` text
WSL2 + Ubuntu 26.04
```

## Infraestructura

``` text
WSL2
 │
 │ DNS / HTTP / HTTPS
 ▼
Ubuntu Server
 │
 ├── Apache
 │
 ├── www.asir.test
 │
 └── www.sri.test
```

## Requisitos

### DNS

``` text
www.asir.test → 192.168.10.10
www.sri.test  → 192.168.10.10
```

### Web

``` text
www.asir.test → /srv/www/asir
www.sri.test  → /srv/www/sri
```

### HTTPS

Ambos sitios:

``` text
TCP/443
TLS
SNI
```

### Seguridad

-   HTTP redirige a HTTPS.
-   Zona `/privado` protegida.
-   Permisos mínimos.
-   Logs independientes.
-   Módulos innecesarios desactivados.

### Diagnóstico

Debes demostrar:

``` text
dig
curl
openssl s_client
apachectl -S
ss
journalctl
Wireshark
```

------------------------------------------------------------------------


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


# 🏆 62. Reto profesional

Una empresa solicita:

``` text
                 INTERNET
                     │
                  FIREWALL
                     │
                REVERSE PROXY
                     │
          ┌──────────┼──────────┐
          │          │          │
        WEB 1      WEB 2      APP
          │          │          │
        HTTPS      HTTPS      HTTPS
```

Requisitos:

1.  Dos sitios web.
2.  Un único servidor físico/virtual.
3.  DNS.
4.  HTTPS.
5.  Redirección HTTP → HTTPS.
6.  Autenticación para una zona privada.
7.  Logs.
8.  Monitorización.
9.  Reverse proxy.
10. Diagnóstico documentado.

### Entrega

``` text
01-arquitectura.md
02-dns.md
03-apache.md
04-https.md
05-proxy.md
06-seguridad.md
07-pruebas.md
08-diagnostico.md
```

------------------------------------------------------------------------

# 📊 63. Comparativa de protocolos Web

  Tecnología   Transporte habitual         Puerto Cifrado       Uso
  ------------ ------------------------- -------- ------------- ----------------
  HTTP/1.1     TCP                             80 ❌            Web sin TLS
  HTTPS        TCP + TLS                      443 ✅            Web segura
  HTTP/2       TCP + TLS habitualmente        443 ✅ habitual   Web moderna
  HTTP/3       QUIC/UDP                       443 ✅            Web sobre QUIC

> ⚠️ No debe enseñarse «HTTP/2 = TCP/443» como una equivalencia
> absoluta: HTTP/2 está definido sobre un transporte fiable y puede
> funcionar sobre HTTP sin TLS en ciertos escenarios, aunque en la Web
> pública se utiliza predominantemente con TLS.

------------------------------------------------------------------------

# 📚 64. Apache: estructura mental

``` text
/etc/apache2/
│
├── apache2.conf       ← configuración global
├── ports.conf         ← puertos
│
├── mods-available/    ← módulos disponibles
├── mods-enabled/      ← módulos activos
│
├── conf-available/    ← configuraciones disponibles
├── conf-enabled/      ← configuraciones activas
│
├── sites-available/   ← sitios disponibles
└── sites-enabled/     ← sitios activos
```

Herramientas:

``` text
a2enmod    → activar módulo
a2dismod   → desactivar módulo

a2ensite   → activar sitio
a2dissite  → desactivar sitio

apachectl -S       → VirtualHosts
apache2ctl -M      → módulos
apache2ctl configtest → sintaxis
```

Ubuntu documenta estas utilidades y la organización modular de Apache.


------------------------------------------------------------------------

# 🔐 65. HTTPS y producción

Para un laboratorio:

``` text
certificado autofirmado
```

Para una infraestructura pública:

``` text
DNS
 ↓
dominio real
 ↓
CA / ACME
 ↓
certificado válido
 ↓
HTTPS
```

Ubuntu documenta Certbot y los plugins para Apache y Nginx como
mecanismos para obtener y configurar certificados ACME.


### No confundir

``` text
HTTPS
  ≠
aplicación segura
```

HTTPS protege el canal.

La aplicación sigue necesitando:

``` text
validación
autorización
gestión de sesiones
protección contra XSS
protección contra CSRF
consultas seguras
actualizaciones
```

------------------------------------------------------------------------

# 🧠 66. Resumen

``` text
                       🌐 WEB
                         │
             ┌───────────┼───────────┐
             │           │           │
            URL         HTTP        TLS
             │           │           │
             │      ┌────┴────┐      │
             │      │         │      │
             │    request   response │
             │      │         │      │
             └──────┼─────────┼──────┘
                    │
                 Apache
                    │
          ┌─────────┼─────────┐
          │         │         │
       sitio A    sitio B    proxy
          │         │         │
          └─────────┴─────────┘
```

Ideas fundamentales:

1.  La Web es un servicio construido sobre Internet.
2.  HTTP utiliza un modelo petición/respuesta.
3.  URI y URL permiten identificar/localizar recursos.
4.  Los métodos HTTP expresan diferentes operaciones.
5.  Las cabeceras transportan metadatos.
6.  Los códigos 2xx, 3xx, 4xx y 5xx representan categorías de respuesta.
7.  MIME informa sobre el tipo de contenido.
8.  Las cookies permiten mantener estado entre peticiones.
9.  La caché reduce latencia y tráfico.
10. HTTPS utiliza TLS para proteger HTTP.
11. Un certificado no hace segura por sí mismo una aplicación.
12. Apache es modular.
13. Ubuntu organiza Apache mediante `mods-*`, `conf-*` y `sites-*`.
14. Los Virtual Hosts permiten alojar varios sitios en un servidor.
15. El alojamiento basado en nombres permite compartir una IP.
16. SNI permite seleccionar el sitio/certificado durante TLS.
17. Los logs son fundamentales para diagnóstico y auditoría.
18. `curl`, `openssl`, `ss`, `tcpdump` y Wireshark permiten observar el
    funcionamiento real.
19. Un reverse proxy puede separar el acceso público de las
    aplicaciones.
20. Nginx y Apache pueden desempeñar funciones de servidor y proxy,
    según configuración.

------------------------------------------------------------------------

# ❓ 67. Autoevaluación

1.  ¿Qué diferencia existe entre Internet y la Web?
2.  ¿Qué papel desempeña HTTP?
3.  ¿Qué diferencia existe entre URI y URL?
4.  ¿Qué diferencia existe entre página, sitio y aplicación web?
5.  ¿Qué es un servidor web?
6.  ¿Qué diferencia existe entre proxy directo y reverse proxy?
7.  ¿Qué estructura básica tiene una petición HTTP?
8.  ¿Qué estructura básica tiene una respuesta HTTP?
9.  ¿Qué función tiene la cabecera `Host`?
10. ¿Qué diferencias fundamentales existen entre GET y POST?
11. ¿Qué significan las familias 2xx, 3xx, 4xx y 5xx?
12. ¿Qué diferencia existe entre 401 y 403?
13. ¿Qué función tiene `Content-Type`?
14. ¿Qué es una cookie?
15. ¿Qué mecanismos HTTP participan en la caché?
16. ¿Qué es una conexión persistente?
17. ¿Qué diferencia existe entre HTTP y HTTPS?
18. ¿Qué función desempeña TLS?
19. ¿Qué información aporta un certificado digital?
20. ¿Qué es un Virtual Host?
21. ¿Qué diferencia existe entre VirtualHost basado en IP y basado en
    nombre?
22. ¿Qué función tiene `ServerName`?
23. ¿Qué función tiene `DocumentRoot`?
24. ¿Qué hacen `a2enmod` y `a2dismod`?
25. ¿Qué hacen `a2ensite` y `a2dissite`?
26. ¿Qué utilidad tiene `apachectl -S`?
27. ¿Dónde se encuentran habitualmente los logs de Apache en Ubuntu?
28. ¿Qué herramientas utilizarías para diagnosticar un error HTTP?
29. ¿Qué ventaja aporta SNI?
30. ¿Por qué HTTPS no garantiza que una aplicación web sea segura?

------------------------------------------------------------------------

# ✅ 68. Solucionario de la autoevaluación

### 1. Internet y Web

Internet es la infraestructura mundial de redes interconectadas. La Web
es un servicio distribuido que funciona sobre esa infraestructura.

### 2. HTTP

HTTP permite que un cliente solicite recursos o realice operaciones y
que un servidor responda.

### 3. URI y URL

URI identifica un recurso. URL es un tipo de URI que proporciona
información para localizarlo mediante un mecanismo de acceso.

### 4. Página, sitio y aplicación

Una página es un recurso concreto. Un sitio agrupa recursos
relacionados. Una aplicación web incorpora lógica de aplicación y
normalmente procesamiento dinámico.

### 5. Servidor web

Es un software que acepta peticiones HTTP/HTTPS y devuelve recursos o
respuestas generadas dinámicamente.

### 6. Proxy y reverse proxy

Un proxy directo actúa en nombre del cliente. Un reverse proxy se sitúa
delante de los servidores de backend y recibe las peticiones de los
clientes.

### 7. Petición HTTP

Incluye línea inicial, cabeceras, línea vacía y un cuerpo opcional.

### 8. Respuesta HTTP

Incluye línea de estado, cabeceras, línea vacía y cuerpo opcional.

### 9. Host

Permite indicar el nombre del recurso/servidor solicitado y es
fundamental para el alojamiento virtual basado en nombres.

### 10. GET y POST

GET se utiliza habitualmente para recuperar recursos. POST permite
enviar datos al servidor para que sean procesados. La diferencia no debe
reducirse a «GET seguro y POST inseguro».

### 11. Familias de códigos

``` text
2xx → éxito
3xx → redirección
4xx → problema asociado a la petición/cliente
5xx → problema en el procesamiento del servidor
```

### 12. 401 y 403

401 indica que se requiere una autenticación válida. 403 indica que el
acceso está prohibido aunque la petición pueda estar correctamente
formada.

### 13. Content-Type

Indica el tipo de representación que contiene el mensaje.

### 14. Cookie

Es información que el servidor puede solicitar al cliente que almacene y
que este puede devolver posteriormente para mantener estado o
preferencias.

### 15. Caché

Participan mecanismos como:

``` text
Cache-Control
ETag
Last-Modified
Expires
If-None-Match
If-Modified-Since
```

### 16. Conexión persistente

Permite reutilizar una conexión para varias peticiones/respuestas,
reduciendo el coste de establecer conexiones repetidamente.

### 17. HTTP y HTTPS

HTTPS protege HTTP mediante TLS, proporcionando confidencialidad e
integridad del canal y autenticación del servidor mediante certificados
cuando la validación es correcta.

### 18. TLS

Proporciona un canal criptográficamente protegido y negocia mecanismos
de autenticación, cifrado e integridad.

### 19. Certificado

Asocia una identidad con una clave pública y contiene información
firmada por una autoridad certificadora o por el propio emisor si es
autofirmado.

### 20. Virtual Host

Permite que un mismo servidor atienda diferentes sitios mediante
configuraciones diferenciadas.

### 21. IP frente a nombre

El Virtual Host basado en IP distingue sitios mediante diferentes
direcciones IP. El basado en nombre puede compartir una misma IP y
utilizar el nombre solicitado para seleccionar el sitio.

### 22. ServerName

Define el nombre principal al que responde un Virtual Host.

### 23. DocumentRoot

Define el directorio desde el que Apache sirve los recursos del sitio.

### 24. a2enmod / a2dismod

Activan y desactivan módulos Apache.

### 25. a2ensite / a2dissite

Activan y desactivan sitios o Virtual Hosts.

### 26. apachectl -S

Muestra cómo Apache ha interpretado la configuración de Virtual Hosts.

### 27. Logs

Habitualmente:

``` text
/var/log/apache2/access.log
/var/log/apache2/error.log
```

aunque cada Virtual Host puede definir sus propios logs.

### 28. Diagnóstico

Una combinación razonable:

``` text
dig
ping
nc
ss
curl
openssl s_client
apachectl -S
apache2ctl -M
journalctl
logs
tcpdump
Wireshark
```

### 29. SNI

Permite que el cliente indique el nombre solicitado durante el handshake
TLS, facilitando la selección del Virtual Host y del certificado
correspondiente.

### 30. HTTPS no equivale a aplicación segura

HTTPS protege la comunicación entre extremos, pero no corrige
vulnerabilidades de la aplicación, autenticación, autorización,
sesiones, validación de datos o lógica de negocio.

------------------------------------------------------------------------

# 📝 69. Test de repaso

### 1. ¿Qué protocolo utiliza el navegador para solicitar recursos web?

a)  FTP\
b)  HTTP\
c)  DHCP\
d)  DNS

### 2. El puerto tradicional de HTTP es:

a)  21\
b)  22\
c)  80\
d)  443

### 3. HTTPS utiliza habitualmente:

a)  TCP/21\
b)  TCP/53\
c)  TCP/80\
d)  TCP/443

### 4. ¿Qué método se utiliza habitualmente para recuperar un recurso?

a)  GET\
b)  POST\
c)  DELETE\
d)  PATCH

### 5. ¿Qué código indica normalmente que un recurso no existe?

a)  200\
b)  301\
c)  404\
d)  500

### 6. ¿Qué cabecera identifica el host solicitado en HTTP/1.1?

a)  Content-Type\
b)  Host\
c)  Location\
d)  Server

### 7. ¿Qué directiva Apache define el directorio de los recursos del sitio?

a)  ServerAlias\
b)  Listen\
c)  DocumentRoot\
d)  ErrorDocument

### 8. ¿Qué comando activa un Virtual Host en Ubuntu?

a)  `a2ensite`\
b)  `a2enable`\
c)  `apache-enable-site`\
d)  `site2enable`

### 9. ¿Qué comando permite inspeccionar los Virtual Hosts interpretados por

Apache?

a)  `apachectl -S`\
b)  `apachectl -P`\
c)  `apachectl -VHOST`\
d)  `a2list`

### 10. ¿Qué mecanismo permite seleccionar un certificado según el nombre

solicitado durante TLS?

a)  MIME\
b)  SNI\
c)  FTP\
d)  DHCP

### 11. ¿Qué código indica normalmente una redirección permanente?

a)  200\
b)  301\
c)  401\
d)  503

### 12. ¿Qué cabecera indica el tipo MIME de una respuesta?

a)  Host\
b)  Server\
c)  Content-Type\
d)  Location

### 13. ¿Qué componente permite proteger HTTP mediante TLS?

a)  HTTPS\
b)  FTP\
c)  TFTP\
d)  DHCP

### 14. ¿Qué utilidad es especialmente apropiada para consultar una respuesta

HTTP desde terminal?

a)  `dig`\
b)  `curl`\
c)  `ip`\
d)  `ss`

### 15. ¿Qué diferencia principal existe entre proxy directo y reverse proxy?

a)  El protocolo utilizado.\
b)  La dirección IP utilizada.\
c)  El lado de la comunicación en cuyo nombre actúa el proxy.\
d)  El puerto de HTTP.

------------------------------------------------------------------------

# ✅ 70. Respuestas del test

    Nº  Respuesta
  ---- -----------
     1    **b**
     2    **c**
     3    **d**
     4    **a**
     5    **c**
     6    **b**
     7    **c**
     8    **a**
     9    **a**
    10    **b**
    11    **b**
    12    **c**
    13    **a**
    14    **b**
    15    **c**

------------------------------------------------------------------------


# 🧱 72. Evolución tecnológica

``` text
                 CAPÍTULO ORIGINAL
                        │
       ┌────────────────┼─────────────────┐
       │                │                 │
   Apache 2.2         IIS 7.5          Zentyal
       │                │                 │
       └────────────────┼─────────────────┘
                        ▼
                 UT5 ACTUALIZADA
                        │
       ┌────────────────┼─────────────────┐
       │                │                 │
 Apache 2.4         Nginx             OpenSSL
 Ubuntu 26.04       reverse proxy     TLS
       │                │                 │
       └────────────────┼─────────────────┘
                        ▼
                🧪 LABORATORIO ASIR
                        │
        ┌───────────────┼────────────────┐
        │               │                │
      WSL2          VirtualBox       Packet Tracer
    cliente        Ubuntu Server      red/simulación
```

La configuración moderna de Apache en Ubuntu se apoya en módulos,
Virtual Hosts y ficheros separados para sitios y configuraciones.


------------------------------------------------------------------------

# 🏁 73. Resultado esperado

Al finalizar la UT5, el alumno debería poder enfrentarse a:

> **«Tengo un Ubuntu Server con una IP y necesito publicar dos sitios,
> protegerlos con HTTPS, autenticar una zona privada, registrar accesos
> y diagnosticar cualquier fallo.»**

La solución no debe comenzar por:

``` text
sudo apt install apache2
```

sino por:

``` text
REQUISITOS
    ↓
DNS
    ↓
RED
    ↓
PROTOCOLO
    ↓
SERVIDOR
    ↓
VIRTUAL HOSTS
    ↓
PERMISOS
    ↓
HTTPS
    ↓
AUTENTICACIÓN
    ↓
LOGS
    ↓
MONITORIZACIÓN
    ↓
PRUEBAS
    ↓
DIAGNÓSTICO
```

------------------------------------------------------------------------

