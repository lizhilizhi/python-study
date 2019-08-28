import pytest


@pytest.fixture(scope = 'function')
def setup_function(request):
    def teardown_function():
        print("1")
    request.addfinalizer(teardown_function)
    print(2)



@pytest.fixture(scope = 'module')
def setup_module(request):
    def teardown_function():
        print("1")
    request.addfinalizer(teardown_function)
    print(2)


@pytest.mark.website
def test_1(setup_function):
    print('Test_1 called.')

def test_2(setup_module):
    print('Test_2 called.')

def test_3(setup_module):
    print('Test_3 called.')
    assert 2==1+1



def test_success():
    """ this test success"""
    assert True
