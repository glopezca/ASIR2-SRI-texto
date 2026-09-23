# 🖥️ ANEXO VI · Webmin: administración gráfica de servidores Linux

## 1. 🎯 Objetivos

Al terminar este anexo podrás:

- explicar qué es Webmin y qué problema resuelve;
- instalarlo en Ubuntu Server;
- acceder de forma segura a su interfaz web;
- comprender el concepto de módulo;
- administrar servicios mediante CLI y mediante Webmin;
- identificar qué configuración real modifica Webmin;
- validar por CLI cualquier cambio realizado desde la interfaz;
- realizar copias de seguridad antes de cambios importantes;
- distinguir Webmin de las interfaces propias de aplicaciones como Roundcube o Sympa.

> 🧭 **Idea fundamental**
> 
> Webmin **no sustituye Linux ni los servicios que administra**. Es una capa de administración que lee y modifica la configuración real del sistema y de los servicios mediante módulos. Por eso un administrador ASIR debe saber utilizar Webmin **y** comprender la CLI que existe debajo.

---

## 2. 🧠 Modelo mental

```text
                 ADMINISTRADOR
                       │
              ┌────────┴────────┐
              ▼                 ▼
           CLI Linux          Webmin
              │                 │
              └────────┬────────┘
                       ▼
              Ficheros / systemd
                       │
                       ▼
                    SERVICIO
                       │
                       ▼
                     RED
```

Webmin no crea una arquitectura paralela. En términos generales, proporciona formularios y operaciones que terminan modificando los mismos ficheros y servicios que el administrador podría gestionar manualmente. La documentación oficial destaca precisamente que Webmin trabaja directamente con los ficheros de configuración del sistema.

---

## 3. 📦 Instalación en Ubuntu Server

La documentación oficial recomienda utilizar el script de configuración del repositorio para sistemas Debian/Ubuntu.

```bash
curl -o webmin-setup-repo.sh https://raw.githubusercontent.com/webmin/webmin/master/webmin-setup-repo.sh
sudo sh webmin-setup-repo.sh
sudo apt-get install webmin --install-recommends
```

Comprueba el servicio:

```bash
systemctl status webmin
sudo ss -lntp | grep 10000
```

La interfaz se publica normalmente en:

```text
https://IP_DEL_SERVIDOR:10000
```

> ⚠️ El certificado inicial puede ser autofirmado. En un laboratorio es normal recibir una advertencia del navegador. En producción se debe utilizar un certificado adecuado y restringir el acceso.

---

## 4. 🔐 Seguridad inicial

No conviene dejar Webmin accesible indiscriminadamente.

Buenas prácticas de laboratorio y producción:

1. restringir el acceso por red o firewall;
2. utilizar HTTPS;
3. utilizar cuentas administrativas con los privilegios mínimos necesarios;
4. evitar exponer el puerto 10000 directamente a Internet salvo necesidad justificada;
5. mantener Webmin actualizado;
6. realizar copias de seguridad antes de modificaciones importantes.

Webmin dispone de **IP Access Control** para limitar desde qué direcciones se permite la administración.

---

## 5. 🖥️ Conocer la interfaz

La interfaz organiza las funciones en categorías y módulos. Las categorías pueden variar según los módulos instalados y el sistema operativo.

| Categoría | Ejemplos |
|---|---|
| Webmin | configuración de Webmin, módulos, usuarios Webmin |
| System | usuarios, paquetes, procesos, logs |
| Servers | BIND, Postfix, Dovecot, Nginx, SSH, ProFTPD |
| Networking | configuración de red, servicios de red |
| Tools | terminal, explorador de ficheros y utilidades |

### Terminal integrada

Webmin incluye un módulo **Terminal** que permite ejecutar comandos desde el navegador. Esto resulta especialmente útil para relacionar interfaz gráfica y CLI, pero no debe ocultar al alumnado que las operaciones siguen siendo operaciones Linux.

---

## 6. 🔄 Método de trabajo profesional

