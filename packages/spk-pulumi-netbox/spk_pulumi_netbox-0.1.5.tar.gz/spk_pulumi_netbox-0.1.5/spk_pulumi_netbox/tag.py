# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['TagArgs', 'Tag']

@pulumi.input_type
class TagArgs:
    def __init__(__self__, *,
                 color_hex: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 slug: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Tag resource.
        :param pulumi.Input[str] color_hex: Defaults to `9e9e9e`.
        """
        if color_hex is not None:
            pulumi.set(__self__, "color_hex", color_hex)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if slug is not None:
            pulumi.set(__self__, "slug", slug)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="colorHex")
    def color_hex(self) -> Optional[pulumi.Input[str]]:
        """
        Defaults to `9e9e9e`.
        """
        return pulumi.get(self, "color_hex")

    @color_hex.setter
    def color_hex(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "color_hex", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def slug(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "slug")

    @slug.setter
    def slug(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "slug", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _TagState:
    def __init__(__self__, *,
                 color_hex: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 slug: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering Tag resources.
        :param pulumi.Input[str] color_hex: Defaults to `9e9e9e`.
        """
        if color_hex is not None:
            pulumi.set(__self__, "color_hex", color_hex)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if slug is not None:
            pulumi.set(__self__, "slug", slug)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="colorHex")
    def color_hex(self) -> Optional[pulumi.Input[str]]:
        """
        Defaults to `9e9e9e`.
        """
        return pulumi.get(self, "color_hex")

    @color_hex.setter
    def color_hex(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "color_hex", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def slug(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "slug")

    @slug.setter
    def slug(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "slug", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class Tag(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 color_hex: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 slug: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        From the [official documentation](https://docs.netbox.dev/en/stable/models/extras/tag/):
        > Tags are user-defined labels which can be applied to a variety of objects within NetBox. They can be used to establish dimensions of organization beyond the relationships built into NetBox. For example, you might create a tag to identify a particular ownership or condition across several types of objects.
        > 
        > Each tag has a label, color, and a URL-friendly slug. For example, the slug for a tag named "Dunder Mifflin, Inc." would be dunder-mifflin-inc. The slug is generated automatically and makes tags easier to work with as URL parameters. Each tag can also be assigned a description indicating its purpose.

        ## Example Usage

        <!--Start PulumiCodeChooser -->
        ```python
        import pulumi
        import spk_pulumi_netbox as netbox

        dmz = netbox.Tag("dmz", color_hex="ff00ff")
        ```
        <!--End PulumiCodeChooser -->

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] color_hex: Defaults to `9e9e9e`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[TagArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        From the [official documentation](https://docs.netbox.dev/en/stable/models/extras/tag/):
        > Tags are user-defined labels which can be applied to a variety of objects within NetBox. They can be used to establish dimensions of organization beyond the relationships built into NetBox. For example, you might create a tag to identify a particular ownership or condition across several types of objects.
        > 
        > Each tag has a label, color, and a URL-friendly slug. For example, the slug for a tag named "Dunder Mifflin, Inc." would be dunder-mifflin-inc. The slug is generated automatically and makes tags easier to work with as URL parameters. Each tag can also be assigned a description indicating its purpose.

        ## Example Usage

        <!--Start PulumiCodeChooser -->
        ```python
        import pulumi
        import spk_pulumi_netbox as netbox

        dmz = netbox.Tag("dmz", color_hex="ff00ff")
        ```
        <!--End PulumiCodeChooser -->

        :param str resource_name: The name of the resource.
        :param TagArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TagArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 color_hex: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 slug: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TagArgs.__new__(TagArgs)

            __props__.__dict__["color_hex"] = color_hex
            __props__.__dict__["description"] = description
            __props__.__dict__["name"] = name
            __props__.__dict__["slug"] = slug
            __props__.__dict__["tags"] = tags
        super(Tag, __self__).__init__(
            'netbox:index/tag:Tag',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            color_hex: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            slug: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'Tag':
        """
        Get an existing Tag resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] color_hex: Defaults to `9e9e9e`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _TagState.__new__(_TagState)

        __props__.__dict__["color_hex"] = color_hex
        __props__.__dict__["description"] = description
        __props__.__dict__["name"] = name
        __props__.__dict__["slug"] = slug
        __props__.__dict__["tags"] = tags
        return Tag(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="colorHex")
    def color_hex(self) -> pulumi.Output[Optional[str]]:
        """
        Defaults to `9e9e9e`.
        """
        return pulumi.get(self, "color_hex")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def slug(self) -> pulumi.Output[str]:
        return pulumi.get(self, "slug")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "tags")

