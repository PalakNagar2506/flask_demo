from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string("""
    <h1>Hello Flask 👋</h1>
    <p>This is a simple Flask app.</p>
    """)

if __name__ == "__main__":
    app.run(debug=True)
