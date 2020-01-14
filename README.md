# file-generator
Creates files on the Fly, Flask API

Allows the creation of files on demand for testing web proxies, or email policy.

## Installation

Clone this repository using:

<pre>
$ git clone https://github.com/daemonchild/file-generator.git
</pre>

Generate a virtual environment:
<pre>
$ cd file-generator
$ virtualenv -p python3 venv
</pre>

Activate the virtual environment:

<pre>
$ . venv\bin\activate
</pre>

Install the required python packages:
<pre>
$ pip install -r requirements.txt
</pre>

## Start the API

Install the required python packages:
<pre>
$ python3 file-generator-api.py
</pre>

NB: By default, the app runs on port 9000. This can be changed in config.py.

# Web App

The API includes a simple web app that generates a file and downloads it via the web browser. 

<pre>http://[your-ip]/webapp</pre>

This allows simple testing of web proxy policies.

The real power of the API is more apparent when it is called directly. I would recommend that you develop your own calling scripts; some examples have been included in the 'example-clients' folder.


