# 🧱 ENTORNO IV · Infraestructura de las UT1–UT8 con Docker Compose

> **Material docente integral · CFGS ASIR**

## 1. 🎯 Objetivos

Convertir los laboratorios en infraestructuras reproducibles y versionables, con especial atención a **redes, puertos, DNS interno, volúmenes, healthchecks y pruebas**.

## 2. 🧭 Patrón común

```text
compose.yaml
  ├── services
  ├── networks
  ├── volumes
  └── healthchecks
```

## 3. UT1 · TCP/IP

Para herramientas de diagnóstico puede utilizarse un contenedor de laboratorio:

```yaml
services:
  toolbox:
    image: nicolaka/netshoot:latest
    command: ["sleep", "infinity"]
```

```bash
docker compose up -d
docker compose exec toolbox ip addr
docker compose exec toolbox ip route
docker compose exec toolbox ss -lntup
docker compose down
```

Para prácticas de routing real se mantiene VirtualBox/Packet Tracer.

## 4. UT2 · DHCP

DHCP requiere cuidado con broadcast, interfaces y privilegios. Compose sirve para laboratorios controlados, pero las pruebas que necesitan una LAN real se realizarán en VirtualBox o Packet Tracer.

Kea debe validarse antes de iniciar:

```bash
kea-dhcp4 -t /etc/kea/kea-dhcp4.conf
```

## 5. UT3 · DNS

Arquitectura:

```text
DNS server ──┐
             ├── dnsnet ── client
```

Ejemplo conceptual:

```yaml
services:
  dns:
    image: ubuntu/bind9:latest
    ports:
      - "5353:53/udp"
      - "5353:53/tcp"
    networks: [dnsnet]

  client:
    image: alpine:latest
    command: ["sleep", "infinity"]
    networks: [dnsnet]

networks:
  dnsnet:
```

Prueba:

```bash
docker compose exec client nslookup ejemplo.test dns
```

## 6. UT4 · Transferencia

SFTP se basa en SSH. El laboratorio debe mantener el acceso limitado y no publicar credenciales reales.

```text
cliente ── SSH/SFTP ── servidor
```

Cuando se utilice una imagen de terceros, fijar una versión o digest para hacer reproducible la práctica.

## 7. UT5 · Web

```text
localhost:8080
      ↓
   Nginx
      ↓
   app:8000
```

```yaml
services:
  proxy:
    image: nginx:alpine
    ports:
      - "8080:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
    networks: [frontend, backend]

  app:
    image: python:3-alpine
    command: ["python", "-m", "http.server", "8000", "--bind", "0.0.0.0"]
    working_dir: /srv
    volumes:
      - ./app:/srv:ro
    expose: ["8000"]
    networks: [backend]

networks:
  frontend:
  backend:
```

## 8. UT6 · Correo

Arquitectura de referencia:

```text
MUA → Submission → MTA → SMTP → MTA → Mailbox → IMAP
```

El laboratorio debe ser privado y nunca convertirse en relay abierto.

## 9. UT7 · Mensajería

```text
           red-comunica
          /      |      \
       XMPP     IRC    cliente
```

Prosody, InspIRCd y herramientas equivalentes deben fijarse a versiones compatibles con la práctica.

## 10. UT8 · Multimedia

```text
FFmpeg → Icecast → VLC
FFmpeg → RTMP → Nginx → HLS → cliente
```

Separar siempre generación, codificación, distribución y reproducción.

## 11. 🔌 Regla de puertos

```text
¿Necesita acceso el host?
  ├─ sí → ports
  └─ no → red interna
```

Ejemplo:

```yaml
ports:
  - "8080:80"
```

significa **HOST 8080 → CONTENEDOR 80**.

## 12. ❤️ Healthcheck

```yaml
healthcheck:
  test: ["CMD", "wget", "--spider", "-q", "http://localhost/"]
  interval: 10s
  timeout: 3s
  retries: 5
```

Un contenedor ejecutándose no implica que la aplicación esté lista.

## 13. 🧪 Matriz de pruebas

| UT | Configuración | Arranque | Red | Funcionalidad | Diagnóstico |
|---|---|---|---|---|---|
| UT1 | ✓ | ✓ | ✓ | ✓ | ✓ |
| UT2 | ✓ | ✓ | depende del modo de red | ✓ | ✓ |
| UT3 | ✓ | ✓ | ✓ | `dig` | ✓ |
| UT4 | ✓ | ✓ | ✓ | transferencia | ✓ |
| UT5 | ✓ | ✓ | ✓ | HTTP | ✓ |
| UT6 | ✓ | ✓ | ✓ | SMTP/IMAP | ✓ |
| UT7 | ✓ | ✓ | ✓ | sesión | ✓ |
| UT8 | ✓ | ✓ | ✓ | streaming | ✓ |

## 14. ⚠️ Validación real

En el entorno de generación de esta  no existe Docker Engine ni un Codespace ejecutable. Por tanto, esta guía **no afirma haber ejecutado extremo a extremo** los ocho Compose. Antes de usar estos despliegues como evaluación práctica deben probarse en:

1. WSL2 + Docker Desktop;
2. un Codespace con Docker operativo;
3. VirtualBox para protocolos que requieren capacidades de red específicas.

## 15. 📚 Documentación oficial

- https://docs.docker.com/compose/
- https://docs.docker.com/reference/compose-file/
- https://docs.docker.com/engine/network/
- https://docs.docker.com/engine/storage/volumes/
- https://bind9.readthedocs.io/
- https://nginx.org/en/docs/
- https://www.openssh.com/manual.html
- https://www.postfix.org/documentation.html
- https://doc.dovecot.org/
- https://prosody.im/doc/
- https://icecast.org/docs/
- https://ffmpeg.org/documentation.html
