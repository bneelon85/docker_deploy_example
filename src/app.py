from flask import Flask, jsonify, request

# initialize our Flask application
app= Flask(__name__)
@app.route("/post-to-me", methods=["POST"])
def postMessageBack():
    if request.method=='POST':
        posted_data = str(request.get_json())
        return jsonify("You sent {}".format(posted_data))

#  main thread of execution to start the server
if __name__=='__main__':
    from waitress import serve
    serve(app, host='0.0.0.0', port=80)