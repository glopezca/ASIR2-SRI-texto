# 🧹 ANEXO XVI · Auditoría de obsolescencia y sustitución

## Regla de oro

Una tecnología se mantiene en la edición principal cuando sigue siendo válida para el objetivo didáctico y dispone de un camino razonable de aprendizaje. Cuando envejece, hay tres opciones: **actualizar**, **mantener como histórico** o **retirar**.

| Tecnología/tema | Estado v6.5.1 | Tratamiento |
|---|---|---|
| Ubuntu 26.04 LTS | principal | laboratorio de referencia |
| BIND9 | principal | DNS autoritativo, caché, transferencias |
| Kea | principal | DHCP moderno |
| ISC DHCP clásico | histórico | explicar migración conceptual a Kea cuando proceda |
| Apache HTTP Server | principal | práctica y comparación |
| Nginx | principal | reverse proxy, HTTP/2/3, streaming |
| FTP | conceptual/histórico | se mantiene para comprender activo/pasivo y legado |
| FTPS | vigente en escenarios que lo requieran | comparar con SFTP |
| SFTP | principal | opción recomendada para laboratorio de transferencia segura |
| Postfix + Dovecot | principal | administración del servicio de correo |
| Roundcube | principal | MUA web de laboratorio |
| Mailman 3 | principal | listas de distribución |
| Sympa | alternativa docente | práctica de listas y administración web |
| XMPP | principal/histórico-profesional | modelo abierto de mensajería y presencia |
| NNTP/Usenet | histórico con valor didáctico | práctica de protocolo y publicación distribuida |
| Icecast | principal en audio | streaming de audio de laboratorio |
| RTMP | ingesta/legado | enseñar arquitectura, no presentarlo como único modelo moderno |
| HLS | principal | distribución HTTP segmentada |
| HTTP/3 + QUIC | ampliación profesional | comprender cambio de transporte y diagnóstico |
| Docker Compose | principal | despliegue reproducible |
| Kubernetes | ampliación profesional | modelo de Pods/Services/Probes y transición desde Compose |
