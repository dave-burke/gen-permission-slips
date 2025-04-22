from flask import Flask, request, make_response
from flask_cors import CORS
from make_pdf import make_pdf
import yaml
import json

app = Flask(__name__)

CORS(app)

@app.route('/health', methods=['GET'])
def health():
    return "UP"

@app.route('/pdf', methods=['POST'])
def pdf():
    try:
        # Read JSON data from the request body
        data = request.get_json()

        # Process the JSON data (you can print it for now to check if it's correct)
        print(json.dumps(data, indent=2))

        with open('template.html', 'r') as f:
            template_content = f.read()

        pdf_content = make_pdf(template_content, data)

        # Create a response with the PDF content
        response = make_response(pdf_content)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'attachment; filename="permission-slip.pdf"'

        return response

    except Exception as e:
        return {'error': str(e)}, 400

if __name__ == '__main__':
    app.run(debug=True)
