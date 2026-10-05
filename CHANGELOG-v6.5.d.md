# CHANGELOG · v6.5.d

## Correcciones de sintaxis y compatibilidad Webmin

- Corregidas las cadenas base de `nftables` para mantener en una única sentencia declarativa `type`, `hook`, `priority` y `policy`.
- En particular, se han corregido los casos de `input`, `forward` y `output` del cortafuegos y `postrouting` de NAT.
- Se mantiene la sintaxis válida de `nftables`; el cambio evita que Webmin interprete una línea independiente `policy ...;` como si fuese una regla.
- Revisadas las órdenes de creación de cadenas para mantener las sentencias compuestas entre llaves y correctamente entrecomilladas cuando se ejecutan desde la shell.
- Añadida una explicación específica en UT1 sobre la diferencia entre la sintaxis de `nftables` y la forma en que el módulo Linux Firewall (nftables) de Webmin representa las cadenas.
- Mantenida la separación entre configuración temporal, validación con `nft -c -f` y persistencia en `/etc/nftables.conf`.
