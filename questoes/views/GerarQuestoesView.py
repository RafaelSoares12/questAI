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
            resposta_gerada = response.json()
            print(resposta_gerada)
            return JsonResponse({'resposta': resposta_gerada})
        else:
            erro_msg = f'Erro na solicitação à API do GPT-3 (status {response.status_code})'
            return JsonResponse({'erro': erro_msg}, status=response.status_code)
