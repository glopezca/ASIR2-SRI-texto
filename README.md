# 🌐 Servicios de Red e Internet · ASIR

## Material docente integral · `ASIR2-SRI-texto` · 

Material autónomo de estudio, laboratorio y evaluación para el módulo profesional **0375 · Servicios de red e Internet** del **CFGS Técnico Superior en Administración de Sistemas Informáticos en Red (ASIR)**.

Esta edición supone un cambio de alcance: el repositorio deja de ser una colección de apuntes complementarios y se plantea como **material docente integral**, con fundamentos, administración de servicios, prácticas, diagnóstico, autoevaluación, resultados de aprendizaje, Docker, GitHub, Codespaces, bibliografía y materiales para el profesor.

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

Las ocho unidades se pueden trabajar mediante **cuatro entornos complementarios**. Los cuatro forman parte del mismo laboratorio de Servicios de Red e Internet: no son itinerarios alternativos ni niveles excluyentes. Cada entorno responde a una necesidad didáctica distinta.

```text
                         🧪 LABORATORIO SRI
                                │
              ┌─────────────────┼─────────────────┐
              │                 │                 │
              ▼                 ▼                 ▼
      🧪 ENTORNO I       🐧 ENTORNO II      🖥️ ENTORNO III
      Cisco Packet       WSL2 + Ubuntu      VirtualBox +
      Tracer             26.04              Ubuntu 26.04 Server
              │                 │                 │
              └─────────────────┼─────────────────┘
                                │
                                ▼
                         🐳 ENTORNO IV
                         Docker Compose
                                │
                                ▼
                         🌐 SERVICIOS SRI
```

> 🧭 **Cómo interpretar la arquitectura**
>
> Los cuatro entornos están conectados pedagógicamente. **Entorno I** permite observar la red y sus protocolos mediante simulación. **Entorno II** proporciona un Linux ligero para utilizar clientes, herramientas de diagnóstico y scripts. **Entorno III** permite administrar servidores completos con sus interfaces, servicios, procesos, firewall y sistema de archivos. **Entorno IV** convierte una arquitectura multicontenedor en una infraestructura reproducible y versionable.
>
> Una misma práctica puede pasar por varios entornos: primero se observa el fenómeno en Packet Tracer, después se diagnostica con Linux, se implementa como servicio real en VirtualBox y, cuando el servicio lo permite, se reproduce mediante Docker Compose.

| Entorno | Plataforma | Función principal | Pregunta didáctica |
|---|---|---|---|
| **I** | Cisco Packet Tracer | Simulación de topologías y protocolos | **¿Cómo se comporta la red?** |
| **II** | WSL2 + Ubuntu 26.04 | Herramientas, clientes, scripts y diagnóstico | **¿Qué está ocurriendo realmente?** |
| **III** | VirtualBox + Ubuntu 26.04 Server | Administración de servidores completos | **¿Cómo se instala, configura y mantiene?** |
| **IV** | Docker Compose | Infraestructura reproducible y multicontenedor | **¿Cómo convierto la arquitectura en infraestructura como código?** |

# 🧪 5. Entornos de prácticas

Los entornos se distribuyen por función. No es obligatorio utilizar los cuatro en cada actividad: se selecciona el que mejor permite alcanzar el objetivo de aprendizaje.

- **Entorno I · Cisco Packet Tracer:** redes, direccionamiento, routing, VLAN, DHCP y experimentación de protocolos.
- **Entorno II · WSL2 + Ubuntu 26.04:** clientes, `curl`, `dig`, `ss`, `tcpdump`, scripts, análisis y diagnóstico.
- **Entorno III · VirtualBox + Ubuntu 26.04 Server:** instalación y administración de servicios reales.
- **Entorno IV · Docker Compose:** despliegues reproducibles, redes internas, puertos, volúmenes y arquitecturas multicontenedor.

La documentación completa del cuarto entorno se encuentra en el **[Anexo VI · Entorno IV · Docker Compose para UT1–UT8](ANEXO-VI-Docker-Compose-UT1-UT8.md)**.

# 📚 6. Anexos

Los anexos amplían las UT sin romper su secuencia didáctica. El alumnado puede consultarlos cuando la unidad lo indique.

## [🧰 Anexo I · Visual Studio Code + WSL2](ANEXO-I-VSCode-WSL2.md)

Herramienta transversal de edición, terminal, exploración de archivos, YAML/JSON/Markdown, validación y trabajo con Git.

## [🐳 Anexo II · Docker, Docker Compose y fundamentos de Kubernetes](ANEXO-II-Docker-WSL2.md)

