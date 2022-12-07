from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import pdb



class DataMixin(TemplateView):
    template_name = 'cronapp/home.html'

    def get_context_data(self, **kwargs):      
        context = {
            'mins_iterator': range(0, 60),
            'days_iterator': range(1, 31),
            
        }
        return context




class HomeView(DataMixin):

    
    
    def post(self, request, *args, **kwargs):
        mins = str(request.POST.get('cron_mins'))
        hours = request.POST.get('cron_hours')
        days = str(request.POST.get('cron_days'))
        months = request.POST.get('cron_months')
        weeks = request.POST.get('cron_weeks')

        if mins == 'select':
            mins = ','.join(request.POST.getlist('cron_mins[]'))
            mins_list = [int(item) for item in mins.split(',')]
            end = start = mins_list[0]
            mins = ''

            
            for item in range(1, len(mins_list)):
                if (mins_list[item] == (mins_list[item - 1] + 1)):
                    end = mins_list[item]

                else:
                    if start == end:
                        mins += str(start) + ","
                    else:
                        mins += str(start) + "-" + str(end) + ","
                    
                    start = end = mins_list[item]

            if start == end:
                mins += str(start)
            else:
                mins += str(start) + "-" + str(end)

        else:
            m = request.POST.get('cron_mins')
            if m == '*':
                
                return HttpResponseRedirect(reverse('everyminute'))
            else:
                m = m.split('/')
                if m[1] == '2':
                    return HttpResponseRedirect(reverse('everyevenminute', kwargs=))
                
                else :
                    return HttpResponseRedirect(reverse('minutes', kwargs={'n':m[1]}))

        
        


        if hours == 'select':
            hours = ','.join(request.POST.getlist('cron_hours[]'))
            hours_list = [int(item) for item in hours.split(',')]
            end = start = hours_list[0]
            hours = ''
            

            for item in range(1, len(hours_list)):
                if (hours_list[item] == (hours_list[item - 1] + 1)):
                    end = hours_list[item]

                else:
                    if start == end:
                        hours += str(start) + ","
                    else:
                        hours += str(start) + "-" + str(end) + ","
                    
                    start = end = hours_list[item]

            if start == end:
                hours += str(start)
            else:
                hours += str(start) + "-" + str(end)



        if days == 'select':
            days = ','.join(request.POST.getlist('cron_days[]'))
            days_list = [int(item) for item in days.split(',')]
            end = start = days_list[0]
            days = ''

            for item in range(1,len(days_list)):
                if (days_list[item] == (days_list[item-1]+1)):
                    end = days_list[item]

                else:
                    if start == end:
                        days +=str(start) + ','
                    else:
                        days += str(start) + "-" + str(end) + ","
                    

                    start = end = days_list[item]

            if start == end:
                days += str(start)
            else:
                days += str(start) + "-" + str(end)


        if months == 'select':
            months = ','.join(request.POST.getlist('cron_months[]'))
            months_list = [int(item) for item in months.split(',')]
            end = start = months_list[0]

            months = ''
            for item in range(1, len(months_list)):
                if (months_list[item] == (months_list[item - 1] + 1)):
                    end = months_list[item]

                else:
                    if start == end:
                        months += str(start) + ","
                    else:
                        months += str(start) + "-" + str(end) + ","

                    start = end = months_list[item]

            if start == end:
                months += str(start)
            else:
                months += str(start) + "-" + str(end)


        if weeks == 'select':
            weeks = ','.join(request.POST.getlist('cron_weeks[]'))
            weeks_list = [int(item) for item in weeks.split(',')]
            end = start = weeks_list[0]

            weeks = ''
            for item in range(1, len(weeks_list)):
                if (weeks_list[item] == (weeks_list[item - 1] + 1)):
                    end = weeks_list[item]

                else:
                    if start == end:
                        weeks += str(start) + ","
                    else:
                        weeks += str(start) + "-" + str(end) + ","
                    

                    start = end = weeks_list[item]

            if start == end:
                weeks += str(start)
            else:
                weeks += str(start) + "-" + str(end)

       

        context = {

            'mins': mins,
            'hours': hours,
            'days': days,
            'months': months,
            'weeks': weeks,
            'mins_iterator': range(0, 60),
            'days_iterator': range(1, 32),

        }

        return render(request, self.template_name, context)


class BlogView(TemplateView):
    template_name = 'cronapp/blog.html'


class ContactView(TemplateView):
    template_name = 'cronapp/contact.html'


class TermsView(TemplateView):
    template_name = 'cronapp/terms_condition.html'


class PrivacyView(TemplateView):
    template_name = 'cronapp/privacy_policy.html'


class CookieView(TemplateView):
    template_name = 'cronapp/cookie_policy.html'


class MinuteView(DataMixin):
    def get(self,request, *args, **kwargs):
        n = kwargs.get('n')
        context = {
        'n':n
        }
        return render(request, self.template_name, context)
    
        

    
    
