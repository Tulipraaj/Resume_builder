# views.py
from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from xhtml2pdf import pisa
from .forms import UserDetailsForm

class GeneratePDF(View):

    def get(self, request, *args, **kwargs):
        form = UserDetailsForm()
        return render(request, 'my_temp.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserDetailsForm(request.POST)
        if form.is_valid():
            user_details = form.save()

            # Load the PDF template
            pdf_template = get_template('pdf_template.html')
            context = {'user_details': user_details}
            pdf_content = pdf_template.render(context)

            # Create a PDF response
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="output.pdf"'

            # Convert HTML to PDF using xhtml2pdf
            pisa_status = pisa.CreatePDF(pdf_content, dest=response)
            if pisa_status.err:
                return HttpResponse('Error during PDF generation.')

            return response

        return render(request, 'my_temp.html', {'form': form})
