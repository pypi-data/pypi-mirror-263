from datetime import timedelta
from typing import Union

from aws_cdk import Duration
from aws_cdk.aws_cloudwatch import Metric, ComparisonOperator, TreatMissingData, GraphWidget
from aws_cdk.aws_lambda import Function

from infraflow.cdk.core.utils import to_duration


class LambdaMetrics:
    def __init__(self, function: Function):
        self.function = function

    def duration_ave(self, period: Union[int, timedelta, Duration]) -> Metric:
        return self.function.metric_duration(statistic="average", period=to_duration(period))

    def duration_max(self, period: Union[int, timedelta, Duration]) -> Metric:
        return self.function.metric_duration(statistic="max", period=to_duration(period))

    def duration_min(self, period: Union[int, timedelta, Duration]) -> Metric:
        return self.function.metric_duration(statistic="min", period=to_duration(period))

    def concurrent_executions_ave(self, period: Union[int, timedelta, Duration]) -> Metric:
        return self.function.metric_all_concurrent_executions(statistic="average", period=to_duration(period))

    def concurrent_executions_max(self, period: Union[int, timedelta, Duration]) -> Metric:
        return self.function.metric_all_concurrent_executions(statistic="max", period=to_duration(period))

    def concurrent_executions_min(self, period: Union[int, timedelta, Duration]) -> Metric:
        return self.function.metric_all_concurrent_executions(statistic="min", period=to_duration(period))

    def invocations_ave(self, period: Union[int, timedelta, Duration]) -> Metric:
        return self.function.metric_invocations(statistic="average", period=to_duration(period))

    def invocations_max(self, period: Union[int, timedelta, Duration]) -> Metric:
        return self.function.metric_all_invocations(statistic="max", period=to_duration(period))

    def invocations_min(self, period: Union[int, timedelta, Duration]) -> Metric:
        return self.function.metric_invocations(statistic="min", period=to_duration(period))

    def invocations_sum(self, period: Union[int, timedelta, Duration]) -> Metric:
        return self.function.metric_invocations(statistic="sum", period=to_duration(period))

    def errors_ave(self, period: Union[int, timedelta, Duration]) -> Metric:
        return self.function.metric_errors(statistic="average", period=to_duration(period))

    def errors_max(self, period: Union[int, timedelta, Duration]) -> Metric:
        return self.function.metric_errors(statistic="max", period=to_duration(period))

    def errors_min(self, period: Union[int, timedelta, Duration]) -> Metric:
        return self.function.metric_errors(statistic="min", period=to_duration(period))

    def errors_sum(self, period: Union[int, timedelta, Duration]) -> Metric:
        return self.function.metric_errors(statistic="sum", period=to_duration(period))

    def throttles_ave(self, period: Union[int, timedelta, Duration]) -> Metric:
        return self.function.metric_throttles(statistic="average", period=to_duration(period))

    def throttles_max(self, period: Union[int, timedelta, Duration]) -> Metric:
        return self.function.metric_throttles(statistic="max", period=to_duration(period))

    def throttles_min(self, period: Union[int, timedelta, Duration]) -> Metric:
        return self.function.metric_throttles(statistic="min", period=to_duration(period))

    def throttles_sum(self, period: Union[int, timedelta, Duration]) -> Metric:
        return self.function.metric_throttles(statistic="sum", period=to_duration(period))


