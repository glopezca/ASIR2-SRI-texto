# 🌐⚡ Unidad de Trabajo 3 · SERVICIO DE NOMBRES DE DOMINIO (DNS) ⚡🌐

### RA1 · Resolución de nombres.

> **SERVICIOS DE RED E INTERNET · CFGS ASIR · Material docente integral · 2026**
>
> Material autónomo actualizado para el perfil profesional de Técnico Superior en Administración de Sistemas Informáticos en Red. Laboratorio de referencia: **Cisco Packet Tracer**, **WSL2 + Ubuntu 26.04** y **VirtualBox + Ubuntu 26.04 Server**.
>
> ### 🎯 Resultado de aprendizaje trabajado
>
> **RA1.** Administra servicios de resolución de nombres, analizándolos y garantizando la seguridad del servicio.

---


> 🧭 **ANTES DE UTILIZAR DNS**
>
> **DNS (Domain Name System)** es el sistema distribuido que relaciona nombres de dominio con direcciones y otros datos. Un **FQDN (Fully Qualified Domain Name)** es un nombre completamente cualificado. Un **TLD (Top-Level Domain)** es el nivel superior de la jerarquía, como `.es`. Un **servidor autoritativo** contiene información oficial de una zona y un **resolver** consulta DNS en nombre de clientes. **BIND9** es la implementación de servidor DNS utilizada en estas prácticas.

> 🎯 **MISIÓN DE LA UT**
>
> Comprender cómo funciona el sistema DNS desde el cliente hasta los
> servidores autoritativos, y ser capaz de **instalar, configurar,
> consultar, verificar y diagnosticar** un servicio DNS utilizando BIND9
> y herramientas de consulta como `dig`, `host` y `nslookup`.

> 💡 **Idea central**
>
> DNS no es simplemente «traducir nombres a IP». Es una **base de datos
> distribuida y jerárquica**, organizada en zonas y administrada
> mediante servidores que pueden desempeñar diferentes funciones:
> autoritativas, secundarias, caché y reenviadoras.

------------------------------------------------------------------------

# 🧭 Mapa de la unidad

```text
                              🌐 DNS
                               │
              ┌────────────────┼─────────────────┐
              │                │                 │
          🏷️ NOMBRES        🗂️ ZONAS          📦 REGISTROS
              │                │                 │
              │          ┌─────┴─────┐      ┌────┼────┐
              │          │           │      │    │    │
              │       DIRECTA     INVERSA   A    AAAA MX
              │
              └──────────────┬────────────────────┘
                             │
                         🔎 RESOLUCIÓN
                             │
                 ┌───────────┴───────────┐
                 │                       │
             RECURSIVA                 ITERATIVA
                 │                       │
                 └───────────┬───────────┘
                             │
                       🖥️ SERVIDORES
                             │
             ┌───────────────┼────────────────┐
             │               │                │
          PRIMARIO        SECUNDARIO       CACHÉ
             │               │                │
             └───────────────┼────────────────┘
                             │
                         🛡️ SEGURIDAD
                             │
                   DNSSEC · TSIG · TKEY
┌──────────────────────────────────────────────────────────────────────┐
│ 🧪 ENTORNOS · I Packet Tracer · II WSL2 · III VirtualBox · IV Compose │
└──────────────────────────────────────────────────────────────────────┘
```

------------------------------------------------------------------------

> 🧪 **LOS CUATRO ENTORNOS DE PRÁCTICAS**
>
> **I · Cisco Packet Tracer** — simulación de red y protocolos.  
> **II · WSL2 + Ubuntu 26.04** — herramientas, clientes y diagnóstico.  
> **III · VirtualBox + Ubuntu 26.04 Server** — administración de servidores completos.  
> **IV · Docker Compose** — infraestructura reproducible y multicontenedor.



> 📇 **ANALOGÍA · LA GUÍA TELEFÓNICA**
>
> Preguntar «¿dónde está la empresa Juan de Colonia?» y obtener su dirección postal se parece a resolver un nombre mediante DNS. La diferencia fundamental es que DNS no es una guía única: es una **base de datos distribuida y jerárquica**. Si la oficina local no conoce la respuesta, puede preguntar a otros niveles. Por eso conviene distinguir entre servidor autoritativo, servidor de caché y servidor raíz.

# 🎯 0. Objetivos

Al finalizar esta unidad deberás ser capaz de:

-   Explicar qué problema resuelve DNS.
-   Comprender el espacio jerárquico de nombres.
-   Diferenciar nombre relativo, nombre absoluto y FQDN.
-   Distinguir dominio, zona y subdominio.
-   Comprender la función de los servidores raíz y los TLD.
-   Explicar la delegación de dominios.
-   Diferenciar servidores primarios, secundarios, caché y reenviadores.
-   Comprender las consultas recursivas e iterativas.
-   Explicar el funcionamiento de la caché y el TTL.
-   Resolver nombres en sentido directo e inverso.
-   Interpretar registros `SOA`, `NS`, `A`, `AAAA`, `CNAME`, `MX`, `SRV`
    y `PTR`.
-   Configurar zonas DNS en BIND9.
-   Validar configuraciones mediante `named-checkconf` y
    `named-checkzone`.
-   Utilizar `dig`, `host` y `nslookup`.
-   Configurar transferencia de zonas entre servidores.
-   Comprender DNS dinámico.
-   Conocer las amenazas principales contra DNS.
-   Introducir mecanismos de seguridad como DNSSEC y TSIG.

------------------------------------------------------------------------

# 🚀 1. ¿Por qué necesitamos DNS?

Los dispositivos trabajan con direcciones IP, pero las personas
utilizamos nombres.

Recordar:

```text
142.250.x.x
151.101.x.x
...
```

es mucho menos práctico que utilizar:

```text
www.google.com
www.ubuntu.com
www.ejemplo.es
```

DNS proporciona un espacio de nombres que permite asociar nombres con
información de red.

```text
              👤 Usuario
                  │
                  │ www.ejemplo.es
                  ▼
              🔎 RESOLVER
                  │
                  │ consulta DNS
                  ▼
             🖥️ SERVIDOR DNS
                  │
                  │ respuesta
                  ▼
             192.168.10.20
```

------------------------------------------------------------------------

> 🧭 **ANTES DE EMPEZAR · DNS como sistema distribuido**
>
> DNS debe entenderse como una **base de datos distribuida y jerárquica**, no como una tabla local de nombres. Los datos están organizados en una jerarquía y distintos servidores pueden ser responsables de distintas partes del espacio de nombres.

# 🧱 2. DNS es una base de datos distribuida

No existe un único servidor que contenga todos los nombres de Internet.

La información está distribuida entre numerosos servidores y organizada
jerárquicamente.

ICANN describe el DNS como una jerarquía que comienza en la raíz y se
estructura mediante delegaciones hacia los dominios de nivel superior.


```text
                         .
                         │
             ┌───────────┼───────────┐
             │           │           │
            com         org         es
             │                       │
           google                   red
             │                       │
            www                    www
```

La raíz contiene información de referencia hacia los TLD; no contiene
todos los registros de todos los dominios finales. 

------------------------------------------------------------------------

> 🧭 **PREPARACIÓN DIDÁCTICA**
>
> 🧭 **ANTES DE EMPEZAR · NOMBRES FRENTE A DIRECCIONES**
> 
> DNS no es una agenda telefónica gigantesca que contiene todas las respuestas. Es un sistema jerárquico y distribuido. Primero distinguiremos nombre, dominio, zona, servidor autoritativo y resolvedor; después veremos cómo cooperan.

# 🌳 3. Espacio de nombres de dominio

El DNS utiliza una estructura jerárquica.

Ejemplo:

```text
www.sri.iesburgos.es.
│   │   │       │
│   │   │       └── TLD
│   │   └────────── dominio
│   └────────────── subdominio
└────────────────── host
```

Cada nivel está separado mediante un punto.

El árbol completo tiene como raíz:

```text
.
```

Por eso un FQDN completo puede terminar conceptualmente en punto:

```text
www.sri.iesburgos.es.
                    ↑
                  raíz
```

------------------------------------------------------------------------

# 🏷️ 4. Dominios de primer nivel --- TLD

Los TLD (*Top-Level Domains*) aparecen inmediatamente bajo la raíz.

### Genéricos

```text
.com
.org
.net
.info
```

### Geográficos

```text
.es
.fr
.pt
.de
```

Existen además otras categorías y dominios especializados.

> 🧠 **Importante**
>
> El TLD no es simplemente «la última palabra». Es un nivel concreto
> dentro de la jerarquía DNS.

------------------------------------------------------------------------

# 📛 5. Nombre relativo, absoluto y FQDN

Supongamos:

```text
www.asir.example.
```

Un nombre **absoluto** especifica completamente su posición en el árbol.

Un **FQDN** (*Fully Qualified Domain Name*) identifica un nombre
completo dentro del espacio DNS.

```text
www.asir.example.
└───────┬────────┘
       FQDN
```

El punto final representa la raíz.

### Ejemplo

```text
www
 └── asir
      └── example
            └── .
```

------------------------------------------------------------------------

> 🧭 **ANTES DE EMPEZAR · Dominio frente a zona**
>
> En DNS, el nombre que forma parte de la jerarquía y la unidad administrativa que contiene los datos no son necesariamente lo mismo. Por eso distinguiremos **dominio, subdominio, zona y delegación** antes de comenzar a editar archivos de BIND9.

# 🧩 6. Dominio, subdominio y zona

Estos conceptos no deben confundirse.

### Dominio

Es una parte del espacio de nombres.

### Subdominio

Es un dominio situado por debajo de otro.

```text
juandecolonia.jc
└── asir.juandecolonia.jc
    └── aula.asir.juandecolonia.jc
```

### Zona

Es una **parte del espacio DNS administrada por una entidad o servidor
autoritativo**.

Un dominio puede contener una o varias zonas cuando se realizan
delegaciones.

> ⚠️ **Dominio ≠ zona**
>
> Una zona es una unidad administrativa de datos DNS, no simplemente una
> cadena de caracteres del nombre.

------------------------------------------------------------------------

> 🧭 **PREPARACIÓN DIDÁCTICA**
>
> 🧭 **ANTES DE EMPEZAR · RESOLUCIÓN RECURSIVA E ITERATIVA**
> 
> Cuando un cliente pregunta por un nombre, la respuesta puede proceder de una caché o requerir consultas sucesivas. La diferencia entre **recursión** e **iteración** es imprescindible para entender `dig`, los resolvedores y la propagación de errores.

