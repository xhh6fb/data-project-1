FROM python:3.9-slim
LABEL maintainer="My DS2022 (Data Project 1) Dockerfile <xhh6fb@virginia.edu>"

WORKDIR /app
COPY . /app/

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOSE 80
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
