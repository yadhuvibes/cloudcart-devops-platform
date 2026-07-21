# EC2 Instance
resource "aws_instance" "cloudcart" {

  ami                  = "ami-0b910d1016287a5e7"
  instance_type        = var.instance_type
  key_name             = var.key_name
  iam_instance_profile = aws_iam_instance_profile.cloudcart_profile.name

  vpc_security_group_ids = [
    aws_security_group.cloudcart_sg.id
  ]

  tags = {
    Name = "CloudCart-Terraform"
  }
}



resource "aws_eip" "cloudcart_eip" {
  instance = aws_instance.cloudcart.id
  domain   = "vpc"

  tags = {
    Name = "CloudCart-EIP"
  }
}
