from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["1000 per minute"]
)

@app.route('/', methods=['GET'])
@limiter.limit("10 per second")
def index():
    return jsonify({"message": "Welcome to the server!"})

if __name__ == '__main__':
    app.run(debug=True)
