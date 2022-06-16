# nettipelit-tk-server
Server code for Nettipelit.tk

Hello! This is the source code for my hobby project Nettipelit.tk. This **development** deploy is currently hosted at https://nettipelit-web-example.herokuapp.com/.

## What is this🤔 ##
This repository is source code for Nettipelit.tk game portal. It loads games from an game portal API and users can play the games at our site without even leaving the site. The front end of this site has been built on bootstrap-dark-5 css framework.

### How it works ###
Before initializing the app, views.py loads games etc. from the API and stores them at variable called loaded_games. We could make a new REST GET-request to the API every time user loads our page, but the i felt like the content won't update so often. Because of that we do not need to make additional requests to API, and that will speed up our website **A LOT**. The games are served on HTML-pages via HTTP GET requests as usually. All pages are rendered using flask's built-in render_template -function, but some content are loaded using AJAX-requests directly at the client side directly from the API.

I published this project to github as public, because this project does not contain any sensitive data or keys and i got bored when i finished this project. I also learned how to use git.