La metodología recomendada para cualquier práctica es:

```text
1. Comprender el servicio
        ↓
2. Configurar por CLI
        ↓
3. Validar
        ↓
4. Repetir una parte mediante Webmin
        ↓
5. Observar qué ha cambiado
        ↓
6. Validar otra vez por CLI
        ↓
7. Probar desde un cliente
```

Así se evita el aprendizaje mecánico de botones y se desarrolla la capacidad de administración independiente de una herramienta concreta.

---

## 7. 📡 Módulos relevantes para SRI

| Servicio | Módulo Webmin | Uso didáctico |
|---|---|---|
| BIND9 | **BIND DNS Server** | zonas y registros DNS |
| ISC DHCP | **DHCP Server** | subredes, hosts y concesiones |
| SSH/OpenSSH | **SSH Server** | escucha, autenticación y acceso |
| ProFTPD | **ProFTPD Server** | configuración FTP |
| Nginx | **Nginx Webserver** | server blocks, proxy, SSL |
| Postfix | **Postfix Mail Server** | SMTP y dominios |
| Dovecot | **Dovecot IMAP/POP3 Server** | acceso a buzones |
| Sympa | Sin módulo estándar específico | utilizar WWSympa |
| Kea | Sin módulo estándar específico documentado | CLI/configuración propia |

> 💡 La existencia de un módulo no significa que todas las posibilidades del servicio estén expuestas en la interfaz. Cuando una opción no aparece, la CLI y los ficheros de configuración siguen siendo la referencia.

---

## 8. 🌐 BIND DNS Server

La interfaz de BIND permite administrar zonas y registros y aplicar cambios. Después de cualquier modificación, valida desde CLI:

```bash
sudo named-checkconf
sudo named-checkzone ejemplo.test /ruta/a/zona
dig @127.0.0.1 ejemplo.test SOA
```

La documentación oficial advierte además que el módulo modifica directamente los ficheros de configuración. Esto es importante cuando existen otros sistemas que actualizan dinámicamente las zonas.

---

## 9. 📡 DHCP Server

El módulo **DHCP Server** está orientado al servidor DHCP de ISC. Permite administrar subredes, hosts, grupos y concesiones.

En este material la implementación principal es **Kea**, por lo que no debe asumirse que el módulo DHCP de Webmin administra automáticamente la configuración de Kea.

---

## 10. 🔐 SSH Server

El módulo permite revisar opciones de autenticación, acceso, direcciones y puertos de escucha y otras opciones del servidor SSH.

Después de modificarlo:

```bash
sudo sshd -t
sudo systemctl reload ssh
sudo ss -lntp | grep ':22'
```

Nunca cierres tu única sesión SSH antes de comprobar que la nueva configuración es válida.

---

## 11. 📂 ProFTPD Server

El módulo de ProFTPD permite gestionar configuración global, servidores virtuales, acceso anónimo y opciones por directorio.

En esta unidad se utiliza principalmente como contraste con SFTP. El hecho de que Webmin permita configurar FTP no convierte FTP en equivalente a SFTP.

---

## 12. 🌍 Nginx Webserver

El módulo permite administrar:

- configuración global;
- *server blocks*;
- `location`;
- logs;
- SSL;
- FastCGI;
- proxy inverso;
- compresión;
- control de acceso.

La validación final debe realizarse con:

```bash
sudo nginx -t
sudo systemctl reload nginx
curl -I http://servidor/
```

---

## 13. ✉️ Postfix y Dovecot

Webmin dispone de módulos para ambos servicios.

| Servicio | Configuración que interesa relacionar | Comprobación CLI |
|---|---|---|
| Postfix | dominios, relay, opciones SMTP | `postconf -n`, `postfix check` |
| Dovecot | IMAP/POP3, autenticación | `doveconf -n`, `ss -lntp` |

La administración de Webmin debe acompañarse de pruebas reales con SMTP, IMAP y POP3.

---

## 14. 💬 Sympa: por qué no usar Webmin

