# CHANGELOG · v6.5.5

## Objetivo

Elevar la coherencia entre UT1–UT8 mediante un único ecosistema de laboratorio Tierra Media y una regla de oro común para todos los servicios.

## Cambios principales

- Nueva topología Packet Tracer con **Arnor `192.168.10.192`**.
- Tres zonas claramente diferenciadas: **red externa**, **red interna** y **DMZ**.
- UT2: DHCP gráfico en Arnor → sustitución por DHCP CLI en Mordor → DHCP real con Kea en Mordor (VirtualBox).
- WSL pasa a ser siempre **WSL**.
- Eliminado el servidor DHCP en WSL: queda como cliente/analizador.
- VirtualBox fija cinco VMs: Mordor, Gondor, Rohan, Lothlorien y Rivendel.
- Lothlorien se establece como servidor principal de servicios; Rivendel queda para auxiliares.
- UT1 amplía nftables con ruta persistente `/etc/nftables.conf`, tablas, cadenas, reglas, pruebas temporales, validación y persistencia.
- Se incorporan ubicaciones, sintaxis, validación, persistencia y Webmin a las fichas de servicio de UT1–UT8.
- Se actualizan la chuleta de comandos de red y el glosario.
- Se añade `ANEXO-XIX-Arquitectura-Laboratorio-v6.5.5.md`.
- Se sustituye el esquema gráfico por una versión estilizada y etiquetada.
