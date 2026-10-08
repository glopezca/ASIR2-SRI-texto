# Informe de pruebas · v6.5.8e

## 1. Revisión de sintaxis nftables

Se ha realizado una revisión dirigida de todos los fragmentos `nftables` presentes en el material actual. Los fragmentos se concentran en UT1.

### Cadenas base

La forma adoptada es:

```nft
chain input {
    type filter hook input priority 0; policy drop;
}
```

y análogamente para `forward`, `output` y `postrouting`.

Esta forma es sintácticamente válida para `nftables` y, además, evita el problema observado en Webmin cuando `policy ...;` aparece como una línea independiente dentro de la cadena.

### NAT

Se conserva:

```nft
chain postrouting {
    type nat hook postrouting priority srcnat; policy accept;
}
```

y la regla `masquerade` permanece separada como regla de la cadena.

### Comando de creación de una cadena

Se conserva la forma shell:

```bash
sudo nft add chain inet prueba input '{ type filter hook input priority 0; policy accept; }'
```

Las comillas simples son necesarias aquí para impedir que la shell trate las llaves y los `;` como sintaxis propia.

## 2. Validaciones automáticas del repositorio

- Búsqueda de `policy drop;` / `policy accept;` en línea independiente: **0 casos en los fragmentos actuales de nftables**.
- Búsqueda de pares `type filter hook ...` + `policy ...` separados por salto de línea: **0 casos**.
- Búsqueda de identificadores internos de citación: **0 casos**.
- Comprobación de enlaces Markdown internos: se debe mantener el mismo resultado de la edición anterior, sin introducir referencias al antiguo nombre de arquitectura.

## 3. Validación funcional recomendada en el laboratorio

En Ubuntu Server, antes de aplicar la configuración:

```bash
sudo nft -c -f /etc/nftables.conf
```

Después:

```bash
sudo nft -f /etc/nftables.conf
sudo nft list ruleset
```

Desde Webmin, tras guardar/aplicar cambios, volver a comprobar:

```bash
sudo nft list ruleset
```

La CLI es la referencia para confirmar qué configuración ha quedado realmente activa.
