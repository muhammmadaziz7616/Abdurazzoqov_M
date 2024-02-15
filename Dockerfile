FROM python:3.11

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app
COPY . /app
RUN --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install -r /app/req.txt && pip install gunicorn
EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "0:8000"]


# docker build -t muhammadaziz_w:latest .
# docker run --name p17_gruppa_container -p 8000:8000 muhammadaziz_w:latest