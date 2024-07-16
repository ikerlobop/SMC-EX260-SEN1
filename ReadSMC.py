from cpppo.server.enip import client
from cpppo.server.enip.get_attribute import attribute_operations
from cpppo.server.enip.get_attribute import proxy_simple

# Dirección IP del dispositivo EtherNet/IP por defecto la libreía se conectará al puerto 44818, según estandar de Ethernet/IP
HOST = "192.168.0.202"

# Dirección del área de salida, assembly, instance, attribute.
output_area_address = ("@4/150/3")

# Leer valor actual 
TAGS = [output_area_address]

# Crear un objeto proxy simple
via = proxy_simple(HOST)

with client.connector(host=HOST) as conn:
    for index, descr, op, reply, status, value in conn.synchronous(
        operations=attribute_operations(
            TAGS, route_path=[], send_path='' )):
        
        print("Índice: %s" % index)
        print("Operación: %s" % op)
        print("Respuesta: %s" % reply)
        print("Estado: %s" % status)
        print(": %s" % ( descr))
        print(value)
