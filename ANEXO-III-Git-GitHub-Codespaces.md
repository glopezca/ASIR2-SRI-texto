# 🐙 ANEXO III · Git, GitHub, Codespaces y Visual Studio Code

> 🧭 **ANTES DE EMPEZAR · VOCABULARIO TÉCNICO**
>
> Las siglas, abreviaturas y conceptos técnicos que van a aparecer en esta unidad se presentan aquí antes de su desarrollo. La explicación local de cada tema podrá ampliar estas definiciones cuando sea necesario.
>
> **UT** — Unidad de Trabajo: unidad didáctica del módulo profesional.
> **CFGS** — Ciclo Formativo de Grado Superior.
> **ASIR** — Administración de Sistemas Informáticos en Red.
> **SRI** — Servicios de Red e Internet.
> **Git** — Sistema distribuido de control de versiones.
> **GitHub** — Servicio de alojamiento y colaboración basado en repositorios Git.
> **Codespaces** — Entornos de desarrollo alojados en GitHub que proporcionan un espacio de trabajo remoto.
> **CLI** — Interfaz de línea de comandos, es decir, administración mediante órdenes escritas.
> **VS Code** — Visual Studio Code, editor de código extensible con terminal y herramientas de desarrollo.
> **HEAD** — Referencia de Git que identifica el commit actual de la línea de trabajo seleccionada.
> **Docker** — Plataforma de contenerización para construir, distribuir y ejecutar aplicaciones aisladas en contenedores.
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

- comprender Git como control de versiones distribuido;
- diferenciar working tree, staging, commit, rama y remoto;
- crear y mantener `ASIR2-SRI-texto`;
- utilizar GitHub Web, GitHub Desktop, Git CLI y GitHub CLI;
- trabajar con Codespaces desde navegador y VS Code;
- ejecutar y documentar el laboratorio desde el repositorio.

## 2. 🧠 Modelo mental

```text
GitHub remoto
     ▲
     │ push / pull
     ▼
Repositorio local
     │
     ├── working tree
     ├── staging area
     └── commits
```

## 3. 🆕 Crear el repositorio

Nombre del proyecto:

```text
ASIR2-SRI-texto
```

El repositorio ya está organizado como producto docente. Por eso no se incluye un capítulo artificial sobre «cómo estructurar el repositorio».

## 4. 🔧 Configurar Git

```bash
git config --global user.name "Nombre Apellidos"
git config --global user.email "correo@juandecolonia.jc"
git config --global init.defaultBranch main
```

Comprobar:

```bash
git config --global --list
git --version
```

## 5. 📥 Clonar

```bash
git clone https://github.com/USUARIO/ASIR2-SRI-texto.git
cd ASIR2-SRI-texto
git status
git remote -v
```

## 6. 🔄 Flujo normal

```text
git pull
   ↓
editar
   ↓
git diff
   ↓
git add
   ↓
git diff --staged
   ↓
git commit
   ↓
git push
```

Revisar siempre el diff antes del commit.

## 7. 🌿 Ramas

```bash
git switch -c mejora-ut5
git status
git push -u origin mejora-ut5
```

Volver:

```bash
git switch main
```

## 8. 🔍 Historial

```bash
git log --oneline --decorate --graph --all
git show HEAD
git diff main..mejora-ut5
```

## 9. 🖥️ GitHub Web

Para pequeños cambios puede utilizarse la interfaz web: editar, previsualizar, confirmar y crear un Pull Request. Para trabajos extensos es preferible un entorno de desarrollo completo.

## 10. 🖱️ GitHub Desktop

Flujo visual:

```text
Clone → Edit → Changes → Commit → Push
```

Es útil durante la introducción porque permite observar claramente qué ficheros cambian.

## 11. ⌨️ GitHub CLI

```bash
gh auth login
gh repo list
gh repo clone USUARIO/ASIR2-SRI-texto
gh codespace list
```

## 12. ☁️ Codespaces

Un Codespace proporciona un entorno de desarrollo conectado al repositorio. Puede abrirse en navegador o desde VS Code de escritorio mediante la extensión correspondiente.

```text
GitHub
  ↓
Codespace
  ↓
Linux + herramientas
  ↓
VS Code
  ↓
Terminal
  ↓
Git / Docker / pruebas
```

## 13. 🧩 Codespaces + VS Code

En VS Code instala la extensión **GitHub Codespaces**, autentícate y utiliza la paleta de comandos para conectarte a un Codespace.

La ventana debe conservar la misma ergonomía del Anexo I:

```text
┌──────────────┬───────────────────────────────┐
│ 📁 Explorer  │ 📝 Editor                     │
├──────────────┴───────────────────────────────┤
│ 🐧 Terminal del Codespace                    │
└──────────────────────────────────────────────┘
```

## 14. 🐳 Docker en Codespaces

Comprobar antes de usar Compose:

```bash
docker version
docker compose version
docker compose config
```

La capacidad de ejecutar Docker depende de la configuración del Codespace. Si el entorno no proporciona un daemon utilizable, no debe presentarse como equivalente a Docker Desktop local.

## 15. 🔐 Secretos

No guardes tokens, contraseñas ni claves en Git. Utiliza secretos del entorno y variables documentadas mediante ejemplos sin valores reales.

## 16. 🧪 Práctica de 75 minutos

1. Crear/clonar el repositorio.
2. Crear una rama.
3. Modificar una UT.
4. Revisar `git diff`.
5. Commit y push.
6. Abrir un Codespace.
7. Conectar desde VS Code.
8. Ejecutar `git status` y `git log`.
9. Realizar un segundo commit.
10. Documentar el flujo.

## 17. 📚 Documentación oficial

- https://docs.github.com/en/get-started/using-git
- https://docs.github.com/en/get-started/git-basics/set-up-git
- https://docs.github.com/en/get-started/start-your-journey/creating-a-repository-for-your-project-on-github
- https://cli.github.com/manual/
- https://docs.github.com/en/codespaces
- https://docs.github.com/en/codespaces/developing-in-a-codespace/using-github-codespaces-in-visual-studio-code
