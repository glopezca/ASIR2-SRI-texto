# Informe de pruebas · ASIR2-SRI-texto · v6.5.4

## Alcance

Iteración centrada en la integración de Cisco Packet Tracer de UT1, UT2 y UT3 mediante la topología Tierra Media.

## Comprobaciones realizadas

- [x] Direccionamiento coherente entre las tres LAN.
- [x] Máscaras: `10.0.0.0/16`, `192.168.10.0/24` y `192.168.20.0/24`.
- [x] Mordor configurado con tres interfaces activas.
- [x] DHCP en Mordor para `192.168.10.0/24`.
- [x] Reservas DHCP documentadas para Gondor y Rohan.
- [x] Lothlorien establecido como DNS `192.168.20.192`.
- [x] Dominio `tierramedia.jc` y registros A documentados.
- [x] Imagen de topología incluida como recurso local.
- [x] Separación didáctica entre servidor DHCP local y DHCP relay.

## Validación pendiente de runtime

La concesión DHCP, la resolución DNS y los pings deben ejecutarse en Cisco Packet Tracer sobre el archivo `.pkt` de la práctica. No se marca esa ejecución como realizada en este entorno.
