```python
from flask import Flask, render_template
from shared_dependencies.exported_variables import npc_list

app = Flask(__name__)

@app.route("/npc_cradle")
def npc_cradle():
    return render_template("npc_cradle.html", npc_list=npc_list)

if __name__ == "__main__":
    app.run(debug=True)
```