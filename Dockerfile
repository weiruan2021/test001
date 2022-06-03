# Dockerfile, image, container

FROM python:3.8

ADD test_helpo_main.py .

RUN appium
RUN pip install time selenium appium

CMD ["python", "./test_helpo_main.py"]
