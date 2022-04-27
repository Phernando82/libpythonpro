from libpythonpro.spam.sender_email import Sender


def test_create_send_email():
    sender = Sender()
    assert sender is not None


def test_remetente():
    sender = Sender()
    resultado = sender.send(
        'nandovalverde@gmail.com',
        'nandovalverde@gmail.com',
        'Cursos Python Pro',
        'Primeira turma Guido Von Rossum aberta.'
    )
    assert 'nandovalverde@gmail.com' in resultado