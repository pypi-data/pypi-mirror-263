"""A class providing common s3 functions"""
import json
import os

import boto3
from botocore.exceptions import ClientError


class S3Util:
    """Provides common s3 functions"""

    def __init__(self, bucket: str = None) -> None:
        self.s3 = boto3.resource("s3")
        self.bucket_name = bucket or self.get_bucket()

    def get_bucket(self) -> str:
        """Get the bucket name from the environment or raise exception"""
        if os.environ.get("S3_BUCKET") is None:
            raise ValueError("S3_BUCKET environment variable not set")
        return os.environ.get("S3_BUCKET")

    def exists(self, key: str) -> bool:
        try:
            client = boto3.client("s3")
            client.head_object(Bucket=self.bucket_name, Key=key)
            return True
        except ClientError:
            return False

    def read_json(self, key: str) -> dict:
        return json.loads(self.read_file(key))

    def write_json(self, key: str, data: dict) -> None:
        self.write_file(key, json.dumps(data))

    def read_file(self, key: str) -> str:
        print(f"Reading from {self.bucket_name}/{key}")
        obj = self.s3.Object(self.bucket_name, key)
        return obj.get()["Body"].read().decode("utf-8")

    def write_file(self, key: str, data: dict) -> None:
        print(f"Writing to {self.bucket_name}/{key}")
        self.s3.Object(self.bucket_name, key).put(Body=data)

    def delete_file(self, key: str) -> None:
        """Deletes a file from S3"""
        print(f"Deleting {self.bucket_name}/{key}")
        self.s3.Object(self.bucket_name, key).delete()

    def list_contents(self, prefix: str = None) -> list:
        """Return list of keys within the bucket/prefix set, 1000 keys max per call"""
        items = []
        response = self.s3.list_objects_v2(Bucket=self.bucket_name, Prefix=prefix)

        try:
            for obj in response["Contents"]:
                if obj["Key"][-1] == "/":
                    continue

                items.append(obj["Key"])
        except KeyError:
            return None

        return items

    def copy_file(self, source_key: str, destination_key: str) -> None:
        """Copies a file from one location to another"""
        print(f"Copying {self.bucket_name}/{source_key} to {self.bucket_name}/{destination_key}")
        copy_source = {"Bucket": self.bucket_name, "Key": source_key}
        self.s3.meta.client.copy(copy_source, self.bucket_name, destination_key)
