# -*- coding: utf-8 -*-

from claseManejadorProyecto import ManejadorProyecto
from claseManejadorIntegrantesProyecto import ManejadorIntegrantes
if __name__ == '__main__':
    mp = ManejadorProyecto()
    mp.CargaProyectos()
    print('Se han cargado los proyectos.')
    mi = ManejadorIntegrantes()
    mi.CargaIntegrantes()
    print('Se han cargado los integrantes de proyectos.')
    mp.CalculaPuntaje(mi.GetLista())
    mp.RankProyectos()
