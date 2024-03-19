# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['InventoryItemArgs', 'InventoryItem']

@pulumi.input_type
class InventoryItemArgs:
    def __init__(__self__, *,
                 device_id: pulumi.Input[int],
                 asset_tag: Optional[pulumi.Input[str]] = None,
                 component_id: Optional[pulumi.Input[int]] = None,
                 component_type: Optional[pulumi.Input[str]] = None,
                 custom_fields: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 discovered: Optional[pulumi.Input[bool]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 manufacturer_id: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parent_id: Optional[pulumi.Input[int]] = None,
                 part_id: Optional[pulumi.Input[str]] = None,
                 role_id: Optional[pulumi.Input[int]] = None,
                 serial: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a InventoryItem resource.
        :param pulumi.Input[int] component_id: Required when `component_type` is set.
        :param pulumi.Input[bool] discovered: Defaults to `false`.
        """
        pulumi.set(__self__, "device_id", device_id)
        if asset_tag is not None:
            pulumi.set(__self__, "asset_tag", asset_tag)
        if component_id is not None:
            pulumi.set(__self__, "component_id", component_id)
        if component_type is not None:
            pulumi.set(__self__, "component_type", component_type)
        if custom_fields is not None:
            pulumi.set(__self__, "custom_fields", custom_fields)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if discovered is not None:
            pulumi.set(__self__, "discovered", discovered)
        if label is not None:
            pulumi.set(__self__, "label", label)
        if manufacturer_id is not None:
            pulumi.set(__self__, "manufacturer_id", manufacturer_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if parent_id is not None:
            pulumi.set(__self__, "parent_id", parent_id)
        if part_id is not None:
            pulumi.set(__self__, "part_id", part_id)
        if role_id is not None:
            pulumi.set(__self__, "role_id", role_id)
        if serial is not None:
            pulumi.set(__self__, "serial", serial)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="deviceId")
    def device_id(self) -> pulumi.Input[int]:
        return pulumi.get(self, "device_id")

    @device_id.setter
    def device_id(self, value: pulumi.Input[int]):
        pulumi.set(self, "device_id", value)

    @property
    @pulumi.getter(name="assetTag")
    def asset_tag(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "asset_tag")

    @asset_tag.setter
    def asset_tag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "asset_tag", value)

    @property
    @pulumi.getter(name="componentId")
    def component_id(self) -> Optional[pulumi.Input[int]]:
        """
        Required when `component_type` is set.
        """
        return pulumi.get(self, "component_id")

    @component_id.setter
    def component_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "component_id", value)

    @property
    @pulumi.getter(name="componentType")
    def component_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "component_type")

    @component_type.setter
    def component_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "component_type", value)

    @property
    @pulumi.getter(name="customFields")
    def custom_fields(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "custom_fields")

    @custom_fields.setter
    def custom_fields(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "custom_fields", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def discovered(self) -> Optional[pulumi.Input[bool]]:
        """
        Defaults to `false`.
        """
        return pulumi.get(self, "discovered")

    @discovered.setter
    def discovered(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "discovered", value)

    @property
    @pulumi.getter
    def label(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "label")

    @label.setter
    def label(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "label", value)

    @property
    @pulumi.getter(name="manufacturerId")
    def manufacturer_id(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "manufacturer_id")

    @manufacturer_id.setter
    def manufacturer_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "manufacturer_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="parentId")
    def parent_id(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "parent_id")

    @parent_id.setter
    def parent_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "parent_id", value)

    @property
    @pulumi.getter(name="partId")
    def part_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "part_id")

    @part_id.setter
    def part_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "part_id", value)

    @property
    @pulumi.getter(name="roleId")
    def role_id(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "role_id")

    @role_id.setter
    def role_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "role_id", value)

    @property
    @pulumi.getter
    def serial(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "serial")

    @serial.setter
    def serial(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "serial", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _InventoryItemState:
    def __init__(__self__, *,
                 asset_tag: Optional[pulumi.Input[str]] = None,
                 component_id: Optional[pulumi.Input[int]] = None,
                 component_type: Optional[pulumi.Input[str]] = None,
                 custom_fields: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 device_id: Optional[pulumi.Input[int]] = None,
                 discovered: Optional[pulumi.Input[bool]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 manufacturer_id: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parent_id: Optional[pulumi.Input[int]] = None,
                 part_id: Optional[pulumi.Input[str]] = None,
                 role_id: Optional[pulumi.Input[int]] = None,
                 serial: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering InventoryItem resources.
        :param pulumi.Input[int] component_id: Required when `component_type` is set.
        :param pulumi.Input[bool] discovered: Defaults to `false`.
        """
        if asset_tag is not None:
            pulumi.set(__self__, "asset_tag", asset_tag)
        if component_id is not None:
            pulumi.set(__self__, "component_id", component_id)
        if component_type is not None:
            pulumi.set(__self__, "component_type", component_type)
        if custom_fields is not None:
            pulumi.set(__self__, "custom_fields", custom_fields)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if device_id is not None:
            pulumi.set(__self__, "device_id", device_id)
        if discovered is not None:
            pulumi.set(__self__, "discovered", discovered)
        if label is not None:
            pulumi.set(__self__, "label", label)
        if manufacturer_id is not None:
            pulumi.set(__self__, "manufacturer_id", manufacturer_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if parent_id is not None:
            pulumi.set(__self__, "parent_id", parent_id)
        if part_id is not None:
            pulumi.set(__self__, "part_id", part_id)
        if role_id is not None:
            pulumi.set(__self__, "role_id", role_id)
        if serial is not None:
            pulumi.set(__self__, "serial", serial)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="assetTag")
    def asset_tag(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "asset_tag")

    @asset_tag.setter
    def asset_tag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "asset_tag", value)

    @property
    @pulumi.getter(name="componentId")
    def component_id(self) -> Optional[pulumi.Input[int]]:
        """
        Required when `component_type` is set.
        """
        return pulumi.get(self, "component_id")

    @component_id.setter
    def component_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "component_id", value)

    @property
    @pulumi.getter(name="componentType")
    def component_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "component_type")

    @component_type.setter
    def component_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "component_type", value)

    @property
    @pulumi.getter(name="customFields")
    def custom_fields(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "custom_fields")

    @custom_fields.setter
    def custom_fields(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "custom_fields", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="deviceId")
    def device_id(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "device_id")

    @device_id.setter
    def device_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "device_id", value)

    @property
    @pulumi.getter
    def discovered(self) -> Optional[pulumi.Input[bool]]:
        """
        Defaults to `false`.
        """
        return pulumi.get(self, "discovered")

    @discovered.setter
    def discovered(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "discovered", value)

    @property
    @pulumi.getter
    def label(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "label")

    @label.setter
    def label(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "label", value)

    @property
    @pulumi.getter(name="manufacturerId")
    def manufacturer_id(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "manufacturer_id")

    @manufacturer_id.setter
    def manufacturer_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "manufacturer_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="parentId")
    def parent_id(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "parent_id")

    @parent_id.setter
    def parent_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "parent_id", value)

    @property
    @pulumi.getter(name="partId")
    def part_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "part_id")

    @part_id.setter
    def part_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "part_id", value)

    @property
    @pulumi.getter(name="roleId")
    def role_id(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "role_id")

    @role_id.setter
    def role_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "role_id", value)

    @property
    @pulumi.getter
    def serial(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "serial")

    @serial.setter
    def serial(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "serial", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class InventoryItem(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 asset_tag: Optional[pulumi.Input[str]] = None,
                 component_id: Optional[pulumi.Input[int]] = None,
                 component_type: Optional[pulumi.Input[str]] = None,
                 custom_fields: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 device_id: Optional[pulumi.Input[int]] = None,
                 discovered: Optional[pulumi.Input[bool]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 manufacturer_id: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parent_id: Optional[pulumi.Input[int]] = None,
                 part_id: Optional[pulumi.Input[str]] = None,
                 role_id: Optional[pulumi.Input[int]] = None,
                 serial: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        From the [official documentation](https://docs.netbox.dev/en/stable/models/dcim/inventoryitem/):

        > Inventory items represent hardware components installed within a device, such as a power supply or CPU or line card. They are intended to be used primarily for inventory purposes.

        ## Example Usage

        <!--Start PulumiCodeChooser -->
        ```python
        import pulumi
        import spk_pulumi_netbox as netbox

        # Note that some terraform code is not included in the example for brevity
        test_device = netbox.Device("testDevice",
            device_type_id=netbox_device_type["test"]["id"],
            tenant_id=netbox_tenant["test"]["id"],
            role_id=netbox_device_role["test"]["id"],
            site_id=netbox_site["test"]["id"])
        test_device_rear_port = netbox.DeviceRearPort("testDeviceRearPort",
            device_id=test_device.id,
            type="8p8c",
            positions=1,
            mark_connected=True)
        parent = netbox.InventoryItem("parent", device_id=test_device.id)
        test_inventory_item = netbox.InventoryItem("testInventoryItem",
            device_id=test_device.id,
            parent_id=parent.id,
            component_type="dcim.rearport",
            component_id=test_device_rear_port.id)
        ```
        <!--End PulumiCodeChooser -->

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] component_id: Required when `component_type` is set.
        :param pulumi.Input[bool] discovered: Defaults to `false`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: InventoryItemArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        From the [official documentation](https://docs.netbox.dev/en/stable/models/dcim/inventoryitem/):

        > Inventory items represent hardware components installed within a device, such as a power supply or CPU or line card. They are intended to be used primarily for inventory purposes.

        ## Example Usage

        <!--Start PulumiCodeChooser -->
        ```python
        import pulumi
        import spk_pulumi_netbox as netbox

        # Note that some terraform code is not included in the example for brevity
        test_device = netbox.Device("testDevice",
            device_type_id=netbox_device_type["test"]["id"],
            tenant_id=netbox_tenant["test"]["id"],
            role_id=netbox_device_role["test"]["id"],
            site_id=netbox_site["test"]["id"])
        test_device_rear_port = netbox.DeviceRearPort("testDeviceRearPort",
            device_id=test_device.id,
            type="8p8c",
            positions=1,
            mark_connected=True)
        parent = netbox.InventoryItem("parent", device_id=test_device.id)
        test_inventory_item = netbox.InventoryItem("testInventoryItem",
            device_id=test_device.id,
            parent_id=parent.id,
            component_type="dcim.rearport",
            component_id=test_device_rear_port.id)
        ```
        <!--End PulumiCodeChooser -->

        :param str resource_name: The name of the resource.
        :param InventoryItemArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(InventoryItemArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 asset_tag: Optional[pulumi.Input[str]] = None,
                 component_id: Optional[pulumi.Input[int]] = None,
                 component_type: Optional[pulumi.Input[str]] = None,
                 custom_fields: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 device_id: Optional[pulumi.Input[int]] = None,
                 discovered: Optional[pulumi.Input[bool]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 manufacturer_id: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parent_id: Optional[pulumi.Input[int]] = None,
                 part_id: Optional[pulumi.Input[str]] = None,
                 role_id: Optional[pulumi.Input[int]] = None,
                 serial: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = InventoryItemArgs.__new__(InventoryItemArgs)

            __props__.__dict__["asset_tag"] = asset_tag
            __props__.__dict__["component_id"] = component_id
            __props__.__dict__["component_type"] = component_type
            __props__.__dict__["custom_fields"] = custom_fields
            __props__.__dict__["description"] = description
            if device_id is None and not opts.urn:
                raise TypeError("Missing required property 'device_id'")
            __props__.__dict__["device_id"] = device_id
            __props__.__dict__["discovered"] = discovered
            __props__.__dict__["label"] = label
            __props__.__dict__["manufacturer_id"] = manufacturer_id
            __props__.__dict__["name"] = name
            __props__.__dict__["parent_id"] = parent_id
            __props__.__dict__["part_id"] = part_id
            __props__.__dict__["role_id"] = role_id
            __props__.__dict__["serial"] = serial
            __props__.__dict__["tags"] = tags
        super(InventoryItem, __self__).__init__(
            'netbox:index/inventoryItem:InventoryItem',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            asset_tag: Optional[pulumi.Input[str]] = None,
            component_id: Optional[pulumi.Input[int]] = None,
            component_type: Optional[pulumi.Input[str]] = None,
            custom_fields: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            description: Optional[pulumi.Input[str]] = None,
            device_id: Optional[pulumi.Input[int]] = None,
            discovered: Optional[pulumi.Input[bool]] = None,
            label: Optional[pulumi.Input[str]] = None,
            manufacturer_id: Optional[pulumi.Input[int]] = None,
            name: Optional[pulumi.Input[str]] = None,
            parent_id: Optional[pulumi.Input[int]] = None,
            part_id: Optional[pulumi.Input[str]] = None,
            role_id: Optional[pulumi.Input[int]] = None,
            serial: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'InventoryItem':
        """
        Get an existing InventoryItem resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] component_id: Required when `component_type` is set.
        :param pulumi.Input[bool] discovered: Defaults to `false`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _InventoryItemState.__new__(_InventoryItemState)

        __props__.__dict__["asset_tag"] = asset_tag
        __props__.__dict__["component_id"] = component_id
        __props__.__dict__["component_type"] = component_type
        __props__.__dict__["custom_fields"] = custom_fields
        __props__.__dict__["description"] = description
        __props__.__dict__["device_id"] = device_id
        __props__.__dict__["discovered"] = discovered
        __props__.__dict__["label"] = label
        __props__.__dict__["manufacturer_id"] = manufacturer_id
        __props__.__dict__["name"] = name
        __props__.__dict__["parent_id"] = parent_id
        __props__.__dict__["part_id"] = part_id
        __props__.__dict__["role_id"] = role_id
        __props__.__dict__["serial"] = serial
        __props__.__dict__["tags"] = tags
        return InventoryItem(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="assetTag")
    def asset_tag(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "asset_tag")

    @property
    @pulumi.getter(name="componentId")
    def component_id(self) -> pulumi.Output[Optional[int]]:
        """
        Required when `component_type` is set.
        """
        return pulumi.get(self, "component_id")

    @property
    @pulumi.getter(name="componentType")
    def component_type(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "component_type")

    @property
    @pulumi.getter(name="customFields")
    def custom_fields(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        return pulumi.get(self, "custom_fields")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="deviceId")
    def device_id(self) -> pulumi.Output[int]:
        return pulumi.get(self, "device_id")

    @property
    @pulumi.getter
    def discovered(self) -> pulumi.Output[Optional[bool]]:
        """
        Defaults to `false`.
        """
        return pulumi.get(self, "discovered")

    @property
    @pulumi.getter
    def label(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "label")

    @property
    @pulumi.getter(name="manufacturerId")
    def manufacturer_id(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "manufacturer_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="parentId")
    def parent_id(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "parent_id")

    @property
    @pulumi.getter(name="partId")
    def part_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "part_id")

    @property
    @pulumi.getter(name="roleId")
    def role_id(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "role_id")

    @property
    @pulumi.getter
    def serial(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "serial")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "tags")

