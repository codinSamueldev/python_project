FROM python:3.11

WORKDIR /app
COPY environment/requirements.txt /app/environment/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/environment/requirements.txt

COPY . /app

CMD bash -c "while true; do sleep 1; done"