from pydoc import render_doc
from time import sleep
import jinja2, uuid, json, os
from flask import Flask, jsonify, render_template, request, Response, send_file

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
  if(request.method == 'GET'):
    data = "hello world"
    return jsonify({
      'message': data,
      'status': 200,
      'mimetype': 'application/json'
    })

@app.route('/template', methods = ['GET'])
def template():
  if(request.method == 'GET'):
    context = {
      'label': 'nginx',
      'port': '80'
    }

    file_name=str(uuid.uuid4())
    global file_path
    file_path="./temp/" + file_name + ".yaml"
    file = open(file_path, "w")
    file_contents = render_template(
      'some.yaml',
      **context
    )
    file.write(file_contents)
    file.close()
    
    return send_file(file_path, as_attachment=True, cache_timeout=0)

# @app.after_request
# def delete_temp(response):
#   sleep(1)
#   global file_path
#   if request.endpoint=="template":
#     os.remove(file_path)
#   return response

if __name__ == 'main':
  app.run()