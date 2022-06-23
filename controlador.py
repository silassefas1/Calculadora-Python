import time
from main import *
from funções import *

def controle_menu():
    while True:
        opcao_Usuario = menu_inicial()
        if opcao_Usuario == 1:
            pass
        elif opcao_Usuario == 2:
            time.sleep(0.3)
            listar_Operadores()
            time.sleep(0.7)
        elif opcao_Usuario == 3:
            break
        elif opcao_Usuario != 1 or 2:
            print(f'a opcão {opcao_Usuario} é invalida!')
            time.sleep(2)


controle_menu()
