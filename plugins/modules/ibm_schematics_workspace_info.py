#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_schematics_workspace_info
short_description: Retrieve IBM Cloud 'ibm_schematics_workspace' resource

version_added: "2.8"

description:
    - Retrieve an IBM Cloud 'ibm_schematics_workspace' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.2.5
    - Terraform v0.12.20

options:
    template_id:
        description:
            - The id of templates
        required: False
        type: list
        elements: str
    name:
        description:
            - The name of workspace
        required: False
        type: str
    resource_group:
        description:
            - The resource group of workspace
        required: False
        type: str
    types:
        description:
            - None
        required: False
        type: list
        elements: str
    tags:
        description:
            - None
        required: False
        type: list
        elements: str
    workspace_id:
        description:
            - The id of workspace
        required: True
        type: str
    status:
        description:
            - The status of workspace
        required: False
        type: str
    is_frozen:
        description:
            - None
        required: False
        type: bool
    is_locked:
        description:
            - None
        required: False
        type: bool
    resource_controller_url:
        description:
            - The URL of the IBM Cloud dashboard that can be used to explore and view details about this workspace
        required: False
        type: str
    ibmcloud_api_key:
        description:
            - The API Key used for authentification. This can also be
              provided via the environment variable 'IC_API_KEY'.
        required: True
    ibmcloud_region:
        description:
            - Denotes which IBM Cloud region to connect to
        default: us-south
        required: False
    ibmcloud_zone:
        description:
            - Denotes which IBM Cloud zone to connect to in multizone
              environment. This can also be provided via the environmental
              variable 'IC_ZONE'.
        required: False

author:
    - Jay Carman (@jaywcarman)
'''

# Top level parameter keys required by Terraform module
TL_REQUIRED_PARAMETERS = [
    ('workspace_id', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'template_id',
    'name',
    'resource_group',
    'types',
    'tags',
    'workspace_id',
    'status',
    'is_frozen',
    'is_locked',
    'resource_controller_url',
]

# define available arguments/parameters a user can pass to the module
from ansible.module_utils.basic import env_fallback
module_args = dict(
    template_id=dict(
        required=False,
        elements='',
        type='list'),
    name=dict(
        required=False,
        type='str'),
    resource_group=dict(
        required=False,
        type='str'),
    types=dict(
        required=False,
        elements='',
        type='list'),
    tags=dict(
        required=False,
        elements='',
        type='list'),
    workspace_id=dict(
        required=True,
        type='str'),
    status=dict(
        required=False,
        type='str'),
    is_frozen=dict(
        required=False,
        type='bool'),
    is_locked=dict(
        required=False,
        type='bool'),
    resource_controller_url=dict(
        required=False,
        type='str'),
    ibmcloud_api_key=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IC_API_KEY']),
        required=True),
    ibmcloud_region=dict(
        type='str',
        fallback=(env_fallback, ['IC_REGION']),
        default='us-south'),
    ibmcloud_zone=dict(
        type='str',
        fallback=(env_fallback, ['IC_ZONE']))
)


def run_module():
    from ansible.module_utils.basic import AnsibleModule
    import ansible.module_utils.ibmcloud as ibmcloud

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    result = ibmcloud.ibmcloud_terraform(
        resource_type='ibm_schematics_workspace',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.2.5',
        tl_required_params=TL_REQUIRED_PARAMETERS,
        tl_all_params=TL_ALL_PARAMETERS)

    if result['rc'] > 0:
        module.fail_json(
            msg=ibmcloud.Terraform.parse_stderr(result['stderr']), **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
