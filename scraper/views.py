# scraper/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.conf import settings
import requests
from bs4 import BeautifulSoup

from django.template.loader import render_to_string 


@login_required
def scrape_view(request):
    resultados = []
    email_enviado = False

    if request.method == 'POST':
        palabra_clave = request.POST.get('palabra_clave', '')
        search_url = f"https://es.wikipedia.org/wiki/{palabra_clave.replace(' ', '_')}" 
        
        try:
            headers = {'User-Agent': 'Mozilla/5.0'}
            response = requests.get(search_url, headers=headers, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            article_body = soup.find(id="bodyContent")
            
            if article_body:
                links = article_body.find_all('a', title=True, limit=5)
                
                for link in links:
                    if link.get('href', '').startswith('/wiki/'):
                        resultados.append({
                            'titulo': link['title'],
                            'url': "https://es.wikipedia.org" + link['href']
                        })

            
            if resultados:
                
                email_body_html = render_to_string('scraper/email_results.html', {
                    'palabra_clave': palabra_clave,
                    'resultados': resultados
                })
                
                email = EmailMessage(
                    subject=f'[Scraper] Resultados para "{palabra_clave}"',
                    body=email_body_html,
                    from_email=settings.EMAIL_HOST_USER,
                    to=[request.user.email],
                )
                email.content_subtype = "html" 
                email.send()
                email_enviado = True

        except requests.exceptions.RequestException as e:
           
            print(f"Error en el scraping: {e}")
            pass

    context = {
        'resultados': resultados,
        'email_enviado': email_enviado,
    }
    return render(request, 'scraper/scraper_home.html', context)