{
    "_ansible_facts_gathered": true,
    "ansible_all_ipv4_addresses": [
        "192.168.31.188"
    ],
    "ansible_all_ipv6_addresses": [
        "fe80::17ff:fe02:b89a"
    ],
    "ansible_apparmor": {
        "status": "enabled"
    },
    "ansible_architecture": "x86_64",
    "ansible_bios_date": "02/27/2023",
    "ansible_bios_vendor": "EFI Development Kit II / OVMF",
    "ansible_bios_version": "1.6.4",
    "ansible_board_asset_tag": "NA",
    "ansible_board_name": "NA",
    "ansible_board_serial": "NA",
    "ansible_board_vendor": "NA",
    "ansible_board_version": "NA",
    "ansible_chassis_asset_tag": "OracleCloud.com",
    "ansible_chassis_serial": "NA",
    "ansible_chassis_vendor": "QEMU",
    "ansible_chassis_version": "pc-i440fx-7.2",
    "ansible_cmdline": {
        "BOOT_IMAGE": "/boot/vmlinuz-5.15.0-1045-oracle",
        "console": "ttyS0",
        "crash_kexec_post_notifiers": true,
        "libiscsi.debug_libiscsi_eh": "1",
        "nvme.shutdown_timeout": "10",
        "ro": true,
        "root": "LABEL=cloudimg-rootfs"
    },
    "ansible_date_time": {
        "date": "2025-04-16",
        "day": "16",
        "epoch": "1744813158",
        "epoch_int": "1744813158",
        "hour": "14",
        "iso8601": "2025-04-16T14:19:18Z",
        "iso8601_basic": "20250416T141918640726",
        "iso8601_basic_short": "20250416T141918",
        "iso8601_micro": "2025-04-16T14:19:18.640726Z",
        "minute": "19",
        "month": "04",
        "second": "18",
        "time": "14:19:18",
        "tz": "UTC",
        "tz_dst": "UTC",
        "tz_offset": "+0000",
        "weekday": "Wednesday",
        "weekday_number": "3",
        "weeknumber": "15",
        "year": "2025"
    },
    "ansible_default_ipv4": {
        "address": "192.168.31.188",
        "alias": "ens3",
        "broadcast": "",
        "gateway": "192.168.0.1",
        "interface": "ens3",
        "macaddress": "02:00:17:02:b8:9a",
        "mtu": 9000,
        "netmask": "255.255.192.0",
        "network": "192.168.0.0",
        "prefix": "18",
        "type": "ether"
    },
    "ansible_default_ipv6": {},
    "ansible_device_links": {
        "ids": {
            "sda": [
                "scsi-360dd210ad0864c21a7807ced149fefc1",
                "wwn-0x60dd210ad0864c21a7807ced149fefc1"
            ],
            "sda1": [
                "scsi-360dd210ad0864c21a7807ced149fefc1-part1",
                "wwn-0x60dd210ad0864c21a7807ced149fefc1-part1"
            ],
            "sda14": [
                "scsi-360dd210ad0864c21a7807ced149fefc1-part14",
                "wwn-0x60dd210ad0864c21a7807ced149fefc1-part14"
            ],
            "sda15": [
                "scsi-360dd210ad0864c21a7807ced149fefc1-part15",
                "wwn-0x60dd210ad0864c21a7807ced149fefc1-part15"
            ]
        },
        "labels": {
            "sda1": [
                "cloudimg-rootfs"
            ],
            "sda15": [
                "UEFI"
            ]
        },
        "masters": {},
        "uuids": {
            "sda1": [
                "ba398682-9547-45a5-858a-aad7620c10a3"
            ],
            "sda15": [
                "1FC5-9E05"
            ]
        }
    },
    "ansible_devices": {
        "loop0": {
            "holders": [],
            "host": "",
            "links": {
                "ids": [],
                "labels": [],
                "masters": [],
                "uuids": []
            },
            "model": null,
            "partitions": {},
            "removable": "0",
            "rotational": "1",
            "sas_address": null,
            "sas_device_handle": null,
            "scheduler_mode": "none",
            "sectors": 91024,
            "sectorsize": "512",
            "size": "44.45 MB",
            "support_discard": "4096",
            "vendor": null,
            "virtual": 1
        },
        "loop1": {
            "holders": [],
            "host": "",
            "links": {
                "ids": [],
                "labels": [],
                "masters": [],
                "uuids": []
            },
            "model": null,
            "partitions": {},
            "removable": "0",
            "rotational": "1",
            "sas_address": null,
            "sas_device_handle": null,
            "scheduler_mode": "none",
            "sectors": 0,
            "sectorsize": "512",
            "size": "0.00 Bytes",
            "support_discard": "4096",
            "vendor": null,
            "virtual": 1
        },
        "loop2": {
            "holders": [],
            "host": "",
            "links": {
                "ids": [],
                "labels": [],
                "masters": [],
                "uuids": []
            },
            "model": null,
            "partitions": {},
            "removable": "0",
            "rotational": "1",
            "sas_address": null,
            "sas_device_handle": null,
            "scheduler_mode": "none",
            "sectors": 91008,
            "sectorsize": "512",
            "size": "44.44 MB",
            "support_discard": "4096",
            "vendor": null,
            "virtual": 1
        },
        "loop3": {
            "holders": [],
            "host": "",
            "links": {
                "ids": [],
                "labels": [],
                "masters": [],
                "uuids": []
            },
            "model": null,
            "partitions": {},
            "removable": "0",
            "rotational": "1",
            "sas_address": null,
            "sas_device_handle": null,
            "scheduler_mode": "none",
            "sectors": 113384,
            "sectorsize": "512",
            "size": "55.36 MB",
            "support_discard": "4096",
            "vendor": null,
            "virtual": 1
        },
        "loop4": {
            "holders": [],
            "host": "",
            "links": {
                "ids": [],
                "labels": [],
                "masters": [],
                "uuids": []
            },
            "model": null,
            "partitions": {},
            "removable": "0",
            "rotational": "1",
            "sas_address": null,
            "sas_device_handle": null,
            "scheduler_mode": "none",
            "sectors": 158368,
            "sectorsize": "512",
            "size": "77.33 MB",
            "support_discard": "4096",
            "vendor": null,
            "virtual": 1
        },
        "loop5": {
            "holders": [],
            "host": "",
            "links": {
                "ids": [],
                "labels": [],
                "masters": [],
                "uuids": []
            },
            "model": null,
            "partitions": {},
            "removable": "0",
            "rotational": "1",
            "sas_address": null,
            "sas_device_handle": null,
            "scheduler_mode": "none",
            "sectors": 113384,
            "sectorsize": "512",
            "size": "55.36 MB",
            "support_discard": "4096",
            "vendor": null,
            "virtual": 1
        },
        "loop6": {
            "holders": [],
            "host": "",
            "links": {
                "ids": [],
                "labels": [],
                "masters": [],
                "uuids": []
            },
            "model": null,
            "partitions": {},
            "removable": "0",
            "rotational": "1",
            "sas_address": null,
            "sas_device_handle": null,
            "scheduler_mode": "none",
            "sectors": 181376,
            "sectorsize": "512",
            "size": "88.56 MB",
            "support_discard": "4096",
            "vendor": null,
            "virtual": 1
        },
        "loop7": {
            "holders": [],
            "host": "",
            "links": {
                "ids": [],
                "labels": [],
                "masters": [],
                "uuids": []
            },
            "model": null,
            "partitions": {},
            "removable": "0",
            "rotational": "1",
            "sas_address": null,
            "sas_device_handle": null,
            "scheduler_mode": "none",
            "sectors": 0,
            "sectorsize": "512",
            "size": "0.00 Bytes",
            "support_discard": "4096",
            "vendor": null,
            "virtual": 1
        },
        "sda": {
            "holders": [],
            "host": "",
            "links": {
                "ids": [
                    "scsi-360dd210ad0864c21a7807ced149fefc1",
                    "wwn-0x60dd210ad0864c21a7807ced149fefc1"
                ],
                "labels": [],
                "masters": [],
                "uuids": []
            },
            "model": "BlockVolume",
            "partitions": {
                "sda1": {
                    "holders": [],
                    "links": {
                        "ids": [
                            "scsi-360dd210ad0864c21a7807ced149fefc1-part1",
                            "wwn-0x60dd210ad0864c21a7807ced149fefc1-part1"
                        ],
                        "labels": [
                            "cloudimg-rootfs"
                        ],
                        "masters": [],
                        "uuids": [
                            "ba398682-9547-45a5-858a-aad7620c10a3"
                        ]
                    },
                    "sectors": 104630239,
                    "sectorsize": 512,
                    "size": "49.89 GB",
                    "start": "227328",
                    "uuid": "ba398682-9547-45a5-858a-aad7620c10a3"
                },
                "sda14": {
                    "holders": [],
                    "links": {
                        "ids": [
                            "scsi-360dd210ad0864c21a7807ced149fefc1-part14",
                            "wwn-0x60dd210ad0864c21a7807ced149fefc1-part14"
                        ],
                        "labels": [],
                        "masters": [],
                        "uuids": []
                    },
                    "sectors": 8192,
                    "sectorsize": 512,
                    "size": "4.00 MB",
                    "start": "2048",
                    "uuid": null
                },
                "sda15": {
                    "holders": [],
                    "links": {
                        "ids": [
                            "scsi-360dd210ad0864c21a7807ced149fefc1-part15",
                            "wwn-0x60dd210ad0864c21a7807ced149fefc1-part15"
                        ],
                        "labels": [
                            "UEFI"
                        ],
                        "masters": [],
                        "uuids": [
                            "1FC5-9E05"
                        ]
                    },
                    "sectors": 217088,
                    "sectorsize": 512,
                    "size": "106.00 MB",
                    "start": "10240",
                    "uuid": "1FC5-9E05"
                }
            },
            "removable": "0",
            "rotational": "1",
            "sas_address": null,
            "sas_device_handle": null,
            "scheduler_mode": "none",
            "sectors": 104857600,
            "sectorsize": "512",
            "size": "50.00 GB",
            "support_discard": "32768",
            "vendor": "ORACLE",
            "virtual": 1,
            "wwn": "0x60dd210ad0864c21a7807ced149fefc1"
        }
    },
    "ansible_distribution": "Ubuntu",
    "ansible_distribution_file_parsed": true,
    "ansible_distribution_file_path": "/etc/os-release",
    "ansible_distribution_file_variety": "Debian",
    "ansible_distribution_major_version": "22",
    "ansible_distribution_release": "jammy",
    "ansible_distribution_version": "22.04",
    "ansible_dns": {
        "nameservers": [
            "127.0.0.53"
        ],
        "options": {
            "edns0": true,
            "trust-ad": true
        },
        "search": [
            "durgasri.oraclevcn.com"
        ]
    },
    "ansible_domain": "",
    "ansible_effective_group_id": 1001,
    "ansible_effective_user_id": 1001,
    "ansible_ens3": {
        "active": true,
        "device": "ens3",
        "features": {
            "esp_hw_offload": "off [fixed]",
            "esp_tx_csum_hw_offload": "off [fixed]",
            "fcoe_mtu": "off [fixed]",
            "generic_receive_offload": "on",
            "generic_segmentation_offload": "on",
            "highdma": "on [fixed]",
            "hsr_dup_offload": "off [fixed]",
            "hsr_fwd_offload": "off [fixed]",
            "hsr_tag_ins_offload": "off [fixed]",
            "hsr_tag_rm_offload": "off [fixed]",
            "hw_tc_offload": "off [fixed]",
            "l2_fwd_offload": "off [fixed]",
            "large_receive_offload": "off [fixed]",
            "loopback": "off [fixed]",
            "macsec_hw_offload": "off [fixed]",
            "netns_local": "off [fixed]",
            "ntuple_filters": "off [fixed]",
            "receive_hashing": "off [fixed]",
            "rx_all": "off [fixed]",
            "rx_checksumming": "on [fixed]",
            "rx_fcs": "off [fixed]",
            "rx_gro_hw": "on",
            "rx_gro_list": "off",
            "rx_udp_gro_forwarding": "off",
            "rx_udp_tunnel_port_offload": "off [fixed]",
            "rx_vlan_filter": "on [fixed]",
            "rx_vlan_offload": "off [fixed]",
            "rx_vlan_stag_filter": "off [fixed]",
            "rx_vlan_stag_hw_parse": "off [fixed]",
            "scatter_gather": "on",
            "tcp_segmentation_offload": "on",
            "tls_hw_record": "off [fixed]",
            "tls_hw_rx_offload": "off [fixed]",
            "tls_hw_tx_offload": "off [fixed]",
            "tx_checksum_fcoe_crc": "off [fixed]",
            "tx_checksum_ip_generic": "on",
            "tx_checksum_ipv4": "off [fixed]",
            "tx_checksum_ipv6": "off [fixed]",
            "tx_checksum_sctp": "off [fixed]",
            "tx_checksumming": "on",
            "tx_esp_segmentation": "off [fixed]",
            "tx_fcoe_segmentation": "off [fixed]",
            "tx_gre_csum_segmentation": "off [fixed]",
            "tx_gre_segmentation": "off [fixed]",
            "tx_gso_list": "off [fixed]",
            "tx_gso_partial": "off [fixed]",
            "tx_gso_robust": "on [fixed]",
            "tx_ipxip4_segmentation": "off [fixed]",
            "tx_ipxip6_segmentation": "off [fixed]",
            "tx_lockless": "off [fixed]",
            "tx_nocache_copy": "off",
            "tx_scatter_gather": "on",
            "tx_scatter_gather_fraglist": "off [fixed]",
            "tx_sctp_segmentation": "off [fixed]",
            "tx_tcp6_segmentation": "on",
            "tx_tcp_ecn_segmentation": "on",
            "tx_tcp_mangleid_segmentation": "off",
            "tx_tcp_segmentation": "on",
            "tx_tunnel_remcsum_segmentation": "off [fixed]",
            "tx_udp_segmentation": "off [fixed]",
            "tx_udp_tnl_csum_segmentation": "off [fixed]",
            "tx_udp_tnl_segmentation": "off [fixed]",
            "tx_vlan_offload": "off [fixed]",
            "tx_vlan_stag_hw_insert": "off [fixed]",
            "vlan_challenged": "off [fixed]"
        },
        "hw_timestamp_filters": [],
        "ipv4": {
            "address": "192.168.31.188",
            "broadcast": "",
            "netmask": "255.255.192.0",
            "network": "192.168.0.0",
            "prefix": "18"
        },
        "ipv6": [
            {
                "address": "fe80::17ff:fe02:b89a",
                "prefix": "64",
                "scope": "link"
            }
        ],
        "macaddress": "02:00:17:02:b8:9a",
        "module": "virtio_net",
        "mtu": 9000,
        "pciid": "virtio0",
        "promisc": false,
        "speed": -1,
        "timestamping": [],
        "type": "ether"
    },
    "ansible_env": {
        "DBUS_SESSION_BUS_ADDRESS": "unix:path=/run/user/1001/bus",
        "HOME": "/home/ubuntu",
        "LANG": "C.UTF-8",
        "LC_CTYPE": "C.UTF-8",
        "LOGNAME": "ubuntu",
        "MOTD_SHOWN": "pam",
        "PATH": "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin",
        "PWD": "/home/ubuntu",
        "SHELL": "/bin/bash",
        "SHLVL": "0",
        "SSH_CLIENT": "106.222.235.7 32137 22",
        "SSH_CONNECTION": "106.222.235.7 32137 192.168.31.188 22",
        "SSH_TTY": "/dev/pts/0",
        "TERM": "xterm-256color",
        "USER": "ubuntu",
        "XDG_RUNTIME_DIR": "/run/user/1001",
        "XDG_SESSION_CLASS": "user",
        "XDG_SESSION_ID": "67",
        "XDG_SESSION_TYPE": "tty",
        "_": "/bin/sh"
    },
    "ansible_fibre_channel_wwn": [],
    "ansible_fips": false,
    "ansible_flags": [
        "fpu",
        "vme",
        "de",
        "pse",
        "tsc",
        "msr",
        "pae",
        "mce",
        "cx8",
        "apic",
        "sep",
        "mtrr",
        "pge",
        "mca",
        "cmov",
        "pat",
        "pse36",
        "clflush",
        "mmx",
        "fxsr",
        "sse",
        "sse2",
        "ht",
        "syscall",
        "nx",
        "mmxext",
        "fxsr_opt",
        "pdpe1gb",
        "rdtscp",
        "lm",
        "rep_good",
        "nopl",
        "cpuid",
        "extd_apicid",
        "tsc_known_freq",
        "pni",
        "pclmulqdq",
        "ssse3",
        "fma",
        "cx16",
        "sse4_1",
        "sse4_2",
        "x2apic",
        "movbe",
        "popcnt",
        "tsc_deadline_timer",
        "aes",
        "xsave",
        "avx",
        "f16c",
        "rdrand",
        "hypervisor",
        "lahf_lm",
        "cmp_legacy",
        "cr8_legacy",
        "abm",
        "sse4a",
        "misalignsse",
        "3dnowprefetch",
        "osvw",
        "topoext",
        "perfctr_core",
        "ssbd",
        "ibpb",
        "vmmcall",
        "fsgsbase",
        "tsc_adjust",
        "bmi1",
        "avx2",
        "smep",
        "bmi2",
        "rdseed",
        "adx",
        "smap",
        "clflushopt",
        "sha_ni",
        "xsaveopt",
        "xsavec",
        "xgetbv1",
        "clzero",
        "xsaveerptr",
        "virt_ssbd",
        "arat",
        "arch_capabilities"
    ],
    "ansible_form_factor": "Other",
    "ansible_fqdn": "node-1",
    "ansible_hostname": "node-1",
    "ansible_hostnqn": "",
    "ansible_interfaces": [
        "ens3",
        "lo"
    ],
    "ansible_is_chroot": false,
    "ansible_iscsi_iqn": "",
    "ansible_kernel": "5.15.0-1045-oracle",
    "ansible_kernel_version": "#51-Ubuntu SMP Fri Sep 22 10:55:32 UTC 2023",
    "ansible_lo": {
        "active": true,
        "device": "lo",
        "features": {
            "esp_hw_offload": "off [fixed]",
            "esp_tx_csum_hw_offload": "off [fixed]",
            "fcoe_mtu": "off [fixed]",
            "generic_receive_offload": "on",
            "generic_segmentation_offload": "on",
            "highdma": "on [fixed]",
            "hsr_dup_offload": "off [fixed]",
            "hsr_fwd_offload": "off [fixed]",
            "hsr_tag_ins_offload": "off [fixed]",
            "hsr_tag_rm_offload": "off [fixed]",
            "hw_tc_offload": "off [fixed]",
            "l2_fwd_offload": "off [fixed]",
            "large_receive_offload": "off [fixed]",
            "loopback": "on [fixed]",
            "macsec_hw_offload": "off [fixed]",
            "netns_local": "on [fixed]",
            "ntuple_filters": "off [fixed]",
            "receive_hashing": "off [fixed]",
            "rx_all": "off [fixed]",
            "rx_checksumming": "on [fixed]",
            "rx_fcs": "off [fixed]",
            "rx_gro_hw": "off [fixed]",
            "rx_gro_list": "off",
            "rx_udp_gro_forwarding": "off",
            "rx_udp_tunnel_port_offload": "off [fixed]",
            "rx_vlan_filter": "off [fixed]",
            "rx_vlan_offload": "off [fixed]",
            "rx_vlan_stag_filter": "off [fixed]",
            "rx_vlan_stag_hw_parse": "off [fixed]",
            "scatter_gather": "on",
            "tcp_segmentation_offload": "on",
            "tls_hw_record": "off [fixed]",
            "tls_hw_rx_offload": "off [fixed]",
            "tls_hw_tx_offload": "off [fixed]",
            "tx_checksum_fcoe_crc": "off [fixed]",
            "tx_checksum_ip_generic": "on [fixed]",
            "tx_checksum_ipv4": "off [fixed]",
            "tx_checksum_ipv6": "off [fixed]",
            "tx_checksum_sctp": "on [fixed]",
            "tx_checksumming": "on",
            "tx_esp_segmentation": "off [fixed]",
            "tx_fcoe_segmentation": "off [fixed]",
            "tx_gre_csum_segmentation": "off [fixed]",
            "tx_gre_segmentation": "off [fixed]",
            "tx_gso_list": "on",
            "tx_gso_partial": "off [fixed]",
            "tx_gso_robust": "off [fixed]",
            "tx_ipxip4_segmentation": "off [fixed]",
            "tx_ipxip6_segmentation": "off [fixed]",
            "tx_lockless": "on [fixed]",
            "tx_nocache_copy": "off [fixed]",
            "tx_scatter_gather": "on [fixed]",
            "tx_scatter_gather_fraglist": "on [fixed]",
            "tx_sctp_segmentation": "on",
            "tx_tcp6_segmentation": "on",
            "tx_tcp_ecn_segmentation": "on",
            "tx_tcp_mangleid_segmentation": "on",
            "tx_tcp_segmentation": "on",
            "tx_tunnel_remcsum_segmentation": "off [fixed]",
            "tx_udp_segmentation": "on",
            "tx_udp_tnl_csum_segmentation": "off [fixed]",
            "tx_udp_tnl_segmentation": "off [fixed]",
            "tx_vlan_offload": "off [fixed]",
            "tx_vlan_stag_hw_insert": "off [fixed]",
            "vlan_challenged": "on [fixed]"
        },
        "hw_timestamp_filters": [],
        "ipv4": {
            "address": "127.0.0.1",
            "broadcast": "",
            "netmask": "255.0.0.0",
            "network": "127.0.0.0",
            "prefix": "8"
        },
        "ipv6": [
            {
                "address": "::1",
                "prefix": "128",
                "scope": "host"
            }
        ],
        "mtu": 65536,
        "promisc": false,
        "timestamping": [],
        "type": "loopback"
    },
    "ansible_loadavg": {
        "15m": 0.00537109375,
        "1m": 0.080078125,
        "5m": 0.0166015625
    },
    "ansible_local": {},
    "ansible_locally_reachable_ips": {
        "ipv4": [
            "127.0.0.0/8",
            "127.0.0.1",
            "192.168.31.188"
        ],
        "ipv6": [
            "::1",
            "fe80::17ff:fe02:b89a"
        ]
    },
    "ansible_lsb": {
        "codename": "jammy",
        "description": "Ubuntu 22.04.5 LTS",
        "id": "Ubuntu",
        "major_release": "22",
        "release": "22.04"
    },
    "ansible_lvm": "N/A",
    "ansible_machine": "x86_64",
    "ansible_machine_id": "8980dfb7466740dc9b3ee681654674c1",
    "ansible_memfree_mb": 78,
    "ansible_memory_mb": {
        "nocache": {
            "free": 715,
            "used": 237
        },
        "real": {
            "free": 78,
            "total": 952,
            "used": 874
        },
        "swap": {
            "cached": 0,
            "free": 0,
            "total": 0,
            "used": 0
        }
    },
    "ansible_memtotal_mb": 952,
    "ansible_mounts": [
        {
            "block_available": 10682554,
            "block_size": 4096,
            "block_total": 12655054,
            "block_used": 1972500,
            "device": "/dev/sda1",
            "dump": 0,
            "fstype": "ext4",
            "inode_available": 6341891,
            "inode_total": 6451200,
            "inode_used": 109309,
            "mount": "/",
            "options": "rw,relatime,discard,errors=remount-ro",
            "passno": 0,
            "size_available": 43755741184,
            "size_total": 51835101184,
            "uuid": "ba398682-9547-45a5-858a-aad7620c10a3"
        },
        {
            "block_available": 201337,
            "block_size": 512,
            "block_total": 213716,
            "block_used": 12379,
            "device": "/dev/sda15",
            "dump": 0,
            "fstype": "vfat",
            "inode_available": 0,
            "inode_total": 0,
            "inode_used": 0,
            "mount": "/boot/efi",
            "options": "rw,relatime,fmask=0077,dmask=0077,codepage=437,iocharset=iso8859-1,shortname=mixed,errors=remount-ro",
            "passno": 0,
            "size_available": 103084544,
            "size_total": 109422592,
            "uuid": "1FC5-9E05"
        },
        {
            "block_available": 0,
            "block_size": 131072,
            "block_total": 443,
            "block_used": 443,
            "device": "/dev/loop3",
            "dump": 0,
            "fstype": "squashfs",
            "inode_available": 0,
            "inode_total": 10767,
            "inode_used": 10767,
            "mount": "/snap/core18/2846",
            "options": "ro,nodev,relatime,errors=continue",
            "passno": 0,
            "size_available": 0,
            "size_total": 58064896,
            "uuid": "N/A"
        },
        {
            "block_available": 0,
            "block_size": 131072,
            "block_total": 619,
            "block_used": 619,
            "device": "/dev/loop4",
            "dump": 0,
            "fstype": "squashfs",
            "inode_available": 0,
            "inode_total": 405,
            "inode_used": 405,
            "mount": "/snap/oracle-cloud-agent/72",
            "options": "ro,nodev,relatime,errors=continue",
            "passno": 0,
            "size_available": 0,
            "size_total": 81133568,
            "uuid": "N/A"
        },
        {
            "block_available": 0,
            "block_size": 131072,
            "block_total": 356,
            "block_used": 356,
            "device": "/dev/loop2",
            "dump": 0,
            "fstype": "squashfs",
            "inode_available": 0,
            "inode_total": 608,
            "inode_used": 608,
            "mount": "/snap/snapd/23545",
            "options": "ro,nodev,relatime,errors=continue",
            "passno": 0,
            "size_available": 0,
            "size_total": 46661632,
            "uuid": "N/A"
        },
        {
            "block_available": 0,
            "block_size": 131072,
            "block_total": 443,
            "block_used": 443,
            "device": "/dev/loop5",
            "dump": 0,
            "fstype": "squashfs",
            "inode_available": 0,
            "inode_total": 10767,
            "inode_used": 10767,
            "mount": "/snap/core18/2855",
            "options": "ro,nodev,relatime,errors=continue",
            "passno": 0,
            "size_available": 0,
            "size_total": 58064896,
            "uuid": "N/A"
        },
        {
            "block_available": 0,
            "block_size": 131072,
            "block_total": 356,
            "block_used": 356,
            "device": "/dev/loop0",
            "dump": 0,
            "fstype": "squashfs",
            "inode_available": 0,
            "inode_total": 608,
            "inode_used": 608,
            "mount": "/snap/snapd/23771",
            "options": "ro,nodev,relatime,errors=continue",
            "passno": 0,
            "size_available": 0,
            "size_total": 46661632,
            "uuid": "N/A"
        },
        {
            "block_available": 0,
            "block_size": 131072,
            "block_total": 709,
            "block_used": 709,
            "device": "/dev/loop6",
            "dump": 0,
            "fstype": "squashfs",
            "inode_available": 0,
            "inode_total": 408,
            "inode_used": 408,
            "mount": "/snap/oracle-cloud-agent/94",
            "options": "ro,nodev,relatime,errors=continue",
            "passno": 0,
            "size_available": 0,
            "size_total": 92930048,
            "uuid": "N/A"
        }
    ],
    "ansible_nodename": "node-1",
    "ansible_os_family": "Debian",
    "ansible_pkg_mgr": "apt",
    "ansible_proc_cmdline": {
        "BOOT_IMAGE": "/boot/vmlinuz-5.15.0-1045-oracle",
        "console": [
            "tty1",
            "ttyS0"
        ],
        "crash_kexec_post_notifiers": true,
        "libiscsi.debug_libiscsi_eh": "1",
        "nvme.shutdown_timeout": "10",
        "ro": true,
        "root": "LABEL=cloudimg-rootfs"
    },
    "ansible_processor": [
        "0",
        "AuthenticAMD",
        "AMD EPYC 7551 32-Core Processor",
        "1",
        "AuthenticAMD",
        "AMD EPYC 7551 32-Core Processor"
    ],
    "ansible_processor_cores": 1,
    "ansible_processor_count": 1,
    "ansible_processor_nproc": 2,
    "ansible_processor_threads_per_core": 2,
    "ansible_processor_vcpus": 2,
    "ansible_product_name": "Standard PC (i440FX + PIIX, 1996)",
    "ansible_product_serial": "NA",
    "ansible_product_uuid": "NA",
    "ansible_product_version": "pc-i440fx-7.2",
    "ansible_python": {
        "executable": "/usr/bin/python3.11",
        "has_sslcontext": true,
        "type": "cpython",
        "version": {
            "major": 3,
            "micro": 0,
            "minor": 11,
            "releaselevel": "candidate",
            "serial": 1
        },
        "version_info": [
            3,
            11,
            0,
            "candidate",
            1
        ]
    },
    "ansible_python_version": "3.11.0rc1",
    "ansible_real_group_id": 1001,
    "ansible_real_user_id": 1001,
    "ansible_selinux": {
        "status": "disabled"
    },
    "ansible_selinux_python_present": true,
    "ansible_service_mgr": "systemd",
    "ansible_ssh_host_key_dsa_public": "AAAAB3NzaC1kc3MAAACBALsMAwyNCdsb06wjxJiSXiCjpCRC2NwcEbnWViXZUNbXB6TWzPIezd6s1rH1P6SECWgp/3cN7nYj1GCEE8sRZz7SCqmke+219gPen8XB6JFTOxyTEky5t66qdBW4Byts+gfH91xIwVuBsvP9rTSA0wqhCzDQMhY5P3PXemG69JBHAAAAFQDanrOYI0q1N/Ad87VGdGlNcoCUxwAAAIBetsCp0jDODujlFHjBQ4qY6qx5nOw/xCGO4W8VnFeRkVrjyivBd9T/PjA6CJiCPRwudU+Kj67lj8c8dd0jPIfPp6WRGI/AA/JUls8kvdxmhYtuhIMIxgMh+9oBK3wNDqP2UCtJZczK2fqHYw6zmXSXdsjCwkt5G5dJxtwm/UGVugAAAIAxS8+mP+PO/omecm3q2jRjlip2nu9QcaZkr2/+2oOto9uAqaSKOTbd2/k80XOuiFIdOuVzzAmrXsh0PiIg1VHjLF52k40PG3hQlw0PCFtlab6+fFqP/xEMD/FsU+xOFPRSHtON54QUS1wf/A/CDvXOcWYy4vOOVnCkm6xLc8mi7w==",
    "ansible_ssh_host_key_dsa_public_keytype": "ssh-dss",
    "ansible_ssh_host_key_ecdsa_public": "AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBM8DkYnmep3mOKJkBnZVV1spvxEI4dLoAPTuuYhUxxRs/m7veaDyVJrNGW7KRPIwI6pel9sfg8d0hO9v9eP2UBY=",
    "ansible_ssh_host_key_ecdsa_public_keytype": "ecdsa-sha2-nistp256",
    "ansible_ssh_host_key_ed25519_public": "AAAAC3NzaC1lZDI1NTE5AAAAIF7f2mqNYvfyZbZMInEviVEzHnagRttn10LhdilwyVAu",
    "ansible_ssh_host_key_ed25519_public_keytype": "ssh-ed25519",
    "ansible_ssh_host_key_rsa_public": "AAAAB3NzaC1yc2EAAAADAQABAAABgQCrAeV/ir3F+nmfRc/wIdqlEZOl/dOprckRqLbJYl1VE7S/qJm4OpwaB6/5SdnkfHjU6X9kiWqQWWk1Ccd1WUeNc0TiajkSBczGKC+w9tDhkX7rHpcmVSmAmrOzdsWAMDwimXdjvkGZNWwzwlP2Tc7bNjuMVVqSD9gPhcfAacCMB9SNHCVXHbRPE3yiLL2H3JMBdQYjNBYSa+LHsK0iNRPbudTWvu299rNOdeMcz60sMROgAUknL3Aj8wUarAezvUu+dUPFQ2vcSivqRuFcZ8Lur/AintrpqFNoP5dIqN/A6I8garOGeLzeTKE3muIV9KaSnd7Yy8raEqg/NisnKrKgDzFaKJmd2hmPXfStAGuGuiUY2QzlDEldmM5eXZcF5ji9pdyPYSxJxF6liO2AJGPC8+OQIXuoU4gCgPWDsWgu89+zQfV3Uh7JhlvtsrzsNYISXWj79Ao2DfHzMyimpiONcVSVvdnDXGSTawnW1dpJ/Ev35+/Ic6iiGQR+IhVIyu0=",
    "ansible_ssh_host_key_rsa_public_keytype": "ssh-rsa",
    "ansible_swapfree_mb": 0,
    "ansible_swaptotal_mb": 0,
    "ansible_system": "Linux",
    "ansible_system_capabilities": [
        ""
    ],
    "ansible_system_capabilities_enforced": "True",
    "ansible_system_vendor": "QEMU",
    "ansible_systemd": {
        "features": "+PAM +AUDIT +SELINUX +APPARMOR +IMA +SMACK +SECCOMP +GCRYPT +GNUTLS +OPENSSL +ACL +BLKID +CURL +ELFUTILS +FIDO2 +IDN2 -IDN +IPTC +KMOD +LIBCRYPTSETUP +LIBFDISK +PCRE2 -PWQUALITY -P11KIT -QRENCODE +BZIP2 +LZ4 +XZ +ZLIB +ZSTD -XKBCOMMON +UTMP +SYSVINIT default-hierarchy=unified",
        "version": 249
    },
    "ansible_uptime_seconds": 14294787,
    "ansible_user_dir": "/home/ubuntu",
    "ansible_user_gecos": "Ubuntu",
    "ansible_user_gid": 1001,
    "ansible_user_id": "ubuntu",
    "ansible_user_shell": "/bin/bash",
    "ansible_user_uid": 1001,
    "ansible_userspace_architecture": "x86_64",
    "ansible_userspace_bits": "64",
    "ansible_virtualization_role": "guest",
    "ansible_virtualization_tech_guest": [
        "kvm"
    ],
    "ansible_virtualization_tech_host": [],
    "ansible_virtualization_type": "kvm",
    "discovered_interpreter_python": "/usr/bin/python3.11",
    "gather_subset": [
        "all"
    ],
    "module_setup": true
}