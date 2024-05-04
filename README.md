
# Calculadora Propria | Resumos

 O programa possui 4 ferramentas, sendo elas:

| Ferramentas | Resumos |
|-------|---------|
|Calcular Raiz Quadrada|Utiliza a Importação do módulo math e a função math.sqrt(valor)|
|Calcular Tabuada|Utiliza um for para armazenar todos os resultados em uma variavel e imprimir tudo de uma vez.|
|Calcular Potência| Utiliza um campo para colocar a base e outro para colocar o expoente e calcular a exponenciação. |
|Calcular Multiplicação|Utiliza dois campos para fazer a multiplicação.|

## 📖 Arquivo main


```
main.py
```

Foi utilizado o framework PySide6 para criação da aplicação


| Bibliotecas | Resumos |
|-------|---------|
| QApplication | Ao criar uma instância de QApplication, você basicamente inicializa a aplicação, configurando-a para responder a eventos de entrada do usuário.|
|QMainWindow | Fornece uma estrutura robusta e flexível para desenvolver janelas de aplicativos. |
|QWidget |Fornece funcionalidades para renderização gráfica, gerenciamento de layout, manipulação de eventos e muito mais.|
|QLabel | Oferece várias opções de personalização, como alinhamento de texto, quebra de linha automática, redimensionamento automático e muito mais|
| QLineEdit|É uma ferramenta versátil para coletar entradas de texto de uma única linha. |
|QPushButton |Permite que os usuários acionem ações específicas com um simples clique de botão. |
|QVBoxLayout |Organiza eficientemente widgets e facilita a criação de layouts verticais bem estruturados e responsivos.|
|QDialog| Utilizado para criar novas janelas ao clicar no botão.|
| QScrollArea| Utilizado para conseguir visualizar uma grande informação em um espaço pequeno no resultado da tabuada.|
| QTextEdit| Utilizado também para visualizar o resultado da tabuada em forma de leitura pois o QScrollArea não permite texto. |

## 💻 Arquivo setup

```
setup.py
```
Foi utilizado o framework cx_Freeze para criação de um executavel independente.


# Observação:
### Além de fazer o programa, criei o executavel e utilizei a ferramenta inno setup para criar um arquivo de instalação com todos os arquivos necessários (criados pelo cx_Freeze) para utilizar o programa em outros computadores que nao possuem todos esses parâmetros que usei para programar.


# Comandos
No cx_freeze utilizei os seguintes comandos:
```
pip install cx_Freeze

python setup.py build
```
cria o executavel com todos os arquivos necessários para abri-lo

## Inno Setup

[Inno Setup site](https://jrsoftware.org/isdl.php)

Só utilizar ele colocando os arquivos e o executavel (criados pelo cx_freeze) dentro da mesma pasta e compilar.