# 🏛️ 7. Delegación

La delegación permite transferir la autoridad administrativa de una
parte del espacio de nombres a otros servidores.

Ejemplo:

```text
              juandecolonia.jc
                  │
                  │ delegación
                  ▼
          ┌─────────────────┐
          │ asir.juandecolonia.jc│
          └─────────────────┘
                  │
            DNS propio
```

La zona padre mantiene información que permite encontrar los servidores
autoritativos de la zona hija.

La delegación es un elemento fundamental de la arquitectura DNS
jerárquica. 

------------------------------------------------------------------------

# 🌐 8. Servidores raíz

Los servidores raíz proporcionan referencias hacia los servidores de los
TLD.

Actualmente existen **13 identidades de servidores raíz**, operadas por
distintos operadores, que se sirven mediante una infraestructura global
de más de 1500 instancias. 

```text
CLIENTE
   │
   ▼
RESOLVER
   │
   ▼
ROOT ─────────► .es
                  │
                  ▼
                .es DNS
                  │
                  ▼
             juandecolonia.jc
                  │
                  ▼
             www.juandecolonia.jc
```

> 💡 No hay que imaginar los root servers como «el servidor DNS de
> Internet». Su función principal es proporcionar referencias en la raíz
> de la jerarquía.

------------------------------------------------------------------------

> 🧭 **ANTES DE EMPEZAR · Resolución DNS**
>
> Resolver un nombre significa obtener la información necesaria a partir de la jerarquía DNS. En este proceso aparecerán los conceptos de **recursividad, iteración, caché, servidor autoritativo y servidor reenviador**.

# 🔎 9. Resolución de nombres

Resolver un nombre significa obtener la información DNS asociada.

Ejemplo:

```text
www.juandecolonia.jc
       │
       ▼
    ¿qué IP?
       │
       ▼
192.0.2.20
```

La resolución puede ser:

-   directa,
-   inversa.

Y las consultas pueden realizarse:

-   recursivamente,
-   iterativamente.

------------------------------------------------------------------------

> 🧑‍💼 **ANALOGÍA · UN RECEPCIONISTA QUE SE ENCARGA DE TODO**
>
> Si preguntas en recepción por una dirección y el recepcionista se compromete a hacer todas las llamadas necesarias hasta conseguirla, está asumiendo la responsabilidad de completar la búsqueda. Esa es la intuición de una consulta recursiva: el cliente espera que el resolvedor continúe preguntando hasta obtener una respuesta final o un error.

# 🔄 10. Resolución recursiva

En una consulta recursiva, el servidor al que pregunta el cliente asume
la responsabilidad de obtener una respuesta completa o un error.

```text
CLIENTE
   │
   │ www.juandecolonia.jc ?
   ▼
DNS RECURSOR
   │
   ├──► ROOT
   │
   ├──► .es
   │
   ├──► juandecolonia.jc
   │
   └──► respuesta
            │
            ▼
        CLIENTE
```

El cliente no necesita realizar cada consulta intermedia.

------------------------------------------------------------------------

> 🗺️ **ANALOGÍA · UNA CADENA DE INDICACIONES**
>
> En una consulta iterativa, una oficina puede no darte la dirección final, pero sí indicarte cuál es la siguiente oficina que debes consultar. El proceso se parece a seguir un mapa de ventanillas: cada una aporta el siguiente paso de la ruta.

# 🔁 11. Resolución iterativa

En una consulta iterativa el servidor responde con la mejor información
que tiene, pudiendo proporcionar una referencia a otro servidor.

```text
Resolver ──► Root
              │
              └──► servidores .es

Resolver ──► .es
              │
              └──► NS de juandecolonia.jc

Resolver ──► juandecolonia.jc
              │
              └──► respuesta
```

El proceso recursivo completo puede estar compuesto internamente por
varias consultas iterativas.

------------------------------------------------------------------------

# 🧠 12. Recursividad vs. iteración

| Característica | Consulta recursiva | Consulta iterativa |
|---|---|---|
| ¿El servidor consultado debe resolver por el cliente? | Sí, si acepta la recursión | No necesariamente |
| ¿Puede devolver una referencia a otro servidor? | Puede hacerlo internamente | Sí, es habitual |
| Carga de trabajo | Mayor para el resolvedor | Menor por consulta |
| Uso típico | Cliente → resolvedor | Resolvedor → servidores autoritativos |

### Analiza con `dig`

``` bash
dig www.juandecolonia.jc
```

Consulta un resolver.

Para observar el proceso:

``` bash
dig +trace www.juandecolonia.jc
```

`dig` es una herramienta específica para interrogar servidores DNS y es
una de las herramientas habituales de diagnóstico de DNS.


------------------------------------------------------------------------

# 🗃️ 13. Zonas DNS

Un servidor autoritativo almacena información de una o más zonas.

En BIND9, Ubuntu organiza habitualmente la configuración bajo:

```text
/etc/bind/
```

Incluyendo:

```text
named.conf
named.conf.options
named.conf.local
named.conf.default-zones
```

Ubuntu documenta esta estructura para BIND9. 

------------------------------------------------------------------------

# 🖥️ 14. Tipos de servidores DNS

Un mismo servidor puede desempeñar varias funciones dependiendo de la
configuración.

## 14.1. Primario

Mantiene los datos de una zona de forma autoritativa.

En BIND9 actual se utiliza el término **primary** en la configuración de
zonas.

## 14.2. Secundario

Obtiene una copia de la zona desde otro servidor autoritativo mediante
transferencias de zona.

## 14.3. Caché

Almacena temporalmente respuestas para evitar repetir consultas.

## 14.4. Reenviador

Envía consultas a otros servidores DNS.

```text
             BIND9
               │
       ┌───────┼────────┐
       │       │        │
   primary  secondary  cache
                       │
                    forwarder
```

Ubuntu documenta que BIND9 puede funcionar simultáneamente como caché,
primary y secondary dependiendo de las zonas que sirva.


------------------------------------------------------------------------

# 🧾 15. Registros de recursos --- RR
### 📊 Registros DNS esenciales

| Registro | Función | Ejemplo conceptual |
|---|---|---|
| `A` | Nombre → IP | `www → 192.0.2.10` |
| `AAAA` | Nombre → IPv6 | `www → 2001:db8::10` |
| `CNAME` | Alias → nombre canónico | `web → servidor` |
| `MX` | Servidor de correo del dominio | `dominio → mail.dominio` |
| `NS` | Servidor autoritativo de una zona | `dominio → ns1.dominio` |
| `PTR` | IP → nombre | `10.2.0.192 → host` |
| `SOA` | Información administrativa de la zona | serial, refresh, retry... |
| `TXT` | Texto asociado al nombre | SPF, verificaciones, etc. |



La información DNS se almacena mediante **Resource Records (RR)**.

Formato conceptual:

```text
NOMBRE   TTL   CLASE   TIPO   DATOS
```

Ejemplo:

```text
www.juandecolonia.jc.   3600   IN   A   192.0.2.10
```

BIND9 utiliza registros de recursos para describir las características
de una zona. 

------------------------------------------------------------------------

# 🟦 16. Registro A

Asocia un nombre con una dirección IP.

```text
www.juandecolonia.jc.   IN   A   192.0.2.10
```

```text
www.juandecolonia.jc
       │
       ▼
  192.0.2.10
```

Consulta:

``` bash
dig www.juandecolonia.jc A
```

------------------------------------------------------------------------

# 🟪 17. Registro AAAA

Asocia un nombre con una dirección IPv6.

```text
www.juandecolonia.jc.   IN   AAAA   2001:db8::10
```

Consulta:

``` bash
dig www.juandecolonia.jc AAAA
```

------------------------------------------------------------------------

> 🧭 **PREPARACIÓN DIDÁCTICA**
>
> 🧭 **ANTES DE EMPEZAR · BIND9**
> 
> BIND9 implementa funciones DNS concretas sobre los conceptos que acabamos de estudiar. Primero entenderemos qué papel desempeña cada fichero; después escribiremos configuraciones y finalmente validaremos sintaxis y resolución.

# 🟨 18. Registro CNAME

Crea un alias para otro nombre.

```text
web.juandecolonia.jc.   IN   CNAME   www.juandecolonia.jc.
```

```text
web
 │
 └──── CNAME ───► www
                    │
                    └── A ──► 192.0.2.10
```

> ⚠️ Un CNAME apunta a un **nombre**, no directamente a una dirección
> IP.

------------------------------------------------------------------------

# 🟥 19. Registro MX

Indica qué servidores reciben correo para un dominio.

```text
juandecolonia.jc.   IN   MX   10   mail.juandecolonia.jc.
```

El número es la **preferencia**: un valor menor tiene prioridad sobre
uno mayor.

Ejemplo:

```text
MX 10 mail1.juandecolonia.jc.
MX 20 mail2.juandecolonia.jc.
```

------------------------------------------------------------------------

# 🟩 20. Registro NS

Indica los servidores de nombres autoritativos de una zona.

```text
juandecolonia.jc.   IN   NS   ns1.juandecolonia.jc.
juandecolonia.jc.   IN   NS   ns2.juandecolonia.jc.
```

Una zona debería contar con servidores autoritativos adecuadamente
configurados.

------------------------------------------------------------------------

# 🟧 21. Registro PTR

Se utiliza en la resolución inversa.

```text
10.2.0.192.in-addr.arpa.
             │
             ▼
        www.juandecolonia.jc.
```

Consulta:

``` bash
dig -x 192.0.2.10
```

------------------------------------------------------------------------

# 🟦 22. Registro SOA

El registro **SOA (Start of Authority)** contiene información
fundamental sobre una zona.

Ejemplo conceptual:

```text
juandecolonia.jc. IN SOA ns1.juandecolonia.jc. hostmaster.juandecolonia.jc. (
    2026091701
    3600
    600
    604800
    300
)
```

Incluye valores como:

-   servidor primario,
-   contacto administrativo,
-   número de serie,
-   refresh,
-   retry,
-   expire,
-   TTL negativo.

------------------------------------------------------------------------

# 🔢 23. Número de serie del SOA

El `serial` permite detectar cambios en la zona.

Ejemplo:

```text
2026091701
```

Al modificar la zona:

```text
2026091702
```

Los servidores secundarios pueden utilizar este valor para determinar si
deben actualizar su copia.

