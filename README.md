# 🚀 Resume Analyzer (AI-powered)

🔗 Live Demo: https://resume-analyzer-k716.onrender.com

---

## 📌 Overview

Resume Analyzer is a web-based application built using **Python Flask** that helps users evaluate and improve their resumes. The application analyzes uploaded PDF resumes, assigns a score, identifies missing sections, and provides actionable suggestions to enhance resume quality.

This project simulates an **AI-powered resume review system** by combining text extraction, keyword analysis, and dynamic feedback generation.

---

## 🎯 Features

* 📄 Upload Resume (PDF format)
* 🔍 Extract text using PyPDF2
* 📊 Resume scoring system (out of 100)
* ❌ Detect missing sections:

  * Projects
  * Skills
  * Experience
  * Education
  * Programming knowledge
* 💡 Smart suggestions:

  * Add GitHub/portfolio links
  * Include internships
  * Improve content length
* 📉 Detect weak resumes (short content)
* 🎨 Modern UI with teal theme
* 🌐 Fully deployed web app

---

## 🧠 How It Works

1. User uploads a resume (PDF)
2. The backend extracts text using **PyPDF2**
3. Text is analyzed for key sections and keywords
4. A scoring algorithm calculates resume strength
5. Missing elements are identified
6. Suggestions are generated dynamically
7. Results are displayed in a clean UI

---

## ⚙️ Tech Stack

* **Backend:** Python, Flask
* **Frontend:** HTML, CSS (Jinja templating)
* **PDF Processing:** PyPDF2
* **Deployment:** Render
* **Version Control:** GitHub

---

## 📊 Scoring Logic

* Base score starts at 100
* Points deducted for:

  * Missing sections
  * Lack of important keywords
  * Short content length
* Minimum score capped to ensure usability

---

## 🎨 UI Design

* Clean, modern layout
* Teal gradient theme
* Responsive sections:

  * Hero (Upload + Analyze)
  * Score display
  * Missing sections
  * Suggestions
  * Resume importance section
  * Sample resumes

---

## 💡 Key Highlights

* Real-time resume analysis
* Beginner-friendly AI simulation
* Practical use-case project
* Clean UI + functional backend
* Deployable and scalable

---

## 🚀 Deployment

The app is deployed using **Render** and is accessible via:

👉 https://resume-analyzer-k716.onrender.com

---

## 📁 Project Structure

resume-analyzer/
│── app.py
│── requirements.txt
│── templates/
│     └── index.html
│── static/
│     └── style.css

---

## 🔮 Future Improvements

* 🤖 Real AI integration (OpenAI API)
* 📄 Support for DOCX files
* 🎯 Job-role based scoring
* 📊 ATS keyword matching
* 👤 User login & saved resumes
* 📈 Resume improvement tracking

---

## 🙌 Conclusion

Resume Analyzer acts as a **smart assistant for job seekers**, helping them identify weaknesses in their resumes and improve their chances of getting shortlisted by recruiters.

---

⭐ If you like this project, give it a star!
