# Anexo XXII · Simulador netsim: DHCP en Cisco IOS y servicios en Server-PT

## 1. Qué es netsim y para qué se usa

**netsim** es un simulador de redes que funciona en el navegador y reproduce el aspecto de Cisco Packet Tracer. Tiene dos partes:

- **Routers y switches Cisco IOS** con la CLI real y un **servidor DHCP completo**. Acepta toda la sintaxis de pools, incluidas las reservas que algunas versiones de Packet Tracer no implementan.
- **Servidores tipo Server-PT** con DHCP, DNS, HTTP, correo (SMTP, POP3 e IMAP) y SSH. Cada servidor tiene un terminal GNU/Linux (Ubuntu) o Windows, con `systemctl`, `journalctl` y comandos de red básicos. Los PC incluyen navegador, cliente de correo, cliente SSH y ambos terminales.

**▶ [Abrir netsim](https://raw.githack.com/glopezca/netsim/main/demo/netsim-dhcp-lab.html)**. No requiere instalación ni cuenta y funciona en cualquier navegador moderno de escritorio.

En este material netsim es una **herramienta de apoyo del Entorno I** (Packet Tracer), no un entorno nuevo. Se usa cuando Packet Tracer no permite completar una parte de la práctica. Es especialmente útil en dos casos:
- Las **reservas DHCP**: por MAC en el servidor gráfico (Práctica 1 de UT2) y por `client-identifier` o `hardware-address` en IOS (Práctica 2).
- Ver **paquete a paquete** los protocolos de UT3, UT4 y UT6.

```text
                      ENTORNO I · SIMULACIÓN
                               │
       ┌───────────────────────┴───────────────────────┐
       ▼                                               ▼
 Packet Tracer                                      netsim
 topología Tierra Media                CLI IOS + DHCP completo (UT2)
 Arnor GUI / Mordor CLI                Server-PT: DHCP con reservas, DNS,
 Lothlorien DNS / HTTP / Email         HTTP, correo y SSH (UT2–UT6)
       │                                               │
       └────────────── misma configuración ────────────┘
                               │
                               ▼
     VirtualBox: Kea · BIND9 · Apache/Nginx · Postfix/Dovecot (Entorno III)
```

> **Regla:** la configuración y las evidencias de referencia son las de cada UT. Este anexo no repite comandos: explica cómo llevar a netsim los que ya aparecen en las unidades.

## 2. Correspondencia con las prácticas

| Unidad y práctica | Qué aporta netsim |
|---|---|
| **UT2 · Práctica 1** · DHCP gráfico en Arnor (§25) | Server-PT con pool por **IP inicial + número máximo de usuarios**, como en Packet Tracer, y además una **tabla de reservas por MAC**. Permite completar §25.3 (Gondor `.64` y Rohan `.65` fuera del rango `.1`–`.32`) en lugar de dejarlas estáticas. |
| **UT2 · Práctica 2** · DHCP en Mordor por CLI (§26) | El mismo pool, las mismas exclusiones y opciones, con la salida real de IOS. Permite completar las **reservas de Gondor y Rohan**, que dependen de la versión de Packet Tracer. Funciona `show running-config \| section dhcp`. |
| **UT2 · Práctica 3** · DHCP Relay (§27) | `ip helper-address`, `giaddr` y el pool de la red remota, observables paso a paso. El servidor puede ser un router o un Server-PT. |
| **UT2 · Práctica 4** · VirtualBox + Kea (§28) | Nada: es DHCP real. Sirve para comparar: el terminal Linux del Server-PT muestra un `/etc/kea/kea-dhcp4.conf` generado desde el pool y `journalctl -u kea-dhcp4-server`. |
| **UT2 · Seguridad** · DHCP rogue (§24) | Laboratorio de DHCP snooping con un servidor falso bloqueado por el switch. |
| **UT3 · Práctica integradora** · DNS en Lothlorien | Los registros `A` y el `CNAME` de `tierramedia.jc`, consultados con `nslookup` desde Gondor y con `dig` o `host` desde el terminal Linux. Añade **PTR automáticos**, respuestas `NXDOMAIN` y la vista de cada consulta y respuesta DNS en modo simulación. |
| **UT4 · Ruta Packet Tracer** · HTTP en Server-PT | Páginas editables en el servidor, navegador en el PC y `curl -I` desde los terminales. En simulación se ven el *handshake* TCP en el puerto 80, la petición `GET` y la respuesta `200`/`404`. |
| **UT6 · Prácticas 6.1 y 6.2** · Correo en Packet Tracer | Servicio de correo con SMTP, POP3 e IMAP por separado, cuentas de usuario y cliente de correo en el PC. Incluye reenvío entre dominios por registro **MX**, para recorrer MUA → MTA → DNS → MTA destino → buzón. |
| **Transversal** · administración remota | Servidor SSH con usuarios. `ssh usuario@servidor` abre el terminal Linux o Windows del servidor, donde se gestionan los servicios con `systemctl`/`journalctl` o con `sc`/`net start`. |

## 3. Primer uso

1. Abre netsim con el enlace del apartado 1. Se carga el laboratorio **DHCP básico**: un router, un switch y tres PC que ya han obtenido IP.
2. **Doble clic en el router** abre su consola IOS. Funcionan `?`, el tabulador, las abreviaturas (`sh ip dhcp b`), los filtros `| include` y `| section` y `Ctrl+Z`.
3. **Doble clic en un PC** abre su escritorio:
   - **Configuración IP**: estática o DHCP. Muestra la **MAC** y el **Client-ID** del PC listos para copiar, y permite elegir Windows o GNU/Linux.
   - **Navegador** y **Correo**: clientes HTTP y de correo (POP3/IMAP + SMTP).
   - **Símbolo del sistema** y **Terminal Linux**:
     - Windows: `ipconfig /all|/release|/renew`, `ping`, `arp -a`, `nslookup`, `netstat -an`, `curl`, `ssh`.
     - Linux: `ip a`, `ip r`, `ping -c`, `dig`, `host`, `curl`, `ssh`, `sudo dhclient`.
4. **Servidor** en la paleta coloca un Server-PT. Su ventana tiene las pestañas **Servicios** (DHCP, DNS, HTTP, Correo, SSH y Registros), **Configuración IP** y los terminales.
5. Para construir la topología Tierra Media, usa **Nuevo**, coloca routers, switches, servidores y PC, y conéctalos con la herramienta **Cable**.
6. **Guardar** (o `Ctrl+S`) crea un archivo `.json` con toda la arquitectura: la configuración IOS, las IP y los servicios de los servidores. **Abrir…** la recupera. Sirve como evidencia de entrega. En Chrome y Edge se elige nombre y carpeta; en otros navegadores el archivo se descarga.

## 4. Reservas DHCP: obtener el identificador sin inventarlo

UT2 exige obtener primero la identidad del cliente y construir después la reserva.

**En Server-PT (Práctica 1, Arnor):**

1. En **Servicios → DHCP** crea el pool `TIERRAMEDIA-LAN` con los parámetros de §25.2.
2. Copia la **MAC** de Gondor y de Rohan desde su **Configuración IP**.
3. Añádelas en **Reservas** con `.64` y `.65`. Pueden quedar fuera del rango dinámico, como en un servidor DHCP completo.
4. En el PC ejecuta `ipconfig /release` y después `ipconfig /renew`. La tabla de concesiones de Arnor y su `journalctl -u kea-dhcp4-server` muestran la asignación.

**En IOS (Práctica 2, Mordor):**

1. Pon el PC en **DHCP** y comprueba en el router que ha obtenido una concesión dinámica con `show ip dhcp binding`.
2. Copia el **Client-ID** desde el escritorio del PC (es `01` seguido de la MAC, como en Windows) o desde la columna `Client-ID` de la tabla de bindings.
3. Sustituye `<CLIENT-ID-GONDOR>` y `<CLIENT-ID-ROHAN>` en el pool `host` de la Práctica 2 de UT2.
4. En el PC ejecuta `ipconfig /release` y después `ipconfig /renew`. Debe recibir `.64` o `.65`.
5. Comprueba que `show ip dhcp binding` muestra la reserva con el tipo **Manual** y la concesión **Infinite**, y revisa la configuración con `show running-config | section dhcp`.

Tres matices que conviene conocer porque también ocurren en equipos reales:

- **`client-identifier` y `hardware-address`** son alternativas. Con `hardware-address <MAC>` la reserva funciona para clientes que envían como identificador `01` + MAC, o que no envían ninguno.
- **Un router Cisco como cliente** (`ip address dhcp`) envía un identificador del tipo `cisco-<mac>-<interfaz>`. Para reservarle una dirección hay que usar `client-identifier`, porque `hardware-address` no coincide. `show dhcp lease` muestra ese identificador.
- **Los pools `host` heredan opciones** del pool de red que contiene su dirección. Repetir `default-router` y `dns-server` dentro de cada pool `host`, como hace UT2, es correcto y además explícito.

Dentro de un pool de red también se aceptan las reservas `address <ip> client-id <id>` y `address <ip> hardware-address <mac>`. Son útiles para comparar con las reservas de Kea de la Práctica 4.

## 5. Modo simulación: ver los protocolos paquete a paquete

1. Pulsa **Simulación** en la barra superior.
2. Lanza la acción que quieras observar:
   - en un PC, `ipconfig /release` y después `ipconfig /renew` (DHCP);
   - `nslookup` o `ping` a un nombre (DNS);
   - abrir una página en el **Navegador** (HTTP);
   - enviar o recibir correo (SMTP, POP3, IMAP);
   - `ssh usuario@servidor` (SSH).
3. La **lista de eventos** filtra por protocolo:
   - DHCP: `DISCOVER → OFFER → REQUEST → ACK`;
   - DNS: consulta y respuesta;
   - TCP: `SYN`, `SYN+ACK`, datos y `FIN`, o `RST` si el puerto está cerrado;
   - datos de aplicación: HTTP, SMTP, POP3, IMAP y SSH.

   **Paso** y **Reproducir** animan los sobres sobre la topología.
4. Al seleccionar un evento se ve su PDU:
   - DHCP: los campos `xid`, `yiaddr`, `giaddr` y `chaddr`, y las opciones 53, 61, 50, 54, 1, 3, 6, 15 y 51, entre otras;
   - DNS: las preguntas, las respuestas y el `rcode`;
   - TCP: los puertos, los *flags* y la carga de aplicación.

Es la misma lectura que se pide con `tcpdump` en WSL, pero sobre la topología simulada.

## 6. Laboratorios incluidos y usuarios de ejemplo

El menú **Laboratorios…** carga escenarios ya resueltos que sirven de modelo:

| Laboratorio | Relación con el material |
|---|---|
| DHCP básico | UT2: pool, exclusiones, puerta de enlace, DNS, dominio y concesión |
| Reservas | UT2: pool `host` con `client-identifier`, pool `host` con `hardware-address` y `address … client-id` |
| Relay con `ip helper-address` | UT2: servidor DHCP en otra red; el relay rellena `giaddr` |
| Router-on-a-stick | UT2: un pool por VLAN con subinterfaces 802.1Q |
| DHCP snooping | UT2: servidor falso bloqueado; puertos de confianza; opción 82 |
| Router como cliente DHCP | UT2: `ip address dhcp`, identificador `cisco-…` y ruta por defecto |
| Server-PT: DHCP, DNS, web, correo y SSH | UT2–UT6: servidor `srv` (Ubuntu, `192.168.10.2`) con DHCP y reserva por MAC, zona `aula.lab` (A, CNAME, MX, NS), web `http://www.aula.lab`, correo y SSH |

Credenciales de laboratorio del ejemplo Server-PT. Son ficticias y se cambian en la pestaña **Servicios** del servidor:

| Uso | Usuario | Contraseña | Dónde |
|---|---|---|---|
| Correo IMAP | `ana` (`ana@aula.lab`) | `ana1` | Cliente de correo de PC0 |
| Correo POP3 | `luis` (`luis@aula.lab`) | `luis1` | Cliente de correo de PC1 |
| SSH | `admin` | `cisco` | `ssh admin@srv.aula.lab` desde cualquier terminal |

Los terminales locales no piden contraseña:
- En los PC el usuario es `alumno` en GNU/Linux y `user` en Windows.
- En los servidores es `admin` en GNU/Linux y `Administrator` en Windows.
- En GNU/Linux, `systemctl start|stop|restart` exige `sudo`, igual que en Ubuntu.

La lista completa está en el apartado [Usuarios y contraseñas de ejemplo](https://github.com/glopezca/netsim#usuarios-y-contraseñas-de-ejemplo) del README de netsim.

## 7. Límites y criterio de uso

- netsim **no sustituye** a Packet Tracer ni a los servicios reales de VirtualBox. La topología Tierra Media de referencia sigue estando en Packet Tracer. Los servicios reales siguen en VirtualBox ([Anexo XIX](ANEXO-XIX-Arquitectura-Laboratorio-v6.6.md)): Kea, BIND9, Apache/Nginx, Postfix/Dovecot y OpenSSH.
- Simula routers 2911, switches 2960, PC y Server-PT. No incluye IPv6, DHCPv6 ni enrutamiento dinámico.
- Algunos comandos de pool poco habituales (`origin`, `vrf`, `accounting`, `class`) se aceptan y aparecen en `show running-config`, pero no cambian la asignación.
- Simplificaciones en los servicios:
  - TCP lleva una petición y una respuesta por conexión.
  - No hay HTTPS, FTP ni DNS recursivo.
  - SSH no cifra de verdad.
  - Los ficheros de configuración que muestra el terminal Linux (`/etc/kea/…`, `/etc/bind/…`, `/etc/postfix/main.cf`) se generan desde la pestaña **Servicios** y son de solo lectura. La configuración real de esos servicios se practica en VirtualBox.
- Si una evidencia procede de netsim y no de Packet Tracer, se indica en el informe de la práctica.

## 8. Proyecto, licencia y documentación

netsim es un proyecto independiente del mismo autor. Su código y su documentación están en **[github.com/glopezca/netsim](https://github.com/glopezca/netsim)**:
- la referencia completa de comandos IOS y de los terminales;
- la sección [Servidores Server-PT](https://github.com/glopezca/netsim#servidores-server-pt);
- las reglas de identificación de clientes DHCP;
- el desarrollo del proyecto.

- **Código:** GPL-3.0-or-later.
- **Documentación:** CC BY-SA 4.0.

Este anexo solo enlaza a netsim; no incorpora su código. Cisco, Cisco IOS y Packet Tracer son marcas de Cisco Systems, Inc.; netsim no está relacionado con Cisco ni respaldado por ella.
