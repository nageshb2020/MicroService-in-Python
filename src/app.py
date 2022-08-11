from flask import Flask,jsonify, render_template
import socket
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

def fetchdetails():
    hostname= socket.gethostname()
    host_ip= socket.gethostbyname(hostname)
    return str(hostname),str(host_ip)



@app.route("/health")
def health():
    return jsonify(
        status='up'
    )

@app.route("/details")
def details():
    hostname, ip=fetchdetails()
    return render_template('index.html', hostname=hostname, ip=ip)

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=5000)