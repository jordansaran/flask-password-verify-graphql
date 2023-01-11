"""
Executa aplicação Flask
OBS: Este arquivo serve de referência para o arquivo .env
"""


from http import HTTPStatus

from ariadne import load_schema_from_path, make_executable_schema, snake_case_fallback_resolvers, graphql_sync, \
    QueryType
from ariadne.constants import PLAYGROUND_HTML
from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.middleware.proxy_fix import ProxyFix

from resolvers import verify_resolver
from settings.settings import Settings

app = Flask('api')
CORS(app)
app.wsgi_app = ProxyFix(app.wsgi_app)
app.config.from_object(Settings())

type_defs = load_schema_from_path("schema.graphql")
query = QueryType()
query.set_field("verify", verify_resolver)
schema = make_executable_schema(type_defs, query, snake_case_fallback_resolvers)


@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=Settings().debug_is_enabled()
    )
    return jsonify(result), int(HTTPStatus.OK) if success else int(HTTPStatus.BAD_REQUEST)
