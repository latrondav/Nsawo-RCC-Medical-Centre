from django.core.mail import EmailMessage
from django.db import transaction
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from NsawoRCCMCProject import settings
from .models import Contacts

@csrf_exempt
@transaction.atomic
def SendMessage(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        contact_name = data.get('name', '')
        contact_email = data.get('email', '')
        contact_subject = data.get('subject', '')
        contact_message = data.get('message', '')

        # Validate and save contact details to the database
        new_message = Contacts(
            contact_name=contact_name,
            contact_email=contact_email,
            contact_subject=contact_subject,
            contact_message=contact_message
        )
        new_message.save()

        # Construct email messages
        sender_message = (
            f"Hello {contact_name},\n\n"
            f"Thank you for contacting Nsawo RCC Medical Centre. "
            f"Below is the message we have received:\n\n'{contact_message}'\n\n"
            "Thanking you,\nNsawo RCC Medical Centre System Demon."
        )

        admin_message = (
            f"Hello Nsawo RCC Medical Centre Admin,\n\n"
            f"{contact_name} has sent you a message with the details:\n\n'{contact_message}'\n\n"
            "Thanking you,\nNsawo RCC Medical Centre System Demon."
        )

        # Create EmailMessage instances
        sender_email = EmailMessage(
            subject=contact_subject,
            body=sender_message,
            from_email=settings.EMAIL_HOST_USER,
            to=[contact_email]
        )
        sender_email.send(fail_silently=False)

        admin_email = EmailMessage(
            subject=contact_subject,
            body=admin_message,
            from_email=settings.EMAIL_HOST_USER,
            to=[settings.ADMIN_EMAIL]
        )
        admin_email.send(fail_silently=False)

        return JsonResponse({
            'message': 'Message Sent. We Will Get Back To You As Soon As Possible. '
                       'Thank You For Contacting Nsawo RCC Medical Centre.'
        })
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)
