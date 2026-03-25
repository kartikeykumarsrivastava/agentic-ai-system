from typing import TypedDict, Optional, List, Dict

class AgentState(TypedDict):
    query: str
    use_rag: bool
    use_eligibility: bool
    use_policy: bool

    documents: Optional[List[str]]
    eligibility: Optional[Dict]
    policy: Optional[str]

    final_answer: Optional[str]