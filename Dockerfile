FROM python:3.6.0-alpine
LABEL version="1.0"
LABEL description="Python 3 with NLTK and WordNet prepared."
LABEL maintainer "Szymon Szymański szymon.szymanski@hotmail.com"

ADD . /app
WORKDIR /app

RUN apk add --no-cache gcc musl-dev linux-headers && \
    pip install -U nltk && \
    python -W ignore -m nltk.downloader wordnet && \
    pip install -r ./nltk_api/requirements.txt && \
    apk del linux-headers musl-dev gcc && \
    mkdir -p /app

ENV APP_PORT 5000

EXPOSE $APP_PORT

CMD python -m nltk_api
