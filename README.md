# 🌐 Servicios de Red e Internet · ASIR

## Material docente integral · `ASIR2-SRI-texto` · v6.5.3

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

## Índice alfabético

Consulta el **[índice alfabético de conceptos](INDICE-ALFABETICO.md)** para localizar rápidamente términos, servicios, protocolos y conceptos trabajados en las UT.

## Cuatro entornos de trabajo

Los cuatro entornos se presentan al mismo nivel. Cada uno sirve para una tarea distinta y no es necesario usar los cuatro en todas las prácticas.

| 🧪 Entorno I | 🐧 Entorno II |
|---|---|
| **Packet Tracer** | **WSL2 + Ubuntu 26.04** |
| Simular redes, routing y topologías. | Trabajar con herramientas Linux desde Windows. |

| 🖥️ Entorno III | 🐳 Entorno IV |
|---|---|
| **VirtualBox + Ubuntu Server 26.04** | **Docker Compose** |
| Ejecutar servidores y topologías completas. | Desplegar servicios de forma reproducible. |

> **Idea clave:** los cuatro entornos son herramientas del mismo laboratorio. Elige el que indique la práctica; no tienes que repetir el trabajo en todos.

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

La preparación del entorno está en **UT1**, e incluye ficha del puesto, VirtualBox + Ubuntu Server 26.04 LTS, Netplan, SSH, WSL2, Packet Tracer y orientación sobre Docker Compose. Los anexos contienen la profundidad específica de Docker/Compose, Git y Kubernetes.

## Material para el profesor

`APENDICE-PROFESOR.md` reúne banco de tests, propuestas evaluables, rúbricas y banco de incidencias. La matriz curricular de `ANEXO-XIII-Matriz-Curricular.md` permite relacionar RA, prácticas, evidencias e instrumentos.

## Material recuperado del CIFP Juan de Colonia

La v6.5.3 vuelve a contrastar el material con el libro **Preparación del entorno** del CIFP Juan de Colonia. Se fusionan y sintetizan sus contenidos útiles con la documentación del repositorio, evitando duplicaciones y manteniendo una única referencia práctica.

En particular, se amplía la **chuleta de comandos de red de Ubuntu** para cubrir, además de la consulta de interfaces y rutas, conectividad, DNS, puertos y sockets, Netplan, `systemd`, firewall `ufw`, diagnóstico con `nmap`, registros y herramientas auxiliares. También se conserva la preparación común del puesto: identificación del equipo, comprobación TCP/IP, instalación de Ubuntu Server, SSH y comprobación final.

El contenido del libro no se copia de forma literal: se **fusiona, sintetiza y adapta** a un formato de consulta rápida para el alumno. Los procedimientos más extensos siguen ubicados en las UT y anexos correspondientes.

## Fuentes y control de actualidad

`INFORME-REVISION-FUENTES-v6.5.3.md` documenta qué materiales aportados se integran, cuáles se corrigen y cuáles se conservan únicamente como referencia histórica o pedagógica.

El material usa documentación oficial de Ubuntu, BIND9, Kea, Apache, Nginx, Postfix, Dovecot, Mailman 3, Docker, Kubernetes, MDN y RFC Editor como fuentes técnicas primarias.

## Licencia y atribución

El material original del repositorio se distribuye bajo **CC BY-SA 4.0**.

**Atribución recomendada:**

> **Germán López Castro**, *Servicios de Red e Internet · ASIR2-SRI-texto*, v6.5.3, https://github.com/glopezca/ASIR2-SRI-texto, licencia CC BY-SA 4.0.

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
- `ANEXO-II-Docker-WSL2.md`: Docker desde cero.
- `ANEXO-VI-Docker-Compose-UT1-UT8.md`: Entorno IV.
- `ANEXO-VII-Compose-a-Kubernetes.md`: transición a Kubernetes.
- `ANEXO-XII-Plantillas-Entregables.md`: entregables profesionales.
- `ANEXO-XIII-Matriz-Curricular.md`: RA → evidencia → evaluación.
- `ANEXO-XIV-Recursos-Abiertos.md`: documentación técnica y recursos abiertos.
- `ANEXO-XV-Guia-Laboratorio-Reproducible.md`: preparación y reseteo.
- `ANEXO-XVI-Auditoria-Obsolescencia.md`: criterio de sustitución tecnológica.
- `ANEXO-XVII-Algoritmo-Actualizacion.md`: procedimiento de futuras iteraciones.
- `ANEXO-XVIII-Chuleta-Comandos-Red-Ubuntu.md`: consulta rápida de comandos de red para el laboratorio.
- `INFORME-REVISION-FUENTES-v6.5.3.md`: auditoría de las fuentes aportadas.
- `INDICE-ALFABETICO.md`: índice rápido de conceptos.
