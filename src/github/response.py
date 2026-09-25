# INFRASTRUCTURE
from mcp.types import TextContent


# FUNCTIONS

def text_response(text: str) -> list[TextContent]:
    return [TextContent(type="text", text=text)]
