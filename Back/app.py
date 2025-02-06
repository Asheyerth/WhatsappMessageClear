from src import create_app
from flask_cors import CORS

app = create_app()
CORS(app, support_credentials=True)
port = 5000  # Puerto por defecto

if __name__ == '__main__':
    app.run(debug=True, port=port)