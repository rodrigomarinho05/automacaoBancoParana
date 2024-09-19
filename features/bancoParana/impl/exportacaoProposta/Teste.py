#from pywinauto import Application
#from pywinauto.mouse import click

#Teste 18-09
#app = Application(backend='uia').start('calc.exe')
#click('ApplicationFrameInputSinkWindow')

from pywinauto import Application
from pywinauto.keyboard import send_keys

# Iniciar a calculadora
app = Application(backend='uia').start('calc.exe')

# Acessar a janela da calculadora
calc_window = app.window(title='Calculadora')

# Clicar nos botões 1 e 0 (não há botão 10, então é necessário simular o 1 seguido de 0)
calc_window.child_window(title="7", control_type="Button").click()
calc_window.child_window(title="1", control_type="Button").click()
calc_window.child_window(title="0", control_type="Button").click()

# Fechar a calculadora
calc_window.close()

# Confirmar fechamento se necessário (por exemplo, quando há operações não salvas)
