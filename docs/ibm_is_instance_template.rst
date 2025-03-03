
ibm_is_instance_template -- Configure IBM Cloud 'ibm_is_instance_template' resource
===================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_is_instance_template' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/is_instance_template

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.37.1
- Terraform v0.12.20



Parameters
----------

  name (True, str, None)
    (Required for new resource) Instance Template name


  vpc (True, str, None)
    (Required for new resource) VPC id


  dedicated_host (False, str, None)
    Unique Identifier of the Dedicated Host where the instance will be placed


  image (True, str, None)
    (Required for new resource) image name


  zone (True, str, None)
    (Required for new resource) Zone name


  profile (True, str, None)
    (Required for new resource) Profile info


  dedicated_host_group (False, str, None)
    Unique Identifier of the Dedicated Host Group where the instance will be placed


  user_data (False, str, None)
    User data given for the instance


  resource_group (False, str, None)
    Instance template resource group


  total_volume_bandwidth (False, int, None)
    The amount of bandwidth (in megabits per second) allocated exclusively to instance storage volumes


  primary_network_interface (True, list, None)
    (Required for new resource) Primary Network interface info


  network_interfaces (False, list, None)
    None


  keys (True, list, None)
    (Required for new resource) SSH key Ids for the instance template


  placement_group (False, str, None)
    Unique Identifier of the Placement Group for restricting the placement of the instance


  volume_attachments (False, list, None)
    None


  boot_volume (False, list, None)
    None


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  generation (False, int, 2)
    The generation of Virtual Private Cloud infrastructure that you want to use. Supported values are 1 for VPC generation 1, and 2 for VPC generation 2 infrastructure. If this value is not specified, 2 is used by default. This can also be provided via the environment variable 'IC_GENERATION'.


  region (False, str, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

