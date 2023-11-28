```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/the_grimoire")
def the_grimoire():
    return render_template("the_grimoire.html")

if __name__ == "__main__":
    app.run(debug=True)
```