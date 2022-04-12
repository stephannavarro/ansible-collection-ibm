```
pi_cloud_instance_id: YOUR_INSTANCE_ID
pi_api_key : YOUR_API_KEY
region : us-south
zone : us-south


cluster_vm_name_number: 2
cluster_vm_name_prefix: ZZNODE

sys_type: s922
pi_image: "7300-00-01"
proc_type: shared
processors: "0.25"
memory: "2"
ssh_public_key: "ansible-rac-45"
cluster: True
affinity_policy: { name: ZZ , policy: affinity }


data_disk_list:
  - { pi_volume_name: 'ZZOCR01' , pi_volume_size: 10 , pi_volume_type: tier3 ,  pi_volume_shareable: True }
  - { pi_volume_name: 'ZZOCR02' , pi_volume_size: 10 , pi_volume_type: tier3 ,  pi_volume_shareable: True }
  - { pi_volume_name: 'ZZOCR03' , pi_volume_size: 10 , pi_volume_type: tier3 ,  pi_volume_shareable: True }
  - { pi_volume_name: 'ZZREDO01' , pi_volume_size: 10 , pi_volume_type: tier3 ,  pi_volume_shareable: True }
  - { pi_volume_name: 'ZZREDO02' , pi_volume_size: 10 , pi_volume_type: tier3 ,  pi_volume_shareable: True }
  - { pi_volume_name: 'ZZREDO03' , pi_volume_size: 10 , pi_volume_type: tier3 ,  pi_volume_shareable: True }
  - { pi_volume_name: 'ZZDATA01' , pi_volume_size: 30 , pi_volume_type: tier3 ,  pi_volume_shareable: True }
  - { pi_volume_name: 'ZZDATA02' , pi_volume_size: 30 , pi_volume_type: tier3 ,  pi_volume_shareable: True }
  - { pi_volume_name: 'ZZDATA03' , pi_volume_size: 30 , pi_volume_type: tier3 ,  pi_volume_shareable: True }


private_rac_networks:
  - { pi_network_name: PVSDALLAS12_101_SN , pi_cidr: "192.168.101.0/24" , jumbo: True , pi_network_type: vlan }
  - { pi_network_name: RACA , pi_cidr: "192.168.120.0/24" , jumbo: True , pi_network_type: vlan }
  - { pi_network_name: RACB , pi_cidr: "192.168.120.0/24" , jumbo: True , pi_network_type: vlan }
  - { pi_network_name: RACC , pi_cidr: "192.168.122.0/24" , jumbo: True , pi_network_type: vlan  }
  - { pi_network_name: RACD , pi_cidr: "192.168.123.0/24" , jumbo: True , pi_network_type: vlan  }
  - { pi_network_name: RACE , pi_cidr: "192.168.124.0/24" , jumbo: True , pi_network_type: vlan  }

```
