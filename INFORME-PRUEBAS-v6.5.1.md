# Informe de pruebas · ASIR2-SRI-texto · v6.5.1

## Resultado

**PASS condicionado a las pruebas de runtime que requieren infraestructura externa.**

Se valida de forma automática: estructura, versión, licencias/atribución, duplicación de preparación común, pistas específicas, enlaces internos, fences de código, orden de test/soluciones y presencia de materiales y recursos didácticos.

Las pruebas que requieren Docker Engine, Kubernetes o máquinas virtuales no se marcan como ejecutadas si el entorno de construcción no dispone de esos runtimes.

## Criterios específicos de v6.5.1

- 8 UT presentes.
- Una única preparación común por UT.
- Pistas específicas no clonadas literalmente en una misma UT.
- Glosario esencial en las 8 UT.
- Banco de ejercicios propuestos en las 8 UT.
- Recursos oficiales de ampliación en las 8 UT.
- Preparación del entorno ubicada en UT1.
- Autoría explícita de Germán López Castro y referencia al repositorio.
- `ANEXO-XVII` describe el algoritmo para iteraciones futuras.
- ZIP final validado con `unzip -t`.

## Comprobaciones concretas

- 8/8 UT: exactamente una preparación común, situada al inicio del bloque de prácticas.
- 144 pistas específicas en total, sin bloques clonados literalmente dentro de una misma UT.
- 33 documentos Markdown convertibles correctamente con Pandoc GFM.
- Bloques Bash estáticos comprobados con `bash -n` sin errores en los bloques ejecutables sin plantillas.
- Recursos gráficos locales presentes y enlaces internos resueltos.
- No aparecen en las UT recetas con `apt-key`, autenticación Dovecot en claro, SMTP cliente por 25 ni `ProxyPass` genérico RTMP.
