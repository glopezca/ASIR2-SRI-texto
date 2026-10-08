# 📡⚡ Unidad de Trabajo 2 · SERVICIO DE CONFIGURACIÓN DINÁMICA DE HOST (DHCP) ⚡📡


## 🧭 Guía de aprendizaje de la UT

**Objetivo principal:** Diseñar y diagnosticar asignación automática.

### 🚪 Antes de empezar

Responde sin consultar la teoría. No es una nota: sirve para decidir qué prerrequisitos recuperar.

1. ¿Qué concepto previo necesitas dominar?
2. ¿Qué problema resuelve la UT?
3. ¿Qué evidencia demostraría que funciona?
4. ¿Qué herramienta usarías primero para diagnosticar?
5. ¿Qué cambiarías solo después de obtener evidencia?

### 🎯 Lo que debes aprender

| Debes dominar | Evidencia observable |
|---|---|
| **DORA y concesiones** | Explicación, comando, diagrama o evidencia verificable. |
| **pools y reservas** | Explicación, comando, diagrama o evidencia verificable. |
| **relay** | Explicación, comando, diagrama o evidencia verificable. |
| **Kea y DHCPv6** | Explicación, comando, diagrama o evidencia verificable. |

### ✅ Al terminar deberás poder

- Debes poder explicar el broadcast.
- Debes poder validar antes de arrancar.
- Debes poder demostrar una concesión.
- Debes poder separar red/relay/servidor.

### 🔗 Para qué te sirve

- Conecta con SLAAC.
- Conecta con alta disponibilidad.
- Conecta con trazabilidad de concesiones.

### 🧯 Regla de diagnóstico

**Predice → observa → formula hipótesis → cambia una sola variable → valida → documenta → revierte si procede.** Una incidencia no se considera cerrada hasta que puedes explicar su causa y reproducir la verificación.

### RA2 · Configuración automática de red.

> **SERVICIOS DE RED E INTERNET · CFGS ASIR · Material docente integral · 2026**
>
> Material autónomo actualizado para el perfil profesional de Técnico Superior en Administración de Sistemas Informáticos en Red. Laboratorio de referencia: **Cisco Packet Tracer**, **WSL + Ubuntu 26.04**, **VirtualBox + Ubuntu 26.04 Server** y **Docker Compose**.
>
> ### 🎯 Resultado de aprendizaje trabajado
>
> **RA2.** Administra servicios de configuración automática, identificándolos y verificando la correcta asignación de los parámetros.

---


> 🧭 **ANTES DE UTILIZAR DHCP**
>
> **DHCP (Dynamic Host Configuration Protocol)** entrega automáticamente parámetros de red a los clientes. Una **concesión o lease** es una asignación temporal de esos parámetros. **DORA** resume las fases habituales de obtención inicial: *Discover, Offer, Request, Acknowledgement*. Un **agente relay** reenvía mensajes DHCP entre redes cuando cliente y servidor no comparten directamente el mismo dominio de difusión.

> 🎯 **MISIÓN DE LA UT**
>
> Comprender cómo un cliente obtiene automáticamente su configuración de
> red, cómo se mantiene una concesión DHCP y cómo diseñar, configurar,
> verificar y diagnosticar un servicio DHCP en una red real o simulada.

> 💡 **Actualización importante**
>
> El material previo utiliza principalmente **ISC DHCP** y ejemplos
> basados en tecnologías históricas. En esta versión se conserva
> la arquitectura conceptual del capítulo, pero las prácticas Linux se
> trasladan a **Kea DHCP**. ISC declaró ISC DHCP *End of Life* en 2022 y
> recomienda migrar a Kea. Ubuntu 26.04 incluye `kea-dhcp4-server` 3.0.3
> en sus repositorios.\
> Véase la documentación oficial de ISC y el catálogo de paquetes de
> Ubuntu.

------------------------------------------------------------------------

# 🧭 Mapa de la unidad

```text
                         📡 DHCP
                           │
             ┌─────────────┼─────────────┐
             │             │             │
          🏠 CLIENTE    🖥️ SERVIDOR    🌉 RELAY
             │             │             │
             └───────┬─────┴─────┬───────┘
                     │           │
                  🔄 DORA     🗂️ ÁMBITOS
                     │           │
                ⏱️ LEASE     🧷 RESERVAS
                     │           │
                     └─────┬─────┘
                           │
                    🧪 VERIFICACIÓN
                           │
              ┌────────────┼────────────┐
              │            │            │
         Packet Tracer   Ubuntu 26.04   Wireshark
                          + Kea
┌──────────────────────────────────────────────────────────────────────┐
│ 🧪 ENTORNOS · I Packet Tracer · II WSL · III VirtualBox · IV Compose │
└──────────────────────────────────────────────────────────────────────┘
```

------------------------------------------------------------------------

> 🧪 **LOS CUATRO ENTORNOS DE PRÁCTICAS**
>
> **I · Cisco Packet Tracer** — simulación de red y protocolos.  
> **II · WSL + Ubuntu 26.04** — herramientas, clientes y diagnóstico.  
> **III · VirtualBox + Ubuntu 26.04 Server** — administración de servidores completos.  
> **IV · Docker Compose** — infraestructura reproducible y multicontenedor.

### 🧪 Entornos hermanos de esta UT

Las cuatro opciones son **entornos hermanos**. Cambia la herramienta, no el modelo mental: **necesidad → protocolo → servicio → configuración → evidencia → diagnóstico**.

| Entorno | Función didáctica | Uso recomendado |
|---|---|---|
| **Entorno I · Cisco Packet Tracer** | Simulación de topologías y comportamiento de red | Fundamentos, routing, direccionamiento y DHCP cuando proceda |
| **Entorno II · WSL + Ubuntu 26.04** | CLI, clientes, scripts y diagnóstico | `curl`, `dig`, `ss`, `tcpdump` y pruebas |
| **Entorno III · VirtualBox + Ubuntu 26.04 Server** | Administración de servidores | Instalación, configuración, permisos, servicios y logs |
| **Entorno IV · Docker Compose** | Despliegue reproducible | Redes, puertos, volúmenes y healthchecks cuando sea portable |

> 🧠 **Transferencia:** no todas las prácticas deben ejecutarse en los cuatro entornos; la elección se justifica por el objetivo didáctico y la naturaleza técnica del servicio.


> 🏨 **ANALOGÍA · LA RECEPCIÓN DE UN HOTEL**
>
> Cuando llegas a un hotel no tienes que inventarte el número de habitación, la puerta de entrada ni las reglas de acceso: recepción te entrega esos datos y puede renovarte la estancia. DHCP hace algo semejante para un equipo de red: proporciona parámetros, establece una **concesión temporal** y puede renovarla. El cliente no «adivina» su configuración; la obtiene siguiendo un protocolo.

# 🎯 0. Objetivos

### 🧭 Ruta de aprendizaje

> **Cómo trabajar esta unidad.** Avanza como por una escalera: primero comprende el problema, después observa un ejemplo, repítelo con ayuda y finalmente modifica el escenario por tu cuenta. Cuando aparezca un concepto nuevo, detente un momento y comprueba que puedes explicarlo con tus palabras antes de continuar.

| Nivel | Qué haces | Evidencia de que puedes continuar |
|---|---|---|
| 🟢 1 · Comprender | Identificas problema, componentes y recorrido de la comunicación. | Puedes explicarlo sin leer el texto. |
| 🔵 2 · Reproducir | Sigues una práctica guiada y validas cada paso. | La práctica funciona y sabes por qué. |
| 🟣 3 · Diagnosticar | Analizas un fallo y contrastas hipótesis con evidencias. | Puedes localizar y justificar la causa. |
| 🔴 4 · Transferir | Cambias una condición del escenario y adaptas la solución. | Puedes resolver una variante sin copiar la receta. |


Al finalizar esta unidad deberás ser capaz de:

-   Explicar qué problema resuelve DHCP.
-   Diferenciar configuración manual y automática.
-   Identificar los componentes de una arquitectura DHCP.
-   Comprender las fases de obtención y renovación de una concesión.
-   Diferenciar **asignación manual, automática y dinámica**.
-   Trabajar con ámbitos, rangos, exclusiones y reservas.
-   Configurar opciones como máscara, gateway y DNS.
-   Comprender el formato y finalidad de los mensajes DHCP.
-   Analizar **DHCPDISCOVER, DHCPOFFER, DHCPREQUEST y DHCPACK**.
-   Comprender qué ocurre cuando cliente y servidor están en redes
    diferentes.
-   Configurar un **DHCP relay**.
-   Analizar tráfico DHCP con Wireshark.
-   Configurar un servidor DHCP moderno en Ubuntu 26.04 Server mediante
    **Kea**.
-   Diagnosticar errores de direccionamiento automático.

------------------------------------------------------------------------



> 🧭 **PREPARACIÓN COMÚN DE LAS PRÁCTICAS**
>
> Todas las prácticas utilizan la misma rutina profesional: **situarse en el escenario → comprobar prerrequisitos → formular una predicción → cambiar una sola variable → validar → probar desde un cliente → recoger evidencias → diagnosticar si falla → documentar y, cuando proceda, revertir**. Esta guía común se explica una sola vez en la UT. Cada práctica añade únicamente las pistas que son propias de su objetivo.

### 🧪 Escalera de práctica

