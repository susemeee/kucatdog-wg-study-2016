from app import app

debug = True
DEFAULT_PORT = 5000

if __name__ == '__main__':
    app.run(debug=debug, port=DEFAULT_PORT)
