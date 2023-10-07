from .common import Service
from . import providers


Service("Cloud Run", providers.gcp, "https://cloud.google.com/run")
Service("App Runner", providers.aws, "https://aws.amazon.com/apprunner/")
Service("Elastic Beanstalk", providers.aws, "https://aws.amazon.com/elasticbeanstalk/")
Service("Container Apps", providers.azure, "https://azure.microsoft.com/en-us/products/container-apps")