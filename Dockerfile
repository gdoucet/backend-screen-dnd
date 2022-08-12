FROM python:3.10 as builder

RUN python3 -m venv /opt/venv
ENV VIRTUAL_ENV=/opt/venv
ENV PATH=/opt/venv/bin:$PATH

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

FROM python:3.10-slim

ENV VIRTUAL_ENV=/opt/venv
ENV PATH=/opt/venv/bin:$PATH

COPY --from=builder /opt/venv/ /opt/venv/

COPY ./docker-images/start.sh /start.sh
RUN chmod +x /start.sh

COPY ./docker-images/gunicorn_conf.py /gunicorn_conf.py

COPY ./docker-images/start-reload.sh /start-reload.sh
RUN chmod +x /start-reload.sh

COPY ./app /app
WORKDIR /app/

ENV PYTHONPATH=/app

EXPOSE 80

# Run the start script, it will check for an /app/prestart.sh script (e.g. for migrations)
# And then will start Gunicorn with Uvicorn
CMD ["/start.sh"]
