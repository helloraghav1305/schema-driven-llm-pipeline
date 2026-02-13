from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    input_variables=['email'],
    template="""
You are an AI system that converts customer emails into structured support tickets.

Your task:
Analyze the customer email message and extract required information.

Schema:
- issue_type: one of [billing, technical, account, other]
- summary: short summary in 1 sentence
- priority: one of [low, medium, high]
- action_required: true or false
- confidence: number between 0 and 1

Rules:
- Output only valid JSON
- Do not include explanations or extra text
- Use only allowed values for enums
- If information is unclear, make a conservative guess and lower the confidence

Customer Email Message:
{email}
"""
)