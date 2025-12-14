"""Custom tools loader for ha-lmstudio-mcp."""
import logging
import yaml
from pathlib import Path
from typing import Dict, Any, List, Optional

_LOGGER = logging.getLogger(__name__)

class CustomToolsLoader:
    """Load and manage custom tools."""

    def __init__(self, hass, entry=None):
        """Initialize the custom tools loader."""
        self.hass = hass
        self.entry = entry  # Store config entry for options
        self.tools = {}
        self.enabled_tools = []
        self._config_loaded = False

    async def _load_config(self):
        """Load custom tools configuration asynchronously."""
        config_path = Path(__file__).parent / "config.yaml"
        if config_path.exists():
            try:
                # Use executor to avoid blocking the event loop
                def _read_config():
                    with open(config_path, 'r') as f:
                        return yaml.safe_load(f) or {}

                config = await self.hass.async_add_executor_job(_read_config)
                self.enabled_tools = config.get('enabled_tools', [])
                self._config_loaded = True
            except Exception as e:
                _LOGGER.error(f"Failed to load custom tools config: {e}")
                self.enabled_tools = []

    async def initialize(self):
        """Initialize all enabled custom tools."""
        # Load config first if not already loaded
        if not self._config_loaded:
            await self._load_config()
        if "brave_search" in self.enabled_tools:
            try:
                from .brave_search import BraveSearchTool
                # Pass API key from options if available
                api_key = None
                if self.entry:
                    api_key = self.entry.options.get("brave_api_key")
                self.tools["brave_search"] = BraveSearchTool(self.hass, api_key)
                await self.tools["brave_search"].initialize()
            except Exception as e:
                _LOGGER.error(f"Failed to initialize brave_search tool: {e}")

        if "read_url" in self.enabled_tools:
            try:
                from .read_url import ReadUrlTool
                self.tools["read_url"] = ReadUrlTool(self.hass)
                await self.tools["read_url"].initialize()
            except Exception as e:
                _LOGGER.error(f"Failed to initialize read_url tool: {e}")

    def get_tool_definitions(self) -> List[Dict[str, Any]]:
        """Get MCP tool definitions for all enabled tools."""
        definitions = []
        for tool in self.tools.values():
            try:
                definitions.extend(tool.get_tool_definitions())
            except Exception as e:
                _LOGGER.error(f"Error getting tool definitions: {e}")
        return definitions

    async def handle_tool_call(self, tool_name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Handle a custom tool call."""
        for tool in self.tools.values():
            if tool.handles_tool(tool_name):
                return await tool.handle_call(tool_name, arguments)

        raise ValueError(f"Unknown custom tool: {tool_name}")

    def is_custom_tool(self, tool_name: str) -> bool:
        """Check if a tool name is a custom tool."""
        for tool in self.tools.values():
            if tool.handles_tool(tool_name):
                return True
        return False