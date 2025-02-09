import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate
from datetime import datetime

# Configuration (Update these values)
EMAIL_FROM = "your_email@gmail.com"
EMAIL_PASSWORD = "your_password"  # Generate in Google Account > Security
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

def send_learning_summary(email_to, flashcards):
    """Send daily learning summary email"""
    if not flashcards:
        print("No flashcards to email")
        return False

    # Create message container
    msg = MIMEMultipart()
    msg['From'] = EMAIL_FROM
    msg['To'] = email_to
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = f"Daily Learning Summary - {datetime.now().strftime('%Y-%m-%d')}"
    
    # Build HTML content incrementally
    html_parts = [
        f"<h2>Today's Learning Summary ({datetime.now().strftime('%Y-%m-%d')})</h2>",
        f"<p>Processed {len(flashcards)} flashcards:</p><hr>"
    ]
    
    for i, card in enumerate(flashcards):
        card_html = f"""
        <div style='margin: 20px 0; border-left: 4px solid #3498db; padding-left: 10px;'>
            <h3>Card #{i+1}</h3>
            <p><strong>Front:</strong> {card['front']}</p>
            <p><strong>Back:</strong> {card['back']}</p>
            <p><strong>Tags:</strong> {", ".join(card['tags'])}</p>
        </div>
        """
        html_parts.append(card_html)
    
    html_parts.append("<hr><p>Generated by your Learning System</p>")
    
    # Create final HTML
    html = f"""<html><body>{"".join(html_parts)}</body></html>"""
    
    # Attach HTML content
    msg.attach(MIMEText(html, 'html'))
    
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_FROM, EMAIL_PASSWORD)
            server.sendmail(EMAIL_FROM, email_to, msg.as_string())
        return True
    except Exception as e:
        print(f"Email error: {str(e)}")
        return False
