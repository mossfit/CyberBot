from flask import Flask, render_template, request
from agents import advisory_agent, start_agents, vector_db

app = Flask(__name__)

# Start background data collection
start_agents()

@app.route("/", methods=["GET", "POST"])
def index():
    advisory = None
    query = None
    if request.method == "POST":
        query = request.form.get("query")
        if query:
            advisory = advisory_agent(query)
    # Display the 5 most recent entries as the threat dashboard
    recent_entries = vector_db.metadata[-5:] if vector_db and vector_db.metadata else []
    return render_template("index.html", advisory=advisory, query=query, recent_entries=recent_entries)

if __name__ == "__main__":
    app.run(debug=True)
