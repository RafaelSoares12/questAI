from django.urls import path
from questoes.views import GerarQuestoesView

urlpatterns = [
    path("", GerarQuestoesView.as_view(), name="gerar-questoes" ),
]
