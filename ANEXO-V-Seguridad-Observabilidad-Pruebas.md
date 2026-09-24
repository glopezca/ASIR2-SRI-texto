# 🛡️ ANEXO V · Seguridad, observabilidad, pruebas y troubleshooting

> 🧭 **ANTES DE EMPEZAR · VOCABULARIO TÉCNICO**
>
> Las siglas, abreviaturas y conceptos técnicos que van a aparecer en esta unidad se presentan aquí antes de su desarrollo. La explicación local de cada tema podrá ampliar estas definiciones cuando sea necesario.
>
> **RA** — Resultado de Aprendizaje: capacidad que el alumnado debe demostrar al finalizar un bloque curricular.
> **CFGS** — Ciclo Formativo de Grado Superior.
> **ASIR** — Administración de Sistemas Informáticos en Red.
> **ID** — Identificador utilizado para distinguir un objeto de otros.
> **IP** — Protocolo de Internet, responsable del direccionamiento y encaminamiento de paquetes.
> **HTTP** — Protocolo de transferencia de hipertexto utilizado principalmente por la Web.
> **Docker** — Plataforma de contenerización para construir, distribuir y ejecutar aplicaciones aisladas en contenedores.
> **Kubernetes** — Plataforma de orquestación de contenedores que automatiza despliegue, escalado y operación.
> **PID** — Identificador numérico de un proceso en un sistema operativo.
> **TLS** — Protocolo criptográfico que proporciona confidencialidad, integridad y autenticación mediante certificados.
> **Git** — Sistema distribuido de control de versiones.
> **DNS** — Sistema de nombres de dominio: servicio distribuido que relaciona nombres con direcciones IP y otros datos.
> **DHCP** — Protocolo de configuración dinámica de host: entrega automáticamente parámetros de red a los clientes.
> **FTP** — Protocolo de transferencia de archivos que separa un canal de control de los canales de datos.
> **XMPP** — Extensible Messaging and Presence Protocol, protocolo abierto para mensajería y presencia.
>
> **Criterio didáctico:** no se presupone que conocer una sigla equivalga a comprender el concepto. Primero se identifica qué significa y qué función desempeña; después se emplea en comandos, configuraciones y prácticas.

> 🧩 **ANTES DE EMPEZAR · CONCEPTOS BASE**
>
> **Protocolo** — conjunto de reglas que define cómo se comunican dos o más sistemas.
> **Cliente** — programa o equipo que inicia una petición de un servicio.
> **Servidor** — programa o equipo que ofrece un servicio y atiende peticiones.
> **Servicio de red** — aplicación o proceso que ofrece una función accesible mediante la red, normalmente a través de uno o varios puertos.
> **Proceso** — instancia en ejecución de un programa dentro de un sistema operativo.
> **Demonio (daemon)** — proceso que permanece ejecutándose en segundo plano para prestar un servicio; en Linux es habitual que esté gestionado por `systemd`.
> **Puerto** — número lógico asociado a un servicio de transporte; permite distinguir varias comunicaciones que utilizan la misma dirección IP.
> **Socket** — extremo de comunicación que combina, según el contexto, una dirección IP, un puerto y un protocolo de transporte.
> **Interfaz de red** — componente físico o virtual mediante el que un sistema se conecta a una red.
> **Dirección IP** — identificador lógico de una interfaz dentro de una red IP.
> **Subred** — porción de un espacio de direccionamiento IP que comparte un prefijo común.
> **Puerta de enlace predeterminada** — equipo al que un host entrega el tráfico destinado a redes que no conoce directamente.
> **Encaminamiento (routing)** — proceso de decidir por qué camino debe avanzar un paquete para alcanzar su destino.
> **Tabla de encaminamiento** — conjunto de rutas que utiliza un sistema para decidir dónde enviar los paquetes.
> **Broadcast o difusión** — envío dirigido a todos los equipos de un dominio de difusión.
> **Unicast** — comunicación dirigida de un emisor a un receptor concreto.
> **Multicast** — comunicación dirigida a un grupo de receptores que se han suscrito al grupo.
> **Resolución de nombres** — proceso mediante el cual un sistema obtiene información asociada a un nombre, por ejemplo una dirección IP mediante DNS.
> **Caché** — almacenamiento temporal de resultados para poder reutilizarlos sin repetir inmediatamente una consulta o cálculo.
> **Archivo de configuración** — fichero que contiene parámetros con los que un programa determina cómo debe funcionar.
> **Validación** — comprobación de que una configuración tiene una sintaxis y una estructura aceptables antes de aplicarla.
> **Estado** — situación actual de un proceso, servicio, interfaz o recurso; conocerlo es esencial para diagnosticar una incidencia.
> **Registro (log)** — anotación generada por un programa o sistema para dejar constancia de eventos, errores y operaciones.
>
> Estos conceptos son el vocabulario común sobre el que se construyen las prácticas. Cuando una unidad introduzca un concepto especializado —por ejemplo, una zona DNS, una concesión DHCP, un virtual host, un contenedor o un Pod— se explicará de nuevo antes de utilizarlo operativamente.

