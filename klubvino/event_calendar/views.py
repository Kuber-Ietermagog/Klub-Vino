from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, View
from event_calendar.models import EventEntry
from django.urls import reverse_lazy
from django.contrib.auth.models import Permission, User
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.template.loader import render_to_string, get_template

# Create your views here.
class EventMainView(View):

    def get(self, request, *args, **kwargs):
        event_list = EventEntry.objects.all()
        return render(request, 'event_calendar/event_page.html', {'event_list':event_list})

class EventInfoView(DetailView):
    context_object_name = 'entry_detail'
    model = EventEntry
    template_name = 'event_calendar/event_detail.html'

class EventCreateView(CreateView):
    fields = "__all__"
    model = EventEntry

    def get_initial(self):
        initial = super(EventCreateView, self).get_initial()
        initial.update({'created_by': self.request.user.username})
        initial.update({'last_update_by': self.request.user.username})
        return initial

    def form_valid(self, form):
        self.object = form.save()
        email_body = get_template('event_calendar/_mail.html').render({
            'Title': self.object.name,
            'Date': self.object.date,
            'Description': self.object.description,
            'Author': self.object.created_by
        })
        user_list = User.objects.all()
        email_list = []
        for items in user_list:
            if items.email != '':
                email_list.append(items.email)
        msg = EmailMessage('Klub-Vino: Gebeure', email_body, 'mail@klub-vino.co.za', email_list)
        msg.content_subtype = 'html'
        msg.send(fail_silently=True)
        return redirect('event_calendar:events')


class EventUpdateView(UpdateView):
    fields = "__all__"
    model = EventEntry

    def get_initial(self):
        initial = super(EventUpdateView, self).get_initial()
        initial.update({'last_update_by': self.request.user.username})
        return initial


class EventDeleteView(DeleteView):
    model = EventEntry
    success_url = reverse_lazy('event_calendar:events')
