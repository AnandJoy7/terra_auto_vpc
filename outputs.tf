output "vpc_id" {
  value = aws_vpc.my_vpc.id
  description = "The ID of the created VPC"
}

output "subnet_id" {
  value = aws_subnet.my_subnet.id
  description = "The ID of the created Subnet"
}

output "internet_gateway_id" {
  value = aws_internet_gateway.my_igw.id
  description = "The ID of the created Internet Gateway"
}

output "route_table_id" {
  value = aws_route_table.my_route_table.id
  description = "The ID of the created Route Table"
}
