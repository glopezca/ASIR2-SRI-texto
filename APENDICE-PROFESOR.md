# 👨‍🏫 APÉNDICE · Materiales para el profesor

> **Material docente integral · CFGS ASIR · Servicios de Red e Internet**

Este apéndice contiene instrumentos de evaluación y propuestas de laboratorio alineados con las ocho UT y con los resultados de aprendizaje del módulo.

> 🧭 **ANTES DE UTILIZAR LAS RÚBRICAS**
>
> Una **rúbrica** es una matriz que relaciona criterios de evaluación con niveles o evidencias observables. Un **instrumento de evaluación** es el procedimiento o recurso utilizado para recoger evidencias del aprendizaje. El **solucionario** contiene las respuestas o vías de resolución de referencia.

## 1. 🎯 Criterios de uso

Las pruebas tipo test están diseñadas como instrumentos de comprobación, no como sustituto de la evaluación práctica. Cada UT contiene **3 preguntas**, con **una única respuesta válida**. La posición de la respuesta correcta se distribuye deliberadamente para evitar patrones previsibles.

Las actividades prácticas están diseñadas para una duración máxima de **1 h 45 min** y se pueden ejecutar en VirtualBox + Ubuntu 26.04 Server, WSL2 o, cuando proceda, Cisco Packet Tracer.

---

# 2. 📝 Banco de test por UT

## UT1 · TCP/IP

**1. ¿Qué función corresponde principalmente a la capa de transporte?**

A. Resolver nombres DNS.
B. Proporcionar comunicación extremo a extremo mediante protocolos como TCP y UDP.
C. Asignar direcciones MAC.
D. Determinar exclusivamente la ruta IP.

**2. ¿Qué describe mejor una ruta por defecto?**

A. Una ruta utilizada cuando no existe una ruta más específica para el destino.
B. Una ruta que siempre apunta al servidor DNS.
C. Una ruta que sólo funciona con UDP.
D. Una ruta utilizada únicamente para tráfico multicast.

**3. ¿Qué hace PAT en un escenario típico de NAT?**

A. Convierte nombres DNS en direcciones IPv6.
B. Sustituye TCP por UDP.
C. Permite multiplexar conexiones mediante diferentes puertos usando una dirección pública compartida.
D. Elimina la necesidad de encaminamiento.

## UT2 · DHCP

**4. ¿Cuál es el orden habitual del proceso DORA?**

A. Discover → Offer → Request → Acknowledge.
B. Discover → Request → Offer → Acknowledge.
C. Offer → Discover → Acknowledge → Request.
D. Request → Offer → Discover → Acknowledge.

**5. ¿Qué diferencia una reserva DHCP de una concesión dinámica ordinaria?**

A. Una reserva impide utilizar DNS.
B. Una reserva asocia de forma estable determinados parámetros, normalmente una IP, con un cliente identificado.
C. Una reserva sólo funciona con IPv6.
D. Una reserva sustituye al gateway.

**6. ¿Para qué sirve un DHCP relay?**

A. Para cifrar DHCP.
B. Para sustituir el servidor DNS.
C. Para almacenar las concesiones en una base de datos.
D. Para permitir que solicitudes DHCP atraviesen segmentos de red donde el broadcast no puede llegar directamente al servidor.

## UT3 · DNS

**7. ¿Qué registro se utiliza habitualmente para asociar un nombre con una dirección IP?**

A. MX
B. AAAA
C. A
D. PTR

**8. ¿Qué caracteriza a un servidor DNS autoritativo?**

A. Siempre reenvía todas las consultas a Google.
B. Posee información autoritativa sobre una o más zonas.
C. Sólo puede resolver direcciones IPv6.
D. No puede responder consultas recursivas.

**9. ¿Qué comando es especialmente apropiado para comprobar registros DNS y observar respuestas detalladas?**

A. `dig`
B. `scp`
C. `sshd`
D. `ip link set`

## UT4 · Transferencia de ficheros

**10. ¿Cuál es la característica fundamental de SFTP?**

A. Es FTP con UDP.
B. Es un protocolo independiente basado en SSH.
C. Es FTP sin autenticación.
D. Es TFTP sobre TLS.

**11. En FTP tradicional, ¿qué puerto TCP se utiliza normalmente para el canal de control?**

A. 20
B. 22
C. 25
D. 21

**12. ¿Por qué el modo pasivo de FTP es especialmente relevante cuando existen firewalls o NAT?**

A. Porque elimina TCP.
B. Porque utiliza exclusivamente el puerto 21 para todo.
C. Porque permite que el cliente inicie también la conexión de datos, facilitando determinados escenarios atravesando firewalls/NAT.
D. Porque convierte FTP en SFTP.

## UT5 · HTTP

**13. ¿Qué función desempeña un Virtual Host?**

A. Permite servir diferentes sitios o configuraciones desde una misma infraestructura web según criterios como nombre, dirección o puerto.
B. Sustituye siempre al DNS.
C. Convierte HTTP en FTP.
D. Impide utilizar TLS.

