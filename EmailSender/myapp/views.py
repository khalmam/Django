from django.core.mail import send_mail
from django.template import loader
from django.http import HttpResponse
from django.conf import settings
import traceback


def index(request):
    try:
        # Inject values into the HTML template
        html_message = loader.render_to_string(
            'email_sender_app/message.html',
            {
                'name': 'Recipient Name',  # Replace dynamically if needed
                'body': 'This email is to verify whether we can send email in Django from a Gmail account.',
                'sign': 'Sender',  # Replace dynamically if needed
            }
        )

        # Send the email
        send_mail(
            subject='Congratulations!',
            message='You are lucky to receive this mail.',  # Plain text fallback
            from_email=settings.DEFAULT_FROM_EMAIL,  # Use a configured email in settings
            recipient_list=['to@example.com'],  # Replace dynamically if needed
            fail_silently=False,
            html_message=html_message,  # HTML version of the email
        )

        return HttpResponse("Mail Sent Successfully!")
    
    except Exception as e:
        # Log the error and return a bad response
        error_message = f"Error occurred: {str(e)}"
        traceback.print_exc()  # For debugging purposes
        return HttpResponse(f"Failed to send mail. {error_message}", status=500)
