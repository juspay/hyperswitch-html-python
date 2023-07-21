#! /usr/bin/env python3.6
"""
Python 3.6 or newer required.
"""
import http.client
import json
import os
from flask import Flask, render_template, jsonify, request

app = Flask(__name__,
            static_folder='public',
            static_url_path='',
            template_folder='public')

def calculate_order_amount(items):
  # Replace this constant with a calculation of the order's amount
  # Calculate the order total on the server to prevent
  # people from directly manipulating the amount on the client
  return 1400

@app.route('/create-payment', methods=['POST'])
def create_payment():
  try:
    conn = http.client.HTTPSConnection("sandbox.hyperswitch.io")
    payload = "{\n \"amount\": 100,\n \"currency\": \"USD\"\n}"
    headers = {
      'Content-Type': "application/json",
      'Accept': "application/json",
      'api-key': "YOUR_API_KEY",
    }
    conn.request("POST", "/payments", payload, headers)
    res = conn.getresponse()
    data = json.loads(res.read())
    return jsonify({'client_secret': data['client_secret']})
  except Exception as e:
    return jsonify(error=str(e)), 403

if __name__ == '__main__':
  app.run(port=4242)
