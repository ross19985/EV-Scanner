from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="UK EV Planning Finder")


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <title>UK EV Planning Finder</title>

        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 900px;
                margin: 0 auto;
                padding: 40px 20px;
                background: #f5f7fa;
                color: #222;
            }

            .container {
                background: white;
                padding: 35px;
                border-radius: 12px;
                box-shadow: 0 2px 12px rgba(0,0,0,0.08);
            }

            h1 {
                margin-top: 0;
            }

            .search-box {
                display: flex;
                gap: 10px;
                flex-wrap: wrap;
                margin-top: 25px;
            }

            input, select, button {
                padding: 13px;
                font-size: 16px;
                border: 1px solid #ccc;
                border-radius: 6px;
            }

            input {
                flex: 1;
                min-width: 200px;
            }

            button {
                cursor: pointer;
                background: #222;
                color: white;
            }

            .message {
                margin-top: 30px;
                padding: 20px;
                background: #f1f3f5;
                border-radius: 8px;
            }
        </style>
    </head>

    <body>

        <div class="container">

            <h1>UK EV Planning Finder</h1>

            <p>
                Search planning applications relating to
                electric vehicle charging infrastructure.
            </p>

            <div class="search-box">

                <input
                    id="postcode"
                    type="text"
                    placeholder="Enter postcode e.g. NE1 4LP"
                >

                <select id="radius">
                    <option value="1">1 mile</option>
                    <option value="5" selected>5 miles</option>
                    <option value="10">10 miles</option>
                    <option value="25">25 miles</option>
                    <option value="50">50 miles</option>
                </select>

                <button onclick="search()">
                    Search
                </button>

            </div>

            <div id="results" class="message">
                Enter a postcode and click Search.
            </div>

        </div>


        <script>

            function search() {

                const postcode =
                    document.getElementById("postcode").value;

                const radius =
                    document.getElementById("radius").value;

                if (!postcode) {

                    document.getElementById("results").innerHTML =
                        "Please enter a postcode.";

                    return;
                }

                document.getElementById("results").innerHTML =
                    `
                    <strong>Search received</strong>
                    <p>
                        Postcode: ${postcode.toUpperCase()}
                    </p>
                    <p>
                        Radius: ${radius} miles
                    </p>
                    <p>
                        The planning database will be connected
                        in the next stage.
                    </p>
                    `;

            }

        </script>

    </body>
    </html>
    """
