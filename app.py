from flask import Flask, request, Response

app = Flask(__name__)



@app.route("/")
def hello():
    user = request.args.get('user')
    password = request.args.get('password')
    if (user=='atlanticomedio') and(password== '1234' ):
        return "ok"
    else:
        return "ko"

if __name__ == '__main__':
     app.run(port='5000')
