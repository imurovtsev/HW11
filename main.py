from flask import Flask, request, render_template
from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill

app = Flask(__name__)


@app.route('/')
def index():
    """Глвная страница"""
    all_candidates = []
    for candidate in load_candidates_from_json():
        all_candidates.append(f'''<p><a href="/page/{candidate['id']}">{candidate['name']}</a></p>''')

    return f"<h1>Все кандидаты</h1>{''.join(all_candidates)}"


@app.route('/page/<int:x>')
def page(x):
    candidate = get_candidate(x)
    if candidate is None:
        return f"<h1>{x}, {candidate}, Нет кандидата с таким id</h1>"

    return render_template('candidate.html', candidate=candidate, id=candidate['id'], name=candidate['name'], picture=candidate['picture'], position=candidate['position'], gender=candidate['gender'], age=candidate['age'], skills=candidate['skills'])


@app.route('/search/<string:x>')
def search(x):
    candidates = get_candidates_by_name(x)
    all_candidates = []
    for candidate in candidates:
        all_candidates.append(f'''<p><a href="/page/{candidate['id']}">{candidate['name']}</a></p>''')

    return f"<h1>Все кандидаты с именем {x}</h1>{''.join(all_candidates)}"


@app.route('/skills/<string:x>')
def skills(x):
    candidates = get_candidates_by_skill(x)
    all_candidates = []
    for candidate in candidates:
        all_candidates.append(f'''<p><a href="/page/{candidate['id']}">{candidate['name']}</a></p>''')

    return f"<h1>Все кандидаты с навыком {x}</h1>{''.join(all_candidates)}"


if __name__ == '__main__':
    app.run()
