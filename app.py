from flask import Flask, make_response
import sys
from sonda import sonda

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():

    sonda1 = sonda(1, 2, 'N')
    sonda2 = sonda(3, 3, 'E')

    sonda1.parse('LMLMLMLMM')
    sonda2.parse('MMRMMRMRRM')

    return str("Sonda1: " + str(sonda1.output()) + "\n" + "Sonda2: " + str(sonda2.output()))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
