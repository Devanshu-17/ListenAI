from flask import Flask, render_template, request
from dotenv import load_dotenv
from backend.api import api  # Import your api blueprint
from backend.wbot import GPT
from twilio.twiml.messaging_response import MessagingResponse


load_dotenv()

def create_app():
    app = Flask(__name__)

    with app.app_context():
        app.register_blueprint(api, url_prefix="/home/api")  # Register the api blueprint

        @app.route("/")  # Add this route for the root URL
        def index():
            return render_template("index.html")
        


        @app.route("/chatbot", methods=["POST"])
        def chatbot():

            chat_model = GPT(str(request.values.get("WaId", "")))
            incoming_msg = request.values.get("Body", "")
            answer = chat_model.bot(incoming_msg)
            resp = MessagingResponse()
            msg = resp.message()
            msg.body(answer)

            return str(resp)

        @app.after_request
        def after_request(response):
            request.get_data()
            return response

    return app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
