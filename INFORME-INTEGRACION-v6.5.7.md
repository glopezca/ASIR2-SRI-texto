# Informe de integración de mejoras · v6.5.7

La v6.5.7 es una actualización incremental de v6.5.6 centrada en la **coherencia pedagógica de la UT1**. No cambia la arquitectura común del repositorio: la desarrolla y la hace explícita en los puntos 27 y 28.

## 1. Punto 27

Se detectó que la práctica de VirtualBox comenzaba con una topología genérica de tres máquinas y dos LAN, incompatible con la regla de continuidad establecida en el repositorio. Se sustituye por la arquitectura Tierra Media: tres zonas, Mordor como router y las cinco VMs oficiales.

## 2. Punto 28

La explicación de nftables se amplía para que el alumno comprenda primero el problema de red y después la sintaxis. La secuencia conceptual es: **routing → forwarding → filtrado → NAT → persistencia**. Las analogías se conectan directamente con Mordor como frontera/aduana y con el recorrido real de un paquete de Gondor o Lothlorien.

## 3. No regresión

Se mantienen los elementos introducidos en v6.5.6: Packet Tracer Tierra Media completo en UT1/UT3, Arnor DHCP gráfico → Mordor DHCP CLI → Kea en UT2, WSL como cliente/diagnóstico, cinco VMs de VirtualBox, Lothlorien como servidor principal, Rivendel como auxiliar, Webmin en las UT y documentación de nftables con `/etc/nftables.conf`.
