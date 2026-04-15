terraform {
    backend "s3" {
        bucket = "fcaj-s3-bookshop-state"
        region = "ap-southeast-1"
        key = "dev/terraform.tfstate"
        dynamodb_table = "fcaj-dynamodb-bookshop-lock"
    }
}