# CHANGELOG · ASIR2-SRI-texto · v6.6.3

## Simulador de redes

El Entorno I deja de identificarse con un producto y pasa a llamarse **Simulador de redes** en las unidades, los anexos, el README y los índices. Donde se describe la herramienta se dan las opciones, por orden, con sus posibilidades y enlaces:

1. **Netfix** (antes *netsim*): web, libre y sin instalación — [Netfix Lab](https://raw.githack.com/glopezca/netfix/main/demo/netfix-lab.html) · [repositorio](https://github.com/glopezca/netfix).
2. **Cisco Packet Tracer**: [página oficial](https://www.netacad.com/cisco-packet-tracer).
3. **GNS3**: [gns3.com](https://www.gns3.com/) · [documentación](https://docs.gns3.com/) · [GitHub](https://github.com/GNS3).
4. **Boson NetSim**: [página oficial](https://boson.com/netsim-cisco-network-simulator/).

- **Comparativa** (tipo, licencia, posibilidades y enlaces) en UT1 §6, en el README y en el Anexo XXII, con un criterio común para redactar las prácticas con equipos genéricos (router, switch, PC, Server).
- **Anexo XXII** renombrado a [`ANEXO-XXII-Simulador-de-redes.md`](ANEXO-XXII-Simulador-de-redes.md). El nombre anterior se conserva como página de redirección. Límites de Netfix actualizados: NAT, Apache2 en `/etc/apache2`, Internet emulada y DNS públicos.
- **Anexo XIX §3**, **bibliografía**, **glosario** («Simulador de redes», «Netfix») e **índice alfabético** actualizados.
- Los nombres de equipo propios de Packet Tracer (`Server-PT`, `Router-PT`, `Cloud-PT`) pasan a genéricos (`Server`, `Router`, `Cloud`). En los diagramas de texto se usa «Sim. de redes» para conservar la alineación.
- La imagen de la topología pasa a `img/topologia-tierramedia-simulador.png`.

## Enlaces

- `github.com/glopezca/netsim` → `github.com/glopezca/netfix`; demo `netsim-dhcp-lab.html` → `netfix-lab.html`.
- En los CHANGELOG e informes de versiones anteriores solo se actualizan los enlaces y los nombres de archivo; su texto se conserva como registro histórico.

## Metadatos

- Versión 6.6.3 en `VERSION`, `CITATION.cff` y README.