class LambdaAlarms:
    def __init__(self, function: Function, reserved_concurrency: int):
        self.function = function
        self.metrics = LambdaMetrics(function)
        self.reserved_concurrency = reserved_concurrency

    def running_longer_than_expected(self, over_timespan: Union[int, timedelta, Duration], evaluation_periods: int, percent_of_timeout_threshold: float):
        return self.metrics.duration_max(over_timespan).create_alarm(
            alarm_name="LambdaRunningLongerThanExpected",
            alarm_description="Lambda running longer than expected",
            threshold=to_duration(round(self.function.timeout.to_seconds() * percent_of_timeout_threshold)),
            evaluation_periods=evaluation_periods,
            comparison_operator=ComparisonOperator.GREATER_THAN_THRESHOLD,
            treat_missing_data=TreatMissingData.NOT_BREACHING,
        )

    def invocations_exceed_threshold(self, over_timespan: Union[int, timedelta, Duration], evaluation_periods: int, threshold: int):
        return self.metrics.invocations_ave(over_timespan).create_alarm(
            alarm_name="LambdaInvocationsExceedThreshold",
            alarm_description="Lambda invocations exceed threshold",
            threshold=threshold,
            evaluation_periods=evaluation_periods,
            comparison_operator=ComparisonOperator.GREATER_THAN_THRESHOLD,
            treat_missing_data=TreatMissingData.NOT_BREACHING,
        )

    def concurrency_exceed_threshold(self, over_timespan: Union[int, timedelta, Duration], evaluation_periods: int, percent_of_max_threshold: float):
        return self.metrics.concurrent_executions_ave(over_timespan).create_alarm(
            alarm_name="LambdaConcurrencyExceedThreshold",
            alarm_description="Lambda concurrency exceed threshold",
            threshold=round(self.reserved_concurrency * percent_of_max_threshold),
            evaluation_periods=evaluation_periods,
            comparison_operator=ComparisonOperator.GREATER_THAN_THRESHOLD,
            treat_missing_data=TreatMissingData.NOT_BREACHING,
        )

    def errors_exceed_threshold(self, over_timespan: Union[int, timedelta, Duration], evaluation_periods: int, threshold: float):
        return self.metrics.errors_ave(over_timespan).create_alarm(
            alarm_name="LambdaErrorsExceedThreshold",
            alarm_description="Lambda errors exceed threshold",
            threshold=threshold,
            evaluation_periods=evaluation_periods,
            comparison_operator=ComparisonOperator.GREATER_THAN_THRESHOLD,
            treat_missing_data=TreatMissingData.NOT_BREACHING,
        )



class LambdaWidgets:
    def __init__(self, function: Function):
        self.function = function
        self.metrics = LambdaMetrics(function)

    def errors_sum_widget(self, period: Union[int, timedelta, Duration], width: int, height: int):
        widget = GraphWidget(
            title=f"{self.function.function_name} - Total Errors",
            height=height,
            width=width,
        )
        widget.add_left_metric(self.metrics.errors_sum(period=period))
        return widget

    def concurrent_executions_widget(self, period: Union[int, timedelta, Duration], width: int, height: int):
        widget = GraphWidget(
            title=f"{self.function.function_name} - Concurrent Executions",
            height=height,
            width=width,
        )
        widget.add_left_metric(self.metrics.concurrent_executions_max(period=period))
        return widget

    def invocation_widget(self, period: Union[int, timedelta, Duration], width: int, height: int):
        widget = GraphWidget(
            title=f"{self.function.function_name} - Invocations",
            height=height,
            width=width,
        )
        widget.add_left_metric(self.metrics.invocations_sum(period=period))
        return widget

    def duration_widget(self, period: Union[int, timedelta, Duration], width: int, height: int):
        widget = GraphWidget(
            title=f"{self.function.function_name} - Duration",
            height=height,
            width=width,
        )
        widget.add_left_metric(self.metrics.duration_ave(period=period))
        return widget

    def throttle_widget(self, period: Union[int, timedelta, Duration], width: int, height: int):
        widget = GraphWidget(
            title=f"{self.function.function_name} - Throttles",
            height=height,
            width=width,
        )
        widget.add_left_metric(self.metrics.throttles_sum(period=period))
        return widget


class LambdaInstrumentation:
    def __init__(self, function: Function, reserved_concurrency):
        self.metrics = LambdaMetrics(function)
        self.reserved_concurrency = reserved_concurrency
        self.function = function
        self.widgets = LambdaWidgets(function)
        self.alarms = LambdaAlarms(function=function, reserved_concurrency=reserved_concurrency)

