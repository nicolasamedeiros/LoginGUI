from PySimpleGUI import PySimpleGUI as sg 

#Layout
sg.theme('Reddit')
layout = [
    [sg.Text("Usuário"), sg.Input(key='usuario', size=(20,1))],
    [sg.Text("Senha"), sg.Input(key='senha', password_char='*', size=(20,1))],
    [sg.Checkbox('Salvar o login ?')],
    [sg.Button('Acessar')]
]

#window
janela = sg.Window("GUI do Nicolas", layout) 

#Interect with the window
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    elif eventos == 'Acessar':
        if valores['usuario'] == 'Nicolas' and valores['senha'] == '12345':
            print("Você acessou sua conta, Bem vindo !")
