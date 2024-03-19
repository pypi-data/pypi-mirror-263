from pydantic import BaseModel, Field
from typing import List, Optional, Literal
from phospho.utils import generate_timestamp, generate_uuid


class EvalModel(BaseModel):
    id: str = Field(default_factory=generate_uuid)
    created_at: int = Field(default_factory=generate_timestamp)
    project_id: str
    session_id: Optional[str] = None
    task_id: str
    # Flag to indicate if the task is success or failure
    value: Literal["success", "failure", "undefined"]
    # The source of the event (either "user" or "phospho-{id}")
    source: str


class TaskModel(BaseModel):
    id: str = Field(default_factory=generate_uuid)
    created_at: int = Field(default_factory=generate_timestamp)
    project_id: str
    session_id: Optional[str] = None
    input: str
    additional_input: Optional[dict] = Field(default_factory=dict)
    output: Optional[str] = None
    additional_output: Optional[dict] = Field(default_factory=dict)
    metadata: Optional[dict] = Field(default_factory=dict)
    data: Optional[dict] = Field(default_factory=dict)
    # Flag to indicate if the task is success or failure
    flag: Optional[Literal["success", "failure"]] = None
    last_eval: Optional[EvalModel] = None
    # Events are stored in a subcollection of the task document
    events: Optional[List] = Field(default_factory=list)
    # The environment is a label
    environment: str = Field(default="default environment")


class Test(BaseModel):
    id: str = Field(default_factory=generate_uuid)
    project_id: str
    created_by: str  # uid of the user who created the test
    created_at: int = Field(default_factory=generate_timestamp)
    last_updated_at: int
    terminated_at: Optional[int] = None
    status: Literal["started", "completed", "canceled"]
    summary: dict = Field(default_factory=dict)


ComparisonResults = Literal[
    "Old output is better",
    "New output is better",
    "Same quality",
    "Both are bad",
    "Error",
]


class Comparison(BaseModel):
    id: str
    created_at: int
    project_id: str
    instructions: Optional[str] = None
    context_input: str
    old_output: str
    new_output: str
    comparison_result: ComparisonResults
    source: str


class FlattenedTask(BaseModel, extra="allow"):
    task_id: str
    task_input: Optional[str] = None
    task_output: Optional[str] = None
    task_metadata: Optional[dict] = None
    task_eval: Optional[Literal["success", "failure"]] = None
    task_eval_source: Optional[str] = None
    task_eval_at: Optional[int] = None
    task_created_at: Optional[int] = None
    session_id: Optional[str] = None
    session_length: Optional[int] = None
    event_name: Optional[str] = None
    event_created_at: Optional[int] = None


class Project(BaseModel):
    id: str = Field(default_factory=generate_uuid)
    created_at: int = Field(default_factory=generate_timestamp)
    project_name: str
    org_id: str
    settings: dict = Field(default_factory=dict)
    user_id: Optional[str] = None


class EventDefinition(BaseModel):
    event_name: str
    description: str
    webhook: Optional[str] = None
    webhook_headers: Optional[dict] = None
