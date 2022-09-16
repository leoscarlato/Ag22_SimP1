import datetime
import difflib 


def corrigir(gabarito, resposta):
    dif = difflib.SequenceMatcher(None, gabarito, resposta)
    return 10*(1 - dif.ratio())



class User(object):
    def __init__(self, nome):
        self.nome = nome 


class Professor(object):
    def __init__(self, nome):
        self.nome = nome
        self.turmas = [] 

class Estudante(object):
    def __init__(self, nome):    
        self.nome = nome
        self.turmas = [] 
        self.submissoes = []

class Disciplina(object):
    def __init__(self,nome):
        self.nome = nome 

class Turma(object):
    EM_ABERTO = 0 
    CONCLUIDO = 1
    CANCELADO = 2
    def __init__(self,nome, data = datetime.now):
        self.nome = nome
        self.status = Turma.EM_ABERTO
        self.data = data


class Tarefa(object):
    submissoes = []
    def __init__(self, turma, gabarito):
        self.turma = turma 
        self.gabarito = gabarito

    def submeter(self, resposta, aluno, data = datetime.now):
        submissao = Submissao(resposta)
        submissao.nota = corrigir(self.gabarito, submissao.resposta)
        Tarefa.submissoes.append(submissao)
        aluno.submissoes.append(submissao) # isso é um bom encapsulamento? Por quê? 


class Submissao(object):
    def __init(self, tarefa, resposta):
        self.__nota == 0 
        self.tarefa = tarefa 
        self.resposta = resposta 

    @property
    def nota(self):
        return self.__nota

    @nota.getter
    def get_nota(self):
        return self.__nota

    @nota.setter
    def set_nota(self, nova_nota):
        self.__nota = nova_nota

class FachadaTarefa:
    def listar_tarefas():
        """Deve retornar uma lista com o nome de todas as tarefas"""
        pass

    def listar_notas_estudante(nome_tarefa:str, nome_estudante:str):
        """Deve retornar uma lista com as notas que o estudante obteve em todas as suas submissões para uma dada tarefa"""
        pass 

    def listar_disciplinas(nome_estudante:str): 
        """Deve retornar os nomes de todas as disciplinas que alguém cursa"""
        pass 









