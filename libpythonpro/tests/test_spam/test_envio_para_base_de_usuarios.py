from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.tests.spam.main import EnviadorDeSpam


def test_envio_de_spam(sessao):
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.enviar_emails(
        'thiagoof.facul@gmail.com',
        'Curso Python Pro',
        'Confira os modulos'
    )