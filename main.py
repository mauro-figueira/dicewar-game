from kivy.app import App
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout

class DiceWarLab(App):
    '''Jogo de guerra de dados'''
    pass

class DiceWarJogo(BoxLayout):
    tamanho_x = 0.5
    tamanho_y = .7
    rodadas = 0
    n_rodadas = StringProperty('0')
    dado1 = 0
    dado2 = 0
    resultado_dado1 = StringProperty('Jogue o dado')
    resultado_dado2 = StringProperty('Jogue o dado')
    vez_jogador1 = BooleanProperty(True)
    vez_jogador2 = BooleanProperty(False)
    vitórias_jogador1 = 0
    mostrar_vitórias1 = StringProperty('0')
    vitórias_jogador2 = 0
    mostrar_vitórias2 = StringProperty('0')
    empates = 0
    mostrar_empates = StringProperty('0')

    def zerar_rodadas(self):
        self.rodadas = 0
        self.n_rodadas = str(self.rodadas)

    def zerar_dado1(self):
        self.dado1 = 0
        self.resultado_dado1 = 'Jogue o dado novamente'

    def zerar_dado2(self):
        self.dado2 = 0
        self.resultado_dado2 = 'Jogue o dado novamente'

    def jogar_dado1(self):
        if self.vez_jogador1 is True:
            import random as rd
            self.dado1 = rd.randint(1,6)
            self.resultado_dado1 = str(self.dado1)
            self.vez_jogador1 = False
            self.vez_jogador2 = True

    def jogar_dado2(self):
        if self.vez_jogador2 is True:
            self.rodadas = self.rodadas + 1
            self.n_rodadas = str(self.rodadas)
            import random as rd
            self.dado2 = rd.randint(1,6)
            self.resultado_dado2 = str(self.dado2)
            self.vez_jogador2 = False
        if self.dado1 > self.dado2:
            self.vitórias_jogador1 += 1
            self.mostrar_vitórias1 = str(self.vitórias_jogador1)
        elif self.dado1 < self.dado2:
            self.vitórias_jogador2 +=1
            self.mostrar_vitórias2 = str(self.vitórias_jogador2)
        elif self.dado1 == self.dado2:
            self.empates +=1
            self.mostrar_empates = str(self.empates)

    def nova_rodada(self):
        self.vez_jogador1 = True
        self.vez_jogador2 = False

DiceWarLab().run()
