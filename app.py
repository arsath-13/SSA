from application import app
from application.securefiles.secretkey import SESSION_ENABLE_KEY

if __name__ == "__main__":
    app.run(debug = True)

