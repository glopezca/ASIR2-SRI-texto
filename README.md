# 🌐 Servicios de Red e Internet · ASIR

## Material docente integral · `ASIR2-SRI-texto` · v6.5.8

**Edición 2026** para el módulo profesional **0375 · Servicios de red e Internet** del **CFGS Técnico Superior en Administración de Sistemas Informáticos en Red (ASIR)**.

Este repositorio se concibe como un sistema completo de aprendizaje y operación técnica: **teoría → laboratorio → diagnóstico → evaluación → documentación → transferencia profesional**.

## Qué encontrarás en esta edición

Cada UT integra objetivos observables, mapa conceptual, activación de conocimientos previos, analogías, conceptos con definiciones contextuales, rutas de aprendizaje, prácticas guiadas/semiguiadas/autónomas, incidencias, diagnóstico sistemático, evidencia, rúbricas, autoevaluación, test, solucionario y recursos de ampliación.

Se añaden además plantillas profesionales, matriz curricular, guía de laboratorio reproducible, auditoría de obsolescencia, índice alfabético y un algoritmo reproducible de actualización.

## Unidades de trabajo

| UT | Contenido | RA |
|---|---|---|
| UT1 | TCP/IP, direccionamiento, routing, NAT/PAT y preparación del laboratorio | base transversal |
| UT2 | DHCP, concesiones, relay, Kea y seguridad | RA2 |
| UT3 | DNS, BIND9, zonas, registros, transferencias y DNSSEC | RA1 |
| UT4 | FTP, FTPS, SFTP, TFTP, permisos y diagnóstico | RA4 |
| UT5 | HTTP, HTTPS, Apache, Nginx, Virtual Hosts, proxy y observabilidad | RA3 |
| UT6 | SMTP, IMAP, POP3, Postfix, Dovecot, Roundcube y autenticación | RA5 |
| UT7 | XMPP, IRC, listas de distribución y NNTP | RA6 |
| UT8 | Audio, vídeo, FFmpeg, Icecast, HLS, RTP y videoconferencia | RA7 + RA8 |

## Índice general

Consulta el **[índice general](INDICE-GENERAL.md)** para acceder directamente a todas las UT, anexos y materiales complementarios.

## Anexos incorporados en v6.5.8

- [Anexo XX · Scripts personalizados de ASIR2-SRI](ANEXO-XX-Scripts-Personalizados-ASIR2-SRI.md) — uso, revisión e integración en PowerShell, `.profile` y `.bashrc`.
- [Anexo XXI · Chuleta de utilidades TUI](ANEXO-XXI-Chuleta-TUI-Administracion.md) — procesos, servicios, logs, árboles, discos, red, contenedores y administración remota.

## Índice alfabético

Consulta el **[índice alfabético de conceptos](INDICE-ALFABETICO.md)** para localizar rápidamente términos, servicios, protocolos y conceptos trabajados en las UT.

## Tres entornos de trabajo + Docker como extensión

La v6.5.8 fija **tres entornos primarios y coherentes** para las prácticas: **Cisco Packet Tracer**, **WSL** y **VirtualBox + Ubuntu Server**. Docker Compose queda como extensión reproducible en los anexos y no sustituye al laboratorio principal.

| Entorno | Papel en v6.5.8 |
|---|---|
| 🧪 **Packet Tracer** | Topología, routing y demostración gráfica de DHCP; en UT2 se compara **Arnor (DHCP gráfico)** con **Mordor (DHCP por CLI)**. |
| 🐧 **WSL + Ubuntu** | Cliente, herramientas de diagnóstico, captura, consultas y automatización. **No se despliega un servidor DHCP en WSL.** |
| 🖥️ **VirtualBox + Ubuntu Server** | Servidores reales del laboratorio. Las cinco VMs son **Mordor, Gondor, Rohan, Lothlorien y Rivendel**. Mordor presta DHCP; Lothlorien centraliza la práctica de servicios; Rivendel se reserva para configuraciones auxiliares. |
| 🐳 **Docker Compose** | Extensión opcional para reproducibilidad, tratada en los anexos; no redefine la arquitectura principal. |

