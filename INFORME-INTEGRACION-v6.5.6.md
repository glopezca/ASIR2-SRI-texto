# Informe de integración de mejoras · v6.5.6

## Propósito

Esta versión parte de **v6.5.5** y audita explícitamente las mejoras introducidas en **v6.5.4** para evitar regresiones. Se incorporan las mejoras relevantes de v6.5.4 allí donde seguían siendo necesarias, adaptándolas al ecosistema v6.5.6 (Arnor, WSL, cinco VMs y Lothlorien como servidor principal).

## Mejoras de v6.5.4 recuperadas e integradas

| Mejora de v6.5.4 | Estado en v6.5.6 |
|---|---|
| Topología común Tierra Media | Integrada y ampliada con Arnor y zonas externa/interna/DMZ. |
| Plan de direccionamiento de Mordor, Hobbiton, Gondor, Rohan, Lothlorien y Rivendel | Integrado en arquitectura y UT1–UT3. |
| UT1 con práctica Packet Tracer completa | Recuperada: configuración de Mordor, switches, equipos, verificación progresiva y diagnóstico. |
| UT2 con DHCP en Mordor | Conservada y mejorada: ahora precedida por Arnor gráfico y seguida por Kea en VirtualBox. |
| DORA en Simulation Mode | Conservada en UT2. |
| Distinción DHCP local / DHCP relay | Conservada; relay queda como ampliación independiente. |
| UT3 con DNS en Lothlorien en Packet Tracer | Recuperada como práctica integradora completa con registros A, CNAME, `nslookup`, ping e integración DHCP. |
| Integración progresiva UT1 → UT2 → UT3 | Reforzada mediante el Anexo XIX y las prácticas concretas. |
| Validación estática frente a ejecución real | Conservada y explicitada en el informe de pruebas. |
| Índice general y navegación del material | Conservados en `README.md` e `INDICE-GENERAL.md`. |

## Adaptaciones necesarias

- `la denominación anterior` se normaliza a **WSL**, conforme al diseño posterior del proyecto.
- Arnor se incorpora como servidor DHCP gráfico en `192.168.10.192`.
- En VirtualBox no se utiliza Arnor: DHCP queda en Mordor mediante Kea.
- Lothlorien `192.168.20.192` queda como servidor principal de servicios; Rivendel `192.168.20.193` se reserva para funciones auxiliares.
- La DMZ se documenta como `192.168.20.0/24`, la red interna como `192.168.10.0/24` y la red externa como `10.0.0.0/16`.

## Comprobaciones de no regresión

- Las ocho UT están presentes.
- No existen referencias activas a `la denominación anterior` en el material principal.
- No se mantiene un segundo anexo la denominación anterior duplicado.
- Los enlaces internos del índice general apuntan a los nombres canónicos.
- La topología gráfica existe en `img/topologia-tierramedia-packettracer.png`.
- `UT1` contiene la práctica Tierra Media completa de Packet Tracer.
- `UT2` contiene Arnor → Mordor CLI → Kea.
- `UT3` contiene la práctica DNS de Packet Tracer en Lothlorien.
- `/etc/nftables.conf`, tablas, cadenas, reglas, validación y persistencia siguen documentados.

## Alcance de la validación

La comprobación automática valida estructura, enlaces, referencias y documentación. La ejecución extremo a extremo de Cisco Packet Tracer, WSL y las VMs de Ubuntu debe realizarse en el laboratorio físico/virtual correspondiente.
