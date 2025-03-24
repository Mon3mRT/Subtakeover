from flask import Flask, request, redirect

app = Flask(__name__)

@app.route("/")
def log_request():
    target = request.args.get("url")
    if target:
        print(f"Received request with URL: {target}")
        return redirect(target)  # This creates an open redirect
    return "Use ?url= to test redirects."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