> 🧠 **Regla práctica**
>
> Cada modificación relevante de una zona debe acompañarse de una
> actualización coherente del número de serie.

------------------------------------------------------------------------

# ⏱️ 24. TTL

**TTL --- Time To Live** determina durante cuánto tiempo una respuesta
puede permanecer en caché.

```text
Consulta
   │
   ▼
Respuesta
   │
   ├── TTL 3600
   │
   ▼
Caché durante un máximo aproximado de 3600 s
```

Un TTL bajo permite cambios más rápidos, pero puede aumentar las
consultas.

Un TTL alto reduce consultas, pero prolonga la permanencia de
información en caché.

------------------------------------------------------------------------

# 🔄 25. TTL positivo y negativo

No solo se almacenan respuestas positivas.

También puede almacenarse información sobre nombres que no existen.

```text
www.juandecolonia.jc  ──► existe ──► A
noexiste.es      ──► NXDOMAIN
```

El TTL negativo controla durante cuánto tiempo puede mantenerse en caché
determinada información negativa.

------------------------------------------------------------------------

# 🗂️ 26. Resolución inversa

La resolución directa:

```text
NOMBRE ─────► IP
```

La resolución inversa:

```text
IP ──────────► NOMBRE
```

Para IP se utiliza:

```text
in-addr.arpa
```

Ejemplo:

```text
192.0.2.10

10.2.0.192.in-addr.arpa
```

Consulta:

``` bash
dig -x 192.0.2.10
```

------------------------------------------------------------------------

# 🧩 27. Zonas directas e inversas

Una configuración completa puede tener:

```text
Zona directa
juandecolonia.jc
     │
     └── www → 192.0.2.10


Zona inversa
2.0.192.in-addr.arpa
     │
     └── 10 → www.juandecolonia.jc
```

Ambas zonas son independientes y deben configurarse correctamente.

------------------------------------------------------------------------

# 🖥️ 28. Cliente DNS --- Resolver

Las aplicaciones normalmente no consultan directamente todos los
servidores DNS de Internet.

Utilizan un **resolver** proporcionado por el sistema operativo o por
una biblioteca.

En Linux moderno pueden intervenir:

```text
Aplicación
    │
    ▼
Resolver
    │
    ▼
Configuración DNS del sistema
    │
    ▼
Servidor DNS
```

Herramientas útiles:

``` bash
resolvectl status
resolvectl query www.juandecolonia.jc
```

------------------------------------------------------------------------

# 🔍 29. `dig`

`dig` proporciona información detallada sobre las consultas.

``` bash
dig www.juandecolonia.jc
```

Especificar servidor:

``` bash
dig @192.168.10.10 www.juandecolonia.jc
```

Tipo concreto:

``` bash
dig @192.168.10.10 www.juandecolonia.jc MX
```

Respuesta corta:

``` bash
dig +short www.juandecolonia.jc
```

Resolución inversa:

``` bash
dig -x 192.168.10.10
```

Traza:

``` bash
dig +trace www.juandecolonia.jc
```

------------------------------------------------------------------------

# 🔎 30. `host`

Herramienta sencilla para consultas rápidas.

``` bash
host www.juandecolonia.jc
```

Consulta inversa:

``` bash
host 192.168.10.10
```

Consultar un servidor concreto:

``` bash
host www.juandecolonia.jc 192.168.10.10
```

------------------------------------------------------------------------

# 🧰 31. `nslookup`

Aunque `dig` suele ser preferible para diagnóstico detallado, `nslookup`
continúa siendo útil para consultas rápidas y para comparar el
comportamiento entre plataformas.

``` bash
nslookup www.juandecolonia.jc
```

Modo interactivo:

```text
> server 192.168.10.10
> set type=MX
> juandecolonia.jc
```

------------------------------------------------------------------------


---

# 🗂️ Antes de las prácticas · árbol de configuración de BIND9

En DNS no basta con saber escribir `dig`. Debes poder localizar **qué fichero define la zona, cuál declara la zona y qué fichero controla el comportamiento global del servidor**.

```text
/etc/bind/
├── named.conf                 → punto de entrada principal
├── named.conf.options        → opciones globales, recursión, forwarders…
├── named.conf.local          → zonas locales declaradas por el administrador
├── named.conf.default-zones  → zonas estándar de instalación
└── db.juandecolonia.jc       → fichero de datos de la zona autoritativa

/var/log/                      → logs, si se han configurado por archivo/syslog/journald
```

Inspección inicial:
sudo find /etc/bind -maxdepth 1 -type f -print
sudo sed -n '1,220p' /etc/bind/named.conf.options
sudo sed -n '1,220p' /etc/bind/named.conf.local
sudo named-checkconf
sudo named-checkzone juandecolonia.jc /etc/bind/db.juandecolonia.jc

### 🖥️ Webmin

En Webmin, el módulo **Servers → BIND DNS Server** permite inspeccionar y editar zonas y determinadas opciones. Después de cualquier cambio importante, vuelve a la CLI y ejecuta `named-checkconf` y `named-checkzone`.

> 💡 **Secuencia profesional:** localizar → leer → modificar → validar → recargar → consultar con `dig` → revisar logs.



> 👨‍🏫 **Criterio de corrección de las prácticas**
>
> La solución de referencia no se reduce a una configuración final. Se valoran el proceso, la capacidad para localizar ficheros, validar la sintaxis, comprobar puertos y conectividad, interpretar logs y justificar técnicamente cada decisión. Cuando el ejercicio admita varias soluciones, cualquier solución equivalente y correctamente justificada es válida.
# 🧪 32. PRÁCTICA 1 --- Explorar DNS desde WSL2
> 🧭 **PREPARACIÓN DE LA PRÁCTICA**
>
> **1 · Sitúate.** Lee primero el objetivo y localiza en la unidad el concepto que estamos llevando a la práctica. No empieces copiando comandos: primero debes poder explicar qué componente estamos construyendo y para qué sirve.
>
> **2 · Prepara el entorno.** Comprueba si esta práctica utiliza **Entorno I · Packet Tracer**, **Entorno II · WSL2**, **Entorno III · VirtualBox + Ubuntu 26.04 Server** o **Anexo VI · Entorno IV · Docker Compose**. Verifica conectividad, nombres, interfaces y estado de los servicios antes de modificar nada.
>
> **3 · Predice.** Antes de ejecutar un comando importante, escribe qué esperas que ocurra. Por ejemplo: «después de `ss -lnt`, espero encontrar el servicio escuchando en TCP/80». Esta pequeña predicción convierte la práctica en una investigación y no en una receta.
>
> **4 · Construye paso a paso.** Cada número debe dejar el sistema en un estado ligeramente más completo que el anterior. Después de cada bloque, realiza una comprobación corta. Si el paso 4 depende del 3, no avances hasta que el 3 funcione.
>
> **5 · Diagnostica si falla.** No empieces reiniciando. Sigue esta secuencia: **estado → configuración → logs → puertos → red → prueba desde el cliente**. Conserva las órdenes utilizadas y la evidencia del fallo.
>
> **6 · Demuestra.** La práctica termina cuando puedes demostrar el resultado con una evidencia: captura, salida de comando, conexión desde cliente, fichero de configuración o tráfico observado.
>
> **7 · Explica.** Cierra con una breve explicación técnica: qué has configurado, qué protocolo interviene, qué puerto utiliza, cómo se verifica y qué error sería el primero que investigarías si dejara de funcionar.




## Objetivo

Observar el funcionamiento del resolver del sistema.

Ejecuta:

``` bash
resolvectl status
```

Después:

``` bash
dig www.juandecolonia.jc
```

``` bash
dig +short www.juandecolonia.jc
```

``` bash
dig www.juandecolonia.jc NS
```

``` bash
dig www.juandecolonia.jc MX
```

``` bash
dig -x 8.8.8.8
```

Y finalmente:

``` bash
dig +trace www.juandecolonia.jc
```

### Entrega

Una tabla:

  Consulta            Servidor utilizado   Tipo     Resultado
  ------------------- -------------------- -------- -----------
  `www.juandecolonia.jc`                        A/AAAA   
  `juandecolonia.jc NS`                         NS       
  `juandecolonia.jc MX`                         MX       
  `8.8.8.8`                                PTR      

------------------------------------------------------------------------


### 🧭 Guía de resolución y comprobación

Esta práctica se considera resuelta cuando puedes **explicar y demostrar** el resultado, no solo cuando el comando termina sin errores. Sigue siempre esta secuencia:

1. **Identifica el estado inicial.** Anota interfaces, direcciones, rutas y servicios que ya estaban activos.
2. **Aplica el cambio mínimo.** No modifiques varias cosas a la vez: si algo falla, necesitas saber qué cambio lo provocó.
3. **Valida inmediatamente.** Comprueba la sintaxis o el estado del servicio antes de probar desde el cliente.
4. **Prueba desde el punto de vista del usuario.** Una configuración correcta debe producir el comportamiento esperado desde el cliente, no solo desde el servidor.
5. **Observa evidencias.** Conserva la salida de comandos, logs, capturas de tráfico y capturas de pantalla que demuestren el resultado.

**Comandos de referencia para esta práctica:**

- `resolvectl status`
- `dig @<DNS> <nombre>`
- `sudo named-checkconf`
- `sudo named-checkzone <zona> <fichero>`
- `sudo journalctl -u bind9 --no-pager`

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


# 🧪 33. PRÁCTICA 2 --- Instalar BIND9 en VirtualBox + Ubuntu 26.04 Server
> 🧭 **PREPARACIÓN DE LA PRÁCTICA**
>
> **1 · Sitúate.** Lee primero el objetivo y localiza en la unidad el concepto que estamos llevando a la práctica. No empieces copiando comandos: primero debes poder explicar qué componente estamos construyendo y para qué sirve.
>
> **2 · Prepara el entorno.** Comprueba si esta práctica utiliza **Entorno I · Packet Tracer**, **Entorno II · WSL2**, **Entorno III · VirtualBox + Ubuntu 26.04 Server** o **Anexo VI · Entorno IV · Docker Compose**. Verifica conectividad, nombres, interfaces y estado de los servicios antes de modificar nada.
>
> **3 · Predice.** Antes de ejecutar un comando importante, escribe qué esperas que ocurra. Por ejemplo: «después de `ss -lnt`, espero encontrar el servicio escuchando en TCP/80». Esta pequeña predicción convierte la práctica en una investigación y no en una receta.
>
> **4 · Construye paso a paso.** Cada número debe dejar el sistema en un estado ligeramente más completo que el anterior. Después de cada bloque, realiza una comprobación corta. Si el paso 4 depende del 3, no avances hasta que el 3 funcione.
>
> **5 · Diagnostica si falla.** No empieces reiniciando. Sigue esta secuencia: **estado → configuración → logs → puertos → red → prueba desde el cliente**. Conserva las órdenes utilizadas y la evidencia del fallo.
>
> **6 · Demuestra.** La práctica termina cuando puedes demostrar el resultado con una evidencia: captura, salida de comando, conexión desde cliente, fichero de configuración o tráfico observado.
>
> **7 · Explica.** Cierra con una breve explicación técnica: qué has configurado, qué protocolo interviene, qué puerto utiliza, cómo se verifica y qué error sería el primero que investigarías si dejara de funcionar.




