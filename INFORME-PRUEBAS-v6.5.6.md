# Informe de pruebas · v6.5.6

## Validaciones automáticas

- [x] Ocho UT presentes.
- [x] Anexos canónicos presentes.
- [x] Índice general y enlaces internos revisables.
- [x] Bloques Markdown equilibrados.
- [x] No hay referencias activas a `la denominación anterior` en el material principal.
- [x] No hay anexos duplicados la denominación anterior.
- [x] Topología Tierra Media presente.
- [x] Arnor `192.168.10.192` documentado.
- [x] UT1 contiene Packet Tracer Tierra Media completo.
- [x] UT2 contiene Arnor → Mordor CLI → Kea.
- [x] UT3 contiene DNS en Packet Tracer con Lothlorien.
- [x] `/etc/nftables.conf`, tablas, cadenas, reglas, validación y persistencia presentes.
- [x] Auditoría de integración v6.5.4 → v6.5.6 incluida.

## Validación de ejecución

La ejecución real de Cisco Packet Tracer, WSL y Ubuntu 26.04 Server requiere el entorno de laboratorio. Este informe no marca como ejecutadas pruebas que no hayan sido ejecutadas físicamente.

### Batería recomendada

1. UT1: `show ip interface brief`, `show ip route`, pings entre las tres redes.
2. UT2: DORA en Arnor, sustitución por Mordor, reservas `.64/.65`, Kea en Mordor.
3. UT3: resolución de `tierramedia.jc` desde Gondor y Hobbiton y comprobación BIND9.
4. UT4–UT8: pruebas funcionales de cada servicio desde cliente y servidor, logs, puertos y persistencia.
5. Reinicio de las VMs y comprobación de persistencia de las configuraciones.
