def hello_world(name):
    return "Hello {}".format(name)

def test_hello():
    assert hello_world("World!") == "Hello World!"

    