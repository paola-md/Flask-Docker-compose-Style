FROM tensorflow/tensorflow:1.9.0

ADD . .

WORKDIR .

#Copy all files
COPY . .

# install libraries
RUN pip install flask
RUN pip install pillow
RUN pip install scipy
RUN pip install keras
RUN pip install requests

COPY styleWebService.py .
CMD python styleWebService.py
