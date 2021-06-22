provider "aws" {
  region = "us-east-1"
}


module "nomad" {
  source  = "hashicorp/nomad/aws"
  version = "0.6.6"
  ami_id  = "ami-0d4a1b09d2a2fd91a"
  cluster_name  = "Nomad-Demo"
  cluster_tag_key = "nomad-servers"
  instance_type  = "t2.micro"
  ssh_key_name  = "Add-Your-Key-Name"
}
