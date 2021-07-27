from flask import Flask, render_template, make_response, jsonify, request

app = Flask(__name__)

PORT = 3200
HOST = '0.0.0.0'