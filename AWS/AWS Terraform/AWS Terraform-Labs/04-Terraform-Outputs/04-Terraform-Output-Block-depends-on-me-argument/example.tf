# Terraform AWS Configuration Reference

# Configure the AWS Provider
provider "aws" {
  region = "us-east-1"
}


# Configure the AWS vpc
resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"

  tags = {
    Name = "my-vpc"
  }
}


# Configure the AWS vpc subnet
resource "aws_subnet" "public-subnet-1" {
  vpc_id            = aws_vpc.main.id
  cidr_block        = "10.0.1.0/24"
  availability_zone = "us-east-1a"

  tags = {
    Name = "public-subnet-1"
  }
}

resource "aws_subnet" "public-subnet-2" {
  vpc_id            = aws_vpc.main.id
  cidr_block        = "10.0.2.0/24"
  availability_zone = "us-east-1b"

  tags = {
    Name = "public-subnet-2"
  }
}



resource "aws_subnet" "private-subnet-1" {
  vpc_id            = aws_vpc.main.id
  cidr_block        = "10.0.11.0/24"
  availability_zone = "us-east-1a"

  tags = {
    Name = "private-subnet-1"
  }
}

resource "aws_subnet" "private-subnet-2" {
  vpc_id            = aws_vpc.main.id
  cidr_block        = "10.0.12.0/24"
  availability_zone = "us-east-1b"

  tags = {
    Name = "private-subnet-2"
  }
}


# Configure the security group
resource "aws_security_group" "allow_tls" {
  name        = "allow_tls"
  description = "Allow TLS inbound traffic and all outbound traffic"
  vpc_id      = aws_vpc.main.id

  tags = {
    Name = "allow_tls"
  }
}
# Configure the security group ingress rule 
resource "aws_vpc_security_group_ingress_rule" "allow_tls_ipv4" {
  security_group_id = aws_security_group.allow_tls.id
  cidr_ipv4         = aws_vpc.main.cidr_block
  from_port         = 443
  ip_protocol       = "tcp"
  to_port           = 443
}

# Configure the security group egress rule 
resource "aws_vpc_security_group_egress_rule" "allow_all_traffic_ipv4" {
  security_group_id = aws_security_group.allow_tls.id
  cidr_ipv4         = "0.0.0.0/0"
  ip_protocol       = "-1" # semantically equivalent to all ports
}


# Configure AWS Instance - EC2
resource "aws_instance" "web" {
  ami                         = "resolve:ssm:/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-default-x86_64"
  instance_type               = "t3.micro"
  subnet_id                   = aws_subnet.public-subnet-1.id
  associate_public_ip_address = true
  vpc_security_group_ids      = [aws_security_group.allow_tls.id]
  tags = {
    Name = "first-instance-web"
  }
}


output "ec2-public" {
  value      = aws_instance.web.public_ip
  depends_on = [aws_vpc_security_group_ingress_rule.allow_tls_ipv4]
}

