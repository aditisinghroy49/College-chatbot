from flask import Flask, render_template, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
import os

app = Flask(__name__)

# Initialize the ChatBot
chatbot = ChatBot("CollegeBot")

# Train the chatbot with Dataset.txt if it exists
trainer = ListTrainer(chatbot)

if os.path.exists("Dataset.txt"):
    with open("Dataset.txt", "r") as f:
        conversation_data = f.readlines()
    trainer.train(conversation_data)
else:
    print("Dataset.txt not found. Please make sure it exists in the project folder.")

# You can also train with ChatterBot's prebuilt corpus if needed
corpus_trainer = ChatterBotCorpusTrainer(chatbot)
corpus_trainer.train("chatterbot.corpus.english")  # Optional, trains on a general English corpus

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html', title="Chatbot Home")

# Chat route to handle AJAX calls
@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        user_input = request.get_json().get('user_input')
        
        # Get response from the chatbot based on the user input
        bot_response = str(chatbot.get_response(user_input))
        
        return jsonify(response=bot_response)
    return render_template('chat.html', title="Chatbot")

if __name__ == "__main__":
    app.run(debug=True)

