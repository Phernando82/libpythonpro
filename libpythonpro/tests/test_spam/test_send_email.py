import pytest

from libpythonpro.spam.enviador_email import Enviador, EmailInvalido


def test_create_send_email():
    sender = Enviador()
    assert sender is not None

@pytest.mark.parametrize(
    'destinatario',
    ['fernandoperesvalverde@hotmail.com','nandovalverde@gmail.com']
)

def test_remetente( destinatario):
    sender = Enviador()
    destinatarios = ['nandovalverde@gmail.com', 'fernandoperesvalverde@hotmail.com']
    destinatario
    resultado = sender.send(
        destinatario,
        'nandovalverde@gmail.com',
        'Cursos Python Pro',
        'Primeira turma Guido Von Rossum aberta.'
    )
    assert destinatario in resultado


@pytest.mark.parametrize(
    'remetente',
    ['','nandovalverde']
)
def test_remetente_invalido(remetente):
    sender = Enviador()
    with pytest.raises(EmailInvalido):
        sender.send(
        remetente,
        'nandovalverde@gmail.com',
        'Cursos Python Pro',
        'Primeira turma Guido Von Rossum aberta.'
    )
