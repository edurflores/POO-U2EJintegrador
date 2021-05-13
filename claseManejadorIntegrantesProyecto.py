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
                bandera = not bandera # Saltea la primera linea
            else:
                idProy = fila[0]
                apeNom = fila[1]
                docu = fila[2]
                catInv = fila[3]
                rol = fila[4]
                unInvestigador = Integrante(idProy,apeNom,docu,catInv,rol)
                self.AgregaIntegrante(unInvestigador)
        archivo.close()
    def GetLista(self):
        return self.__listaIntegrante
    def MostrarIntegrantes(self):
        print('Lista de integrantes.')
        for i in range(len(self.__listaIntegrante)):
            print('Integrante Nro. {}'.format(int(i+1)))
            print('ID de proyecto en que esta:',self.__listaIntegrante[i].GetIdIntegr())
            print('Apellido y nombre:{}'.format(str(self.__listaIntegrante[i].GetApeNom())))
            print('DNI:{}'.format(str(self.__listaIntegrante[i].GetDni())))
            print('Categoria:{}'.format(str(self.__listaIntegrante[i].GetCatInvest())))
            print('Rol:{}'.format(str(self.__listaIntegrante[i].GetRol())))
