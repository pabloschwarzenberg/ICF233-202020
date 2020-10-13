FROM python:3.7

ENV DJANGO_SETTINGS_MODULE servicioplanificacion.production

ENV PYTHONUNBUFFERED 1

RUN mkdir servicioplanificacion

WORKDIR /servicioplanificacion

ADD . /servicioplanificacion

RUN ./setup.sh

ENTRYPOINT ["./start.sh"]

EXPOSE 80