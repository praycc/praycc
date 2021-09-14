import pytest


@pytest.fixture(scope='session')
def session_fixture():
    pass

@pytest.fixture(scope='module')
def module_fixture():
    pass

@pytest.fixture(scope='class')
def clas_fixture():
    pass

@pytest.fixture(scope='function')
def funciton_fixture():
    pass

def test_fixture1(session_fixture,module_fixture,clas_fixture,funciton_fixture):
    pass

if __name__ == '__main__':
    pytest.main(['--setup-show,-sv','test_fixture.py'])