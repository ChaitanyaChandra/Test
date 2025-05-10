# install ssh
sudo apt install openssh-server -y
sudo ufw allow ssh
sudo systemctl enable ssh
sudo ufw allow 22/tcp


# to switch the GUI and console
sudo systemctl isolate multi-user.target
sudo systemctl isolate graphical.target

# to set at boot
sudo systemctl set-default multi-user.target
sudo systemctl set-default multi-user.target

sudo apt purge ubuntu-desktop gnome-shell gdm3
sudo apt autoremove --purge

# to enable
sudo apt install ubuntu-desktop gnome-shell gdm3 -y
sudo systemctl isolate graphical.target

echo "off" | sudo tee /sys/class/drm/card1-eDP-1/status
echo "on" | sudo tee /sys/class/drm/card1-eDP-1/status

HandleLidSwitch=ignore
HandleLidSwitchDocked=ignore
HandleLidSwitchExternalPower=ignore

sudo nano /etc/systemd/logind.conf
sudo systemctl restart systemd-logind