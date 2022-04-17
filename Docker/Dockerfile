FROM cseelye/rpi-nginx-uwsgi-flask:latest

COPY app.py /app/
COPY sonda.py /app/

WORKDIR /app

EXPOSE 5000

ENTRYPOINT ["python","app.py", "--host=0.0.0.0"]
