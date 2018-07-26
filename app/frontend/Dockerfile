FROM nginx:alpine

COPY ./ /var/app

WORKDIR /var/app

RUN apk --update add nodejs

RUN npm install && npm run build

RUN cp -r dist/* /usr/share/nginx/html

EXPOSE 80
