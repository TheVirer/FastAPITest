from fastapi import APIRouter
from schemas import STask, STaskAdd, STaskId
from repository import TaskRepository
from typing import Annotated
from fastapi import Depends

router = APIRouter(prefix="/tasks",tags=["Tаски"])

@router.post("")
async def add_task(task: Annotated[STaskAdd, Depends()]) -> STaskId:
    task_id = await TaskRepository.add_task(task)
    return {"ok": True, "task_id": task_id}

@router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.find_all()
    return tasks