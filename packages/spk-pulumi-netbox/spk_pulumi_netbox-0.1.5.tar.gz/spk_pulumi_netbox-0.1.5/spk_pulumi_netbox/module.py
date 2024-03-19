# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ModuleArgs', 'Module']

@pulumi.input_type
class ModuleArgs:
    def __init__(__self__, *,
                 device_id: pulumi.Input[int],
                 module_bay_id: pulumi.Input[int],
                 module_type_id: pulumi.Input[int],
                 status: pulumi.Input[str],
                 asset_tag: Optional[pulumi.Input[str]] = None,
                 comments: Optional[pulumi.Input[str]] = None,
                 custom_fields: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 serial: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Module resource.
        :param pulumi.Input[str] status: One of [offline, active, planned, staged, failed, decommissioning].
        """
        pulumi.set(__self__, "device_id", device_id)
        pulumi.set(__self__, "module_bay_id", module_bay_id)
        pulumi.set(__self__, "module_type_id", module_type_id)
        pulumi.set(__self__, "status", status)
        if asset_tag is not None:
            pulumi.set(__self__, "asset_tag", asset_tag)
        if comments is not None:
            pulumi.set(__self__, "comments", comments)
        if custom_fields is not None:
            pulumi.set(__self__, "custom_fields", custom_fields)
        if description is not None:
            pulumi.set(__self__, "description", description)
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
    @pulumi.getter(name="moduleBayId")
    def module_bay_id(self) -> pulumi.Input[int]:
        return pulumi.get(self, "module_bay_id")

    @module_bay_id.setter
    def module_bay_id(self, value: pulumi.Input[int]):
        pulumi.set(self, "module_bay_id", value)

    @property
    @pulumi.getter(name="moduleTypeId")
    def module_type_id(self) -> pulumi.Input[int]:
        return pulumi.get(self, "module_type_id")

    @module_type_id.setter
    def module_type_id(self, value: pulumi.Input[int]):
        pulumi.set(self, "module_type_id", value)

    @property
    @pulumi.getter
    def status(self) -> pulumi.Input[str]:
        """
        One of [offline, active, planned, staged, failed, decommissioning].
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: pulumi.Input[str]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter(name="assetTag")
    def asset_tag(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "asset_tag")

    @asset_tag.setter
    def asset_tag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "asset_tag", value)

    @property
    @pulumi.getter
    def comments(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "comments")

    @comments.setter
    def comments(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "comments", value)

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
class _ModuleState:
    def __init__(__self__, *,
                 asset_tag: Optional[pulumi.Input[str]] = None,
                 comments: Optional[pulumi.Input[str]] = None,
                 custom_fields: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 device_id: Optional[pulumi.Input[int]] = None,
                 module_bay_id: Optional[pulumi.Input[int]] = None,
                 module_type_id: Optional[pulumi.Input[int]] = None,
                 serial: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering Module resources.
        :param pulumi.Input[str] status: One of [offline, active, planned, staged, failed, decommissioning].
        """
        if asset_tag is not None:
            pulumi.set(__self__, "asset_tag", asset_tag)
        if comments is not None:
            pulumi.set(__self__, "comments", comments)
        if custom_fields is not None:
            pulumi.set(__self__, "custom_fields", custom_fields)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if device_id is not None:
            pulumi.set(__self__, "device_id", device_id)
        if module_bay_id is not None:
            pulumi.set(__self__, "module_bay_id", module_bay_id)
        if module_type_id is not None:
            pulumi.set(__self__, "module_type_id", module_type_id)
        if serial is not None:
            pulumi.set(__self__, "serial", serial)
        if status is not None:
            pulumi.set(__self__, "status", status)
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
    @pulumi.getter
    def comments(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "comments")

    @comments.setter
    def comments(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "comments", value)

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
    @pulumi.getter(name="moduleBayId")
    def module_bay_id(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "module_bay_id")

    @module_bay_id.setter
    def module_bay_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "module_bay_id", value)

    @property
    @pulumi.getter(name="moduleTypeId")
    def module_type_id(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "module_type_id")

    @module_type_id.setter
    def module_type_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "module_type_id", value)

    @property
    @pulumi.getter
    def serial(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "serial")

    @serial.setter
    def serial(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "serial", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        One of [offline, active, planned, staged, failed, decommissioning].
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class Module(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 asset_tag: Optional[pulumi.Input[str]] = None,
                 comments: Optional[pulumi.Input[str]] = None,
                 custom_fields: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 device_id: Optional[pulumi.Input[int]] = None,
                 module_bay_id: Optional[pulumi.Input[int]] = None,
                 module_type_id: Optional[pulumi.Input[int]] = None,
                 serial: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        From the [official documentation](https://docs.netbox.dev/en/stable/models/dcim/module/):

        > A module is a field-replaceable hardware component installed within a device which houses its own child components. The most common example is a chassis-based router or switch.

        Similar to devices, modules are instantiated from module types, and any components associated with the module type are automatically instantiated on the new model. Each module must be installed within a module bay on a device, and each module bay may have only one module installed in it.

        ## Example Usage

        <!--Start PulumiCodeChooser -->
        ```python
        import pulumi
        import spk_pulumi_netbox as netbox

        # Note that some terraform code is not included in the example for brevity
        test_device = netbox.Device("testDevice",
            device_type_id=netbox_device_type["test"]["id"],
            role_id=netbox_device_role["test"]["id"],
            site_id=netbox_site["test"]["id"])
        test_device_module_bay = netbox.DeviceModuleBay("testDeviceModuleBay", device_id=test_device.id)
        test_manufacturer = netbox.Manufacturer("testManufacturer")
        test_module_type = netbox.ModuleType("testModuleType",
            manufacturer_id=test_manufacturer.id,
            model="Networking")
        test_module = netbox.Module("testModule",
            device_id=test_device.id,
            module_bay_id=test_device_module_bay.id,
            module_type_id=test_module_type.id,
            status="active",
            description="SFP card")
        ```
        <!--End PulumiCodeChooser -->

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] status: One of [offline, active, planned, staged, failed, decommissioning].
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ModuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        From the [official documentation](https://docs.netbox.dev/en/stable/models/dcim/module/):

        > A module is a field-replaceable hardware component installed within a device which houses its own child components. The most common example is a chassis-based router or switch.

        Similar to devices, modules are instantiated from module types, and any components associated with the module type are automatically instantiated on the new model. Each module must be installed within a module bay on a device, and each module bay may have only one module installed in it.

        ## Example Usage

        <!--Start PulumiCodeChooser -->
        ```python
        import pulumi
        import spk_pulumi_netbox as netbox

        # Note that some terraform code is not included in the example for brevity
        test_device = netbox.Device("testDevice",
            device_type_id=netbox_device_type["test"]["id"],
            role_id=netbox_device_role["test"]["id"],
            site_id=netbox_site["test"]["id"])
        test_device_module_bay = netbox.DeviceModuleBay("testDeviceModuleBay", device_id=test_device.id)
        test_manufacturer = netbox.Manufacturer("testManufacturer")
        test_module_type = netbox.ModuleType("testModuleType",
            manufacturer_id=test_manufacturer.id,
            model="Networking")
        test_module = netbox.Module("testModule",
            device_id=test_device.id,
            module_bay_id=test_device_module_bay.id,
            module_type_id=test_module_type.id,
            status="active",
            description="SFP card")
        ```
        <!--End PulumiCodeChooser -->

        :param str resource_name: The name of the resource.
        :param ModuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ModuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 asset_tag: Optional[pulumi.Input[str]] = None,
                 comments: Optional[pulumi.Input[str]] = None,
                 custom_fields: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 device_id: Optional[pulumi.Input[int]] = None,
                 module_bay_id: Optional[pulumi.Input[int]] = None,
                 module_type_id: Optional[pulumi.Input[int]] = None,
                 serial: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ModuleArgs.__new__(ModuleArgs)

            __props__.__dict__["asset_tag"] = asset_tag
            __props__.__dict__["comments"] = comments
            __props__.__dict__["custom_fields"] = custom_fields
            __props__.__dict__["description"] = description
            if device_id is None and not opts.urn:
                raise TypeError("Missing required property 'device_id'")
            __props__.__dict__["device_id"] = device_id
            if module_bay_id is None and not opts.urn:
                raise TypeError("Missing required property 'module_bay_id'")
            __props__.__dict__["module_bay_id"] = module_bay_id
            if module_type_id is None and not opts.urn:
                raise TypeError("Missing required property 'module_type_id'")
            __props__.__dict__["module_type_id"] = module_type_id
            __props__.__dict__["serial"] = serial
            if status is None and not opts.urn:
                raise TypeError("Missing required property 'status'")
            __props__.__dict__["status"] = status
            __props__.__dict__["tags"] = tags
        super(Module, __self__).__init__(
            'netbox:index/module:Module',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            asset_tag: Optional[pulumi.Input[str]] = None,
            comments: Optional[pulumi.Input[str]] = None,
            custom_fields: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            description: Optional[pulumi.Input[str]] = None,
            device_id: Optional[pulumi.Input[int]] = None,
            module_bay_id: Optional[pulumi.Input[int]] = None,
            module_type_id: Optional[pulumi.Input[int]] = None,
            serial: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'Module':
        """
        Get an existing Module resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] status: One of [offline, active, planned, staged, failed, decommissioning].
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ModuleState.__new__(_ModuleState)

        __props__.__dict__["asset_tag"] = asset_tag
        __props__.__dict__["comments"] = comments
        __props__.__dict__["custom_fields"] = custom_fields
        __props__.__dict__["description"] = description
        __props__.__dict__["device_id"] = device_id
        __props__.__dict__["module_bay_id"] = module_bay_id
        __props__.__dict__["module_type_id"] = module_type_id
        __props__.__dict__["serial"] = serial
        __props__.__dict__["status"] = status
        __props__.__dict__["tags"] = tags
        return Module(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="assetTag")
    def asset_tag(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "asset_tag")

    @property
    @pulumi.getter
    def comments(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "comments")

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
    @pulumi.getter(name="moduleBayId")
    def module_bay_id(self) -> pulumi.Output[int]:
        return pulumi.get(self, "module_bay_id")

    @property
    @pulumi.getter(name="moduleTypeId")
    def module_type_id(self) -> pulumi.Output[int]:
        return pulumi.get(self, "module_type_id")

    @property
    @pulumi.getter
    def serial(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "serial")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        One of [offline, active, planned, staged, failed, decommissioning].
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "tags")

