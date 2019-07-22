from flask import Flask, request, Response
import predict
import time

app = Flask(__name__)


@app.route('/lips-to-text', methods=['POST'])
def lips_to_text():
    start = time.time()
    video = request.files.get("video")
    if video == None:
        return Response("No video received", status=400)

    vname = "video." + video.filename.split(".")[-1]
    video.save(vname)
    result = predict.main(vname)
    print("request time ", time.time() - start)
    return Response(result)


@app.route("/")
def index():
    return "<h1>LipsReaderAPI...Running<h1>";


if __name__ == "__main__":
    app.run(threaded=True)
