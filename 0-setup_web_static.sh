#!/usr/bin/env bash
# Script that sets up web servers for the deployment of web_static

# Update package lists for upgrades
sudo apt-get update

# Install Nginx
sudo apt-get -y install nginx

# Allow incoming traffic on port 80 (HTTP) for Nginx
sudo ufw allow 'Nginx HTTP'

# Create directory structure for storing static website files
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create index.html file with HTML content
tee /data/web_static/releases/test/index.html > /dev/null <<'EOF'
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

# Create symbolic link to set current version of website
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

# Change ownership of directories and files to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Check if the line already exists in the Nginx configuration file
if ! grep -q "location /hbnb_static" /etc/nginx/sites-enabled/default; then
    # If the line doesn't exist, add it to serve static files
    sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default
fi

# Restart Nginx service to apply changes
sudo service nginx restart
