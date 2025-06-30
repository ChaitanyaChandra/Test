tcpdump -c 4 # pockets
tcpdump -D   # list devices
tcpdump -i any -c 5
tcpdump -i enp0s6 -c 5
tcpdump -i enp0s6 -c 5 host master.chaitu.net
tcpdump -i enp0s6 src host master.chaitu.net
tcpdump -i enp0s6 dst host master.chaitu.net
tcpdump -i enp0s6 ether  host 02:00:17:00:64:05
tcpdump -i enp0s6 dst host master.chaitu.net or port 22
tcpdump -i enp0s6 not icmp
tcpdump -i enp0s6 not icmp -w /tmp/demo.pcmp -c 25
tcpdump -r /tmp/demo.pcmp
tcpdump -r /tmp/demo.pcmp -c1
tcpdump -r /tmp/demo.pcmp -c 1 -tttt