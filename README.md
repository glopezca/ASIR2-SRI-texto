# 🌐 Servicios de Red e Internet · ASIR

## Material docente integral · `ASIR2-SRI-texto` · v6.4

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

## 🧠 Método pedagógico común

Las UT y las prácticas siguen una secuencia de aprendizaje progresiva:

```text
SITUACIÓN
   ↓
PROBLEMA
   ↓
MODELO MENTAL
   ↓
CONCEPTO NUEVO
   ↓
EJEMPLO RESUELTO
   ↓
PRÁCTICA GUIADA
   ↓
PRÁCTICA SEMIGUIADA
   ↓
PRÁCTICA AUTÓNOMA
   ↓
DIAGNÓSTICO
   ↓
TRANSFERENCIA
```

Antes de introducir un concepto que pueda resultar nuevo, el texto activa los conocimientos necesarios y proporciona una explicación breve. Las prácticas piden anticipar resultados, modificar de forma controlada, validar, probar desde el cliente y justificar las evidencias. La estrategia se alinea con principios de **Diseño Universal para el Aprendizaje (DUA)**, especialmente la conexión entre conocimientos previos y nuevos, la representación mediante múltiples medios y la construcción progresiva de fluidez.

También se fomenta la metacognición: el alumnado debe formular una predicción, comprobarla, interpretar el resultado y explicar qué evidencia respalda su conclusión.

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

Los cuatro entornos son **niveles hermanos** del laboratorio, no una cadena de sustituciones:

```text
                         🧪 LABORATORIO SRI
                                │
      ┌─────────────────────────┼─────────────────────────┐
      │                         │                         │                         │
      ▼                         ▼                         ▼                         ▼
 🧪 ENTORNO I             🐧 ENTORNO II            🖥️ ENTORNO III            🐳 ENTORNO IV
 Packet Tracer             WSL2 + Ubuntu            VirtualBox + Ubuntu        Docker Compose
 simulación de red         herramientas Linux       26.04 Server              infraestructura
````

Cada entorno responde a una pregunta diferente: **cómo se comporta la red, qué podemos observar desde Linux, cómo se administra un servidor completo y cómo se reproduce una infraestructura como código**.


# 🧪 5. Entornos de prácticas

Los entornos se distribuyen por función. No es obligatorio utilizar los cuatro en cada actividad: se selecciona el que mejor permite alcanzar el objetivo de aprendizaje.

- **Entorno I · Cisco Packet Tracer:** redes, direccionamiento, routing, VLAN, DHCP y experimentación de protocolos.
- **Entorno II · WSL2 + Ubuntu 26.04:** clientes, `curl`, `dig`, `ss`, `tcpdump`, scripts, análisis y diagnóstico.
- **Entorno III · VirtualBox + Ubuntu 26.04 Server:** instalación y administración de servicios reales.
- **Entorno IV · Docker Compose:** despliegues reproducibles, redes internas, puertos, volúmenes y arquitecturas multicontenedor.

La documentación completa del cuarto entorno se encuentra en el **[Entorno IV · Docker Compose para UT1–UT8](ANEXO-VI-Docker-Compose-UT1-UT8.md)**.
# 🧪 8. Evaluación y transferencia

Cada UT debe permitir comprobar cinco dimensiones: **comprender, interpretar, ejecutar, diagnosticar y diseñar**. Por eso se combinan preguntas conceptuales, interpretación de salidas reales, prácticas guiadas, incidencias deliberadas y problemas abiertos.

El material incluye apoyos graduados para que un alumno con dificultades pueda seguir una práctica sin depender de explicaciones orales continuas, y actividades de transferencia para que el alumno avanzado pueda enfrentarse a escenarios no idénticos al ejemplo. Este enfoque coincide con los principios de conectar conocimientos previos, ofrecer múltiples medios de representación y expresión y retirar gradualmente los apoyos a medida que aumenta la fluidez.


# ⚖️ 6. Licencia, derechos de reproducción y citación

Este repositorio contiene **material docente original** elaborado para el módulo 0375 · Servicios de red e Internet. La licencia del material original de este repositorio es **Creative Commons Atribución-CompartirIgual 4.0 Internacional (CC BY-SA 4.0)**, salvo que un fichero indique expresamente otra condición.

La licencia permite reutilizar, adaptar y redistribuir el material, incluso con fines comerciales, siempre que se cumplan sus condiciones de **atribución** y **CompartirIgual**. La licencia no sustituye ni modifica las condiciones de materiales de terceros incorporados al repositorio: documentación, logotipos, marcas, capturas o fragmentos de código ajenos conservan los derechos y licencias que les correspondan.

> ⚠️ **Importante sobre material de terceros**
>
> Antes de reutilizar un fragmento, imagen, código o documentación procedente de otra fuente, hay que comprobar su licencia concreta. Que una fuente esté disponible gratuitamente en Internet no significa que su contenido pueda reproducirse o redistribuirse sin condiciones.

### Cómo citar este material

Para citar el repositorio completo se recomienda indicar, como mínimo:

1. **Título:** *Servicios de Red e Internet · ASIR2-SRI-texto*.
2. **Versión:** v6.4.
3. **Repositorio:** `https://github.com/glopezca/ASIR2-SRI-texto`.
4. **Fecha de consulta o de la versión utilizada.**
5. **Licencia:** CC BY-SA 4.0.

