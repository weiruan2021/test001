# Dockerfile, image, container

FROM python:3.8
#FROM appium:1.22.3

ADD test_helpo_main.py .


RUN pip install pytest webdriver

CMD ["python", "./test_helpo_main.py"]
