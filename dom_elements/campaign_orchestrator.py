```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/campaign_orchestrator")
def campaign_orchestrator():
    return render_template("campaign_orchestrator.html")

if __name__ == "__main__":
    app.run(debug=True)
```