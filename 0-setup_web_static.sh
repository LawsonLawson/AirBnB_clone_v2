#!/usr/bin/env bash

# Check if running as root
if [[ $EUID -ne 0 ]]; then
    echo "You need root permission to run this script"
    exit 1
fi

# Check if Nginx is installed
if ! dpkg -l | grep -q nginx; then
    # If not installed, update package lists and install Nginx
    apt-get update
    apt-get -y install nginx
fi

# Create necessary directories, including /data/ if it doesn't exist
mkdir -p /data/web_static/shared /data/web_static/releases/test /data/

# Create a dummy HTML file for testing purposes
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

# Create or update symbolic link for current release
ln -sf /data/web_static/releases/test /data/web_static/current

# Set ownership permissions for /data/ recursively
chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to add alias if not already present
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

# Restart Nginx to apply changes
service nginx restart
