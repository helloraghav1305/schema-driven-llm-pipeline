from typing import Optional
from pydantic import ValidationError

from pipeline import output
from schemas import SupportTicket

def output_with_retry(
        email: str,
        max_retries: int = 2
) -> Optional[SupportTicket]:
    
    attempt=0

    while attempt <= max_retries:
        try:
            return output(email)
        
        except ValidationError as e:
            print(f"\n[Attempt {attempt + 1}] Validation failed:")
            print(e)

        attempt += 1

        if attempt > max_retries:
            print('Max retries reached. Returning None.')
            return None
        
        email = f"""
The previous output validation failed due to:
{str(e)}

Please strictly follow the required JSON schema and allowed enum values.

Email Text- 
{email}
"""
        