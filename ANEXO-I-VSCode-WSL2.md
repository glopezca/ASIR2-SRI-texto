# 🧰 ANEXO I · Visual Studio Code + WSL2 para administración de servicios

> 🧭 **ANTES DE EMPEZAR · VOCABULARIO TÉCNICO**
>
> Las siglas, abreviaturas y conceptos técnicos que van a aparecer en esta unidad se presentan aquí antes de su desarrollo. La explicación local de cada tema podrá ampliar estas definiciones cuando sea necesario.
>
> **CFGS** — Ciclo Formativo de Grado Superior.
> **ASIR** — Administración de Sistemas Informáticos en Red.
> **WSL** — Windows Subsystem for Linux, plataforma de Windows para ejecutar entornos Linux.
> **WSL2** — Windows Subsystem for Linux 2: tecnología de Windows que ejecuta un entorno Linux mediante una máquina virtual ligera.
> **VS Code** — Visual Studio Code, editor de código extensible con terminal y herramientas de desarrollo.
> **YAML** — Formato de representación de datos estructurados, muy usado en configuración.
> **JSON** — Formato textual para representar datos estructurados mediante objetos y listas.
> **Docker** — Plataforma de contenerización para construir, distribuir y ejecutar aplicaciones aisladas en contenedores.
> **Git** — Sistema distribuido de control de versiones.
> **HTML** — HyperText Markup Language, lenguaje de marcado para estructurar documentos web.
> **BIND** — Berkeley Internet Name Domain, implementación de servidor DNS.
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

Aprender a utilizar VS Code como centro de trabajo para configuración, código, documentación y administración Linux:

- Explorador de archivos;
- editor;
- terminal WSL2;
- YAML, JSON, Markdown, Bash y Dockerfile;
- Git;
- validación de configuraciones;
- diagnóstico.

## 2. 🖥️ Modelo de trabajo

```text
┌────────────────────────────────────────────────────────────┐
│ 📁 EXPLORADOR       📝 EDITOR                              │
│                                                            │
│ compose.yaml          nginx.conf                           │
│ Dockerfile            kea-dhcp4.conf                       │
│ config/               named.conf                           │
│                                                            │
├────────────────────────────────────────────────────────────┤
│ 🐧 TERMINAL WSL2                                          │
│ $ docker compose config                                   │
│ $ sudo nginx -t                                           │
│ $ git status                                              │
└────────────────────────────────────────────────────────────┘
```

La interfaz puede ejecutarse en Windows mientras el proyecto y las herramientas Linux trabajan en WSL2.

## 3. 📦 Instalación y primer proyecto

Instala VS Code y la extensión oficial **WSL**. En Ubuntu:

```bash
sudo apt update
sudo apt install git curl wget
mkdir -p ~/sri/laboratorio
cd ~/sri/laboratorio
code .
```

## 4. 🧭 Explorador

Estructura típica:

```text
laboratorio/
├── compose.yaml
├── Dockerfile
├── config/
│   ├── nginx.conf
│   └── app.conf
├── html/
│   └── index.html
└── README.md
```

Mantén una única ubicación de trabajo principal. Para proyectos con mucha E/S, es preferible trabajar en el sistema de archivos de WSL2 en lugar de mantener el proyecto bajo `/mnt/c`.

## 5. ✍️ Editor y atajos

- búsqueda global: `Ctrl+Shift+F`;
- buscar: `Ctrl+F`;
- reemplazar: `Ctrl+H`;
- guardar: `Ctrl+S`;
- terminal integrada: **Ctrl + tecla de acento grave**;
- dividir editor: **Ctrl + \**;
- paleta: `Ctrl+Shift+P`.

> Las combinaciones que contienen una comilla invertida deben escribirse en Markdown de forma que la combinación no aparezca como escape literal.

## 6. 🐧 Terminal WSL2

```bash
pwd
ls -la
ip addr
ip route
ss -lntup
```

La terminal debe estar realmente asociada a WSL2 cuando trabajemos con servicios Linux.

## 7. 🧪 Flujo profesional de configuración

```text
EDITAR → VALIDAR → APLICAR → COMPROBAR → DOCUMENTAR
```

Nginx:

```bash
sudo nginx -t
sudo systemctl reload nginx
systemctl status nginx --no-pager
```

BIND:

```bash
sudo named-checkconf
sudo named-checkzone ejemplo.test /etc/bind/db.ejemplo.test
sudo systemctl reload bind9
```

Kea:

```bash
kea-dhcp4 -t /etc/kea/kea-dhcp4.conf
sudo systemctl restart kea-dhcp4-server
```

Nunca utilices `restart` como primer paso del diagnóstico.

## 8. 📄 YAML y JSON

Compose:

```bash
docker compose config
```

JSON genérico:

```bash
python3 -m json.tool fichero.json
```

La validación genérica no sustituye la validación específica de cada servicio.

## 9. 🧩 Terminales múltiples

Una configuración especialmente útil:

```text
Terminal 1 → logs
Terminal 2 → administración
Terminal 3 → cliente de pruebas
```

Por ejemplo:

```bash
journalctl -fu nginx
```

mientras:

```bash
curl -v http://localhost
```

## 10. 🔐 Seguridad

Nunca almacenes en el repositorio contraseñas, claves privadas, tokens, secretos o credenciales de producción. Utiliza `.gitignore`, ficheros `.example` y mecanismos de secretos.

## 11. 🧪 Práctica de 60 minutos

1. Crear un proyecto WSL2.
2. Abrirlo con `code .`.
3. Crear una página HTML y un `compose.yaml`.
4. Dividir editor y terminal.
5. Levantar Nginx.
6. Modificar la página.
7. Comprobar el cambio con `curl`.
8. Registrar la solución con Git.

## 12. 📚 Documentación oficial

- https://code.visualstudio.com/docs
- https://code.visualstudio.com/docs/remote/wsl
- https://learn.microsoft.com/windows/wsl/
- https://code.visualstudio.com/docs/containers/overview
