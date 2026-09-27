# 📋 ANEXO XII · Plantillas y entregables profesionales

Este anexo convierte las prácticas en documentos reutilizables de operación técnica.

## 1. Ficha de práctica

| Campo | Contenido |
|---|---|
| Servicio | |
| Objetivo | |
| Entorno | I / II / III / IV |
| Estado inicial | |
| Riesgos | |
| Cambio aplicado | |
| Validación de sintaxis | |
| Prueba funcional | |
| Evidencia | |
| Incidencias | |
| Reversión | |
| Resultado | |

## 2. Registro de incidencia

```text
INCIDENCIA:
Síntoma:
Fecha/hora:
Entorno:
Estado inicial demostrado:
Hipótesis 1:
Evidencia:
Hipótesis 2:
Evidencia:
Intervención mínima:
Resultado:
Causa confirmada:
Corrección permanente:
Prueba de regresión:
Reversión disponible:
```

## 3. Registro de cambio

```text
CAMBIO:
Motivo:
Configuración afectada:
Dependencias:
Riesgo:
Ventana de cambio:
Prueba previa:
Cambio realizado:
Prueba posterior:
Plan de reversión:
Resultado:
```

## 4. Checklist de cierre

- [ ] El servicio está activo.
- [ ] La configuración es válida.
- [ ] La prueba desde cliente funciona.
- [ ] Los logs no muestran errores relevantes.
- [ ] La exposición de red coincide con lo previsto.
- [ ] Se ha documentado el cambio.
- [ ] Existe una forma de volver al estado anterior.

## 5. Evidencia de alta calidad

Una captura debe responder **qué demuestra, desde dónde se obtiene y qué resultado esperado confirma**. El comando sin contexto tampoco es suficiente: hay que relacionarlo con la hipótesis o con el criterio de aceptación.
