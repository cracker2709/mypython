FROM python:3
ADD src/main.py /
ADD src/modules/*.py /modules/
ADD src/objects/*.py /objects/
RUN pip3 install flask
CMD [ "python3", "./main.py" ]