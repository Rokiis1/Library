FROM python:3.11-slim-buster

RUN mkdir -p /app
COPY . main.py /app/
WORKDIR /app
RUN pip install -r requirements.txt
RUN python main.py
EXPOSE 8080
CMD [ "main.py" ]
ENTRYPOINT [ "python" ]