import os
from flask import Flask, redirect
from logging import Logger, basicConfig

basicConfig(level=os.environ.get("LOG_LEVEL", "INFO"))
logger = Logger(__name__)

app = Flask(__name__)

@app.route('/')
def index():
    logger.info("Visitor")
    return redirect(os.environ.get("TARGET","http://example.org"), code=302)

@app.route('/health')
def health():
    logger.info("Health Check")
    return "Healthy"

if __name__ == '__main__' and os.environ.get("DEBUG",False):
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)