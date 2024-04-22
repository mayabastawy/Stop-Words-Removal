
FROM python:3.9-slim

WORKDIR /app

COPY script.py /app/

COPY random_paragraphs.txt /app/

RUN pip install nltk

CMD ["python", "./script.py"]
