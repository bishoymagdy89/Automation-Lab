/*
1) Create a VPC in us-east-1, CIDR 10.0.0.0/16
2) Create a subnet with the CIDR 10.0.2.0/24 into the above VPC
3) Create an S3 bucket in the same region
*/


provider "aws" {
  region = "us-east-1"
}


resource "aws_vpc" "lab_vpc" {
  cidr_block = "10.0.0.0/16"

  tags = {
    Name = "custom_vpc"
  }
}

resource "aws_subnet" "main" {
  vpc_id     = aws_vpc.lab_vpc.id
  cidr_block = "10.0.1.0/24"

  tags = {
    Name = "first_subnet"
  }
}


# Create S3 
resource "aws_s3_bucket" "bucket-test" {
  bucket = "my-tf-test-bucket-bishoy-1"

  tags = {
    Name        = "My bucket"
    Environment = "Dev"
  }
}




