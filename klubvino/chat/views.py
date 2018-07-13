from django.shortcuts import render
from django.views.generic import View
from accounts.models import UserProfileInfo
from chat.models import ChatLog
from django.utils import timezone
import json
# Create your views here.

def setJsonData(filename, data):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    JSON_DIR = os.path.join(BASE_DIR, 'static', 'json', filename)
    with open(JSON_DIR, 'wt') as my_file:
       new_data = json.dumps(data)
       my_file.write(new_data)
    my_file.close()

class ChatView(View):

    def get(self, request, *args, **kwargs):
        myModel = ChatLog.objects.all()
        userId = self.request.user.id
        profile_pic = UserProfileInfo.objects.get(user=userId).profile_pic
        user_name = UserProfileInfo.objects.get(user=userId).user.username
        return render(request, 'chat/chat.html', {'user_name': user_name, 'userid': userId, 'profile_pic': profile_pic, 'myModel': myModel})

    def post(self, request, *args, **kwargs):
        userId = self.request.user.id
        profile_pic = UserProfileInfo.objects.get(user=userId).profile_pic
        user_name = UserProfileInfo.objects.get(user=userId).user.username
        myModel = ChatLog.objects.all()
        message = request.POST['message']
        if message == '':
            return render(request, 'chat/chat.html', {'user_name': user_name, 'userid': userId, 'profile_pic': profile_pic,'myModel': myModel})
        else:
            timeis = timezone.now()
            newChat = ChatLog()
            newChat.profile_pic = UserProfileInfo.objects.get(user=userId).profile_pic
            newChat.timestamp = timeis
            newChat.message = message
            newChat.save()
            return render(request, 'chat/chat.html', {'user_name': user_name, 'userid': userId, 'profile_pic': profile_pic,'myModel': myModel})
