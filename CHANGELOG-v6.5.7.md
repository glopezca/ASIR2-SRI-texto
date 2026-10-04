# CHANGELOG · v6.5.7

## Objetivo

Corrección pedagógica de la UT1 sobre la arquitectura de VirtualBox y la explicación de NAT/nftables, manteniendo la continuidad acumulativa de Tierra Media.

## Cambios principales

- **Punto 27 completamente reestructurado** para partir explícitamente del ecosistema Tierra Media y de las tres zonas comunes: externa `10.0.0.0/16`, interna `192.168.10.0/24` y DMZ `192.168.20.0/24`.
- Se incorporan las **cinco VMs exactas** de VirtualBox: Mordor, Gondor, Rohan, Lothlorien y Rivendel.
- Mordor queda explicado como router Linux de tres interfaces; se separan claramente direccionamiento, rutas y `ip_forward`.
- Se relaciona de forma directa VirtualBox con la topología de Packet Tracer, distinguiendo la IP externa de PT de la dirección que pueda recibir Mordor mediante DHCP en VirtualBox.
- **Punto 28 reescrito con mayor pedagogía sobre nftables**: analogías de fortaleza/aduana, relación con las zonas de Tierra Media, jerarquía tabla → cadena → regla, recorrido `input` → `forward` → `postrouting`, `conntrack`, NAT y `masquerade`.
- Se mantiene el criterio de trabajo **temporal → validación → persistencia**, con `/etc/nftables.conf`, `nft -c -f`, carga y comprobación mediante systemd.
- Se conserva Webmin como capa de administración, manteniendo la CLI y el fichero como referencia técnica.
- Se actualiza la arquitectura activa al Anexo XIX v6.5.7 y se mantiene el resto del material de v6.5.6 sin regresiones intencionadas.
