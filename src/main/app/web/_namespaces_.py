from flask_restx import Namespace

from main.app import api

org_namespace = Namespace('organisation', description='Organisation operations')
risk_factor_namespace = Namespace('risk_factor', description='Risk factor operations')

api.add_namespace(org_namespace)
api.add_namespace(risk_factor_namespace)
