from functools import cached_property
from typing import Dict

import boto3
from boto3.dynamodb.conditions import Key


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


class BusinessReviewsCommonQueries:
    @staticmethod
    def get_review_business_info(table, business_id: str) -> Dict:
        query_params = {
            "KeyConditionExpression": Key("PK").eq(f"business#{business_id}")
            & Key("SK").eq("info")
        }

        response = table.query(**query_params)

        if response["Items"]:
            business_info = response["Items"][0]
            return business_info
        else:
            return {}