## Topología

```text
               VirtualBox
                    │
          ┌─────────┴─────────┐
          │                   │
       🖥️ DNS01             💻 CLIENTE
       192.168.10.10        DHCP/estática
          │                   │
          └──── SRI-DNS ──────┘
```

Ubuntu documenta BIND9 como servidor DNS y mantiene su configuración
bajo `/etc/bind`. 

Instalación:

``` bash
sudo apt update
sudo apt install bind9 bind9-utils bind9-dnsutils
```

Comprobar:

``` bash
systemctl status bind9
```

Versión:

``` bash
named -v
```

En Ubuntu 26.04 LTS el paquete `bind9` pertenece a la rama BIND 9.20.24
en los repositorios publicados para `resolute`.


------------------------------------------------------------------------


### 🧭 Guía de resolución y comprobación

Esta práctica se considera resuelta cuando puedes **explicar y demostrar** el resultado, no solo cuando el comando termina sin errores. Sigue siempre esta secuencia:

1. **Identifica el estado inicial.** Anota interfaces, direcciones, rutas y servicios que ya estaban activos.
2. **Aplica el cambio mínimo.** No modifiques varias cosas a la vez: si algo falla, necesitas saber qué cambio lo provocó.
3. **Valida inmediatamente.** Comprueba la sintaxis o el estado del servicio antes de probar desde el cliente.
4. **Prueba desde el punto de vista del usuario.** Una configuración correcta debe producir el comportamiento esperado desde el cliente, no solo desde el servidor.
5. **Observa evidencias.** Conserva la salida de comandos, logs, capturas de tráfico y capturas de pantalla que demuestren el resultado.

**Comandos de referencia para esta práctica:**

- `resolvectl status`
- `dig @<DNS> <nombre>`
- `sudo named-checkconf`
- `sudo named-checkzone <zona> <fichero>`
- `sudo journalctl -u bind9 --no-pager`

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


# 🧪 34. PRÁCTICA 3 --- Servidor DNS caché/reenviador
> 🧭 **PREPARACIÓN DE LA PRÁCTICA**
>
> **1 · Sitúate.** Lee primero el objetivo y localiza en la unidad el concepto que estamos llevando a la práctica. No empieces copiando comandos: primero debes poder explicar qué componente estamos construyendo y para qué sirve.
>
> **2 · Prepara el entorno.** Comprueba si esta práctica utiliza **Entorno I · Packet Tracer**, **Entorno II · WSL2**, **Entorno III · VirtualBox + Ubuntu 26.04 Server** o **Anexo VI · Entorno IV · Docker Compose**. Verifica conectividad, nombres, interfaces y estado de los servicios antes de modificar nada.
>
> **3 · Predice.** Antes de ejecutar un comando importante, escribe qué esperas que ocurra. Por ejemplo: «después de `ss -lnt`, espero encontrar el servicio escuchando en TCP/80». Esta pequeña predicción convierte la práctica en una investigación y no en una receta.
>
> **4 · Construye paso a paso.** Cada número debe dejar el sistema en un estado ligeramente más completo que el anterior. Después de cada bloque, realiza una comprobación corta. Si el paso 4 depende del 3, no avances hasta que el 3 funcione.
>
> **5 · Diagnostica si falla.** No empieces reiniciando. Sigue esta secuencia: **estado → configuración → logs → puertos → red → prueba desde el cliente**. Conserva las órdenes utilizadas y la evidencia del fallo.
>
> **6 · Demuestra.** La práctica termina cuando puedes demostrar el resultado con una evidencia: captura, salida de comando, conexión desde cliente, fichero de configuración o tráfico observado.
>
> **7 · Explica.** Cierra con una breve explicación técnica: qué has configurado, qué protocolo interviene, qué puerto utiliza, cómo se verifica y qué error sería el primero que investigarías si dejara de funcionar.




## Objetivo

Configurar BIND9 para proporcionar resolución a una LAN y utilizar
*forwarders* para las consultas externas.

Archivo:

```text
/etc/bind/named.conf.options
```

Estructura conceptual:

```text
options {
    directory "/var/cache/bind";

    recursion yes;

    forwarders {
        1.1.1.1;
        8.8.8.8;
    };
};
```

> ⚠️ En una red real los forwarders deben elegirse según las políticas y
> requisitos de la organización. Los valores anteriores son únicamente
> un ejemplo de laboratorio.

Ubuntu documenta el uso de `forwarders` en BIND9 para un servidor caché.


### Verificación

``` bash
dig @127.0.0.1 www.juandecolonia.jc
```

Repite la consulta y compara:

```text
;; Query time:
```

El almacenamiento en caché puede reducir el tiempo necesario para
resolver consultas repetidas.

------------------------------------------------------------------------


### 🧭 Guía de resolución y comprobación

Esta práctica se considera resuelta cuando puedes **explicar y demostrar** el resultado, no solo cuando el comando termina sin errores. Sigue siempre esta secuencia:

1. **Identifica el estado inicial.** Anota interfaces, direcciones, rutas y servicios que ya estaban activos.
2. **Aplica el cambio mínimo.** No modifiques varias cosas a la vez: si algo falla, necesitas saber qué cambio lo provocó.
3. **Valida inmediatamente.** Comprueba la sintaxis o el estado del servicio antes de probar desde el cliente.
4. **Prueba desde el punto de vista del usuario.** Una configuración correcta debe producir el comportamiento esperado desde el cliente, no solo desde el servidor.
5. **Observa evidencias.** Conserva la salida de comandos, logs, capturas de tráfico y capturas de pantalla que demuestren el resultado.

**Comandos de referencia para esta práctica:**

- `resolvectl status`
- `dig @<DNS> <nombre>`
- `sudo named-checkconf`
- `sudo named-checkzone <zona> <fichero>`
- `sudo journalctl -u bind9 --no-pager`

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


# 🧪 35. PRÁCTICA 4 --- Crear una zona autoritativa
> 🧭 **PREPARACIÓN DE LA PRÁCTICA**
>
> **1 · Sitúate.** Lee primero el objetivo y localiza en la unidad el concepto que estamos llevando a la práctica. No empieces copiando comandos: primero debes poder explicar qué componente estamos construyendo y para qué sirve.
>
> **2 · Prepara el entorno.** Comprueba si esta práctica utiliza **Entorno I · Packet Tracer**, **Entorno II · WSL2**, **Entorno III · VirtualBox + Ubuntu 26.04 Server** o **Anexo VI · Entorno IV · Docker Compose**. Verifica conectividad, nombres, interfaces y estado de los servicios antes de modificar nada.
>
> **3 · Predice.** Antes de ejecutar un comando importante, escribe qué esperas que ocurra. Por ejemplo: «después de `ss -lnt`, espero encontrar el servicio escuchando en TCP/80». Esta pequeña predicción convierte la práctica en una investigación y no en una receta.
>
> **4 · Construye paso a paso.** Cada número debe dejar el sistema en un estado ligeramente más completo que el anterior. Después de cada bloque, realiza una comprobación corta. Si el paso 4 depende del 3, no avances hasta que el 3 funcione.
>
> **5 · Diagnostica si falla.** No empieces reiniciando. Sigue esta secuencia: **estado → configuración → logs → puertos → red → prueba desde el cliente**. Conserva las órdenes utilizadas y la evidencia del fallo.
>
> **6 · Demuestra.** La práctica termina cuando puedes demostrar el resultado con una evidencia: captura, salida de comando, conexión desde cliente, fichero de configuración o tráfico observado.
>
> **7 · Explica.** Cierra con una breve explicación técnica: qué has configurado, qué protocolo interviene, qué puerto utiliza, cómo se verifica y qué error sería el primero que investigarías si dejara de funcionar.




Dominio de laboratorio:

```text
asir.test
```

Servidor:

```text
dns01.asir.test
192.168.10.10
```

Edita:

``` bash
sudo nano /etc/bind/named.conf.local
```

Añade:

```text
zone "asir.test" {
    type primary;
    file "/etc/bind/db.asir.test";
};
```

Crea:

``` bash
sudo nano /etc/bind/db.asir.test
```

Ejemplo:

```text
$TTL 3600
@   IN SOA dns01.asir.test. admin.asir.test. (
        2026091701
        3600
        600
        604800
        300
)

    IN NS dns01.asir.test.

dns01   IN A 192.168.10.10
www     IN A 192.168.10.20
mail    IN A 192.168.10.30
```

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
- `ss -lntup`
- `journalctl -b --no-pager`
- `ping <destino>`

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


# 🔎 36. Validar una zona

Primero:

``` bash
sudo named-checkconf
```

Después:

``` bash
sudo named-checkzone asir.test /etc/bind/db.asir.test
```

`named-checkconf` comprueba la sintaxis de la configuración de `named`,
pero no sustituye a la comprobación de las zonas. `named-checkzone`
comprueba la sintaxis e integridad de un fichero de zona antes de
cargarlo. 

Finalmente:

``` bash
sudo systemctl restart bind9
```

Y consulta:

``` bash
dig @192.168.10.10 www.asir.test
```

------------------------------------------------------------------------

