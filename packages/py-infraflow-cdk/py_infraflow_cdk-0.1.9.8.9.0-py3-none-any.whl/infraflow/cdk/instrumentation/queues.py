from datetime import timedelta
from typing import Union

from aws_cdk import Duration
from aws_cdk.aws_cloudwatch import ComparisonOperator, TreatMissingData, GraphWidget
from aws_cdk.aws_sqs import Queue

from infraflow.cdk.core.utils import to_duration


class QueueMetrics:
    def __init__(self, queue: Queue):
        self.queue = queue

    def sent_ave(self, period: Union[int, timedelta, Duration]):
        return self.queue.metric_number_of_messages_sent(period=to_duration(period) if period else None, statistic="average")

    def sent_max(self, period: Union[int, timedelta, Duration]):
        return self.queue.metric_number_of_messages_sent(period=to_duration(period) if period else None, statistic="max")

    def sent_min(self, period: Union[int, timedelta, Duration]):
        return self.queue.metric_number_of_messages_sent(period=to_duration(period) if period else None, statistic="min")

    def sent_sum(self, period: Union[int, timedelta, Duration]):
        return self.queue.metric_number_of_messages_sent(period=to_duration(period) if period else None, statistic="sum")

    def length_ave(self, period: Union[int, timedelta, Duration]):
        return self.queue.metric_approximate_number_of_messages_visible(period=to_duration(period) if period else None, statistic="average")

    def length_max(self, period: Union[int, timedelta, Duration]):
        return self.queue.metric_approximate_number_of_messages_visible(period=to_duration(period) if period else None, statistic="max")

    def length_min(self, period: Union[int, timedelta, Duration]):
        return self.queue.metric_approximate_number_of_messages_visible(period=to_duration(period) if period else None, statistic="min")

    def age_of_oldest_ave(self, period: Union[int, timedelta, Duration]):
        return self.queue.metric_approximate_age_of_oldest_message(period=to_duration(period) if period else None, statistic="average")

    def age_of_oldest_max(self, period: Union[int, timedelta, Duration]):
        return self.queue.metric_approximate_age_of_oldest_message(period=to_duration(period) if period else None, statistic="max")

    def age_of_oldest_min(self, period: Union[int, timedelta, Duration]):
        return self.queue.metric_approximate_age_of_oldest_message(period=to_duration(period) if period else None, statistic="min")


class QueueAlarms:
    def __init__(self, queue: Queue):
        self.queue = queue
        self.metrics = QueueMetrics(queue)

    def age_of_oldest_over_threshold(self, threshold: int, period: Union[int, timedelta, Duration], evaluation_periods: int):
        return self.metrics.age_of_oldest_ave(period).create_alarm(
            alarm_name=f"{self.queue.queue_name}_AgeOfOldestOverThreshold",
            threshold=threshold,
            evaluation_periods=evaluation_periods,
            comparison_operator=ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD,
            period=to_duration(period),
            statistic="average",
            treat_missing_data=TreatMissingData.NOT_BREACHING,
        )

    def length_over_threshold(self, threshold: int, period: Union[int, timedelta, Duration], evaluation_periods: int):
        return self.metrics.length_ave(period).create_alarm(
            alarm_name=f"{self.queue.queue_name}_LengthOverThreshold",
            threshold=threshold,
            evaluation_periods=evaluation_periods,
            comparison_operator=ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD,
            period=to_duration(period),
            statistic="average",
            treat_missing_data=TreatMissingData.NOT_BREACHING,
        )

    def sent_over_threshold(self, threshold: int, period: Union[int, timedelta, Duration], evaluation_periods: int):
        return self.metrics.sent_ave(period).create_alarm(
            alarm_name=f"{self.queue.queue_name}_SentOverThreshold",
            threshold=threshold,
            evaluation_periods=evaluation_periods,
            comparison_operator=ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD,
            period=to_duration(period),
            statistic="average",
            treat_missing_data=TreatMissingData.NOT_BREACHING,
        )


class QueueWidgets:
    def __init__(self, queue: Queue):
        self.queue = queue
        self.metrics = QueueMetrics(queue)

    def age_max_widget(self, period: Union[int, timedelta, Duration], width: int, height: int):
        widget = GraphWidget(
            title=f"{self.queue.queue_name} - Age of Oldest Message",
            height=height,
            width=width,
        )
        widget.add_left_metric(self.metrics.age_of_oldest_max(period=period))
        return widget

    def length_max_widget(self, period: Union[int, timedelta, Duration], width: int, height: int):
        widget = GraphWidget(
            title=f"{self.queue.queue_name} - Length of Queue",
            height=height,
            width=width,
        )
        widget.add_left_metric(self.metrics.length_max(period=period))
        return widget

    def sent_sum_widget(self, period: Union[int, timedelta, Duration], width: int, height: int):
        widget = GraphWidget(
            title=f"{self.queue.queue_name} - Total Messages Sent",
            height=height,
            width=width,
        )
        widget.add_left_metric(self.metrics.sent_sum(period=period))
        return widget


class QueueInstrumentation:
    def __init__(self, queue: Queue):
        self.metrics = QueueMetrics(queue)
        self.queue = queue
        self.widgets = QueueWidgets(queue)
        self.alarms = QueueAlarms(queue)
