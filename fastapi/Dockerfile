# syntax=docker/dockerfile:1.3
FROM python:3

# 
# WORKDIR /code

# 
COPY ./requirements.txt requirements.txt
# ARG FTP_SERVER
# COPY use-secret.sh .
# RUN --mount=type=secret,id=ftp_server ./use-secret.sh
# RUN --mount=type=secret,id=ftp_server ./use_secret.sh
RUN pip install --no-cache-dir --upgrade -r requirements.txt
# 

COPY ./app /app
COPY ../../appdata ../../appdata
# COPY .git /code/.git
# VOLUME /appdata
# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]



EXPOSE 80