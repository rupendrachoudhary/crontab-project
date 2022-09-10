from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'cronapp/home.html'


    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context = {
            'mins_iterator':range(0, 60),

        }
        return context


    def post(self, request, *args, **kwargs):
        mins = int(request.POST.get('cron_mins'))
        hours = request.POST.get('cron_hours')
        days = request.POST.get('cron_days')
        months = request.POST.get('cron_months')
        weeks = request.POST.get('cron_weeks')

        context = {
            'mins': mins,
            'hours': hours,
            'days': days,
            'months': months,
            'weeks': weeks,
            'mins_iterator':range(0, 60),

        }
        print(f'{mins}{hours}{days}{months}{weeks}')
        return render(request, self.template_name, context)


class BlogView(TemplateView):
    template_name = 'cronapp/blog.html'


class ContactView(TemplateView):
    template_name = 'cronapp/contact.html'