> 🔎 **PISTAS ESPECÍFICAS · 🧪 Escalera de práctica**
>
> **Qué debes fijar:** Explicita qué comportamiento debe observarse al finalizar y qué dato objetivo demostrará que el servicio está funcionando.
>
> **Evidencia:** Usa como evidencia principal el artefacto que mejor demuestre el objetivo de esta práctica; evita capturas sin contexto y conserva comando, salida y fecha de la prueba.
>
> **Pista de troubleshooting:** si el resultado no coincide con tu predicción, vuelve al último punto demostrado, conserva la evidencia y modifica una sola variable antes de repetir la prueba.

- **Guiada:** el procedimiento aparece completo y se valida paso a paso.
- **Semiguiada:** se conserva el objetivo, pero el alumno debe decidir parte de la configuración y las pruebas.
- **Autónoma:** se proporcionan requisitos y restricciones; la solución y la evidencia deben ser justificadas.


# 🚀 1. Introducción

DHCP (*Dynamic Host Configuration Protocol*) permite proporcionar
automáticamente a los clientes los parámetros necesarios para
comunicarse mediante IP.

Un cliente DHCP puede recibir, entre otros:

-   Dirección IP.
-   Máscara de red.
-   Puerta de enlace predeterminada.
-   Servidores DNS.
-   Nombre de dominio.
-   Tiempo de concesión.
-   Otros parámetros definidos mediante opciones DHCP.

Sin DHCP, cada equipo tendría que recibir manualmente esta información.

```text
              CONFIGURACIÓN MANUAL
              ─────────────────────
                 👨‍💻 Administrador
                        │
                        ├── IP
                        ├── Máscara
                        ├── Gateway
                        └── DNS


              CONFIGURACIÓN DHCP
              ──────────────────
                 🖥️ Cliente
                     │
                     │ DHCP
                     ▼
                📡 Servidor
                     │
             ┌───────┴───────┐
             ▼               ▼
            IP              DNS
```

------------------------------------------------------------------------

# 🧠 2. ¿Qué problema resuelve DHCP?

En una red pequeña puede parecer sencillo configurar manualmente todos
los equipos.

En una red con cientos o miles de dispositivos aparecen rápidamente
problemas:

-   Duplicación de direcciones.
-   Errores de máscara.
-   Gateways incorrectos.
-   DNS mal configurado.
-   Dificultad para modificar parámetros.
-   Equipos que cambian de ubicación.
-   Direcciones que quedan ocupadas innecesariamente.
-   Mayor carga administrativa.

DHCP centraliza esta configuración.

> ⚠️ **DHCP no sustituye al direccionamiento bien diseñado.**
>
> El administrador sigue teniendo que definir correctamente las redes,
> los rangos disponibles, las reservas y las opciones que recibirán los
> clientes.

------------------------------------------------------------------------

> 🧭 **ANTES DE EMPEZAR · Arquitectura DHCP**
>
> DHCP no es solamente «un servidor que entrega IP». Intervienen clientes, servidores, ámbitos de direcciones, opciones, concesiones y, cuando existen varias redes, agentes relay. Conviene conocer estos componentes antes de configurar el servicio.

# 🧱 3. Componentes del servicio DHCP

El funcionamiento puede entenderse mediante cuatro elementos
principales:

| Componente | Función |
|---|---|
| 📡 Servidor DHCP | Asigna direcciones y parámetros |
| 💻 Cliente DHCP | Solicita y utiliza la configuración |
| 📜 Protocolo DHCP | Define mensajes y reglas |
| 🌉 Relay DHCP | Transporta peticiones entre redes |

```text
       CLIENTE
          │
          │ DHCP
          ▼
    ┌─────────────┐
    │ DHCP SERVER │
    └─────────────┘

Si están en redes diferentes:

       CLIENTE
          │
          ▼
    🌉 DHCP RELAY
          │
          ▼
    DHCP SERVER
```

------------------------------------------------------------------------

# 🏷️ 4. Asignación de direcciones

El material previo distingue tres mecanismos.

## 4.1. Asignación manual o reserva

El administrador establece una correspondencia entre un cliente y una
dirección determinada.

Ejemplo conceptual:

```text
MAC  00:11:22:33:44:55
          │
          ▼
       192.168.10.50
```

La dirección se entrega mediante DHCP, pero queda asociada al cliente.

En Kea puede realizarse mediante **host reservations**.

------------------------------------------------------------------------

## 4.2. Asignación dinámica

El servidor selecciona una dirección disponible de un conjunto o *pool*
y la entrega durante un tiempo determinado.

```text
POOL DHCP

192.168.10.100 ─────────────── 192.168.10.200
       │                              │
       └──────── direcciones ─────────┘
```

La dirección pertenece al cliente durante una **concesión** (*lease*).

------------------------------------------------------------------------

## 4.3. Asignación automática

El servidor puede asignar una dirección de forma persistente siguiendo
la política configurada.

La distinción exacta entre automática y dinámica depende de la
implementación y de la política de administración utilizada.

------------------------------------------------------------------------

# 📦 5. Ámbitos, subredes y pools

Un servidor DHCP debe saber **para qué red** está sirviendo direcciones.

En terminología tradicional se habla de:

-   Ámbito.
-   Rango.
-   Exclusiones.
-   Reservas.
-   Opciones.

En Kea la configuración DHCP utiliza principalmente el concepto
`subnet4`, dentro del cual se pueden definir uno o varios `pools`.

Ejemplo:

```text
SUBRED
192.168.10.0/24
       │
       ├── Gateway: 192.168.10.1
       ├── DNS:     192.168.10.10
       │
       └── POOL
           192.168.10.100 - 192.168.10.200
```

------------------------------------------------------------------------

# 🚫 6. Exclusiones

No todas las direcciones de una subred deben entregarse dinámicamente.

Por ejemplo:

```text
192.168.10.0/24

.1       Router
.10      Servidor DNS
.20      Servidor web
.30      Impresora
.100-.200 DHCP
```

La zona dinámica debe evitar direcciones utilizadas por dispositivos con
configuración estática.

> 💡 En un diseño actual es frecuente separar claramente:
>
> -   infraestructura,
> -   servidores,
> -   dispositivos reservados,
> -   clientes dinámicos.

------------------------------------------------------------------------

# 🧷 7. Reservas DHCP

Una reserva permite que un cliente concreto reciba siempre una dirección
determinada.

En Kea una reserva puede asociarse, entre otros identificadores, a una
dirección MAC mediante `hw-address`.

Ejemplo:

``` json
{
  "reservations": [
    {
      "hw-address": "00:11:22:33:44:55",
      "ip-address": "192.168.10.50"
    }
  ]
}
```

> ⚠️ Una reserva **no es lo mismo que configurar manualmente la IP en el
> cliente**.
>
> En una reserva el cliente sigue utilizando DHCP.

------------------------------------------------------------------------

# ⏱️ 8. Tiempo de concesión --- Lease Time

Una dirección dinámica se entrega durante un periodo limitado.

```text
     OBTENCIÓN
        │
        ▼
┌───────────────────┐
│   LEASE ACTIVA    │
└───────────────────┘
        │
        ├── renovación
        │
        └── expiración
```

El tiempo de concesión debe adaptarse al tipo de red.

### Red con pocos clientes

Puede utilizar concesiones largas.

### Red con muchos clientes temporales

Puede interesar reducir la duración.

Ejemplos:

-   Aula informática.
-   Red Wi-Fi de invitados.
-   Laboratorio.
-   Red de dispositivos temporales.

------------------------------------------------------------------------

> 🧭 **ANTES DE EMPEZAR · DORA y broadcast**
>
> Un cliente que todavía no conoce su configuración necesita localizar un servidor. Por eso el intercambio inicial utiliza mensajes DHCP y mecanismos de difusión. La secuencia **Discover → Offer → Request → ACK (DORA)** describe el proceso básico de obtención de una concesión IP.

# 🔄 9. Funcionamiento DHCP: DORA

La secuencia clásica para obtener una concesión IP se resume mediante
**DORA**:

```text
        CLIENTE                         SERVIDOR
           │                                │
           │──── DHCPDISCOVER ─────────────>│
           │                                │
           │<──── DHCPOFFER ────────────────│
           │                                │
           │──── DHCPREQUEST ──────────────>│
           │                                │
           │<──── DHCPACK ──────────────────│
           │                                │
           ▼                                ▼
       CONFIGURADO                       CONCESIÓN
```

------------------------------------------------------------------------

# 📡 10. DHCPDISCOVER

El cliente todavía no dispone de una configuración IP válida para esa
red.

Emite un mensaje **DHCPDISCOVER** para localizar servidores DHCP.

En el escenario inicial puede utilizar difusión (*broadcast*).

------------------------------------------------------------------------

# 📤 11. DHCPOFFER

Un servidor DHCP que puede atender la petición responde con una oferta.

La oferta puede incluir:

-   Dirección IP propuesta.
-   Máscara.
-   Tiempo de concesión.
-   Gateway.
-   DNS.
-   Otras opciones.

------------------------------------------------------------------------

# 📬 12. DHCPREQUEST

El cliente selecciona una oferta y solicita formalmente la
configuración.

Cuando existen varios servidores, este mensaje también permite indicar
cuál ha sido seleccionado.

------------------------------------------------------------------------

# ✅ 13. DHCPACK

El servidor confirma la concesión mediante **DHCPACK**.

El cliente puede configurar entonces:

```text
IP       → 192.168.10.101
Máscara  → 255.255.255.0
Gateway  → 192.168.10.1
DNS      → 192.168.10.10
Lease    → 8 horas
```