> 🧠 **CONCEPTOS QUE NO DEBEMOS DAR POR SUPUESTOS**
>
> **`systemd`** — sistema de inicio y gestor de servicios habitual en Linux; `systemctl` permite consultar y administrar esos servicios.
> **Archivo de configuración** — fichero que contiene los parámetros con los que un servicio determina su comportamiento.
> **Registro DNS** — entrada de una zona DNS que asocia un nombre con un dato, como una dirección IP, un servidor de correo o un alias.
> **Zona DNS** — parte de la jerarquía DNS administrada por un servidor autoritativo concreto.
> **Servidor autoritativo** — servidor que posee la información oficial de una zona DNS y puede responder con autoridad sobre ella.
> **Resolver o resolvedor** — componente que realiza consultas DNS en nombre de una aplicación o de un usuario y obtiene la respuesta siguiendo el proceso de resolución.
> **Consulta recursiva** — consulta en la que el servidor consultado asume la tarea de obtener una respuesta completa para el cliente, si tiene habilitada la recursión.
> **Consulta iterativa** — consulta en la que el servidor responde con la mejor información que conoce, pudiendo remitir al consultante hacia otro servidor.
> **Concesión DHCP** — asignación temporal de una dirección IP y otros parámetros de red a un cliente.
> **Imagen de contenedor** — plantilla inmutable a partir de la cual se crean contenedores.
> **Volumen** — almacenamiento gestionado que permite conservar datos independientemente del ciclo de vida de un contenedor.
> **Red Docker** — red virtual administrada por Docker que permite conectar contenedores y, según su configuración, publicar servicios hacia el host.
> **Orquestación** — automatización de la ejecución, escalado, recuperación y coordinación de múltiples cargas de trabajo o contenedores.
> **Pod** — unidad mínima desplegable de Kubernetes; contiene uno o varios contenedores que comparten determinados recursos.
> **Virtual host** — configuración que permite que un mismo servidor web atienda distintos sitios o nombres mediante configuraciones diferenciadas.
> **Certificado digital** — credencial criptográfica que vincula una identidad con una clave pública y que puede estar firmada por una autoridad de certificación.
> **Códec** — algoritmo que codifica y decodifica audio, vídeo u otro tipo de datos; un códec no es lo mismo que un contenedor multimedia.
> **Contenedor multimedia** — formato de archivo que agrupa una o varias pistas de audio, vídeo, subtítulos o metadatos.
> **Streaming** — distribución de contenido de forma que el receptor puede comenzar a consumirlo mientras continúa recibiendo datos.
> **Commit** — instantánea registrada por Git que conserva un conjunto concreto de cambios.
> **Staging area** — área intermedia de Git donde se seleccionan los cambios que formarán el próximo commit.
> **Rama (branch)** — línea de desarrollo independiente dentro de un repositorio Git.
> **Remoto (remote)** — referencia a un repositorio Git externo con el que se intercambian commits mediante `fetch`, `pull` o `push`.
> **Codespace** — entorno de desarrollo remoto proporcionado por GitHub para trabajar con un repositorio.
> **Webmin** — interfaz web de administración de sistemas que permite gestionar determinados servicios y parámetros de un sistema Linux.
> **Roundcube** — cliente de correo web que accede al buzón mediante IMAP y puede enviar mensajes mediante SMTP.
> **Sympa** — gestor de listas de distribución que proporciona funciones de suscripción, moderación, administración y distribución de mensajes.

