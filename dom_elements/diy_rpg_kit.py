```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/diy_rpg_kit")
def diy_rpg_kit():
    return render_template("diy_rpg_kit.html")
```