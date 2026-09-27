# Anexo XVIII · Chuleta de comandos de red en Ubuntu

> **Objetivo:** tener en una sola página los comandos que más vas a utilizar para comprobar una red. Sirve para **consultar, probar y diagnosticar**.

## 1. ¿Qué interfaces tengo?

| Necesito saber… | Comando |
|---|---|
| Direcciones y estado de las interfaces | `ip addr` |
| Una interfaz concreta | `ip addr show ens33` |
| Estado de los enlaces | `ip link show` |
| Estadísticas de una interfaz | `ip -s link show ens33` |

## 2. ¿Por dónde salen los paquetes?

```bash
ip route
ip route get 8.8.8.8
```

`ip route` muestra la tabla de rutas. `ip route get DESTINO` indica qué ruta utilizaría el kernel.

## 3. ¿Tengo conectividad?

```bash
ping -c 4 192.168.1.1
ping -c 4 8.8.8.8
```

Prueba en este orden: **tu configuración → puerta de enlace → conectividad por IP → DNS**.

> Si funciona `ping 8.8.8.8` pero falla `ping google.com`, la conectividad IP existe y debes investigar la resolución de nombres.

## 4. ¿Qué DNS estoy usando?

```bash
resolvectl status
resolvectl dns
resolvectl query example.com
systemctl status systemd-resolved
```

No edites `/etc/resolv.conf` a ciegas: en Ubuntu moderno puede estar gestionado por el sistema.

## 5. ¿Qué servicios están escuchando?

```bash
ss -lntup
ss -lntup | grep ':53'
ss -lntup | grep ':22'
ss -lntup | grep ':80'
```

- `-l` → escucha
- `-n` → no resuelve nombres
- `-t` → TCP
- `-u` → UDP
- `-p` → muestra el proceso, si tienes permisos

## 6. ¿Qué proceso utiliza un puerto?

```bash
sudo ss -lntup
sudo lsof -i :80
```

## 7. ¿Qué vecinos tengo en la red local?

```bash
ip neigh
```

Es útil para diagnosticar ARP/ND.

## 8. ¿Cómo pruebo DNS?

```bash
host example.com
dig example.com
dig @192.168.1.10 example.com
dig example.com A
dig example.com AAAA
dig example.com MX
dig -x 192.168.1.10
```

## 9. ¿Cómo pruebo un puerto TCP?

```bash
nc -vz 192.168.1.10 22
nc -vz 192.168.1.10 80
```

Si no está instalado:

```bash
sudo apt install netcat-openbsd
```

## 10. ¿Cómo veo el camino hasta un destino?

```bash
tracepath 8.8.8.8
```

Alternativa:

```bash
sudo apt install traceroute
traceroute 8.8.8.8
```

## 11. ¿Cómo consulto y aplico Netplan?

```bash
sudo netplan get
sudo ls -l /etc/netplan/
sudo sed -n '1,240p' /etc/netplan/*.yaml
sudo netplan generate
sudo netplan apply
```

Para cambios delicados, especialmente por SSH:

```bash
sudo netplan try
```

> `netplan try` permite confirmar el cambio y recuperar la configuración anterior si no lo confirmas.

## 12. ¿Qué gestor de red está activo?

En Ubuntu Server es habitual encontrar `systemd-networkd` junto con Netplan:

```bash
systemctl status systemd-networkd
networkctl status
```

Si utiliza NetworkManager:

```bash
systemctl status NetworkManager
nmcli device status
nmcli connection show
```

Comprueba primero qué renderer utiliza Netplan.

## 13. ¿Cómo reinicio una interfaz?

```bash
sudo ip link set ens33 down
sudo ip link set ens33 up
```

Para cambios permanentes, modifica Netplan y valida/aplica la configuración. Los comandos históricos `ifup`/`ifdown` pueden aparecer en documentación antigua, pero no son la vía principal en un Ubuntu Server moderno basado en Netplan.

## 14. ¿Cómo compruebo un servicio?

```bash
systemctl status NOMBRE_SERVICIO
systemctl is-active NOMBRE_SERVICIO
systemctl is-enabled NOMBRE_SERVICIO
```

## 15. ¿Dónde miro los errores?

```bash
journalctl -u NOMBRE_SERVICIO -n 50 --no-pager
journalctl -u NOMBRE_SERVICIO -f
```

## 16. Diagnóstico rápido

```text
1. ¿La interfaz está UP?
        ↓
2. ¿Tiene la IP/prefijo esperado?
        ↓
3. ¿Existe una ruta por defecto?
        ↓
4. ¿Responde la puerta de enlace?
        ↓
5. ¿Hay conectividad por IP?
        ↓
6. ¿Funciona DNS?
        ↓
7. ¿El servicio escucha en el puerto esperado?
        ↓
8. ¿El firewall permite el tráfico?
        ↓
9. ¿Qué dicen los registros?
```

### Regla de oro

**No cambies cinco cosas a la vez.**

> **observar → formular hipótesis → cambiar una cosa → probar → documentar**

## Procedencia

Esta chuleta recupera y reorganiza la sección **«Comandos de red en Ubuntu»** del material `Preparación del entorno` del CIFP Juan de Colonia. Se han mantenido los comandos útiles y se han actualizado las recomendaciones que podían inducir a utilizar procedimientos antiguos como vía principal.

## Fuentes técnicas

- Ubuntu 26.04 LTS: https://documentation.ubuntu.com/release-notes/26.04/
- Netplan: https://netplan.io/
- systemd-networkd: https://www.freedesktop.org/software/systemd/man/latest/systemd-networkd.service.html
- iproute2: https://www.kernel.org/pub/linux/utils/net/iproute2/
