# 0.0.1
* Features
    * Upload files - Support upload of files to s3 bucket
    * List files - This will allow you to list all or specific content from the s3 bucket

Example of use:
```
# imports
import s3simplemanager


s3 = S3SimpleManager()

s3.set_bucket_name("bucket_name")
s3.set_endpoint_url("url_of_bucket")
s3.set_access_key_id("access_key_id")
s3.set_secret_access_key("secret_access_key")

s3.upload_files("example_path_local_file", "example_path_bucket_file")
s3.list_files("example_path_bucket_file")
```
or
```
# imports
import s3simplemanager


s3 = S3SimpleManager(ssl_verification=False, bucket="s3_bucket_online", url="http://example.url.com/bucket", key_id="12345678", key_value="87654321")
s3.upload_files("example_path_local_file", "example_path_bucket_file")
s3.list_files("example_path_bucket_file")
```
