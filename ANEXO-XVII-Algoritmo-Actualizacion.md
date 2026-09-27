# 🔄 ANEXO XVII · Algoritmo de actualización y publicación

## 1. Principio

Cada release debe mejorar **contenido, pedagogía, técnica, laboratorio, evaluación, recursos y trazabilidad** sin degradar lo ya validado.

El proceso distingue tres capas:

```text
FUENTE → DECISIÓN → CAMBIO → PRUEBA → PUBLICACIÓN
```

El actualizador automático se limita a metadatos y controles estructurales. Nunca sustituye una directiva técnica, una versión de software o una arquitectura mediante búsqueda y reemplazo ciego.

## 2. Entrada de una iteración

1. Clonar o ramificar la versión estable.
2. Ejecutar `--check` antes de editar.
3. Registrar cambios propuestos.
4. Auditar fuentes nuevas y materiales aportados.
5. Clasificar cada dato: **vigente / correcto pero contextual / histórico / incorrecto / no verificable**.
6. Solo después diseñar el cambio técnico o pedagógico.

## 3. Regla de validación de fuentes

Una afirmación entra en el material principal cuando existe:

- fuente primaria vigente;
- contexto de versión/entorno;
- práctica o ejemplo reproducible cuando sea una receta;
- coherencia con el resto del módulo.

La antigüedad de una fuente no basta para descartarla, pero una receta antigua tampoco basta para conservarla.

## 4. Regla de preparación común

Cada UT debe tener **exactamente un bloque** de `PREPARACIÓN COMÚN DE LAS PRÁCTICAS`.

Ese bloque explica una sola vez el método profesional:

```text
situarse → prerrequisitos → predicción → cambio mínimo
→ validación → prueba cliente → evidencia → diagnóstico → documentación → reversión
```

Cada práctica contiene después una **Pista específica**, adaptada a su objetivo. No se permite clonar el bloque común en cada práctica.

## 5. Arquitectura didáctica obligatoria de una UT

Cada UT debe contener:

1. misión y objetivos observables;
2. puerta de entrada o diagnóstico inicial;
3. mapa conceptual;
4. glosario esencial;
5. conceptos previos y analogías;
6. explicación teórica;
7. ejemplo resuelto;
8. práctica guiada;
9. práctica semiguiada;
10. práctica autónoma;
11. al menos una incidencia o error productivo;
12. diagnóstico sistemático;
13. transferencia profesional;
14. autoevaluación;
15. test de repaso **antes** del solucionario;
16. solucionario razonado;
17. banco de ejercicios propuestos;
18. recursos oficiales y ampliación.

## 6. Calidad de laboratorio

Cada práctica debe permitir registrar:

```text
estado inicial
→ cambio
→ validación
→ prueba desde cliente
→ evidencia
→ diagnóstico
→ reversión
```

Para servicios, se comprueban cuando proceda: configuración, proceso, puerto, firewall, DNS, cliente, logs y tráfico.

## 7. Seguridad y futuro profesional

Cada release debe revisar, como mínimo:

- IPv6;
- TLS y certificados;
- DNSSEC, TSIG y mecanismos de transporte DNS seguros;
- SMTP Submission, IMAP seguro, SPF/DKIM/DMARC;
- HTTP/2 y HTTP/3/QUIC;
- reverse proxy y balanceo;
- contenedores, imágenes, redes, volúmenes y healthchecks;
- Kubernetes: Pod, Deployment, Service, DNS, probes y NetworkPolicy;
- Git, automatización, IaC y trazabilidad de cambios;
- logs, métricas, captura de tráfico y diagnóstico.

Estos temas se incorporan como **puentes profesionales**, no como relleno independiente del objetivo curricular.

## 8. Control de materiales de terceros

Para cada nuevo recurso:

1. registrar autor/proveedor;
2. registrar URL y fecha de consulta;
3. comprobar licencia o condiciones de uso;
4. decidir: enlazar, citar, describir o integrar una adaptación propia;
5. actualizar `NOTICE.md` si es necesario.

## 9. Actualizador automático

Desde la raíz:

```bash
python3 tools/update_material.py --check
python3 tools/update_material.py --dry-run --bump 6.6
python3 tools/update_material.py --bump 6.6
python3 tools/update_material.py --check
python3 tools/update_material.py --package
```

El actualizador debe:

- leer `VERSION`;
- validar coherencia de README, CFF y changelog;
- comprobar estructura didáctica;
- detectar duplicación de preparación común;
- detectar pistas clonadas exactamente;
- validar enlaces internos;
- validar fences de código;
- comprobar que el test está antes del solucionario;
- generar ZIP reproducible con nombre de versión;
- no modificar contenido técnico salvo los metadatos expresamente definidos.

## 10. Quality gate por capas

### Gate A · editorial/estructural

Markdown, enlaces, encabezados, tablas, versiones, atribución y documentos obligatorios.

### Gate B · didáctico

Preparación común única, pistas específicas, glosario, ejercicios, test y solución, evidencia y transferencia.

### Gate C · sintaxis

YAML/JSON/Bash y configuraciones comprobables de forma estática.

### Gate D · ejecución

Cuando el runner disponga de Docker Engine, Kubernetes, VirtualBox/VM o simuladores, ejecutar smoke tests representativos. Nunca se declara una prueba ejecutada si no se ha ejecutado.

## 11. Publicación

1. ejecutar todos los gates;
2. generar `INFORME-PRUEBAS-vX.Y.md`;
3. actualizar `CHANGELOG.md`;
4. actualizar `VERSION` y metadatos;
5. crear ZIP;
6. comprobar el ZIP con `unzip -t`;
7. verificar que el contenido del ZIP coincide con el árbol validado;
8. publicar solo después de revisar el diff.

## 12. Política de rollback

La publicación se puede revertir si:

- falla un test estructural;
- una práctica pierde reproducibilidad;
- una fuente vigente demuestra una incompatibilidad;
- una actualización técnica introduce una regresión.

El changelog debe explicar qué se revirtió y por qué.
