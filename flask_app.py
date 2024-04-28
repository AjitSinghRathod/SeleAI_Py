from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save_text():
    text = request.form['text']
    # Implement code to save the text
    return 'Text saved successfully'

@app.route('/clear', methods=['POST'])
def clear_text():
    # Implement code to clear the text
    return 'Text cleared successfully'

if __name__ == '__main__':
    app.run()