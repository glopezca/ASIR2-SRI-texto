# 🐙 ANEXO III · Git, GitHub, Codespaces y Visual Studio Code

> **Material docente integral · CFGS ASIR**

## 1. 🎯 Objetivos

- comprender Git como control de versiones distribuido;
- diferenciar working tree, staging, commit, rama y remoto;
- crear y mantener `ASIR2-SRI-texto`;
- utilizar GitHub Web, GitHub Desktop, Git CLI y GitHub CLI;
- trabajar con Codespaces desde navegador y VS Code;
- ejecutar y documentar el laboratorio desde el repositorio.

## 2. 🧠 Modelo mental

```text
GitHub remoto
     ▲
     │ push / pull
     ▼
Repositorio local
     │
     ├── working tree
     ├── staging area
     └── commits
```

## 3. 🆕 Crear el repositorio

Nombre del proyecto:

```text
ASIR2-SRI-texto
```

El repositorio ya está organizado como producto docente. Por eso no se incluye un capítulo artificial sobre «cómo estructurar el repositorio».

## 4. 🔧 Configurar Git

```bash
git config --global user.name "Nombre Apellidos"
git config --global user.email "correo@example.com"
git config --global init.defaultBranch main
```

Comprobar:

```bash
git config --global --list
git --version
```

## 5. 📥 Clonar

```bash
git clone https://github.com/USUARIO/ASIR2-SRI-texto.git
cd ASIR2-SRI-texto
git status
git remote -v
```

## 6. 🔄 Flujo normal

```text
git pull
   ↓
editar
   ↓
git diff
   ↓
git add
   ↓
git diff --staged
   ↓
git commit
   ↓
git push
```

Revisar siempre el diff antes del commit.

## 7. 🌿 Ramas

```bash
git switch -c mejora-ut5
git status
git push -u origin mejora-ut5
```

Volver:

```bash
git switch main
```

## 8. 🔍 Historial

```bash
git log --oneline --decorate --graph --all
git show HEAD
git diff main..mejora-ut5
```

## 9. 🖥️ GitHub Web

Para pequeños cambios puede utilizarse la interfaz web: editar, previsualizar, confirmar y crear un Pull Request. Para trabajos extensos es preferible un entorno de desarrollo completo.

## 10. 🖱️ GitHub Desktop

Flujo visual:

```text
Clone → Edit → Changes → Commit → Push
```

Es útil durante la introducción porque permite observar claramente qué ficheros cambian.

## 11. ⌨️ GitHub CLI

```bash
gh auth login
gh repo list
gh repo clone USUARIO/ASIR2-SRI-texto
gh codespace list
```

## 12. ☁️ Codespaces

Un Codespace proporciona un entorno de desarrollo conectado al repositorio. Puede abrirse en navegador o desde VS Code de escritorio mediante la extensión correspondiente.

```text
GitHub
  ↓
Codespace
  ↓
Linux + herramientas
  ↓
VS Code
  ↓
Terminal
  ↓
Git / Docker / pruebas
```

## 13. 🧩 Codespaces + VS Code

En VS Code instala la extensión **GitHub Codespaces**, autentícate y utiliza la paleta de comandos para conectarte a un Codespace.

La ventana debe conservar la misma ergonomía del Anexo I:

```text
┌──────────────┬───────────────────────────────┐
│ 📁 Explorer  │ 📝 Editor                     │
├──────────────┴───────────────────────────────┤
│ 🐧 Terminal del Codespace                    │
└──────────────────────────────────────────────┘
```

## 14. 🐳 Docker en Codespaces

Comprobar antes de usar Compose:

```bash
docker version
docker compose version
docker compose config
```

La capacidad de ejecutar Docker depende de la configuración del Codespace. Si el entorno no proporciona un daemon utilizable, no debe presentarse como equivalente a Docker Desktop local.

## 15. 🔐 Secretos

No guardes tokens, contraseñas ni claves en Git. Utiliza secretos del entorno y variables documentadas mediante ejemplos sin valores reales.

## 16. 🧪 Práctica de 75 minutos

1. Crear/clonar el repositorio.
2. Crear una rama.
3. Modificar una UT.
4. Revisar `git diff`.
5. Commit y push.
6. Abrir un Codespace.
7. Conectar desde VS Code.
8. Ejecutar `git status` y `git log`.
9. Realizar un segundo commit.
10. Documentar el flujo.

## 17. 📚 Documentación oficial

- https://docs.github.com/en/get-started/using-git
- https://docs.github.com/en/get-started/git-basics/set-up-git
- https://docs.github.com/en/get-started/start-your-journey/creating-a-repository-for-your-project-on-github
- https://cli.github.com/manual/
- https://docs.github.com/en/codespaces
- https://docs.github.com/en/codespaces/developing-in-a-codespace/using-github-codespaces-in-visual-studio-code
