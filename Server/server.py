from flask import Flask
import numpy as np

app = Flask(__name__)

@app.route('/random')
def home():
    random = np.random.randint(10)
    return str(random)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)