# Anexo XXII · Simulador de redes: Netfix, Cisco Packet Tracer, GNS3 y Boson NetSim

El **Entorno I** del laboratorio es el **Simulador de redes**: la herramienta con la que se construye la topología Tierra Media y se observan los protocolos sin desplegar servidores reales. Estas son las opciones, por orden:

| Opción | Tipo y licencia | Posibilidades | Enlaces |
|---|---|---|---|
| **1 · Netfix** (recomendado) | Web, sin instalación ni cuenta; libre (código GPL-3.0-or-later, documentación CC BY-SA 4.0) | CLI de Cisco IOS con servidor DHCP completo (reservas, relay, snooping), NAT/PAT y ACL estándar, gestión web de routers y switches; servidores con DHCP (reservas por MAC o Client-ID), DNS, Apache2, correo SMTP/POP3/IMAP con Roundcube y SSH; terminales GNU/Linux (bash 5.3) y Windows; nube ISP con Internet emulada y DNS públicos 8.8.8.8/8.8.4.4; modo simulación paquete a paquete | [Abrir Netfix Lab](https://raw.githack.com/glopezca/netfix/main/demo/netfix-lab.html) · [Repositorio y documentación](https://github.com/glopezca/netfix) |
| **2 · Cisco Packet Tracer** | Aplicación de escritorio (Windows, Linux y macOS); gratuita con cuenta de Cisco Networking Academy; propietaria | Simulación de routers y switches Cisco IOS, servidores con servicios básicos (DHCP, DNS, HTTP, Email, FTP/TFTP), IoT y modo Simulación; actividades evaluables `.pka` | [Página oficial](https://www.netacad.com/cisco-packet-tracer) |
| **3 · GNS3** | Escritorio con servidor local o máquina virtual GNS3 (Windows, macOS y Linux); libre (GPL-3.0) | **Emulación** con imágenes reales: Cisco IOSv/IOSvL2 o Dynamips (las imágenes las aporta el usuario), contenedores Docker y VMs QEMU (Linux y otros fabricantes); puede conectarse a redes reales; necesita más recursos | [gns3.com](https://www.gns3.com/) · [Descargas](https://gns3.com/software) · [Documentación](https://docs.gns3.com/) · [GitHub](https://github.com/GNS3) |
| **4 · Boson NetSim** | Web (navegador); comercial, suscripción anual | Simulador orientado a certificaciones Cisco (CCNA 200-301, CCNP ENCOR y ENARSI) con laboratorios guiados y corregidos | [Página oficial](https://boson.com/netsim-cisco-network-simulator/) |

> **Criterio:** en el material, **Simulador de redes** designa el Entorno I sea cual sea la herramienta. Las prácticas se redactan con equipos genéricos (router, switch, PC, Server); los nombres de menú como *Configuración IP* o *Servicios* son los de Netfix, con equivalentes directos en Packet Tracer (*Desktop → IP Configuration*, *Services*). En GNS3 los servidores son VMs o contenedores Linux, y en Boson NetSim se trabaja sobre todo la CLI de IOS. Si una función no existe en el simulador elegido, se indica en el informe y se completa con Netfix o en VirtualBox.

El resto del anexo detalla **Netfix**, la opción recomendada, porque cubre todas las prácticas de UT1 a UT6 y es la que se usa como referencia para las reservas DHCP y para ver los protocolos paquete a paquete.

## 1. Qué es Netfix y para qué se usa

**Netfix** es un simulador de redes que funciona en el navegador, con un manejo parecido al de Cisco Packet Tracer. Reúne:

- **Routers y switches Cisco IOS** con la CLI real y un **servidor DHCP completo**. Acepta toda la sintaxis de pools, incluidas las reservas que algunas versiones de Cisco Packet Tracer no implementan. También NAT/PAT, ACL estándar, `traceroute` y gestión web (`ip http server`).
- **Servidores tipo Server** con DHCP, DNS, HTTP, correo (SMTP, POP3 e IMAP) y SSH. Cada servidor tiene un terminal GNU/Linux (Ubuntu) o Windows, con `systemctl`, `journalctl` y comandos de red básicos. Los PC incluyen navegador, cliente de correo, cliente SSH y ambos terminales.
- **Nube ISP** con líneas de cable, xDSL y fibra, Internet emulada y DNS públicos `8.8.8.8`/`8.8.4.4`.

**▶ [Abrir Netfix](https://raw.githack.com/glopezca/netfix/main/demo/netfix-lab.html)**. No requiere instalación ni cuenta y funciona en cualquier navegador moderno de escritorio.

En este material Netfix es **una de las opciones del Entorno I** (Simulador de redes), no un entorno nuevo. Si se trabaja con otro simulador, Netfix se usa cuando ese simulador no permite completar una parte de la práctica. Es especialmente útil en dos casos:
- Las **reservas DHCP**: por MAC en el servidor gráfico (Práctica 1 de UT2) y por `client-identifier` o `hardware-address` en IOS (Práctica 2).
- Ver **paquete a paquete** los protocolos de UT3, UT4 y UT6.

```text
                      ENTORNO I · SIMULACIÓN
                               │
       ┌───────────────────────┴───────────────────────┐
       ▼                                               ▼
 Sim. de redes                                      Netfix
 topología Tierra Media                CLI IOS + DHCP completo (UT2)
 Arnor GUI / Mordor CLI                Server   : DHCP con reservas, DNS,
 Lothlorien DNS / HTTP / Email         HTTP, correo y SSH (UT2–UT6)
       │                                               │
       └────────────── misma configuración ────────────┘
                               │
                               ▼
     VirtualBox: Kea · BIND9 · Apache/Nginx · Postfix/Dovecot (Entorno III)
```

> **Regla:** la configuración y las evidencias de referencia son las de cada UT. Este anexo no repite comandos: explica cómo llevar a Netfix los que ya aparecen en las unidades.

## 2. Correspondencia con las prácticas

| Unidad y práctica | Qué aporta Netfix |
|---|---|
| **UT2 · Práctica 1** · DHCP gráfico en Arnor (§25) | Server con pool por **IP inicial + número máximo de usuarios**, como en el Simulador de redes, y además una **tabla de reservas por MAC**. Permite completar §25.3 (Gondor `.64` y Rohan `.65` fuera del rango `.1`–`.32`) en lugar de dejarlas estáticas. |
| **UT2 · Práctica 2** · DHCP en Mordor por CLI (§26) | El mismo pool, las mismas exclusiones y opciones, con la salida real de IOS. Permite completar las **reservas de Gondor y Rohan**, que dependen de la versión del Simulador de redes. Funciona `show running-config \| section dhcp`. |
| **UT2 · Práctica 3** · DHCP Relay (§27) | `ip helper-address`, `giaddr` y el pool de la red remota, observables paso a paso. El servidor puede ser un router o un Server. |
| **UT2 · Práctica 4** · VirtualBox + Kea (§28) | Nada: es DHCP real. Sirve para comparar: el terminal Linux del Server muestra un `/etc/kea/kea-dhcp4.conf` generado desde el pool y `journalctl -u kea-dhcp4-server`. |
| **UT2 · Seguridad** · DHCP rogue (§24) | Laboratorio de DHCP snooping con un servidor falso bloqueado por el switch. |
| **UT3 · Práctica integradora** · DNS en Lothlorien | Los registros `A` y el `CNAME` de `tierramedia.jc`, consultados con `nslookup` desde Gondor y con `dig` o `host` desde el terminal Linux. Añade **PTR automáticos**, respuestas `NXDOMAIN` y la vista de cada consulta y respuesta DNS en modo simulación. |
| **UT4 · Ruta Simulador de redes** · HTTP en Server | Páginas editables en el servidor, navegador en el PC y `curl -I` desde los terminales. En simulación se ven el *handshake* TCP en el puerto 80, la petición `GET` y la respuesta `200`/`404`. |
| **UT6 · Prácticas 6.1 y 6.2** · Correo en el Simulador de redes | Servicio de correo con SMTP, POP3 e IMAP por separado, cuentas de usuario y cliente de correo en el PC. Incluye reenvío entre dominios por registro **MX**, para recorrer MUA → MTA → DNS → MTA destino → buzón. |
| **Transversal** · administración remota | Servidor SSH con usuarios. `ssh usuario@servidor` abre el terminal Linux o Windows del servidor, donde se gestionan los servicios con `systemctl`/`journalctl` o con `sc`/`net start`. |

## 3. Primer uso

1. Abre Netfix con el enlace del apartado 1. Se carga el laboratorio **DHCP básico**: un router, un switch y tres PC que ya han obtenido IP.
2. **Doble clic en el router** abre su consola IOS. Funcionan `?`, el tabulador, las abreviaturas (`sh ip dhcp b`), los filtros `| include` y `| section` y `Ctrl+Z`.
3. **Doble clic en un PC** abre su escritorio:
   - **Configuración IP**: estática o DHCP. Muestra la **MAC** y el **Client-ID** del PC listos para copiar, y permite elegir Windows o GNU/Linux.
   - **Navegador** y **Correo**: clientes HTTP y de correo (POP3/IMAP + SMTP).
   - **Símbolo del sistema** y **Terminal Linux**:
     - Windows: `ipconfig /all|/release|/renew`, `ping`, `arp -a`, `nslookup`, `netstat -an`, `curl`, `ssh`.
     - Linux: `ip a`, `ip r`, `ping -c`, `dig`, `host`, `curl`, `ssh`, `sudo dhclient`.
4. **Servidor** en la paleta coloca un Server. Su ventana tiene las pestañas **Servicios** (DHCP, DNS, HTTP, Correo, SSH y Registros), **Configuración IP** y los terminales.
5. Para construir la topología Tierra Media, usa **Nuevo**, coloca routers, switches, servidores y PC, y conéctalos con la herramienta **Cable**.
6. **Guardar** (o `Ctrl+S`) crea un archivo `.json` con toda la arquitectura: la configuración IOS, las IP y los servicios de los servidores. **Abrir…** la recupera. Sirve como evidencia de entrega. En Chrome y Edge se elige nombre y carpeta; en otros navegadores el archivo se descarga.

## 4. Reservas DHCP: obtener el identificador sin inventarlo

UT2 exige obtener primero la identidad del cliente y construir después la reserva.

**En Server (Práctica 1, Arnor):**

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
| Server: DHCP, DNS, web, correo y SSH | UT2–UT6: servidor `srv` (Ubuntu, `192.168.10.2`) con DHCP y reserva por MAC, zona `aula.lab` (A, CNAME, MX, NS), web `http://www.aula.lab`, correo y SSH |

Credenciales de laboratorio del ejemplo Server. Son ficticias y se cambian en la pestaña **Servicios** del servidor:

| Uso | Usuario | Contraseña | Dónde |
|---|---|---|---|
| Correo IMAP | `ana` (`ana@aula.lab`) | `ana1` | Cliente de correo de PC0 |
| Correo POP3 | `luis` (`luis@aula.lab`) | `luis1` | Cliente de correo de PC1 |
| SSH | `admin` | `cisco` | `ssh admin@srv.aula.lab` desde cualquier terminal |

Los terminales locales no piden contraseña:
- En los PC el usuario es `alumno` en GNU/Linux y `user` en Windows.
- En los servidores es `admin` en GNU/Linux y `Administrator` en Windows.
- En GNU/Linux, `systemctl start|stop|restart` exige `sudo`, igual que en Ubuntu.

La lista completa está en el apartado [Usuarios y contraseñas de ejemplo](https://github.com/glopezca/netfix#usuarios-y-contraseñas-de-ejemplo) del README de Netfix.

## 7. Límites y criterio de uso

- Netfix **no sustituye** a los servicios reales de VirtualBox. La topología Tierra Media de referencia es la del Simulador de redes, con cualquiera de las cuatro opciones. Los servicios reales siguen en VirtualBox ([Anexo XIX](ANEXO-XIX-Arquitectura-Laboratorio-v6.6.md)): Kea, BIND9, Apache/Nginx, Postfix/Dovecot y OpenSSH.
- Simula routers 2911, switches 2960, PC y Server. No incluye IPv6, DHCPv6 ni enrutamiento dinámico.
- Algunos comandos de pool poco habituales (`origin`, `vrf`, `accounting`, `class`) se aceptan y aparecen en `show running-config`, pero no cambian la asignación.
- Simplificaciones en los servicios:
  - TCP lleva una petición y una respuesta por conexión.
  - No hay HTTPS ni FTP; el DNS recursivo solo existe en la Internet emulada (`8.8.8.8`).
  - SSH no cifra de verdad.
  - Apache2 se configura en `/etc/apache2` como en Ubuntu; los ficheros de Kea, BIND y Postfix (`/etc/kea/…`, `/etc/bind/…`, `/etc/postfix/main.cf`) se generan desde la pestaña **Servicios** y son de solo lectura. La configuración real de esos servicios se practica en VirtualBox.
- Si una evidencia procede de un simulador distinto del indicado en la práctica, se indica en el informe.

## 8. Proyecto, licencia y documentación

Netfix es un proyecto independiente del mismo autor. Su código y su documentación están en **[github.com/glopezca/netfix](https://github.com/glopezca/netfix)**:
- la referencia completa de comandos IOS y de los terminales;
- la sección [Servidores Server](https://github.com/glopezca/netfix#servidores-server);
- las reglas de identificación de clientes DHCP;
- el desarrollo del proyecto.

- **Código:** GPL-3.0-or-later.
- **Documentación:** CC BY-SA 4.0.

Este anexo solo enlaza a Netfix; no incorpora su código. Cisco, Cisco IOS y Packet Tracer son marcas de Cisco Systems, Inc.; GNS3 es marca de GNS3 Technologies Inc.; Boson y NetSim son marcas de Boson Software, LLC. Netfix no está relacionado con ninguna de ellas ni respaldado por ellas.
