# v6.5.8e

## Correcciones curriculares y visuales

- Se incorpora de forma explícita la correspondencia curricular del módulo 0375 con los **RA1–RA8**.
- Se fija la correspondencia: **UT2→RA2, UT3→RA1, UT4→RA4, UT5→RA3, UT6→RA5, UT7→RA6 y UT8→RA7+RA8**.
- **UT1** queda identificada como unidad de fundamentación transversal y no se fuerza su asignación a un RA.
- Se recupera como **único esquema del entorno de red del laboratorio** el PNG mejorado basado en Cisco Packet Tracer: `img/topologia-tierramedia-packettracer.png`.
- Se elimina del repositorio el SVG de topología generado posteriormente.
- Se actualizan README, matriz curricular, índice, arquitectura y documentación de versión a v6.5.8e.

# CHANGELOG · v6.5.8e

## Correcciones de sintaxis y compatibilidad Webmin

- Corregidas las cadenas base de `nftables` para mantener en una única sentencia declarativa `type`, `hook`, `priority` y `policy`.
- En particular, se han corregido los casos de `input`, `forward` y `output` del cortafuegos y `postrouting` de NAT.
- Se mantiene la sintaxis válida de `nftables`; el cambio evita que Webmin interprete una línea independiente `policy ...;` como si fuese una regla.
- Revisadas las órdenes de creación de cadenas para mantener las sentencias compuestas entre llaves y correctamente entrecomilladas cuando se ejecutan desde la shell.
- Añadida una explicación específica en UT1 sobre la diferencia entre la sintaxis de `nftables` y la forma en que el módulo Linux Firewall (nftables) de Webmin representa las cadenas.
- Mantenida la separación entre configuración temporal, validación con `nft -c -f` y persistencia en `/etc/nftables.conf`.

## Restauración visual Packet Tracer

- Se recupera la ilustración completa de la topología **Tierra Media en Cisco Packet Tracer** utilizada en las versiones anteriores del material.
- Se conserva la composición didáctica de las tres zonas: red externa, red interna y DMZ, con Mordor como router y los equipos de Hobbiton, Gondor, Rohan, Arnor, Lothlorien y Rivendel.
- No se sustituye la ilustración por un esquema genérico: la imagen de Packet Tracer vuelve a ser el recurso visual de referencia de la práctica de UT1.
