## Tasks:

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


## IMPLEMENTATION:

<br />

<img width="1728" alt="Home" src="https://github.com/smartinternz02/SBSPS-Challenge-10019-LISTNER---AI-based-Life-Assistance-Chatbot-Integration-for-public-welfare/assets/93381397/8e3017dc-776b-4a8f-bfa8-986b9c3404d8">

<p align="center">
  <br />
  <a><b> Fig 1.1 Home Page</b></a>
</p>


<img width="1728" alt="Chat" src="https://github.com/smartinternz02/SBSPS-Challenge-10019-LISTNER---AI-based-Life-Assistance-Chatbot-Integration-for-public-welfare/assets/93381397/38b302a2-4706-490d-9ae4-c22465d1fda3">

<p align="center">
  <br />
  <a><b> Fig 1.2 Chat Page</b></a>
</p>

<img width="1672" alt="Whatsapp" src="https://github.com/smartinternz02/SBSPS-Challenge-10019-LISTNER---AI-based-Life-Assistance-Chatbot-Integration-for-public-welfare/assets/93381397/4b591294-4bca-44de-ab38-5499c3a59f8e">

<p align="center">
  <br />
  <a><b> Fig 1.3 Whatsapp Bot Page</b></a>
</p>


## Resouces:

-   https://python.langchain.com/docs/get_started/introduction.html
-   https://docs.cohere.com/reference/sentiment-analysis
-   https://github.com/DanteNoguez/FlaskGPT
-   https://www.trychroma.com/
-   https://dev.to/rowy
-   https://medium.com/@ritikkhndelwal/creating-webhooks-using-python-flask-and-ngrok-for-instagram-messenger-api-6d595012ed79

## WORKFLOW:

![image](https://github.com/smartinternz02/SBSPS-Challenge-10019-LISTNER---AI-based-Life-Assistance-Chatbot-Integration-for-public-welfare/assets/93381397/056e0ae3-98a9-4914-b22a-625d292faad1)


## FLOWCHART

![image](https://github.com/smartinternz02/SBSPS-Challenge-10019-LISTNER---AI-based-Life-Assistance-Chatbot-Integration-for-public-welfare/assets/93381397/f9a5199f-8a0a-4b47-9c46-f57a7e3b26a9)


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
