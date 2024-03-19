from functools import cached_property

import boto3


# noinspection PyMethodMayBeStatic
class BaseDynamoDBClient:
    def __init__(
        self,
        region_name="us-east-1",
        profile_name=None,
    ):
        self.region_name = region_name
        self.profile_name = profile_name


class DynamoDBClient(BaseDynamoDBClient):
    @cached_property
    def client(self):
        session = boto3.Session(
            region_name=self.region_name, profile_name=self.profile_name
        )
        return session.client("dynamodb")

    def put_item(self, table_name, item):
        return self.client.put_item(TableName=table_name, Item=item)
