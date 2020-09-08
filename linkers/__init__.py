from flask_restplus import Api

from .link import api as link_api

api = Api(
  title='Linkers API',
  version='1.0.0',
  description='Linkers API 1.0.0'
)

api.add_namespace(link_api)