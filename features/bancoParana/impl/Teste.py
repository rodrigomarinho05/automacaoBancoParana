from pywinauto import Application
from pywinauto.mouse import click

#Teste 18-09
app = Application(backend='uia').start('calc.exe')

click('ApplicationFrameInputSinkWindow')

