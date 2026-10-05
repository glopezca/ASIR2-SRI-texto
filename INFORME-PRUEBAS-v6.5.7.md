# Informe de pruebas · v6.5.7

## Comprobaciones estáticas realizadas

- [x] VERSION = `6.5.7`.
- [x] Anexo XIX activo renombrado a v6.5.7.
- [x] Referencias activas al Anexo XIX actualizadas.
- [x] Punto 27 de UT1 parte del ecosistema Tierra Media y de las cinco VMs de VirtualBox.
- [x] Punto 28 de UT1 relaciona nftables con la topología y el recorrido de paquetes de Tierra Media.
- [x] Se mantienen `/etc/nftables.conf`, `nft -c -f`, carga, systemd y Webmin.
- [x] No se afirma ejecución real de las prácticas; la validación de Packet Tracer/VirtualBox debe realizarse en el laboratorio.

## Validación técnica del paquete

Resultados de esta construcción:

- `python3 tests/validate_material.py` → `PASS: validator.py`.
- Comprobación de enlaces Markdown internos → `MISSING 0`.
- Bloques Markdown balanceados → `0` bloques con número impar de delimitadores.
- Referencias activas a `la denominación anterior` → `0`.
- Referencias activas a Garceta/García/Enamorado/ISBN → `0`.
- Las ocho UT contienen referencia a Webmin.
- Solo existe el Anexo XIX activo en versión v6.5.7.

La ejecución funcional real de Packet Tracer, VirtualBox, Ubuntu y nftables debe realizarse en el laboratorio; este informe no la simula ni la da por realizada.