**14. ¿Qué herramienta es adecuada para realizar una prueba HTTP desde una terminal?**

A. `dig`
B. `curl`
C. `scp`
D. `ip neigh flush`

**15. ¿Qué diferencia fundamental existe entre `proxy_pass` de Nginx y un servidor web que entrega directamente un fichero estático?**

A. `proxy_pass` permite reenviar la petición a otro servicio backend.
B. `proxy_pass` sólo funciona con FTP.
C. Un servidor estático no utiliza HTTP.
D. `proxy_pass` desactiva DNS.

## UT6 · Correo electrónico

**16. ¿Cuál es la función principal de SMTP?**

A. Leer exclusivamente mensajes mediante IMAP.
B. Transferir mensajes de correo entre agentes y servidores de correo.
C. Resolver nombres de dominio.
D. Cifrar discos.

**17. ¿Qué protocolo está orientado principalmente al acceso remoto a un buzón manteniendo los mensajes en el servidor?**

A. IMAP
B. TFTP
C. DNS
D. ARP

**18. ¿Qué registro DNS se utiliza para indicar servidores de correo de un dominio?**

A. TXT exclusivamente
B. PTR
C. MX
D. CNAME exclusivamente

## UT7 · Mensajería, noticias y listas

**19. ¿Qué protocolo está asociado históricamente con la mensajería instantánea extensible y la presencia?**

A. XMPP
B. FTP
C. SMTP
D. SNMP

**20. ¿Qué caracteriza a una lista de distribución?**

A. Cada mensaje sólo puede tener un destinatario.
B. Permite distribuir mensajes a un conjunto de suscriptores según las reglas configuradas.
C. Sustituye necesariamente a DNS.
D. Utiliza exclusivamente UDP.

**21. ¿Qué protocolo se asocia con los servicios de noticias Usenet?**

A. DHCP
B. HTTP
C. NNTP
D. IMAP

## UT8 · Audio y vídeo

**22. ¿Qué diferencia básica existe entre un códec y un contenedor multimedia?**

A. Son exactamente lo mismo.
B. El códec define la compresión/codificación; el contenedor organiza uno o varios flujos y metadatos.
C. El contenedor sólo existe para audio.
D. El códec sólo define la dirección IP.

**23. ¿Qué componente es apropiado para servir audio mediante streaming en un laboratorio SRI?**

A. Icecast
B. BIND9
C. Kea DHCP
D. Postfix

**24. ¿Qué ventaja fundamental aporta HLS?**

A. Elimina la necesidad de cualquier servidor HTTP.
B. Permite distribuir vídeo mediante HTTP utilizando una playlist y segmentos.
C. Sólo funciona sobre FTP.
D. Sustituye a los códecs.

---

# 3. ✅ Solucionario del test

| Pregunta | Respuesta | UT |
|---:|:---:|:---:|
| 1 | **B** | UT1 |
| 2 | **A** | UT1 |
| 3 | **C** | UT1 |
| 4 | **A** | UT2 |
| 5 | **B** | UT2 |
| 6 | **D** | UT2 |
| 7 | **C** | UT3 |
| 8 | **B** | UT3 |
| 9 | **A** | UT3 |
| 10 | **B** | UT4 |
| 11 | **D** | UT4 |
| 12 | **C** | UT4 |
| 13 | **A** | UT5 |
| 14 | **B** | UT5 |
| 15 | **A** | UT5 |
| 16 | **B** | UT6 |
| 17 | **A** | UT6 |
| 18 | **C** | UT6 |
| 19 | **A** | UT7 |
| 20 | **B** | UT7 |
| 21 | **C** | UT7 |
| 22 | **B** | UT8 |
| 23 | **A** | UT8 |
| 24 | **B** | UT8 |

La distribución de respuestas evita utilizar una única posición como patrón de corrección.

---

# 4. 🧪 Prácticas evaluables de máximo 1 h 45 min

## PE01 · TCP/IP y diagnóstico

**Entorno:** VirtualBox + Ubuntu 26.04 Server + cliente Linux.

### Enunciado

Configura una red privada entre dos máquinas. El servidor debe tener una dirección estática y el cliente debe poder alcanzarlo. Documenta direccionamiento, rutas y puertos abiertos.

### Evidencias

```bash
ip addr
ip route
ss -lntup
ping -c 4 SERVIDOR
```

**Duración:** 1 h 30 min.

## PE02 · DHCP con Kea

**Entorno:** VirtualBox + Ubuntu Server.

Instala Kea DHCP, configura una subred de laboratorio, un pool y una reserva. Valida la configuración antes de reiniciar el servicio y demuestra una concesión correcta.

**Duración:** 1 h 45 min.

## PE03 · DNS con BIND9

Crea una zona directa e inversa. Añade registros `A`, `AAAA` y `MX`. Comprueba la resolución con `dig` y documenta el resultado.

**Duración:** 1 h 45 min.

## PE04 · Transferencia segura

Configura SSH/SFTP. Crea un usuario limitado y demuestra una transferencia de fichero. Comprueba permisos y registra las pruebas.

