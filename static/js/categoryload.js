var categoryUrl = categoryData["category_url"];

// send xmlhttprequest to categoryUrl 

var xhr = new XMLHttpRequest();


xhr.onload = () => {
    content = JSON.parse(xhr.responseText);
    addGames(content["data"]);
};

xhr.open('GET', categoryUrl, false);
xhr.send();

function createContent () {
    // create content here...
}


function addGames(games) {

    var gamesStartIndex = Math.floor(Math.random() * 20);
    var gameBaseDoms = document.getElementsByClassName('gamebasecard');

    // replace placeholders with working elements

    for (var i = 0; i < gameBaseDoms.length; i++) {
        let currentBaseDom = gameBaseDoms[i];

        // set style's

        currentBaseDom.style.height = '375px';
        currentBaseDom.style.width = '260px';

        //style="width: 260px; height: 375px;"

        let placeholderContent = currentBaseDom.firstElementChild;

        let gamesIndex = gamesStartIndex + i;

        let gameurl = categoryData["url_prefix_for_game"] + "?id=" + games[gamesIndex]["id"];

        let currentGameDom = createGameDomElement(games[gamesIndex], currentBaseDom, gameurl);

        currentBaseDom.removeChild(placeholderContent);
    }

}

function createGameDomElement (game, basedom, playGameUrl) {
    var contentbase = document.createElement('div');

    // create game image => append to contentbase

    var game_img = document.createElement('img');
    game_img.src = game['thumbnailUrl'];
    game_img.classList = 'card-img-top gamebaseimg';
    basedom.appendChild(game_img);
    
    // create body & content (append content 2 body as childNode) => append to contentbase

    var cardbody = document.createElement('div');
    cardbody.classList = 'card-body';

    var gameCardHeading = document.createElement('h5');
    gameCardHeading.innerHTML = game['title'];
    cardbody.appendChild(gameCardHeading);

    

    var playGameButton = document.createElement('a');
    playGameButton.innerHTML = "Pelaa peliä";
    playGameButton.classList = 'btn btn-primary';
    playGameButton.href = playGameUrl;
    cardbody.appendChild(playGameButton);


    cardbody.appendChild(document.createElement('br'));

    // finally add contentbase to basedom

    basedom.appendChild(cardbody);

}