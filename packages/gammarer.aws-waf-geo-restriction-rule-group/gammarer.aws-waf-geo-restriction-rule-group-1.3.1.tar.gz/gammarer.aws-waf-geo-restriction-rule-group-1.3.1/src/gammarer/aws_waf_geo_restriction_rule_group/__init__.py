'''
# AWS WAF(v2) GEO Restriction Rule Group

[![GitHub](https://img.shields.io/github/license/gammarer/aws-waf-geo-restriction-rule-group?style=flat-square)](https://github.com/gammarer/aws-waf-geo-restriction-rule-group/blob/main/LICENSE)
[![npm (scoped)](https://img.shields.io/npm/v/@gammarer/aws-waf-geo-restriction-rule-group?style=flat-square)](https://www.npmjs.com/package/@gammarer/aws-waf-geo-restriction-rule-group)
[![PyPI](https://img.shields.io/pypi/v/gammarer.aws-waf-geo-restriction-rule-group?style=flat-square)](https://pypi.org/project/gammarer.aws-waf-geo-restriction-rule-group/)
[![Nuget](https://img.shields.io/nuget/v/Gammarer.CDK.AWS.WafGeoRestrictionRuleGroup?style=flat-square)](https://www.nuget.org/packages/Gammarer.CDK.AWS.WafGeoRestrictionRuleGroup/)
[![Sonatype Nexus (Releases)](https://img.shields.io/nexus/r/com.gammarer/aws-waf-geo-restriction-rule-group?server=https%3A%2F%2Fs01.oss.sonatype.org%2F&style=flat-square)](https://s01.oss.sonatype.org/content/repositories/releases/com/gammarer/aws-waf-geo-restriction-rule-group/)
[![GitHub Workflow Status (branch)](https://img.shields.io/github/actions/workflow/status/gammarer/aws-waf-geo-restriction-rule-group/release.yml?branch=main&label=release&style=flat-square)](https://github.com/gammarer/aws-waf-geo-restriction-rule-group/actions/workflows/release.yml)
[![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/gammarer/aws-waf-geo-restriction-rule-group?sort=semver&style=flat-square)](https://github.com/gammarer/aws-waf-geo-restriction-rule-group/releases)

[![View on Construct Hub](https://constructs.dev/badge?package=@gammarer/aws-waf-geo-restriction-rule-group)](https://constructs.dev/packages/@gammarer/aws-waf-geo-restriction-rule-group)

This is an AWS CDK Construct for Geo Restriction Rule Group on WAF V2

## Resources

This construct creating resource list.

* WAF V2 RuleGroup

## Install

### TypeScript

```shell
npm install @gammarer/aws-waf-geo-restriction-rule-group
# or
yarn add @gammarer/aws-waf-geo-restriction-rule-group
```

### Python

```shell
pip install gammarer.aws-waf-geo-restriction-rule-group
```

### C# / .Net

```shell
dotnet add package Gammarer.CDK.AWS.WafGeoRestrictionRuleGroup
```

### Java

Add the following to pom.xml:

```xml
<dependency>
  <groupId>com.gammarer</groupId>
  <artifactId>aws-waf-geo-restriction-rule-group</artifactId>
</dependency>
```

## Example

```python
import { WafGeoRestrictRuleGroup } from '@gammarer/aws-waf-geo-restriction-rule-group';

new WafGeoRestrictRuleGroup(stack, 'WafGeoRestrictRuleGroup', {
  scope: Scope.GLOBAL, // GLOBAL(CloudFront) or REIGONAL(Application Load Balancer (ALB), Amazon API Gateway REST API, an AWS AppSync GraphQL API, or an Amazon Cognito user pool)
  allowCountries: ['JP'], // alpha-2 country and region codes from the International Organization for Standardization (ISO) 3166 standard
});
```

## License

This project is licensed under the Apache-2.0 License.
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from ._jsii import *

import aws_cdk.aws_wafv2 as _aws_cdk_aws_wafv2_ceddda9d
import constructs as _constructs_77d1e7e8


@jsii.data_type(
    jsii_type="@gammarer/aws-waf-geo-restriction-rule-group.IpRateLimitingProperty",
    jsii_struct_bases=[],
    name_mapping={"count": "count", "enable": "enable"},
)
class IpRateLimitingProperty:
    def __init__(self, *, count: jsii.Number, enable: builtins.bool) -> None:
        '''
        :param count: 
        :param enable: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__739ac4ed6a9b914a12643543829770bcba7b63c6bca74db070a2cb1f8b4e0e62)
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument enable", value=enable, expected_type=type_hints["enable"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "count": count,
            "enable": enable,
        }

    @builtins.property
    def count(self) -> jsii.Number:
        result = self._values.get("count")
        assert result is not None, "Required property 'count' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def enable(self) -> builtins.bool:
        result = self._values.get("enable")
        assert result is not None, "Required property 'enable' is missing"
        return typing.cast(builtins.bool, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IpRateLimitingProperty(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@gammarer/aws-waf-geo-restriction-rule-group.Scope")
class Scope(enum.Enum):
    GLOBAL = "GLOBAL"
    REGIONAL = "REGIONAL"


class WafGeoRestrictRuleGroup(
    _aws_cdk_aws_wafv2_ceddda9d.CfnRuleGroup,
    metaclass=jsii.JSIIMeta,
    jsii_type="@gammarer/aws-waf-geo-restriction-rule-group.WafGeoRestrictRuleGroup",
):
    def __init__(
        self,
        scope_: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        allow_countries: typing.Sequence[builtins.str],
        scope: Scope,
        allow_ip_set_arn: typing.Optional[builtins.str] = None,
        ip_rate_limiting: typing.Optional[typing.Union[IpRateLimitingProperty, typing.Dict[builtins.str, typing.Any]]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope_: Specifies whether this is for an Amazon CloudFront distribution or for a regional application. A regional application can be an Application Load Balancer (ALB), an Amazon API Gateway REST API, an AWS AppSync GraphQL API, an Amazon Cognito user pool, or an AWS App Runner service. Valid Values are ``CLOUDFRONT`` and ``REGIONAL`` . .. epigraph:: For ``CLOUDFRONT`` , you must create your WAFv2 resources in the US East (N. Virginia) Region, ``us-east-1`` .
        :param id: -
        :param allow_countries: 
        :param scope: 
        :param allow_ip_set_arn: 
        :param ip_rate_limiting: 
        :param name: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49910962e21cac0e33700d9e5fe55d0b8a4510be6bea8d6b8e8a5c00ae638dd4)
            check_type(argname="argument scope_", value=scope_, expected_type=type_hints["scope_"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = WafGeoRestrictRuleGroupProps(
            allow_countries=allow_countries,
            scope=scope,
            allow_ip_set_arn=allow_ip_set_arn,
            ip_rate_limiting=ip_rate_limiting,
            name=name,
        )

        jsii.create(self.__class__, self, [scope_, id, props])


@jsii.data_type(
    jsii_type="@gammarer/aws-waf-geo-restriction-rule-group.WafGeoRestrictRuleGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "allow_countries": "allowCountries",
        "scope": "scope",
        "allow_ip_set_arn": "allowIpSetArn",
        "ip_rate_limiting": "ipRateLimiting",
        "name": "name",
    },
)
class WafGeoRestrictRuleGroupProps:
    def __init__(
        self,
        *,
        allow_countries: typing.Sequence[builtins.str],
        scope: Scope,
        allow_ip_set_arn: typing.Optional[builtins.str] = None,
        ip_rate_limiting: typing.Optional[typing.Union[IpRateLimitingProperty, typing.Dict[builtins.str, typing.Any]]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param allow_countries: 
        :param scope: 
        :param allow_ip_set_arn: 
        :param ip_rate_limiting: 
        :param name: 
        '''
        if isinstance(ip_rate_limiting, dict):
            ip_rate_limiting = IpRateLimitingProperty(**ip_rate_limiting)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9af4984acc9555fcd5cc63841dbf316c2b4cf484bce49dcdfe62faa5c7054e03)
            check_type(argname="argument allow_countries", value=allow_countries, expected_type=type_hints["allow_countries"])
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument allow_ip_set_arn", value=allow_ip_set_arn, expected_type=type_hints["allow_ip_set_arn"])
            check_type(argname="argument ip_rate_limiting", value=ip_rate_limiting, expected_type=type_hints["ip_rate_limiting"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "allow_countries": allow_countries,
            "scope": scope,
        }
        if allow_ip_set_arn is not None:
            self._values["allow_ip_set_arn"] = allow_ip_set_arn
        if ip_rate_limiting is not None:
            self._values["ip_rate_limiting"] = ip_rate_limiting
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def allow_countries(self) -> typing.List[builtins.str]:
        result = self._values.get("allow_countries")
        assert result is not None, "Required property 'allow_countries' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def scope(self) -> Scope:
        result = self._values.get("scope")
        assert result is not None, "Required property 'scope' is missing"
        return typing.cast(Scope, result)

    @builtins.property
    def allow_ip_set_arn(self) -> typing.Optional[builtins.str]:
        result = self._values.get("allow_ip_set_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ip_rate_limiting(self) -> typing.Optional[IpRateLimitingProperty]:
        result = self._values.get("ip_rate_limiting")
        return typing.cast(typing.Optional[IpRateLimitingProperty], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WafGeoRestrictRuleGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "IpRateLimitingProperty",
    "Scope",
    "WafGeoRestrictRuleGroup",
    "WafGeoRestrictRuleGroupProps",
]

publication.publish()

def _typecheckingstub__739ac4ed6a9b914a12643543829770bcba7b63c6bca74db070a2cb1f8b4e0e62(
    *,
    count: jsii.Number,
    enable: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49910962e21cac0e33700d9e5fe55d0b8a4510be6bea8d6b8e8a5c00ae638dd4(
    scope_: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    allow_countries: typing.Sequence[builtins.str],
    scope: Scope,
    allow_ip_set_arn: typing.Optional[builtins.str] = None,
    ip_rate_limiting: typing.Optional[typing.Union[IpRateLimitingProperty, typing.Dict[builtins.str, typing.Any]]] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9af4984acc9555fcd5cc63841dbf316c2b4cf484bce49dcdfe62faa5c7054e03(
    *,
    allow_countries: typing.Sequence[builtins.str],
    scope: Scope,
    allow_ip_set_arn: typing.Optional[builtins.str] = None,
    ip_rate_limiting: typing.Optional[typing.Union[IpRateLimitingProperty, typing.Dict[builtins.str, typing.Any]]] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
