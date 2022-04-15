
# Confg file :

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
# IBM Power Virtual Server in IBM Cloud

This example creates a Power Systems Virtual Server running AIX or IBMi. The
server is configured to allow incoming SSH connections through a publicly
accessible IP address and authenticated using the provided SSH key.

## Power Systems Virtual Server Resources

The following infrastructure resources will be created (Ansible modules in
parentheses):

* SSH Key (ibm_pi_key)
* Network (ibm_pi_network)
* Virtual Server Instance (ibm_pi_instance)

## Configuration Parameters

The following parameters can be set by the user:

* `pi_name`: Name assigned to Virtual Server Instance
* `sys_type`: The type of system on which to create the VM (s922/e880/any)
* `pi_image`: VM image name ([retrieve available images])
* `proc_type`: The type of processor mode in which the VM will run
               (shared/dedicated)
* `processors`: The number of vCPUs to assign to the VM (as visibile within the
                guest operating system)
* `memory`: The amount of memory (GB) to assign to the VM
* `pi_cloud_instance_id`: The cloud_instance_id for this account
* `ssh_public_key`: The value of the ssh public key to be authorized for SSH
                    access

## Running

### Set API Key and Region

1. [Obtain an IBM Cloud API key].

2. Export your API key to the `IC_API_KEY` environment variable:

    ```
    export IC_API_KEY=<YOUR_API_KEY_HERE>
    ```

    Note: Modules also support the 'ibmcloud_api_key' parameter, but it is
    recommended to only use this when encrypting your API key value.

3. Export desired IBM Cloud region to the 'IC_REGION' environment variable:

    ```
    export IC_REGION=<REGION_NAME_HERE>
    ```

    Note: Modules also support the 'ibmcloud_region' parameter.

4. Export desired IBM Cloud zone to the 'IC_ZONE' environment variable:

    ```
    export IC_ZONE=<ZONE_NAMW_HERE>
    ```

    Note: This is used of multizone supported power instances.

### Create

1. To create all resources and test public SSH connection to the VM, run the
   'create' playbook:

    ```
    ansible-playbook create.yml
    ```

### List Available PI VM Images

1. To list available images run the 'list_pi_images' playbook. *note: Images
   are specific to a PI instance, and thus the 'pi_cloud_instance_id' var
   must be set before running this playbook.:

    ```
    ansible-playbook list_pi_images.yml
    ```

[retrieve available images]: #list-available-pi-images
[Ansible search path]: https://docs.ansible.com/ansible/latest/dev_guide/overview_architecture.html#ansible-search-path
