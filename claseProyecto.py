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
    def SetPuntos(self,punt):
        if type(punt) is int:
            self.__puntaje = punt
    