import os
from flask import Flask, request

app = Flask(__name__)

# Organization Constants
GMAIL_ID = "ameenullahkhaninayti@gmail.com"
PHONE_NUMBER = "9068495437"

@app.route("/", methods=["GET", "POST"])
def home():
    current_tab = request.args.get("tab", "home")
    
    assessment_submitted = False
    contact_submitted = False
    
    name = ""
    age = 0
    eligibility_html = ""
    program_title = ""
    program_details = ""
    next_action_steps = ""
    
    contact_name = ""

    if request.method == "POST":
        form_type = request.form.get("form_identity")
        
        if form_type == "assessment":
            assessment_submitted = True
            current_tab = "home"
            name = request.form.get("username", "")
            try:
                age = int(request.form.get("userage") or 0)
            except ValueError:
                age = 0
            user_choice = request.form.get("choice", "")
            
            if age >= 18:
                eligibility_html = "<p style='color: #28a745; margin: 5px 0;'><strong>Eligibility Status:</strong> \u2714 Approved for independent adult programs.</p>"
            else:
                eligibility_html = """
                <div style='color: #856404; background-color: #fff3cd; border: 1px solid #ffeeba; padding: 12px; border-radius: 6px; margin: 10px 0; font-weight: bold;'>
                    \u26a0 Age Check: Minor track active. Parental or guardian authorization is required to finalize formal registration.
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
            contact_name = request.form.get("c_name", "")

    # Active State Engine
    tab_home_active = "active" if current_tab == "home" else ""
    tab_services_active = "active" if current_tab == "services" else ""
    tab_founder_active = "active" if current_tab == "founder" else ""
    tab_contact_active = "active" if current_tab == "contact" else ""

    # Part 1: Layout Wrapper
    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>Inayti Youth Foundation</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
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
        .form-group input[type="text"], .form-group input[type="email"], .form-group input[type="number"], .form-group textarea {{ width: 100%; padding: 10px; border: 1px solid #cbd5e1; border-radius: 6px; box-sizing: border-box; font-size: 14px; background-color: #fff; }}
        .option-block {{ background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin-top: 15px; }}
        .radio-row {{ display: flex; align-items: flex-start; margin-bottom: 15px; padding-bottom: 12px; border-bottom: 1px dashed #e2e8f0; }}
        .radio-row:last-child {{ margin-bottom: 0; padding-bottom: 0; border-bottom: none; }}
        .radio-row input {{ margin-top: 4px; margin-right: 12px; transform: scale(1.2); cursor: pointer; }}
        button {{ background-color: #2563eb; color: white; border: none; padding: 12px 20px; border-radius: 6px; font-size: 15px; font-weight: 700; width: 100%; cursor: pointer; }}
        .btn-social {{ display: block; text-decoration: none; text-align: center; font-weight: bold; padding: 12px; border-radius: 6px; margin-top: 12px; color: white; font-size: 14.5px; }}
        .btn-whatsapp {{ background-color: #25D366; }}
        .btn-email {{ background-color: #EA4335; }}
        .result-container {{ margin-top: 35px; padding: 25px; background-color: #f3faf6; border-left: 6px solid #28a745; border-radius: 8px; border: 1px solid #d4edda; }}
        .step-card {{ background: white; padding: 15px 20px; border-radius: 6px; border: 1px dashed #28a745; margin-top: 15px; }}
        .step-card ul {{ margin: 0; padding-left: 20px; }}
        .success-banner {{ background-color: #dcfce7; color: #166534; border: 1px solid #bbf7d0; padding: 15px; border-radius: 6px; font-weight: bold; margin-bottom: 25px; }}
        .footer {{ text-align: center; margin-top: 50px; padding: 20px; font-size: 12px; background-color: #0f172a; color: #94a3b8; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>Inayti Youth Foundation</h1>
        <p>Strategic Advisory & Solutions-Driven Counseling Ecosystem</p>
    </div>
    <div class="navbar">
        <a href="/?tab=home" class="{tab_home_active}">Overview Assessment</a>
        <a href="/?tab=services" class="{tab_services_active}">Practice Areas</a>
        <a href="/?tab=founder" class="{tab_founder_active}">About Our Founder</a>
        <a href="/?tab=contact" class="{tab_contact_active}">Engagement Hub</a>
    </div>
    <div class="main-container">
        <div class="card">
"""

    # Part 2: Page Routing Content Injection
    if current_tab == "home":
        html_content += """
            <h2>Strategic Resource Overview & Assessment</h2>
            <p>Welcome to the <strong>Inayti Youth Foundation</strong>, a premier diagnostic and consulting firm dedicated to navigating critical professional, technical, and vocational challenges.</p>
            <div class="vision-card">
                🏛 Corporate Vision:<br>
                "To extend comprehensive tactical intervention strategies for individuals navigating complex vocational pathways."
            </div>
            <h3 style="margin-top:30px;">Program Guidance Assessment Form</h3>
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
                    <label style="font-weight: bold; display: block; margin-bottom: 12px; color: #334155;">Select Your Primary Strategic Goal:</label>
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
                <h3 style="color: #155724;">Your Custom Roadmap Output</h3>
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

    elif current_tab == "services":
        html_content += """
            <h2>Strategic Advisory Practice Areas</h2>
            <p>Our foundation delivers top-tier structural assistance across multi-disciplinary sectors, blending technical competence with consultation blueprints.</p>
            <div class="pillar-grid">
                <div class="pillar-item">
                    <strong>Aerospace & Technological Advisory</strong>
                    High-level mapping for students specializing in aviation architecture, engineering fields, and advanced maintenance ecosystems.
                </div>
                <div class="pillar-item">
                    <strong>Curricular & Institutional Strategy</strong>
                    Deciding on college majors, university streams, or international credit transfers to optimize organic skill deployment.
                </div>
                <div class="pillar-item">
                    <strong>Psychological & Burnout Mitigation</strong>
                    Safe, highly confidential digital architecture to navigate academic burnout, workspace anxiety, and performance fatigue.
                </div>
                <div class="pillar-item">
                    <strong>Commercial Incubation Blueprinting</strong>
                    Mentorship architectures focusing on Lean Canvas models, minimum viable product (MVP) infrastructure, and initial monetization frameworks.
                </div>
            </div>
        """

    elif current_tab == "founder":
        html_content += """
            <h2>Executive Profile: Our Founder</h2>
            <p>The core philosophy of the Inayti Youth Foundation is entirely built upon a simple driving conviction: <strong>"Start for helping others."</strong></p>
            <p>The comprehensive design of this digital portal is engineered under the exclusive vision of our founder, <strong>Ameen Ullah Khan Inayti</strong>.</p>
            <p>In a complex world, young students, scaling developers, and modern professionals frequently find themselves systemically isolated when attempting to resolve major vocational or structural bottlenecks. Under his guidance, this portal serves as a radical bridge, turning chaotic hurdles into clear milestones.</p>
            <h3>Operational Core Pillars:</h3>
            <ul style="padding-left: 20px; line-height: 1.8; color: #475569;">
                <li><strong>Radical Accessibility:</strong> Providing structural, transparent check-stops free of elite enterprise jargon.</li>
                <li><strong>Multi-Dimensional Synergy:</strong> Merging tough tech/business roadmaps seamlessly with human-focused emotional counseling.</li>
                <li><strong>Immediate Action Items:</strong> Every diagnostic interaction produces instant execution steps.</li>
            </ul>
        """

    elif current_tab == "contact":
        if contact_submitted:
            html_content += f"""
            <div class="success-banner">
                ✔ Request Logged. Founder Ameen Ullah Khan Inayti and the triage team will review your case file.
            </div>
            """
        html_content += f"""
            <h2>Engagement Hub & Consultation Booking</h2>
            <p>Have an extended custom system issue, strategic commercial alignments, or wish to finalize a formal call allocation with Founder Ameen Ullah Khan Inayti? Secure your data packet using our headquarters slip below.</p>
            
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
                    <textarea id="c_message" name="message" rows="5" placeholder="Detail your background situation here..." required></textarea>
                </div>
                <input type="hidden" name="_to" value="{GMAIL_ID}">
                <button type="submit">Transmit Secure Message</button>
            </form>

            <h3 style="margin-top: 35px;">Instant Communication Pipelines</h3>
            <a href="https://wa.me/91{PHONE_NUMBER}?text=Hello%20Founder%20Ameen%20Ullah%20Khan%20Inayti" target="_blank" class="btn-social btn-whatsapp">
                <i class="fab fa-whatsapp"></i> Chat Instantly via WhatsApp Office
            </a>
            <a href="mailto:{GMAIL_ID}?subject=Inayti%20Youth%20Foundation%20Consultation" class="btn-social btn-email">
                <i class="far fa-envelope"></i> Route Official Mail Packet
            </a>
            
            <div style="margin-top: 35px; background-color: #f8fafc; padding: 20px; border-radius: 8px; border: 1px dashed #cbd5e1;">
                <strong style="display:block; margin-bottom: 5px; color: #334155;">General Operations Directory:</strong>
                <span style="font-size:13.5px; color:#64748b;">
                    📧 Secure System Mail: {GMAIL_ID}<br>
                    📞 Operational Hotline: +91 {PHONE_NUMBER}<br>
                    🏢 Location Context: Regional Digital Support Center
                </span>
            </div>
        """

    # Part 3: Base Template Ending
    html_content += """
        </div>
    </div>
    <div c
