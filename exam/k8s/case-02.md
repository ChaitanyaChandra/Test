> Case2 

* This question needs to be solved on node node01. 
* To access the node using SSH:
* As an administrator, you need to prepare node01 to install kubernetes. 
* One of the steps is installing a container runtime. 
* Install the `cri-docker_0.3.16.3-0.debian.deb` package located in /root and ensure that the cri-docker service is running and enabled to start on boot.

> Acceptance

* Is the package installed successfully on node01?
* Is the service running?
* Is the service enabled?

> Solution

```shell
sudo apt install -y ./cri-docker_0.3.16.3-0.debian.deb
sudo systemctl start cri-docker
sudo systemctl enable cri-docker
sudo systemctl status cri-docker
```