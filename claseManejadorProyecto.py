import csv
from claseProyecto import Proyecto
class ManejadorProyecto:
    def __init__(self):
        self.__listaProyectos = []
    def AgregaProy(self,proyecto):
        self.__listaProyectos.append(proyecto)
    def BuscaProy(self,clave): # La clave es el ID del proyecto
        for i in enumerate(self.__listaProyectos):
            if self.__listaProyectos[i].GetIdProy() == clave:
                return i
    def CargaProyectos(self):
        archivo = open('proyectos.csv')
        reader = csv.reader(archivo, delimiter=';')
        ban = True
        for fila in reader:
            if ban:
                ban = not ban # Niega bandera (esto se hace una vez y es para saltear la primera linea)
            else:
                idProy = fila[0]
                titu = fila[1]
                palclav = fila[2]
                unProyecto = Proyecto(idProy, titu, palclav)
                self.AgregaProy(unProyecto)
    def CalculaPuntaje(self,listaIntegrantes):
        for i in range(len(self.__listaProyectos)):
            acum = 0 # Variable acumulador para puntaje total
            cantint = 0 # Cantidad de integrantes
            banDirector = False # Bandera para indicar si el proyecto tiene director (False por defecto)
            banCatDirector = False # Bandera para indicar si el director es de categoria I o II (False por defecto)
            banCoDirector = False # Bandera para indicar si el proyecto tiene codirector (False por defecto)
            banCatCoDirector = False # Bandera para indicar si el codirector es de categoria I, II, o III (False por defecto)
            print('Proyecto en revision: {}'.format(str(self.__listaProyectos[i].GetIdProy())))
            print('Observaciones:')
            for j in range(len(listaIntegrantes)): 
                if self.__listaProyectos[i].GetIdProy() == listaIntegrantes[j].GetIdIntegr(): 
                    if listaIntegrantes[j].GetRol() == 'integrante': # Criterio: cantidad de integrantes
                        cantint += 1
                    if listaIntegrantes[j].GetRol() == 'director': # Criterio: tiene director y su categoría es I o II
                        banDirector = True # Tiene director
                        if listaIntegrantes[j].GetCatInvest() == 'I' or listaIntegrantes[j].GetCatInvest() == 'II':
                            banCatDirector = True
                    if listaIntegrantes[j].GetRol() == 'codirector': # Criterio: tiene codirector
                        banCoDirector = True
                        if listaIntegrantes[j].GetCatInvest() == 'I' or listaIntegrantes[j].GetCatInvest() == 'II' or listaIntegrantes[j].GetCatInvest() == 'III':
                            banCatCoDirector = True # Criterio:tiene codirector y su categoria es I, II o III
            if cantint >= 3:
                acum += 10 # Tiene minimo de 3 integrantes, +10 puntos
            else:
                print('El Proyecto debe tener como mínimo 3 integrantes.')
                acum -= 20 # No llega a 3 integrantes, -20 puntos
            if banDirector == True or banCoDirector == True: # Tiene director o codirector
                if banDirector == True:
                    if banCatDirector == True: # Tiene director con categoría I o II, +10 puntos
                        acum += 10
                    else:
                        print('El Director del Proyecto debe tener categoría I o II.')
                        acum -= 5
                else:
                    print('El Proyecto debe tener un Director.') 
                if banCoDirector == True:
                    if banCatCoDirector == True:
                        acum += 10
                    else:
                        print('El Codirector del Proyecto debe tener como mínimo categoría III.')
                        acum -= 5
                else:
                    print('El Proyecto debe tener un Codirector.')
            else:
                acum -= 10 # El proyecto no tiene director o codirector
            print('Puntaje obtenido:{}'.format(str(acum)))
            print('------------------------------------------------------')
            self.__listaProyectos[i].SetPuntos(acum) # Registra los puntos
        print('Se ha registrado el puntaje de todos los proyectos.')
    def RankProyectos(self):
        print('Ranking de proyectos de mayor a menor puntaje:')
        print('------------------------------------------------------')
        self.__listaProyectos.sort(reverse=True) # Metodo de lista que la ordena de mayor a menor (se hizo sobrecarga de operadores antes)
        for i in range(len(self.__listaProyectos)):
            print('Puesto {}'.format(str(i+1)))
            self.__listaProyectos[i].MostrarProyecto()
            print('------------------------------------------------------')
