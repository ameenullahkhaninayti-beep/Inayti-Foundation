from flask import Flask, render_template_string, request

app = Flask(__name__)

# Aapki details
GMAIL_ID = "ameenullahkhaninayti@gmail.com"
PHONE_NUMBER = "9068495437"

@app.route('/', methods=['GET', 'POST'])
def home():
    # URL mein se 'tab' pata karne ke liye (Default: home)
    current_tab = request.args.get('tab', 'home')
    contact_submitted = False
    client_name = ""

    if request.method == 'POST':
        contact_submitted = True
        client_name = request.form.get('client_name', '')
        current_tab = 'contact'  # Form submit hone par contact page hi dikhega

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Inayti Youth Foundation</title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
        <style>
            body {{ font-family: 'Segoe UI', Arial, sans-serif; margin: 0; padding: 0; background-color: #f4f6f9; color: #333; }}
            
            /* Navigation Menu Bar */
            nav {{ background-color: #2c3e50; padding: 15px 0; text-align: center; position: sticky; top: 0; z-index: 1000; }}
            nav a {{ color: white; text-decoration: none; font-size: 1.1em; font-weight: bold; margin: 0 15px; padding: 8px 16px; border-radius: 5px; transition: 0.3s; }}
            nav a:hover, nav a.active {{ background-color: #3498db; }}

            /* Main Content Container */
            .container {{ max-width: 800px; margin: 40px auto; padding: 30px; background: white; border-radius: 12px; box-shadow: 0 5px 15px rgba(0,0,0,0.1); text-align: center; min-height: 400px; }}
            h1 {{ color: #2c3e50; font-size: 2.5em; }}
            p {{ color: #555; font-size: 1.1em; line-height: 1.6; }}
            
            /* Contact Form Style */
            .form-group {{ margin-bottom: 15px; text-align: left; width: 90%; margin-left: auto; margin-right: auto; }}
            label {{ display: block; margin-bottom: 5px; font-weight: bold; color: #555; }}
            input, textarea {{ width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 6px; box-sizing: border-box; }}
            
            /* Buttons Style */
            .btn {{ display: block; width: 85%; margin: 15px auto; padding: 12px; font-size: 1.1em; font-weight: bold; text-decoration: none; border-radius: 8px; transition: 0.3s; color: white; border: none; cursor: pointer; text-align: center; }}
            .btn-submit {{ background-color: #3498db; width: 90%; }}
            .btn-submit:hover {{ background-color: #2980b9; }}
            .btn-whatsapp {{ background-color: #25D366; }}
            .btn-whatsapp:hover {{ background-color: #1ebd58; }}
            .btn-email {{ background-color: #EA4335; }}
            .btn-email:hover {{ background-color: #d3382c; }}
            
            /* Success Message */
            .success-msg {{ background-color: #2ecc71; color: white; padding: 15px; border-radius: 6px; margin-bottom: 20px; font-weight: bold; }}
            
            /* Gallery Fake Images Grid */
            .gallery-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; margin-top: 20px; }}
            .photo-card {{ background: #eee; padding: 40px 10px; border-radius: 8px; font-weight: bold; color: #777; border: 2px dashed #ccc; }}
            
            footer {{ text-align: center; padding: 20px; color: #95a5a6; font-size: 0.9em; margin-top: 40px; border-top: 1px solid #ddd; }}
        </style>
    </head>
    <body>

        <!-- Navigation Bar (4 Pages Links) -->
        <nav>
            <a href="/?tab=home" class="{"active" if current_tab == "home" else ""}">Home</a>
            <a href="/?tab=about" class="{"active" if current_tab == "about" else ""}">About Us</a>
            <a href="/?tab=gallery" class="{"active" if current_tab == "gallery" else ""}">Gallery</a>
            <a href="/?tab=contact" class="{"active" if current_tab == "contact" else ""}">Contact Us</a>
        </nav>

        <div class="container">
            
            <!-- PAGE 1: HOME PAGE -->
            {" " if current_tab != "home" else f'''
                <h1>Inayti Youth Foundation</h1>
                <p style="font-style: italic; color: #3498db;">"Empowering Youth, Transforming Futures"</p>
                <img src="https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=600" alt="Youth" style="width:100%; max-width:500px; border-radius:8px; margin: 15px 0;">
                <p>Welcome to our official multi-page website. Inayti Youth Foundation is dedicated to support the social, educational, and welfare development of young individuals. Explore our platform to see our impact or to get involved with us today!</p>
            '''}

            <!-- PAGE 2: ABOUT US PAGE -->
            {" " if current_tab != "about" else f'''
                <h1>About Us</h1>
                <p><strong>Our Vision:</strong> To build a society where every youth has the resource, skills, and platform to lead a dignified and successful life.</p>
                <p><strong>Our Mission:</strong> We conduct skill development workshops, social awareness drives, and continuous youth mentorship programs to build future leaders.</p>
                <p>Founded with passion and driven by dedicated volunteers, our community works tirelessly to bring sustainable, positive changes to grassroots levels.</p>
            '''}

            <!-- PAGE 3: GALLERY PAGE -->
            {" " if current_tab != "gallery" else f'''
                <h1>Our Event Gallery</h1>
                <p>Take a look at some of our recent community works and foundation activities:</p>
                <div class="gallery-grid">
                    <div class="photo-card"><i class="fas fa-users fa-2x"></i><br><br>Youth Meetup 2026</div>
                    <div class="photo-card"><i class="fas fa-graduation-cap fa-2x"></i><br><br>Education Drive</div>
                    <div class="photo-card"><i class="fas fa-hands-helping fa-2x"></i><br><br>Social Service</div>
                    <div class="photo-card"><i class="fas fa-ribbon fa-2x"></i><br><br>Awareness Camp</div>
                </div>
            '''}

            <!-- PAGE 4: CONTACT US PAGE (With Email Form & WhatsApp) -->
            {" " if current_tab != "contact" else f'''
                <h1>Contact Us</h1>
                
                {" " if not contact_submitted else f'''
                <div class="success-msg">
                    Thank you, {client_name}! Your details have been securely sent. We will review your inquiry.
                </div>
                '''}

                <p>Fill out the form below to drop us an automated email alert, or reach out directly via call/chat.</p>

                <!-- Connected Email Notification Form -->
                <form action="https://formspree.io/f/xoqggyrd" method="POST">
                    <div class="form-group">
                        <label>Full Name:</label>
                        <input type="text" name="client_name" required placeholder="Enter your full name">
                    </div>
                    <div class="form-group">
                        <label>Your Email ID:</label>
                        <input type="email" name="_replyto" required placeholder="Enter your email address">
                    </div>
                    <div class="form-group">
                        <label>Message/Inquiry:</label>
                        <textarea name="message" rows="4" required placeholder="Type your message for the foundation here..."></textarea>
                    </div>
                    
                    <!-- Notification Destination Setting -->
                    <input type="hidden" name="_to" value="{GMAIL_ID}">
                    
                    <button type="submit" class="btn btn-submit">Submit Details</button>
                </form>

                <p style="margin: 25px 0; color: #aaa; font-weight: bold;">— OR CONNECT IMMEDIATELY —</p>

                <!-- Direct Social Channels Links -->
                <a href="https://wa.me/91{PHONE_NUMBER}?text=Hello%20Inayti%20Foundation" target="_blank" class="btn btn-whatsapp">
                    <i class="fab fa-whatsapp"></i> Chat directly on WhatsApp (+91 {PHONE_NUMBER})
                </a>
                
                <a href="mailto:{GMAIL_ID}?subject=Website%20Inquiry" class="btn btn-email">
                    <i class="far fa-envelope"></i> Send Direct Email ({GMAIL_ID})
                </a>
            '''}

        </div>

        <footer>
            <p>&copy; 2026 Inayti Youth Foundation. All Rights Reserved.</p>
        </footer>
    </body>
    </html>
    """
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True)
