import keybord

def listar_Operadores():
    print(f""" {'-'*10}Operadores Aritmeticos{'-'*10}
    fatorial = fat 
    raiz quadrada = raiz
    seno = seno
    coseno = cos
    tangente = tang
    soma =  +
    subtracao =  -
    multiplicacao =  * 
    divisao =  / 
    divisao_inteira =  // 
    modulo =  % 
    exponenciacao =  **
    {'-'*30}
    """) # math.factorial(x) valor fatorial// sqrt(x) raiz quadrada// math.sin(x) Seno //math.tan(x) tangente // math.cos(x)
def calcular():
    print("""- Para realizar um calculo digite um valor e um operador
        - Presione a tecla esc paravoltar ao menu a qualquermomento
        - Presione Backspace parazerar o calculo
        """)
    while True:

        if keyboard.is_pressed('Esc'): # deixar essaparte nofinal
            print('Voltando ao menu')
            break