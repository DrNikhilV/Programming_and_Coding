from flask import Flask, render_template, request
import g4f
import nest_asyncio

nest_asyncio.apply()

app = Flask(__name__)

g4f.debug.logging = True
g4f.debug.version_check = False 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/response', methods=['POST'])
def get_response():
    prompt = request.form['prompt']
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        stream=True,
    )
    # Iterate over the generator object and accumulate chat history
    chat_history = ''
    for message in response:
        if 'choices' in message and message['choices']:
            choice = message['choices'][0]
            if 'message' in choice and 'content' in choice['message']:
                chat_history += choice['message']['content']

    # Return the accumulated chat history
    return chat_history


if __name__ == '__main__':
    app.run(debug=True)
