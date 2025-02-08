# 🎙️ AI-Powered Debate Assistant

An AI-driven debate assistant that generates structured arguments, counterarguments, and rebuttals for a given topic. Powered by Groq AI models and built with FastAPI (backend) & Streamlit (frontend).

🚀 Live Demo: Your Streamlit App URL

🛠️ Features

* ✅ AI-generated pro & con arguments
* ✅ AI-generated counterarguments & rebuttals
* ✅ FastAPI backend for argument generation
* ✅ Streamlit UI for user interaction
* ✅ Deployed on Streamlit Cloud & Render

📂 Project Structure

```bash
debate-assistant/
├── backend/
│   ├── main.py              # FastAPI backend  
│   ├── debate_generator.py  # Argument generation logic  
├── frontend/
│   ├── app.py               # Streamlit frontend  
├── requirements.txt         # Dependencies  
├── README.md                # Documentation  
└── .gitignore               # Ignore unnecessary files

```
🚀 Installation & Setup

1️⃣ Clone the Repository

```bash
git clone [https://github.com/MVenkatsai02/debate-assistant.git]
cd debate-assistant
```

2️⃣ Set Up a Virtual Environment and Activating the Envinorment

```bash
conda create -p venv python==3.10 -y # Windows
``` 

```bash
conda activate venv/
```

3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

🖥️ Running Locally

🔹 Start FastAPI Backend

```bash
uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload
```

Your API will be available at:

👉 http://localhost:8000/docs

🔹 Start Streamlit Frontend

Update app.py with your FastAPI backend URL, then run:

```bash
streamlit run frontend/app.py
```

Your UI will be available at:

👉 http://localhost:8501

🌍 Deployment

3️⃣ Deploy Backend (FastAPI) on Render

Push the backend folder to GitHub.
Go to Render.com → Create a New Web Service.
Connect to GitHub repo, select Python runtime.
Add environment variable:
```bash
GROQ_API_KEY = your-groq-api-key
```
Set Start Command:
```bash
uvicorn backend.main:app --host 0.0.0.0 --port 8000
```
Deploy Web service → Copy the API URL(Render).

4️⃣ Deploy Frontend (Streamlit) on Streamlit Cloud
Update app.py with the Render API URL
Push the frontend folder to GitHub.
Go to Streamlit Cloud → Click "Deploy an App".
Select GitHub repo → Set main file path to frontend/app.py.
Deploy and share your app link.

📌 Example Usage

Open the Streamlit UI.
Enter a debate topic (e.g., "Is AI good for humanity?").
Click "Generate Debate".
View AI-generated arguments & rebuttals.
🔧 Troubleshooting

💡 Issue: Streamlit App Not Connecting to Backend

✔️ Ensure app.py has the correct Render API URL.
✔️ Check Render logs for API errors.
💡 Issue: FastAPI Deployment Fails on Render

✔️ Add GROQ_API_KEY in Render environment variables.
✔️ Make sure requirements.txt is correctly installed.
🛡️ License

This project is open-source under the MIT License.

📩 Contact & Contributions

🔹 Feel free to fork this repo & contribute!
🔹 Found a bug? Create an issue on GitHub.
🔹 Questions? Reach out via venkatsaimacha123@gmail.com

🚀 Built with ❤️ using FastAPI, Streamlit & Groq AI 🚀

👉 https://aidebateassistant.streamlit.app





