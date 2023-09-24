from django.views import View
from django.shortcuts import render

class GerarQuestoesView(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        assunto = request.POST.get('assunto')
        qtdQuestoes = request.POST.get('quantidade-questoes')
        nvlDificuldade = request.POST.get('nivel-dificuldade')

        print(assunto, qtdQuestoes, nvlDificuldade)