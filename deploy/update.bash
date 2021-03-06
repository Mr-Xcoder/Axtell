#!/usr/bin/env bash

# Ensure correct directory
cd /var/www/ppcg-v2

echo "HEAD initially at version:"
echo "$(git rev-parse @)"

git fetch origin
git reset --hard origin/master

echo "Deployed to version:"
echo "$(git rev-parse @)"

# Ensure webasset dirs exist
mkdir -p static/css
chmod 755 static/css
chmod g+s static/css

mkdir -p static/lib
chmod 755 static/lib
chmod g+s static/lib

sudo service ppcg-v2 restart
