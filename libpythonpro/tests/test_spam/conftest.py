import pytest

from libpythonpro.tests.spam.db import Conexao


@pytest.fixture(scope='module')
def conexao():
    # Setup
    conexao_obj = Conexao()
    # Value of tests
    yield conexao_obj
    # Tear Down
    conexao_obj.fechar()


@pytest.fixture
def sessao(conexao):
    sessao_obj = conexao.get_sessao()
    yield sessao_obj
    sessao_obj.roll_back()
    sessao_obj.fechar()