from flask import Flask
from flask import jsonify
from flask import request
app = Flask(__name__)

import pickle
with open("model.pickle",'r') as f:
    clf2 = pickle.load(f)

with open("labels.pickle",'r') as f:
    le = pickle.load(f)


@app.route("/", methods=['POST'])
def suggest():
    content = request.get_json(silent=True)
    synopsis = content[u"synopsis"]
    predicted = clf2.predict([synopsis])
    # return jsonify(content)
    #
    return jsonify({"synopsis": synopsis, "suggested": le.inverse_transform(predicted[0])})