### Ecosistema Tierra Media v6.5.8

![Topología Tierra Media v6.5.8](img/topologia-tierramedia-packettracer.png)

| Zona | Red | Elementos principales | Papel |
|---|---|---|---|
| 🟨 **Red externa** | `10.0.0.0/16` | Hobbiton `10.0.32.64`, Mordor `10.0.2.15` | Acceso externo / salida |
| 🟩 **Red interna** | `192.168.10.0/24` | Mordor `192.168.10.254`, Gondor `.64`, Rohan `.65`, Arnor `.192` | Clientes y DHCP en Packet Tracer |
| 🟧 **DMZ** | `192.168.20.0/24` | Mordor `192.168.20.254`, Lothlorien `.192`, Rivendel `.193` | Servicios publicados |

**Dominio de laboratorio:** `tierramedia.jc` · **DNS:** `192.168.20.192` · **DHCP gráfico PT:** Arnor `192.168.10.192` · **DHCP CLI PT:** Mordor `192.168.10.254`.

### VMs de VirtualBox

```text
Mordor       → router/gateway Linux + DHCP
Gondor       → cliente interno
Rohan        → cliente interno
Lothlorien   → servidor principal de servicios
Rivendel     → servidor auxiliar / secundario / pruebas
```

> **Regla de continuidad:** una UT posterior no inventa una red nueva si puede completar la infraestructura anterior. Cuando el servicio real se despliega en Ubuntu, se centraliza en **Lothlorien** salvo que el objetivo de la práctica exija específicamente **Mordor** o **Rivendel**.

## v6.5.8 · Cambio de arquitectura de laboratorio

La v6.5.8 fija una arquitectura acumulativa única para las ocho UT. El objetivo es que cada unidad **añada un servicio al mismo escenario**, no que reinicie el laboratorio con una topología distinta.

### Regla de oro de documentación técnica

Para **cada servicio** se exige:

1. ecosistema y equipo donde se instala;
2. ubicación exacta de los ficheros;
3. estructura y sintaxis del formato;
4. ejemplo mínimo;
5. configuración completa del caso Tierra Media;
6. guardado y persistencia;
7. batería de pruebas;
8. comprobación de sintaxis;
9. incorporación de comandos al glosario/chuleta;
10. módulo Webmin equivalente, cuando exista, y declaración expresa cuando no exista.

La matriz y la arquitectura completa están en [Anexo XIX](ANEXO-XIX-Arquitectura-Laboratorio-v6.5.8.md).

## Cómo está organizada cada UT

1. **Situación:** qué problema vas a resolver.
2. **Idea clave:** qué necesitas entender antes de tocar la configuración.
3. **Ejemplo:** cómo se hace en un caso sencillo.
4. **Práctica:** primero guiada, después con menos ayuda y finalmente autónoma.
5. **Diagnóstico:** qué hacer cuando el resultado no coincide con lo esperado.
6. **Evidencia:** qué debes enseñar para demostrar que funciona.
7. **Evaluación:** preguntas, pruebas y actividades.

La **preparación común de las prácticas aparece una sola vez en cada UT**. Cada práctica conserva únicamente sus **pistas específicas**.

## Laboratorio base

La preparación del entorno está en **UT1**, e incluye ficha del puesto, VirtualBox + Ubuntu Server 26.04 LTS, Netplan, SSH, WSL, Packet Tracer y orientación sobre Docker Compose. Los anexos contienen la profundidad específica de Docker/Compose, Git, Kubernetes, scripts de automatización y utilidades TUI.

## Material para el profesor

`APENDICE-PROFESOR.md` reúne banco de tests, propuestas evaluables, rúbricas y banco de incidencias. La matriz curricular de `ANEXO-XIII-Matriz-Curricular.md` permite relacionar RA, prácticas, evidencias e instrumentos.

## Material recuperado del CIFP Juan de Colonia

