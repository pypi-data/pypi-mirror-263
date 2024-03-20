from dataclasses import dataclass, field
import uuid
import time
from typing import List, Optional, TypeVar
import requests
import os

from deepthread import RoleThread

from guisurfer.db.models import TaskRecord
from guisurfer.db.conn import WithDB
from guisurfer.server.models import TaskModel, TaskUpdateModel, TasksModel
from .env import HUB_API_KEY_ENV


T = TypeVar("T", bound="Task")


@dataclass
class Task(WithDB):
    """An agent task"""

    description: Optional[str] = None
    owner_id: Optional[str] = None
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    url: Optional[str] = None
    status: str = "defined"
    created: float = time.time()
    started: float = 0.0
    completed: float = 0.0
    feed: RoleThread = field(default_factory=RoleThread)
    thread: RoleThread = field(default_factory=RoleThread)
    assigned_to: Optional[str] = None
    error: str = ""
    output: str = ""
    remote: Optional[str] = None

    def __post_init__(self) -> None:
        if not self.remote and not self.description:
            raise ValueError("Task must have a description or a remote task")
        if self.remote:
            if not self.id:
                raise ValueError("ID must be set for remote tasks")
            print("\n!calling remote task", self.id)
            existing_task = self._remote_request(
                self.remote, "GET", f"/v1/tasks/{self.id}"
            )
            if not existing_task:
                raise ValueError("Remote task not found")
            print("\nfound existing task", existing_task)
            self.refresh()
            print("\nrefreshed tasks")
            print("\ntask: ", self.__dict__)
        else:
            self.save()

    def to_record(self) -> TaskRecord:
        return TaskRecord(
            id=self.id,
            owner_id=self.owner_id,
            description=self.description,
            url=self.url,
            status=self.status,
            created=self.created,
            started=self.started,
            completed=self.completed,
            thread_id=self.thread._id,
            assigned_to=self.assigned_to,
            feed_id=self.feed._id,
            error=self.error,
            output=self.output,
        )

    @classmethod
    def from_record(cls, record: TaskRecord) -> "Task":
        obj = cls.__new__(cls)
        obj.id = record.id
        obj.owner_id = record.owner_id
        obj.description = record.description
        obj.url = record.url
        obj.status = record.status
        obj.created = record.created
        obj.started = record.started
        obj.completed = record.completed
        obj.thread = RoleThread.find(id=record.thread_id)[0]
        obj.feed = RoleThread.find(id=record.feed_id)[0]
        obj.assigned_to = record.assigned_to
        obj.error = record.error
        obj.output = record.output
        return obj

    def post_message(
        self,
        role: str,
        msg: str,
        images: List[str] = [],
        private: bool = False,
        metadata: Optional[dict] = None,
    ) -> None:
        self.thread.post(role, msg, images, private, metadata)
        self.save()

    def post_feed(
        self,
        role: str,
        msg: str,
        images: List[str] = [],
        metadata: Optional[dict] = None,
    ) -> None:
        self.feed.post(role, msg, images, metadata=metadata)
        self.save()

    def save(self) -> None:
        print("\n!saving task", self.id)
        if self.remote:
            print("\n!saving remote task", self.id)
            try:
                existing_task = self._remote_request(
                    self.remote, "GET", f"/tasks/{self.id}"
                )
                print("\nfound existing task", existing_task)
            except:
                existing_task = None
            if existing_task:
                print("\nupdating existing task", existing_task)
                self._remote_request(
                    self.remote,
                    "PUT",
                    f"/tasks/{self.id}",
                    json_data=self.to_update_schema().model_dump(),
                )
                print("\nupdated existing task", self.id)
            else:
                print("\ncreating new task", self.id)
                self._remote_request(
                    self.remote,
                    "POST",
                    "/tasks",
                    json_data=self.to_schema().model_dump(),
                )
                print("\ncreated new task", self.id)
        else:
            print("\n!saving local db task", self.id)
            for db in self.get_db():
                db.merge(self.to_record())
                db.commit()

    @classmethod
    def find(cls, remote: Optional[str] = None, **kwargs) -> List["Task"]:
        if remote:
            remote_response = cls._remote_request(
                remote, "GET", "/tasks", json_data=kwargs
            )
            tasks = TasksModel(**remote_response)
            if remote_response is not None:
                return [cls.from_schema(TaskModel(**record)) for record in tasks.tasks]
        else:
            for db in cls.get_db():
                records = db.query(TaskRecord).filter_by(**kwargs).all()
                return [cls.from_record(record) for record in records]

    def update(self, **kwargs) -> None:
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

        self.save()

    @classmethod
    def delete(cls, id: str, owner_id: str, remote: Optional[str] = None) -> None:
        if cls.remote:
            cls._remote_request(remote, "DELETE", f"/tasks/{id}")
        else:
            for db in cls.get_db():
                record = (
                    db.query(TaskRecord).filter_by(id=id, owner_id=owner_id).first()
                )
                if record:
                    db.delete(record)
                    db.commit()

    def to_schema(self) -> TaskModel:
        return TaskModel(
            id=self.id,
            description=self.description,
            url=self.url,
            thread=self.thread.to_schema(),
            feed=self.feed.to_schema(),
            status=self.status,
            created=self.created,
            started=self.started,
            completed=self.completed,
            assigned_to=self.assigned_to,
            error=self.error,
            output=self.output,
        )

    def to_update_schema(self) -> TaskUpdateModel:
        return TaskUpdateModel(
            description=self.description,
            url=self.url,
            status=self.status,
            assigned_to=self.assigned_to,
            feed=self.feed.to_schema(),
            thread=self.thread.to_schema(),
            error=self.error,
            output=self.output,
            completed=self.completed,
        )

    @classmethod
    def from_schema(cls, schema: TaskModel, owner_id: str) -> "Task":
        return cls(
            id=schema.id if schema.id else str(uuid.uuid4()),
            owner_id=owner_id,
            description=schema.description,
            thread=(
                RoleThread.from_schema(schema.thread)
                if schema.thread
                else RoleThread(owner_id=owner_id)
            ),
            status=schema.status if schema.status else "defined",
            created=schema.created,
            started=schema.started,
            feed=(
                RoleThread.from_schema(schema.feed)
                if schema.feed
                else RoleThread(owner_id=owner_id)
            ),
            completed=schema.completed,
            assigned_to=schema.assigned_to,
            error=schema.error,
            output=schema.output,
        )

    def refresh(self, auth_token: Optional[str] = None) -> None:
        print("\n!refreshing task", self.id)
        if self.remote:
            print("\n!refreshing remote task", self.id)
            try:

                remote_task = self._remote_request(
                    self.remote, "GET", f"/tasks/{self.id}", auth_token=auth_token
                )
                print("\nfound remote task", remote_task)
                if remote_task:
                    schema = TaskModel(**remote_task)
                    self.description = schema.description
                    self.url = schema.url
                    self.status = schema.status if schema.status else "defined"
                    self.created = schema.created
                    self.started = schema.started
                    self.completed = schema.completed
                    self.assigned_to = schema.assigned_to
                    self.error = schema.error
                    self.output = schema.output
                    self.thread = (
                        RoleThread.from_schema(schema.thread)
                        if schema.thread
                        else RoleThread(owner_id=self.owner_id)
                    )
                    self.feed = (
                        RoleThread.from_schema(schema.feed)
                        if schema.feed
                        else RoleThread(owner_id=self.owner_id)
                    )
                    print("\nrefreshed remote task", self.id)
            except requests.RequestException as e:
                raise e
        else:
            raise ValueError("Refresh is only supported for remote tasks")

    @classmethod
    def _remote_request(
        self,
        addr: str,
        method: str,
        endpoint: str,
        json_data: Optional[dict] = None,
        auth_token: Optional[str] = None,
    ) -> Optional[List[T]]:
        url = f"{addr}{endpoint}"
        headers = {}
        if not auth_token:
            auth_token = os.getenv(HUB_API_KEY_ENV)
            if not auth_token:
                raise Exception(f"Hub API key not found, set ${HUB_API_KEY_ENV}")
        print(f"\n!auth_token: {auth_token}")
        headers["Authorization"] = f"Bearer {auth_token}"
        try:
            if method.upper() == "GET":
                print("\ncalling remote task GET with url: ", url)
                print("\ncalling remote task GET with headers: ", headers)
                response = requests.get(url, headers=headers)
            elif method.upper() == "POST":
                print("\ncalling remote task POST with: ", url, json_data)
                print("\ncalling remote task POST with headers: ", headers)
                response = requests.post(url, json=json_data, headers=headers)
            elif method.upper() == "PUT":
                print("\ncalling remote task PUT with: ", url, json_data)
                print("\ncalling remote task PUT with headers: ", headers)
                response = requests.put(url, json=json_data, headers=headers)
            elif method.upper() == "DELETE":
                print("\ncalling remote task DELETE with: ", url)
                print("\ncalling remote task DELETE with headers: ", headers)
                response = requests.delete(url, headers=headers)
            else:
                return None

            try:
                response.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print("HTTP Error:", e)
                print("Status Code:", response.status_code)
                try:
                    print("Response Body:", response.json())
                except ValueError:
                    print("Raw Response:", response.text)
                raise
            print("\nresponse: ", response.__dict__)
            print("\response.status_code: ", response.status_code)

            try:
                response_json = response.json()
                print("\nresponse_json: ", response_json)
                return response_json
            except ValueError:
                print("Raw Response:", response.text)
                return None

        except requests.RequestException as e:
            raise e
