import requests
from datetime import datetime
import random

def get_wordle_data():
    date_str = datetime.now().strftime("%Y-%m-%d")
    url = f"https://www.nytimes.com/svc/wordle/v2/{date_str}.json"
    try:
        data = requests.get(url).json()
        return data['solution'].upper()
    except:
        return "Check back soon!"

def get_connections_data():
    url = "https://www.nytimes.com/svc/connections/v2/today.json"
    try:
        return requests.get(url).json()
    except:
        return None

def generate_page():
    wordle = get_wordle_data()
    conn_data = get_connections_data()
    date_pretty = datetime.now().strftime('%B %d, 2026')
    
    # SEO Text to please Google Ads
    vowels = sum(1 for char in wordle if char in "AEIOU")
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>NYT Games Answers Today - {date_pretty}</title>
        <style>
            body {{ font-family: sans-serif; line-height: 1.6; max-width: 700px; margin: auto; padding: 20px; background: #f4f4f4; }}
            .card {{ background: white; padding: 20px; margin-bottom: 20px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }}
            .ans {{ display: none; background: #333; color: #fff; padding: 10px; margin-top: 10px; font-weight: bold; text-align: center; }}
            button {{ background: #007bff; color: white; border: none; padding: 10px; cursor: pointer; border-radius: 4px; }}
            .ad-box {{ background: #eee; border: 1px solid #ddd; height: 100px; margin: 20px 0; text-align: center; line-height: 100px; color: #888; }}
        </style>
    </head>
    <body>
        <h1>NYT Hints & Answers: {date_pretty}</h1>
        
        <div class="ad-box">AD UNIT 1</div>

        <div class="card">
            <h2>Wordle Hint</h2>
            <p>Today's word starts with <strong>{wordle[0]}</strong> and has <strong>{vowels}</strong> vowels.</p>
            <button onclick="document.getElementById('w').style.display='block'">Show Answer</button>
            <div id="w" class="ans">{wordle}</div>
        </div>

        <div class="ad-box">AD UNIT 2</div>

        <div class="card">
            <h2>Connections Answers</h2>
            <p>The categories for today are focused on general knowledge and wordplay.</p>
            <button onclick="document.getElementById('c').style.display='block'">Show All Groups</button>
            <div id="c" class="ans">
                {"".join([f"<p>{cat['title']}: {', '.join(cat['cards'])}</p>" for cat in conn_data['categories']]) if conn_data else "Loading..."}
            </div>
        </div>

        <div class="card">
            <h2>About NYT Games</h2>
            <p>Wordle and Connections are daily puzzles released by the New York Times. We provide daily hints to help you keep your streak alive without spoiling the fun immediately!</p>
        </div>

        <div class="ad-box">AD UNIT 3</div>

        <footer><p>&copy; 2026 Game Solvers | <a href="privacy.html">Privacy Policy</a></p></footer>
    </body>
    </html>
    """
    with open("index.html", "w") as f:
        f.write(html_content)

if __name__ == "__main__":
    generate_page()
