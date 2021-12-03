from libpythonpro.tests.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Thiago')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(sessao):
    usuarios = [Usuario(nome='Thiago'), Usuario(nome='Ferreira')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()








