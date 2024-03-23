"""setting configuration for aws client wrapper"""
import os
from .stats import AwsStats
aws_stats = AwsStats()

def configure(aws_role_arn=None, redis_host=None, aws_stats_func=None, aws_stats_project_id=None,
              aws_stats_dataset_id=None, aws_stats_table_id=None):
    """configure aws client"""
    os.environ['AWS_ROLE_ARN'] = aws_role_arn
    os.environ['REDISHOST'] = redis_host
    aws_stats.set(aws_stats_func=aws_stats_func, aws_stats_project_id=aws_stats_project_id,
                  aws_stats_dataset_id=aws_stats_dataset_id, aws_stats_table_id=aws_stats_table_id)
