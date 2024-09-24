import autoit
from pywinauto import Application
from pywinauto.mouse import click

app = Application().start(r'explorer.exe C:\Alura\Senhas')
autoit.mouse_click("left",329, 143,clicks=2)
autoit.send("{ENTER}")