#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_compute_autoscale_group
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/compute_autoscale_group

short_description: Configure IBM Cloud 'ibm_compute_autoscale_group' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_compute_autoscale_group' resource
    - This module does not support idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.37.1
    - Terraform v0.12.20

options:
    tags:
        description:
            - List of tags
        required: False
        type: list
        elements: str
    maximum_member_count:
        description:
            - (Required for new resource) Maximum member count
        required: True
        type: int
    cooldown:
        description:
            - (Required for new resource) Cooldown value
        required: True
        type: int
    termination_policy:
        description:
            - (Required for new resource) Termination policy
        required: True
        type: str
    port:
        description:
            - Port number
        required: False
        type: int
    health_check:
        description:
            - None
        required: False
        type: dict
    virtual_guest_member_template:
        description:
            - (Required for new resource) Virtual guest member template
        required: True
        type: list
        elements: dict
    network_vlan_ids:
        description:
            - List of network VLAN ids
        required: False
        type: list
        elements: int
    name:
        description:
            - (Required for new resource) Name
        required: True
        type: str
    regional_group:
        description:
            - (Required for new resource) regional group
        required: True
        type: str
    minimum_member_count:
        description:
            - (Required for new resource) Minimum member count
        required: True
        type: int
    virtual_server_id:
        description:
            - virtual server ID
        required: False
        type: int
    id:
        description:
            - (Required when updating or destroying existing resource) IBM Cloud Resource ID.
        required: False
        type: str
    state:
        description:
            - State of resource
        choices:
            - available
            - absent
        default: available
        required: False
    iaas_classic_username:
        description:
            - (Required when generation = 1) The IBM Cloud Classic
              Infrastructure (SoftLayer) user name. This can also be provided
              via the environment variable 'IAAS_CLASSIC_USERNAME'.
        required: False
    iaas_classic_api_key:
        description:
            - (Required when generation = 1) The IBM Cloud Classic
              Infrastructure API key. This can also be provided via the
              environment variable 'IAAS_CLASSIC_API_KEY'.
        required: False
    region:
        description:
            - The IBM Cloud region where you want to create your
              resources. If this value is not specified, us-south is
              used by default. This can also be provided via the
              environment variable 'IC_REGION'.
        default: us-south
        required: False
    ibmcloud_api_key:
        description:
            - The IBM Cloud API key to authenticate with the IBM Cloud
              platform. This can also be provided via the environment
              variable 'IC_API_KEY'.
        required: True

author:
    - Jay Carman (@jaywcarman)
'''

# Top level parameter keys required by Terraform module
TL_REQUIRED_PARAMETERS = [
    ('maximum_member_count', 'int'),
    ('cooldown', 'int'),
    ('termination_policy', 'str'),
    ('virtual_guest_member_template', 'list'),
    ('name', 'str'),
    ('regional_group', 'str'),
    ('minimum_member_count', 'int'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'tags',
    'maximum_member_count',
    'cooldown',
    'termination_policy',
    'port',
    'health_check',
    'virtual_guest_member_template',
    'network_vlan_ids',
    'name',
    'regional_group',
    'minimum_member_count',
    'virtual_server_id',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
]

TL_ALL_PARAMETERS_DS = [
]

TL_CONFLICTS_MAP = {
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    tags=dict(
        required=False,
        elements='',
        type='list'),
    maximum_member_count=dict(
        required=False,
        type='int'),
    cooldown=dict(
        required=False,
        type='int'),
    termination_policy=dict(
        required=False,
        type='str'),
    port=dict(
        required=False,
        type='int'),
    health_check=dict(
        required=False,
        type='dict'),
    virtual_guest_member_template=dict(
        required=False,
        elements='',
        type='list'),
    network_vlan_ids=dict(
        required=False,
        elements='',
        type='list'),
    name=dict(
        required=False,
        type='str'),
    regional_group=dict(
        required=False,
        type='str'),
    minimum_member_count=dict(
        required=False,
        type='int'),
    virtual_server_id=dict(
        required=False,
        type='int'),
    id=dict(
        required=False,
        type='str'),
    state=dict(
        type='str',
        required=False,
        default='available',
        choices=(['available', 'absent'])),
    iaas_classic_username=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IAAS_CLASSIC_USERNAME']),
        required=False),
    iaas_classic_api_key=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IAAS_CLASSIC_API_KEY']),
        required=False),
    region=dict(
        type='str',
        fallback=(env_fallback, ['IC_REGION']),
        default='us-south'),
    ibmcloud_api_key=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IC_API_KEY']),
        required=True)
)


def run_module():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    # New resource required arguments checks
    missing_args = []
    if module.params['id'] is None:
        for arg, _ in TL_REQUIRED_PARAMETERS:
            if module.params[arg] is None:
                missing_args.append(arg)
        if missing_args:
            module.fail_json(msg=(
                "missing required arguments: " + ", ".join(missing_args)))

    conflicts = {}
    if len(TL_CONFLICTS_MAP) != 0:
        for arg in TL_CONFLICTS_MAP:
            if module.params[arg]:
                for conflict in TL_CONFLICTS_MAP[arg]:
                    try:
                        if module.params[conflict]:
                            conflicts[arg] = conflict
                    except KeyError:
                        pass
    if len(conflicts):
        module.fail_json(msg=("conflicts exist: {}".format(conflicts)))

    result = ibmcloud_terraform(
        resource_type='ibm_compute_autoscale_group',
        tf_type='resource',
        parameters=module.params,
        ibm_provider_version='1.37.1',
        tl_required_params=TL_REQUIRED_PARAMETERS,
        tl_all_params=TL_ALL_PARAMETERS)

    if result['rc'] > 0:
        module.fail_json(
            msg=Terraform.parse_stderr(result['stderr']), **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
