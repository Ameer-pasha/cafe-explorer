# ☕ Cafe Explorer

**Cafe Explorer** is a Flask-based web application that helps users find work and study-friendly cafes in London. It includes an interactive map, search functionality, and the ability to add new cafes to the database.

---

## 📸 Preview

> Find cafes with WiFi, sockets, toilets, and a good environment to work in — all displayed beautifully!

![Cafe Explorer Screenshot](https://via.placeholder.com/800x400?text=Screenshot+Preview)

---

## 🚀 Features

- 🔍 **Search cafes** by location
- 🗺️ **Interactive map** (via Leaflet + OpenStreetMap)
- ✅ View cafe amenities like WiFi, sockets, toilets, etc.
- ➕ **Add new cafes** through a simple form
- 💾 Powered by SQLite and Flask backend

---

## 🧾 Project Structure

your-project-folder/ 
│
├── templates/           # HTML template files (cafe_explorer, search_results, form)
│   ├── cafe_explorer.html    # Homepage with map and cafe list
│   ├── search_results.html   # Search results page
│   └── form.html             # Add cafe form page
│
├── cafes.db             # SQLite database file (auto-created)
├── main.py              # Main Flask application file with routes and DB setup


---

## 📦 Installation

1. **Clone the repo**  
```bash
git clone https://github.com/Ameer-pasha/cafe-explorer.git
cd cafe-explorer

## Run the app
bash
Copy code
python main.py

🌐 Deployment
You can deploy this app on platforms like:
Render

🛠️ Tech Stack
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
