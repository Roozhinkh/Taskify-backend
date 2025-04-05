# ✅ Taskify – Enkel uppgiftshantering

## 🧩 Projektbeskrivning

**Taskify** är en webbaserad applikation för uppgiftshantering där användare kan skapa, uppdatera och ta bort sina uppgifter. Applikationen består av ett React-baserat gränssnitt (frontend) och ett Flask-baserat REST API (backend). Den är byggd med enkelhet i fokus – utan användarinloggning – för att snabbt och smidigt hantera sina "to-dos".

---

## ⚙️ Installation och Start

### 🛠 Förkrav

- [Node.js](https://nodejs.org/)
- [Python 3.x](https://www.python.org/)
- [MySQL Server](https://dev.mysql.com/)
- [pip](https://pip.pypa.io/)
- [Git](https://git-scm.com/)

---

### 📥 Steg-för-steg Guide

#### 1. Klona projektet

```bash
git clone https://github.com/Roozhinkh/Taskify-frontend.git
git clone https://github.com/Roozhinkh/Taskify-backend.git
```

---

#### 2. Starta backend

```bash
cd Taskify-backend
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Skapa en `.env`-fil i projektroten med följande innehåll (anpassa efter din databas):

```env
DATABASE_URL=mysql+pymysql://<användare>:<lösenord>@localhost/<databasnamn>
```

Installera MySQL-drivrutinen:
```bash
pip install pymysql
```

Starta backend-servern:
```bash
python app.py
```

Backend körs på: `http://localhost:5000`

---

#### 3. Starta frontend

```bash
cd ../Taskify-frontend
npm install
npm start
```

Frontend körs på: `http://localhost:3000`

---

### 📦 Beroenden

#### Python (från `requirements.txt`)

- Flask  
- Flask-Cors  
- SQLAlchemy  
- PyMySQL  

> Installera med:
```bash
pip install -r requirements.txt
```

#### Node (från `package.json`)

- React  
- Axios  
- React Router  

> Installera med:
```bash
npm install
```

---

## 🎨 Grafisk Profil

### Färgpalett

| Typ         | Färgkod     |
|-------------|-------------|
| Primär      | `#3498db`   |
| Sekundär    | `#2ecc71`   |
| Bakgrund    | `#f4f4f4`   |
| Text        | `#2c3e50`   |

### Typsnitt

- **Primärt:** Roboto  
- **Sekundärt:** Open Sans

### Designprinciper

- Enkel och intuitiv användarupplevelse  
- Responsiv layout  
- Tydlig färgkontrast för tillgänglighet  
- Ikoner och visuella statusindikatorer för uppgifter

---

## 🌿 Branchstruktur

Vi följer ett enkelt men effektivt Git-workflow:

| Branch         | Beskrivning                                |
|----------------|---------------------------------------------|
| `main`         | Stabil, produktionsklar kod                |
| `dev`          | Samlingspunkt för aktiv utveckling         |
| `feature/*`    | Funktionella brancher per ny feature       |

- Nya features utvecklas i `feature/[namn]`
- PRs skickas till `dev`
- `main` uppdateras endast med testad och godkänd kod

---

## 🗄️ Databasstruktur (MySQL)

Projektet använder **MySQL** för lagring av uppgifter. Backend ansluter till databasen via SQLAlchemy och PyMySQL.

### Anslutningsexempel (i `.env`):

```env
DATABASE_URL=mysql+pymysql://root:password@localhost/taskify
```

Se till att databasen `taskify` är skapad i din MySQL-server.

---

### 📋 Tasks-tabellen

| Fält        | Typ        | Beskrivning                        |
|-------------|------------|------------------------------------|
| `id`        | INT (PK)   | Unikt ID för varje uppgift         |
| `title`     | VARCHAR    | Uppgiftens titel                   |
| `description` | TEXT     | Beskrivning av uppgiften           |
| `status`    | VARCHAR    | Status, t.ex. `todo`, `done`       |
| `created_at`| DATETIME   | Tidsstämpel för när uppgiften skapades |

> Tabellen skapas automatiskt via ORM, eller kan skapas manuellt via SQL.

---

### HTTP-Requests

post_task(): - POST - Roozhin
get_task(task_id): - GET - Abdelrahman
get_tasks(): - GET - Roozhin
put_task(task_id): - PUT - Diana
remove_task(task_id): - DELETE - Diana
search_by_deadline(): - GET - Alvin
search_task_by_title(): - GET - Abdelrahman
completed_task(task_id): - PATCH - Alvin