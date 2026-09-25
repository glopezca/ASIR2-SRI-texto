# ✅ ANEXO X · Garantía de calidad y pruebas del material

## 1. Objetivo

Este anexo define una puerta de calidad que debe superar el repositorio antes de considerarse publicable.

## 2. Pruebas estructurales

- existen las ocho UT;
- cada UT declara su RA cuando corresponde;
- cada UT menciona los cuatro entornos;
- existe autoevaluación y test;
- el solucionario aparece después del test;
- las prácticas incluyen guía y rúbrica;
- README enlaza a los documentos existentes.

## 3. Pruebas de Markdown

- bloques de código equilibrados;
- ausencia de `:::` y artefactos internos de citación;
- enlaces locales resolubles;
- tablas con cabeceras y filas coherentes cuando se puedan validar automáticamente.

## 4. Pruebas de código

- `bash -n` para bloques Bash independientes y sin marcadores de sustitución;
- parseo de JSON y YAML;
- validaciones específicas de configuración cuando el software esté disponible.

## 5. Pruebas pedagógicas

Cada UT debe ofrecer: situación de partida, concepto previo antes del salto técnico, ejemplo resuelto, práctica guiada, diagnóstico, transferencia y evaluación.

## 6. Pruebas experimentales

Cuando se disponga de Docker Engine, máquinas Ubuntu o Packet Tracer se ejecutarán las pruebas funcionales. Si un entorno de ejecución no está disponible, el informe debe distinguir claramente **validación estática** de **ejecución experimental**. Nunca se marcará una práctica como ejecutada si no se ha ejecutado.

## 7. Ejecución local

```bash
python3 tests/validate_material.py
```

El script devuelve código `0` cuando supera todos los controles automáticos.
