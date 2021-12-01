FROM python:3.6

WORKDIR /app

COPY requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

COPY . /app

ENV PORT=3000


ENTRYPOINT ["python"]
CMD ["app.py"]

