                                            # Passo a passo do projeto

import pyautogui
import time

                                         # Passo 1 - Entrar no sistema da empresa
pyautogui.PAUSE=1

# Apertar a tecla do Windons
pyautogui.press('win')

# Digitar o nome do navegador
pyautogui.write('chrome')

# Apertar o enter
pyautogui.press('enter')
time.sleep(2)
# Clicar na barra de endereço
pyautogui.click(x=532, y=63)

# Digitar o link no navegador
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.write(link)

#  Apertar o enter
pyautogui.press('enter')

# Esperar 4 segundos

time.sleep(3)


                                         # Passo 2 - Fazer Login
pyautogui.click(x=690, y=409)

# Digitar e-mail
pyautogui.write('testeaula01@gmail.com')

# Passar para o campo de senha
pyautogui.press ('tab')

# Digitar senha
pyautogui.write ('testeaula01')

# Apertar/Clicar no botão LOGAR
pyautogui.write('tab')
pyautogui.press ('enter')
time.sleep(2)

                                        # Passo 3 - Importar a base de dados
import pandas
tabela = pandas.read_csv('produtos.csv')
print(tabela) 



                                        # Passo 4 - Cadastrar um produto
# para cada LINHA  na TABELA, indexar linha
for linha in tabela.index:
    pyautogui.click(x=585, y=291)
    # Código
    codigo=tabela.loc[linha, 'codigo']
    pyautogui.write(codigo)
    pyautogui.press('tab')

    # Marca
    marca=tabela.loc[linha, 'marca']
    pyautogui.write(marca)
    pyautogui.press('tab')

    # Tipo
    tipo=tabela.loc[linha, 'tipo']
    pyautogui.write(tipo)
    pyautogui.press('tab')

    # Categoria
    categoria=tabela.loc[linha,'categoria']
    pyautogui.write(str(categoria))
    pyautogui.press('tab')

    # Preço Unitário
    preco_unitario=tabela.loc[linha, 'preco_unitario']
    pyautogui.write(str(preco_unitario))
    pyautogui.press('tab')

    # Custo
    custo=tabela.loc[linha, 'custo']
    pyautogui.write(str(custo))
    pyautogui.press('tab')

    # OBS
    # tratar uma condição, porque o NaN (Not a Number) estará vazio para alguns cadastros
    obs=tabela.loc[linha, 'obs']

    #se não estiver vazio, então ele vai escrever o que estiver na coluna do 'obs'
    if not pandas.isna(obs):
        pyautogui.write(obs)

    pyautogui.press('tab')

    # Botão ENVIAR
    pyautogui.press("enter")
    pyautogui.scroll(5000)

                                        # Passo 5 Repetir isso até acabar a base de dados