Ejemplo:

> *Servicios de Red e Internet · ASIR2-SRI-texto*, v6.4, repositorio GitHub `glopezca/ASIR2-SRI-texto`, CC BY-SA 4.0, consultado en 2026.

Cuando se reutilice **una UT, práctica o fragmento concreto**, debe indicarse además el nombre del fichero o apartado correspondiente y conservarse la atribución exigida por la licencia.

### Fuentes técnicas

Las explicaciones técnicas se han elaborado y contrastado utilizando documentación abierta de organismos de normalización, proyectos de software y fabricantes. Las fuentes relevantes se identifican en el **Anexo IV · Bibliografía y documentación técnica abierta**. Para una reproducción o adaptación técnica, conviene citar la fuente primaria y consultar su licencia actual en lugar de citar únicamente este repositorio.

### Licencia del repositorio

El fichero [`LICENSE.md`](LICENSE.md) contiene la declaración de licencia aplicable al material original. El fichero [`CITATION.cff`](CITATION.cff) proporciona una referencia estructurada para citar el repositorio y [`NOTICE.md`](NOTICE.md) resume las cautelas relativas a materiales de terceros. La licencia oficial puede consultarse en [Creative Commons BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

---

# 📚 7. Anexos

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

## [🐳 Entorno IV · Docker Compose para UT1–UT8](ANEXO-VI-Docker-Compose-UT1-UT8.md)

Laboratorio reproducible de las ocho UT mediante Docker Compose. Incluye introducción conceptual, preparación, estructura de proyectos, redes, puertos, volúmenes, comandos, soluciones de referencia, troubleshooting y criterios de validación.

## [☸️ Entorno IVI · Migración guiada de Docker Compose a Kubernetes](ANEXO-VII-Compose-a-Kubernetes.md)

Recorrido paso a paso para transformar una aplicación descrita mediante Compose en recursos Kubernetes. Explica primero Kubernetes desde cero y después traduce progresivamente servicios, redes, puertos, volúmenes, configuración, secretos, dependencias y comprobaciones. Incluye un procedimiento de conversión manual y el uso de Kompose como herramienta auxiliar, dejando claro qué partes requieren revisión humana.

## [📖 Entorno IVII · Glosario técnico completo](ANEXO-VIII-Glosario.md)

Glosario acumulativo y ordenado alfabéticamente con las siglas, abreviaturas, protocolos, tecnologías, objetos de infraestructura y conceptos técnicos empleados en el material.

> 📌 **Criterio de lectura del glosario**
>
> El glosario es una referencia general, no un sustituto de las explicaciones locales. Cuando una UT introduce un concepto que puede resultar nuevo, se presenta **inmediatamente antes de utilizarlo** mediante un cuadro breve y contextualizado. El Entorno IVII permite consultar después la definición completa y localizar rápidamente otros términos relacionados.

# 👨‍🏫 8. Material para el profesor

## [Apéndice · Evaluación y prácticas](APENDICE-PROFESOR.md)

Incluye bancos de preguntas tipo test, solucionarios, prácticas evaluables de hasta 1 h 45 min, propuestas de resolución y rúbricas.

# 🧭 9. Secuencia didáctica

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

# 🔬 10. Método común de todas las prácticas

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

# ⚠️ 11. Estado de las pruebas técnicas

El paquete incluye revisión estática y coherencia de los ejemplos. Cuando una práctica depende de un daemon, una VM, Docker Desktop, una red virtual específica o GitHub Codespaces, la ejecución final debe realizarse en el entorno indicado.

En particular, el entorno de generación de este paquete **no dispone de Docker Engine ni de un Codespace ejecutable**, por lo que no se presenta como ejecutada una validación extremo a extremo que no haya sido posible realizar.

Esto es deliberado: en administración de sistemas, **una configuración que no se ha probado no debe presentarse como probada**.

---

# 📜 12. Normativa y fuentes curriculares

El material se ha actualizado tomando como referencia la normativa vigente y, para Castilla y León, la información oficial publicada para el título de ASIR.

- Portal oficial de FP de Castilla y León: https://www.educa.jcyl.es/fp/
- Ficha oficial de ASIR: https://www.educa.jcyl.es/fp/es/catalogo-titulos-fp-castilla-leon/catalogo-titulos-grado-superior/administracion-sistemas-informaticos-red
- Real Decreto 1629/2009: https://www.boe.es/buscar/doc.php?id=BOE-A-2009-18355
- Real Decreto 500/2024: https://www.boe.es/buscar/doc.php?id=BOE-A-2024-10685
- Real Decreto 659/2023: https://www.boe.es/buscar/act.php?id=BOE-A-2023-16889
- Orden EFD/659/2024: https://www.boe.es/eli/es/o/2024/06/25/efd659

---

# 🧑‍🎓 13. Cómo utilizar este material

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

# 🏁 14. Principio rector

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
