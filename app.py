from flask import Flask, request, Response
import predict
import time

app = Flask(__name__)


@app.route('/lips-to-text', methods=['POST'])
def lips_to_text():
    try:
        start = time.time()
        video = request.files.get("video")
        if video == None:
            return Response("No video received", status=400)

        vname = "video." + video.filename.split(".")[-1]

        start0 = time.time()
        video.save(vname)
        print("video saving ", time.time() - start0)

        result = predict.main(vname)
        print("request time ", time.time() - start)
        return Response(result)
    except Exception as e:
        msg = str(e)
        print('Exception : ' + msg)
        return Response(msg, status=400)


@app.route("/")
def index():
    return "<h1>LipsReaderAPI...Running<h1>";


if __name__ == "__main__":
    app.run(threaded=True)
