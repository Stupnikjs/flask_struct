FROM python:3.12-alpine


WORKDIR /app 
COPY . ./app
RUN pip install -r app/requirements.txt

# test RUN source .env 
# ENV DB_URI=postgresql://lziqbjkd:HP_7F8AFjzdQO8vXtVPrEJLV0wRRcML2@dumbo.db.elephantsql.com:5432/lziqbjkd
ENV DB_URI='postgresql://mavkwomw:AcfRavZm6hKU42I0rDRzYcruMuFtI8D6@horton.db.elephantsql.com/mavkwomw'


EXPOSE $PORT 

CMD ["python", "app/server.py"]

