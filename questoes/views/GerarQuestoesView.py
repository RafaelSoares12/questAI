import os
from django.http import JsonResponse
from django.views import View
from django.shortcuts import render
import requests


class GerarQuestoesView(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        assunto = request.POST.get('assunto')
        qtdQuestoes = request.POST.get('quantidade-questoes')
        nvlDificuldade = request.POST.get('nivel-dificuldade')

        mensagens = [
            {"role": "system", "content": "Você é um assistente para professores que gera questões apenas sobre assuntos escolares, retorne apenas as questões."},
            {"role": "user", "content": f"Gere {qtdQuestoes} questões sobre {assunto} com nível de dificuldade {nvlDificuldade}."}
        ]

        url = "https://chatgpt-api8.p.rapidapi.com/"

        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": os.getenv('RAPID_API_KEY'),
            "X-RapidAPI-Host": "chatgpt-api8.p.rapidapi.com"
        }

        response = requests.post(url, json=mensagens, headers=headers)

        if response.status_code == 200:
            respostaGerada = response.json()
            print(respostaGerada)
            linhasQuestoes = respostaGerada.text.split('\n')
            
            return render(request, self.template_name, {'respostaGerada': linhasQuestoes})
        else:
            return render(request, self.template_name, {'erroMsg': f'Erro na requisição para a API! Status: {response.status_code}'})
