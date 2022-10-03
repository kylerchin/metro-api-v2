# syntax=docker/dockerfile:1.3
FROM python:3.6

# 
WORKDIR ../code

# 
COPY ./requirements.txt ../code/requirements.txt
# ARG FTP_SERVER
# COPY use-secret.sh .
# RUN --mount=type=secret,id=ftp_server ./use-secret.sh
# RUN --mount=type=secret,id=ftp_server ./use_secret.sh
# RUN pip install --upgrade cython
RUN pip install --no-cache-dir --upgrade -r ../code/requirements.txt
# 

COPY ./app ../code/app
# COPY .git /code/.git
# 
CMD ["python","app/main.py"]
