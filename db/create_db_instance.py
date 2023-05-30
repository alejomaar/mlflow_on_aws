import boto3

def create_postgres_instance():
    rds = boto3.client('rds')

    try:
        response = rds.create_db_instance(
            DBInstanceIdentifier='mydatabase',
            Engine='postgres',
            AllocatedStorage=20,
            DBInstanceClass='db.t2.micro',
            MasterUsername='admin',
            MasterUserPassword='password123',
            VpcSecurityGroupIds=['sg-12345678'],
            AvailabilityZone='us-west-2a',
            Tags=[
                {
                    'Key': 'Name',
                    'Value': 'mydatabase'
                },
            ],
            LicenseModel='postgresql-license',
            EngineVersion='13.4',
            PubliclyAccessible=False,
            BackupRetentionPeriod=0
        )
        print("PostgreSQL instance creation initiated.")
        print(f"DB instance identifier: {response['DBInstance']['DBInstanceIdentifier']}")
    except Exception as e:
        print(f"Error creating PostgreSQL instance: {str(e)}")

# Call the function to create the PostgreSQL instance
create_postgres_instance()