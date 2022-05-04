import pytest

from libpythonpro.spam.enviador_email import Enviador, EmailInvalido


def test_create_send_email():
    enviador = Enviador()
    assert enviador is not None

@pytest.mark.parametrize(
    'destinatario',
    ['fernandoperesvalverde@hotmail.com','nandovalverde@gmail.com']
)

def test_remetente( destinatario):
    enviador = Enviador()
    destinatarios = ['nandovalverde@gmail.com', 'fernandoperesvalverde@hotmail.com']
    destinatario
    resultado = enviador.enviar(destinatario, 'nandovalverde@gmail.com', 'Cursos Python Pro',
                              'Primeira turma Guido Von Rossum aberta.')
    assert destinatario in resultado


@pytest.mark.parametrize(
    'remetente',
    ['','nandovalverde']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(remetente, 'nandovalverde@gmail.com', 'Cursos Python Pro',
                      'Primeira turma Guido Von Rossum aberta.')
