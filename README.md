# MCP AI Tools Suite

A modular, AI-powered server built using [FastMCP](https://github.com/openai/fastmcp) that hosts practical tools for drafting content, automating email, generating learning courses, and assigning interview panelists. Tools are designed to be composable and reusable via prompts or direct interaction.

---

## 🔧 Tools Overview

### 1. 📧 Email Drafter Tool

- Drafts professional emails based on context and purpose.
- Uses Gemini AI for language generation.
- Input: Subject, recipient type, purpose/context
- Output: Drafted email content

### 2. 📬 Email Sender Tool _(details to be shared)_

- Sends emails using authenticated SMTP/Graph APIs.
- Integrates with email drafting tool to automate delivery.
- Credentials to be configured securely.

### 3. 📘 Course Drafter Tool

- Generates structured learning material (chapters/modules) based on a given topic.
- Uses **Gemini AI** for knowledge synthesis.
- Input: Topic (e.g., "Machine Learning")
- Output: Course outline with chapters

### 4. 🧑‍💼 Panelist Selector Tool

- Matches candidate skills to suitable interview panelists.
- Based on Excel sheet of panelists (primary and secondary skills).
- Uses Gemini AI for intelligent fallback or ranking logic.
- Input: Candidate’s primary & secondary skills
- Output: Best-matching panelist(s)

---

## 🧠 Prompts

### Prompt 1: `course_drafter_and_send_email`

- Combines **Course Drafter Tool** and **Email Sender Tool**
- Use case: Automatically draft a course and email it to a learner

### Prompt 2: `panelist_selector_and_send_email`

- Combines **Panelist Selector Tool** and **Email Sender Tool**
- Use case: Select an interview panelist and notify them via email

---

## 🔐 Credential Management

- **Gemini AI API Key** is securely stored in the **Resources** section of the MCP server
- Reused across tools like `email_drafter`, `course_drafter`, and `panelist_selector`

---

## 🛠 Setup Instructions

```bash
# 1. Clone the repository
git clone https://github.com/SriMidhinesh/mcp-ai-tools-suite.git
cd mcp-ai-tools-suite

# 2. Create and activate a virtual environment
python -m venv .venv
# On Linux/macOS:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the MCP server
uvicorn mcp_server:app --host 0.0.0.0 --port 8000 ("Replace 'mcp_server' with the appropriate file name")
```
