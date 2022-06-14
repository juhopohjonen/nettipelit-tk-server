
from flask import Flask, redirect, render_template, request, Blueprint, abort, url_for
from jinja2 import TemplateNotFound
from app import app

import random

import json

from apidata import get_best_games, get_best_mobile_games, load_categories, load_games, get_game_by_id, categoryData

loaded_games = load_games()
loaded_categories = load_categories()



@app.route('/')
def index():


    return render_template('main_index.html', 
    best_games=get_best_games(games=loaded_games, limit=40, start=random.randint(1, 100)),
    newest_games=get_best_games(games=loaded_games, limit=40, start=random.randint(100, 300)),
    categories=loaded_categories
    )

@app.route('/game')
def view_game():
    game_id = request.args.get('id')
    full_screen = request.args.get('fullscreen')


    if game_id == None:
        return abort(404)

    server_response = get_game_by_id(game_id)

    if server_response["code"] == 404:
        return abort(404)

    gameobject = server_response["data"]


    if full_screen != 'true':
        # do not use full screen

        return render_template('play_game.html',
        game=gameobject,
        categories=loaded_categories,
        recommended_games=get_best_games(games=loaded_games, limit=24, start=random.randint(1, 100))
        )  
    else:
        # use full screen

        return render_template('play_game_fullscreen.html',
        game=gameobject,
        categories=loaded_categories,
        recommended_games=get_best_games(games=loaded_games, limit=24, start=random.randint(1, 100))
        )



@app.route('/categories/<string:categoryid>')
def category_list(categoryid):
    category = None

    # find category

    for i in loaded_categories:
        if categoryid == i['id']:
            category = i

    if category == None:
        abort(404)

    cur_category_data = categoryData(id=categoryid,
    urlPrefixForGame=url_for('view_game')
    )
    

    return render_template('view_category.html',
    category=category,
    categoryDataObj=cur_category_data.createCategoryDataObj(),
    categories=loaded_categories
    )

@app.route('/info')
def info():
    return render_template('info.html', categories=loaded_categories)
    
@app.route('/tietosuoja')
def tietosuoja():
    return render_template('tietosuoja.html')


# ERRORS

@app.errorhandler(404)
def notfound(message):
    app.logger.error(message)
    return render_template('error.html', errorcode=404)

@app.errorhandler(500)
def internalError(message):
    app.logger.error(message)
    return render_template('error.html', errorcode=500)
