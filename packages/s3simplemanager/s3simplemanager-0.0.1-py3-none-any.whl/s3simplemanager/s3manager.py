# imports
import boto3
import os


class S3SimpleManager:
    def __init__(self, ssl_verification: bool = False, bucket: str = "", url: str = "", key_id: str = "", key_value: str = "") -> None:
        self.bucket_name = bucket
        self.endpoint_url = url
        self.access_key_id = key_id
        self.secret_access_key = key_value
        self.s3_session = boto3.client("s3", aws_access_key_id=self.access_key_id, aws_secret_access_key=self.secret_access_key, endpoint_url=self.endpoint_url, verify=ssl_verification)

    # Getters
    def get_bucket_name(self) -> str:
        return self.bucket_name
    
    def get_endpoint_url(self) -> str:
        return self.endpoint_url
    
    def get_access_key_id(self) -> str:
        return self.access_key_id
    
    def get_secret_access_key(self) -> str:
        return self.secret_access_key

    # Setters
    def set_bucket_name(self, bucket: str) -> None:
        self.bucket_name = bucket
    
    def set_endpoint_url(self, url: str) -> None:
        self.endpoint_url = url
    
    def set_access_key_id(self, key_id: str) -> None:
        self.access_key_id = key_id
    
    def set_secret_access_key(self, secret: str) -> None:
        self.secret_access_key = secret
    
    # Methods
    def upload_files(self, local_file_path: str, bucket_file_path: str) -> None:
        """
        This function will upload the file passed by <local_loaction> to s3 bucket in the destination folder <bucket_location>
        :param local_file_path: File local path (this path must exists)
        :param bucket_file_path: Bucket path where to store the file (this path will be created automatically)
        :return:
        """
        if os.path.exists(local_file_path):
            if os.path.isfile(local_file_path):
                self.s3_session.upload_file(f"{local_file_path}", self.bucket_name, f"{bucket_file_path}")

    def list_files(self, location: str = "") -> None:
        """
        This fuction list all files inside a s3 bucket.
        :param location: string value that will have the file location inside s3 bucket. If left empty all Content inside the bucket will be printed.
        :return:
        """
        if location == "":
            for object in self.s3_session.list_objects(Bucket=self.bucket_name)['Contents']:
                print(object)
        else:
            for object in self.s3_session.list_objects(Bucket=self.bucket_name)['Contents']:
                if location in object['Key']:
                    print(object)
