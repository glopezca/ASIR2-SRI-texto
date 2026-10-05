# Anexo XVIII · Chuleta de comandos de red en Ubuntu

> **Objetivo:** tener en un solo sitio los comandos que más vas a utilizar para **observar, comprobar y diagnosticar** una red en Ubuntu Server.

> **Idea clave:** primero observa; después formula una hipótesis; cambia una sola cosa; vuelve a probar.

## 1. Ver interfaces, direcciones y estado

| Necesito saber… | Comando |
|---|---|
| Direcciones y configuración | `ip addr` |
| Una interfaz concreta | `ip addr show enp0s3` |
| Estado de las interfaces | `ip link show` |
| Estadísticas de una interfaz | `ip -s link show enp0s3` |
| Vecinos de la red local (ARP/ND) | `ip neigh` |

También puedes encontrar `ifconfig` en material antiguo, pero en Ubuntu actual la herramienta principal es `ip`.

## 2. Ver las rutas

```bash
ip route
ip route get 8.8.8.8
ip route | grep default
```

- `ip route`: muestra la tabla de rutas.
- `ip route get DESTINO`: indica qué ruta utilizaría el sistema para llegar a ese destino.

## 3. Comprobar conectividad

Empieza por un destino cercano y avanza hacia fuera:

```bash
ping -c 4 192.168.1.1
ping -c 4 8.8.8.8
ping -c 4 example.com
```

Si responde la IP pero no el nombre de dominio, la conectividad IP funciona y debes investigar **DNS**.

## 4. Comprobar DNS

```bash
resolvectl status
resolvectl dns
resolvectl query example.com
```

Consultas DNS:

```bash
host example.com
nslookup example.com
dig example.com
dig @192.168.1.10 example.com
dig example.com A
dig example.com AAAA
dig example.com MX
dig -x 192.168.1.10
```

Servicio de resolución local:

```bash
systemctl status systemd-resolved
```

> En Ubuntu moderno, no edites `/etc/resolv.conf` a ciegas: comprueba antes quién gestiona la resolución.

## 5. Ver qué servicios están escuchando

La herramienta principal es `ss`:

```bash
ss -lntup
ss -lntup | grep ':22'
ss -lntup | grep ':53'
ss -lntup | grep ':80'
```

- `-l` → sockets en escucha.
- `-n` → no resolver nombres.
- `-t` → TCP.
- `-u` → UDP.
- `-p` → proceso asociado, cuando se dispone de permisos.

Para localizar un proceso concreto:

```bash
sudo lsof -i :80
```

También puede aparecer `netstat` en documentación antigua:

```bash
sudo netstat -plnt
sudo netstat -tuln
```

Si necesitas `netstat`:

```bash
sudo apt update
sudo apt install net-tools
```

## 6. Probar un puerto TCP

```bash
nc -vz 192.168.1.10 22
nc -vz 192.168.1.10 80
```

Si `nc` no está instalado:

```bash
sudo apt install netcat-openbsd
```

## 7. Ver el camino hasta un destino

```bash
tracepath 8.8.8.8
```

Alternativa:

```bash
sudo apt install traceroute
traceroute 8.8.8.8
```

## 8. Configurar y comprobar Netplan

Los archivos están en:

```bash
/etc/netplan/
```

Consultar:

```bash
sudo ls -l /etc/netplan/
sudo netplan get
sudo sed -n '1,240p' /etc/netplan/*.yaml
```

Ejemplo:

```yaml
network:
  version: 2
  ethernets:
    enp0s3:
      dhcp4: false
      addresses:
        - 192.168.1.10/24
      routes:
        - to: default
          via: 192.168.1.1
      nameservers:
        addresses:
          - 8.8.8.8
          - 8.8.4.4
```

Comprobar y aplicar:

```bash
sudo netplan generate
sudo netplan try
sudo netplan apply
```

> Si estás conectado por SSH, `netplan try` es especialmente útil porque permite comprobar el cambio antes de dejarlo aplicado de forma permanente.

## 9. Gestionar interfaces

```bash
sudo ip link set enp0s3 down
sudo ip link set enp0s3 up
```

Los comandos `ifdown`/`ifup` pueden aparecer en documentación antigua:

```bash
sudo ifdown enp0s3 && sudo ifup enp0s3
```

En Ubuntu Server moderno con Netplan, no deben ser la primera opción.

## 10. ¿Qué componente gestiona la red?

```bash
systemctl status systemd-networkd
networkctl status
```

Si el sistema utiliza NetworkManager:

```bash
systemctl status NetworkManager
nmcli device status
nmcli connection show
```

## 11. Gestionar servicios con systemd y systemctl

`systemctl` **no es una TUI**: es la interfaz CLI principal para consultar y administrar unidades de `systemd`. Por ello se mantiene en esta chuleta de comandos y no en el Anexo XXI.

### Estado de un servicio

```bash
systemctl status NOMBRE_SERVICIO
systemctl is-active NOMBRE_SERVICIO
systemctl is-enabled NOMBRE_SERVICIO
```

Ejemplos del laboratorio:

```bash
systemctl status ssh
systemctl status bind9
systemctl status nginx
```

### Arrancar, detener y reiniciar

```bash
sudo systemctl start NOMBRE_SERVICIO
sudo systemctl stop NOMBRE_SERVICIO
sudo systemctl restart NOMBRE_SERVICIO
sudo systemctl reload NOMBRE_SERVICIO
```

