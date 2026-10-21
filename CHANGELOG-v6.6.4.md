# CHANGELOG · ASIR2-SRI-texto · v6.6.4

## UT2 · Ejemplos de Kea completos y ejecutables

Revisión de los cinco ejemplos JSON de Kea de la [UT2](UT2-Servicio-DHCP.md). Ninguno se podía cargar tal cual en el
Kea de Ubuntu 26.04 (Kea 3.0):

| Ejemplo | Problema | `kea-dhcp4 -t` antes |
|---|---|---|
| §7 Reservas y práctica de reservas (§30) | Fragmento `{ "reservations": [...] }` sin `Dhcp4` ni subred | `syntax error, unexpected constant string, expecting Dhcp4` |
| §20 Opciones (`option-data`) | Fragmento sin `Dhcp4` ni subred | `syntax error, unexpected constant string, expecting Dhcp4` |
| §28.2 Mordor · Tierra Media | Subred sin `id`; sin reservas `.64`/`.65` que la práctica comprueba | `subnet configuration failed: missing parameter 'id'` |
| §29 Solución de referencia | Subred sin `id`; interfaz `<interfaz>` | `subnet configuration failed: missing parameter 'id'` |

Cambios:

- Todos son ahora un `/etc/kea/kea-dhcp4.conf` completo: `interfaces-config` (`enp0s8`, la tarjeta interna de la VM),
  `lease-database` (`memfile` en `/var/lib/kea/kea-leases4.csv`), `valid-lifetime` y `subnet4` con su **`id`**,
  obligatorio desde Kea 2.6.0 ([ISC: cambios al migrar a Kea 2.6.0](https://kb.isc.org/docs/changes-to-be-aware-of-when-migrating-to-kea-2-6-0)).
- Las reservas van dentro de la subred (`subnet4[].reservations`) y fuera del pool. En Tierra Media se añaden las de
  Gondor (`.64`) y Rohan (`.65`) con MAC de ejemplo de VirtualBox (`08:00:27:…`), que el alumno sustituye por las reales.
- El esquema de la estructura de Kea (§28.2) muestra `id` y `reservations` dentro de `subnet4`, y una nota explica el
  error que da Kea cuando falta `id`.
- §28.3 valida también con `kea-dhcp4 -t`: `python3 -m json.tool` acepta una subred sin `id`.
- Los subapartados de la práctica 4 (§28) se numeraban 27.1–27.5; ahora 28.1–28.5.

## Cómo se ha comprobado

Con `kea-dhcp4` 3.0.4 compilado desde el código fuente de ISC, sobre los bloques extraídos del propio texto:
`python3 -m json.tool` y `kea-dhcp4 -t` aceptan los cinco (código 0). El único cambio para la prueba fue el nombre de
la interfaz, porque Kea comprueba que exista: en la VM se usa `enp0s8`.

## Metadatos

- Versión 6.6.4 en `VERSION`, `CITATION.cff` y README.
