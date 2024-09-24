import pywinauto
from pywinauto import Application

app = Application().start(r'explorer.exe D:\EXPORTACAO\FI.WFIUtilNet')
pywinauto.mouse.click(button='left',coords=(2042,0))
