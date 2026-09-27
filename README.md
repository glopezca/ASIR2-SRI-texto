# 🌐 Servicios de Red e Internet · ASIR

## Material docente integral · `ASIR2-SRI-texto` · v6.5

**Edición Premium 2026** para el módulo profesional **0375 · Servicios de red e Internet** del **CFGS Técnico Superior en Administración de Sistemas Informáticos en Red (ASIR)**.

Este repositorio se concibe como un sistema completo de aprendizaje y operación técnica: **teoría → laboratorio → diagnóstico → evaluación → documentación → transferencia profesional**.

## Qué aporta una edición Premium

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

## Cuatro entornos hermanos

```text
                         🧪 LABORATORIO SRI
                                │
      ┌─────────────────────────┼─────────────────────────┐
      │                         │                         │                         │
      ▼                         ▼                         ▼                         ▼
 🧪 ENTORNO I             🐧 ENTORNO II            🖥️ ENTORNO III            🐳 ENTORNO IV
 Packet Tracer             WSL2 + Ubuntu            VirtualBox + Ubuntu        Docker Compose
 simulación                26.04                     26.04 Server             despliegue reproducible
```

El mismo modelo mental se traslada entre entornos; no se obliga a ejecutar una práctica en los cuatro.

## Arquitectura didáctica

```text
situación → modelo mental → concepto → ejemplo
→ guiada → semiguiada → autónoma
→ incidencia → diagnóstico → transferencia → evaluación
```

La **preparación común de las prácticas aparece una sola vez en cada UT**. Cada práctica conserva únicamente sus **pistas específicas**.

## Laboratorio base

La preparación del entorno está en **UT1**, e incluye ficha del puesto, VirtualBox + Ubuntu Server 26.04 LTS, Netplan, SSH, WSL2, Packet Tracer y orientación sobre Docker Compose. Los anexos contienen la profundidad específica de Docker/Compose, Git y Kubernetes.

## Material para el profesor

`APENDICE-PROFESOR.md` reúne banco de tests, propuestas evaluables, rúbricas y banco de incidencias. La matriz curricular de `ANEXO-XIII-Matriz-Curricular.md` permite relacionar RA, prácticas, evidencias e instrumentos.

## Fuentes y control de actualidad

`INFORME-REVISION-FUENTES-v6.5.md` documenta qué materiales aportados se integran, cuáles se corrigen y cuáles se conservan únicamente como referencia histórica o pedagógica.

El material usa documentación oficial de Ubuntu, BIND9, Kea, Apache, Nginx, Postfix, Dovecot, Mailman 3, Docker, Kubernetes, MDN y RFC Editor como fuentes técnicas primarias.

## Licencia y atribución

El material original del repositorio se distribuye bajo **CC BY-SA 4.0**.

**Atribución recomendada:**

> **Germán López Castro**, *Servicios de Red e Internet · ASIR2-SRI-texto*, v6.5, https://github.com/glopezca/ASIR2-SRI-texto, licencia CC BY-SA 4.0.

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
- `INFORME-REVISION-FUENTES-v6.5.md`: auditoría de las fuentes aportadas.
- `INDICE-ALFABETICO.md`: índice rápido de conceptos.
