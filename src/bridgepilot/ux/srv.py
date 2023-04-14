import os
import sys
import time
import json
import yaml
import shutil
import hashlib
import zipfile
import base64
import uuid
from os import environ
from pathlib import Path

import requests
import click
from flask import Flask, jsonify, request
from flask_restful import Resource, Api, fields, marshal_with
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec
from flask_jsonrpc import JSONRPC

from cli_passthrough import cli_passthrough

from basekit.objects import globalconfig
from basekit.infosources.distribution import info
from basekit.ops.scaffolding import set_global_bracket_data, get_global_bracket_data
from basekit.ops.scaffolding import get_hydrated_scaffolding_paths, build_scaffolding, test_scaffolding, get_scaffolding_style, scaffolding_styles
from basekit.infosources.distribution import get_distribution_name, get_distribution_version, distribution_install_editable, caller_info, call_order, get_distribution_files, get_distribution_filepaths

from bridgepilot.config import host, port
from bridgepilot.content.htmlfiles import indexhtml
from bridgepilot.datatransfer.restapi import AwesomeAPI

flask_app = Flask("application")
restapi_app = Api(flask_app)

flask_app.config.update({
	'APISPEC_SPEC': APISpec(
		title='Awesome Project',
		version='v1',
		plugins=[MarshmallowPlugin()],
		openapi_version='2.0.0'
	),
	'APISPEC_SWAGGER_URL': '/swagger/',
	'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'
})

@flask_app.route('/')
def root():
	return indexhtml

@flask_app.route('/system/info')
def info_main():
	return info()

def start_server():
	flask_app.run(debug=True, port=port, host=host)

restapi_app.add_resource(AwesomeAPI, '/awesome')
docs = FlaskApiSpec(flask_app)
docs.register(AwesomeAPI)

jsonrpc = JSONRPC(flask_app, "/rpc", enable_web_browsable_api=True)

@jsonrpc.method("App.index")
def index() -> str:
    return "Welcome to Flask JSON-RPC test"