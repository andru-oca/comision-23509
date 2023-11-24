from django.views.generic import TemplateView


class Index(TemplateView):
    extra_context = {"comision": "23509"}
    template_name = "index.html"
