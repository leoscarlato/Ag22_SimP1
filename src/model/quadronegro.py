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

    def matricular(self, turma):
        self.turmas.append(turma)
        turma.estudantes.append(self)

class Disciplina(object):
    def __init__(self,nome):
        self.nome = nome 

class Turma(object):
    EM_ABERTO = 0 
    CONCLUIDO = 1
    CANCELADO = 2
    def __init__(self,disciplina:Disciplina, nome:str, data = datetime.datetime.now()):
        self.nome = nome
        self.status = Turma.EM_ABERTO
        self.data = data
        self.estudantes = []
        self.disciplina = disciplina
        self.tarefas = []

class Tarefa(object):
    submissoes = []
    tarefas = [] # adicionado
    def __init__(self, turma, gabarito):
        self.turma = turma 
        self.gabarito = gabarito
        Tarefa.tarefas.append(self) # adicionado

    def submeter(self, resposta, aluno, data = datetime.datetime.now()):
        submissao = Submissao(self, resposta)
        submissao.nota = corrigir(self.gabarito, submissao.resposta)
        Tarefa.submissoes.append(submissao)
        aluno.submissoes.append(submissao) # TODO: isso é um bom encapsulamento? Por quê? 

    @classmethod
    def listar_submissoes_aluno(cls, estudante:Estudante): 
        """Lista todas as submissões de um dado aluno"""
        submissoes_aluno = []
        for submissao in cls.submissoes:
            if submissao in estudante.submissoes:
                submissoes_aluno.append(submissao)
        return submissoes_aluno

class Submissao(object):
    def __init__(self, tarefa, resposta):
        self.__nota = 0
        self.tarefa = tarefa 
        self.resposta = resposta 

    @property
    def nota(self):
        return self.__nota

    @nota.setter
    def nota(self, nova_nota):
        self.__nota = nova_nota

class FachadaTarefa:
    def listar_tarefas():
        gabaritos = []
        for tarefa in Tarefa.tarefas:
            gabaritos.append(tarefa.gabarito)
        return gabaritos
            

    def listar_notas_estudante(nome_tarefa:str, nome_estudante:str):
        submissoes = Tarefa.submissoes
        estudantes = Estudante.estudantes

        for e in estudantes:
            if e.nome == nome_estudante:
                estud = e

        notas = []

        for s in estud.submissoes: 
            if s.tarefa.gabarito == nome_tarefa: 
                notas.append(s.nota)

        return notas 

    def listar_disciplinas(nome_estudante:str): 
        estudantes = Estudante.estudantes
        disciplinas = []

        for e in estudantes:
            if e.nome == nome_estudante:
                estud = e

        for t in estud.turmas:
            disciplinas.append(t.disciplina.nome)

        return disciplinas

if __name__ == "__main__":
    d = Disciplina("DevLife")
    tur = Turma(d, "DevLife 2022/1")
    estudante = Estudante("Diana Deana")
    estudante.matricular(tur)
    tarefa = Tarefa(tur, "Pedro Álvares Cabral")
    tur.tarefas.append(tarefa)
    tarefa.submeter("Pedro A", estudante, datetime.datetime(2022, 9, 16))
    print(Tarefa.submissoes)
    print(estudante.turmas)
    print(tarefa.turma)
    print(FachadaTarefa.listar_disciplinas(estudante))
    