> **Material docente integral · CFGS ASIR**

## 1. 🎯 Método profesional

```text
REQUISITOS → DISEÑO → IMPLEMENTACIÓN → VALIDACIÓN → OBSERVABILIDAD → SEGURIDAD → DOCUMENTACIÓN
```

«El servicio arranca» no significa «el servicio está correctamente administrado».

## 2. 🔎 Diagnóstico por capas

```text
Aplicación
  ↓
Protocolo
  ↓
Puerto
  ↓
Transporte
  ↓
IP
  ↓
Ruta
  ↓
Interfaz
  ↓
Enlace
```

Ejemplo:

```bash
curl -v http://servidor:8080/
ss -lntp
ip addr
ip route
```

## 3. 📜 Logs

Linux:

```bash
journalctl -u nginx
journalctl -f
```

Docker:

```bash
docker logs servicio
docker compose logs -f servicio
```

Kubernetes:

```bash
kubectl logs pod
kubectl describe pod pod
kubectl get events
```

## 4. 🔌 Puertos

```bash
ss -lntup
sudo lsof -i -P -n
```

Preguntas obligatorias:

- ¿hay proceso escuchando?
- ¿en qué dirección?
- ¿qué protocolo?
- ¿qué PID?
- ¿qué firewall interviene?
- ¿coincide el puerto publicado con el interno?

## 5. 🧪 Plan de pruebas

| ID | Prueba | Resultado esperado | Evidencia |
|---|---|---|---|
| P01 | estado | servicio activo | `systemctl status` |
| P02 | escucha | puerto correcto | `ss` |
| P03 | resolución | nombre correcto | `dig` / `getent` |
| P04 | conectividad | conexión | `curl` / cliente |
| P05 | función | operación correcta | salida/captura |
| P06 | fallo controlado | diagnóstico | log |

## 6. 🔐 Seguridad

- mínimo privilegio;
- segmentación;
- no publicar puertos innecesarios;
- TLS cuando proceda;
- autenticación robusta;
- actualizaciones;
- copias de seguridad;
- secretos fuera de Git;
- laboratorio separado de producción.

## 7. 🧯 Fallos deliberados

Introducir uno por práctica:

- DNS: registro incorrecto;
- DHCP: pool incorrecto;
- FTP: rango pasivo bloqueado;
- HTTP: VirtualHost incorrecto;
- correo: relay incorrecto;
- XMPP: dominio erróneo;
- streaming: bitrate incompatible;
- Docker: puerto mal publicado.

El alumno debe aportar hipótesis, prueba, evidencia, causa, corrección y verificación.

## 8. 📝 Informe de incidencia

```text
INCIDENCIA
Servicio:
Impacto:

SÍNTOMA

HIPÓTESIS

PRUEBAS

EVIDENCIAS

CAUSA RAÍZ

CORRECCIÓN

VERIFICACIÓN

PREVENCIÓN
```

## 9. ⏱️ Reto de 1 h 45 min

Un Nginx publicado en `localhost:8080` deja de responder. El alumno debe:

1. comprobar contenedor;
2. consultar logs;
3. revisar publicación;
4. entrar en shell;
5. comprobar escucha interna;
6. localizar el error;
7. corregirlo;
8. demostrar el funcionamiento;
9. entregar el informe.

## 10. 🧠 Regla transversal

```text
OBSERVAR → HIPÓTESIS → MEDIR → CORREGIR → VERIFICAR → DOCUMENTAR
```
