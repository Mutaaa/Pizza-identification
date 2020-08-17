FROM tensorflow/tensorflow:latest-gpu
WORKDIR /app
COPY ./requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt
COPY . /app
RUN mkdir /app/upload
ENTRYPOINT ["python"]
CMD ["app.py"]