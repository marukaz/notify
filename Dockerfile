FROM python:3.10

WORKDIR /app

COPY pyproject.toml ./

ENV PATH /root/.local/bin:$PATH
RUN curl -sSL https://install.python-poetry.org | python3 - \
    && poetry config virtualenvs.create false \
    && poetry install
COPY discord.py ./

CMD ["python", "discord.py"]
