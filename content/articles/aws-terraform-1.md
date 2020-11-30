Title: My first touch to Terraform and AWS
Date: 2019-10-21 20:41
Modified: 2020-02-27 19:06
Category: tech
Slug: terraform-aws-1
Authors: Petri Salminen
Summary: I tried to grasp Terraform, AWS and AWS-cli at the same time. It was pretty confusing, but easily beats the AWS web console.

I decided to turn a new leaf on my professional development and try to learn AWS (Amazon Web Services). To this day, I have been quite anti-cloud but now I have to admit that cloud services like AWS may have their use. At least the potential employers require some kind of prior knowledge on at least one of the well-known cloud providers.

I have tried AWS before, but, to be honest, I had a hard time grasping the concepts and the confusing web console at the same time. Now I am going to utilize Terraform and AWS-cli to use AWS only from command line and code. No more web consoles!!! Feels so good already!

## Installing Terraform

For whatever reason, Terraform is not available from the Fedora's repositories. I would prefer installing it from the repos. Then I would be (relatively) sure that it is build from the [source](https://github.com/hashicorp/terraform). 

However, installing Terraform is possible only by downloading a zip and unzipping the binary from there. 

## Setting up aws-cli

When spinning servers up with Terraform, it obviously needs a permission to access your AWS account. This is easiest done with [aws-cli](https://github.com/aws/aws-cli).

Install aws-cli with `pip3`:

```
pip3 install awscli --user # Assuming user-installation just to be sure :)
```

Then, follow [this guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) to set up aws-cli. 

## Terraforming

I then proceeded to follow the [quick-start guide from Terraform](https://learn.hashicorp.com/terraform/getting-started/build). I did not want to use the `us-east-1` region, which made the ami change. Ami stands for Amazon Machine Image. The ami changes based on the image (of course) and region and stuff like that. I didn't find a way to get the ami from the Amazon AMI marketplace. I then resorted to search-engines to find a way to programmically find out the right AMI. I wanted to use CentOS 7(link!), just because I am using Fedora on my laptop and my server experience is very Ubuntu-based.  CentOS has a wiki article on [how to get started with CentOS on AWS](https://wiki.centos.org/Cloud/AWS). I picked the product-code for later use.

### The code

I ended up combining the Getting Started from Terraform and Mark Burke's wonderful article [Get the latest AWS AMI IDs with terraform](https://letslearndevops.com/2018/08/23/terraform-get-latest-centos-ami/). Here's what the result looked like:

```
provider "aws" {
  profile = "default"
  region  = "eu-central-1"
}

data "aws_ami" "centos7" {
  most_recent = true
  owners = ["aws-marketplace"]

  filter {
    name = "product-code"
    values = ["aw0evgkw8e5c1q413zgy5pjce"]
  }
}

resource "aws_instance" "example" {
  ami     = "${data.aws_ami.centos7.id}"
  instance_type = "t2.nano"
}
```

I find the terraform DSL (domain specific language) syntax very nice. I think that in the above example, the code explains itself quite well. "Use provider aws with this profile and region. Then find the aws_ami of the product-code, which is CentOS 7. Then spin up an instance with the ami." Remember, that Terraform does not quite behave like code, since the data part is computed with `terraform plan` and only after that `terraform apply` works to find the ami for the resource. 

I checked the AWS web console (https://eu-central-1.console.aws.amazon.com/ec2/v2/) and the instance was there! WOW!!!! This is quite cool. Remember to destory it if you don't need it. It is easily done using `terraform destroy`.

## Conclusion

I didn't really test the AWS in any way. However, I can say with confidence, that using Terraform is quite easy to grasp and the aws-cli is a handy tool. I will probably try to do more of stuff like this in the future.
