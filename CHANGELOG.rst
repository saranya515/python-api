Changelog
=========

1.3.0 - (2016-03-15)
--------------------
* feature:``Session``: Add ``get_available_partitions`` and
  ``get_available_regions`` methods to determine partitions and a service's
  available regions.
* feature:``EC2``: Update resource model to include ``Route`` resources.
  (`issue 532 <https://github.com/boto/boto3/pull/532>`__)


1.2.6 - (2016-03-01)
--------------------
* bugfix:Resources: Properly alias identifiers which are also in the shape.


1.2.5 - (2016-02-25)
--------------------

* bugfix:``S3``: Forward ``extra_args`` when using multipart
  downloads.
  (`issue 503 <https://github.com/boto/boto3/pull/503>`__)


1.2.4 - (2016-02-18)
--------------------
* feature:``EC2``: Add delete_tags() action to Instance resource.
  (`issue 459 <https://github.com/boto/boto3/pull/459>`__)
* feature:``Session``: Add ``region_name`` property on session.
  (`issue 414 <https://github.com/boto/boto3/pull/414>`__)
* bugfix:``S3``: Fix issue with hanging downloads.
  (`issue 471 <https://github.com/boto/boto3/pull/471>`__)


1.2.3 - (2015-12-17)
--------------------

* feature:``CloudWatch``: Add resource model.
  (`issue 412 <https://github.com/boto/boto3/pull/412>`__)
* feature:``S3``: Add a start_restore() on Object and ObjectSummary resources.
  (`issue 408 <https://github.com/boto/boto3/pull/408>`__)
* feature:Documentation: Add examples for S3.
  (`issue 402 <https://github.com/boto/boto3/pull/402>`__)
* bugfix:Collections: Fix regression where filters could not be chained.
  (`issue 401 <https://github.com/boto/boto3/pull/401>`__)
* bugfix:``S3``: Progress callback will be triggered when rewinding stream.
  (`issue 395 <https://github.com/boto/boto3/pull/395>`__)


1.2.2 - (2015-11-19)
--------------------

* feature:Dependencies: Relax version constraint of ``futures`` to support
  version 3.x.
* feature:Resources: Allow ``config`` object to be provided when creating
  resources
  (`issue 325 <https://github.com/boto/boto3/pull/325>`__)
* feature:Documentation: Add docstrings for resource collections and waiters
  (`issue 267 <https://github.com/boto/boto3/pull/267>`__,
   `issue 261 <https://github.com/boto/boto3/pull/261>`__)


1.2.1 - (2015-10-22)
--------------------

* bugfix:setup.cfg: Fix issue in formatting that broke PyPI distributable


1.2.0 - (2015-10-22)
--------------------

* feature:Docstrings: Add docstrings for resource identifiers, attributes,
  references, and subresources.
  (`issue 239 <https://github.com/boto/boto3/pull/239>`__)
* feature:``S3``: Add ability to configure host addressing style when making
  requests to Amazon S3.
  (`botocore issue 673 <https://github.com/boto/botocore/pull/673>`__)
* bugfix:``IAM``: Fix model issue with attached groups, roles, and policies.
  (`issue 304 <https://github.com/boto/boto3/pull/304>`__)
* bugfix:``EC2.ServiceResource.create_key_pair``: Fix model issue where
  creating key pair does not have a ``key_material`` on ``KeyPair`` resource.
  (`issue 290 <https://github.com/boto/boto3/pull/290>`__)


1.1.4 - (2015-09-24)
--------------------

* bugfix:Identifier: Make resource identifiers immutable.
  (`issue 246 <https://github.com/boto/boto3/pull/246>`__)
* feature: Both S3 Bucket and Object obtain upload_file() and download_file()
  (`issue 243 <https://github.com/boto/boto3/pull/243>`__)


1.1.3 - 2015-09-03
------------------

* feature:``aws storagegateway``: Add support for resource tagging.
* feature: Add support for customizable timeouts.


1.1.2 - 2015-08-25
------------------

