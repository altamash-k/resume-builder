from django.shortcuts import render
from .forms import ResumeForm
from .models import Resume
from django.views import View
from django.http import HttpResponse
from easy_pdf.views import PDFTemplateResponseMixin
from django.views.generic import DetailView
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
# Create your views here.

class HomeView(View):
    def get(self, request):
        form = ResumeForm()
        candidates = Resume.objects.all()
        return render(request, 'myapp/home.html',{'candidates':candidates,'form':form})

    def post(self, request):
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'myapp/home.html', {'form':form})
        
class CandidateView(View):
    def get(self, request, pk):
        candidate = Resume.objects.get(pk=pk)
        return render(request, 'myapp/candidate.html', {'candidate':candidate})


