from flask import Flask, render_template_string

app = Flask(__name__)

GMAIL_ID = "ameenullahkhaninayti@gmail.com"
PHONE_NUMBER = "9068495437"

@app.route('/')
def home():
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Inayti Youth Foundation</title>
        <style>
            body {{ font-family: 'Segoe UI', Arial, sans-serif; margin: 0; background-color: #f8f9fa; color: #333; text-align: center; }}
            .container {{ max-width: 550px; margin: 40px auto; padding: 30px; background: white; border-radius: 10px; box-shadow: 0 4px 12px rgba(0,0,0,0.08); }}
            h1 {{ color: #2c3e50; }}
            .form-group {{ margin-bottom: 15px; text-align: left; width: 90%; margin-left: auto; margin-right: auto; }}
            label {{ display: block; margin-bottom: 5px; font-weight: bold; color: #555; }}
            input, textarea {{ width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 6px; box-sizing: border-box; }}
            button {{ background-color: #3498db; color: white; padding: 12px 20px; border: none; border-radius: 6px; cursor: pointer; width: 100%; font-size: 1.1em; font-weight: bold; }}
            button:hover {{ background-color: #2980b9; }}
            .direct-info {{ margin-top: 25px; font-size: 0.95em; color: #7f8c8d; border-top: 1px solid #eee; padding-top: 15px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Inayti Youth Foundation</h1>
            <p>Empowering the youth for a better future.</p>
            
            <hr style="border: 0; border-top: 1px solid #eee; margin: 20px 0;">
            
            <h3>Contact Us</h3>
            <!-- Formspree will automatically forward submissions to your Gmail -->
            <form action="https://formspree.io/f/xoqggyrd" method="POST">
                <div class="form-group">
                    <label>Your Name:</label>
                    <input type="text" name="name" required placeholder="Enter your full name">
                </div>
                <div class="form-group">
                    <label>Your Email:</label>
                    <input type="email" name="_replyto" required placeholder="Enter your email address">
                </div>
                <div class="form-group">
                    <label>Message:</label>
                    <textarea name="message" rows="4" required placeholder="Type your message here..."></textarea>
                </div>
                <!-- Hidden input to make sure it sends to your specified email address -->
                <input type="hidden" name="_to" value="{GMAIL_ID}">
                
                <div class="form-group">
                    <button type="submit">Submit Message</button>
                </div>
            </form>
            
            <div class="direct-info">
                <p><strong>Direct Call/WhatsApp:</strong> +91 {PHONE_NUMBER}</p>
                <p><strong>Official Email:</strong> {GMAIL_ID}</p>
            </div>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True)
