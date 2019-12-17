from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django_messages.models import Message
# Create your views here.
from django.views.generic import TemplateView
import json
from django.http import HttpResponse
from django.utils import timezone
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class InboxView(ListView):
    model = Message
    template_name = 'django_messages/inbox.html'
    context_object_name = 'message_list'
    paginate_by = 5

    def get_queryset(self):
        queryset = Message.objects.inbox_for(self.request.user)
        return queryset


class HomeView(TemplateView):
    template_name = "dashboard/home.html"


@method_decorator(login_required, name='dispatch')
class MessageDeleteView(View):
    model = Message
    template_name = None

    def post(self, request, *args, **kwargs):

        user = request.user
        now = timezone.now()
        message_id = kwargs.get("pk")
        message = get_object_or_404(Message, id=message_id)
        deleted = False
        if message.recipient == user:
            message.recipient_deleted_at = now
            deleted = True
        if deleted:
            message.save()
            message = "Message successfully deleted."
        payload = {'delete': 'ok', 'message': message,
                   'message_id': message_id}
        return HttpResponse(content=json.dumps(payload), content_type='application/json')
