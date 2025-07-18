import pandas as pd
from google import genai
from dotenv import load_dotenv
import os
from fastmcp import FastMCP

mcp = FastMCP("panelist_selector")

load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key = google_api_key)

input_data = {
    "panel_df" : "pd.read_excel('panel_member_info.xlsx')",
    "candidate_info" : "Sri Midhinesh Sankurabhukta, with 6 months of experience in Sonata Software whose skills are Python and Machine Learning, is scheduled for an interview on 19th July 2025 at 10:00 AM."
}

@mcp.tool()
def panelist_selector(panel_info: pd.DataFrame, candidate_info: str) -> str | None:
    """
    Matches a candidate to the most suitable panelist based on Primary, Secondary skills, Availablity and Expereince using data from an Excel file.
    """
    columns = list(panel_info.columns)
    panel_text = "\n".join(
        " | ".join(f"{col}: {row[col]}" for col in columns)
        for _, row in panel_info.iterrows()
    )
    
    prompt = f"""
    
    This is the Information available on the candidate. {candidate_info}
    
    Here is the list of panelists:
    {panel_text}
    
    Based on skill, match and experience, Select the most suitable panelist.
    Make sure that the interview's experience is always more than the candidate's experience
    Respond with their name and reason for your choice. Give a sarcastic reason as well.
    """
    
    response = client.models.generate_content(
        model = "gemini-2.5-flash-lite",
        contents = prompt
    )
    
    return response.text

if __name__ == "__main__":
    mcp.run(transport = "stdio")