- `start`: inicia ahora.
- `stop`: detiene ahora.
- `restart`: detiene y vuelve a iniciar.
- `reload`: pide al servicio que recargue su configuración sin reiniciar el proceso, **si el servicio soporta esta operación**.

### Arranque automático

```bash
sudo systemctl enable NOMBRE_SERVICIO
sudo systemctl disable NOMBRE_SERVICIO
```

Consultar unidades instaladas:

```bash
sudo systemctl list-unit-files --type=service --all
```

### Diagnóstico: systemctl + journalctl

```bash
systemctl status NOMBRE_SERVICIO --no-pager
sudo journalctl -u NOMBRE_SERVICIO -n 50 --no-pager
sudo journalctl -u NOMBRE_SERVICIO -f
```

La secuencia recomendada es:

```text
¿Está activo?      → systemctl is-active
        ↓
¿Está habilitado?  → systemctl is-enabled
        ↓
¿Qué estado tiene? → systemctl status
        ↓
¿Qué ha ocurrido?  → journalctl -u
        ↓
¿Escucha?          → ss -lntup
        ↓
¿Funciona?         → prueba desde cliente
```

### NetworkManager

Si el sistema utiliza NetworkManager:

```bash
systemctl status NetworkManager
nmcli device status
nmcli connection show
```

> **Pro tip:** `systemctl` responde a «¿qué está haciendo systemd con este servicio?»; una TUI como `btop` responde a «¿qué está haciendo el sistema/proceso?». Son herramientas complementarias, no equivalentes.

## 12. Comprobar el firewall UFW

```bash
sudo ufw status
sudo ufw enable
sudo ufw disable
sudo ufw allow 22/tcp
sudo ufw deny 22/tcp
```

> Antes de activar un firewall remoto, asegúrate de haber permitido el acceso que necesitas, por ejemplo SSH.

## 13. Escanear puertos con Nmap

```bash
nmap localhost
nmap -p- localhost
nmap -sV localhost
sudo nmap -A localhost
nmap -p 80,443 localhost
nmap -p 20-80 localhost
nmap --script=banner localhost
```

Si no está instalado:

```bash
sudo apt update
sudo apt install nmap
```

> Utiliza Nmap sobre sistemas y redes donde tengas autorización para realizar el escaneo.

## 14. Consultar registros

```bash
sudo journalctl -u NOMBRE_SERVICIO -n 50 --no-pager
sudo journalctl -u NOMBRE_SERVICIO -f
```

Si el sistema dispone de `syslog`:

```bash
sudo tail -f /var/log/syslog
```

## 15. Herramientas que pueden faltar

```bash
sudo apt update
sudo apt install net-tools iproute2 traceroute dnsutils netcat-openbsd nmap
```

No necesitas instalar `iproute2` en una instalación normal de Ubuntu: `ip` forma parte del sistema base. La línea anterior sirve como referencia cuando se prepara un entorno mínimo.

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

Esta chuleta integra y sintetiza la sección **«Comandos de red en Ubuntu»** del libro **Preparación del entorno** del CIFP Juan de Colonia, junto con la chuleta ya incorporada al repositorio.

Se han recuperado los apartados que faltaban o estaban menos representados: `ifconfig`/`ifup`/`ifdown` como referencia histórica, `systemctl`, `ping`, `traceroute`, `nslookup`, `netstat`, `ufw`, instalación de herramientas, `nmap` y consulta de registros.

El resultado no reproduce literalmente el libro: organiza sus contenidos por **pregunta o problema que el alumno quiere resolver**, para facilitar su uso durante las prácticas.

---

## 18. 🆕 v6.5.6 · Comandos incorporados al laboratorio

### Netplan

```bash
sudo netplan generate
sudo netplan try
sudo netplan apply
sudo netplan get
```

### sysctl

```bash
sysctl net.ipv4.ip_forward
sudo sysctl --system
sudo sysctl -w net.ipv4.ip_forward=1
```

### nftables

```bash
sudo nft list ruleset
sudo nft -c -f /etc/nftables.conf
sudo nft -f /etc/nftables.conf
sudo nft list table inet filter
sudo nft list table ip nat
sudo systemctl enable nftables
sudo systemctl restart nftables
```

**Ruta persistente:** `/etc/nftables.conf`.

### DHCP / Kea

```bash
python3 -m json.tool /etc/kea/kea-dhcp4.conf >/dev/null
sudo systemctl status kea-dhcp4-server
sudo journalctl -u kea-dhcp4-server -b --no-pager
sudo ss -lunp | grep ':67'
```

### DNS / BIND9

```bash
sudo named-checkconf
sudo named-checkzone tierramedia.jc /etc/bind/db.tierramedia.jc
sudo rndc reload
```

### Web

```bash
sudo apache2ctl configtest
sudo nginx -t
```

### SSH / transferencia

```bash
sudo sshd -t
sftp usuario@192.168.20.192
scp fichero usuario@192.168.20.192:/ruta/
```

### Correo

```bash
sudo postfix check
sudo dovecot -n
```

### Mensajería

```bash
sudo prosodyctl check config
```

### Multimedia

```bash
xmllint --noout /etc/icecast2/icecast.xml
ffprobe fichero.mp4
```

> **Regla:** validar → aplicar/recargar → comprobar → persistir. Nunca confundir la configuración escrita en disco con el estado activo del kernel o del daemon.