# 🧪 37. PRÁCTICA 5 --- Zona inversa
> 🧭 **PREPARACIÓN DE LA PRÁCTICA**
>
> **1 · Sitúate.** Lee primero el objetivo y localiza en la unidad el concepto que estamos llevando a la práctica. No empieces copiando comandos: primero debes poder explicar qué componente estamos construyendo y para qué sirve.
>
> **2 · Prepara el entorno.** Comprueba si esta práctica utiliza **Entorno I · Packet Tracer**, **Entorno II · WSL2**, **Entorno III · VirtualBox + Ubuntu 26.04 Server** o **Anexo VI · Entorno IV · Docker Compose**. Verifica conectividad, nombres, interfaces y estado de los servicios antes de modificar nada.
>
> **3 · Predice.** Antes de ejecutar un comando importante, escribe qué esperas que ocurra. Por ejemplo: «después de `ss -lnt`, espero encontrar el servicio escuchando en TCP/80». Esta pequeña predicción convierte la práctica en una investigación y no en una receta.
>
> **4 · Construye paso a paso.** Cada número debe dejar el sistema en un estado ligeramente más completo que el anterior. Después de cada bloque, realiza una comprobación corta. Si el paso 4 depende del 3, no avances hasta que el 3 funcione.
>
> **5 · Diagnostica si falla.** No empieces reiniciando. Sigue esta secuencia: **estado → configuración → logs → puertos → red → prueba desde el cliente**. Conserva las órdenes utilizadas y la evidencia del fallo.
>
> **6 · Demuestra.** La práctica termina cuando puedes demostrar el resultado con una evidencia: captura, salida de comando, conexión desde cliente, fichero de configuración o tráfico observado.
>
> **7 · Explica.** Cierra con una breve explicación técnica: qué has configurado, qué protocolo interviene, qué puerto utiliza, cómo se verifica y qué error sería el primero que investigarías si dejara de funcionar.




Para:

```text
192.168.10.0/24
```

crea:

```text
10.168.192.in-addr.arpa
```

En:

```text
/etc/bind/named.conf.local
```

```text
zone "10.168.192.in-addr.arpa" {
    type primary;
    file "/etc/bind/db.192.168.10";
};
```

Zona:

```text
$TTL 3600
@ IN SOA dns01.asir.test. admin.asir.test. (
    2026091701
    3600
    600
    604800
    300
)

  IN NS dns01.asir.test.

10 IN PTR dns01.asir.test.
20 IN PTR www.asir.test.
30 IN PTR mail.asir.test.
```

Validar:

``` bash
sudo named-checkzone 10.168.192.in-addr.arpa /etc/bind/db.192.168.10
```

Consultar:

``` bash
dig @192.168.10.10 -x 192.168.10.20
```

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
- `ss -lntup`
- `journalctl -b --no-pager`
- `ping <destino>`

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


# 🧪 38. PRÁCTICA 6 --- Registros DNS
> 🧭 **PREPARACIÓN DE LA PRÁCTICA**
>
> **1 · Sitúate.** Lee primero el objetivo y localiza en la unidad el concepto que estamos llevando a la práctica. No empieces copiando comandos: primero debes poder explicar qué componente estamos construyendo y para qué sirve.
>
> **2 · Prepara el entorno.** Comprueba si esta práctica utiliza **Entorno I · Packet Tracer**, **Entorno II · WSL2**, **Entorno III · VirtualBox + Ubuntu 26.04 Server** o **Anexo VI · Entorno IV · Docker Compose**. Verifica conectividad, nombres, interfaces y estado de los servicios antes de modificar nada.
>
> **3 · Predice.** Antes de ejecutar un comando importante, escribe qué esperas que ocurra. Por ejemplo: «después de `ss -lnt`, espero encontrar el servicio escuchando en TCP/80». Esta pequeña predicción convierte la práctica en una investigación y no en una receta.
>
> **4 · Construye paso a paso.** Cada número debe dejar el sistema en un estado ligeramente más completo que el anterior. Después de cada bloque, realiza una comprobación corta. Si el paso 4 depende del 3, no avances hasta que el 3 funcione.
>
> **5 · Diagnostica si falla.** No empieces reiniciando. Sigue esta secuencia: **estado → configuración → logs → puertos → red → prueba desde el cliente**. Conserva las órdenes utilizadas y la evidencia del fallo.
>
> **6 · Demuestra.** La práctica termina cuando puedes demostrar el resultado con una evidencia: captura, salida de comando, conexión desde cliente, fichero de configuración o tráfico observado.
>
> **7 · Explica.** Cierra con una breve explicación técnica: qué has configurado, qué protocolo interviene, qué puerto utiliza, cómo se verifica y qué error sería el primero que investigarías si dejara de funcionar.




Amplía la zona `asir.test` con:

### A

```text
web IN A 192.168.10.20
```

### AAAA

```text
web IN AAAA 2001:db8:10::20
```

### CNAME

```text
portal IN CNAME web.asir.test.
```

### MX

```text
@ IN MX 10 mail.asir.test.
```

### TXT

```text
@ IN TXT "Laboratorio SRI"
```

### SRV

Como actividad de investigación:

```text
_servicio._tcp.asir.test.
```

Consulta:

``` bash
dig @192.168.10.10 asir.test ANY
```

> ⚠️ En entornos modernos, `ANY` no debe utilizarse como método general
> para obtener «todos» los registros. Es preferible consultar
> explícitamente el tipo que interesa.

------------------------------------------------------------------------


### 🧭 Guía de resolución y comprobación

Esta práctica se considera resuelta cuando puedes **explicar y demostrar** el resultado, no solo cuando el comando termina sin errores. Sigue siempre esta secuencia:

1. **Identifica el estado inicial.** Anota interfaces, direcciones, rutas y servicios que ya estaban activos.
2. **Aplica el cambio mínimo.** No modifiques varias cosas a la vez: si algo falla, necesitas saber qué cambio lo provocó.
3. **Valida inmediatamente.** Comprueba la sintaxis o el estado del servicio antes de probar desde el cliente.
4. **Prueba desde el punto de vista del usuario.** Una configuración correcta debe producir el comportamiento esperado desde el cliente, no solo desde el servidor.
5. **Observa evidencias.** Conserva la salida de comandos, logs, capturas de tráfico y capturas de pantalla que demuestren el resultado.

**Comandos de referencia para esta práctica:**

- `resolvectl status`
- `dig @<DNS> <nombre>`
- `sudo named-checkconf`
- `sudo named-checkzone <zona> <fichero>`
- `sudo journalctl -u bind9 --no-pager`

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


# 🧪 39. PRÁCTICA 7 --- Servidor secundario y transferencia de zona
> 🧭 **PREPARACIÓN DE LA PRÁCTICA**
>
> **1 · Sitúate.** Lee primero el objetivo y localiza en la unidad el concepto que estamos llevando a la práctica. No empieces copiando comandos: primero debes poder explicar qué componente estamos construyendo y para qué sirve.
>
> **2 · Prepara el entorno.** Comprueba si esta práctica utiliza **Entorno I · Packet Tracer**, **Entorno II · WSL2**, **Entorno III · VirtualBox + Ubuntu 26.04 Server** o **Anexo VI · Entorno IV · Docker Compose**. Verifica conectividad, nombres, interfaces y estado de los servicios antes de modificar nada.
>
> **3 · Predice.** Antes de ejecutar un comando importante, escribe qué esperas que ocurra. Por ejemplo: «después de `ss -lnt`, espero encontrar el servicio escuchando en TCP/80». Esta pequeña predicción convierte la práctica en una investigación y no en una receta.
>
> **4 · Construye paso a paso.** Cada número debe dejar el sistema en un estado ligeramente más completo que el anterior. Después de cada bloque, realiza una comprobación corta. Si el paso 4 depende del 3, no avances hasta que el 3 funcione.
>
> **5 · Diagnostica si falla.** No empieces reiniciando. Sigue esta secuencia: **estado → configuración → logs → puertos → red → prueba desde el cliente**. Conserva las órdenes utilizadas y la evidencia del fallo.
>
> **6 · Demuestra.** La práctica termina cuando puedes demostrar el resultado con una evidencia: captura, salida de comando, conexión desde cliente, fichero de configuración o tráfico observado.
>
> **7 · Explica.** Cierra con una breve explicación técnica: qué has configurado, qué protocolo interviene, qué puerto utiliza, cómo se verifica y qué error sería el primero que investigarías si dejara de funcionar.




## Topología

```text
             PRIMARY
          192.168.10.10
                │
                │ AXFR/IXFR
                ▼
            SECONDARY
          192.168.10.11
```

El servidor secundario obtiene los datos de la zona desde el primary.

Ubuntu documenta esta función de BIND9: el primary obtiene los datos de
zona desde un fichero local y el secondary obtiene los datos desde otro
servidor autoritativo. 

### Objetivos

-   Configurar primary.
-   Configurar secondary.
-   Permitir transferencia únicamente al secondary.
-   Modificar el serial.
-   Comprobar la actualización.

### Verificación

``` bash
dig @192.168.10.11 www.asir.test
```

Y:

``` bash
dig @192.168.10.11 asir.test SOA
```

Compara el `serial` de ambos servidores.

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
- `ss -lntup`
- `journalctl -b --no-pager`
- `ping <destino>`

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


# 🔐 40. Transferencias de zona y seguridad

Una transferencia de zona puede proporcionar mucha información sobre la
infraestructura DNS.

Por ello no debe permitirse indiscriminadamente.

```text
❌ CUALQUIER HOST ──► AXFR ──► DNS

✅ PRIMARY ──► SECONDARY autorizado
```

La política debe restringir las transferencias a servidores autorizados.

Para autenticación puede utilizarse **TSIG**.

------------------------------------------------------------------------

> 🧭 **ANTES DE EMPEZAR · Autenticación de transferencias DNS**
>
> Cuando dos servidores DNS intercambian información administrativa, no basta con que exista conectividad: necesitamos poder autenticar al interlocutor y proteger la integridad del intercambio. **TSIG** proporciona autenticación basada en una clave compartida para operaciones como transferencias de zona.

# 🔑 41. TSIG

TSIG permite autenticar comunicaciones entre servidores DNS mediante una
clave compartida.

```text
PRIMARY                         SECONDARY
   │                                │
   │──── consulta firmada ─────────►│
   │                                │
   │◄── respuesta autenticada ──────│
```

En BIND9, TSIG utiliza claves compartidas para autenticar determinadas
comunicaciones y operaciones. 

### Idea fundamental

```text
MISMA CLAVE
    │
    ├── Primary
    │
    └── Secondary
```

No se debe incluir una clave TSIG real en un repositorio Git público.

------------------------------------------------------------------------

