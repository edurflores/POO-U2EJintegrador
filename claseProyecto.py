class Proyecto:
    __idProyecto = ''
    __titulo = ''
    __palabrasClave = ''
    __puntaje = 0
    def __init__(self,idproy,tit,palcla):
        if type(idproy) is str:
            self.__idProyecto = idproy
        if type(tit) is str:
            self.__titulo = tit
        if type(palcla) is str:
            self.__palabrasClave = palcla # Ojo, podria ser una lista de palabras
    def GetIdProy(self):
        return self.__idProyecto
    def GetTitulo(self):
        return self.__titulo
    def GetPalabras(self):
        return self.__palabrasClave
    def SetPuntos(self,punt):
        if type(punt) is int:
            self.__puntaje = punt
    def GetPuntos(self):
        return self.__puntaje
    def __gt__(self,otroproy):
        if self.__puntaje > otroproy.GetPuntos():
            return True
        else:
            return False
    def MostrarProyecto(self):
            print('ID de proyecto:{}'.format(str(self.__idProyecto)))
            print('Titulo:{}'.format(str(self.__titulo)))
            print('Palabras clave:{}'.format(str(self.__palabrasClave)))
            print('Puntaje obtenido:{}'.format(str(self.__puntaje)))
