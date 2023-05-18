# Documentação do Atualizador com Interface Gráfica

Este código é um atualizador de aplicativos que utiliza a biblioteca `urllib` para verificar e baixar atualizações e a biblioteca `PySimpleGUI` para criar uma interface gráfica simples.

## Requisitos

Você precisará das seguintes bibliotecas para executar este código:

- urllib
- PySimpleGUI
- shutil

Para instalar as bibliotecas necessárias, execute o seguinte comando:

```sh
pip install PySimpleGUI
```

## Como usar

O código é um script que, quando executado, exibe uma janela com uma interface gráfica para verificar se há atualizações disponíveis para algum aplicativo.

### Interface gráfica

A interface possui o seguinte botão:

- **Verificar**: Botão para verificar se há atualizações disponíveis.

## Estrutura do código

O código possui uma classe chamada `Tela` que contém a estrutura e a lógica da interface gráfica.

### Classe Tela

A classe `Tela` possui os seguintes métodos:

- `__init__(self)`: Construtor da classe. Define o layout da interface gráfica e cria a janela usando a biblioteca `PySimpleGUI`.
- `Iniciar(self)`: Método que inicia a interface gráfica e aguarda a interação do usuário. Quando o botão "Verificar" é pressionado, verifica se há atualizações disponíveis, exibe informações sobre a atualização e pergunta ao usuário se deseja atualizar. Se o usuário decidir atualizar, o aplicativo baixa e instala a atualização.

## Exemplo de uso

Antes de usar o atualizador, é necessário inserir os links corretos nos seguintes lugares do código:

- Link do RAW do arquivo contendo a versão: `versao = urllib.request.urlopen('Insira aqui o link').read().decode('utf8').splitlines()[0]`
- Link do RAW do arquivo contendo o changelog: `changelogs = urllib.request.urlopen('Insira aqui o link').read().decode('utf8')`
- Link do download no GitHub: `link = 'Insira aqui o link'`

Para usar o atualizador, siga estas etapas:

1. Salve o código em um arquivo chamado, por exemplo, `atualizador.py`.
2. Execute o script `atualizador.py`:

```sh
python atualizador.py
```

A janela da interface gráfica será exibida. Clique no botão "Verificar" para verificar se há atualizações disponíveis. Se houver uma atualização, o aplicativo exibirá informações sobre a atualização e perguntará se você deseja atualizar. Se você decidir atualizar, o aplicativo baixará e instalará a atualização.
