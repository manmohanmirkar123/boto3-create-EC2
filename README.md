# boto3-create-EC2
You can deploy multiple EC2 instances using this Python script by specifying the configuration in the CSV file called "server.csv".

**Pre-requisite**
1.  AWS profile needs to be configured using AWS cli if not follow  [Link](https://linuxroutes.com/install-aws-command-line-interface-microsoft-windows/) then use `aws configure` command to set the profile.
2.  Python needs to be installed.
3.  module **boto3** and **pandas** needs to be installed if not please install it using `pip3 install boto3` and `pip3 install pandas` command.
Change the key_name and other configuration in the "server.csv" as required.

**Execution**
`python server_create.py` 

