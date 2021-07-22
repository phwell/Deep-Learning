# para subir aplicação web com bokeh
# primeira forma mais simples executar a linha dentro da pasta do README.md
bokeh serve --show principal.py

#Se necessário, o servidor Bokeh pode enviar pings de keep-alive em um intervalo fixo.
#Para configurar esse recurso, defina a opção `` --keep-alive``
#O bokeh também pode permitir o uso da proteção de cookie XFRF do Tornado. Para virar isso
#, habilite a opção `` --enable-xsrf-cookies`` ou defina o ambiente
#variável `` BOKEH_XSRF_COOKIES = yes``. Se essa configuração estiver ativada, qualquer PUT, POST,
#operações DELETE ou DELETE em manipuladores personalizados ou de login devem ser instrumentados adequadamente
#para funcionar. Normalmente, isso significa adicionar o `` xsrf_form_html () ``
#módulo para modelos de envio de formulários HTML. Para detalhes completos, consulte:
#https://www.tornadoweb.org/en/stable/guide/security.html#cross-site-request-forgery-protection
#O cross-site request forgery (CSRF ou XSRF), em português falsificação de solicitação entre sites, também conhecido como ataque de um clique (one-click attack) ou 
#montagem de sessão (session riding), é um tipo de exploit malicioso de um website, no qual comandos não autorizados são transmitidos a partir de um usuário em quem 
#a aplicação web confia. Há muitos meios em que um site web malicioso pode transmitir tais comandos, tags de imagem especialmente criadas, formulários ocultos e 
#XMLHttpRequests de JavaScript, por exemplo, podem funcionar sem a interação do usuário ou mesmo seu conhecimento. 
#Diferente do cross-site scripting (XSS), que explora a confiança que um usuário tem para um site específico, o CSRF explora a confiança que um site tem no navegador de um usuário.
#É possível especificar várias origens de websocket permitidas adicionando
#a opção `` --allow-websocket-origin`` várias vezes e para fornecer uma
#lista de hosts separados por vírgula para `` BOKEH_ALLOW_WS_ORIGIN``
#Para que o servidor Bokeh substitua o esquema / protocolo IP e URI remoto para
#todas as solicitações com `` X-Real-Ip``, `` X-Forwarded-For``, `` X-Scheme``,
#Cabeçalhos `` X-Forwarded-Proto`` (se forem fornecidos), defina o
#Opção `` --use-xheaders``:
#--auth-module=auth.py  caso deseje adicionar um código para realizar autenticação na aplicação bokeh
#https://www.tornadoweb.org/en/stable/
#WebSocket é uma tecnologia que permite a comunicação bidirecional por canais full-duplex sobre um único soquete Transmission Control Protocol (TCP)

# segunda forma para subir 
bokeh  serve --port 8080 --keep-alive 10000 --enable-xsrf-cookies  --use-xheaders #--auth-module=auth.py --allow-websocket-origin exemplo_site_apenas.com.br:8081

