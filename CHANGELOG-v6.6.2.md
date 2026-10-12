# CHANGELOG · ASIR2-SRI-texto · v6.6.2

## Anexo XXII

[Anexo XXII · Simulador netsim: DHCP en Cisco IOS y servicios Server-PT](ANEXO-XXII-Simulador-de-redes.md) actualizado a netsim v0.2.

- **Server-PT y terminales.** El anexo recoge los servidores Server-PT con DHCP (con reservas por MAC), DNS, HTTP, correo SMTP/POP3/IMAP y SSH. También describe los terminales GNU/Linux y Windows, el navegador y el cliente de correo de los PC.
- **Correspondencia ampliada** a:
  - UT2 Práctica 1 (Arnor con reservas `.64` y `.65`);
  - UT3 (DNS de Lothlorien para `tierramedia.jc`);
  - UT4 (HTTP en Server-PT);
  - UT6 Prácticas 6.1 y 6.2 (correo con MX).
- **Credenciales.** Nueva tabla con los usuarios y contraseñas de ejemplo del laboratorio Server-PT.
- **Guardado.** Se describe el guardado de arquitecturas en `.json` y la simulación de DNS, TCP, HTTP, SMTP, POP3, IMAP y SSH.
- **Límites actualizados.**

## Enlaces desde las unidades

Cada unidad tiene un único enlace a la sección correspondiente del anexo, sin duplicar contenido:
- UT2 §25.3 (reservas por MAC en el servidor gráfico);
- UT3, práctica integradora de DNS en Packet Tracer;
- UT4, ruta Packet Tracer;
- UT6, Práctica 6.1.

En UT2 §26 se indica que netsim admite `show running-config | section dhcp`.

## Índices y metadatos

- README, índice general e índice alfabético actualizados.
- Versión 6.6.2 en `VERSION`, `CITATION.cff` y README.

## Comprobaciones

Los escenarios Tierra Media de UT2 (Arnor y Mordor) y UT3 (Lothlorien) se verifican como pruebas automáticas en netsim (`tests/services/tierramedia.test.ts`).

## Compatibilidad

El nombre de archivo del anexo no cambia, así que los enlaces existentes siguen funcionando.
