# 🛡️ ANEXO V · Seguridad, observabilidad, pruebas y troubleshooting

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
