FROM python:3.11

RUN mkdir warehouse

WORKDIR warehouse

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x docker/*.sh

CMD gunicorn api.main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000
