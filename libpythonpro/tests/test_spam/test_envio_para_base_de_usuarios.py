from unittest.mock import Mock
import pytest

from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.tests.spam.main import EnviadorDeSpam
from libpythonpro.tests.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
     [
        [
            Usuario(nome='Thiago', email='thiago@email.com'),
            Usuario(nome='Ferreira', email='ferreira@email.com')
        ],
        [
            Usuario(nome='Marcos', email='marcos@email.com')
        ]
    ]
)
def test_qtd_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'thiagoof.facul@gmail.com',
        'Curso Python Pro',
        'Confira os modulos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Marcos', email='marcos@email.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'ferreira.facul@gmail.com',
        'Curso Python Pro',
        'Confira os modulos'
    )
    enviador.enviar.assert_called_once_with (
        'ferreira.facul@gmail.com',
        'marcos@email.com',
        'Curso Python Pro',
        'Confira os modulos'
    )

