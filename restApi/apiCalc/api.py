from unittest import result
from rest_framework.response import Response
from .serializers import CalcSerializer
from rest_framework.views import APIView
from rest_framework import status

# Creado por: Erik S. Medina
# Fecha: 08/05/2022
# Descripción: Clase para realizar la operación de calculo de contraseña en base al archivo keylog.txt
# Parámetros:Ninguno
# Retorno: Clave que coincide con datos del keylog
# Versión: 1.0

class CalcView(APIView):

    def get(self, request):
        serializer = CalcSerializer(data=request.data)
        if serializer.is_valid():
            array1 = []
            lista = ['319', '680', '180', '690', '129', '620', '762', '689', '762', '318', '368', '710', '720', '710', '629', '168', '160', '689', '716', '731', '736', '729', '316', '729', '729', '710', '769', '290', '719', '680', '318', '389', '162', '289', '162', '718', '729', '319', '790', '680', '890', '362', '319', '760', '316', '729', '380', '319', '728', '716']
            lista = list(set(lista)) # elimina duplicados para hacer menos iteraciones

            for x in lista: # itera sobre la lista para obtener solo un digito en cada posicion de la nueva lista
                string = x
                array1.append(int(string[:1]))
                array1.append(int(string[1:2]))
                array1.append(int(string[2:3]))

            array1 = list(set(array1)) # elimina duplicados para solo quedar con numeros que conforman la clave
            
            for j in lista:  # itera sobre la lista principal para comparar contra la nueva lista y ordenar segun indice y valor              
                string = str(j)
                index1 = array1.index(int(string[:1])) 
                index2 = array1.index(int(string[1:2]))
                index3 = array1.index(int(string[2:3])) 

                valor1 = array1[index1]
                valor2 = array1[index2]
                valor3 = array1[index3]
                                
                if index1 > index2:                    
                    array1[index1] = valor2
                    array1[index2] = valor1
                
                if index2 > index3:
                    array1[index2] =valor3
                    array1[index3] =valor2

            result ="".join(str(t) for t in array1)
            return Response(result, status=status.HTTP_200_OK)
            
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)