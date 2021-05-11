import csv
from claseIntegrante import Integrante

class ManejadorIntegrantes:
    def __init__(self):
        self.__listaIntegrante = []
    def AgregaIntegrante(self,integr):
        self.__listaIntegrante.append(integr)
    def CargaIntegrantes(self):
        archivo = open('integrantesProyecto.csv')
        reader = csv.reader(archivo, delimiter=';')
        bandera = True
        for fila in reader:
            if bandera:
                not bandera # Saltea la primera linea
            else:
                idProy = fila[0]
                apeNom = fila[1]
                docu = fila[2]
                catInv = fila[3]
                rol = fila[4]
                unInvestigador = Integrante(idProy,apeNom,docu,catInv,rol)
                self.AgregaIntegrante(unInvestigador)
    def GetLista(self):
        return self.__listaIntegrante