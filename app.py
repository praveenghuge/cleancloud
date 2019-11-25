from flask import (
    Flask
)

tenant_id = ""
client_secret = ""
subscriptionid = ""
client_id = ""


app = Flask(__name__)




@app.route('/')
def home():
    return "Hello World"




if __name__ == "__main__":
    app.run(debug=True)
