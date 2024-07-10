from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from test_app.models import EmailMessageTest, EmailCredentialsUserManager


class MessageListView(TemplateView):
    template_name = 'index.html'

def get_messages(request):
    last_id = int(request.GET.get('last_id', 0))
    messages = EmailMessageTest.objects.filter(id__gt=last_id)
    data = [{
        'id': message.id,
        'subject': message.subject,
        'sent_date': message.sent_date.strftime('%Y-%m-%d'),
        'received_date': message.received_date.strftime('%Y-%m-%d'),
        'description': message.description,
        'attachments': message.attachments
    } for message in messages]
    return JsonResponse(data, safe=False)
