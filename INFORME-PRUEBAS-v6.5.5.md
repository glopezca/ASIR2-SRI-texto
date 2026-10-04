# Informe de pruebas · v6.5.5

## Validaciones automáticas realizadas

- Revisión de la nomenclatura del subsistema Linux de Windows: toda referencia práctica usa ahora `WSL`.
- Comprobación de existencia de los ocho ficheros UT y anexos principales.
- Comprobación de enlaces internos del índice general.
- Comprobación de bloques Markdown cercados equilibrados.
- Comprobación de existencia de `img/topologia-tierramedia-packettracer.png`.
- Comprobación de presencia de `/etc/nftables.conf`, estructura table/chain/rule y comandos de validación/persistencia.
- Comprobación de que UT2 no presenta WSL como servidor DHCP.
- Comprobación de que la arquitectura VirtualBox menciona exactamente las cinco VMs definidas.

## Validación que requiere ejecución real

Packet Tracer, VirtualBox, WSL y los servicios Ubuntu deben ejecutarse en el laboratorio para validar extremo a extremo: DORA, Kea, BIND9, FTP/SFTP, Apache/Nginx, Postfix/Dovecot, Prosody/NNTP y multimedia.
