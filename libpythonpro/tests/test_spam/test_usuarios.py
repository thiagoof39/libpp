from libpythonpro.tests.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Thiago', email='marcos@email.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(sessao):
    usuarios = [
        Usuario(nome='Thiago', email='marcos@email.com'),
        Usuario(nome='Ferreira', email='marcos@email.com')
    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()








