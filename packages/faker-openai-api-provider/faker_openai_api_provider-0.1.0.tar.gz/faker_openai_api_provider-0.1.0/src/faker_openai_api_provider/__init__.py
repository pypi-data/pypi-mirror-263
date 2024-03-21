from typing import Any

from faker.providers import BaseProvider

from .__version__ import __version__
from ._chat import ChatProvider
from ._file import FileProvider
from ._assistants import AssistantProvider
from ._thread import ThreadProvider


class OpenAiApiProvider(BaseProvider):
    def __init__(self, generator: Any) -> None:
        super().__init__(generator)
        self._api = OpenAiApiProvider.Api()

    def openai(self):
        return self._api

    class Api:
        def __init__(self) -> None:
            self.chat = ChatProvider()
            self.file = FileProvider()
            self.beta = OpenAiApiProvider.Api.BetaProviders()

        class BetaProviders:
            def __init__(self) -> None:
                self.assistant = AssistantProvider()
                self.thread = ThreadProvider()
