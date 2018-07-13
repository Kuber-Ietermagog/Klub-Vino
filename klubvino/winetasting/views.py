from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, View
from winetasting.models import WineTasting, WineTastingInfo, WineTastingResults
from winetasting.forms import WineTastingInfoForm
from wineinfo.models import Cultivar, WineInfo
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import Permission, User
from django.utils.dateparse import parse_datetime

# Create your views here.

class TastingMainView(View):

    def get(self, request, *args, **kwargs):
        tasting_list = WineTasting.objects.all()
        return render(request, 'winetasting/winetasting_page.html', {'tasting_list':tasting_list})

class WineTastingDetailView(DetailView):
    context_object_name = 'proe_goed'
    model = WineTasting
    template_name = 'winetasting/tasting_detail.html'

    def get_context_data(self, **kwargs):
        context = super(WineTastingDetailView, self).get_context_data(**kwargs)
        chk_date = context['proe_goed'].pk
        chk_closed = context['proe_goed'].close_tasting
        chk_list = WineTastingInfo.objects.filter(date=chk_date)
        if len(chk_list) != 0:
            context['result_btn'] = True
        else:
            context['result_btn'] = False
        return context

class TastingCreateView(CreateView):
    fields = "__all__"
    model = WineTasting

    def get_context_data(self, **kwargs):
        context = super(TastingCreateView, self).get_context_data(**kwargs)
        context['creating'] = True
        context['closing'] = False
        return context

    def get_initial(self):
        initial = super(TastingCreateView, self).get_initial()
        initial.update({'created_by': self.request.user.username})
        return initial


class TastingUpdateView(UpdateView):
    fields = ('close_tasting', )
    model = WineTasting

    def get_context_data(self, **kwargs):
        context = super(TastingUpdateView, self).get_context_data(**kwargs)
        context['creating'] = False
        context['closing'] = True
        return context

class MysteryWineCreateView(CreateView):
    fields = '__all__'
    model = WineTastingInfo

    def get_initial(self):
        initial = super(MysteryWineCreateView, self).get_initial()
        mySearch = self.request.GET['search']
        header_info = WineTasting.objects.filter(id=mySearch)
        for items in header_info:
            initial.update({'date': items.id})
            initial.update({'cultivar': items.cultivar})
        initial.update({'username': self.request.user.username})
        return initial

    # success_url = redirect('tasting:tasting', pk=7)

class MysteryWineUpdateView(UpdateView):
    fields = "__all__"
    model = WineTastingInfo

class MysteryWineDeleteView(DeleteView):
    model = WineTastingInfo
    success_url = reverse_lazy('winetasting:tasting')

class ResultView(View):

    def get(self, request, *args, **kwargs):
        mySearch = request.GET['results']
        header_info = WineTasting.objects.filter(id=mySearch)
        users_name = request.user.username
        result_header = WineTasting()
        code_names = []
        import string
        for letters in string.ascii_uppercase:
            code_names.append(letters)
        for items in header_info:
            result_header.cultivar = items.cultivar
            result_header.date = items.date
            result_header.location = items.location
            result_header.close_tasting = items.close_tasting
            result_header.created_by = items.created_by
            result_header.pk = items.pk
            number_of_wines = items.qty_wines
        body_info = []
        for items in range(0,number_of_wines):
            body_info.append(WineTastingInfo.objects.filter(date_id=mySearch, wine_code_name=code_names[items]))
        results_date = str(body_info[0][0].date).split(',')
        results_date = results_date[0]
        old_data = WineTastingResults.objects.filter(relative_date=results_date)
        save_object_data = {}
        if len(old_data) != 0:
            for items in old_data:
                save_object_data[str(items.wine_code_name)] = [items.real_name, items.cellar, items.price, items.pics, items.year]
            WineTastingResults.objects.filter(relative_date=results_date).delete()
        for stuff in range(0, len(body_info)):
            if len(body_info[stuff]) != 0:
                subtotal = 0
                number_of_votes = 0
                number_of_items = 0
                update_results = WineTastingResults()
                for items in range(0,len(body_info[stuff])):
                    number_of_votes += 1
                    subtotal += body_info[stuff][items].points
                    number_of_items += 1
                total = (subtotal/number_of_votes)
                date_unmod = str(body_info[stuff][items].date).split(',')
                date_mod = date_unmod[0]
                update_results.relative_date = date_mod
                update_results.cultivar = body_info[stuff][items].cultivar
                update_results.wine_code_name = body_info[stuff][items].wine_code_name
                update_results.total = total
                if body_info[stuff][items].wine_code_name in save_object_data:
                    update_results.real_name = save_object_data[body_info[stuff][items].wine_code_name][0]
                    update_results.cellar = save_object_data[body_info[stuff][items].wine_code_name][1]
                    update_results.price = save_object_data[body_info[stuff][items].wine_code_name][2]
                    update_results.pics = save_object_data[body_info[stuff][items].wine_code_name][3]
                    update_results.year = save_object_data[body_info[stuff][items].wine_code_name][4]
                update_results.save()
        if len(body_info) != 0:
            display_results = WineTastingResults.objects.filter(relative_date=results_date)
        return render(request, 'winetasting/results.html', {'result_header': result_header, 'display_results': display_results})

    def post(self, request, *args, **kwargs):
        relative_dt = request.POST.get('date')
        wines_to_save = WineTastingResults.objects.filter(relative_date=relative_dt)
        for items in wines_to_save:
            cultivar_name = items.cultivar
        chk_cultivar = Cultivar.objects.filter(name=cultivar_name).exists()
        if not chk_cultivar:
            save_cultivar = Cultivar()
            save_cultivar.name = cultivar_name
            save_cultivar.save()
        create_cultivar = Cultivar.objects.get(name=cultivar_name)
        for wines in wines_to_save:
            save_wine = WineInfo()
            chk_wine = WineInfo.objects.filter(cultivar=create_cultivar, cellar=wines.cellar, year=wines.year).exists()
            if not chk_wine:
                #create_cultivar = Cultivar.objects.get(name=cultivar_name)
                save_wine.cultivar = create_cultivar
                save_wine.name = wines.real_name
                save_wine.cellar = wines.cellar
                save_wine.year = wines.year
                save_wine.price = wines.price
                save_wine.rating = wines.total
                save_wine.pics = wines.pics
                save_wine.save()

        tasting_list = WineTasting.objects.all()
        return redirect('wineinfo:detail', pk=create_cultivar.id)

class ResultUpdateView(UpdateView):
    fields = '__all__'
    model = WineTastingResults