**Duración:** 1 h 30 min.

## PE05 · Dos sitios web

Configura Apache o Nginx con dos sitios virtuales y acceso HTTPS de laboratorio. Analiza los logs y demuestra mediante `curl` qué sitio responde a cada nombre.

**Duración:** 1 h 45 min.

## PE06 · Correo en laboratorio

Configura un MTA y un servicio de acceso al buzón en una red privada. Demuestra SMTP y acceso al buzón. Comprueba que el servidor no funciona como relay abierto.

**Duración:** 1 h 45 min.

## PE07 · Mensajería instantánea

Despliega un servidor XMPP de laboratorio, crea dos cuentas y demuestra una sesión entre dos clientes. Documenta autenticación y puertos.

**Duración:** 1 h 30 min.

## PE08 · Streaming de audio

Instala Icecast y utiliza FFmpeg para producir un flujo de audio de laboratorio. Accede desde VLC, mide el bitrate y documenta el recorrido completo.

**Duración:** 1 h 45 min.

---

# 5. 🧩 Práctica integradora

## Proyecto · Servicios de red reproducibles

Construye una infraestructura que contenga como mínimo:

```text
                 ┌──────────────┐
                 │     DNS      │
                 └──────┬───────┘
                        │
          ┌─────────────┼─────────────┐
          ▼             ▼             ▼
       HTTP           SFTP          XMPP
          │             │             │
          └─────────────┼─────────────┘
                        ▼
                  cliente de pruebas
```

El proyecto debe incluir:

- diagrama de red;
- direccionamiento;
- puertos;
- configuración;
- pruebas;
- logs;
- medidas de seguridad;
- README técnico;
- repositorio Git;
- versión Docker Compose cuando el servicio lo permita.

**Duración recomendada:** varias sesiones. No utilizar como práctica de 1 h 45 min.

---

# 6. 📚 Sobre las preguntas de evaluación del material de referencia

El apéndice se ha diseñado a partir de los **contenidos, objetivos y criterios de evaluación del módulo**, y sus preguntas están formuladas específicamente para el currículo y las tecnologías actuales. Se priorizan preguntas que permitan comprobar comprensión conceptual y capacidad de razonamiento técnico.

La cobertura de evaluación se mantiene mediante bloques equivalentes:

| UT | Contenidos evaluados |
|---|---|
| UT1 | arquitectura TCP/IP, IP/IPv6, subredes, transporte, puertos, NAT/PAT, routing y virtualización |
| UT2 | DHCP, DORA, concesiones, reservas, opciones, relay, DHCPv6 y seguridad |
| UT3 | DNS, zonas, registros, resolución, BIND9, delegación, transferencia de zona y seguridad |
| UT4 | FTP, FTPS, TFTP, SFTP/SCP, modos, autenticación, permisos y seguridad |
| UT5 | WWW, URI/URL, HTTP, MIME, servidores, proxies, Virtual Hosts, HTTPS y logs |
| UT6 | arquitectura de correo, SMTP, IMAP, POP3, MIME, MTA/MUA/MRA, TLS, spam y autenticación |
| UT7 | mensajería instantánea, XMPP, IRC, listas de distribución, NNTP, servidores y clientes |
| UT8 | formatos, códecs, contenedores, reproducción, streaming, podcast, VoIP y videoconferencia |

La adaptación evita trasladar preguntas dependientes de productos, versiones o interfaces que han quedado obsoletas y permite evaluar los conceptos mediante las plataformas actuales del laboratorio.

---

# 7. 🧾 Rúbrica común para prácticas

| Criterio | Peso orientativo |
|---|---:|
| Comprensión del problema | 15 % |
| Diseño de la solución | 15 % |
| Configuración correcta | 25 % |
| Pruebas y evidencias | 20 % |
| Diagnóstico | 10 % |
| Seguridad | 5 % |
| Documentación | 10 % |

La ponderación concreta debe adaptarse a la programación didáctica y a los criterios de evaluación del RA correspondiente.

---

# 8. 🧠 Lista de comprobación del profesor

Antes de utilizar una práctica:

- [ ] ¿La versión de Ubuntu está disponible?
- [ ] ¿El paquete/software sigue existiendo?
- [ ] ¿Los puertos son correctos?
- [ ] ¿La configuración se valida antes de reiniciar?
- [ ] ¿Existe una prueba funcional objetiva?
- [ ] ¿Hay una incidencia deliberada o supuesto de diagnóstico?
- [ ] ¿La práctica puede completarse en el tiempo previsto?
- [ ] ¿La evidencia entregada permite corregirla sin repetir el laboratorio?
- [ ] ¿Los secretos están fuera del repositorio?
- [ ] ¿La práctica está vinculada al RA y a sus criterios de evaluación?

---

# 9. 🏁 Principio metodológico

> **No evaluar sólo que el servicio funcione. Evaluar que el alumno sepa explicar por qué funciona, demostrarlo, detectar cuándo deja de funcionar y justificar cómo lo ha solucionado.**
