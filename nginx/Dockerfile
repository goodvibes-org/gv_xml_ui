FROM nginxproxy/nginx-proxy
RUN mkdir -p /etc/nginx/vhost.d/
RUN echo "client_max_body_size 100m;" > /etc/nginx/vhost.d/goodvibes.work.gd
RUN echo "client_max_body_size 100m;" > /etc/nginx/vhost.d/app.localhost
RUN echo "client_max_body_size 100m;" > /etc/nginx/vhost.d/localhost