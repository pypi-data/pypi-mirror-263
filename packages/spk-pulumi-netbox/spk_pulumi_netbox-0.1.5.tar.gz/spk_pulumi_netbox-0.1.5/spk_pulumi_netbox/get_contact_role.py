# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetContactRoleResult',
    'AwaitableGetContactRoleResult',
    'get_contact_role',
    'get_contact_role_output',
]

@pulumi.output_type
class GetContactRoleResult:
    """
    A collection of values returned by getContactRole.
    """
    def __init__(__self__, id=None, name=None, slug=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if slug and not isinstance(slug, str):
            raise TypeError("Expected argument 'slug' to be a str")
        pulumi.set(__self__, "slug", slug)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        At least one of `name` or `slug` must be given.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def slug(self) -> str:
        """
        At least one of `name` or `slug` must be given.
        """
        return pulumi.get(self, "slug")


class AwaitableGetContactRoleResult(GetContactRoleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetContactRoleResult(
            id=self.id,
            name=self.name,
            slug=self.slug)


def get_contact_role(name: Optional[str] = None,
                     slug: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetContactRoleResult:
    """
    Use this data source to access information about an existing resource.

    :param str name: At least one of `name` or `slug` must be given.
    :param str slug: At least one of `name` or `slug` must be given.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['slug'] = slug
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('netbox:index/getContactRole:getContactRole', __args__, opts=opts, typ=GetContactRoleResult).value

    return AwaitableGetContactRoleResult(
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        slug=pulumi.get(__ret__, 'slug'))


@_utilities.lift_output_func(get_contact_role)
def get_contact_role_output(name: Optional[pulumi.Input[Optional[str]]] = None,
                            slug: Optional[pulumi.Input[Optional[str]]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetContactRoleResult]:
    """
    Use this data source to access information about an existing resource.

    :param str name: At least one of `name` or `slug` must be given.
    :param str slug: At least one of `name` or `slug` must be given.
    """
    ...