* feature:``session.Session``: Add ``events`` property to access session's
  event emitter.
  (`issue 204 <https://github.com/boto/boto3/pull/204`__)
* bugfix:``Glacier.Account``: Fix issue with resource model.
  (`issue 196 <https://github.com/boto/boto3/pull/196>`__)
* bugfix:``DynamoDB``: Fix misspelling of error class to
  ``DynamoDBOperationNotSupportedError``.
  (`issue 218 <https://github.com/boto/boto3/pull/218>`__)


1.1.1 - 2015-07-23
------------------

* bugfix:``EC2.ServiceResource.create_tags``: Fix issue when creating
  multiple tags.
  (`issue 160 <https://github.com/boto/boto3/pull/160>`__)


1.1.0 - 2015-07-07
------------------
* bugfix:``EC2.Vpc.filter``: Fix issue with clobbering of ``Filtering``
  paramter.
  (`issue 154 `https://github.com/boto/boto3/pull/154`__)


1.0.1 - 2015-06-24
------------------
* feature: Update documentation


1.0.0 - 2015-06-22
------------------
* feature: Announced GA


0.0.22 - 2015-06-12
-------------------

* bugfix:``s3.client.upload_file``: Fix double invocation of callbacks when
  using signature version 4.
  (`issue 133 <https://github.com/boto/boto3/pull/133>`__)
* bugfix::``s3.Bucket.load``: Add custom load method for Bucket resource.
  (`issue 128 <https://github.com/boto/boto3/pull/128>`__)


0.0.21 - 2015-06-12
-------------------

* bugfix:Installation: Fix regression when installing via older versions of
  pip on python 2.6.
  (`issue 132 <https://github.com/boto/boto3/pull/132`__)


0.0.20 - 2015-06-11
-------------------

* feature:ec2: Update resource model.
  (`issue 129 <https://github.com/boto/boto3/pull/129>`__)


0.0.19 - 2015-06-04
-------------------

* breakingchange:Collections: Remove the ``page_count`` and ``limit``
  arguments from ``all()``. Undocument support for the two arguments in the
  ``filter()`` method.
  (`issue 119 <https://github.com/boto/boto3/pull/119>`__)
* feature:DynamoDB: Add batch writer.
  (`issue 118 <https://github.com/boto/boto3/pull/118>`__)


0.0.18 - 2015-06-01
-------------------

* feature:DynamoDB: Add document level interface for Table resource
  (`issue 103 <https://github.com/boto/boto3/pull/103>`__)
* feature:DynamoDB: Add ConditionExpression interface for querying and
  filtering Table resource.
  (`issue 103 <https://github.com/boto/boto3/pull/103>`__)
* feature:Clients: Add support for passing of ``botocore.client.Config`` object
  to instantiation of clients.

0.0.17 - 2015-05-07
-------------------

* feature:Botocore: Update to Botocore 0.107.0.

  * Adopt new data structure model.

0.0.16 - 2015-04-20
-------------------

* bugfix:Packaging: Fix release sdist and whl files from 0.0.15.
* feature:Amazon Dynamodb: Add resource model for Amazon DynamoDB.

0.0.15 - 2015-04-13
-------------------

* bugfix:Packaging: Fix an issue with the Amazon S3 ``upload_file`` and
  ``download_file`` customization.
  (`issue 85 <https://github.com/boto/boto3/pull/85>`__)
* bugfix:Resource: Fix an issue with the Amazon S3 ``BucketNofitication``
  resource.
* feature:Botocore: Update to Botocore 0.103.0.

  * Documentation updates for Amazon EC2 Container Service.

0.0.14 - 2015-04-02
-------------------

* feature:Resources: Update to the latest resource models for:

  * AWS CloudFormation
  * Amazon EC2
  * AWS IAM

* feature:Amazon S3:  Add an ``upload_file`` and ``download_file``
  to S3 clients that transparently handle parallel multipart transfers.
* feature:Botocore: Update to Botocore 0.102.0.

  * Add support for Amazon Machine Learning.
  * Add support for Amazon Workspaces.
  * Update ``requests`` to 2.6.0.
  * Update AWS Lambda to the latest API.
  * Update Amazon EC2 Container Service to the latest API.
  * Update Amazon S3 to the latest API.
  * Add ``DBSnapshotCompleted`` support to Amazon RDS waiters.
  * Fixes for the REST-JSON protocol.

0.0.13 - 2015-04-02
-------------------

* feature:Botocore: Update to Botocore 0.100.0.

  * Update AWS CodeDeploy to the latest service API.
  * Update Amazon RDS to support the ``describe_certificates``
    service operation.
  * Update Amazon Elastic Transcoder to support PlayReady DRM.
  * Update Amazon EC2 to support D2 instance types.

0.0.12 - 2015-03-26
-------------------

* feature:Resources: Add the ability to load resource data from a
  ``has`` relationship. This saves a call to ``load`` when available,
  and otherwise fixes a problem where there was no way to get at
  certain resource data.
  (`issue 74 <https://github.com/boto/boto3/pull/72>`__,
* feature:Botocore: Update to Botocore 0.99.0

  * Update service models for amazon Elastic Transcoder, AWS IAM
    and AWS OpsWorks to the latest versions.
  * Add deprecation warnings for old interface.

0.0.11 - 2015-03-24
-------------------

* feature:Resources: Add Amazon EC2 support for ClassicLink actions
  and add a delete action to EC2 ``Volume`` resources.
* feature:Resources: Add a ``load`` operation and ``user`` reference
  to AWS IAM's ``CurrentUser`` resource.
  (`issue 72 <https://github.com/boto/boto3/pull/72>`__,
* feature:Resources: Add resources for AWS IAM managed policies.
  (`issue 71 <https://github.com/boto/boto3/pull/71>`__)
* feature:Botocore: Update to Botocore 0.97.0

  * Add new Amazon EC2 waiters.
  * Add support for Amazon S3 cross region replication.
  * Fix an issue where empty config values could not be specified for
    Amazon S3's bucket notifications.
    (`botocore issue 495 <https://github.com/boto/botocore/pull/495>`__)
  * Update Amazon CloudWatch Logs to the latest API.
  * Update Amazon Elastic Transcoder to the latest API.
  * Update AWS CloudTrail to the latest API.
  * Fix bug where explicitly passed ``profile_name`` will now override
    any access and secret keys set in environment variables.
    (`botocore issue 486 <https://github.com/boto/botocore/pull/486>`__)
  * Add ``endpoint_url`` to ``client.meta``.
  * Better error messages for invalid regions.
  * Fix creating clients with unicode service name.

0.0.10 - 2015-03-05
-------------------

* bugfix:Documentation: Name collisions are now handled at the resource
  model layer instead of the factory, meaning that the documentation
  now uses the correct names.
  (`issue 67 <https://github.com/boto/boto3/pull/67>`__)
* feature:Session: Add a ``region_name`` option when creating a session.
  (`issue 69 <https://github.com/boto/boto3/pull/69>`__,
  `issue 21 <https://github.com/boto/boto3/issues/21>`__)
* feature:Botocore: Update to Botocore 0.94.0

  * Update to the latest Amazon CloudeSearch API.
  * Add support for near-realtime data updates and exporting historical
    data from Amazon Cognito Sync.
  * **Removed** the ability to clone a low-level client. Instead, create
    a new client with the same parameters.
  * Add support for URL paths in an endpoint URL.
  * Multithreading signature fixes.
  * Add support for listing hosted zones by name and getting hosted zone
    counts from Amazon Route53.
  * Add support for tagging to AWS Data Pipeline.

0.0.9 - 2015-02-19
------------------

* feature:Botocore: Update to Botocore 0.92.0

  * Add support for the latest Amazon EC2 Container Service API.
  * Allow calling AWS STS ``assume_role_with_saml`` without credentials.
  * Update to latest Amazon CloudFront API
  * Add support for AWS STS regionalized calls by passing both a region
    name and an endpoint URL.
    (`botocore issue 464 <https://github.com/boto/botocore/pull/464>`__)
  * Add support for Amazon Simple Systems Management Service (SSM)
  * Fix Amazon S3 auth errors when uploading large files
    to the ``eu-central-1`` and ``cn-north-1`` regions.
    (`botocore issue 462 <https://github.com/boto/botocore/pull/462>`__)
  * Add support for AWS IAM managed policies
  * Add support for Amazon ElastiCache tagging
  * Add support for Amazon Route53 Domains tagging of domains

0.0.8 - 2015-02-10
------------------

* bugfix:Resources: Fix Amazon S3 resource identifier order.
  (`issue 62 <https://github.com/boto/boto3/pull/62>`__)
* bugfix:Resources: Fix collection resource hydration path.
  (`issue 61 <https://github.com/boto/boto3/pull/61>`__)
* bugfix:Resources: Re-enable service-level access to all resources,
  allowing e.g. ``obj = s3.Object('bucket', 'key')``.
  (`issue 60 <https://github.com/boto/boto3/pull/60>`__)
* feature:Botocore: Update to Botocore 0.87.0

  * Add support for Amazon DynamoDB secondary index scanning.
  * Upgrade to ``requests`` 2.5.1.
  * Add support for anonymous (unsigned) clients.
    (`botocore issue 448 <https://github.com/boto/botocore/pull/448>`__)

0.0.7 - 2015-02-05
------------------

* feature:Resources: Enable support for Amazon Glacier.
* feature:Resources: Support plural references and nested JMESPath
  queries for data members when building parameters and identifiers.
  (`issue 52 <https://github.com/boto/boto3/pull/52>`__)
* feature:Resources: Update to the latest resource JSON format. This is
  a **backward-incompatible** change as not all resources are exposed
  at the service level anymore. For example, ``s3.Object('bucket', 'key')``
  is now ``s3.Bucket('bucket').Object('key')``.
  (`issue 51 <https://github.com/boto/boto3/pull/51>`__)
* feature:Resources: Make ``resource.meta`` a proper object. This allows
  you to do things like ``resource.meta.client``. This is a **backward-
  incompatible** change.
  (`issue 45 <https://github.com/boto/boto3/pull/45>`__)
* feature:Dependency: Update to JMESPath 0.6.1
* feature:Botocore: Update to Botocore 0.86.0

  * Add support for AWS CloudHSM
  * Add support for Amazon EC2 and Autoscaling ClassicLink
  * Add support for Amazon EC2 Container Service (ECS)
  * Add support for encryption at rest and CloudHSM to Amazon RDS
  * Add support for Amazon DynamoDB online indexing.
  * Add support for AWS ImportExport ``get_shipping_label``.
  * Add support for Amazon Glacier.
  * Add waiters for AWS ElastiCache.
    (`botocore issue 443 <https://github.com/boto/botocore/pull/443>`__)
  * Fix an issue with Amazon CloudFront waiters.
    (`botocore issue 426 <https://github.com/boto/botocore/pull/426>`_)
  * Allow binary data to be passed to ``UserData``.
    (`botocore issue 416 <https://github.com/boto/botocore/pull/416>`_)
  * Fix Amazon EMR endpoints for ``eu-central-1`` and ``cn-north-1``.
    (`botocore issue 423 <https://github.com/boto/botocore/pull/423>`__)
  * Fix issue with base64 encoding of blob types for Amazon EMR.
    (`botocore issue 413 <https://github.com/boto/botocore/pull/413>`__)

0.0.6 - 2014-12-18
------------------

* feature:Amazon SQS: Add ``purge`` action to queue resources
* feature:Waiters: Add documentation for client and resource waiters
  (`issue 44 <https://github.com/boto/boto3/pull/44>`__)
* feature:Waiters: Add support for resource waiters
  (`issue 43 <https://github.com/boto/boto3/pull/43>`__)
* bugfix:Installation: Remove dependency on the unused ``six`` module
  (`issue 42 <https://github.com/boto/boto3/pull/42>`__)
* feature:Botocore: Update to Botocore 0.80.0

  * Update Amazon Simple Workflow Service (SWF) to the latest version
  * Update AWS Storage Gateway to the latest version
  * Update Amazon Elastic MapReduce (EMR) to the latest version
  * Update AWS Elastic Transcoder to the latest version
  * Enable use of ``page_size`` for clients
    (`botocore issue 408 <https://github.com/boto/botocore/pull/408>`__)

0.0.5 - 2014-12-09
------------------

* feature: Add support for batch actions on collections.
  (`issue 32 <https://github.com/boto/boto3/pull/32>`__)
* feature: Update to Botocore 0.78.0

  * Add support for Amazon Simple Queue Service purge queue which allows
    users to delete the messages in their queue.
  * Add AWS OpsWorks support for registering and assigning existing Amazon
    EC2 instances and on-premises servers.
  * Fix issue with expired signatures when retrying failed requests
    (`botocore issue 399 <https://github.com/boto/botocore/pull/399>`__)
  * Port Route53 resource ID customizations from AWS CLI to Botocore.
    (`botocore issue 398 <https://github.com/boto/botocore/pull/398>`__)
  * Fix handling of blob type serialization for JSON services.
    (`botocore issue 397 <https://github.com/boto/botocore/pull/397>`__)

0.0.4 - 2014-12-04
------------------

* feature: Update to Botocore 0.77.0

  * Add support for Kinesis PutRecords operation. It writes multiple
    data records from a producer into an Amazon Kinesis stream in a
    single call.
  * Add support for IAM GetAccountAuthorizationDetails operation. It
    retrieves information about all IAM users, groups, and roles in
    your account, including their relationships to one another and
    their attached policies.
  * Add support for updating the comment of a Route53 hosted zone.
  * Fix base64 serialization for JSON protocol services.
  * Fix issue where certain timestamps were not being accepted as valid input
    (`botocore issue 389 <https://github.com/boto/botocore/pull/389>`__)

* feature: Update `Amazon EC2 <http://aws.amazon.com/ec2/>`_ resource model.
* feature: Support `belongsTo` resource reference as well as `path`
  specified in an action's resource definition.
* bugfix: Fix an issue accessing SQS message bodies
  (`issue 33 <https://github.com/boto/boto3/issues/33>`__)

0.0.3 - 2014-11-26
------------------

* feature: Update to Botocore 0.76.0.

  * Add support for using AWS Data Pipeline templates to create
    pipelines and bind values to parameters in the pipeline
  * Add support to Amazon Elastic Transcoder client for encryption of files
    in Amazon S3.
  * Fix issue where Amazon S3 requests were not being
    resigned correctly when using Signature Version 4.
    (`botocore issue 388 <https://github.com/boto/botocore/pull/388>`__)
  * Add support for custom response parsing in Botocore clients.
    (`botocore issue 387 <https://github.com/boto/botocore/pull/387>`__)

0.0.2 - 2014-11-20
------------------

* Adds resources for
  `AWS CloudFormation <http://aws.amazon.com/cloudformation/>`_ and
  `AWS OpsWorks <http://aws.amazon.com/opsworks/>`_.
* Update to Botocore 0.73.0 and JMESPath 0.5.0
* Adds support for
  `AWS CodeDeploy <http://aws.amazon.com/codedeploy/>`_,
  `AWS Config <http://aws.amazon.com/config/>`_,
  `AWS KMS <http://aws.amazon.com/kms/>`_,
  `AWS Lambda <http://aws.amazon.com/lambda/>`_.
* Make requests with a customized HTTP user-agent

0.0.1 - 2014-11-11
------------------

* Initial developer preview refresh of Boto 3
* Supports S3, EC2, SQS, SNS, and IAM resources
* Supports low-level clients for most services
