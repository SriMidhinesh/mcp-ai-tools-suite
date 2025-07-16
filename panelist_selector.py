import asyncio
import pandas as pd
from typing import List
import openpyxl
from fastmcp import FastMCP
from mcp.server.streamable_http import StreamableHTTPServerTransport

path = "panel_member_info.xlsx"
mcp = FastMCP("mcp-member-selector")
df = pd.read_excel(path)
transport = StreamableHTTPServerTransport(
    mcp_session_id="panelist_selector"
)

@mcp.tool()
def member_selector(primary: str, secondary: str) -> List[str]:
    """
    Matches a candidate to the most suitable panelist based on primary and secondary skills using data from an Excel file.
    """
    matched_primary = df[df["Primary Skill"] == primary]["Panel Member"]
    matched_secondary = df[df["Secondary Skill"] == secondary]["Panel Member"]
    
    matched_panelists = pd.concat([matched_primary, matched_secondary]) \
                           .drop_duplicates() \
                           .tolist()
                           
    return matched_panelists

app = mcp.streamable_http_app()
 
#execution logic on startup
@app.on_event("startup")
async def startup():
    transport.connect()
    asyncio.create_task(mcp.run_streamable_http_async())

