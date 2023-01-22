from flask import Flask
import cohere
import os

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello World!</h1>"


@app.route("/item/")
def text_completion():
    co = cohere.Client("<api_key>")

    prompt = """ Given a post, this program will generate relevant hashtags.

    Post: Why are there no country songs about software engineering
    Hashtag: #softwareengineering
    --
    Post: Your soulmate is in the WeWork you decided not to go to
    Hashtag: #wework
    --
    Post: If shes talking to you once a day im sorry bro thats not flirting that standup
    Hashtag: #standup
    --
    Post: Going to unmute at the end of the Zoom meeting to say bye and realizing you were actually unmuted the whole call
    Hashtag: """

    response = co.generate(
        model="xlarge",
        prompt=prompt,
        max_tokens=10,
        temperature=0.5,
        k=0,
        p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop_sequences=["--"],
        return_likelihoods="NONE",
    )

    summary = f"Predictions: {response.generations[0].text.strip()}"
    return summary
