from flask import Flask, make_response, render_template, send_from_directory, jsonify, request, redirect
import os
import datetime
import requests
import string
import random
import uuid

import config as config
import modules

# GLOBAL Variables


APPNAME = "file-generator"
VERSION = "v0.3"


app = Flask(__name__)


# Functions

def getjsontext (url):
# Get JSON data
	jsonResponse = requests.get(url)
	return (json.loads(jsonResponse.text))


@app.route('/', methods=['GET'])
def root_page():

    # Generate a non-cacheable page uuid

    nocache = str((uuid.uuid1()))
    print(nocache)
    return redirect('/webapp?nocache=' + nocache)


@app.route('/list', methods=['GET'])
def list_alltypes():

    return (make_response(jsonify({'error': 'specify type'}), 400))


@app.route('/list/documents', methods=['GET'])
def list_doctypes():


    return (make_response(jsonify({'filetypes': modules.documents.filetypes}), 200))


@app.route('/list/compress', methods=['GET'])
def list_compresstypes():


    return (make_response(jsonify({'filetypes': modules.compress.filetypes}), 200))

@app.route('/list/encrypt', methods=['GET'])
def list_encrypttypes():


    return (make_response(jsonify({'filetypes': modules.encrypt.filetypes}), 200))


def make_filename(doctype):

    stringLength = 8
    chars = string.ascii_lowercase + string.digits
    uid = ''.join(random.choice(chars) for i in range(stringLength))

    return(doctype + "-" + datetime.datetime.now().strftime("%Y%m%d") + "-" + uid)

def sanitise(u_string):

    return (u_string
        .replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        .replace("'", "&#39;").replace('"', "&quot;")
        )

@app.route('/fetch', methods=['GET'])
def fetch():

    return make_response(jsonify('error', 'try fetch/[document_type]'), 400)


@app.route('/fetch/<string:u_doctype>', methods=['GET'])
def fetch_document(u_doctype):

    compress = False
    encrypt = False
    malware = False

    sourcefile = config.respath() + "plaintext.txt"

    if request.args:

        # We have some optional parameters

        if 'compress' in request.args:
            if 'compress' != 'none':
                compress = True

        if 'malware' in request.args:
            if 'malware' != 'none':
                sourcefile = config.respath() + "eicar.txt"
                malware = True

    t_doctype= sanitise(u_doctype)

    # generate the file
    if t_doctype in modules.documents.filetypes:

        method = getattr(modules.documents, 'doc_' + t_doctype)
        file = method(make_filename(t_doctype), sourcefile)

        osfilepath = config.filespath() + file.fullname

        returnfile = file.fullname
        returnmimetype = file.mimetype


        if compress:


            u_compresstype = request.args['compress']
            t_compresstype = sanitise(u_compresstype)


            if t_compresstype in modules.compress.filetypes:

                method = getattr(modules.compress, 'cmp_' + t_compresstype)

                compressedfile = method(returnfile, osfilepath)
                returnfile = compressedfile.fullname
                returnmimetype = compressedfile.mimetype
                osfilepath = config.filespath() + compressedfile.fullname

        exists = os.path.isfile(osfilepath)
        if exists:
            return (send_from_directory(os.path.join(config.apppath(), 'files'), returnfile ,mimetype=returnmimetype, as_attachment=True))


    return make_response(jsonify('error','file generation failed'), 500)


@app.route('/webapp', methods=['GET'])
def webapp():

    # Get document types


    if request.args:

        # We have some optional parameters

        if 'nocache' in request.args:

            documents = modules.documents.filetypes
            compressed = modules.compress.filetypes

            return render_template('index.html', doctype_list = documents, comptype_list = compressed)

    else:

        # Generate a non-cacheable page uuid

        nocache = str((uuid.uuid1()))
        print (nocache)
        return redirect('/webapp?nocache=' + nocache)

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0'"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    return r


# Main Application Loop
if __name__ == '__main__':

    # Ensure an empty files directory exists
    if not os.path.exists('files'):
        os.makedirs('files')

    # Let's go :)
    app.run(debug=True, host='0.0.0.0', port=config.appport())



