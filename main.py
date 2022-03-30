from Tkfull import Janela
from dados import funcao

class interface:
    obj = [['Menu'],[("Percetual de genero feminino e masculino.",
            "Genero separados por virgula.",
            "Eficacia em jovens, adultos e idoso.",
            "Eficacia da vacina.",
            "Eficacia separada por genero.")],
           ["*Resultado",None],
           [""],
           ]
    def __init__(self):
        self.classe = Janela()
        self.classe.gerar(self.obj)
        self.classe.setEvento(3,self.click) 
        self.classe.start()
    
    def click(self):

        seletor = self.classe.getTexto(2)
        
        if seletor == "Percetual de genero feminino e masculino.":
            self.classe.mensagem(funcao.genero_masclino_feminino())

        if seletor == "Genero separados por virgula.":
            self.classe.mensagem(funcao.genero_virgula())
     
        if seletor == "Eficacia em jovens, adultos e idoso.":
            self.classe.mensagem(funcao.jovem_adulto_idoso())
     
        if seletor == "Eficacia da vacina.":
            self.classe.mensagem(funcao.eficacia_vacina())
     
        if seletor == "Eficacia separada por genero.":
            self.classe.mensagem(funcao.eficacia_masculino_feminino())
            
interface()