Introduce Docker desde cero y presenta, sin presuponer conocimientos previos, los conceptos esenciales de Kubernetes: clúster, plano de control, nodo, Pod, contenedor, Deployment, Service, red, almacenamiento, `kubectl`, acceso a shells y diagnóstico.

## [🐙 Anexo III · Git, GitHub, Codespaces y VS Code](ANEXO-III-Git-GitHub-Codespaces.md)

Desde el repositorio local hasta GitHub y Codespaces, incluyendo edición y ejecución desde VS Code.

## [📚 Anexo IV · Bibliografía y documentación abierta](ANEXO-IV-Bibliografia.md)

Bibliografía organizada por áreas y enlaces a documentación oficial de las herramientas y protocolos utilizados.

## [🛡️ Anexo V · Seguridad, observabilidad y pruebas](ANEXO-V-Seguridad-Observabilidad-Pruebas.md)

Método transversal para validar servicios, observar procesos, analizar logs, introducir fallos deliberados, diagnosticar incidencias y documentar resultados.

## [🐳 Anexo VI · Entorno IV · Docker Compose para UT1–UT8](ANEXO-VI-Docker-Compose-UT1-UT8.md)

Laboratorio reproducible de las ocho UT mediante Docker Compose. Incluye introducción conceptual, preparación, estructura de proyectos, redes, puertos, volúmenes, comandos, soluciones de referencia, troubleshooting y criterios de validación.

## [☸️ Anexo VII · Migración guiada de Docker Compose a Kubernetes](ANEXO-VII-Compose-a-Kubernetes.md)

Recorrido paso a paso para transformar una aplicación descrita mediante Compose en recursos Kubernetes. Explica primero Kubernetes desde cero y después traduce progresivamente servicios, redes, puertos, volúmenes, configuración, secretos, dependencias y comprobaciones. Incluye un procedimiento de conversión manual y el uso de Kompose como herramienta auxiliar, dejando claro qué partes requieren revisión humana.

## [📖 Anexo VIII · Glosario técnico completo](ANEXO-VIII-Glosario.md)

Glosario acumulativo y ordenado alfabéticamente con las siglas, abreviaturas, protocolos, tecnologías, objetos de infraestructura y conceptos técnicos empleados en el material.

> 📌 **Criterio de lectura del glosario**
>
> El glosario es una referencia general, no un sustituto de las explicaciones locales. Cuando una UT introduce un concepto que puede resultar nuevo, se presenta **inmediatamente antes de utilizarlo** mediante un cuadro breve y contextualizado. El Anexo VIII permite consultar después la definición completa y localizar rápidamente otros términos relacionados.

# 👨‍🏫 7. Material para el profesor

## [Apéndice · Evaluación y prácticas](APENDICE-PROFESOR.md)

Incluye bancos de preguntas tipo test, solucionarios, prácticas evaluables de hasta 1 h 45 min, propuestas de resolución y rúbricas.

# 🧭 8. Secuencia didáctica

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

# 🔬 9. Método común de todas las prácticas

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

# ⚠️ 10. Estado de las pruebas técnicas

El paquete incluye revisión estática y coherencia de los ejemplos. Cuando una práctica depende de un daemon, una VM, Docker Desktop, una red virtual específica o GitHub Codespaces, la ejecución final debe realizarse en el entorno indicado.

En particular, el entorno de generación de este paquete **no dispone de Docker Engine ni de un Codespace ejecutable**, por lo que no se presenta como ejecutada una validación extremo a extremo que no haya sido posible realizar.

Esto es deliberado: en administración de sistemas, **una configuración que no se ha probado no debe presentarse como probada**.

---

# 📜 11. Normativa y fuentes curriculares

El material se ha actualizado tomando como referencia la normativa vigente y, para Castilla y León, la información oficial publicada para el título de ASIR.

- Portal oficial de FP de Castilla y León: https://www.educa.jcyl.es/fp/
- Ficha oficial de ASIR: https://www.educa.jcyl.es/fp/es/catalogo-titulos-fp-castilla-leon/catalogo-titulos-grado-superior/administracion-sistemas-informaticos-red
- Real Decreto 1629/2009: https://www.boe.es/buscar/doc.php?id=BOE-A-2009-18355
- Real Decreto 500/2024: https://www.boe.es/buscar/doc.php?id=BOE-A-2024-10685
- Real Decreto 659/2023: https://www.boe.es/buscar/act.php?id=BOE-A-2023-16889
- Orden EFD/659/2024: https://www.boe.es/eli/es/o/2024/06/25/efd659

---

# 🧑‍🎓 12. Cómo utilizar este material

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

# 🏁 13. Principio rector

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
