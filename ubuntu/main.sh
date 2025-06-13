# install ssh
sudo apt install openssh-server -y
sudo ufw allow ssh

sudo nano /etc/systemd/logind.conf
sudo systemctl restart systemd-logind
#HandleLidSwitch=ignore
#HandleLidSwitchExternalPower=ignore
#HandleLidSwitchDocked=ignore


echo "off" | sudo tee /sys/class/drm/card1-eDP-1/status
echo "on" | sudo tee /sys/class/drm/card1-eDP-1/status




# mount hardisk
sudo fdisk /dev/sdb
#d -> delete partition
#n → (new partition)
#p → (primary)
#Press Enter (for partition number)
#Press Enter (for first sector)
#Press Enter (for last sector — use full disk)
#w → (write and exit)


sudo mkfs.ext4 /dev/sdb1


sudo mkdir /mnt/chandra
sudo mount /dev/sdb1 /mnt/chandra

fsck -f /dev/sdb1