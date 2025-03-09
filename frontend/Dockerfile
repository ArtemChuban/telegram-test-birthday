FROM node:lts-alpine3.21 AS builder
ARG VITE_API_URL
ARG VITE_WEB_APP_URL
WORKDIR /app
COPY package*.json ./
RUN npm i
COPY . .
RUN VITE_API_URL=${VITE_API_URL} VITE_WEB_APP_URL=${VITE_WEB_APP_URL} npm run build

FROM nginx:1.27.4-alpine3.21-slim
COPY --from=builder /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