# 🧪 42. PRÁCTICA 8 --- Transferencia autenticada
> 🧭 **PREPARACIÓN DE LA PRÁCTICA**
>
> **1 · Sitúate.** Lee primero el objetivo y localiza en la unidad el concepto que estamos llevando a la práctica. No empieces copiando comandos: primero debes poder explicar qué componente estamos construyendo y para qué sirve.
>
> **2 · Prepara el entorno.** Comprueba si esta práctica utiliza **Entorno I · Packet Tracer**, **Entorno II · WSL2**, **Entorno III · VirtualBox + Ubuntu 26.04 Server** o **Anexo VI · Entorno IV · Docker Compose**. Verifica conectividad, nombres, interfaces y estado de los servicios antes de modificar nada.
>
> **3 · Predice.** Antes de ejecutar un comando importante, escribe qué esperas que ocurra. Por ejemplo: «después de `ss -lnt`, espero encontrar el servicio escuchando en TCP/80». Esta pequeña predicción convierte la práctica en una investigación y no en una receta.
>
> **4 · Construye paso a paso.** Cada número debe dejar el sistema en un estado ligeramente más completo que el anterior. Después de cada bloque, realiza una comprobación corta. Si el paso 4 depende del 3, no avances hasta que el 3 funcione.
>
> **5 · Diagnostica si falla.** No empieces reiniciando. Sigue esta secuencia: **estado → configuración → logs → puertos → red → prueba desde el cliente**. Conserva las órdenes utilizadas y la evidencia del fallo.
>
> **6 · Demuestra.** La práctica termina cuando puedes demostrar el resultado con una evidencia: captura, salida de comando, conexión desde cliente, fichero de configuración o tráfico observado.
>
> **7 · Explica.** Cierra con una breve explicación técnica: qué has configurado, qué protocolo interviene, qué puerto utiliza, cómo se verifica y qué error sería el primero que investigarías si dejara de funcionar.




Configura:

```text
DNS01 → primary
DNS02 → secondary
```

Objetivo:

1.  Crear clave TSIG.
2.  Asociarla a la transferencia.
3.  Permitir AXFR/IXFR solo con autenticación.
4.  Intentar una transferencia desde un host no autorizado.
5.  Comprobar que se rechaza.
6.  Comprobar que DNS02 continúa funcionando.

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
- `ss -lntup`
- `journalctl -b --no-pager`
- `ping <destino>`

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


# 🔄 43. DNS dinámico --- DDNS

DNS dinámico permite modificar registros automáticamente.

Caso típico:

```text
DHCP
 │
 │ asigna IP
 ▼
CLIENTE
 │
 │ actualización DNS
 ▼
DNS
```

Esto resulta especialmente útil cuando las direcciones cambian con
frecuencia.

Puede utilizarse para integrar DHCP y DNS en determinados entornos.

------------------------------------------------------------------------

# 🧪 44. PRÁCTICA 9 --- DHCP + DNS dinámico
> 🧭 **PREPARACIÓN DE LA PRÁCTICA**
>
> **1 · Sitúate.** Lee primero el objetivo y localiza en la unidad el concepto que estamos llevando a la práctica. No empieces copiando comandos: primero debes poder explicar qué componente estamos construyendo y para qué sirve.
>
> **2 · Prepara el entorno.** Comprueba si esta práctica utiliza **Entorno I · Packet Tracer**, **Entorno II · WSL2**, **Entorno III · VirtualBox + Ubuntu 26.04 Server** o **Anexo VI · Entorno IV · Docker Compose**. Verifica conectividad, nombres, interfaces y estado de los servicios antes de modificar nada.
>
> **3 · Predice.** Antes de ejecutar un comando importante, escribe qué esperas que ocurra. Por ejemplo: «después de `ss -lnt`, espero encontrar el servicio escuchando en TCP/80». Esta pequeña predicción convierte la práctica en una investigación y no en una receta.
>
> **4 · Construye paso a paso.** Cada número debe dejar el sistema en un estado ligeramente más completo que el anterior. Después de cada bloque, realiza una comprobación corta. Si el paso 4 depende del 3, no avances hasta que el 3 funcione.
>
> **5 · Diagnostica si falla.** No empieces reiniciando. Sigue esta secuencia: **estado → configuración → logs → puertos → red → prueba desde el cliente**. Conserva las órdenes utilizadas y la evidencia del fallo.
>
> **6 · Demuestra.** La práctica termina cuando puedes demostrar el resultado con una evidencia: captura, salida de comando, conexión desde cliente, fichero de configuración o tráfico observado.
>
> **7 · Explica.** Cierra con una breve explicación técnica: qué has configurado, qué protocolo interviene, qué puerto utiliza, cómo se verifica y qué error sería el primero que investigarías si dejara de funcionar.




Utilizando la infraestructura de la UT2:

```text
          DHCP / KEA
              │
              │ IP
              ▼
           CLIENTE
              │
              │ actualización
              ▼
          BIND9 DNS
```

Investiga y documenta:

-   qué componente genera la actualización,
-   cómo se autentica,
-   qué registros se actualizan,
-   cómo se evita que cualquier cliente pueda modificar la zona.

------------------------------------------------------------------------

> 🧭 **ANTES DE EMPEZAR · DNSSEC**
>
> DNSSEC añade autenticación criptográfica de los datos DNS mediante firmas digitales y una cadena de confianza. **No cifra las consultas DNS**: su finalidad principal es permitir validar la autenticidad e integridad de los datos.


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


# 🛡️ 45. DNSSEC

DNSSEC proporciona mecanismos para validar la autenticidad e integridad
de los datos DNS.

Añade registros como:

```text
DNSKEY
RRSIG
NSEC / NSEC3
DS
```

BIND9 proporciona herramientas y políticas específicas para firmar zonas
y mantener sus claves. 

```text
Zona DNS
   │
   ├── A
   ├── AAAA
   ├── NS
   └── ...
        │
        ▼
     DNSSEC
        │
        ├── DNSKEY
        ├── RRSIG
        └── NSEC/NSEC3
```

> ⚠️ **DNSSEC no cifra las consultas DNS.**
>
> Su objetivo es proporcionar autenticidad e integridad de los datos
> DNS, no confidencialidad del tráfico. 

------------------------------------------------------------------------

# 🧨 46. Amenazas DNS

Entre los problemas de seguridad tratados en el material previo se
encuentran:

-   DNS spoofing.
-   Envenenamiento de caché.
-   Transferencias de zona no autorizadas.
-   Modificaciones no autorizadas.
-   Ataques contra servidores DNS.
-   Actualizaciones dinámicas no protegidas.

```text
                 🚨 ATAQUE
                    │
       ┌────────────┼────────────┐
       │            │            │
     CACHE         ZONA        SERVIDOR
    POISONING    ALTERADA       DoS
```

------------------------------------------------------------------------

# 🔐 47. Buenas prácticas de seguridad

### En un servidor autoritativo

-   Mantener BIND actualizado.
-   Limitar las transferencias de zona.
-   Restringir recursividad cuando no sea necesaria.
-   Separar servidores autoritativos y resolvers cuando el diseño lo
    requiera.
-   Utilizar TSIG para operaciones que lo necesiten.
-   Utilizar DNSSEC cuando corresponda.
-   Revisar logs.
-   Evitar exponer interfaces de administración.
-   Aplicar firewall.

### Principio

```text
           DNS
            │
      ┌─────┴─────┐
      │           │
 AUTORITATIVO   RECURSOR
      │           │
      ▼           ▼
   zonas        caché
```

------------------------------------------------------------------------

# 🧪 48. PRÁCTICA 10 --- Diagnóstico DNS con Wireshark
> 🧭 **PREPARACIÓN DE LA PRÁCTICA**
>
> **1 · Sitúate.** Lee primero el objetivo y localiza en la unidad el concepto que estamos llevando a la práctica. No empieces copiando comandos: primero debes poder explicar qué componente estamos construyendo y para qué sirve.
>
> **2 · Prepara el entorno.** Comprueba si esta práctica utiliza **Entorno I · Packet Tracer**, **Entorno II · WSL2**, **Entorno III · VirtualBox + Ubuntu 26.04 Server** o **Anexo VI · Entorno IV · Docker Compose**. Verifica conectividad, nombres, interfaces y estado de los servicios antes de modificar nada.
>
> **3 · Predice.** Antes de ejecutar un comando importante, escribe qué esperas que ocurra. Por ejemplo: «después de `ss -lnt`, espero encontrar el servicio escuchando en TCP/80». Esta pequeña predicción convierte la práctica en una investigación y no en una receta.
>
> **4 · Construye paso a paso.** Cada número debe dejar el sistema en un estado ligeramente más completo que el anterior. Después de cada bloque, realiza una comprobación corta. Si el paso 4 depende del 3, no avances hasta que el 3 funcione.
>
> **5 · Diagnostica si falla.** No empieces reiniciando. Sigue esta secuencia: **estado → configuración → logs → puertos → red → prueba desde el cliente**. Conserva las órdenes utilizadas y la evidencia del fallo.
>
> **6 · Demuestra.** La práctica termina cuando puedes demostrar el resultado con una evidencia: captura, salida de comando, conexión desde cliente, fichero de configuración o tráfico observado.
>
> **7 · Explica.** Cierra con una breve explicación técnica: qué has configurado, qué protocolo interviene, qué puerto utiliza, cómo se verifica y qué error sería el primero que investigarías si dejara de funcionar.




Captura tráfico mientras ejecutas:

``` bash
dig www.juandecolonia.jc
```

Filtro:

```text
dns
```

Analiza:

-   dirección IP origen,
-   destino,
-   puerto UDP 53,
-   consulta,
-   respuesta,
-   tipo de registro,
-   flags,
-   `Transaction ID`,
-   `Answer`,
-   `Authority`,
-   `Additional`.

Después repite:

``` bash
dig +tcp www.juandecolonia.jc
```

Compara UDP y TCP.

------------------------------------------------------------------------


### 🧭 Guía de resolución y comprobación

Esta práctica se considera resuelta cuando puedes **explicar y demostrar** el resultado, no solo cuando el comando termina sin errores. Sigue siempre esta secuencia:

1. **Identifica el estado inicial.** Anota interfaces, direcciones, rutas y servicios que ya estaban activos.
2. **Aplica el cambio mínimo.** No modifiques varias cosas a la vez: si algo falla, necesitas saber qué cambio lo provocó.
3. **Valida inmediatamente.** Comprueba la sintaxis o el estado del servicio antes de probar desde el cliente.
4. **Prueba desde el punto de vista del usuario.** Una configuración correcta debe producir el comportamiento esperado desde el cliente, no solo desde el servidor.
5. **Observa evidencias.** Conserva la salida de comandos, logs, capturas de tráfico y capturas de pantalla que demuestren el resultado.

