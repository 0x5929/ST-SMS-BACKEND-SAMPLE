from django.views.generic.edit import FormView
from .forms import ImportFormView


class ImportFormView(FormView):
    template_name = "import-csv.html"
    form_class = ImportFormView
    success_url = '/index.html'
