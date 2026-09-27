# Create a VPC
resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
}

# Create S3 
resource "aws_s3_bucket" "example" {
  bucket = "my-tf-test-bucket-bishoy"

  tags = {
    Name        = "My bucket"
    Environment = "Dev"
  }
}

