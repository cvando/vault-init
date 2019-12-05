FROM python:3.6-alpine
ADD init-vault /init-vault
RUN pip install requests 
EXPOSE 8090/tcp

CMD [ "python", "./init-vault/main.py" ]