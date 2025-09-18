from flask import Flask, jsonify
import os
import json

app = Flask(__name__)

CONFIG_PATH = "/config/config.json"
config_data = {}

def load_config():
    global config_data
    try:
        with open(CONFIG_PATH, "r") as f:
            config_data = json.load(f)
        print("Config reloaded:", config_data)
    except Exception as e:
        print("Failed to load config", e)


@app.route('/')
def home():
    load_config()
    return jsonify(config_data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)