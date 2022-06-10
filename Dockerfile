##Autor: Krzysztof Litka
FROM python:alpine3.15
WORKDIR /usr/src/aplikacja
COPY /aplikacja/* ./
RUN pip install --no-cache-dir flask
CMD ["python","app.py"] 