------------------------------------------------------------------------

# ❌ 14. DHCPNAK

El servidor puede responder con **DHCPNAK** cuando la solicitud no puede
aceptarse, por ejemplo porque la configuración solicitada no es válida
para la red atendida.

No debe confundirse con una simple ausencia de respuesta.

------------------------------------------------------------------------

# 🔁 15. Renovación de la concesión

Una concesión no permanece indefinidamente.

El cliente intenta renovarla antes de que expire.

```text
          LEASE
            │
            │
       ┌────▼────┐
       │   T1    │ ──► intento de renovación
       └────┬────┘
            │
            │ si no responde
            ▼
       ┌─────────┐
       │   T2    │ ──► búsqueda más amplia
       └────┬────┘
            │
            ▼
        EXPIRACIÓN
```

La implementación concreta de T1 y T2 depende de la configuración y del
protocolo.

------------------------------------------------------------------------

# 🔌 16. Puertos utilizados por DHCP

DHCP para IP utiliza **UDP**.

| Función | Puerto |
|---|---|
| Servidor DHCP | UDP 67 |
| Cliente DHCP | UDP 68 |

```text
CLIENTE                         SERVIDOR
UDP 68  ───── DHCP ──────────► UDP 67
UDP 68  ◄──── DHCP ─────────── UDP 67
```

> 🧠 **Para recordar:** DHCP no utiliza TCP para el intercambio normal
> de mensajes DHCP.

------------------------------------------------------------------------

> 🧭 **ANTES DE EMPEZAR · DHCP Relay**
>
> Los routers separan dominios de broadcast. Por ello, un cliente DHCP situado en otra subred no puede depender de que su difusión atraviese el router como si fuera tráfico IP normal. Un **DHCP relay** recibe la petición y la reenvía hacia el servidor, conservando la información necesaria para identificar la red del cliente.

> 📬 **ANALOGÍA · UNA CENTRAL DE CORREOS**
>
> Imagina que una oficina de correos recibe cartas de un barrio y las envía a una central situada en otra ciudad. El cartero local no necesita que la central esté en su misma calle. Un agente relay desempeña una función semejante: recibe mensajes DHCP de una red y los reenvía hacia el servidor situado en otra red.

# 🌉 17. DHCP Relay
### 📊 DORA de un vistazo

| Mensaje | Origen → destino | Finalidad |
|---|---|---|
| DHCPDISCOVER | Cliente → broadcast/relay | Localizar servidores DHCP |
| DHCPOFFER | Servidor → cliente/relay | Proponer una configuración |
| DHCPREQUEST | Cliente → servidor/broadcast | Solicitar la concesión elegida |
| DHCPACK | Servidor → cliente | Confirmar la concesión |
| DHCPNAK | Servidor → cliente | Rechazar la solicitud |


Un broadcast DHCP no atraviesa routers de forma normal.

Por tanto:

```text
❌ NO

LAN A ── DHCP Broadcast ──X── Router ──X── DHCP Server


✅ SÍ

LAN A
  │
  ▼
🌉 RELAY
  │
  │ DHCP reenviado
  ▼
DHCP SERVER
```

El relay recibe la petición en una red y genera/reenvía un mensaje hacia
el servidor DHCP.

En Cisco IOS se utiliza habitualmente:

```text
interface GigabitEthernet0/0
 ip helper-address 192.168.20.10
```

El `ip helper-address` permite reenviar broadcasts UDP, incluyendo DHCP,
hacia el servidor configurado.

------------------------------------------------------------------------

# 🧭 18. ¿Cómo sabe el servidor qué red debe atender?

Cuando existe un relay, el mensaje reenviado incorpora información que
permite al servidor determinar la red desde la que procede la petición.

En Cisco aparece especialmente el campo **giaddr** (*gateway IP
address*).

```text
CLIENTE
192.168.10.0/24
      │
      ▼
R1
192.168.10.1
      │
      │ relay
      ▼
DHCP SERVER
192.168.20.10
```

El servidor puede utilizar esa información para seleccionar el `subnet4`
correspondiente.

------------------------------------------------------------------------

# 🧩 19. DHCP en varias redes

Un único servidor DHCP puede proporcionar configuración a varias
subredes cuando existe conectividad y un mecanismo de relay.

```text
                 DHCP SERVER
                 192.168.30.10
                       │
             ┌─────────┴─────────┐
             │                   │
          RELAY               RELAY
             │                   │
        192.168.10.0/24     192.168.20.0/24
```

Esto evita tener que desplegar un servidor DHCP independiente en cada
LAN.

------------------------------------------------------------------------

# 🧮 20. Opciones DHCP

Una dirección IP no es suficiente para configurar un cliente.

Entre las opciones habituales:

| Opción | Función |
|---|---|
| `routers` | Gateway predeterminado |
| `domain-name-servers` | Servidores DNS |
| `domain-name` | Dominio |
| `host-name` | Nombre del host |
| `ntp-servers` | Servidores NTP |
| `broadcast-address` | Broadcast de la red |

En Kea se pueden establecer mediante `option-data`.

Ejemplo:

``` json
{
  "option-data": [
    {
      "name": "routers",
      "data": "192.168.10.1"
    },
    {
      "name": "domain-name-servers",
      "data": "192.168.10.10"
    }
  ]
}
```

------------------------------------------------------------------------

# 🗃️ 21. Base de datos de concesiones

El servidor necesita conservar información sobre las concesiones.

Kea puede utilizar distintos backends. Para un laboratorio sencillo es
especialmente útil `memfile`.

```text
       KEA DHCP
          │
          ▼
    ┌──────────────┐
    │  LEASE DATA  │
    └──────────────┘
          │
          ├── cliente
          ├── dirección
          ├── estado
          └── tiempos
```

Para entornos más complejos puede utilizarse una base de datos como
MySQL/MariaDB o PostgreSQL, según la arquitectura desplegada.

------------------------------------------------------------------------

# 🛡️ 22. Varios servidores DHCP

El material previo introduce el funcionamiento con varios servidores
DHCP.

Puede utilizarse para:

-   redundancia,
-   continuidad del servicio,
-   reparto de carga,
-   disponibilidad.

Pero **dos servidores independientes no deben configurarse sin
coordinación sobre el mismo pool**, porque podrían producir asignaciones
conflictivas.

------------------------------------------------------------------------

# 🔄 23. Alta disponibilidad y DHCP Failover


La tecnología ha evolucionado. En el laboratorio actual se distinguirán:

-   el concepto de redundancia DHCP,
-   la coordinación de concesiones,
-   las implementaciones concretas de alta disponibilidad.

Kea dispone de mecanismos de **High Availability**, mientras que el
antiguo ISC DHCP Failover pertenece a una tecnología asociada al
software ya retirado.

> ⚠️ No se debe trasladar literalmente una configuración de `dhcpd.conf`
> antigua a Kea. Son productos y modelos de configuración diferentes.

------------------------------------------------------------------------

# 🔐 24. Seguridad DHCP

DHCP es un servicio crítico porque controla parte de la configuración de
red.

Amenazas posibles:

### 🕵️ DHCP Rogue

Un equipo no autorizado actúa como servidor DHCP.

```text
CLIENTE
   │
   ├──── DHCPDISCOVER ────► Servidor legítimo
   │
   └──── DHCPDISCOVER ────► 🚨 Rogue DHCP
```

El cliente podría recibir:

-   gateway malicioso,
-   DNS controlado por un atacante,
-   direcciones incorrectas,
-   información de red manipulada.

### 🛡️ Medidas

En switches gestionables pueden utilizarse mecanismos como **DHCP
Snooping** y políticas de puertos.

------------------------------------------------------------------------

> 🧭 **PREPARACIÓN DIDÁCTICA**
>
> 🧭 **ANTES DE LA PRÁCTICA · QUÉ VAS A OBSERVAR**
> 
> Antes de teclear comandos, identifica el flujo esperado: cliente → descubrimiento → oferta → solicitud → confirmación. La práctica debe terminar con una concesión verificable, no simplemente con un servicio arrancado.

# 🖥️ Administración web con Webmin

La administración de servicios mediante terminal es una competencia fundamental en ASIR, pero una interfaz web puede resultar útil como **capa de observación y administración**, especialmente cuando queremos relacionar parámetros del servicio con su representación gráfica. Webmin no sustituye la comprensión de los ficheros de configuración ni de los comandos: es una interfaz sobre el sistema.

> 🧭 **IDEA CLAVE · WEBMIN ES EL CUADRO DE MANDOS, NO EL MOTOR**
>
> Imagina un automóvil: el volante y el salpicadero facilitan la conducción, pero no sustituyen el conocimiento del motor. En ASIR debemos saber qué cambia Webmin, dónde se almacena esa configuración y cómo comprobarla desde la terminal.

**No se usa una recreación de la interfaz.** Las capturas deben proceder de una instalación real y corresponder a la versión utilizada en el laboratorio. Para esta UT se recomienda consultar la documentación oficial de Webmin:

- [Webmin · documentación general](https://webmin.com/docs/)
- [Webmin · módulo DHCP Server](https://webmin.com/docs/modules/dhcp-server/)
- [Webmin · módulo Kea DHCP Server](https://webmin.com/docs/modules/kea-dhcp-server/)

> **Para el alumno:** si la pantalla de tu versión no coincide con una captura antigua, sigue los nombres de los módulos y comprueba el resultado en la configuración y desde la terminal.

### Flujo recomendado

1. Comprueba el estado del servicio desde la terminal.
2. Abre Webmin y localiza el módulo correspondiente.
3. Realiza un cambio pequeño.
4. Comprueba qué configuración ha cambiado.
5. Valida la configuración.
6. Reinicia o recarga sólo si es necesario.
7. Verifica el resultado desde un cliente.

Comandos que conviene recordar:

```bash
systemctl status kea-dhcp4-server
sudo journalctl -u kea-dhcp4-server -n 50
sudo kea-dhcp4 -t /etc/kea/kea-dhcp4.conf
```

La práctica correcta es, por tanto, **GUI → configuración → validación → servicio → cliente**.


---

# 🗂️ Antes de las prácticas · localizar la configuración de DHCP

DHCP parece sencillo porque el cliente solo recibe una IP, pero detrás existe un servidor que mantiene **subredes, pools, reservas, opciones y concesiones**. Antes de configurarlo, aprende a encontrar cada pieza.

### 🐧 / 🖥️ Kea DHCP

```text
/etc/kea/
├── kea-dhcp4.conf           → configuración principal de DHCPv4
├── kea-dhcp6.conf           → configuración de DHCPv6, si se utiliza
└── kea-ctrl-agent.conf      → API de control, cuando está habilitada

/var/lib/kea/                → ficheros de estado/concesiones según backend
/var/log/                    → registros, según configuración del sistema
```

Comandos fundamentales:
sudo ls -la /etc/kea
sudo sed -n '1,260p' /etc/kea/kea-dhcp4.conf
sudo systemctl status kea-dhcp4-server
sudo journalctl -u kea-dhcp4-server --no-pager

Antes de reiniciar un servicio, valida la sintaxis con la herramienta de comprobación disponible en tu instalación. Una configuración DHCP incorrecta puede dejar sin dirección a toda una LAN.

### 🖥️ Webmin

Si la instalación dispone de un módulo DHCP compatible, localízalo en **Servers**. No des por hecho que Webmin dispone de un módulo actualizado para cada versión de Kea: si el módulo no representa una directiva, edítala y valídala desde CLI.

> 🧠 **Analogía:** el fichero de configuración es el plano de la oficina; Webmin es la recepción que te ayuda a llegar a algunas salas, pero el técnico debe conocer el plano completo.


> 👨‍🏫 **Criterio de corrección de las prácticas**
>
> La solución de referencia no se reduce a una configuración final. Se valoran el proceso, la capacidad para localizar ficheros, validar la sintaxis, comprobar puertos y conectividad, interpretar logs y justificar técnicamente cada decisión. Cuando el ejercicio admita varias soluciones, cualquier solución equivalente y correctamente justificada es válida.
# 🧪 25. PRÁCTICA 1 --- DHCP gráfico en Packet Tracer · Arnor

> **Escenario v6.6:** Arnor es el primer servidor DHCP de la red interna. Se configura exclusivamente mediante la interfaz gráfica de **Server-PT** para que el alumno comprenda el ámbito, las opciones y las reservas antes de trasladar exactamente el mismo servicio al router Mordor mediante CLI.

## Objetivo

Configurar desde cero el servidor **Arnor** y entregar por DHCP la configuración de los clientes de la red `192.168.10.0/24`.

### Parámetros obligatorios

| Parámetro | Valor |
|---|---|
| Arnor | `192.168.10.192/24` |
| Puerta de enlace | `192.168.10.254` |
| DNS | `192.168.20.192` |
| Dominio | `tierramedia.jc` |
| Pool dinámico | `192.168.10.1–192.168.10.32` |
| Reserva Gondor | `192.168.10.64` |
| Reserva Rohan | `192.168.10.65` |

> Las direcciones `.64` y `.65` quedan fuera del rango dinámico y se mantienen mediante reservas. Arnor `.192` es una dirección fija del servidor y tampoco debe ser entregada dinámicamente.

## 25.1. Configurar la red de Arnor

En **Arnor → Desktop → IP Configuration → Static**:

```text
IP Address:      192.168.10.192
Subnet Mask:     255.255.255.0
Default Gateway: 192.168.10.254
DNS Server:      192.168.20.192
```

Comprueba desde **Command Prompt**:

```text
ipconfig /all
ping 192.168.10.254
ping 192.168.20.192
```

Si falla el primer ping, no continúes con DHCP: primero corrige la conectividad de UT1.

## 25.2. Activar DHCP en Arnor

En **Services → DHCP**:

1. Selecciona **DHCP: On**.
2. Crea el pool `TIERRAMEDIA-LAN`.
3. Introduce:

```text
Default Gateway:   192.168.10.254
DNS Server:        192.168.20.192
Start IP Address:  192.168.10.1
Subnet Mask:       255.255.255.0
Maximum Number of Users: 32
Domain Name:       tierramedia.jc
```

4. Guarda con **Add**.

El objetivo es que el ámbito dinámico cubra `.1`–`.32`. Si la versión de Packet Tracer no muestra un campo de dominio, se documentará esa limitación y se conservarán gateway y DNS como opciones obligatorias.

## 25.3. Direcciones ya establecidas: Gondor y Rohan

La interfaz gráfica estándar de **Server-PT** de Packet Tracer permite crear ámbitos DHCP, pero no ofrece en todas las versiones una tabla de reservas por MAC equivalente a la de un servidor DHCP completo. Por tanto, en esta **primera fase visual** no se debe simular una reserva que la herramienta no implementa.

Mantén temporalmente las direcciones ya establecidas de los clientes como configuración estática:

```text
Gondor → 192.168.10.64/24
Rohan  → 192.168.10.65/24
Gateway → 192.168.10.254
DNS → 192.168.20.192
```

La reserva DHCP real se implementará en la **segunda fase**, cuando sustituyamos Arnor por Mordor mediante CLI. Así se distingue claramente entre:

```text
IP estática del cliente
        ≠
reserva DHCP basada en identidad del cliente
```

> **Criterio de calidad:** si una función no está disponible en la GUI concreta de Packet Tracer, se documenta la limitación y se demuestra correctamente en el entorno que sí la soporta.

## 25.4. Probar el ámbito dinámico

Para demostrar la asignación dinámica en esta fase, utiliza un cliente de prueba o cambia temporalmente un equipo no reservado a **Desktop → IP Configuration → DHCP**.

Resultado esperado:

```text
IP → 192.168.10.1–192.168.10.32
Gateway → 192.168.10.254
DNS → 192.168.20.192
```

Gondor y Rohan conservan `.64` y `.65` hasta la fase CLI de Mordor, donde se convertirán en reservas DHCP reales.

## 25.5. Batería de pruebas

```text
ipconfig /all
ping 192.168.10.254
ping 192.168.20.192
```

En **Simulation Mode**, filtra `DHCP` y observa:

```text
DHCPDISCOVER → DHCPOFFER → DHCPREQUEST → DHCPACK
```

### Evidencias mínimas

- configuración IP de Arnor;
- pantalla **Services → DHCP** con el pool;
- direcciones estáticas `.64` y `.65` de Gondor/Rohan;
- concesión dinámica de un cliente de prueba;
- `ipconfig /all` de ambos clientes;
- secuencia DORA en Simulation Mode;
- conectividad con gateway y DNS.

---

# 🧪 26. PRÁCTICA 2 --- Sustituir Arnor por DHCP en Mordor (CLI)

> **Mismo servicio, otra capa de administración:** ahora se elimina la función DHCP de Arnor y se configura **Mordor**, el Router-PT, para proporcionar exactamente el mismo ámbito, opciones y reservas.

## 26.1. Desactivar Arnor

En **Arnor → Services → DHCP**, selecciona **DHCP: Off**. Mantén Arnor con su IP `192.168.10.192` para futuras ampliaciones, pero ya no debe responder a DHCP.

## 26.2. Configurar Mordor

En la CLI:

```text
Mordor> enable
Mordor# configure terminal
Mordor(config)# service dhcp
Mordor(config)# ip dhcp excluded-address 192.168.10.33 192.168.10.63
Mordor(config)# ip dhcp excluded-address 192.168.10.66 192.168.10.254
Mordor(config)# ip dhcp excluded-address 192.168.10.192
Mordor(config)# ip dhcp pool TIERRAMEDIA-LAN
Mordor(dhcp-config)# network 192.168.10.0 255.255.255.0
Mordor(dhcp-config)# default-router 192.168.10.254
Mordor(dhcp-config)# dns-server 192.168.20.192
Mordor(dhcp-config)# domain-name tierramedia.jc
Mordor(dhcp-config)# exit
Mordor(config)# end
Mordor# copy running-config startup-config
```

> El rango `.1–.32` queda disponible. `.64`, `.65`, `.192` y la infraestructura del router quedan protegidos mediante exclusiones.

### Reservas

Cisco IOS permite definir reservas mediante pools host. La forma exacta del `client-identifier` depende de la identificación DHCP que utilice Packet Tracer. Por ello, primero se obtiene la información del cliente y después se construye la reserva; nunca se inventa el identificador.

```text
Mordor# show ip dhcp binding
Mordor# show ip dhcp pool
Mordor# show ip dhcp conflict
Mordor# show running-config | section dhcp
```

Cuando la versión de Packet Tracer admita el identificador de cliente:

```text
ip dhcp pool GONDOR
 host 192.168.10.64 255.255.255.0
 client-identifier <CLIENT-ID-GONDOR>
 default-router 192.168.10.254
 dns-server 192.168.20.192
 domain-name tierramedia.jc

ip dhcp pool ROHAN
 host 192.168.10.65 255.255.255.0
 client-identifier <CLIENT-ID-ROHAN>
 default-router 192.168.10.254
 dns-server 192.168.20.192
 domain-name tierramedia.jc
```

### 26.3. Comprobación de equivalencia

El resultado de la fase CLI debe ser funcionalmente equivalente a Arnor:

```text
                FASE 1                    FASE 2
             Arnor DHCP                Mordor DHCP
                 │                          │
                 └────── mismos clientes ──┘
                         │
               misma puerta de enlace
                         │
                    mismo DNS
                         │
                mismas reservas
```

La evidencia debe demostrar que, tras apagar DHCP en Arnor, los clientes siguen obteniendo configuración desde Mordor.

# 🧪 27. PRÁCTICA 3 --- DHCP Relay como ampliación

> 🔎 **PISTAS ESPECÍFICAS · -- DHCP en varias redes con relay**
>
> **Qué debes fijar:** Distingue cliente, servidor, ámbito, reserva y relay. Comprueba la concesión real y no des por válida la configuración hasta verificar las opciones recibidas.
>
> **Evidencia:** La evidencia mínima debe mostrar la configuración concedida al cliente y, cuando sea posible, el intercambio o la concesión en el servidor.
>
> **Pista de troubleshooting:** si el resultado no coincide con tu predicción, vuelve al último punto demostrado, conserva la evidencia y modifica una sola variable antes de repetir la prueba.


## Objetivo

Comprobar que un servidor DHCP puede atender clientes de varias redes
mediante un router configurado como relay.

```text
       LAN 10                         LAN 20
192.168.10.0/24                 192.168.20.0/24
      │                                │
      ▼                                ▼
     PCs                              PCs
      │                                │
      └──────────── Router ────────────┘
                       │
                       │
                 DHCP Server
                 192.168.30.10
```

En cada interfaz del router que reciba peticiones DHCP se configurará:

```text
ip helper-address 192.168.30.10
```

Cisco documenta `ip helper-address` como mecanismo para reenviar
broadcasts UDP, incluidos BOOTP y DHCP. 

### Evidencias

El alumno deberá demostrar:

-   IP obtenida en LAN 10.
-   IP obtenida en LAN 20.
-   Gateway correcto en cada LAN.
-   Que ambas concesiones proceden del mismo servidor.
-   Diferencias entre los pools.

------------------------------------------------------------------------


### 🧭 Guía de resolución y comprobación

Esta práctica se considera resuelta cuando puedes **explicar y demostrar** el resultado, no solo cuando el comando termina sin errores. Sigue siempre esta secuencia:

1. **Identifica el estado inicial.** Anota interfaces, direcciones, rutas y servicios que ya estaban activos.
2. **Aplica el cambio mínimo.** No modifiques varias cosas a la vez: si algo falla, necesitas saber qué cambio lo provocó.
3. **Valida inmediatamente.** Comprueba la sintaxis o el estado del servicio antes de probar desde el cliente.
4. **Prueba desde el punto de vista del usuario.** Una configuración correcta debe producir el comportamiento esperado desde el cliente, no solo desde el servidor.
5. **Observa evidencias.** Conserva la salida de comandos, logs, capturas de tráfico y capturas de pantalla que demuestren el resultado.

**Comandos de referencia para esta práctica:**

- `ip addr`
- `ip route`
- `sudo systemctl status kea-dhcp4-server`
- `sudo journalctl -u kea-dhcp4-server --no-pager`
- `ip neigh`

> 💡 **Si algo falla:** no empieces reiniciando. Compara primero **estado → configuración → logs → puertos → red → cliente**. Un reinicio puede ocultar la causa y hacer más difícil aprender de la incidencia.

### 🧪 Rúbrica de evaluación

| Criterio | Puntos | Evidencia esperada |
|---|---:|---|
| Comprensión del objetivo y del protocolo | 2 | Explica qué servicio/protocolo está utilizando y por qué. |
| Preparación y configuración | 2 | Ficheros, comandos o topología correctamente preparados. |
| Verificación funcional | 2 | Demuestra el resultado desde un cliente o herramienta adecuada. |
| Diagnóstico y razonamiento | 2 | Utiliza evidencias para justificar la solución. |
| Documentación técnica | 1 | Incluye comandos, configuraciones y capturas relevantes. |
| Seguridad y buenas prácticas | 1 | Aplica permisos, exposición de puertos y credenciales con criterio. |
| **Total** | **10** | **Superación recomendada: ≥ 5 puntos y práctica funcional.** |


# 🧪 28. PRÁCTICA 4 --- DHCP en VirtualBox · Mordor + Kea

> **Arquitectura v6.6:** en VirtualBox no se utiliza Arnor como servidor DHCP. La función DHCP se concentra en la VM **Mordor**. Gondor y Rohan son clientes; Lothlorien es el servidor de servicios; Rivendel queda reservado para tareas auxiliares.

## 27.1. Inventario de las cinco VMs

| VM | IP | Papel |
|---|---|---|
| Mordor | `192.168.10.254/24` | router/gateway + DHCP |
| Gondor | DHCP / reserva `.64` | cliente |
| Rohan | DHCP / reserva `.65` | cliente |
| Lothlorien | `192.168.20.192/24` | servicios principales |
| Rivendel | `192.168.20.193/24` | servicios auxiliares/pruebas |

La topología física/virtual se documenta en el [Anexo de arquitectura v6.6](ANEXO-XIX-Arquitectura-Laboratorio-v6.6.md).

## 27.2. Ubicación y sintaxis de Kea

La configuración IPv4 está en:

```text
/etc/kea/kea-dhcp4.conf
```

Es un fichero **JSON**. La estructura fundamental es:

```text
Dhcp4
 ├── interfaces-config
 ├── lease-database
 ├── subnet4
 │    ├── subnet
 │    ├── pools
 │    └── option-data
 └── reservations
```

Ejemplo de ámbito didáctico:

```json
{
  "Dhcp4": {
    "interfaces-config": { "interfaces": [ "enp0s8" ] },
    "subnet4": [
      {
        "subnet": "192.168.10.0/24",
        "pools": [ { "pool": "192.168.10.1-192.168.10.32" } ],
        "option-data": [
          { "name": "routers", "data": "192.168.10.254" },
          { "name": "domain-name-servers", "data": "192.168.20.192" },
          { "name": "domain-name", "data": "tierramedia.jc" }
        ]
      }
    ]
  }
}
```

Las reservas `.64` y `.65` se añaden en la sección `reservations` utilizando la identificación real de los clientes.

## 27.3. Instalar y configurar

En Mordor:

```bash
sudo apt update
sudo apt install kea-dhcp4-server
sudo cp /etc/kea/kea-dhcp4.conf /etc/kea/kea-dhcp4.conf.bak
sudo -e -- /etc/kea/kea-dhcp4.conf
```

Valida el JSON antes de reiniciar:

```bash
python3 -m json.tool /etc/kea/kea-dhcp4.conf >/dev/null
```

Después:

```bash
sudo systemctl restart kea-dhcp4-server
sudo systemctl enable kea-dhcp4-server
sudo systemctl status kea-dhcp4-server --no-pager
sudo journalctl -u kea-dhcp4-server -b --no-pager
```

> **Persistencia:** en Ubuntu, el cambio persistente es el fichero JSON; `systemctl enable` hace persistente el arranque del servicio. Primero valida y prueba; después persiste.

## 27.4. Pruebas

En Gondor y Rohan:

```bash
ip addr
ip route
resolvectl status
```

En Mordor:

```bash
sudo journalctl -u kea-dhcp4-server -f
sudo ss -lunp | grep ':67'
```

La prueba funcional debe demostrar:

```text
Gondor → 192.168.10.64
Rohan  → 192.168.10.65
DNS    → 192.168.20.192
GW     → 192.168.10.254
```

## 27.5. Webmin

Webmin dispone de un módulo **DHCP Server**, pero su documentación oficial describe el módulo para el servidor ISC DHCP, no como editor universal de Kea. Por tanto:

- para **Kea**, la fuente de verdad es `/etc/kea/kea-dhcp4.conf` y su validación CLI;
- si la instalación concreta ofrece un módulo Kea compatible, se puede usar para observar/editar;
- si no lo ofrece, no se debe presentar el módulo ISC como si administrara Kea.

La interfaz Webmin queda como capa de apoyo, no como sustituto de la configuración JSON.

# 🧪 29. Validar la configuración de Kea
### 🧭 Guía de resolución y comprobación

**Puntos a conseguir:** dejar el sistema en el estado solicitado, poder explicar qué protocolo interviene, comprobarlo desde un cliente y aportar evidencias reproducibles.

1. **Preparar** el entorno y registrar el estado inicial.
2. **Construir** solo el siguiente elemento necesario.
3. **Validar** sintaxis y servicio.
4. **Probar** desde el cliente.
5. **Observar** puertos, logs y tráfico cuando proceda.
6. **Documentar** configuración, comandos y capturas.


#### Solución de referencia

La configuración mínima de Kea debe contener una subred y un pool coherentes con la red de la práctica. Como patrón didáctico:

```json
{
  "Dhcp4": {
    "interfaces-config": {"interfaces": ["<interfaz>"]},
    "subnet4": [
      {
        "subnet": "192.168.10.0/24",
        "pools": [{"pool": "192.168.10.100-192.168.10.199"}],
        "option-data": [
          {"name": "routers", "data": "192.168.10.1"},
          {"name": "domain-name-servers", "data": "192.168.10.10"}
        ]
      }
    ]
  }
}
```

Adapta interfaz, red, pool, gateway y DNS a la topología real. Después valida la configuración, reinicia o recarga el servicio y demuestra la concesión desde un cliente.


### 📸 Evidencias y capturas

Incluye, cuando aporte información, una captura de la topología, del fichero o interfaz configurada, del estado del servicio y de la prueba final. Cada captura debe llevar una frase que explique **qué demuestra**; una imagen sin interpretación no constituye una evidencia técnica suficiente.

### 🧪 Rúbrica de evaluación

| Criterio | Puntos |
|---|---:|
| Comprensión del servicio/protocolo | 2 |
| Configuración y proceso | 2 |
| Funcionamiento demostrado | 2 |
| Diagnóstico y razonamiento | 2 |
| Documentación y evidencias | 1 |
| Seguridad y buenas prácticas | 1 |
| **Total** | **10** |


Antes de iniciar el servicio conviene comprobar que el JSON es válido y
que la configuración puede ser aceptada por Kea.

La comprobación recomendada para Kea es:

``` bash
sudo kea-dhcp4 -t /etc/kea/kea-dhcp4.conf
```

`-t` comprueba la configuración e informa del primer error detectado.

Consulta la ayuda y la versión disponibles:

``` bash
kea-dhcp4 -V
kea-dhcp4 --help
```

Después verifica el estado del servicio:

``` bash
systemctl status kea-dhcp4-server
```

Y revisa los registros:

``` bash
journalctl -u kea-dhcp4-server
```

### Objetivo de diagnóstico

Si el cliente no obtiene IP, no debemos empezar modificando el pool al
azar.

Seguir:

```text
1️⃣ ¿La interfaz del servidor existe?
        ↓
2️⃣ ¿Tiene IP en la LAN?
        ↓
3️⃣ ¿Kea escucha en esa interfaz?
        ↓
4️⃣ ¿El servicio está activo?
        ↓
5️⃣ ¿El pool pertenece a esa subred?
        ↓
6️⃣ ¿El cliente está realmente en DHCP?
        ↓
7️⃣ ¿Hay firewall?
        ↓
8️⃣ ¿Qué muestran los paquetes?
```

------------------------------------------------------------------------

# 🧷 30. PRÁCTICA 4 --- Reservas DHCP con Kea

> 🔎 **PISTAS ESPECÍFICAS · -- Reservas DHCP con Kea**
>
> **Qué debes fijar:** Distingue cliente, servidor, ámbito, reserva y relay. Comprueba la concesión real y no des por válida la configuración hasta verificar las opciones recibidas.
>
> **Evidencia:** La evidencia mínima debe mostrar la configuración concedida al cliente y, cuando sea posible, el intercambio o la concesión en el servidor.
>
> **Pista de troubleshooting:** si el resultado no coincide con tu predicción, vuelve al último punto demostrado, conserva la evidencia y modifica una sola variable antes de repetir la prueba.


Configura:

```text
Cliente A
MAC: 00:11:22:33:44:55
IP reservada: 192.168.10.50
```

Ejemplo:

``` json
{
  "reservations": [
    {
      "hw-address": "00:11:22:33:44:55",
      "ip-address": "192.168.10.50"
    }
  ]
}
```

### Comprobaciones

1.  Arrancar cliente.
2.  Solicitar configuración DHCP.
3.  Verificar que recibe `.50`.
4.  Liberar la concesión.
5.  Volver a solicitar configuración.
6.  Comprobar que continúa recibiendo `.50`.

La documentación de Kea permite reservas mediante `hw-address`,
`client-id`, DUID y otros identificadores. 

------------------------------------------------------------------------

# 📡 31. PRÁCTICA 5 --- Analizar DHCP con Wireshark

> 🔎 **PISTAS ESPECÍFICAS · -- Analizar DHCP con Wireshark**
>
> **Qué debes fijar:** Empieza por observar antes de modificar: identifica interlocutores, puertos, protocolo y resultado esperado. Formula qué campo o paquete debería confirmar tu hipótesis. Distingue cliente, servidor, ámbito, reserva y relay. Comprueba la concesión real y no des por válida la configuración hasta verificar las opciones recibidas.
>
> **Evidencia:** La evidencia debe incluir el filtro aplicado y al menos un paquete/campo que confirme la hipótesis.
>
> **Pista de troubleshooting:** si el resultado no coincide con tu predicción, vuelve al último punto demostrado, conserva la evidencia y modifica una sola variable antes de repetir la prueba.


## Objetivo

Dejar de considerar DHCP como una "caja negra".

Captura tráfico en la interfaz correspondiente.

Filtro Wireshark:

```text
dhcp
```

o:

```text
bootp
```

Busca:

```text
DHCPDISCOVER
DHCPOFFER
DHCPREQUEST
DHCPACK
```

### Actividad

Construye una tabla:

| Mensaje | Origen | Destino | Función |
|---|---|---|---|
| DISCOVER | Cliente | Broadcast/servidor | Buscar servidores |
| OFFER | Servidor | Cliente | Ofrecer configuración |
| REQUEST | Cliente | Servidor | Solicitar oferta |
| ACK | Servidor | Cliente | Confirmar concesión |

### Reto

Identifica en una captura:

-   dirección MAC del cliente,
-   dirección ofrecida,
-   servidor DHCP,
-   gateway,
-   DNS,
-   duración de la concesión.

------------------------------------------------------------------------

# 🌉 32. PRÁCTICA 6 --- DHCP Relay

> 🔎 **PISTAS ESPECÍFICAS · -- DHCP Relay**
>
> **Qué debes fijar:** Distingue cliente, servidor, ámbito, reserva y relay. Comprueba la concesión real y no des por válida la configuración hasta verificar las opciones recibidas.
>
> **Evidencia:** La evidencia mínima debe mostrar la configuración concedida al cliente y, cuando sea posible, el intercambio o la concesión en el servidor.
>
> **Pista de troubleshooting:** si el resultado no coincide con tu predicción, vuelve al último punto demostrado, conserva la evidencia y modifica una sola variable antes de repetir la prueba.


Construye:

```text
LAN A                         LAN B
192.168.10.0/24               192.168.20.0/24
     │                              │
    PC ──────── Router ─────────────┘
                   │
                   ▼
             DHCP SERVER
             192.168.20.10
```

En la interfaz del router conectada a la LAN A:

```text
ip helper-address 192.168.20.10
```

### Comprobación

El cliente de LAN A debe recibir una dirección del pool correspondiente
a `192.168.10.0/24`.

> 🧠 **Pregunta clave**
>
> ¿Cómo puede el servidor saber que la solicitud procede de LAN A si el
> servidor está en LAN B?
>
> Analiza el campo `giaddr` en una captura.

------------------------------------------------------------------------

# 🧪 33. PRÁCTICA 7 --- WSL como cliente y analizador DHCP

WSL **no se utilizará como servidor DHCP**. Su papel en esta UT es analizar y comprobar la red desde el punto de vista de un cliente Linux.

### Comprobaciones

```bash
ip addr
ip route
resolvectl status
ss -lunp
```

Para observar DHCP cuando la interfaz de WSL permita capturar ese tráfico:

```bash
sudo tcpdump -ni any 'udp port 67 or udp port 68'
```

Relaciona la observación con la práctica de VirtualBox:

```text
Mordor (DHCP) → DHCPDISCOVER
             → DHCPOFFER
             → DHCPREQUEST
             → DHCPACK
                    ↓
                 cliente
```

> WSL sirve aquí para **observar y diagnosticar**; el servidor DHCP real de la práctica se encuentra en Mordor (VirtualBox) o en Mordor (Packet Tracer).

# 🧭 Guía de resolución y comprobación

Esta práctica se considera resuelta cuando puedes **explicar y demostrar** el resultado, no solo cuando el comando termina sin errores. Sigue siempre esta secuencia:

1. **Identifica el estado inicial.** Anota interfaces, direcciones, rutas y servicios que ya estaban activos.
2. **Aplica el cambio mínimo.** No modifiques varias cosas a la vez: si algo falla, necesitas saber qué cambio lo provocó.
3. **Valida inmediatamente.** Comprueba la sintaxis o el estado del servicio antes de probar desde el cliente.
4. **Prueba desde el punto de vista del usuario.** Una configuración correcta debe producir el comportamiento esperado desde el cliente, no solo desde el servidor.
5. **Observa evidencias.** Conserva la salida de comandos, logs, capturas de tráfico y capturas de pantalla que demuestren el resultado.

**Comandos de referencia para esta práctica:**

- `ip addr`
- `ip route`
- `sudo systemctl status kea-dhcp4-server`
- `sudo journalctl -u kea-dhcp4-server --no-pager`
- `ip neigh`

> 💡 **Si algo falla:** no empieces reiniciando. Compara primero **estado → configuración → logs → puertos → red → cliente**. Un reinicio puede ocultar la causa y hacer más difícil aprender de la incidencia.

### 🧪 Rúbrica de evaluación

| Criterio | Puntos | Evidencia esperada |
|---|---:|---|
| Comprensión del objetivo y del protocolo | 2 | Explica qué servicio/protocolo está utilizando y por qué. |
| Preparación y configuración | 2 | Ficheros, comandos o topología correctamente preparados. |
| Verificación funcional | 2 | Demuestra el resultado desde un cliente o herramienta adecuada. |
| Diagnóstico y razonamiento | 2 | Utiliza evidencias para justificar la solución. |
| Documentación técnica | 1 | Incluye comandos, configuraciones y capturas relevantes. |
| Seguridad y buenas prácticas | 1 | Aplica permisos, exposición de puertos y credenciales con criterio. |
| **Total** | **10** | **Superación recomendada: ≥ 5 puntos y práctica funcional.** |


# 🧰 34. Herramientas fundamentales

## `ip addr`

``` bash
ip addr
```

Muestra interfaces y direcciones.

## `ip route`

``` bash
ip route
```

Muestra la tabla de routing.

## `ping`

``` bash
ping 192.168.10.1
```

Comprueba conectividad IP.

## `ss`

``` bash
ss -lunp
```

Permite observar sockets UDP.

## `journalctl`

``` bash
journalctl -u kea-dhcp4-server
```

Permite estudiar los registros del servicio.

## Wireshark

Permite analizar el intercambio DHCP paquete a paquete.

------------------------------------------------------------------------

# 🚨 35. Errores frecuentes

### ❌ El cliente obtiene `169.254.x.x`

Posibles causas:

-   no encuentra servidor DHCP,
-   servidor apagado,
-   relay incorrecto,
-   interfaz equivocada,
-   firewall,
-   VLAN incorrecta.

### ❌ El cliente recibe IP pero no navega

Comprobar:

```text
IP       ✓
Máscara  ✓
Gateway  ?
DNS      ?
Routing  ?
```

### ❌ El servidor funciona pero no entrega IP

Comprobar:

``` bash
systemctl status kea-dhcp4-server
journalctl -u kea-dhcp4-server
```

### ❌ Kea no arranca

Revisar:

-   JSON mal formado,
-   nombre de interfaz incorrecto,
-   puerto ocupado,
-   permisos,
-   configuración incompatible.

### ❌ Dos servidores entregan direcciones

No asumir automáticamente que existe alta disponibilidad.

Comprobar qué servidores están respondiendo.

------------------------------------------------------------------------

# 🔎 36. Diagnóstico sistemático

Utiliza siempre este árbol:

```text
                 CLIENTE SIN IP
                       │
                       ▼
             ¿Interfaz activa?
                 /          \
               NO            SÍ
               │              │
           solucionar         ▼
                         ¿DHCP activo?
                          /        \
                        NO          SÍ
                        │            │
                    revisar          ▼
                              ¿Servidor visible?
                               /           \
                             NO             SÍ
                             │               │
                         relay/VLAN       ▼
                                      ¿Pool válido?
                                       /       \
                                     NO         SÍ
                                     │           │
                                  corregir      ▼
                                           ¿Firewall?
```

------------------------------------------------------------------------

# 📚 37. DHCP y otros servicios

DHCP suele trabajar conjuntamente con:

```text
        DHCP
         │
    ┌────┼────┐
    │    │    │
   IP   DNS  Gateway
    │    │    │
    └────┼────┘
         │
       RED IP
```

DHCP proporciona información de configuración.

DNS resuelve nombres.

El router proporciona conectividad entre redes.

No deben confundirse las funciones.

------------------------------------------------------------------------

## 📘 Glosario esencial de la UT

| Término | Definición |
|---|---|
| **DORA** | Secuencia clásica DHCPDISCOVER, DHCPOFFER, DHCPREQUEST y DHCPACK. |
| **Concesión / lease** | Asignación temporal de parámetros de red a un cliente. |
| **Exclusión** | Dirección o intervalo que se reserva para que el pool no lo entregue dinámicamente. |
| **Kea** | Implementación moderna de servicios DHCP mantenida por Internet Systems Consortium. |
| **Pool** | Conjunto de direcciones que el servidor puede asignar dinámicamente. |
| **Reserva** | Asociación de una identidad de cliente con una asignación establecida por configuración. |
| **Relay** | Agente que reenvía mensajes DHCP entre clientes y servidores a través de redes distintas. |
| **Rogue DHCP** | Servidor DHCP no autorizado que responde a clientes y puede introducir parámetros incorrectos. |
| **DHCPv4** | Servicio DHCP para IPv4. |
| **DHCPv6** | Servicio DHCP para IPv6, con un modelo de operación diferente al de DHCPv4. |


## 🧩 Banco de ejercicios propuestos

Estos ejercicios complementan las prácticas. Se pueden utilizar para clase, trabajo autónomo, recuperación o examen práctico.

### 1. Un cliente obtiene IP pero no DNS. ¿Qué parte de la concesión inspeccionarías?

**Solución de referencia:** Opciones DHCP entregadas, especialmente `domain-name-servers`, además de la conectividad con el DNS indicado.

### 2. Dos servidores DHCP contestan. ¿Qué evidencia necesitas antes de modificar configuraciones?

**Solución de referencia:** Captura DHCP y logs para identificar qué servidor responde, junto con MAC/identificador y opciones ofrecidas.

### 3. Explica por qué DHCP relay es necesario cuando el servidor está en otra red.

**Solución de referencia:** Los broadcasts DHCP iniciales no atraviesan routers de forma normal; el relay convierte el intercambio local en tráfico dirigido al servidor.

### 4. Diseña una reserva para una impresora que debe conservar siempre la misma IP.

**Solución de referencia:** Identificar un dato estable del cliente, asociarlo a una IP fuera de conflictos y validar la concesión y su renovación.

# 🧠 38. Resumen

```text
                    DHCP
                     │
       ┌─────────────┼─────────────┐
       │             │             │
    CLIENTE       SERVIDOR       RELAY
       │             │             │
       └─────── DORA ──────────────┘
                     │
               CONFIGURACIÓN
                     │
          ┌──────────┼──────────┐
          │          │          │
          IP       GATEWAY      DNS
          │          │          │
          └──────────┼──────────┘
                     │
                  LEASE
                     │
             🔄 RENOVACIÓN
```

Las ideas fundamentales son:

1.  DHCP automatiza la configuración IP.
2.  El servidor administra direcciones y opciones.
3.  Las concesiones tienen duración.
4.  DORA resume la obtención inicial.
5.  DHCP utiliza UDP 67/68 en IP.
6.  Los broadcasts no atraviesan routers normalmente.
7.  Un relay permite atender clientes de otras redes.
8.  Las reservas permiten asociar clientes con direcciones concretas.
9.  Un único servidor puede atender varias subredes mediante relay.
10. ISC DHCP es software histórico y está EOL; el laboratorio
    actualizado utiliza Kea.

------------------------------------------------------------------------

# ❓ 39. Autoevaluación

1.  ¿Qué problema principal resuelve DHCP?
2.  ¿Qué parámetros puede recibir un cliente DHCP?
3.  ¿Qué diferencia existe entre una asignación dinámica y una reserva?
4.  ¿Qué es una concesión (*lease*)?
5.  ¿Qué significa DORA?
6.  ¿Qué función cumple DHCPDISCOVER?
7.  ¿Qué función cumple DHCPREQUEST?
8.  ¿Qué puertos UDP utiliza DHCP?
9.  ¿Por qué es necesario un DHCP relay cuando cliente y servidor están
    en redes diferentes?
10. ¿Qué función cumple `ip helper-address` en Cisco?
11. ¿Qué información permite al servidor determinar la subred atendida
    por un relay?
12. ¿Qué es un pool DHCP?
13. ¿Para qué sirven las exclusiones?
14. ¿Qué diferencia existe entre una reserva DHCP y una IP estática
    configurada en el cliente?
15. ¿Qué es un DHCP rogue?
16. ¿Qué herramienta permite observar DHCP paquete a paquete?
17. ¿Qué utilidad tiene `journalctl -u kea-dhcp4-server`?
18. ¿Qué software sustituye actualmente a ISC DHCP en el laboratorio?
19. ¿Qué estructura de configuración utiliza Kea DHCP para definir
    subredes?
20. ¿Por qué WSL no se utilizará como plataforma principal para una
    topología DHCP de varias LAN?

------------------------------------------------------------------------

# ✅ Solucionario de la autoevaluación

> 📌 Intenta responder primero sin consultar esta sección.

### 1. ¿Qué problema principal resuelve DHCP?

Automatiza la entrega de parámetros de configuración de red a los
clientes, reduciendo la configuración manual y los errores asociados.

### 2. ¿Qué parámetros puede recibir un cliente DHCP?

Como mínimo, una dirección IP y su máscara; habitualmente también
gateway, servidores DNS y otros parámetros mediante opciones DHCP.

### 3. ¿Qué diferencia existe entre asignación dinámica y reserva?

En la asignación dinámica se selecciona una dirección disponible de un
pool durante una concesión. En una reserva, el servidor asocia un
cliente determinado con una dirección concreta.

### 4. ¿Qué es una concesión?

Es el periodo durante el cual un cliente puede utilizar una
configuración asignada por DHCP.

### 5. ¿Qué significa DORA?

```text
D = DHCPDISCOVER
O = DHCPOFFER
R = DHCPREQUEST
A = DHCPACK
```

Es la secuencia clásica de obtención inicial de una concesión DHCP.

### 6. ¿Qué función cumple DHCPDISCOVER?

Permite al cliente localizar servidores DHCP disponibles.

### 7. ¿Qué función cumple DHCPREQUEST?

Permite al cliente solicitar formalmente una configuración/oferta y
comunicar la selección de servidor en el proceso correspondiente.

### 8. ¿Qué puertos UDP utiliza DHCP?

**UDP 67** en el servidor y **UDP 68** en el cliente.

### 9. ¿Por qué es necesario DHCP relay entre redes diferentes?

Porque las peticiones iniciales DHCP utilizan difusión y los routers no
reenvían normalmente esos broadcasts entre redes. El relay recibe la
petición y la reenvía al servidor DHCP.

### 10. ¿Qué función cumple `ip helper-address`?

Configura en Cisco el destino al que se reenvían determinadas difusiones
UDP, incluidas las peticiones DHCP. 

### 11. ¿Qué información permite determinar la subred?

En un escenario con relay Cisco, el campo **giaddr** permite al servidor
identificar la red desde la que procede la petición y seleccionar el
ámbito correspondiente. 

### 12. ¿Qué es un pool DHCP?

Es un conjunto de direcciones disponibles para asignación dinámica a los
clientes.

### 13. ¿Para qué sirven las exclusiones?

Para impedir que determinadas direcciones sean asignadas dinámicamente,
normalmente porque están reservadas para infraestructura o dispositivos
con direccionamiento controlado.

### 14. ¿Reserva DHCP o IP estática?

En una reserva el cliente sigue utilizando DHCP y el servidor decide qué
dirección asignarle. Con una IP estática, el parámetro se configura
directamente en el cliente y no depende de una concesión DHCP.

### 15. ¿Qué es un DHCP rogue?

Un servidor DHCP no autorizado que responde a clientes y puede
proporcionar parámetros de red incorrectos o maliciosos.

### 16. ¿Qué herramienta permite observar DHCP paquete a paquete?

**Wireshark**.

### 17. ¿Qué utilidad tiene `journalctl -u kea-dhcp4-server`?

Permite consultar los registros del servicio Kea DHCP gestionado por
systemd y utilizarlos para diagnosticar errores.

### 18. ¿Qué software sustituye actualmente a ISC DHCP?

**Kea DHCP**. ISC declaró ISC DHCP EOL en 2022 y recomienda migrar a
Kea. 

### 19. ¿Qué estructura utiliza Kea DHCP para definir subredes?

La estructura `subnet4`, que contiene las subredes DHCP y puede
incluir `pools` y opciones asociadas. 

### 20. ¿Por qué WSL no es la plataforma principal para una topología DHCP de

varias LAN?

Porque WSL proporciona un entorno Linux integrado con una arquitectura
de red propia; para estudiar varias LAN, routers, relay e interfaces
virtuales independientes resulta más controlable utilizar Packet Tracer
o máquinas virtuales con VirtualBox.

------------------------------------------------------------------------


## 🔄 Transferencia profesional

> 👨‍💼 **Cambia una condición sin cambiar el problema.** Una vez resuelto el escenario de referencia, modifica una sola condición —subred, servidor, nombre, firewall, número de clientes o entorno de despliegue— y adapta la solución. Explica qué permanece igual y qué debe cambiar.

### Reto de transferencia

1. Identifica qué ha cambiado.
2. Predice qué partes de la arquitectura afectará.
3. Localiza la configuración que tendrás que adaptar.
4. Haz el cambio mínimo.
5. Valida y vuelve a probar.
6. Documenta la diferencia respecto al escenario inicial.


## 🔗 Recursos oficiales y ampliación

- **Kea DHCP documentation:** https://kea.readthedocs.io/
- **Ubuntu networking:** https://ubuntu.com/server/docs/how-to/networking

**Uso recomendado:** consultar la documentación oficial para comprobar sintaxis, compatibilidad y cambios de versión antes de reutilizar una receta.

# 📝 Test de repaso

## 1. ¿Qué problema resuelve principalmente DHCP?
A. Cifrar las conexiones
B. Automatizar parámetros de configuración de red
C. Resolver nombres DNS
D. Transferir ficheros

## 2. ¿Qué secuencia resume la obtención inicial de una concesión DHCP?
A. SYN/ACK/FIN
B. GET/POST/PUT
C. DORA
D. MX/SOA/NS

## 3. ¿Qué puertos utiliza tradicionalmente DHCPv4?
A. UDP 67 servidor y UDP 68 cliente
B. TCP 67 servidor y TCP 68 cliente
C. UDP 53 servidor y cliente
D. TCP 80 y 443

## 4. ¿Por qué se necesita un relay cuando cliente y servidor están en redes IP distintas?
A. Porque DHCP utiliza únicamente TCP
B. Porque los broadcasts DHCP iniciales no atraviesan routers normalmente
C. Porque el servidor no puede tener IP
D. Porque DNS debe retransmitir DHCP

## 5. ¿Qué elemento permite reservar una dirección para un cliente concreto?
A. Una reserva DHCP
B. Un registro MX
C. Un Virtual Host
D. Un certificado TLS

## 6. ¿Qué comando permite observar el estado del servicio Kea?
A. `dig`
B. `systemctl status kea-dhcp4-server`
C. `curl -I`
D. `sshd -t`

## 7. ¿Qué herramienta resulta especialmente útil para comprobar el proceso DORA paquete a paquete?
A. Wireshark/tcpdump
B. `passwd`
C. `tar`
D. `nano`

## 8. ¿Qué describe mejor un pool DHCP?
A. Conjunto de direcciones que el servidor puede conceder
B. Lista de servidores DNS raíz
C. Grupo de puertos TCP
D. Fichero de logs

## 9. ¿Qué ocurre normalmente si un cliente DHCP se encuentra en otra subred y no existe relay?
A. El router convierte automáticamente cualquier broadcast en DHCP
B. El servidor recibe siempre el broadcast directamente
C. El proceso inicial no llega normalmente al servidor DHCP de otra red
D. DNS asume la función de DHCP

## 10. ¿Qué software se utiliza en este material como servidor DHCP actualizado?
A. ISC DHCP 4.x
B. Kea DHCP
C. BIND9
D. Dovecot

### ✅ Respuestas

| Pregunta | Respuesta |
|---:|:---:|
| 1 | **B** |
| 2 | **C** |
| 3 | **A** |
| 4 | **B** |
| 5 | **A** |
| 6 | **B** |
| 7 | **A** |
| 8 | **A** |
| 9 | **C** |
| 10 | **B** |

# 🏆 40. Reto final --- Diseña una infraestructura DHCP

Construye una infraestructura con:

```text
                  INTERNET
                     │
                ┌────┴────┐
                │ ROUTER  │
                └────┬────┘
                     │
             ┌───────┴────────┐
             │                │
          LAN-A             LAN-B
     192.168.10.0/24    192.168.20.0/24
             │                │
             └───────┬────────┘
                     │
                  RELAY
                     │
                     ▼
             DHCP SERVER
       VirtualBox + Ubuntu 26.04 Server
                     │
                    KEA
```

## Requisitos

El servidor deberá:

-   Atender las dos redes.
-   Entregar IP dinámica.
-   Proporcionar gateway.
-   Proporcionar DNS.
-   Tener al menos una reserva.
-   Mantener concesiones.
-   Registrar actividad.
-   Permitir analizar el proceso mediante Wireshark.

## Evidencias

Entrega:

1.  Diagrama de red.
2.  Configuración del servidor.
3.  Configuración del relay.
4.  Captura de `DORA`.
5.  Captura de una concesión.
6.  Captura de una renovación.
7.  Evidencia de la reserva.
8.  Tabla de direccionamiento.
9.  Diagnóstico de un fallo provocado por el profesor.

------------------------------------------------------------------------

---

## 🔷 v6.6 · Laboratorio Tierra Media

### Caso integrado

La secuencia de DHCP es deliberadamente comparativa:

```text
1. Arnor → DHCP gráfico en Packet Tracer
2. Mordor → mismo servicio mediante CLI de Router-PT
3. Mordor → DHCP real con Kea en VirtualBox
4. WSL → solo cliente/análisis; nunca servidor DHCP
```

### Configuración real en VirtualBox

`/etc/kea/kea-dhcp4.conf` → **JSON**. Validación:

```bash
python3 -m json.tool /etc/kea/kea-dhcp4.conf >/dev/null
systemctl status kea-dhcp4-server --no-pager
journalctl -u kea-dhcp4-server -b --no-pager
```

### Webmin

El módulo oficial **DHCP Server** está orientado al servidor ISC DHCP. Para Kea no debe utilizarse como si fuera un editor universal: si no hay módulo Kea compatible, la administración es CLI/JSON.

### Chuleta

Añadir al inventario: `kea-dhcp4-server`, `journalctl -u`, `ss -lunp`, `tcpdump udp port 67/68`, `python3 -m json.tool`.

### Ruta práctica de tres entornos

```text
PACKET TRACER                         VIRTUALBOX                         WSL
Arnor GUI DHCP → Mordor CLI DHCP  →  Mordor + Kea DHCP             →  cliente/análisis
     .1-.32             .64/.65        .1-.32 + reservas .64/.65       tcpdump DORA
```

**Packet Tracer:** primero Arnor gráfico; después apagar DHCP en Arnor y reproducir el mismo servicio desde Mordor CLI.  
**VirtualBox:** DHCP real con Kea en Mordor; Gondor y Rohan reciben sus reservas.  
**WSL:** solo cliente y análisis; no se instala ningún servidor DHCP.
