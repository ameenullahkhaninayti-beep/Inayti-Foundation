from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    current_tab = request.args.get("tab", "home")
    
    contact_submitted = False
    client_name = ""

    if request.method == "POST":
        contact_submitted = True
        client_name = request.form.get("client_name")

    # Clean rendering variables to manage active states
    tab_home_active = "active" if current_tab == "home" else ""
    tab_services_active = "active" if current_tab == "services" else ""
    tab_founder_active = "active" if current_tab == "founder" else ""
    tab_contact_active = "active" if current_tab == "contact" else ""

    # Start of HTML content template string
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Inayti Youth Foundation</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 0; padding: 0; background-color: #f8fafc; color: #1e293b; }}
            .header {{ background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%); color: white; padding: 35px 20px; text-align: center; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); }}
            .header h1 {{ margin: 0; font-size: 28px; font-weight: 800; letter-spacing: 0.5px; text-transform: uppercase; }}
            .header p {{ margin: 12px 0 0 0; opacity: 0.85; font-size: 14px; font-style: italic; font-weight: 300; letter-spacing: 1px; }}
            
            .navbar {{ display: flex; flex-wrap: wrap; justify-content: center; background-color: #0f172a; border-bottom: 4px solid #2563eb; position: sticky; top: 0; z-index: 1000; }}
            .navbar a {{ color: #94a3b8; padding: 12px 18px; text-align: center; text-decoration: none; font-weight: 600; font-size: 14px; transition: all 0.25s ease; }}
            .navbar a:hover {{ color: white; background-color: #1e293b; }}
            .navbar a.active {{ color: white; background-color: #2563eb; }}
            
            .main-container {{ max-width: 850px; margin: 20px auto; padding: 0 15px; box-sizing: border-box; }}
            .card {{ background: white; padding: 25px; border-radius: 12px; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05), 0 4px 6px -2px rgba(0,0,0,0.05); border: 1px solid #e2e8f0; }}
            
            h2 {{ color: #1e3a8a; margin-top: 0; font-size: 22px; border-bottom: 2px solid #f1f5f9; padding-bottom: 12px; font-weight: 700; }}
            h3 {{ color: #334155; margin-top: 25px; font-size: 18px; font-weight: 600; }}
            p {{ line-height: 1.6; font-size: 14.5px; color: #475569; }}
            
            .vision-card {{ background: #eff6ff; border-left: 5px solid #2563eb; padding: 15px; border-radius: 4px; margin: 20px 0; font-size: 15px; font-weight: 500; color: #1e40af; }}
            .pillar-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 15px; margin-top: 20px; }}
            .pillar-item {{ background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 15px; }}
            .pillar-item strong {{ color: #1e3a8a; font-size: 15px; display: block; margin-bottom: 6px; }}
            
            .form-group {{ margin-bottom: 18px; }}
            .form-group label {{ display: block; font-weight: 600; margin-bottom: 6px; color: #334155; font-size: 14px; }}
            .form-group input, .form-group textarea {{ width: 100%; padding: 10px; border: 1px solid #cbd5e1; border-radius: 6px; box-sizing: border-box; font-size: 14px; }}
            
            button {{ background-color: #2563eb; color: white; border: none; padding: 12px 20px; border-radius: 6px; font-size: 15px; font-weight: 700; width: 100%; cursor: pointer; }}
            .success-banner {{ background-color: #dcfce7; color: #166534; border: 1px solid #bbf7d0; padding: 15px; border-radius: 6px; font-weight: bold; margin-bottom: 20px; }}
            .footer {{ text-align: center; margin-top: 50px; padding: 20px; font-size: 12px; background-color: #0f172a; color: #94a3b8; }}
        </style>
    </head>
    <body>

        <div class="header">
            <h1>Inayti Youth Foundation</h1>
            <p>Strategic Advisory & Solutions-Driven Counseling Ecosystem</p>
        </div>

        <div class="navbar">
            <a href="/?tab=home" class="{tab_home_active}">Overview</a>
            <a href="/?tab=services" class="{tab_services_active}">Practice Areas</a>
            <a href="/?tab=founder" class="{tab_founder_active}">About Our Founder</a>
            <a href="/?tab=contact" class="{tab_contact_active}">Engagement Hub</a>
        </div>

        <div class="main-container">
            <div class="card">
    """

    # Dynamically inject web pages using Python conditional statements safely outside layout text strings
    if current_tab == "home":
        html_content += """
                <h2>Strategic Resource Overview</h2>
                <p>Welcome to the <strong>Inayti Youth Foundation</strong>, a premier consulting firm dedicated to navigating critical professional, technical, and vocational challenges.</p>
                <div class="vision-card">
                    🏛 Corporate Vision:<br>
                    "To extend comprehensive tactical intervention strategies for individuals navigating complex vocational pathways."
                </div>
        """

    elif current_tab == "services":
        html_content += """
                <h2>Strategic Advisory Practice Areas</h2>
                <div class="pillar-grid">
                    <div class="pillar-item">
                        <strong>Aerospace & Technological Advisory</strong>
                        High-level mapping for students specializing in aviation architecture and advanced maintenance ecosystems.
                    </div>
                </div>
        """

    elif current_tab == "founder":
        html_content += """
                <h2>Executive Profile: Our Founder</h2>
                <p>The vision of the Inayti Youth Foundation is directed by our founder, <strong>Ameen Ullah Khan Inayti</strong>.</p>
        """

    elif current_tab == "contact":
        if contact_submitted:
            html_content += f"""
                <div class="success-banner">
                    ✔ Request Logged. Founder Ameen Ullah Khan Inayti will review your case file.
                </div>
            """
        html_content += """
                <h2>Engagement Hub & Consultation Booking</h2>
                <form method="POST">
                    <div class="form-group">
                        <label for="client_name">Your Name:</label>
                        <input type="text" id="client_name" name="client_name" required>
                    </div>
                    <button type="submit">Submit Request</button>
                </form>
        """

    html_content += """
            </div>
        </div>

        <div class="footer">
            &copy; 2026 Inayti Youth Foundation. All Rights Reserved.
        </div>
    </body>
    </html>
    """
    return html_content

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
