from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/word', methods=['POST'])
def word_count():
    data = request.get_json()

    # Validate input
    if not data or 'text' not in data:
        return jsonify({'error': 'Missing "text" in request body'}), 400

    text = data['text']
    word_count = len(text.split())

    return jsonify({'word_count': word_count})

if __name__ == '__main__':
    app.run(debug=True)
