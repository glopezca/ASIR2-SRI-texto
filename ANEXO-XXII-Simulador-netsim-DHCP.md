# Anexo XXII · Simulador netsim para DHCP en Cisco IOS

## 1. Qué es netsim y para qué se usa en UT2

**netsim** es un simulador de redes que se ejecuta en el navegador y reproduce el aspecto de Cisco Packet Tracer, pero se centra en la **CLI de Cisco IOS** y en su **servidor DHCP**. Acepta toda la sintaxis de pools de IOS, incluidas las reservas que algunas versiones de Packet Tracer no implementan.

**▶ [Abrir netsim DHCP Lab](https://raw.githack.com/glopezca/netsim/main/demo/netsim-dhcp-lab.html)**: no requiere instalación ni cuenta. Funciona en cualquier navegador moderno de escritorio.

En este material netsim es una **herramienta de apoyo del Entorno I** (Packet Tracer), no un entorno nuevo. Se usa cuando Packet Tracer no permite completar una parte de la práctica, sobre todo las **reservas por `client-identifier` o `hardware-address`** de la Práctica 2 de UT2 (Mordor por CLI).

```text
            ENTORNO I · SIMULACIÓN
                     │
     ┌───────────────┴───────────────┐
     ▼                               ▼
 Packet Tracer                    netsim
 topología Tierra Media          CLI IOS + DHCP completo
 Arnor GUI / Mordor CLI          reservas, relay, snooping
     │                               │
     └────── misma configuración ────┘
                     │
                     ▼
     VirtualBox + Kea (Entorno III) · DHCP real
```

> **Regla:** la configuración y las evidencias de referencia son las de [UT2](UT2-Servicio-DHCP.md). Este anexo no repite comandos: explica cómo llevar a netsim los que ya aparecen en la unidad.

## 2. Correspondencia con las prácticas de UT2

| Práctica de UT2 | Qué aporta netsim |
|---|---|
| **Práctica 1** · DHCP gráfico en Arnor (§25) | Nada: se hace en Packet Tracer. netsim no tiene servidor DHCP gráfico tipo Server-PT. |
| **Práctica 2** · DHCP en Mordor por CLI (§26) | El mismo pool, exclusiones y opciones con salida IOS real. Permite completar las **reservas de Gondor y Rohan**, que dependen de la versión de Packet Tracer. |
| **Práctica 3** · DHCP Relay (§27) | `ip helper-address`, `giaddr` y el pool de la red remota, observables paso a paso en modo simulación. |
| **Práctica 4** · VirtualBox + Kea (§28) | Nada: es DHCP real. netsim sirve para comparar reservas IOS con reservas Kea. |
| **Seguridad** · DHCP rogue (§24) | Laboratorio de DHCP snooping con un servidor falso bloqueado por el switch. |

## 3. Primer uso

1. Abre netsim con el enlace del apartado 1. Se carga el laboratorio **DHCP básico**: un router, un switch y tres PC que ya han obtenido IP.
2. **Doble clic en el router** abre su consola IOS. Funcionan `?`, el tabulador, las abreviaturas (`sh ip dhcp b`) y `Ctrl+Z`.
3. **Doble clic en un PC** abre su escritorio, con dos pestañas:
   - **Configuración IP**: estática o DHCP. Muestra la **MAC** y el **Client-ID** del PC listos para copiar.
   - **Símbolo del sistema**: `ipconfig`, `ipconfig /all`, `ipconfig /release`, `ipconfig /renew`, `ping`, `arp -a`.
4. Para construir la topología Tierra Media, usa **Nuevo**, coloca un router, un switch y los PC, y conéctalos con la herramienta **Cable**.
5. **Guardar** descarga la topología en un archivo `.json` y **Abrir…** la recupera. Sirve como evidencia de entrega.

## 4. Reservas: obtener el identificador sin inventarlo

UT2 exige obtener primero la identidad del cliente y construir después la reserva. En netsim se hace así:

1. Pon el PC en **DHCP** y comprueba en el router que ha obtenido una concesión dinámica con `show ip dhcp binding`.
2. Copia el **Client-ID** desde el escritorio del PC (es `01` seguido de la MAC, como en Windows) o desde la columna `Client-ID` de la tabla de bindings.
3. Sustituye `<CLIENT-ID-GONDOR>` y `<CLIENT-ID-ROHAN>` en el pool `host` de la Práctica 2 de UT2.
4. En el PC ejecuta `ipconfig /release` y después `ipconfig /renew`. Debe recibir `.64` o `.65`.
5. Comprueba que `show ip dhcp binding` muestra la reserva con el tipo **Manual** y la concesión **Infinite**.

Tres matices que conviene conocer porque también ocurren en equipos reales:

- **`client-identifier` y `hardware-address`** son alternativas. Con `hardware-address <MAC>` la reserva funciona para clientes que envían como identificador `01` + MAC, o que no envían ninguno.
- **Un router Cisco como cliente** (`ip address dhcp`) envía un identificador del tipo `cisco-<mac>-<interfaz>`. Para reservarle una dirección hay que usar `client-identifier`, porque `hardware-address` no coincide. `show dhcp lease` muestra ese identificador.
- **Los pools `host` heredan opciones** del pool de red que contiene su dirección. Repetir `default-router` y `dns-server` dentro de cada pool `host`, como hace UT2, es correcto y además explícito.

Dentro de un pool de red también se aceptan las reservas `address <ip> client-id <id>` y `address <ip> hardware-address <mac>`. Son útiles para comparar con las reservas de Kea de la Práctica 4.

## 5. Modo simulación: ver DORA paquete a paquete

1. Pulsa **Simulación** en la barra superior.
2. En un PC ejecuta `ipconfig /release` y después `ipconfig /renew`.
3. La **lista de eventos** muestra `DISCOVER → OFFER → REQUEST → ACK`, además del ARP y el ICMP que aparezcan. **Paso** y **Reproducir** animan los sobres sobre la topología.
4. Al seleccionar un evento se ve su PDU: `xid`, `ciaddr`, `yiaddr`, `giaddr`, `chaddr` y las opciones 53, 61, 50, 54, 1, 3, 6, 15 y 51, entre otras.

Es la misma lectura que se pide con `tcpdump udp port 67 or udp port 68` en WSL, pero sobre la topología simulada.

## 6. Laboratorios incluidos

El menú **Laboratorios…** carga escenarios ya resueltos que sirven de modelo:

| Laboratorio | Relación con UT2 |
|---|---|
| DHCP básico | Pool, exclusiones, puerta de enlace, DNS, dominio y concesión |
| Reservas | Pool `host` con `client-identifier`, pool `host` con `hardware-address` y `address … client-id` |
| Relay con `ip helper-address` | Servidor DHCP en otra red; el relay rellena `giaddr` |
| Router-on-a-stick | Un pool por VLAN con subinterfaces 802.1Q |
| DHCP snooping | Servidor falso bloqueado; puertos de confianza; opción 82 |
| Router como cliente DHCP | `ip address dhcp`, identificador `cisco-…` y ruta por defecto |

## 7. Límites y criterio de uso

- netsim **no sustituye** a Packet Tracer ni a Kea. La topología Tierra Media de referencia sigue estando en Packet Tracer y el DHCP real en VirtualBox ([Anexo XIX](ANEXO-XIX-Arquitectura-Laboratorio-v6.6.md)).
- Solo simula routers 2911, switches 2960 y PC. No incluye servidores gráficos tipo Server-PT, IPv6, DHCPv6 ni enrutamiento dinámico.
- Algunos comandos de pool poco habituales (`origin`, `vrf`, `accounting`, `class`) se aceptan y aparecen en `show running-config`, pero no cambian la asignación.
- Si una evidencia procede de netsim y no de Packet Tracer, se indica en el informe de la práctica.

## 8. Proyecto, licencia y documentación

netsim es un proyecto independiente del mismo autor. Su código y su documentación están en **[github.com/glopezca/netsim](https://github.com/glopezca/netsim)**: referencia completa de comandos, reglas de identificación de clientes y desarrollo.

- **Código:** GPL-3.0-or-later.
- **Documentación:** CC BY-SA 4.0.

Este anexo solo enlaza a netsim; no incorpora su código. Cisco, Cisco IOS y Packet Tracer son marcas de Cisco Systems, Inc.; netsim no está relacionado con Cisco ni respaldado por ella.
