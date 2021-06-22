# Terraform, Consul, Packer and Nomad to provion Crypto Bot on AWS


## This AMI can be used for learning; update if you want to use in production. It has a current version of Nomad and Packer at time of commit

## Pull in the module and it will create 42 resources and setup all the routes and security groups for 9 instances running on AWS with auto-scaling and Consul and Nomad already configured. Scale down as needed. (Adding Vault soon) 


```
$ cd /packer
```

## Not needed for test but if you want to really use build your own AMI using the template

```
$ packer build consul-nomad.json 
```
## Take a look at the module and understand how it works locally versus the registry. Then take it for a test drive following the below commands. (TCO can depend on many factors refer to aws cost calculator for exact cost)

```
$ Terraform init
```
```
$ Terraform Plan 
```
```
$ Terraform Apply
```


## Ensure you grab the SSH Key From AWS and have fun! Check the ./terraform directory for the full use and viewing of the module used.
