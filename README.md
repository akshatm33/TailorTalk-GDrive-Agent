# TailorTalk Google Drive AI Agent

An AI-powered Google Drive assistant built using:

* FastAPI
* Streamlit
* LangChain
* OpenAI
* Google Drive API

The project allows users to search Google Drive files using natural language queries.

---

# Features

* Conversational AI search for Google Drive
* Search PDFs, images, spreadsheets, docs, etc.
* Search files by:

  * file name
  * file type
  * keywords
  * content
* FastAPI backend
* Streamlit frontend
* Google Drive API integration
* LangChain AI agent

---

# Tech Stack

## Backend

* FastAPI
* LangChain
* OpenAI API
* Google Drive API
* Python

## Frontend

* Streamlit

---

# Project Structure

```bash
TailorTalk-GDrive-Agent/
│
├── backend/
│   ├── app.py
│   ├── agent.py
│   ├── drive_service.py
│   ├── tools.py
│   ├── prompts.py
│   ├── requirements.txt
│   ├── .env
│   └── service_account.json
│
├── frontend/
│   └── streamlit_app.py
│
└── README.md
```

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/TailorTalk-GDrive-Agent.git
cd TailorTalk-GDrive-Agent
```

---

# 2. Create Virtual Environment

## Windows

```bash
py -3.11 -m venv venv
```

Activate environment:

```bash
venv\Scripts\Activate.ps1
```

---

# 3. Install Backend Dependencies

Go into backend folder:

```bash
cd backend
```

Install packages:

```bash
python -m pip install -r requirements.txt
```

---

# 4. Configure Google Drive API

## Create Google Cloud Project

1. Open Google Cloud Console
2. Create a new project
3. Enable Google Drive API
4. Create Service Account
5. Generate JSON credentials

Download the credentials file and rename it to:

```bash
service_account.json
```

Place it inside:

```bash
backend/
```

---

# 5. Share Google Drive Folder

Create a Google Drive folder and upload test files.

Share the folder with your service account email.

Give Viewer access.

Copy the folder ID from the URL.

Example:

```bash
https://drive.google.com/drive/folders/1ABCxyz123
```

Folder ID:

```bash
1ABCxyz123
```

---

# 6. Configure Environment Variables

## Credentials Required

Before running the project, configure the following credentials:

* OpenAI API Key
* Google Drive Folder ID
* Google Service Account JSON credentials

Place the Google service account credentials file inside:

```bash
backend/service_account.json
```

The `.env` file should contain:

```env
OPENAI_API_KEY=your_openai_api_key
GOOGLE_DRIVE_FOLDER_ID=your_folder_id
```

IMPORTANT:

* Do not commit real API keys to GitHub
* Do not upload real service account credentials publicly
* Use placeholder values when sharing the project

---

# 6. Configure Environment Variables

Create a `.env` file inside backend folder.

Example:

```env
OPENAI_API_KEY=your_openai_api_key
GOOGLE_DRIVE_FOLDER_ID=your_folder_id
```

---

# 7. Run Backend Server

Inside backend folder:

```bash
python -m uvicorn app:app --reload
```

Backend runs at:

```bash
http://127.0.0.1:8000
```

Swagger Docs:

```bash
http://127.0.0.1:8000/docs
```

---

# 8. Run Frontend

Open another terminal.

Go into frontend folder:

```bash
cd frontend
```

Install Streamlit:

```bash
python -m pip install streamlit requests
```

Run frontend:

```bash
python -m streamlit run streamlit_app.py
```

Frontend runs at:

```bash
http://localhost:8501
```

---

# Example Queries

Users can ask:

```bash
Find PDF files
```

```bash
Find spreadsheets
```

```bash
Find files related to finance
```

```bash
Find images
```

```bash
Find report documents
```

---

# Supported File Types

| File Type     | MIME Type                                |
| ------------- | ---------------------------------------- |
| PDF           | application/pdf                          |
| Google Docs   | application/vnd.google-apps.document     |
| Google Sheets | application/vnd.google-apps.spreadsheet  |
| Google Slides | application/vnd.google-apps.presentation |
| Images        | image/jpeg, image/png                    |

---

# Deployment

## Backend Deployment (Render)

1. Push project to GitHub
2. Create Render Web Service
3. Root Directory:

```bash
backend
```

4. Build Command:

```bash
pip install -r requirements.txt
```

5. Start Command:

```bash
python -m uvicorn app:app --host 0.0.0.0 --port 10000
```

6. Add environment variables:

* OPENAI_API_KEY
* GOOGLE_DRIVE_FOLDER_ID

---

# Challenges Faced

* LangChain version compatibility issues
* Python 3.14 package incompatibility
* OpenAI SDK version conflicts
* Streamlit and Uvicorn PATH issues
* Google Drive authentication setup

---

# Future Improvements

* File preview support
* Semantic vector search
* Multi-user authentication
* Chat history
* Better UI/UX
* Upload files directly from UI

---

# Author

Akshat Maheshwari

---
