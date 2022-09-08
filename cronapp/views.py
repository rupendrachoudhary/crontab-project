from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
	template_name = 'cronapp/home.html'


	def cronoutput(self, request, *args, **kwargs):
		mins = request.POST.get('cron_mins')
		hours = request.POST.get('cron_hours')  
		days = request.POST.get('cron_days')
		months = request.POST.get('cron_months')
		weeks = request.POST.get('cron_weeks')

		context = {
		'mins':mins,
		'hours':hours,
		'days':days,
		'months':months,
		'weeks':weeks,

		}
		
		print("hello")
		print(f'{mins}{hours}{days}{months}{weeks}')
		return render (request, self.template_name, context)



     


def blog(request):
	return render(request, 'cronapp/blog.html')

def contact(request):
	return render(request, 'cronapp/contact.html')