from django.shortcuts import render
from django.views.generic import View, DetailView
from wineinfo.models import WineInfo
from search.models import SearchModel

# Create your views here.

class SearchView(View):

    def post(self, request, *args, **kwargs):
        mySearch = request.POST['search']
        users_name = request.user.username
        SearchModel.objects.filter(user_searched=users_name).delete()
        if mySearch != "":
            hitOnWine = WineInfo.objects.all()
            for wines in hitOnWine:
                search_model = SearchModel()
                if str(wines.cultivar).lower() == mySearch.lower():
                    search_model.cultivar = str(wines.cultivar)
                    search_model.name = wines.name
                    search_model.cellar = wines.cellar
                    search_model.year = wines.year
                    search_model.user_searched = users_name
                    search_model.wine_id = wines.id
                    search_model.save()
                if wines.name.lower() == mySearch.lower():
                    search_model.cultivar = str(wines.cultivar)
                    search_model.name = wines.name
                    search_model.cellar = wines.cellar
                    search_model.year = wines.year
                    search_model.user_searched = users_name
                    search_model.wine_id = wines.id
                    search_model.save()
                if wines.cellar.lower() == mySearch.lower():
                    search_model.cultivar = str(wines.cultivar)
                    search_model.name = wines.name
                    search_model.cellar = wines.cellar
                    search_model.year = wines.year
                    search_model.user_searched = users_name
                    search_model.wine_id = wines.id
                    search_model.save()
                try:
                    if wines.year == int(mySearch):
                        search_model.cultivar = str(wines.cultivar)
                        search_model.name = wines.name
                        search_model.cellar = wines.cellar
                        search_model.year = wines.year
                        search_model.user_searched = users_name
                        search_model.wine_id = wines.id
                        search_model.save()
                except:
                    pass
            search_display = SearchModel.objects.filter(user_searched=users_name)
            return render(request, 'search/search.html', {'mySearch': mySearch, 'search_display': search_display})
        else:
            mySearch = 'Jy het niks gesoek nie!'
            return render(request, 'search/search.html', {'mySearch': mySearch})


class SearchDetailView(DetailView):
    context_object_name = 'wyn_goed'
    model = WineInfo
    template_name = 'search/search_detail.html'
