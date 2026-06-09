import os
from flask import Flask, request

app = Flask(__name__)

GMAIL_ID = "ameenullahkhaninayti@gmail.com"
PHONE_NUMBER = "9068495437"

@app.route("/", methods=["GET", "POST"])
def home():
    current_tab = request.args.get("tab", "home")
    assessment_submitted, contact_submitted = False, False
    name, age, eligibility_html, program_title, program_details, next_action_steps = "", 0, "", "", "", ""

    if request.method == "POST":
        form_type = request.form.get("form_identity")
        if form_type == "assessment":
            assessment_submitted = True
            name = request.form.get("username", "")
            age = int(request.form.get("userage") or 0)
            user_choice = request.form.get("choice", "")
            eligibility_html = "<p style='color: #28a745;'><strong>Status:</strong> Approved.</p>" if age >= 18 else "<p style='color: #856404;'>Minor track.</p>"
            
            # Logic mapping
            paths = {
                "A": ("Career Resolution", "Analyze your core skill profile.", "<li>Check email for worksheet.</li>"),
                "B": ("Academic Strategy", "Optimize curricular paths.", "<li>Webinar access sent.</li>"),
                "D": ("Psychological Track", "Confidential support.", "<li>Ping a counselor.</li>"),
                "E": ("Startup Advisory", "MVP and Lean Canvas.", "<li>Download Blueprint.</li>")
            }
            res = paths.get(user_choice, ("General Exploration", "Mapping trends.", "<li>Review sector.</li>"))
            program_title, program_details, next_action_steps = res[0], res[1], res[2]
        elif form_type == "contact_form":
            contact_submitted = True
            current_tab = "contact"

    # CSS with double braces to escape f-string conflict
    css = """
        body { font-family: sans-serif; background: #f8fafc; }
        .card { max-width: 850px; margin: auto; background: white; padding: 25px; border-radius: 12px; }
        .navbar { background: #0f172a; padding: 15px; text-align: center; }
        .navbar a { color: white; padding: 10px; text-decoration: none; }
        .form-group { margin-bottom: 15px; }
        input, textarea { width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 5px; }
        button { background: #2563eb; color: white; border: none; padding: 10px 20px; cursor: pointer; }
    """

    # Return full page
    return f"""<!DOCTYPE html><html><head><style>{css}</style></head><body>
        <div class='navbar'><a href='/?tab=home'>Home</a> <a href='/?tab=services'>Services</a> <a href='/?tab=contact'>Contact</a></div>
        <div class='card'>
            <h1>Inayti Youth Foundation</h1>
            {"<h2>Results for " + name + "</h2><p>" + program_title + "</p>" if assessment_submitted else "<h2>Assessment</h2><form method='POST'><input type='hidden' name='form_identity' value='assessment'><input type='text' name='username' placeholder='Name' required><input type='number' name='userage' placeholder='Age' required><select name='choice'><option value='A'>Career</option><option value='B'>Academic</option></select><button type='submit'>Submit</button></form>"}
        </div></body></html>"""

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
