set -e

sudo rm -rf /var/www/www.shrike-systems.com
sudo mkdir  /var/www/www.shrike-systems.com
sudo chown root  /var/www/www.shrike-systems.com
sudo chmod 755  /var/www/www.shrike-systems.com
sudo pelican
sudo cp keybase.txt /var/www/www.shrike-systems.com/
