import os
import shutil
import urllib.request
import PySimpleGUI as sg

class Tela:
    sg.theme('Dark')
    def __init__(self) :
        layout = [
            [sg.Text('Atualizador do manteguinha!',  font=("Arial", 12))],
            [sg.Button('Verificar',  font=("Arial", 12) , button_color=('White', 'Green'))]
        ]
        self.janela = sg.Window("Gerador de codigo QR").layout(layout)

    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            if self.button == sg.WINDOW_CLOSED:
                break

            if self.button == 'Verificar':
                versao = urllib.request.urlopen('Insira aqui o lint').read().decode('utf8').splitlines()[0] # Link do RAW do arquivo contendo a versao
                changelogs = urllib.request.urlopen('Insira aqui o link').read().decode('utf8') # Link do RAW do arquivo contendo o changlog
                link = 'Insira aqui o link' # Link do download no GitHub
                path = 'Arquivo.zip' # Nome que deseja para o arquivo

                # Checando nova versão
                if versao == '0.0.0': # Coloque aqui a versão
                    sg.popup('Nenhuma nova versão encontrada.')
                else:
                    if os.path.exists('Atualizado para a versão ' + versao):
                        sg.popup('A atualização foi instalada.')
                    else:
                        if sg.popup(f'Atualização disponível.\n\n=-==-==-==-==-==-==-=\nChangelogs:\n{changelogs}\n=-==-==-==-==-==-==-=\n\nAtualizar agora?\n', custom_text =('Sim', 'Nao')) == 'Sim':
                            self.janela.hide()
                            urllib.request.urlretrieve(link, path)
                            shutil.unpack_archive(path, 'Atualizado para a versão ' + versao)
                            os.remove(path)
                            # Barra de progresso
                            progress_bar = sg.ProgressBar(max_value=100, orientation='h', size=(20, 20), key='progressbar')
                            layout = [
                                [sg.Text('Baixando arquivo...', font=("Arial", 12))],
                                [progress_bar]
                            ]
                            window = sg.Window('Baixando arquivo...', layout, finalize=True)
                            for i in range(100):
                                progress_bar.UpdateBar(i + 1)
                                window.read(timeout=10)
                            window.close()
                            sg.popup('Atualização instalada com sucesso.', custom_text =('Fechar'))
                            self.janela.close()
                            break
                
tela = Tela()
tela.Iniciar()