La v6.5.8 vuelve a contrastar el material con el libro **Preparación del entorno** del CIFP Juan de Colonia. Se fusionan y sintetizan sus contenidos útiles con la documentación del repositorio, evitando duplicaciones y manteniendo una única referencia práctica.

En particular, se amplía la **chuleta de comandos de red de Ubuntu** para cubrir, además de la consulta de interfaces y rutas, conectividad, DNS, puertos y sockets, Netplan, `systemd`, firewall `ufw`, diagnóstico con `nmap`, registros y herramientas auxiliares. También se conserva la preparación común del puesto: identificación del equipo, comprobación TCP/IP, instalación de Ubuntu Server, SSH y comprobación final.

El contenido del libro no se copia de forma literal: se **fusiona, sintetiza y adapta** a un formato de consulta rápida para el alumno. Los procedimientos más extensos siguen ubicados en las UT y anexos correspondientes.

## Fuentes y control de actualidad

`INFORME-REVISION-FUENTES-v6.5.8.md` documenta qué materiales aportados se integran, cuáles se corrigen y cuáles se conservan únicamente como referencia histórica o pedagógica.

El material usa documentación oficial de Ubuntu, BIND9, Kea, Apache, Nginx, Postfix, Dovecot, Mailman 3, Docker, Kubernetes, MDN y RFC Editor como fuentes técnicas primarias.

## Licencia y atribución

El material original del repositorio se distribuye bajo **CC BY-SA 4.0**.

**Atribución recomendada:**

> **Germán López Castro**, *Servicios de Red e Internet · ASIR2-SRI-texto*, v6.5.8, https://github.com/glopezca/ASIR2-SRI-texto, licencia CC BY-SA 4.0.

Los materiales de terceros mantienen sus propias licencias, marcas y derechos.

## Herramientas de actualización

Desde la raíz del repositorio:

```bash
python3 tools/update_material.py --check
python3 tools/update_material.py --dry-run --bump 6.6
python3 tools/update_material.py --bump 6.6
python3 tools/update_material.py --check
python3 tools/update_material.py --package
```

El actualizador no reemplaza recetas técnicas mediante búsquedas globales. Solo cambia metadatos canónicos y genera plantillas de release; el contenido técnico requiere auditoría y pruebas.

## Estructura destacada

- `UT1`-`UT8`: material principal.
- `ANEXO-II-Docker-WSL.md`: Docker desde cero.
- `ANEXO-VI-Docker-Compose-UT1-UT8.md`: Entorno IV.
- `ANEXO-VII-Compose-a-Kubernetes.md`: transición a Kubernetes.
- `ANEXO-XII-Plantillas-Entregables.md`: entregables profesionales.
- `ANEXO-XIII-Matriz-Curricular.md`: RA → evidencia → evaluación.
- `ANEXO-XIV-Recursos-Abiertos.md`: documentación técnica y recursos abiertos.
- `ANEXO-XV-Guia-Laboratorio-Reproducible.md`: preparación y reseteo.
- `ANEXO-XVI-Auditoria-Obsolescencia.md`: criterio de sustitución tecnológica.
- `ANEXO-XVII-Algoritmo-Actualizacion.md`: procedimiento de futuras iteraciones.
- `ANEXO-XVIII-Chuleta-Comandos-Red-Ubuntu.md`: consulta rápida de comandos de red para el laboratorio.
- `ANEXO-XIX-Arquitectura-Laboratorio-v6.5.8.md`: arquitectura común de Packet Tracer, WSL y VirtualBox.
- `ANEXO-XX-Scripts-Personalizados-ASIR2-SRI.md`: scripts personalizados y su integración en Bash y PowerShell.
- `ANEXO-XXI-Chuleta-TUI-Administracion.md`: utilidades TUI para administración local y remota.
- `INFORME-REVISION-FUENTES-v6.5.8.md`: auditoría de las fuentes aportadas.
- `INDICE-ALFABETICO.md`: índice rápido de conceptos.


## Auditoría de continuidad

La integración y no regresión respecto a v6.5.4 se documenta en [INFORME-INTEGRACION-v6.5.8.md](INFORME-INTEGRACION-v6.5.8.md).
