#web_app/routes/twitter_routes.py

from flask import Blueprint, render_template, jsonify
from web_app.models import db, User, Tweet, parse_records
from web_app.services.twitter_service import api as twitter_api_client
from wep_app.services.basilica_service import connection as basilica_api_client

