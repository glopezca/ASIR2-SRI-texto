# Auditoría de fuentes y materiales incorporados · v6.5.8

**Fecha de revisión:** 2026-09-27

Esta auditoría separa tres decisiones: **integrar**, **integrar tras corregir** y **conservar solo como referencia histórica/pedagógica**. Las recetas de terceros no se copian literalmente cuando su tecnología está obsoleta, ni se mantienen afirmaciones dudosas solo por aparecer en una fuente docente.

## Criterios de decisión

1. **Actualidad técnica:** se prioriza documentación oficial y estándares vigentes.
2. **Corrección:** una afirmación incorrecta no se integra; se corrige o se descarta.
3. **Valor didáctico:** se conservan estructuras pedagógicas valiosas aunque la receta técnica original haya envejecido.
4. **Trazabilidad:** cada incorporación importante queda vinculada a una práctica o anexo del repositorio.
5. **No copia literal:** los libros y materiales editoriales se usan como fuentes de contraste; se integran ideas, no reproducción extensa de texto protegido.

## Fuentes aportadas por el docente

| Fuente | Decisión | Aportación incorporada |
|---|---|---|
| `Preparación del entorno · CIFP Juan de Colonia` | **Integrar tras actualizar** | Inventario de red del puesto, instalación de VM, Netplan, SSH, claves, herramientas Linux, Webmin como apoyo, planificación de contenedores. Se sustituye la receta antigua de Webmin con `apt-key` por el flujo oficial actual. |
| `DNS y otros mecanismos de resolución de nombres de red · CIFP Juan de Colonia` | **Integrar tras corregir** | `hostname`, `/etc/hosts`, `systemd-resolved`, `resolv.conf`, Avahi/mDNS/DNS-SD, BIND9, RNDC, DNSSEC, Webmin. Se corrige la simplificación de `/etc/hosts` como orden universal de consulta y se distingue NSS/resolved. |
| `Resolución de nombres: instalación y configuración · CIFP Juan de Colonia` | **Integrar tras corregir** | Zonas directa/inversa, pruebas con `dig`/`nslookup`, cliente Windows 11, DNSSEC y vistas. Se mantiene como apoyo práctico y no como receta exclusiva. |
| `Instalación y configuración de un servidor web · CIFP Juan de Colonia` | **Integrar tras corregir** | MIME, módulos, virtual hosts, autenticación, HTTPS, logs, `apache2ctl`, `.htaccess`, expresiones regulares y Webmin. Se conservan los conceptos transversales y se actualizan ejemplos. |
| `Servicio web · CIFP Juan de Colonia` | **Integrar tras corregir** | Flujo HTTP, métodos, estados, `Content-Type`, módulos, Virtual Hosts, HTTPS, certificados, logs y herramientas de desarrollador. Se descartan referencias no necesarias para SRI. |
| `Servicio de transferencia de ficheros · CIFP Juan de Colonia` | **Integrar tras corregir** | FTP activo/pasivo, FTPS/TLS, SFTP/SSH, permisos, `wget` y `curl`. Se descarta la caracterización de FTP como servicio seguro por defecto. |
| `Servicio de correo electrónico · CIFP Juan de Colonia` | **Integrar tras corregir** | MUA/MSA/MTA/MDA, MIME, Roundcube, Sieve, Postfix/Dovecot, autenticación y seguridad. Se descartan configuraciones inseguras (p. ej. autenticación en claro sin TLS y SMTP de cliente por 25). |
| `Instalación y administración del servicio de correo electrónico · CIFP Juan de Colonia` | **Integrar tras corregir** | Procedimiento de laboratorio Postfix+Dovecot+Roundcube y `postconf`/`doveconf`. Se actualizan submission, TLS y rutas de configuración. |
| `Servicios de mensajería instantánea, noticias y listas de distribución · CIFP Juan de Colonia` | **Integrar tras corregir** | XMPP, presencia, WebSocket como concepto, NNTP/Usenet y modelo de listas. Se evita presentar aplicaciones propietarias como estándares abiertos. |
| `Instalación y configuración de servicios de DL/ML, usenet e IM · CIFP Juan de Colonia` | **Integrar tras actualizar** | Sympa como laboratorio real, administración web y relación con SMTP; NNTP histórico y criterios para comparar con Mailman 3. |
| `Servicio de audio y vídeo · CIFP Juan de Colonia` | **Integrar tras corregir** | Tipos de compresión, códecs, contenedores, podcast, VOD/directo y videoconferencia. Se evita confundir formatos con protocolos. |
| `Instalación y configuración de servicios de streaming · CIFP Juan de Colonia` | **Integrar tras corregir** | Icecast, FFmpeg, HLS y arquitectura Nginx/RTMP. Se descarta la configuración `ProxyPass` de Apache para RTMP como receta genérica. |
| `SRI-Ra-Ma(1).pdf` | **Referencia pedagógica/histórica** | Se rescatan la secuencia de ejercicios propuestos, test de conocimientos, material adicional e índice alfabético. Las recetas ligadas a Windows Server/Skype/WINS y otras tecnologías antiguas no pasan a la práctica principal. |

