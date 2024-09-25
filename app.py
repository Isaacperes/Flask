from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

now = datetime.now()

SITE = {  # Configurações do site
    'name': 'PyBlog',                       # Nome do site
    'slogan': 'Pra quem entende de cobras',  # Slogan do site
    'logo': '/static/img/favicon.png',      # Imagem do logotipo
    'favicon': '/static/img/favicon.png',   # Imagem do favicon
    'owner': 'Joca da Silva',               # Proprietário da licença do site
    'year': 2024,                           # Ano de lançamento do site
    'social': (                             # Lista de redes sociais do footer
        # Use `{{ item.icon | safe }}` para renderizar o HTML do `icon`
        {
            'name': 'Facebook',
            'href': 'https://lufer.click/facebook',
            'icon': '<i class="fa-brands fa-square-facebook fa-fw"></i>'
        }, {
            'name': 'Linkedin',
            'href': 'https://lufer.click/linkedin',
            'icon': '<i class="fa-brands fa-linkedin fa-fw"></i>'
        }, {
            'name': 'GitHub',
            'href': 'https://lufer.click/github',
            'icon': '<i class="fa-brands fa-square-github fa-fw"></i>'
        }
    )
}

if SITE['year'] < now.year:
    SITE['owner'] = f'{SITE['year']} {now.year} {SITE['owner']}'
else:
    SITE['owner'] = f'{SITE['year']} {SITE['owner']}'


@app.route('/')
def home():
    page = {
        'site': SITE,
        'title': f'{SITE['name']} - {SITE['slogan']}',
        'css': 'home.css'
    }
    return render_template('home.html', page=page)


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/policies')
def policies():
    return render_template('policies.html')


@app.errorhandler(404)
def errors(e):
    return render_template('404.html')


if __name__ == '__main__':
    app.run(debug=True, port=80)
