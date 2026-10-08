# 🧭 ANEXO XIII · Matriz curricular, evidencias y evaluación

La matriz se utiliza para comprobar que cada resultado de aprendizaje tiene contenido, práctica, evidencia y evaluación asociados. La correspondencia sigue el currículo del módulo profesional **0375 · Servicios de red e Internet** y no fuerza una coincidencia numérica entre UT y RA.

## Correspondencia UT–RA

| UT | RA | Dominio principal | Evidencia de desempeño | Instrumentos |
|---|---|---|---|---|
| UT1 | — | Fundamentos TCP/IP, routing, forwarding, NAT, nftables y entorno | Infraestructura funcional y diagnóstico reproducible | práctica + test + rúbrica |
| UT2 | RA2 | DHCP, concesiones, relay, Kea, reservas y seguridad | Concesión/reserva comprobada, opciones y captura | práctica + test + rúbrica |
| UT3 | RA1 | DNS, zonas, resolución, seguridad | Zona validada, consultas, logs y diagnóstico | práctica + test + rúbrica |
| UT4 | RA4 | FTP/FTPS/SFTP, permisos | Transferencia segura y control de acceso | práctica + test + rúbrica |
| UT5 | RA3 | HTTP, HTTPS, Virtual Hosts, proxy, logs | Sitio publicado, TLS y diagnóstico | práctica + test + rúbrica |
| UT6 | RA5 | SMTP/IMAP/POP3, TLS, autenticación | Envío/recepción, buzón y trazabilidad | práctica + test + rúbrica |
| UT7 | RA6 | XMPP, IRC, listas, NNTP | Sesión o distribución reproducida | práctica + test + rúbrica |
| UT8 | RA7 + RA8 | Audio, vídeo, codecs, streaming, HLS/RTP | Flujo reproducible, reproducción, captura y diagnóstico | práctica + test + rúbrica |

## Resultados de aprendizaje del módulo 0375

| RA | Resultado de aprendizaje | UT asociada |
|---|---|---|
| **RA1** | Administra servicios de resolución de nombres, analizándolos y garantizando la seguridad del servicio. | **UT3** |
| **RA2** | Administra servicios de configuración automática, identificándolos y verificando la correcta asignación de los parámetros. | **UT2** |
| **RA3** | Administra servidores Web, aplicando criterios de configuración y asegurando el funcionamiento del servicio. | **UT5** |
| **RA4** | Administra servicios de transferencia de archivos, asegurando y limitando el acceso a la información. | **UT4** |
| **RA5** | Administra servidores de correo electrónico, aplicando criterios de configuración y garantizando la seguridad del servicio. | **UT6** |
| **RA6** | Administra servicios de mensajería instantánea, noticias y listas de distribución, verificando y asegurando el acceso de los usuarios. | **UT7** |
| **RA7** | Administra servicios de audio, aplicando criterios de configuración y asegurando el funcionamiento del servicio. | **UT8** |
| **RA8** | Administra servicios de vídeo, aplicando criterios de configuración y asegurando el funcionamiento del servicio. | **UT8** |

> **Criterio de organización:** UT1 es una unidad de fundamentación transversal y no se asigna artificialmente a RA1. UT8 cubre conjuntamente RA7 y RA8.

## Competencias transversales

Además del contenido técnico se observa: lectura de logs, línea de comandos, documentación, seguridad, automatización, control de cambios, trabajo reproducible y comunicación de incidencias.

## Niveles de desempeño

| Nivel | Descripción |
|---|---|
| Inicial | Sigue instrucciones y reconoce elementos principales. |
| Operativo | Configura y verifica siguiendo un procedimiento conocido. |
| Diagnóstico | Aísla un fallo con evidencias y modifica una variable cada vez. |
| Profesional | Diseña, justifica, documenta, automatiza parcialmente y propone reversión. |

La matriz es deliberadamente independiente de una herramienta concreta para facilitar la transferencia entre Packet Tracer, WSL, VirtualBox y Compose.
