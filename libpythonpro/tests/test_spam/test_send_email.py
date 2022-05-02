import pytest

from libpythonpro.spam.sender_email import Sender, EmailInvalido


def test_create_send_email():
    sender = Sender()
    assert sender is not None

@pytest.mark.parametrize(
    'destinatario',
    ['fernandoperesvalverde@hotmail.com','nandovalverde@gmail.com']
)

def test_remetente( destinatario):
    sender = Sender()
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
    sender = Sender()
    with pytest.raises(EmailInvalido):
        sender.send(
        remetente,
        'nandovalverde@gmail.com',
        'Cursos Python Pro',
        'Primeira turma Guido Von Rossum aberta.'
    )
