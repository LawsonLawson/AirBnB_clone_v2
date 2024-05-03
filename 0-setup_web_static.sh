#!/usr/bin/env bash

# Description: Script to set up web servers for the deployment of web_static

# Update package lists
sudo apt-get update

# Install Nginx
sudo apt-get -y install nginx

# Allow incoming HTTP traffic through the firewall to Nginx
sudo ufw allow 'Nginx HTTP'

# Create directory structure
sudo mkdir -p /data/web_static/{releases/test,shared}

# Create index.html file with basic content
sudo tee /data/web_static/releases/test/index.html > /dev/null <<EOF
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>We are in Business!</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .container {
            text-align: center;
        }

        h1 {
            font-size: 36px;
            color: #333;
            margin-bottom: 20px;
        }

        p {
            font-size: 18px;
            color: #666;
        }
    </style>
</head>
<body>
    <div class="container">
    <h1>We are in Business baby :-)</h1>
        <p>Let us COOK!</p>
    </div>
</body>
</html>
EOF

# Create symbolic link to current release
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Change ownership of /data directory to user ubuntu
sudo chown -R ubuntu:ubuntu /data/

# Configure Nginx to serve static files
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

# Restart Nginx to apply changes
sudo service nginx restart
