# using python 3.9
FROM python:3.9

# setting work directory
WORKDIR /code

# copying dependencies file
COPY ./requirements.txt /code/requirements.txt

# installing all dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# copying contents into working dir
COPY ./app /code/app

# running fastapi app via uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
