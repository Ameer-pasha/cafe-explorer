# ☕ Cafe Explorer

A simple Flask web app to explore and add work-friendly cafes with features like Wi-Fi, power availability, seating, and more — visualized on an interactive map.

---

## 🧾 Project Structure

```bash
your-project-folder/
│
├── static/                  # Static files like CSS, JavaScript, images
│   ├── homepage.png         # Screenshot of the homepage
│   └── formpage.png         # Screenshot of the add cafe form
│
├── templates/               # HTML template files
│   ├── cafe_explorer.html   # Homepage with map and cafe list
│   ├── search_results.html  # Search results page
│   └── form.html            # Add cafe form page
│
├── cafes.db                 # SQLite database (auto-created, ignored in .gitignore)
├── main.py                  # Main Flask application file with routes and DB setup
├── .env                     # Environment config file (stores DATABASE_URL)
├── requirements.txt         # Project dependencies
└── .gitignore               # Git ignore rules


## 📦 Installation

1. **Clone the repo**  
```bash
git clone https://github.com/Ameer-pasha/cafe-explorer.git
cd cafe-explorer

## Run the app
python main.py

##🌐 Deployment
You can deploy this app on platforms like:
Render

##🛠️ Tech Stack
Frontend: HTML, Bootstrap 5, Leaflet
Backend: Python, Flask
Database: SQLite (via SQLAlchemy ORM)

🙋‍♂️ Author
👤 Ameer Pasha
🔗 github.com/Ameer-pasha

⭐ Acknowledgements
OpenStreetMap & Leaflet.js

Bootstrap 5

yaml
Copy code

---

### ✅ Steps to add:

1. Open your project folder.
2. Create a new file: `README.md`.
3. Paste the code above and **edit any personal details or screenshot URL**.
4. Save and commit:

```bash
git add README.md
git commit -m "Add README"
git push
