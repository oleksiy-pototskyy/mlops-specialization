terraform {
  required_version = ">= 1.3"
}

module "network" {
  source = "./modules/network"
}

module "cluster" {
  source = "./modules/eks"
}
