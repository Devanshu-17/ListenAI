## Tasks to Do:

-   [x] Utilize Flask, a web framework for Python, to develop the backend infrastructure of the chatbot.

-   [x] Incorporate OpenAI GPT or a similar NLP API to understand and respond effectively to user queries.

[LLAMA 2, OPENAI GPT] – SELECT A MODEL & {FINETUNE} IT USING IBM CLOUD GPU {WATSON}

[Use Qdrant for vector embeddings]

Dataset: - https://www.kaggle.com/datasets/meetnagadia/district-wise-mental-health-patients-20212022

-   [x] Integrate the WhatsApp API to enable seamless message communication between users and the chatbot.

[Twilio – WHATSAPP]

-   [x] Implement sentiment analysis API to extract emotional insights from conversations, enabling the chatbot to provide empathetic and personalized support.

[Using COHERE LLM]

-   [x] Utilize Twilio API for sending SMS or phone notifications to support staff in high-risk situations.

[TWILIO - Whatsapp Integration]

## Resouces:

-   https://python.langchain.com/docs/get_started/introduction.html
-   https://docs.cohere.com/reference/sentiment-analysis
-   https://github.com/DanteNoguez/FlaskGPT
-   https://www.trychroma.com/
-   https://dev.to/rowy
-   https://medium.com/@ritikkhndelwal/creating-webhooks-using-python-flask-and-ngrok-for-instagram-messenger-api-6d595012ed79

## WORKFLOW:

![Workflow](https://github.com/Devanshu-17/Listener-AI/assets/93381397/13cc928d-9e37-4520-8619-183ab81e3e5d)

## How to run the project:

You can run the project by either using the docker image or by cloning the repository and running it locally.

### Using Docker:

#### Build the docker image

```bash
docker build -t listenai .
```

#### Set the environment variables

Rename the .env.example file to .env and set the environment variables.

#### Run the docker image

```bash
docker run -it -p 5000:5000 listenai:latest
```

### Locally:

#### Clone the repository

```bash
git clone https://github.com/smartinternz02/SBSPS-Challenge-10019-LISTNER---AI-based-Life-Assistance-Chatbot-Integration-for-public-welfare.git
```

#### Install the requirements

```bash
pip install -r requirements.txt
```

#### Set the environment variables

Rename the .env.example file to .env and set the environment variables.

#### Run the app

```bash
python app.py
```