## Elementos que se descartan explícitamente

| Elemento | Motivo |
|---|---|
| `apt-key` para instalar Webmin | Flujo obsoleto; se exige el método de repositorio y clave actual documentado por el proveedor. |
| `disable_plaintext_auth = no` como configuración general de Dovecot | Permite autenticación sin exigir canal protegido; esta edición enseña TLS y autenticación segura antes de habilitar acceso remoto. |
| Roundcube enviando por `25/tcp` | El puerto 25 es principalmente transporte SMTP entre MTAs; para clientes se enseña Submission (habitualmente 587/STARTTLS o 465/TLS). |
| `ProxyPass /rtmp rtmp://...` en Apache | No se mantiene como receta general de proxy HTTP; RTMP y HTTP son protocolos diferentes. |
| WINS, Windows Server 2003/2008, Windows XP, recetas antiguas de Skype | Se citan solo cuando aportan contexto histórico; no forman el laboratorio principal. |
| Afirmación de que `/etc/hosts` se consulta siempre “antes que todo” | El orden real depende del mecanismo de resolución del sistema, especialmente NSS y `systemd-resolved`; se enseña esta distinción. |

## Fuentes externas vigentes usadas para la actualización

- Ubuntu Server / DNS y BIND9: https://ubuntu.com/server/docs/how-to/networking/install-dns/
- BIND 9 Documentation: https://bind9.readthedocs.io/en/latest/
- Kea DHCP: https://kea.readthedocs.io/
- Apache HTTP Server 2.4: https://httpd.apache.org/docs/2.4/
- Nginx: https://nginx.org/en/docs/
- Dovecot: https://doc.dovecot.org/
- Postfix: https://www.postfix.org/
- GNU Mailman 3: https://docs.mailman3.org/
- Sympa: https://sympa.community/
- XMPP: https://xmpp.org/
- FFmpeg: https://ffmpeg.org/documentation.html
- Icecast: https://icecast.org/docs/
- Docker Compose: https://docs.docker.com/compose/
- Kubernetes: https://kubernetes.io/docs/concepts/
- MDN HTTP: https://developer.mozilla.org/docs/Web/HTTP
- RFC Editor: https://www.rfc-editor.org/

## Regla para futuras versiones

No se promueve una receta a “actual” por antigüedad o popularidad. Debe existir una fuente primaria vigente, una prueba reproducible y una justificación pedagógica para que entre en el camino principal del alumnado.


## Recuperación explícita en v6.5.8

Se recupera como material visible para el alumnado la sección **«Comandos de red en Ubuntu»** del PDF `Preparación del entorno · CIFP Juan de Colonia`, reorganizada en `ANEXO-XVIII-Chuleta-Comandos-Red-Ubuntu.md`. La nueva versión distingue entre comandos de consulta, resolución DNS, configuración persistente mediante Netplan, comprobación de servicios, registros y herramientas de diagnóstico.

También se conserva como criterio editorial la preparación común del puesto: **identificar → configurar → probar → documentar**.

## Webmin en v6.5.8

Se eliminan las capturas sintéticas de Webmin. El material pasa a utilizar documentación oficial de Webmin como referencia visual y de procedimiento, y las prácticas indican que cualquier captura local debe proceder de una instalación real y de la versión utilizada en el aula. Esto evita que una imagen con textos superpuestos transmita una interfaz que no coincide con el sistema real.
