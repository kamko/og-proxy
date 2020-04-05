import re

import bs4
import requests
from flask import Blueprint, request, render_template, jsonify

blueprint = Blueprint('root', __name__)


def _og_vals(data):
    soup = bs4.BeautifulSoup(data, features='html.parser')
    r = soup.findAll('meta', {'property': re.compile(r'^og:')})

    def map_meta(tag):
        return tag.attrs['property'], tag.attrs['content']

    return {
        'title': soup.find('title').string,
        'tags': [map_meta(i) for i in r]
    }


@blueprint.route('/')
def stats_all():
    target = request.args.get('url')

    if target is None:
        return jsonify({'error': 'missing url param'}), 400

    req = requests.get(target)

    return render_template('index.html.j2', ctx={
        'url': target,
        **_og_vals(req.text)
    })
