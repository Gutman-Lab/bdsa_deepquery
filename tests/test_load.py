import pytest

from girder.plugin import loadedPlugins


@pytest.mark.plugin('bdsa_deepquery')
def test_import(server):
    assert 'bdsa_deepquery' in loadedPlugins()
