import pyautogui
import pandas
import time

#passo 1
pyautogui.PAUSE=2
pyautogui.press('win')
pyautogui.write('opera gx')
pyautogui.press('enter')
pyautogui.PAUSE=5

pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

#passo 2
time.sleep(3)
pyautogui.click(x=422, y=394)

pyautogui.PAUSE=2
pyautogui.write('emeilaouto@gmail.com')
pyautogui.press('tab')
pyautogui.write('senha123')
pyautogui.press('tab')
pyautogui.press('enter')

#passp 3
tabela=pandas.read_csv('produtos.csv')
print(tabela)

time.sleep(2)
pyautogui.click(x=421, y=273)

for linha in tabela.index:
    pyautogui.click(x=421, y=273)
    #codigo
    codigo=tabela.loc[linha, 'codigo']
    pyautogui.write(str(codigo))
    pyautogui.press('tab')
    #marca
    marca=tabela.loc[linha, 'marca']
    pyautogui.write(str(marca))
    pyautogui.press('tab')
    #tipo
    tipo=tabela.loc[linha, 'tipo']
    pyautogui.write(str(tipo))
    pyautogui.press('tab')
    #categoria
    categoria=tabela.loc[linha, 'categoria']
    pyautogui.write(str(categoria))
    pyautogui.press('tab')
    #preco_unitario
    preco_unitario=tabela.loc[linha, 'preco_unitario']
    pyautogui.write(str(preco_unitario))
    pyautogui.press('tab')
    #custo
    custo=tabela.loc[linha, 'custo']
    pyautogui.write(str(custo))
    pyautogui.press('tab')
    #obs
    obs=tabela.loc[linha, 'obs']
    if obs!='nan':
        pyautogui.write(str(obs))
        
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.scroll(10000)
