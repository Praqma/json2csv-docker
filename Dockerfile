FROM node:lts-alpine3.14

RUN npm install -g json2csv

ENTRYPOINT ["json2csv"]
