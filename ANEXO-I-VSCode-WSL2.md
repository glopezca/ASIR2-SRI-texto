# 🧰 ANEXO I · Visual Studio Code + WSL2 para administración de servicios

> **Versión integral v5 · CFGS ASIR**

## 1. 🎯 Objetivos

Aprender a utilizar VS Code como centro de trabajo para configuración, código, documentación y administración Linux:

- Explorador de archivos;
- editor;
- terminal WSL2;
- YAML, JSON, Markdown, Bash y Dockerfile;
- Git;
- validación de configuraciones;
- diagnóstico.


### 📊 Flujo de trabajo recomendado

| Tarea | Explorador | Editor | Terminal WSL2 |
|---|---|---|---|
| Localizar configuración | seleccionar fichero | — | `find`, `ls` |
| Editar | seleccionar fichero | modificar y guardar | — |
| Validar sintaxis | — | revisión visual | ejecutar herramienta de validación |
| Probar servicio | — | consultar configuración | `systemctl`, `curl`, `ss`, `journalctl` |
| Diagnosticar | localizar logs | comparar ficheros | `grep`, `tail`, `tcpdump` |

> 🧭 La ventana dividida no es un fin en sí mismo: permite **ver el fichero, editarlo y comprobar inmediatamente el efecto en el sistema**.

## 2. 🖥️ Modelo de trabajo

```text
┌────────────────────────────────────────────────────────────┐
│ 📁 EXPLORADOR       📝 EDITOR                              │
│                                                            │
│ compose.yaml          nginx.conf                           │
│ Dockerfile            kea-dhcp4.conf                       │
│ config/               named.conf                           │
│                                                            │
├────────────────────────────────────────────────────────────┤
│ 🐧 TERMINAL WSL2                                          │
│ $ docker compose config                                   │
│ $ sudo nginx -t                                           │
│ $ git status                                              │
└────────────────────────────────────────────────────────────┘
```

La interfaz puede ejecutarse en Windows mientras el proyecto y las herramientas Linux trabajan en WSL2.

## 3. 📦 Instalación y primer proyecto

Instala VS Code y la extensión oficial **WSL**. En Ubuntu:

```bash
sudo apt update
sudo apt install git curl wget
mkdir -p ~/sri/laboratorio
cd ~/sri/laboratorio
code .
```

## 4. 🧭 Explorador

Estructura típica:

```text
laboratorio/
├── compose.yaml
├── Dockerfile
├── config/
│   ├── nginx.conf
│   └── app.conf
├── html/
│   └── index.html
└── README.md
```

Mantén una única ubicación de trabajo principal. Para proyectos con mucha E/S, es preferible trabajar en el sistema de archivos de WSL2 en lugar de mantener el proyecto bajo `/mnt/c`.

## 5. ✍️ Editor y atajos

- búsqueda global: `Ctrl+Shift+F`;
- buscar: `Ctrl+F`;
- reemplazar: `Ctrl+H`;
- guardar: `Ctrl+S`;
- terminal integrada: **Ctrl + tecla de acento grave**;
- dividir editor: **Ctrl + \**;
- paleta: `Ctrl+Shift+P`.

> Las combinaciones que contienen una comilla invertida deben escribirse en Markdown de forma que la combinación no aparezca como escape literal.

## 6. 🐧 Terminal WSL2

```bash
pwd
ls -la
ip addr
ip route
ss -lntup
```

La terminal debe estar realmente asociada a WSL2 cuando trabajemos con servicios Linux.

## 7. 🧪 Flujo profesional de configuración

```text
EDITAR → VALIDAR → APLICAR → COMPROBAR → DOCUMENTAR
```

Nginx:

```bash
sudo nginx -t
sudo systemctl reload nginx
systemctl status nginx --no-pager
```

BIND:

```bash
sudo named-checkconf
sudo named-checkzone ejemplo.test /etc/bind/db.ejemplo.test
sudo systemctl reload bind9
```

Kea:

```bash
kea-dhcp4 -t /etc/kea/kea-dhcp4.conf
sudo systemctl restart kea-dhcp4-server
```

Nunca utilices `restart` como primer paso del diagnóstico.

## 8. 📄 YAML y JSON

Compose:

```bash
docker compose config
```

JSON genérico:

```bash
python3 -m json.tool fichero.json
```

La validación genérica no sustituye la validación específica de cada servicio.

## 9. 🧩 Terminales múltiples

Una configuración especialmente útil:

```text
Terminal 1 → logs
Terminal 2 → administración
Terminal 3 → cliente de pruebas
```

Por ejemplo:

```bash
journalctl -fu nginx
```

mientras:

```bash
curl -v http://localhost
```

## 10. 🔐 Seguridad

Nunca almacenes en el repositorio contraseñas, claves privadas, tokens, secretos o credenciales de producción. Utiliza `.gitignore`, ficheros `.example` y mecanismos de secretos.

## 11. 🧪 Práctica de 60 minutos

1. Crear un proyecto WSL2.
2. Abrirlo con `code .`.
3. Crear una página HTML y un `compose.yaml`.
4. Dividir editor y terminal.
5. Levantar Nginx.
6. Modificar la página.
7. Comprobar el cambio con `curl`.
8. Registrar la solución con Git.

## 12. 📚 Documentación oficial

- https://code.visualstudio.com/docs
- https://code.visualstudio.com/docs/remote/wsl
- https://learn.microsoft.com/windows/wsl/
- https://code.visualstudio.com/docs/containers/overview
