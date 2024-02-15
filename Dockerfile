FROM python:3.12-alpine as build
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN pip install pdm
COPY ./pdm.lock .
RUN pdm sync


FROM python:3.12-alpine as run

WORKDIR /app
COPY --from=build /app/.venv .
COPY . .

ENV PATH="/app/.venv/bin:$PATH"
ENV PYTHONUNBUFFERED 1
CMD ["python", "-m", "src.luxonis_task"]
