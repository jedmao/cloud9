from graphene.test import Client

from schema import schema


def test_hello():
    client = Client(schema)
    executed = client.execute('''{ hello }''')
    assert executed == {
        'data': {
            'hello': 'Hello stranger!'
        }
    }
