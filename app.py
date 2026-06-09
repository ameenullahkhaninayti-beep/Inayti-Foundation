from flask import Flask, request

app = Flask(__name__)

# Aapki Verified Information
GMAIL_ID = "ameenullahkhaninayti@gmail.com"
PHONE_NUMBER = "9068495437"

@app.route("/", methods=["GET", "POST"])
def home():
    current_tab = request.args.get("tab", "home")
    
    assessment_submitted = False
    contact_submitted = False
    name, age, eligibility_html, program_title, program_details, next_action_steps = "", 0, "", "", "", ""
    contact_name, contact_email, contact_msg = "", "", ""

    if request.method == "POST":
        form_type = request.form.get("form_identity")
        
        if form_type == "assessment":
            assessment_submitted = True
            current_tab = "home"
            name = request.form.get("username")
            age = int(request.form.get("userage") or 0)
            user_choice = request.form.get("choice")
            
            if age >= 18:
                eligibility_html = "<p style='color: #28a745; margin: 5px 0;'><strong>Eligibility Status:</strong> ✔ Approved for independent adult programs.</p>"
            else:
                eligibility_html = """
                <div style='color: #856404; background-color: #fff3cd; border: 1px solid #ffeeba; padding: 12px; border-radius: 6px; margin: 10px 0; font-weight: bold;'>
                    ⚠ Age Check: Minor track active. Parental or guardian authorization is required to finalize formal registration.
                </div>
                """

            if user_choice in ["A", "C"]:
                program_title = "Career Problem Solutions & Exploration Track"
                program_details = "Career confusion or job-search stagnation can feel challenging. Our program analyzes your core skill profile, aligns your competencies with modern shifting job markets, and builds a definitive hiring roadmap."
                next_action_steps = "<li><strong>Step 1:</strong> Check your email! A complimentary 'Career Profile Worksheet' has been dispatched.</li><li><strong>Step 2:</strong> Organize your updated resume or academic transcripts for our counselor evaluation session.</li>"
            elif user_choice == "B":
                program_title = "Academic & Higher Education Counseling Track"
                program_details = "Deciding on college majors, credit streams, or university transfers is a critical turning point. Our institutional advisors ensure you locate curricular paths optimizing your organic skills and professional market values."
                next_action_steps = "<li><strong>Step 1:</strong> Check your inbox for our upcoming interactive webinar 'Demystifying College Admissions'.</li><li><strong>Step 2:</strong> List your top three academic interests before booking an advisor appointment slot.</li>"
            elif user_choice == "D":
                program_title = "Confidential Psychological Well-being Track"
                program_details = "Mental health and daily emotional balance are our core priorities. We provide safe, fully encrypted, non-judgmental digital architecture to discuss institutional stress, personal burnout, and performance anxiety."
                next_action_steps = "<li><strong>Step 1:</strong> Access your profile message hub to directly ping a licensed staff counselor for an initial evaluation call.</li><li><strong>Step 2:</strong> Note that all files and logs are completely anonymous and protected under privacy protocols.</li>"
            elif user_choice == "E":
                program_title = "Strategic Business Startup & Incubation Track"
                program_details = "Transforming a rough concept into a scaling commercial entity requires specialized navigation. Our corporate mentorship stream covers Lean Canvas planning, minimum viable product (MVP) design, and funding mechanics."
                next_action_steps = "<li><strong>Step 1:</strong> Download the attached 'Startup Blueprint Framework' link forwarded to your email address.</li><li><strong>Step 2:</strong> Draft a simple list of the target customer problems you want to solve before scheduling your call.</li>"

        elif form_type == "contact_form":
            contact_submitted = True
            current_tab = "contact"
            contact_name = request.form.get("c_name")
            contact_email = request.form.get("c_email")
            contact_msg = request.form.get("c_message")

    # Navbar classes handle karne ke liye simple variables (No f-string conflict)
    home_active = "active" if current_tab == "home" else ""
    about_active = "active" if current_tab == "about" else ""
    contact_active = "active" if current_tab == "contact" else ""

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Youth Foundation Portal</title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
        <style>
            body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 0; padding: 0; background-color: #f4f6f9; color: #333; }}
            .header {{ background-color: #004085; color: white; padding: 30px 20px; text-align: center; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
            .header h1 {{ margin: 0; font-size: 32px; font-weight: 700; letter-spacing: 0.5px; }}
            .header p {{ margin: 8px 0 0 0; opacity: 0.9; font-size: 16px; font-style: italic; }}
            
            .navbar {{ display: flex; justify-content: center; background-color: #1e2d3b; border-bottom: 4px solid #007bff; }}
            .navbar a {{ color: #adb5bd; padding: 15px 25px; text-align: center; text-decoration: none; font-weight: bold; font-size: 15px; transition: all 0.3s ease; }}
            .navbar a:hover {{ color: white; background-color: #2c3e50; }}
            .navbar a.active {{ color: white; background-color: #007bff; }}
            
            .main-container {{ max-width: 750px; margin: 40px auto; padding: 0 20px; box-sizing: border-box; }}
            .card {{ background: white; padding: 40px; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #eef2f5; }}
            
            h2 {{ color: #004085; margin-top: 0; font-size: 24px; border-bottom: 2px solid #e9ecef; padding-bottom: 10px; }}
            h3 {{ color: #495057; margin-top: 20px; }}
            p {{ line-height: 1.7; font-size: 15px; color: #4a5568; }}
            
            .form-group {{ margin-bottom: 22px; }}
            .form-group label {{ display: block; font-weight: 600; margin-bottom: 8px; color: #495057; font-size: 14px; }}
            .form-group input[type="text"], .form-group input[type="email"], .form-group input[type="number"], .form-group textarea {{ 
                width: 100%; padding: 12px; border: 1px solid #ced4da; border-radius: 6px; box-sizing: border-box; font-size: 15px; background-color: #fff; transition: border-color 0.15s; 
            }}
            
            .option-block {{ background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin-top: 15px; }}
            .radio-row {{ display: flex; align-items: flex-start; margin-bottom: 15px; padding-bottom: 12px; border-bottom: 1px dashed #e2e8f0; }}
            .radio-row:last-child {{ margin-bottom: 0; padding-bottom: 0; border-bottom: none; }}
            .radio-row input {{ margin-top: 4px; margin-right: 12px; scale: 1.2; cursor: pointer; }}
            
            button {{ background-color: #007bff; color: white; border: none; padding: 14px 24px; border-radius: 6px; font-size: 16px; font-weight: bold; width: 100%; cursor: pointer; }}
            button:hover {{ background-color: #0056b3; }}
            
            .btn-social {{ display: block; text-decoration: none; text-align: center; font-weight: bold; padding: 12px; border-radius: 6px; margin-top: 12px; color: white; font-size: 15px; }}
            .btn-whatsapp {{ background-color: #25D366; }}
            .btn-whatsapp:hover {{ background-color: #1ebd58; }}
            .btn-email {{ background-color: #EA4335; }}
            .btn-email:hover {{ background-color: #d3382c; }}

            .result-container {{ margin-top: 35px; padding: 25px; background-color: #f3faf6; border-left: 6px solid #28a745; border-radius: 8px; border: 1px solid #d4edda; }}
            .step-card {{ background: white; padding: 15px 20px; border-radius: 6px; border: 1px dashed #28a745; margin-top: 15px; }}
            .step-card ul {{ margin: 0; padding-left: 20px; }}
            .success-banner {{ background-color: #d4edda; color: #155724; border: 1px solid #c3e6cb; padding: 15px; border-radius: 6px; font-weight: bold; margin-bottom: 25px; }}
            .footer {{ text-align: center; margin-top: 60px; padding: 20px; font-size: 13px; color: #777; border-top: 1px solid #e1e4e6; }}
        </style>
    </head>
    <body>

        <div class="header">
            <h1>Youth Foundation</h1>
            <p>Empowering the Next Generation to Navigate Life, Education, and Career Choices</p>
        </div>

        <div class="navbar">
            <a href="/?tab=home" class="{home_active}">Program Assessment</a>
            <a href="/?tab=about" class="{about_active}">About Us</a>
            <a href="/?tab=contact" class="{contact_active}">Contact Us</a>
        </div>

        <div class="main-container">
            <div class="card">
    """

    if current_tab == "home":
        html_content += """
                <h2>Program Guidance Assessment</h2>
                <p>Welcome to our diagnostic assessment system. Please input your structural details and objective path below to instantly calculate resource eligibility and review your next execution checkpoints.</p>
                
                <form method="POST">
                    <input type="hidden" name="form_identity" value="assessment">
                    <div class="form-group">
                        <label for="username">Full Name:</label>
                        <input type="text" id="username" name="username" placeholder="e.g. John Doe" required>
                    </div>
                    <div class="form-group">
                        <label for="userage">Your Age:</label>
                        <input type="number" id="userage" name="userage" placeholder="e.g. 21" min="1" max="120" required>
                    </div>

                    <div class="option-block">
                        <label style="font-weight: bold; display: block; margin-bottom: 12px; color: #495057;">Select Your Primary Strategic Goal:</label>
                        <div class="radio-row">
                            <input type="radio" id="A" name="choice" value="A" required>
                            <label for="A"><strong>A) Career Problem Resolution</strong><br><span style="color:#6c757d; font-size:13px;">For individuals stuck in unfavorable job roles or experiencing layout stagnation.</span></label>
                        </div>
                        <div class="radio-row">
                            <input type="radio" id="B" name="choice" value="B">
                            <label for="B"><strong>B) Educational Curriculum Strategy</strong><br><span style="color:#6c757d; font-size:13px;">Assistance choosing higher degrees, stream specializations, or university pathways.</span></label>
                        </div>
                        <div class="radio-row">
                            <input type="radio" id="C" name="choice" value="C">
                            <label for="C"><strong>C) General Career Exploration</strong><br><span style="color:#6c757d; font-size:13px;">Mapping modern skill frameworks to trending commercial sectors for beginners.</span></label>
                        </div>
                        <div class="radio-row">
                            <input type="radio" id="D" name="choice" value="D">
                            <label for="D"><strong>D) Psychological Consultation Track</strong><br><span style="color:#6c757d; font-size:13px;">Safe management systems for academic burnout, personal stress, and social performance.</span></label>
                        </div>
                        <div class="radio-row">
                            <input type="radio" id="E" name="choice" value="E">
                            <label for="E"><strong>E) Business Incubator & Startup Advisory</strong><br><span style="color:#6c757d; font-size:13px;">Mentorship programs focusing on monetization models, prototyping, and investor pitching.</span></label>
                        </div>
                    </div>
                    <button type="submit" style="margin-top: 25px;">Generate Guidance Summary</button>
                </form>
        """
        
        if assessment_submitted:
            html_content += f"""
                <div class="result-container">
                    <h3>Your Custom Roadmap Output</h3>
                    <p><strong>Prepared For:</strong> {name} (Age {age})</p>
                    {eligibility_html}
                    <hr style="border: 0; border-top: 1px solid #ced4da; margin: 15px 0;">
                    <p style="font-size: 16px; color: #155724;"><strong>Assigned Pathway:</strong> {program_title}</p>
                    <p style="color: #2b5435;">{program_details}</p>
                    <div class="step-card">
                        <strong style="color: #155724; display:block; margin-bottom:8px;">Mandatory Action Plan:</strong>
                        <ul>{next_action_steps}</ul>
                    </div>
                </div>
            """

    elif current_tab == "about":
        html_content += """
                <h2>About Youth Foundation</h2>
                <p><strong>Founder:</strong> Ameen Ullah Khan Inayti</p>
                <p>The <strong>Youth Foundation</strong> was born out of a simple, powerful conviction: <em>Start for helping others</em>. In a complex, fast-moving world, young students, aspiring entrepreneurs, and working professionals often find themselves isolated when trying to resolve massive educational and mental health hurdles.</p>
                <p>Under the vision of Ameen Ullah Khan Inayti, this digital portal serves as an accessible bridge connecting individuals with actionable roadmaps. Our organizational structure works to democratize mentoring, guaranteeing that financial or logistical limits never prevent an ambitious individual from finding an advisor.</p>
                <h3>Our Core Strategic Pillars:</h3>
                <ul style="padding-left: 20px; line-height: 1.8; color: #4a5568;">
                    <li><strong>Radical Accessibility:</strong> Providing structured, clear action checkpoints free of complicated industrial jargon.</li>
                    <li><strong>Diverse Expertise:</strong> Blending corporate strategy guides with empathetic psychological consultation tracks.</li>
                    <li><strong>Actionable Checkpoints:</strong> We never simply deliver raw theory—every evaluation generates immediate steps to take.</li>
                </ul>
        """

    elif current_tab == "contact":
        if contact_submitted:
            html_content += f"""
                <div class="success-banner">
                    ✔ Message Dispatched! Thank you, {contact_name}. The Youth Foundation intake office has registered your inquiry and will respond within 24 business hours.
                </div>
            """
            
        html_content += f"""
                <h2>Contact Our Headquarters</h2>
                <p>Have an extended custom issue, curious about corporate partnership alignments, or wish to schedule an immediate intake call with Ameen Ullah Khan Inayti? Fill out our system contact slip below.</p>
                
                <form action="https://formspree.io/f/xoqggyrd" method="POST">
                    <input type="hidden" name="form_identity" value="contact_form">
                    <div class="form-group">
                        <label for="c_name">Full Name:</label>
                        <input type="text" id="c_name" name="c_name" placeholder="Enter your full name" required>
                    </div>
                    <div class="form-group">
                        <label for="c_email">Email Address:</label>
                        <input type="email" id="c_email" name="_replyto" placeholder="name@domain.com" required>
                    </div>
                    <div class="form-group">
                        <label for="c_message">State Your Situation / Inquiry:</label>
                        <textarea id="c_message" name="message" rows="5" placeholder="Detail your background situation or specific question here..." required></textarea>
                    </div>
                    <input type="hidden" name="_to" value="{GMAIL_ID}">
                    <button type="submit">Transmit Secure Message</button>
                </form>

                <h3 style="margin-top: 35px;">Quick Instant Channels</h3>
                <a href="https://wa.me/91{PHONE_NUMBER}?text=Hello%20Founder%20Ameen%20Ullah%20Khan" target="_blank" class="btn-social btn-whatsapp">
                    <i class="fab fa-whatsapp"></i> Chat instantly on WhatsApp
                </a>
                <a href="mailto:{GMAIL_ID}?subject=Youth%20Foundation%20Inquiry" class="btn-social btn-email">
                    <i class="far fa-envelope"></i> Open Mail Client
                </a>
                
                <div style="margin-top: 35px; background-color: #f8fafc; padding: 20px; border-radius: 8px; border: 1px dashed #cbd5e1;">
                    <strong style="display:block; margin-bottom: 5px; color: #334155;">General Operations Directory:</strong>
                    <span style="font-size:14px; color:#64748b;">
                        📧 Secure Email: {GMAIL_ID}<br>
                        📞 Hotline Line: +91 {PHONE_NUMBER}<br>
                        🏢 Location Context: Regional Digital Support Center
                    </span>
                </div>
        """

    html_content += """
            </div>
        </div>
        <div class="footer">
            &copy; 2026 Youth Foundation. Created with a Vision to Help Others. All Rights Preserved.
        </div>
    </body>
    </html>
    """
    return html_content

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
