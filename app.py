from flask import Flask, render_template_string

app = Flask(__name__)

PAGE = """
<!doctype html>
<html>
  <body>

    <h1>This is the POC #100000000</h1>

    <a href="/static/imran.html">Click here</a><br>
    <a href="/static/test00.html">Click here also</a>

    <p>It's a very simple PoC that doesn't require a diploma to do it.</p>

  </body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(PAGE)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
