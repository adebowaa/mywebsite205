from flask import Flask, send_from_directory
app = Flask(__name__);

@app.route('/')
def send_205cde():
    return app.send_205cde_file('ChampionsLeague.html')

@app.route('/<path:path>')
def send_205cde2(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run()
    
    
    