**Comandos de referencia para esta práctica:**

- `resolvectl status`
- `dig @<DNS> <nombre>`
- `sudo named-checkconf`
- `sudo named-checkzone <zona> <fichero>`
- `sudo journalctl -u bind9 --no-pager`

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


# 🧪 49. PRÁCTICA 11 --- Diagnóstico con `dig`
> 🧭 **PREPARACIÓN DE LA PRÁCTICA**
>
> **1 · Sitúate.** Lee primero el objetivo y localiza en la unidad el concepto que estamos llevando a la práctica. No empieces copiando comandos: primero debes poder explicar qué componente estamos construyendo y para qué sirve.
>
> **2 · Prepara el entorno.** Comprueba si esta práctica utiliza **Entorno I · Packet Tracer**, **Entorno II · WSL2**, **Entorno III · VirtualBox + Ubuntu 26.04 Server** o **Anexo VI · Entorno IV · Docker Compose**. Verifica conectividad, nombres, interfaces y estado de los servicios antes de modificar nada.
>
> **3 · Predice.** Antes de ejecutar un comando importante, escribe qué esperas que ocurra. Por ejemplo: «después de `ss -lnt`, espero encontrar el servicio escuchando en TCP/80». Esta pequeña predicción convierte la práctica en una investigación y no en una receta.
>
> **4 · Construye paso a paso.** Cada número debe dejar el sistema en un estado ligeramente más completo que el anterior. Después de cada bloque, realiza una comprobación corta. Si el paso 4 depende del 3, no avances hasta que el 3 funcione.
>
> **5 · Diagnostica si falla.** No empieces reiniciando. Sigue esta secuencia: **estado → configuración → logs → puertos → red → prueba desde el cliente**. Conserva las órdenes utilizadas y la evidencia del fallo.
>
> **6 · Demuestra.** La práctica termina cuando puedes demostrar el resultado con una evidencia: captura, salida de comando, conexión desde cliente, fichero de configuración o tráfico observado.
>
> **7 · Explica.** Cierra con una breve explicación técnica: qué has configurado, qué protocolo interviene, qué puerto utiliza, cómo se verifica y qué error sería el primero que investigarías si dejara de funcionar.




Realiza:

``` bash
dig @192.168.10.10 www.asir.test A
dig @192.168.10.10 www.asir.test AAAA
dig @192.168.10.10 asir.test NS
dig @192.168.10.10 asir.test SOA
dig @192.168.10.10 asir.test MX
dig @192.168.10.10 -x 192.168.10.20
```

Después:

``` bash
dig +trace www.juandecolonia.jc
```

### Informe

Para cada consulta indica:

-   servidor consultado,
-   tipo,
-   respuesta,
-   autoridad,
-   TTL,
-   tiempo de respuesta.

------------------------------------------------------------------------


### 🧭 Guía de resolución y comprobación

Esta práctica se considera resuelta cuando puedes **explicar y demostrar** el resultado, no solo cuando el comando termina sin errores. Sigue siempre esta secuencia:

1. **Identifica el estado inicial.** Anota interfaces, direcciones, rutas y servicios que ya estaban activos.
2. **Aplica el cambio mínimo.** No modifiques varias cosas a la vez: si algo falla, necesitas saber qué cambio lo provocó.
3. **Valida inmediatamente.** Comprueba la sintaxis o el estado del servicio antes de probar desde el cliente.
4. **Prueba desde el punto de vista del usuario.** Una configuración correcta debe producir el comportamiento esperado desde el cliente, no solo desde el servidor.
5. **Observa evidencias.** Conserva la salida de comandos, logs, capturas de tráfico y capturas de pantalla que demuestren el resultado.

**Comandos de referencia para esta práctica:**

- `resolvectl status`
- `dig @<DNS> <nombre>`
- `sudo named-checkconf`
- `sudo named-checkzone <zona> <fichero>`
- `sudo journalctl -u bind9 --no-pager`

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


# 🩺 50. Diagnóstico sistemático

Cuando DNS falla, no empieces cambiando configuraciones al azar.

```text
                 ❌ NO RESUELVE
                       │
                       ▼
              ¿Hay conectividad IP?
                  /          \
                NO            SÍ
                │              │
             resolver          ▼
                          ¿Puerto 53?
                           /       \
                         NO         SÍ
                         │           │
                      firewall       ▼
                               ¿Servidor activo?
                                  /       \
                                NO         SÍ
                                │           │
                              systemd       ▼
                                   ¿Zona correcta?
                                      /      \
                                    NO        SÍ
                                    │          │
                                 zona       registros
                                               │
                                               ▼
                                          ¿caché/TTL?
```

------------------------------------------------------------------------

# 🚨 51. Errores frecuentes de BIND9

### ❌ Error de sintaxis

Comprobar:

``` bash
sudo named-checkconf
```

### ❌ Error en una zona

``` bash
sudo named-checkzone asir.test /etc/bind/db.asir.test
```

### ❌ El servicio no arranca

``` bash
systemctl status bind9
journalctl -u bind9
```

### ❌ El servidor responde REFUSED

Comprobar:

-   `allow-query`,
-   `allow-recursion`,
-   configuración de zona,
-   ACL,
-   interfaz de escucha.

### ❌ NXDOMAIN

Puede indicar:

-   nombre inexistente,
-   zona incorrecta,
-   registro ausente,
-   consulta al servidor equivocado.

### ❌ SERVFAIL

Puede indicar un problema más profundo:

-   servidor autoritativo inaccesible,
-   DNSSEC,
-   configuración,
-   dependencia de otro servidor,
-   error en la resolución.

------------------------------------------------------------------------

# 🧪 52. PRÁCTICA 12 --- Reto integral DNS
> 🧭 **PREPARACIÓN DE LA PRÁCTICA**
>
> **1 · Sitúate.** Lee primero el objetivo y localiza en la unidad el concepto que estamos llevando a la práctica. No empieces copiando comandos: primero debes poder explicar qué componente estamos construyendo y para qué sirve.
>
> **2 · Prepara el entorno.** Comprueba si esta práctica utiliza **Entorno I · Packet Tracer**, **Entorno II · WSL2**, **Entorno III · VirtualBox + Ubuntu 26.04 Server** o **Anexo VI · Entorno IV · Docker Compose**. Verifica conectividad, nombres, interfaces y estado de los servicios antes de modificar nada.
>
> **3 · Predice.** Antes de ejecutar un comando importante, escribe qué esperas que ocurra. Por ejemplo: «después de `ss -lnt`, espero encontrar el servicio escuchando en TCP/80». Esta pequeña predicción convierte la práctica en una investigación y no en una receta.
>
> **4 · Construye paso a paso.** Cada número debe dejar el sistema en un estado ligeramente más completo que el anterior. Después de cada bloque, realiza una comprobación corta. Si el paso 4 depende del 3, no avances hasta que el 3 funcione.
>
> **5 · Diagnostica si falla.** No empieces reiniciando. Sigue esta secuencia: **estado → configuración → logs → puertos → red → prueba desde el cliente**. Conserva las órdenes utilizadas y la evidencia del fallo.
>
> **6 · Demuestra.** La práctica termina cuando puedes demostrar el resultado con una evidencia: captura, salida de comando, conexión desde cliente, fichero de configuración o tráfico observado.
>
> **7 · Explica.** Cierra con una breve explicación técnica: qué has configurado, qué protocolo interviene, qué puerto utiliza, cómo se verifica y qué error sería el primero que investigarías si dejara de funcionar.




Construye:

```text
                         🌐 INTERNET
                              │
                         ┌────┴────┐
                         │ RESOLVER│
                         └────┬────┘
                              │
                 ┌────────────┴────────────┐
                 │                         │
              DNS01                      DNS02
             PRIMARY                   SECONDARY
          192.168.10.10              192.168.10.11
                 │                         │
                 └──────────┬──────────────┘
                            │
                       LAN SRI-DNS
```

## Debe incluir

### Zona directa

```text
asir.test
```

### Zona inversa

```text
10.168.192.in-addr.arpa
```

### Registros

-   SOA.
-   NS.
-   A.  
-   AAAA.
-   CNAME.
-   MX. 
-   PTR.

### Servicios

-   Primary.
-   Secondary.
-   Caché/recursividad según diseño.
-   Transferencia de zona.
-   Consultas con `dig`.

### Seguridad

-   Restricción de AXFR.
-   TSIG.
-   Restricción de recursividad.
-   Firewall.

### Evidencias

1.  Configuración.
2.  Validación.
3.  Estado de servicios.
4.  Consulta directa.
5.  Consulta inversa.
6.  Transferencia.
7.  Captura Wireshark.
8.  Diagnóstico de un fallo introducido deliberadamente.

------------------------------------------------------------------------


### 🧭 Guía de resolución y comprobación

Esta práctica se considera resuelta cuando puedes **explicar y demostrar** el resultado, no solo cuando el comando termina sin errores. Sigue siempre esta secuencia:

1. **Identifica el estado inicial.** Anota interfaces, direcciones, rutas y servicios que ya estaban activos.
2. **Aplica el cambio mínimo.** No modifiques varias cosas a la vez: si algo falla, necesitas saber qué cambio lo provocó.
3. **Valida inmediatamente.** Comprueba la sintaxis o el estado del servicio antes de probar desde el cliente.
4. **Prueba desde el punto de vista del usuario.** Una configuración correcta debe producir el comportamiento esperado desde el cliente, no solo desde el servidor.
5. **Observa evidencias.** Conserva la salida de comandos, logs, capturas de tráfico y capturas de pantalla que demuestren el resultado.

**Comandos de referencia para esta práctica:**

- `resolvectl status`
- `dig @<DNS> <nombre>`
- `sudo named-checkconf`
- `sudo named-checkzone <zona> <fichero>`
- `sudo journalctl -u bind9 --no-pager`

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


# 🧠 53. Resumen

```text
                           DNS
                            │
                ┌───────────┼───────────┐
                │           │           │
             NOMBRES       ZONAS     REGISTROS
                │           │           │
                │       DIRECTA/INV.    │
                │                       │
                └──────────┬────────────┘
                           │
                      RESOLUCIÓN
                           │
                  ┌────────┴────────┐
                  │                 │
              RECURSIVA          ITERATIVA
                  │                 │
                  └────────┬────────┘
                           │
                     SERVIDORES
                           │
            ┌──────────────┼──────────────┐
            │              │              │
         PRIMARY        SECONDARY       CACHÉ
            │              │              │
            └──────────────┼──────────────┘
                           │
                       SEGURIDAD
                           │
                 DNSSEC · TSIG · ACL
```

