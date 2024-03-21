# SPDX-FileCopyrightText: 2019-2024 Helmholtz Centre Potsdam GFZ German Research Centre for Geosciences
# SPDX-FileCopyrightText: 2020-2021 Helmholtz-Zentrum Geesthacht GmbH
# SPDX-FileCopyrightText: 2021-2024 Helmholtz-Zentrum hereon GmbH
#
# SPDX-License-Identifier: Apache-2.0

"""Base module for a websocket connection."""
from __future__ import annotations

import logging
import random
import string
from abc import ABC
from typing import Optional

import websocket
from pydantic import validate_call

from demessaging import config


def get_random_letters(length: int) -> str:
    return "".join(random.choice(string.ascii_letters) for i in range(length))


logger = logging.getLogger(__name__)


class WebsocketConnection(ABC):
    """Base class to connect to a message broker using a websocket."""

    @validate_call
    def __init__(self, pulsar_config: config.BaseMessagingConfig):
        self.pulsar_config = pulsar_config

    def generate_response_topic(self, topic: Optional[str] = None) -> str:
        topic_name = topic or self.pulsar_config.topic or "anonymous"

        return topic_name + "_" + get_random_letters(8)

    def open_socket(
        self,
        subscription: Optional[str] = None,
        topic: Optional[str] = None,
        **connection_kws,
    ) -> websocket.WebSocket:
        topic_name = topic or self.pulsar_config.topic

        topic_url = self.pulsar_config.get_topic_url(topic_name, subscription)

        sock = websocket.create_connection(topic_url, **connection_kws)

        if sock:
            logger.debug("connection to {0} established".format(topic_url))

        return sock
