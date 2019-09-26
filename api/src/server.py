from flask import Flask
from flask_graphql import GraphQLView

import config
from schema import schema

server = Flask(__name__)

server.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        graphiql=True,
        schema=schema,
    ),
)

if __name__ == '__main__':
    server.run(
        debug=config.DEBUG,
        host=config.HOST,
        port=config.PORT,
    )
