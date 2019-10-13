import PySimpleGUI as sg

class MainWindow(sg.Window):
    def __init__(self, windowName):
        self.layout = [[sg.Text('Some text on Row 1')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]
        super().__init__(windowName, self.layout)
        self.loop()
    
    def __del__(self):
        self.close()
    
    def loop(self):
        while True:
            event, values = self.read()
            if event in (None, 'Cancel'):   # if user closes window or clicks cancel
                break
            print('You entered ', values[0])