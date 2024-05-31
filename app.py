import os
from flask import Flask, request, jsonify, Response, stream_with_context
from flask_cors import CORS
from helpers import ...

app = ...

CORS(..., resources={
     r"/*": {"origins": ["..."]
             }
     })


@app.route("/")
def index():
    return ...({
        "status": {
            "code": ...,
            "message": "Success fetching the API",
        },
        "data": ...,
    }), 200


@app.route("/...", methods=["...", "..."])
def generate_text():
    if request.method == "...":
        input_data = request....()
        prompt = input_data["..."]

        model = genai.GenerativeModel(
            model_name="...",
        )

        text_result = model.generate_content(...)

        return jsonify({
            "status": {
                "code": 200,
                "message": "Success generate text",
            },
            "data": {
                "result": ...,
            }
        }), 200
    else:
        return jsonify({
            "status": {
                "code": 405,
                "message": "Method not allowed"
            },
            "data": None,
        }), 405


@app.route("/...", methods=["GET", "POST"])
def generate_text_stream():
    if request.method == "POST":
        input_data = request.get_json()
        prompt = input_data["..."]
        model = genai....(model_name="gemini-pro")

        def generate_stream():
            response = model.generate_content(prompt, ...=True)
            for chunk in ...:
                print(chunk.text)
                yield chunk.text + "\n"

        return Response(stream_with_context(...()), mimetype="text/plain")
    else:
        return jsonify({
            "status": {
                "code": 405,
                "message": "Method not allowed"
            },
            "data": None
        }), 405


if __name__ == "__main__":
    app.run(debug=True,
            host="...",
            port=int(os.environ.get("PORT", ...)))
