FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /app

COPY app.py requirements.txt /app/
ADD templates /app/templates
ADD static /app/static

RUN chmod -R 777 /app

RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 8000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:app"]
