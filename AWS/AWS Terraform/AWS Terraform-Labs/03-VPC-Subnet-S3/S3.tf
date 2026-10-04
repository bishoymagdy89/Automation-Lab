/*
1) Create a VPC in us-east-1, CIDR 10.0.0.0/16
2) Create a subnet with the CIDR 10.0.2.0/24 into the above VPC
3) Create an S3 bucket in the same region
*/


provider "aws" {
  region = "us-east-1"
}


# Create S3 
resource "aws_s3_bucket" "bucket-test" {
  bucket = "my-tf-test-bucket-bishoy-1"

  tags = {
    Name        = "My bucket"
    Environment = "Dev"
  }
}


# Create S3 Bucket In Account-Regional Namespace
data "aws_caller_identity" "current" {}
data "aws_region" "current" {}

resource "aws_s3_bucket" "example" {
  bucket           = format("my-tf-test-bucket-%s-%s-an", data.aws_caller_identity.current.account_id, data.aws_region.current.region)
  bucket_namespace = "account-regional"
}

