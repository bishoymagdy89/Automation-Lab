# Create a VPC
resource "aws_vpc" "lab_vpc" {
  cidr_block = "10.0.0.0/16"

  tags = {
    Name = "custom_vpc"
  }
}

#create subnet
resource "aws_subnet" "first_public" {
  vpc_id     = aws_vpc.lab_vpc.id
  cidr_block = "10.0.1.0/24"

  tags = {
    Name = "first_public_subnet"
  }
}


# Create S3 
resource "aws_s3_bucket" "example" {
  bucket = "my-tf-test-bucket-bishoy"

  tags = {
    Name        = "My bucket"
    Environment = "Dev"
  }
}




