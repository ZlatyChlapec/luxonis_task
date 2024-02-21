FROM python:3.12-slim as build
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY ./pdm.lock .
RUN pip install pdm && \
    pdm sync


FROM python:3.12-slim as run

WORKDIR /app
COPY --from=build /app/.venv .venv
COPY . .

ENV PATH="/app/.venv/bin:$PATH"
ENV PYTHONUNBUFFERED 1
CMD ["python", "-m", "src.luxonis_task"]
