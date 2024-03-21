from datetime import timedelta
from typing import Union

from aws_cdk import Duration
from aws_cdk.aws_cloudwatch import ComparisonOperator, TreatMissingData, GraphWidget
from aws_cdk.aws_ecs import FargateService

from infraflow.cdk.core.utils import to_duration


class EcsServiceMetrics:
    def __init__(self, ecs_service: FargateService):
        self.ecs_service = ecs_service

    def cpu_ave(self, period):
        return self.ecs_service.metric_cpu_utilization(statistic="average", period=to_duration(period))

    def cpu_min(self, period):
        return self.ecs_service.metric_cpu_utilization(statistic="min", period=to_duration(period))

    def cpu_max(self, period):
        return self.ecs_service.metric_cpu_utilization(statistic="max", period=to_duration(period))

    def memory_ave(self, period):
        return self.ecs_service.metric_memory_utilization(statistic="average", period=to_duration(period))

    def memory_min(self, period):
        return self.ecs_service.metric_memory_utilization(statistic="min", period=to_duration(period))

    def memory_max(self, period):
        return self.ecs_service.metric_memory_utilization(statistic="max", period=to_duration(period))

class EcsServiceAlarms:
    def __init__(self, ecs_service: FargateService):
        self.ecs_service = ecs_service
        self.metrics = EcsServiceMetrics(ecs_service)

    def cpu_over_threshold(self, over_timespan: Union[int, timedelta, Duration], evaluation_periods: int, threshold: float):
        return self.metrics.cpu_ave(period=over_timespan).create_alarm(
            alarm_name="ContainerCPUOverThreshold",
            alarm_description="Container CPU Over Threshold",
            evaluation_periods=evaluation_periods,
            threshold=threshold,
            comparison_operator=ComparisonOperator.GREATER_THAN_THRESHOLD,
            treat_missing_data=TreatMissingData.NOT_BREACHING,
        )

    def cpu_under_threshold(self, over_timespan: Union[int, timedelta, Duration], evaluation_periods: int, threshold: float):
        return self.metrics.cpu_ave(period=over_timespan).create_alarm(
            alarm_name="ContainerCPUUnderThreshold",
            alarm_description="Container CPU Under Threshold",
            evaluation_periods=evaluation_periods,
            threshold=threshold,
            comparison_operator=ComparisonOperator.LESS_THAN_THRESHOLD,
            treat_missing_data=TreatMissingData.NOT_BREACHING,
        )

    def memory_over_threshold(self, over_timespan: Union[int, timedelta, Duration], evaluation_periods: int, threshold: float):
        return self.metrics.cpu_ave(period=over_timespan).create_alarm(
            alarm_name="ContainerMemoryOverThreshold",
            alarm_description="Container Memory Over Threshold",
            evaluation_periods=evaluation_periods,
            threshold=threshold,
            comparison_operator=ComparisonOperator.GREATER_THAN_THRESHOLD,
            treat_missing_data=TreatMissingData.NOT_BREACHING,
        )

    def memory_under_threshold(self, over_timespan: Union[int, timedelta, Duration], evaluation_periods: int, threshold: float):
        return self.metrics.cpu_ave(period=over_timespan).create_alarm(
            alarm_name="ContainerMemoryUnderThreshold",
            alarm_description="Container Memory Under Threshold",
            evaluation_periods=evaluation_periods,
            threshold=threshold,
            comparison_operator=ComparisonOperator.LESS_THAN_THRESHOLD,
            treat_missing_data=TreatMissingData.NOT_BREACHING,
        )


class EcsServiceWidgets:
    def __init__(self, ecs_service: FargateService):
        self.ecs_service = ecs_service
        self.metrics = EcsServiceMetrics(ecs_service)

    def combined_widget(self, period: Union[int, timedelta, Duration], width: int, height: int):
        widget = GraphWidget(
            title=f"{self.ecs_service.service_name} - CPU",
            height=height,
            width=width,
        )
        widget.add_left_metric(self.metrics.cpu_ave(period=period))
        widget.add_right_metric(self.metrics.memory_ave(period=period))
        return widget

    def cpu_widget(self, period: Union[int, timedelta, Duration], width: int, height: int):
        widget = GraphWidget(
            title=f"{self.ecs_service.service_name} - CPU",
            height=height,
            width=width,
        )
        widget.add_left_metric(self.metrics.cpu_ave(period=period))
        return widget

    def memory_widget(self, period: Union[int, timedelta, Duration], width: int, height: int):
        widget = GraphWidget(
            title=f"{self.ecs_service.service_name} - Memory",
            height=height,
            width=width,
        )
        widget.add_left_metric(self.metrics.memory_ave(period=period))
        return widget

class EcsServiceInstrumentation:
    def __init__(self, ecs_service: FargateService):
        self.metrics = EcsServiceMetrics(ecs_service)
        self.ecs_service = ecs_service
        self.widgets = EcsServiceWidgets(ecs_service)
        self.alarms = EcsServiceAlarms(ecs_service)
