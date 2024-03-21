'''
# CDK-Hugo-Deploy

This is an AWS CDK Construct for easily deploying [Hugo](https://gohugo.io/) Static websites to AWS S3 behind SSL/Cloudfront.

## Usage

Before deploying, run the `hugo` command in your Hugo project to generate a built site in the `public` directory.

## Typescript

```python
import { App, Stack, StackProps } from 'aws-cdk-lib';
import { HugoDeploy } from 'cdk-hugo-deploy';

export class MyStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    new HugoDeploy(this, 'HugoDeploy', {
      publicDir: 'path/to/hugo-project/public',
      domainName: 'example.com'  // Domain you already have a hosted zone for
    });
}
```

## Python

```python
from constructs import Construct
from aws_cdk import Stack
from cdk_hugo_deploy import HugoDeploy

class MyStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        HugoDeploy(self, "HugoDeploy",
            public_dir="path/to/hugo-project/public",
            domain_name="example.com"
        )
```

## Prerequisites

Assumes that there is already a Route53 hosted zone for `domainName` that can be [looked up](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_route53.HostedZone.html#static-fromwbrlookupscope-id-query)

## Why this construct?

Other constructs for deploying Single Page Applicationis (SPA) such as [CDK-SPA-Deploy](https://github.com/nideveloper/CDK-SPA-Deploy) don't account for how Hugo handles paths that end in `/`.

This construct includes a [Cloudfront Function](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-functions.html) to [rewrite paths](src/hugoPaths.js) to ensure `/path/to/page/` will request `/path/to/page/index.html` from the S3 Origin.

## Contributing

Please open an [issue](https://github.com/maafk/cdk-hugo-deploy/issues) with any updates/features you'd like on this
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

import aws_cdk.aws_route53 as _aws_cdk_aws_route53_ceddda9d
import constructs as _constructs_77d1e7e8


class HugoDeploy(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk-hugo-deploy.HugoDeploy",
):
    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        domain_name: builtins.str,
        public_dir: builtins.str,
        region: typing.Optional[builtins.str] = None,
        zone: typing.Optional[_aws_cdk_aws_route53_ceddda9d.HostedZone] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param domain_name: Domain name of the site deploying to. You should already have a hosted zone in the account you're deploying to with this domain name
        :param public_dir: Path to Hugo public directory, which is generated after running the ``hugo`` command. By default, this will be the ``public`` directory in your hugo project
        :param region: Region deploying to. Default: - us-east-1
        :param zone: Zone the Domain Name is created in.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e03820b2549e7ec849582d7a418c4d7083c889cc04af621d01d3293835348c33)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = HugoDeployProps(
            domain_name=domain_name, public_dir=public_dir, region=region, zone=zone
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @builtins.property
    @jsii.member(jsii_name="publicDir")
    def public_dir(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicDir"))

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "region"))


@jsii.data_type(
    jsii_type="cdk-hugo-deploy.HugoDeployProps",
    jsii_struct_bases=[],
    name_mapping={
        "domain_name": "domainName",
        "public_dir": "publicDir",
        "region": "region",
        "zone": "zone",
    },
)
class HugoDeployProps:
    def __init__(
        self,
        *,
        domain_name: builtins.str,
        public_dir: builtins.str,
        region: typing.Optional[builtins.str] = None,
        zone: typing.Optional[_aws_cdk_aws_route53_ceddda9d.HostedZone] = None,
    ) -> None:
        '''
        :param domain_name: Domain name of the site deploying to. You should already have a hosted zone in the account you're deploying to with this domain name
        :param public_dir: Path to Hugo public directory, which is generated after running the ``hugo`` command. By default, this will be the ``public`` directory in your hugo project
        :param region: Region deploying to. Default: - us-east-1
        :param zone: Zone the Domain Name is created in.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__271c7d0295ae9e51ecb9baa9f1bb05877c6312f1b12ff88b745fac6f0d541f19)
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument public_dir", value=public_dir, expected_type=type_hints["public_dir"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument zone", value=zone, expected_type=type_hints["zone"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_name": domain_name,
            "public_dir": public_dir,
        }
        if region is not None:
            self._values["region"] = region
        if zone is not None:
            self._values["zone"] = zone

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''Domain name of the site deploying to.

        You should already have a hosted zone in the account you're deploying to with this domain name
        '''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def public_dir(self) -> builtins.str:
        '''Path to Hugo public directory, which is generated after running the ``hugo`` command.

        By default, this will be the ``public`` directory in your hugo project
        '''
        result = self._values.get("public_dir")
        assert result is not None, "Required property 'public_dir' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Region deploying to.

        :default: - us-east-1
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def zone(self) -> typing.Optional[_aws_cdk_aws_route53_ceddda9d.HostedZone]:
        '''Zone the Domain Name is created in.'''
        result = self._values.get("zone")
        return typing.cast(typing.Optional[_aws_cdk_aws_route53_ceddda9d.HostedZone], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HugoDeployProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "HugoDeploy",
    "HugoDeployProps",
]

publication.publish()

def _typecheckingstub__e03820b2549e7ec849582d7a418c4d7083c889cc04af621d01d3293835348c33(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    domain_name: builtins.str,
    public_dir: builtins.str,
    region: typing.Optional[builtins.str] = None,
    zone: typing.Optional[_aws_cdk_aws_route53_ceddda9d.HostedZone] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__271c7d0295ae9e51ecb9baa9f1bb05877c6312f1b12ff88b745fac6f0d541f19(
    *,
    domain_name: builtins.str,
    public_dir: builtins.str,
    region: typing.Optional[builtins.str] = None,
    zone: typing.Optional[_aws_cdk_aws_route53_ceddda9d.HostedZone] = None,
) -> None:
    """Type checking stubs"""
    pass
