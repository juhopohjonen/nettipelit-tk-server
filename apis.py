from flask import Flask, render_template, request, jsonify
from app import app

from markupsafe import escape

import views

SEARCH_RESULTS_LIMIT = 50

@app.route('/search')
def search():
    query = request.args.get('q')

    if query == None:
        return render_template('search.html')

    search_query = query.lower()

    query_results = []
    
    for game in views.loaded_games:
        wordlist = []

        # add words to wordlist

        description_wordlist = game["description"].split()

        for word in description_wordlist:
            wordlist.append(word.lower())
        
        title_wordlist = game["title"].split()

        for word in title_wordlist:
            wordlist.append(word.lower())

        
        containsRelatedWords = False

        for word in wordlist:
            if search_query in word and containsRelatedWords == False:
                containsRelatedWords = True
            elif containsRelatedWords:
                break

        if containsRelatedWords:
            query_results.append(game)
        

    if len(query_results) == 0:
        # NO GAMES FOUND, return with 404

        return render_template('search_results.html',
        query=escape(request.args.get('q')),
        games=None), 404
    elif len(query_results) > SEARCH_RESULTS_LIMIT:

        limited_query_results = []

        for i in range(SEARCH_RESULTS_LIMIT):
            gameobject = query_results[i]

            limited_query_results.append(gameobject)

        return render_template('search_results.html',
        query=escape(request.args.get('q')),
        games=limited_query_results
        )
    else:
        return render_template('search_results.html',
        query=escape(request.args.get('q')),
        games=query_results
        )