import pytest

from libpythonpro.spam.db import Conexao
from libpythonpro.spam.modelos import Usuario


@pytest.fixture(scope='session') # escopos: function, module e session, o teste roda em cada um desses níveis
def conexao():
    #Setup
    conexao_obj = Conexao()
    yield conexao_obj
    # Tear Down
    conexao_obj.fechar()


@pytest.fixture
def sessao(conexao):
    sessao_obj = conexao.gerar_sessao()
    yield sessao_obj
    sessao_obj.roll_back()
    sessao_obj.fechar()


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Fernando')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(sessao):
    usuarios = [Usuario(nome='Fernando'), Usuario(nome='Rubens')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()

