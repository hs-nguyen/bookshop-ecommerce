## build stage ##
FROM node:20-alpine as build

WORKDIR /app

COPY . .

RUN npm install 

RUN npm run build

ENV VITE_APP_BACKEND_URL=http://localhost:8081


## run stage ##

FROM nginx:alpine

COPY --from=build /app/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]