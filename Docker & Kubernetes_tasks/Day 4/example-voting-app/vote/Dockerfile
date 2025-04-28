FROM python:3.10-slim AS build
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

FROM python:3.10-slim
RUN groupadd -r app && useradd -r -g app app
WORKDIR /app
COPY --from=build /usr/local /usr/local
COPY --from=build /app /app
USER app
EXPOSE 80
CMD gunicorn app:app -b 0.0.0.0:80 -w 4 --keep-alive 0
