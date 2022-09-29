from src.model.quadronegro import *
import pytest

# Checar se as submissões têm texto no atributo  `resposta`
@pytest.mark.sim_ag22
def test_verificar_se_submissoes_possuem_texto_no_atributo_resposta():
    d = Disciplina("DevLife")
    tur = Turma(d, "DevLife 2022/1")
    estudante = Estudante("Diana Deana")
    estudante.matricular(tur)
    tarefa = Tarefa(tur, "Pedro Álvares Cabral")
    tur.tarefas.append(tarefa)
    tarefa.submeter("Pedro A", estudante, datetime.datetime(2022, 9, 16))

    assert len(Tarefa.submissoes) > 0

# Checar se as submissões do estudante são de tarefas pertencentes a turmas que o estudante cursa 
@pytest.mark.sim_ag22
def test_verificar_se_submissoes_do_estudante_sao_de_tarefas_de_turmas_do_estudante():
    d = Disciplina("DevLife")
    tur = Turma(d, "DevLife 2022/1")
    estudante = Estudante("Diana Deana")
    estudante.matricular(tur)
    tarefa = Tarefa(tur, "Pedro Álvares Cabral")
    tur.tarefas.append(tarefa)
    tarefa.submeter("Pedro A", estudante, datetime.datetime(2022, 9, 16))

    assert tarefa.turma in estudante.turmas
    
 
# Checar se o estudante só pertence a determinada turma uma vez
@pytest.mark.sim_ag22
def test_verificar_se_estudante_pertence_a_uma_turma():
    d = Disciplina("DevLife")
    tur = Turma(d, "DevLife 2022/1")
    estudante = Estudante("Diana Deana")
    estudante.matricular(tur)
    tarefa = Tarefa(tur, "Pedro Álvares Cabral")
    tur.tarefas.append(tarefa)
    tarefa.submeter("Pedro A", estudante, datetime.datetime(2022, 9, 16))

    assert len(estudante.turmas) == 1

# Checar se o estudante só pertence a determinada turma uma vez
@pytest.mark.sim_ag22
def test_verificar_se_todas_as_turmas_do_estudante_sao_do_ano_atual():
    d1 = Disciplina("DevLife")
    d2 = Disciplina("CDados")
    tur1 = Turma(d1, "DevLife 2022/1", datetime.datetime(2022, 9, 20))
    tur2 = Turma(d2, "Ciência dos Dados", datetime.datetime(2022, 4, 20))

    estudante = Estudante("Cássio Andor")
    
    estudante.matricular(tur1)
    estudante.matricular(tur2)    

    agora = datetime.datetime.now()
    
    todas_atuais = True
    for t in estudante.turmas:
        if t.data.year != agora.year: 
            todas_atuais = False
    
    assert True == todas_atuais, "Verificacao se todas as turmas sao do ano atual "
