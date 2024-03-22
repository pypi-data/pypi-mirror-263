import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "alma-cdk.origin-verify",
    "version": "1.0.0.b2",
    "description": "Enforce origin traffic via CloudFront.",
    "license": "Apache-2.0",
    "url": "https://github.com/alma-cdk/origin-verify.git",
    "long_description_content_type": "text/markdown",
    "author": "Alma Media<opensource@almamedia.dev>",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/alma-cdk/origin-verify.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "alma_cdk.origin_verify",
        "alma_cdk.origin_verify._jsii"
    ],
    "package_data": {
        "alma_cdk.origin_verify._jsii": [
            "origin-verify@1.0.0-beta.2.jsii.tgz"
        ],
        "alma_cdk.origin_verify": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.8",
    "install_requires": [
        "aws-cdk-lib>=2.133.0, <3.0.0",
        "constructs>=10.3.0, <11.0.0",
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
        "Development Status :: 4 - Beta",
        "License :: OSI Approved"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
