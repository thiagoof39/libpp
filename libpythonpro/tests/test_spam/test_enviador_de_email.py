import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailIvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'destinatario',
    ['thiagooliveiraf92@gmail.com', 'thiago@gmail.com', 'tof@gmail.com']
)
def test_remetente(destinatario):
    enviador = Enviador()

    resultado = enviador.enviar(
        destinatario, #De
        'thiagoof.dev@gmail.com', #Para
        'Curso Python Pro', #Assunto
        'Primeiro curso Guido' #Corpo
    )
    assert destinatario in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'thiago']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailIvalido):
        enviador = enviador.enviar(
            remetente, #De
            'thiagoof.dev@gmail.com', #Para
            'Curso Python Pro', #Assunto
            'Primeiro curso Guido' #Corpo
        )

