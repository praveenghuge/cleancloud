from flask import (
    Flask
)

tenant_id = "eff7f985-dc58-4935-a906-050609be85c3"
client_secret = "V+obVteoP+Y738u9bcOb7XP60ELdB2f15j524sM3MQA="
subscriptionid = "64caccf3-b508-41e7-92ed-d7ed95b32621"
client_id = "541ac203-1433-4eef-b965-54bccc293f8e"


app = Flask(__name__)




@app.route('/')
def home():
    return "Hello World"




if __name__ == "__main__":
    app.run(debug=True)