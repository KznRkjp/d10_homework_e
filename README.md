# d10_homework_e

nginx:

server {
    listen 80;
    server_name 89.208.211.24;

    location = /favicon.ico { access_log off; log_not_found off; }
    location / {
        proxy_pass http://127.0.0.1:8000;
    }
    location /static/ {
        root /home/ubuntu/sk/mod1/d10/d10_homework_e/carsite;
    }
}



