ARG PY_VERSION

FROM $PY_VERSION

ENV GITHUB_USERNAME=qmbot

WORKDIR /workspace

COPY ./dev ./dev
RUN ./dev/install
COPY . .
