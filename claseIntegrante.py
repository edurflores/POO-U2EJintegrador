class Integrante:
    __idProyecto = '' # Id del proyecto al que pertenece
    __apellidoNombre = ''
    __dni = ''
    __categoriaInvestigacion = ''
    __rol = '' # director, codirector, integrante
    def __init__(self,idProy,apeNom,docu,catInv,r):
        if type(idProy) is str:
            self.__idProyecto = idProy
        if type(apeNom) is str:
            self.__apellidoNombre = apeNom
        if type(docu) is str:
            self.__dni = docu
        if type(catInv) is str:
            self.__categoriaInvestigacion = catInv
        if type(r) is str:
            self.__rol = r
    def GetIdIntegr(self):
        return self.__idProyecto
    def GetCatInvest(self):
        return self.__categoriaInvestigacion
    def GetRol(self):
        return self.__rol
