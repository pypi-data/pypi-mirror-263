"""MultiOn agent."""
from __future__ import annotations

from typing import List

from vectorcraft.agent_toolkits.base import BaseToolkit
from vectorcraft.tools import BaseTool
from vectorcraft.tools.multion.close_session import MultionCloseSession
from vectorcraft.tools.multion.create_session import MultionCreateSession
from vectorcraft.tools.multion.update_session import MultionUpdateSession


class MultionToolkit(BaseToolkit):
    """Toolkit for interacting with the Browser Agent.

    **Security Note**: This toolkit contains tools that interact with the
        user's browser via the multion API which grants an agent
        access to the user's browser.

        Please review the documentation for the multion API to understand
        the security implications of using this toolkit.

        See https://python.langchain.com/docs/security for more information.
    """

    class Config:
        """Pydantic config."""

        arbitrary_types_allowed = True

    def get_tools(self) -> List[BaseTool]:
        """Get the tools in the toolkit."""
        return [MultionCreateSession(), MultionUpdateSession(), MultionCloseSession()]
