from flask import Flask, request, make_response
import json

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return "UP"

@app.route('/test', methods=['POST'])
def example():
    try:
        # Read JSON data from the request body
        data = request.get_json()
        
        # Process the JSON data (you can print it for now to check if it's correct)
        print(json.dumps(data, indent=2))

        # Stub for PDF generation
        # Here you would generate a PDF using the data
        # For example, using a library like ReportLab or FPDF
        pdf_content = b'%PDF-1.4\n%...\n%%EOF'  # Dummy PDF content

        # Create a response with the PDF content
        response = make_response(pdf_content)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'attachment; filename="example.pdf"'

        return response

    except Exception as e:
        return {'error': str(e)}, 400

if __name__ == '__main__':
    app.run(debug=True)
