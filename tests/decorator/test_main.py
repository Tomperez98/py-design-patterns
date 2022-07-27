from typing import Dict, List, Type

import pytest

from patterns import decorator


@pytest.mark.parametrize(
    "desired_notification_services, expected_result",
    [
        (
            [
                "whatsapp",
                "slack",
                "sms",
            ],
            "Default notification of the business process"
            ", also notified via WhatsApp"
            ", also notified via Slack"
            ", also notified via SMS",
        ),
        (
            [
                "slack",
                "whatsapp",
                "sms",
            ],
            "Default notification of the business process"
            ", also notified via Slack"
            ", also notified via WhatsApp"
            ", also notified via SMS",
        ),
        (
            [
                "slack",
            ],
            "Default notification of the business process"
            ", also notified via Slack",
        ),
        (
            [
                "whatsapp",
                "facebook",
            ],
            "Default notification of the business process"
            ", also notified via WhatsApp"
            ", also notified via Facebook",
        ),
    ],
)
def test_pattern(
    desired_notification_services: List[str], expected_result: str
):

    available_notification_services: Dict[str, Type[decorator.BaseNotify]] = {
        "whatsapp": decorator.WhatsAppNotify,
        "slack": decorator.SlackNotify,
        "sms": decorator.SMSNotify,
        "facebook": decorator.FacebookNotify,
    }
    only_with_default_notification = decorator.BusinessProcess()

    stack = only_with_default_notification
    for notification_service in desired_notification_services:
        service = available_notification_services[notification_service]

        stack = service(stack)

    assert stack.notify() == expected_result
