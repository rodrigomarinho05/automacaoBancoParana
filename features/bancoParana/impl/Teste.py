from pywinauto import Application
from pywinauto.mouse import click

app = Application(backend='uia').start('calc.exe')

click('ApplicationFrameInputSinkWindow')

