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
    'GetVlanGroupResult',
    'AwaitableGetVlanGroupResult',
    'get_vlan_group',
    'get_vlan_group_output',
]

@pulumi.output_type
class GetVlanGroupResult:
    """
    A collection of values returned by getVlanGroup.
    """
    def __init__(__self__, description=None, id=None, max_vid=None, min_vid=None, name=None, scope_id=None, scope_type=None, slug=None, vlan_count=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if max_vid and not isinstance(max_vid, int):
            raise TypeError("Expected argument 'max_vid' to be a int")
        pulumi.set(__self__, "max_vid", max_vid)
        if min_vid and not isinstance(min_vid, int):
            raise TypeError("Expected argument 'min_vid' to be a int")
        pulumi.set(__self__, "min_vid", min_vid)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if scope_id and not isinstance(scope_id, int):
            raise TypeError("Expected argument 'scope_id' to be a int")
        pulumi.set(__self__, "scope_id", scope_id)
        if scope_type and not isinstance(scope_type, str):
            raise TypeError("Expected argument 'scope_type' to be a str")
        pulumi.set(__self__, "scope_type", scope_type)
        if slug and not isinstance(slug, str):
            raise TypeError("Expected argument 'slug' to be a str")
        pulumi.set(__self__, "slug", slug)
        if vlan_count and not isinstance(vlan_count, int):
            raise TypeError("Expected argument 'vlan_count' to be a int")
        pulumi.set(__self__, "vlan_count", vlan_count)

    @property
    @pulumi.getter
    def description(self) -> str:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="maxVid")
    def max_vid(self) -> int:
        return pulumi.get(self, "max_vid")

    @property
    @pulumi.getter(name="minVid")
    def min_vid(self) -> int:
        return pulumi.get(self, "min_vid")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        At least one of `name` or `slug` must be given.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="scopeId")
    def scope_id(self) -> Optional[int]:
        """
        Required when `scope_type` is set.
        """
        return pulumi.get(self, "scope_id")

    @property
    @pulumi.getter(name="scopeType")
    def scope_type(self) -> Optional[str]:
        """
        Valid values are `dcim.location`, `dcim.site`, `dcim.sitegroup`, `dcim.region`, `dcim.rack`, `virtualization.cluster` and `virtualization.clustergroup`.
        """
        return pulumi.get(self, "scope_type")

    @property
    @pulumi.getter
    def slug(self) -> str:
        """
        At least one of `name` or `slug` must be given.
        """
        return pulumi.get(self, "slug")

    @property
    @pulumi.getter(name="vlanCount")
    def vlan_count(self) -> int:
        return pulumi.get(self, "vlan_count")


class AwaitableGetVlanGroupResult(GetVlanGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVlanGroupResult(
            description=self.description,
            id=self.id,
            max_vid=self.max_vid,
            min_vid=self.min_vid,
            name=self.name,
            scope_id=self.scope_id,
            scope_type=self.scope_type,
            slug=self.slug,
            vlan_count=self.vlan_count)


def get_vlan_group(name: Optional[str] = None,
                   scope_id: Optional[int] = None,
                   scope_type: Optional[str] = None,
                   slug: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVlanGroupResult:
    """
    ## Example Usage

    <!--Start PulumiCodeChooser -->
    ```python
    import pulumi
    import pulumi_netbox as netbox

    example1 = netbox.get_vlan_group(name="example1")
    example2 = netbox.get_vlan_group(slug="example2")
    example3 = netbox.get_vlan_group(name="example",
        scope_type="dcim.site",
        scope_id=netbox_site["example"]["id"])
    ```
    <!--End PulumiCodeChooser -->


    :param str name: At least one of `name` or `slug` must be given.
    :param int scope_id: Required when `scope_type` is set.
    :param str scope_type: Valid values are `dcim.location`, `dcim.site`, `dcim.sitegroup`, `dcim.region`, `dcim.rack`, `virtualization.cluster` and `virtualization.clustergroup`.
    :param str slug: At least one of `name` or `slug` must be given.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['scopeId'] = scope_id
    __args__['scopeType'] = scope_type
    __args__['slug'] = slug
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('netbox:index/getVlanGroup:getVlanGroup', __args__, opts=opts, typ=GetVlanGroupResult).value

    return AwaitableGetVlanGroupResult(
        description=pulumi.get(__ret__, 'description'),
        id=pulumi.get(__ret__, 'id'),
        max_vid=pulumi.get(__ret__, 'max_vid'),
        min_vid=pulumi.get(__ret__, 'min_vid'),
        name=pulumi.get(__ret__, 'name'),
        scope_id=pulumi.get(__ret__, 'scope_id'),
        scope_type=pulumi.get(__ret__, 'scope_type'),
        slug=pulumi.get(__ret__, 'slug'),
        vlan_count=pulumi.get(__ret__, 'vlan_count'))


@_utilities.lift_output_func(get_vlan_group)
def get_vlan_group_output(name: Optional[pulumi.Input[Optional[str]]] = None,
                          scope_id: Optional[pulumi.Input[Optional[int]]] = None,
                          scope_type: Optional[pulumi.Input[Optional[str]]] = None,
                          slug: Optional[pulumi.Input[Optional[str]]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVlanGroupResult]:
    """
    ## Example Usage

    <!--Start PulumiCodeChooser -->
    ```python
    import pulumi
    import pulumi_netbox as netbox

    example1 = netbox.get_vlan_group(name="example1")
    example2 = netbox.get_vlan_group(slug="example2")
    example3 = netbox.get_vlan_group(name="example",
        scope_type="dcim.site",
        scope_id=netbox_site["example"]["id"])
    ```
    <!--End PulumiCodeChooser -->


    :param str name: At least one of `name` or `slug` must be given.
    :param int scope_id: Required when `scope_type` is set.
    :param str scope_type: Valid values are `dcim.location`, `dcim.site`, `dcim.sitegroup`, `dcim.region`, `dcim.rack`, `virtualization.cluster` and `virtualization.clustergroup`.
    :param str slug: At least one of `name` or `slug` must be given.
    """
    ...
