from lib2to3.pgen2.grammar import opmap_raw
import time
from main import *
from funções import *


def controle():
    while True:
        opcao = menu_Inicial()
        if opcao == 1:
            listar_Operadores()
        elif opcao == 2:
            pass
        elif opcao == 3:
            print("Finalizando!")
            break
        else:
            print("\nOpcao Invalida!\n")
            time.sleep(0.5)

    
controle()