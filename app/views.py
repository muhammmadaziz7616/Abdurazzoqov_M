from app.models import Person
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView


class PersonListView(ListView):
    template_name = 'index.html'
    model = Person
    context_object_name = 'products'
    paginate_by = 4


class PersonDeleteView(DeleteView):
    template_name = 'delete_product.html'
    model = Person
    queryset = Person.objects.all()
    success_url = reverse_lazy('index')