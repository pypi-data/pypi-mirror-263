import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "catnekaise.actions-constructs",
    "version": "0.2.18",
    "description": "CDK Constructs for integrating GitHub Actions and AWS.",
    "license": "Apache-2.0",
    "url": "https://github.com/catnekaise/actions-constructs.git",
    "long_description_content_type": "text/markdown",
    "author": "Daniel Jonsén<djonser1@gmail.com>",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/catnekaise/actions-constructs.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "catnekaise_actions_constructs",
        "catnekaise_actions_constructs._jsii"
    ],
    "package_data": {
        "catnekaise_actions_constructs._jsii": [
            "actions-constructs@0.2.18.jsii.tgz"
        ],
        "catnekaise_actions_constructs": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.8",
    "install_requires": [
        "aws-cdk-lib>=2.82.0, <3.0.0",
        "catnekaise.cdk-iam-utilities>=0.0.13, <0.0.14",
        "constructs>=10.0.5, <11.0.0",
        "jsii>=1.95.0, <2.0.0",
        "publication>=0.0.3",
        "typeguard~=2.13.3"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Typing :: Typed",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
