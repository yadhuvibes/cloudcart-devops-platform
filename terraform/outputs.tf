output "instance_id" {
  value = aws_instance.cloudcart.id
}

output "elastic_ip" {
  value = aws_eip.cloudcart_eip.public_ip
}

output "public_dns" {
  value = aws_instance.cloudcart.public_dns
}