Ideas fundamentales:

1.  DNS es jerárquico y distribuido.
2.  La raíz delega hacia los TLD.
3.  Los dominios pueden dividirse administrativamente en zonas.
4.  Un servidor puede tener diferentes funciones según la zona.
5.  La resolución puede ser recursiva o iterativa.
6.  Las respuestas se almacenan en caché durante un TTL.
7.  Los registros RR contienen la información DNS.
8.  `A` y `AAAA` proporcionan direcciones.
9.  `NS` identifica servidores autoritativos.
10. `SOA` contiene información fundamental de la zona.
11. `MX` identifica servidores de correo.
12. `CNAME` crea alias.
13. `PTR` participa en resolución inversa.
14. Las transferencias permiten mantener secundarios.
15. TSIG puede autenticar operaciones entre servidores.
16. DNSSEC proporciona autenticidad e integridad de los datos DNS.
17. BIND9 sigue siendo una plataforma adecuada para el laboratorio.
18. `dig`, `host`, `named-checkconf` y `named-checkzone` son
    herramientas fundamentales.

------------------------------------------------------------------------

# ❓ 54. Autoevaluación

1.  Explica brevemente cuál es la función de los componentes del
    servicio DNS.
2.  Dibuja una parte del espacio de nombres de dominio que represente
    parte de los dominios de resolución directa y parte de los dominios
    de resolución inversa.
3.  Enumera tres dominios TLD genéricos y tres TLD geográficos.
4.  Explica qué diferencia existe entre dominio, subdominio y zona.
5.  Explica qué es un FQDN y diferencia nombre relativo y absoluto.
6.  Explica en qué consiste la delegación de un dominio y qué utilidad
    tiene.
7.  Explica la secuencia de consultas DNS que se produce cuando un
    resolver realiza una consulta recursiva para un dominio.
8.  Explica qué diferencia existe entre una consulta recursiva y una
    iterativa.
9.  Explica qué es el caché DNS y qué función desempeña el TTL.
10. Explica qué es la resolución inversa y qué espacio de nombres
    utiliza.
11. Explica qué es una transferencia de zona y diferencia AXFR e IXFR.
12. Explica la utilidad del registro SOA.
13. Explica qué es el envenenamiento de caché DNS y qué mecanismos
    pueden utilizarse para reducir el riesgo.
14. Explica qué es DNSSEC y qué aporta frente al DNS tradicional.

------------------------------------------------------------------------

# ✅ Solucionario de la autoevaluación

> 📌 Primero intenta resolver las cuestiones sin consultar esta sección.

### 1. Componentes del servicio DNS

El sistema DNS está formado, entre otros, por:

-   **Clientes/resolvers**, que generan consultas.
-   **Servidores DNS**, que responden a consultas.
-   **Zonas**, que contienen información autoritativa.
-   **Registros de recursos**, que describen nombres y datos.
-   **Jerarquía DNS**, que permite distribuir la autoridad.

### 2. Espacio de nombres

Ejemplo:

```text
                    .
                    │
              ┌─────┴─────┐
             com           es
              │            │
           example        asir
              │            │
             www          www
```

Para resolución inversa:

```text
                in-addr.arpa
                     │
                  192
                     │
                   168
                     │
                    10
                     │
                 host PTR
```

### 3. TLD

Genéricos:

```text
.com
.org
.net
```

Geográficos:

```text
.es
.pt
.fr
```

### 4. Dominio, subdominio y zona

Un **dominio** es un nombre dentro del árbol DNS.

Un **subdominio** está situado bajo otro dominio.

Una **zona** es una parte del espacio DNS cuya información es
administrada autoritativamente.

Un dominio puede incluir delegaciones y, por tanto, varias zonas.

### 5. FQDN, nombre relativo y absoluto

Un FQDN identifica completamente un nombre dentro de la jerarquía.

Ejemplo:

```text
www.asir.example.
```

Un nombre relativo necesita un contexto u origen para interpretarse.

Un nombre absoluto contiene toda la ruta jerárquica hasta la raíz.

### 6. Delegación

La delegación consiste en que una zona padre indica qué servidores son
autoritativos para una zona hija.

Ejemplo:

```text
juandecolonia.jc
     │
     └──► asir.juandecolonia.jc
              │
              └── DNS propio
```

Permite distribuir la administración del espacio DNS.

### 7. Consulta recursiva

El cliente pregunta a un resolver:

```text
www.juandecolonia.jc ?
```

El resolver puede consultar:

```text
ROOT
  ↓
.COM
  ↓
juandecolonia.jc
  ↓
respuesta
```

y devolver al cliente la respuesta final.

### 8. Recursiva vs. iterativa

**Recursiva:** el servidor consultado asume la responsabilidad de
obtener una respuesta completa.

**Iterativa:** el servidor devuelve la información que conoce o una
referencia, y el proceso continúa mediante nuevas consultas.

### 9. Caché y TTL

La caché almacena temporalmente respuestas DNS para evitar consultas
repetidas.

El TTL indica cuánto tiempo puede mantenerse una respuesta en caché.

### 10. Resolución inversa

Es la obtención de un nombre a partir de una dirección IP.

En IP utiliza:

```text
in-addr.arpa
```

Ejemplo:

```text
192.168.10.20
      ↓
20.10.168.192.in-addr.arpa
      ↓
www.asir.test
```

### 11. AXFR e IXFR

**AXFR** realiza una transferencia completa de la zona.

**IXFR** permite transferir los cambios realizados desde una versión
anterior, reduciendo el volumen de datos cuando resulta aplicable.

### 12. SOA

El registro SOA contiene información fundamental de la zona:

-   servidor principal,
-   contacto administrativo,
-   serial,
-   refresh,
-   retry,
-   expire,
-   TTL negativo.

### 13. Envenenamiento de caché

Consiste en introducir información DNS falsa en una caché para que los
clientes reciban respuestas manipuladas.

Medidas relacionadas:

-   DNSSEC.
-   Actualizaciones y configuraciones seguras.
-   BIND actualizado.
-   Control de recursividad.
-   Políticas de seguridad.
-   Evitar servidores abiertos innecesariamente.

### 14. DNSSEC

DNSSEC añade mecanismos criptográficos para validar la autenticidad e
integridad de la información DNS.

Utiliza registros como:

```text
DNSKEY
RRSIG
DS
NSEC/NSEC3
```

No cifra las consultas DNS: su objetivo es validar los datos y proteger
la cadena de confianza. 

------------------------------------------------------------------------

# 📝 55. Test de repaso

## 1. ¿Qué componente suele realizar consultas recursivas para un cliente?
A. El cliente FTP
B. El resolvedor DNS
C. El servidor web
D. El servidor DHCP

## 2. ¿Qué registro contiene información de autoridad de una zona?
A. SOA
B. A
C. MX
D. PTR

## 3. ¿Qué registro asocia normalmente un nombre con una dirección IPv4?
A. AAAA
B. CNAME
C. A
D. NS

## 4. ¿Qué registro se utiliza para localizar servidores de correo?
A. TXT
B. MX
C. PTR
D. SOA

## 5. ¿Qué herramienta permite realizar consultas DNS detalladas desde Linux?
A. `dig`
B. `ss`
C. `scp`
D. `ip route`

## 6. ¿Qué comando valida la sintaxis global de BIND?
A. `named-checkzone`
B. `named-checkconf`
C. `bind-check`
D. `dns-test`

## 7. ¿Qué comando valida los registros de una zona concreta?
A. `named-checkzone`
B. `named-checkconf`
C. `dig +trace`
D. `resolvectl flush-caches`

## 8. ¿Qué registro se utiliza habitualmente para resolución inversa IPv4?
A. MX
B. PTR
C. CNAME
D. TXT

## 9. ¿Qué mecanismo protege la autenticidad de los datos DNS mediante una cadena de confianza?
A. FTP
B. DNSSEC
C. DHCP relay
D. PAT

## 10. ¿Qué herramienta permite seguir la delegación DNS desde la raíz?
A. `dig +trace`
B. `dig +short`
C. `host -v` únicamente
D. `ss -lnt`

### ✅ Respuestas

| Pregunta | Respuesta |
|---:|:---:|
| 1 | **B** |
| 2 | **A** |
| 3 | **C** |
| 4 | **B** |
| 5 | **A** |
| 6 | **B** |
| 7 | **A** |
| 8 | **B** |
| 9 | **B** |
| 10 | **A** |

# 🧪 56. Actividad final --- «¿Dónde está el problema?»
### 🧭 Guía de resolución y comprobación

**Puntos a conseguir:** dejar el sistema en el estado solicitado, poder explicar qué protocolo interviene, comprobarlo desde un cliente y aportar evidencias reproducibles.

1. **Preparar** el entorno y registrar el estado inicial.
2. **Construir** solo el siguiente elemento necesario.
3. **Validar** sintaxis y servicio.
4. **Probar** desde el cliente.
5. **Observar** puertos, logs y tráfico cuando proceda.
6. **Documentar** configuración, comandos y capturas.


#### Solución de referencia

La solución debe dejar un estado reproducible: topología o configuración documentada, comandos ejecutados, resultado esperado y resultado observado. Si el ejercicio pide una incidencia, documenta además **causa → evidencia → corrección → prueba de recuperación**.


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


El profesor proporciona:

```text
Cliente
192.168.10.50

DNS
192.168.10.10

Zona
asir.test
```

El cliente ejecuta:

``` bash
dig @192.168.10.10 www.asir.test
```

y obtiene:

```text
SERVFAIL
```

### El alumno deberá comprobar, en orden:

```text
1️⃣ conectividad IP
       ↓
2️⃣ puerto 53
       ↓
3️⃣ servicio bind9
       ↓
4️⃣ named-checkconf
       ↓
5️⃣ named-checkzone
       ↓
6️⃣ SOA
       ↓
7️⃣ NS
       ↓
8️⃣ A
       ↓
9️⃣ logs
       ↓
🔟 captura DNS
```

### Evidencia final

El alumno debe identificar:

-   causa del fallo,
-   comando utilizado para detectarlo,
-   configuración responsable,
-   corrección aplicada,
-   prueba que demuestra que el problema está resuelto.

------------------------------------------------------------------------


