# CHANGELOG · v6.5.4

## Packet Tracer · Tierra Media

- Sustituida la práctica genérica de routing de UT1 por una topología completa de Tierra Media.
- Incorporado el direccionamiento de Mordor, Hobbiton, Gondor, Rohan, Lothlorien y Rivendel.
- Incorporado Mordor como servidor DHCP de la red `192.168.10.0/24` en UT2.
- Añadidas reservas DHCP para mantener `192.168.10.64` (Gondor) y `192.168.10.65` (Rohan).
- Incorporado Lothlorien como servidor DNS `192.168.20.192` en UT3.
- Incorporada la zona de laboratorio `tierramedia.jc` y registros A para los equipos.
- Añadida la topología gráfica utilizada como recurso local.
- Se mantiene DHCP relay como práctica diferenciada: no se utiliza cuando Mordor actúa como servidor DHCP de la propia LAN.

## Nota de validación

La documentación y los bloques de configuración se han revisado estáticamente. La ejecución extremo a extremo del archivo `.pkt` requiere abrirlo en Cisco Packet Tracer.
