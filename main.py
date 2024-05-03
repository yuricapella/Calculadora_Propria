from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QDialog, QScrollArea, QTextEdit
import sys
import math



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Calculadora")
        
        layout = QVBoxLayout()
        
        self.calculadora_title = QLabel("Minha Calculadora")
        layout.addWidget(self.calculadora_title)
        
        
        #Botões
        self.raiz_button = QPushButton("Calcular Raiz Quadrada")
        self.tabuada_button = QPushButton("Calcular Tabuada")
        self.potencia_button = QPushButton("Calcular Potência")
        self.multiplicacao_button= QPushButton("Calcular Multiplicação")
        
        layout.addWidget(self.raiz_button)
        layout.addWidget(self.tabuada_button)
        layout.addWidget(self.potencia_button)
        layout.addWidget(self.multiplicacao_button)
        
        self.calculadora_hint = QLabel("Você pode utilizar tab e shift tab para se locomover\n e também apertar enter para ter o resultado")
        layout.addWidget(self.calculadora_hint)

        
        #Evento de click
        self.raiz_button.clicked.connect(self.abrir_calculadora_raiz)
        self.tabuada_button.clicked.connect(self.abrir_calculadora_tabuada)
        self.potencia_button.clicked.connect(self.abrir_calculadora_potencia)
        self.multiplicacao_button.clicked.connect(self.abrir_calculadora_multiplicacao)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        central_widget.setFixedSize(300,300)
        self.setCentralWidget(central_widget)
    
    #Funções para abrir janela de cada botão ao clicar
    def abrir_calculadora_raiz(self):
        self.raiz_window = CalculadoraRaiz()
        self.raiz_window.show()
        
    def abrir_calculadora_potencia(self):
        self.potencia_window = CalculadoraPotencia()
        self.potencia_window.show()

    def abrir_calculadora_tabuada(self):
        self.tabuada_window = CalculadoraTabuada()
        self.tabuada_window.show()

    def abrir_calculadora_multiplicacao(self):
        self.multiplicacao_window = CalculadoraMultiplicacao()
        self.multiplicacao_window.show()
        


class CalculadoraRaiz(QDialog):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Calculadora de Raiz Quadrada")
        
        layout = QVBoxLayout()
        
        self.raiz_quadrada_title = QLabel("Digite o numero: ")
        layout.addWidget(self.raiz_quadrada_title)

        self.input_raiz_quadrada = QLineEdit()
        layout.addWidget(self.input_raiz_quadrada)

        self.resultado_label = QLabel("Resultado")
        layout.addWidget(self.resultado_label)

        self.calcular_button = QPushButton("Calcular")
        layout.addWidget(self.calcular_button)

        self.calcular_button.clicked.connect(self.calcular_raiz_quadrada)
        
        self.setLayout(layout)
        self.setFixedSize(300,200)
    
    def calcular_raiz_quadrada(self):
        try:
            valor = int(self.input_raiz_quadrada.text())
            resultado = math.sqrt(valor)
            self.resultado_label.setText(f"A raiz quadrada de {valor} é {resultado}")
        except ValueError:
            self.resultado_label.setText("Entrada inválida")


class CalculadoraPotencia(QDialog):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Calculadora de potencia")
        
        layout = QVBoxLayout()
        
        self.valor_title = QLabel("Digite o numero: ")
        layout.addWidget(self.valor_title)

        self.input_valor = QLineEdit()
        layout.addWidget(self.input_valor)
        
        self.potencia_title = QLabel("Elevado a quanto?")
        layout.addWidget(self.potencia_title)
        
        self.input_potencia = QLineEdit()
        layout.addWidget(self.input_potencia)

        self.resultado_label = QLabel("Resultado")
        layout.addWidget(self.resultado_label)

        self.calcular_button = QPushButton("Calcular")
        layout.addWidget(self.calcular_button)

        self.calcular_button.clicked.connect(self.calcular_raiz_quadrada)
        
        self.setLayout(layout)
        self.setFixedSize(200,200)
    
    def calcular_raiz_quadrada(self):
        try:
            valor = int(self.input_valor.text())
            potencia = int(self.input_potencia.text())
            resultado = valor ** potencia
            self.resultado_label.setText(f"{valor} elevado a {potencia}  é: {resultado}")
        except ValueError:
            self.resultado_label.setText("Entrada inválida")


class CalculadoraTabuada(QDialog):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Calculadora de Tabuada")
        
        layout = QVBoxLayout()

        self.resultado_label = QLabel("Digite o número: ")
        layout.addWidget(self.resultado_label)
        
        self.input_tabuada = QLineEdit()
        layout.addWidget(self.input_tabuada)
        
        self.resultado_label = QLabel("A tabuada irá até onde?")
        layout.addWidget(self.resultado_label)
        
        self.input_tabuada_total = QLineEdit()
        layout.addWidget(self.input_tabuada_total)

        self.resultado_label = QLabel("Resultado")
        layout.addWidget(self.resultado_label)
        
        self.scroll_area_resultado = QScrollArea()
        self.scroll_area_resultado.setWidgetResizable(True)
        
        self.resultado_text_edit = QTextEdit()
        self.resultado_text_edit.setReadOnly(True)  # Para tornar o QTextEdit apenas de leitura
        self.scroll_area_resultado.setWidget(self.resultado_text_edit)
        
        layout.addWidget(self.scroll_area_resultado)

        self.calcular_button = QPushButton("Calcular")
        layout.addWidget(self.calcular_button)

        self.calcular_button.clicked.connect(self.calcular_tabuada)
        
        self.setLayout(layout)
        
    def calcular_tabuada(self):
        try:
            n = int(self.input_tabuada.text())
            tabuada_total = int(self.input_tabuada_total.text())
            tabuada_texto = ""
            for i in range(tabuada_total + 1):
                tabuada = n * i
                tabuada_texto += f"{n} x {i} = {tabuada}\n"
            self.resultado_text_edit.setText(tabuada_texto)
        except ValueError:
            self.resultado_text_edit.setText("Digite um número inteiro!")
                 
class CalculadoraMultiplicacao(QDialog):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Calculadora de Multiplicação")
        
        layout = QVBoxLayout()

        self.input_valor = QLineEdit()
        layout.addWidget(self.input_valor)
        
        self.input_segundo_valor = QLineEdit()
        layout.addWidget(self.input_segundo_valor)

        self.resultado_label = QLabel("Resultado")
        layout.addWidget(self.resultado_label)

        self.calcular_button = QPushButton("Calcular")
        layout.addWidget(self.calcular_button)

        self.calcular_button.clicked.connect(self.calcular_multiplicacao)

        self.setLayout(layout)
    
    def calcular_multiplicacao(self):
        try:
            n = int(self.input_valor.text())
            m = int(self.input_segundo_valor.text())
            resultado = n*m
            self.resultado_label.setText(f"{n}x{m} é = {resultado}")
        except ValueError:
            self.resultado_label.setText("Digite um número inteiro!")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
