# Simple NLTK API [![Build Status](https://travis-ci.org/szyku/nltk-api.svg?branch=master)](https://travis-ci.org/szyku/nltk-api)

Simple python's NLTK API. Provides lexical functionalities like dictionary, synonyms, and lemmatization.

It provides endpoint for looking up entries in the English dictionary powered by [WordNet](https://wordnet.princeton.edu) and NLTK 3.0

### How to run this project?

The preffered way of running this little tool is to use the docker file which is built with every master branch update. You can find this image on the docker hub [here](https://hub.docker.com/r/szyku/nltk-api). If you want to check out the app quickly, just run:
```sh
docker run --rm -d -p 5000:5000 szyku/nltk-api
```

If you do not want to use the docker image you can always install the requirements.txt and setup an virtualenv for python 3.6.1. You can find a guide in [this repo's wiki](https://github.com/szyku/nltk-api/wiki/How-to-develop#setup)

### Endpoints

A full description of the available endpoints can be found [here](https://github.com/szyku/nltk-api/wiki/API-Description)
Be sure to read the remarks as they contains useful information.

### How to develop?
Check out [this guide](https://github.com/szyku/nltk-api/wiki/How-to-develop)
