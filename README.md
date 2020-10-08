# Python-SnapShot
Basic Python BOTO3 EC2 Snapshot script

## About

This project is a demo, and uses boto3 to manage AWS EC2 instance snapshots

## Configuring

shotty uses the configuration files created by the AWS CLI
e.g.
`aws configure --profile snappy`

##Running

`pipenv run "python snappy/snappy.py <command> <--project=PROJECT>"`

*command* is list, start, stop
*project* is optional


