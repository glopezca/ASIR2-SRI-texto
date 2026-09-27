# 🧪 ANEXO XV · Guía de laboratorio reproducible

## 1. Convención de nombres

- Dominio pedagógico: `juandecolonia.jc`
- Servidores: `srv01`, `srv02`, `dns01`, `mail01`, `web01`
- Clientes: `cli01`, `cli02`
- Redes de laboratorio: documentar prefijo y propósito antes de asignar direcciones.

## 2. Estado base

Cada máquina de laboratorio debe disponer de:

```text
nombre conocido
→ interfaces identificadas
→ rutas conocidas
→ DNS conocido
→ SSH operativo
→ snapshot limpio
→ fecha/hora de la preparación
```

## 3. Regla de reproducibilidad

Una práctica es reproducible cuando otro alumno puede reconstruir el estado inicial a partir de la ficha, ejecutar el procedimiento, realizar la misma prueba y obtener una evidencia comparable.

## 4. Reseteo entre prácticas

1. guardar evidencias;
2. detener servicios;
3. revertir cambios del ejercicio;
4. comprobar que los puertos esperados desaparecen o reaparecen según proceda;
5. restaurar snapshot cuando el ejercicio lo requiera;
6. registrar cualquier diferencia residual.

## 5. Paridad entre entornos

| Objetivo | I Packet Tracer | II WSL2 | III VirtualBox | IV Compose |
|---|---|---|---|---|
| topología | excelente | limitada | excelente | redes virtuales |
| cliente CLI | limitada | excelente | excelente | excelente |
| servidor completo | no | parcial | excelente | contenedores |
| configuración declarativa | parcial | scripts | Netplan/config files | YAML Compose |
| multi-servicio reproducible | no | scripts | snapshots | excelente |

## 6. Evidencias

Se recomienda una estructura de carpetas por práctica:

```text
evidencias/
  01-estado-inicial/
  02-configuracion/
  03-pruebas/
  04-diagnostico/
  05-cierre/
```

## 7. Relación con producción

El laboratorio no pretende reproducir toda la complejidad de producción. Su función es practicar el mismo **modelo de operación**: declarar estado, observar, cambiar, validar, registrar y revertir.
