# algo_rem_mem_2025_parcial_3
## santiago acevedo urrego
Implementación de los algoritmos de reemplazo de páginas

Realice fork de este repositorio. Invite al docente fcardonaEAFIT (fcardona@eafit.edu.co).

Parcial.

 * I, III -> Algoritmo FIFO
 * II, IV -> Algoritmo LRU

Abra el archivo `sim_algo_reem_mem.py` implemente la función `procesar`. Esta recibe tres argumentos:

  * `segmentos` es una lista de  tripletas. Ej: `('.text', 0x00, 0x1A)`. Primero el nombre del segmento,
    el segundo la dirección `base` y la tercera el `limite`.
  * `reqs` un lista de requerimientos. Ej: `[0x00, 0x10, 0x20]`.
  * `marcos libres` Una lista de los números de marcos libres.

La función retornar una tripleta:

  * `Req`, el valor del requeriento.
  * `Dirección Física` La dirección fisica donde el requerimiento direccionara.
  * `Acción`: Puede ser uno de estos mensajes.
    * "Marco libre asignado" -> Un marco libre es asignado
    * "Marco ya estaba asigando" -> El valor esta ubicado en memoria y la referencia ya existe
    * "Marco asignado" -> Un marco es quitado y se asigna uno nuevo.
    * "Segmentation Fault" -> Una referencia de memoria invalida. La dirección de retorno debe ser 0x1ff

Con el siguiente ejemplo:

```python
marcos_libres = [0x0,0x1,0x2]
reqs = [ 0x00, 0x12, 0x64, 0x65, 0x8D, 0x8F, 0x19, 0x18, 0xF1, 0x0B, 0xDF, 0x0A ]
segmentos =[ ('.text', 0x00, 0x1A),
             ('.data', 0x40, 0x28),
             ('.heap', 0x80, 0x1F),
             ('.stack', 0xC0, 0x22)] 
```

Se obtiene la siguiente salida:

```shell
Req: 0x00 Direccion Fisica: 0x20 Acción: Marco libre asignado
Req: 0x12 Direccion Fisica: 0x12 Acción: Marco libre asignado.
Req: 0x64 Direccion Fisica: 0x04 Acción: Marco libre asignado
Req: 0x65 Direccion Fisica: 0x05 Acción: Marco ya estaba asignado
Req: 0x8d Direccion Fisica: 0x2d Acción: Marco asignado
Req: 0x8f Direccion Fisica: 0x2f Acción: Marco ya estaba asignado
Req: 0x19 Direccion Fisica: 0x19 Acción: Marco ya estaba asignado
Req: 0x18 Direccion Fisica: 0x18 Acción: Marco ya estaba asignado
Req: 0xf1 Direccion Fisica: 0x1ff Acción: Segmention Fault
```

## Autor.

 * Nombre completo: Santiago Acevedo Urrego
