```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/dm_journal")
def dm_journal():
    return render_template("dm_journal.html")
```