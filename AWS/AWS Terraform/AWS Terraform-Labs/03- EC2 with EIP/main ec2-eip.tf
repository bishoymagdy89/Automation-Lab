provider "aws" {
  region = "us-east-1"
}

#create vpc
resource "aws_vpc" "lab_vpc" {
  cidr_block = "10.0.0.0/16"

  tags = {
    Name = "custom_vpc"
  }
}

resource "aws_internet_gateway" "gw" {
  vpc_id = aws_vpc.lab_vpc.id

  tags = {
    Name = "internet-GW"
  }
}


# first public subnet
resource "aws_subnet" "first_public" {
  vpc_id            = aws_vpc.lab_vpc.id
  cidr_block        = "10.0.1.0/24"
  availability_zone = "us-east-1a"

  tags = {
    Name = "first_public_subnet"
  }
}

# elastic ip
resource "aws_eip" "lb" {
  instance = aws_instance.first-instance.id
  domain   = "vpc"
}

#ec2 instance
resource "aws_instance" "first-instance" {
  ami           = "resolve:ssm:/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-default-x86_64"
  instance_type = "t3.micro"
  subnet_id     = aws_subnet.first_public.id

  tags = {
    Name = "first-web-instance"
  }
}
