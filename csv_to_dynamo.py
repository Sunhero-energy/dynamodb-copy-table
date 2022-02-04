import decimal
import json
import logging
import os
import pprint
import time
import boto3
import csv
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)
dynamodb = boto3.resource('dynamodb')


with open('results.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    keys = []
    for row in csv_reader:
      # create dict for each row
      if line_count == 0:
        keys = row
        line_count =+1 
      else:
        item = {}
        for col in keys:
          if row[keys.index(col)] != '': item[col] = row[keys.index(col)]
        # put to dynamodb
        table = dynamodb.Table('sunhero-coreApi-prod')
        table.put_item(Item=item)
    
