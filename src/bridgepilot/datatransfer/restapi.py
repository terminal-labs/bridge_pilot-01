from flask import Flask
from flask_restful import Resource, Api, fields, marshal_with
from flask_apispec import marshal_with
from flask_apispec.views import MethodResource
from marshmallow import Schema, fields

awesome_response_schema = dict(message=fields.String(default=''))

class AwesomeResponseSchema(Schema):
	message = fields.Str(default='Success')

class AwesomeAPI(MethodResource, Resource):
	#@doc(description='My First GET Awesome API.', tags=['Awesome'])
	@marshal_with(AwesomeResponseSchema)
	def get(self):
		return {'message': 'My First Awesome API'}