# v6.5.8e

## Correcciones curriculares y visuales

- Se incorpora de forma explícita la correspondencia curricular del módulo 0375 con los **RA1–RA8**.
- Se fija la correspondencia: **UT2→RA2, UT3→RA1, UT4→RA4, UT5→RA3, UT6→RA5, UT7→RA6 y UT8→RA7+RA8**.
- **UT1** queda identificada como unidad de fundamentación transversal y no se fuerza su asignación a un RA.
- Se recupera como **único esquema del entorno de red del laboratorio** el PNG mejorado basado en Cisco Packet Tracer: `img/topologia-tierramedia-packettracer.png`.
- Se elimina del repositorio el SVG de topología generado posteriormente.
- Se actualizan README, matriz curricular, índice, arquitectura y documentación de versión a v6.5.8e.

# v6.5.8e

- Corrección de sintaxis declarativa de `nftables` para compatibilidad con Webmin: `type`, `hook`, `priority` y `policy` quedan en una única línea de definición de cadena base.
- Revisados los fragmentos de `input`, `forward`, `output` y `postrouting` de UT1.
- Añadida comprobación específica y documentación del comportamiento de Webmin.

# Changelog

## v6.5.5 — 27/09/2026

- Añadido `INDICE-GENERAL.md` como índice de navegación del repositorio.
- El nuevo índice enlaza directamente las ocho UT, los dieciocho anexos y los materiales complementarios principales.
- Añadido un enlace visible al índice general desde el README, manteniendo separado el índice alfabético de conceptos.


## v6.5.2 — 27/09/2026

- Añadido enlace directo al **índice alfabético** desde el README.
- Reincorporado como fuente de revisión el libro **Preparación del entorno** del CIFP Juan de Colonia.
- Fusionada y sintetizada su sección de comandos de red con `ANEXO-XVIII-Chuleta-Comandos-Red-Ubuntu.md`.
- Incorporados a la chuleta: interfaces, rutas, vecinos, conectividad, DNS, puertos, Netplan, `systemctl`, UFW, Nmap, registros y herramientas auxiliares.
- Conservados como referencia histórica los comandos y herramientas que pueden aparecer en material anterior (`ifconfig`, `ifup`/`ifdown`, `netstat`).
- Corregida la referencia de instalación de `netstat`: se utiliza `net-tools`, no `netstat-nat`.


## v6.5.2 · Revisión didáctica y recuperación de materiales

### Presentación para el alumnado
- Se sustituye la representación gráfica de los cuatro entornos por una cuadrícula 2×2 estable para evitar que el Entorno IV aparezca separado.
- Se reorganizan las guías iniciales de UT2–UT8 para que el alumno vea primero el título, el objetivo y la forma de trabajo.
- Se simplifican etiquetas para dirigir el texto directamente al alumno.
- Se refuerza el patrón visual **mira → entiende → prueba → configura → comprueba → explica**.

### Materiales del CIFP Juan de Colonia
- Se incorpora `ANEXO-XVIII-Chuleta-Comandos-Red-Ubuntu.md`.
- Se recupera explícitamente la preparación común del puesto y los comandos de diagnóstico presentes en los materiales del CIFP.
- Se mantiene la corrección técnica de procedimientos antiguos antes de incorporarlos al camino principal.

### Webmin
- Se elimina `img/captura-webmin-didactica.png`.
- Se eliminan las capturas sintéticas de Webmin del material principal.
- Se añaden referencias a la documentación oficial de Webmin para BIND, red y DHCP/Kea.
- Las capturas utilizadas en clase deben proceder de una instalación real y de la versión del aula.

### Terminología
- Se elimina la palabra de carácter publicitario indicada en la revisión de v6.5.2 de todo el texto de la versión.


## v6.5 · Edición 2026

### Pedagogía y edición

- Se consolida una única preparación común por UT.
- Las prácticas usan pistas específicas y no replican el bloque común.
- Se añaden glosarios esenciales, ejercicios propuestos y recursos oficiales a las UT.
- Se incorporan plantillas de entregables profesionales, matriz curricular, guía de laboratorio reproducible e índice alfabético.
- Se refuerza la metodología de apoyo graduado, metacognición, error productivo y transferencia.

### Actualidad técnica

- La preparación del laboratorio se concentra en UT1.
- Se incorporan y corrigen contenidos aportados por los materiales del CIFP Juan de Colonia.
- Se descartan recetas obsoletas o inseguras y se documentan las decisiones en `INFORME-REVISION-FUENTES-v6.5.md`.
- Se refuerzan IPv6, HTTP/2/3, QUIC, TLS, DNSSEC, correo autenticado, observabilidad, Docker Compose y Kubernetes como puentes profesionales.

### Autoría y licencia

- Se incorpora explícitamente la atribución a **Germán López Castro**.
- Se actualizan `LICENSE.md`, `NOTICE.md` y `CITATION.cff` para identificar autor y repositorio.

### Automatización

- Se documenta y endurece el algoritmo de actualización en `ANEXO-XVII-Algoritmo-Actualizacion.md`.
- Se añade un actualizador ejecutable en `tools/update_material.py`.

## v6.5.8e
- Limpieza de referencias internas de citación visibles.
- Corrección visual de las infografías TUI: Pro Tips precedidos por bombilla.
