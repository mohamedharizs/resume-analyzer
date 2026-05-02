from flask import Flask, render_template, request
import PyPDF2

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('resume')

    if not file:
        return render_template('index.html')

    try:
        reader = PyPDF2.PdfReader(file.stream)
        text = ""

        for page in reader.pages:
            if page.extract_text():
                text += page.extract_text()

        text = text.lower()

        missing = []
        suggestions = []

        checks = {
            "Projects section": ["project"],
            "Skills section": ["skills"],
            "Experience section": ["experience"],
            "Education section": ["education"],
            "Programming (Python/Java)": ["python", "java"]
        }

        for section, keys in checks.items():
            if not any(k in text for k in keys):
                missing.append(section)

        if "github" not in text:
            suggestions.append("Add GitHub or portfolio link")

        if "intern" not in text:
            suggestions.append("Add internships")

        if len(text) < 300:
            missing.append("Resume content too short")

        score = 100 - (len(missing) * 10 + len(suggestions) * 5)
        score = max(score, 40)

        if not missing:
            missing.append("No major sections missing (Good job!)")

        return render_template(
            'index.html',
            score=score,
            missing=missing,
            suggestions=suggestions
        )

    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)