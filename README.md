# Simple NLTK API

Simple python's NLTK API. Provides lexical functionalities like dictionary, synonyms, and lemmatization.

It provides endpoint for looking up entries in the English dictionary powered by [WordNet](https://wordnet.princeton.edu) and NLTK 3.0

### How to run this project?

The preffered way of running this little tool is to use the docker file which is built with every master branch update. You can find this image on the docker hub [here](https://hub.docker.com/r/szyku/nltk-api). If you want to check out the app quickly, just run:
```sh
docker run --rm -d -p 5000:5000 szyku/nltk-api
```

If you do not want to use the docker image you can always install the requirements.txt and setup an virtualenv for python 3.6.1.

### Endpoints

Currenlty, there are three endpoints providing some sort of dictionary-like functionality:

1. Definition

   Definition endpoint provides definitions, that is, searches exact words in the database and returns a collection of found words. This collection contains found meanings of the queried word. You can narrow the search to a certain part of speech like noun or verb. 
2. Similar

   It behaves mostly like the definition endpoint, but it also appends words with similar meaning. For instance, quering for the noun _pig_ will also return definitions for the noun _hog_, the verb _pig_, and the adjective _pig_.
3. Lemma

   Lemma endpoint will attempt to lemmatize provided words. As an example, the verb _jogging_ has a basic form _jog_, but the noun _jogging_ is already at its basic form, so asking for to lemmatize jogging as a noun will result in the same word.
   
Further details are available on the homepage (by default localhost:5000).

### How to develop?
Coming soon...