Sympa dispone de su propia aplicación web de administración, **WWSympa**, que es la interfaz adecuada para propietarios, moderadores y listmasters. La documentación oficial de Sympa describe la creación y administración de listas tanto desde línea de comandos como desde la interfaz web.

Por tanto, la comparación correcta es:

```text
Administración del servicio
        │
        ├── CLI + ficheros de Sympa
        │
        └── WWSympa
               ├── listas
               ├── miembros
               ├── moderación
               └── administración
```

---

## 15. 🧰 Webmin como herramienta de diagnóstico

Webmin no sustituye herramientas como `ss`, `journalctl`, `dig`, `curl`, `openssl`, `tcpdump` o los comandos propios de cada servicio.

Sí puede ayudar a localizar problemas mediante:

- estado del servicio;
- logs;
- terminal;
- configuración del módulo;
- procesos;
- usuarios;
- paquetes;
- firewall.

La evidencia técnica definitiva sigue siendo la observación del servicio real y las pruebas desde un cliente.

---

## 16. 💾 Copias de seguridad antes de modificar

Antes de una práctica importante, conserva una copia de la configuración. Webmin incluye funciones de copia de configuraciones y también puede hacerse desde CLI.

Ejemplo genérico:

```bash
sudo cp -a /etc/postfix /etc/postfix.bak
sudo cp -a /etc/dovecot /etc/dovecot.bak
```

No uses una copia indiscriminada como sustituto de un procedimiento de recuperación probado.

---

## 17. 📊 CLI frente a Webmin

| Criterio | CLI | Webmin |
|---|---|---|
| Automatización | Excelente | Limitada según módulo |
| Comprensión de configuración | Alta | Media |
| Descubrimiento inicial | Menor | Alto |
| Repetibilidad | Excelente con scripts | Depende del procedimiento |
| Diagnóstico fino | Excelente | Complementario |
| Acceso remoto | SSH | HTTPS |
| Dependencia de interfaz | Ninguna | Sí |
| Competencia profesional ASIR | Fundamental | Complementaria |

**Conclusión:** Webmin es una herramienta didáctica y administrativa útil, pero el dominio de la CLI continúa siendo una competencia esencial.

---

## 18. 📝 Práctica integradora · CLI + Webmin

Configura un servicio de laboratorio mediante CLI y después repite una parte mediante Webmin.

Debes entregar:

1. configuración realizada por CLI;
2. capturas de las pantallas relevantes de Webmin;
3. comparación entre ambos métodos;
4. comprobación mediante comandos;
5. prueba desde un cliente;
6. breve conclusión sobre ventajas y limitaciones.

Duración recomendada: **60–90 minutos**.

---

## 19. 📚 Documentación oficial

- Webmin: https://webmin.com/docs/
- Instalación: https://webmin.com/download/
- Introducción: https://webmin.com/docs/intro/
- Webmin CLI: https://webmin.com/docs/reference/webmin-command-line/
- BIND DNS Server: https://webmin.com/docs/modules/bind-dns-server/
- DHCP Server: https://webmin.com/docs/modules/dhcp-server/
- SSH Server: https://webmin.com/docs/modules/ssh-server/
- ProFTPD Server: https://webmin.com/docs/modules/proftpd-server/
- Nginx Webserver: https://webmin.com/docs/modules/nginx-webserver/
- Postfix Mail Server: https://webmin.com/docs/modules/postfix-mail-server/
- Dovecot IMAP/POP3 Server: https://webmin.com/docs/modules/dovecot-imap-pop3-server/
- Sympa: https://www.sympa.community/docs
- Sympa · creación de listas: https://www.sympa.community/manual/admin/list-creation.html
- Sympa · interfaz de listmaster: https://www.sympa.community/manual/admin/web-interface.html
- Roundcube · instalación: https://github.com/roundcube/roundcubemail/wiki/Installation
- Thunderbird · configuración manual: https://support.mozilla.org/en-US/kb/manual-account-configuration
