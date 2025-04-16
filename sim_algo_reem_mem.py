#!/usr/bin/env python

marcos_libres = [0x0,0x1,0x2]
reqs = [ 0x00, 0x12, 0x64, 0x65, 0x8D, 0x8F, 0x19, 0x18, 0xF1, 0x0B, 0xDF, 0x0A ]
segmentos =[ ('.text', 0x00, 0x1A),
             ('.data', 0x40, 0x28),
             ('.heap', 0x80, 0x1F),
             ('.stack', 0xC0, 0x22),
            ]
def procesar(segmentos, reqs, marcos_libres):
    tamaño_pagina = 16
    tabla_paginas = {}  # página -> marco
    resultados = []
    fifo_queue = []

    # Helper: verificar segmento válido
    def segmento_valido(dir_virtual):
        for nombre, base, limite in segmentos:
            if base <= dir_virtual <= base + limite - 1:
                return True
        return False

    for req in reqs:
        # 1. Verificar segmento válido
        if not segmento_valido(req):
            resultados.append((f"0x{req:02x}", "0x1ff", "Segmentation Fault"))
            continue

        # 2. Calcular página y offset
        pagina = req // tamaño_pagina
        offset = req % tamaño_pagina

        print(f"req: 0x{req:02x} pagina: {pagina} offset: {offset}")

        # 3. ¿Ya está asignada?
        if pagina in tabla_paginas:
            marco = tabla_paginas[pagina]
            direccion_fisica = marco * tamaño_pagina + offset
            resultados.append((f"0x{req:02x}", f"0x{direccion_fisica:02x}", "Marco ya estaba asignado"))
            continue

        # 4. Asignar marco
        if marcos_libres:
            marco = marcos_libres.pop(0)
            tabla_paginas[pagina] = marco
            fifo_queue.append(pagina)
            direccion_fisica = marco * tamaño_pagina + offset
            resultados.append((f"0x{req:02x}", f"0x{direccion_fisica:02x}", "Marco libre asignado"))
        else:
            # Reemplazo FIFO
            pagina_vieja = fifo_queue.pop(0)
            marco_reutilizado = tabla_paginas[pagina_vieja]
            del tabla_paginas[pagina_vieja]

            tabla_paginas[pagina] = marco_reutilizado
            fifo_queue.append(pagina)

            direccion_fisica = marco_reutilizado * tamaño_pagina + offset
            resultados.append((f"0x{req:02x}", f"0x{direccion_fisica:02x}", "Marco asignado"))

    return resultados

    
def print_results(results):
    
    for result in results:
        print(f"Req: {result[0]} Direccion Fisica: {result[1]} Acción: {result[2]}")

if __name__ == '__main__':
    results = procesar(segmentos, reqs, marcos_libres)
    print_results(results)

