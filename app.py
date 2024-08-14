from flask import Flask, request, jsonify , render_template
import base64
import json
from google.generativeai import GenerativeModel
import google.generativeai as genai
from mistletoe import markdown

API_KEY = 'enter your gemini ai key here'
genai.configure(api_key=API_KEY)

model = 'gemini-1.0-pro'

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def generate():
    if request.method == 'POST':
        user_input = request.form['user_input']
       
        response = genai.text_generation(prompt=user_input)
      

    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate_response():
    if request.method == 'POST':
    
        user_input = request.form.get('user_input')

        try:
            gemini = GenerativeModel(model_name=model)
            chat = gemini.start_chat(history=[]) 
            response = chat.send_message(user_input)
            return render_template('index.html', response=(response.text))
        except Exception as e:
            print(f"Error generating response: {e}")
            return jsonify({'error': 'Failed to generate response'}), 500
        
    else:
        return render_template('index.html', response="")



if __name__ == '__main__':
    app.run(debug=True)
