from unittest.mock import Mock

import pytest

from libpythonpro.spam.enviador_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Fernando', email='nandovalverde@gmail.com'),
            Usuario(nome='Rubens', email='nandovalverde@gmail.com')
        ],
        [
            Usuario(nome='Fernando', email='nandovalverde@gmail.com')
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'nandovalverde@gmail.com',
        'Curso Python Pro,',
        'Confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.enviar.call_count


class EnviadorMock(Enviador):

    def __init__(self):
        super().__init__()
        self.qtd_email_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_email_enviados += 1


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Fernando', email='nandovalverde@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'rubensminucci@gmail.com',
        'Curso Python Pro,',
        'Confira os módulos fantásticos'
    )
    enviador.enviar.assert_called_once_with(
        'rubensminucci@gmail.com',
        'nandovalverde@gmail.com',
        'Curso Python Pro,',
        'Confira os módulos fantásticos'
    )
