from typing import Any
from carthooks import Client
from .logger import Logger
import os

class Task:
    def __init__(self, handler, app_id, collection_id, task_status_field, task_status_values,
                trigger="pulling_items", 
                filter=None, 
                pagelimit=1,
                include_locked=False,
                sort=['created'], 
                pulling_interval=30):
        self.handler = handler
        self.trigger = trigger
        self.pulling_options = {
            "app_id": app_id,
            "collection_id": collection_id,
            "task_status_field": task_status_field,
            "task_status_values": task_status_values,
            "filter": filter,
            "sort": sort,
            "pulling_interval": pulling_interval,
            "pagelimit": pagelimit,
            "include_locked": include_locked
        }

class Record:
    def __init__(self, sailor, app_id, collection_id, item_id, data):
        self.sailor = sailor
        self.app_id = app_id
        self.collection_id = collection_id
        self.item_id = item_id
        self.__record = data
        self.id = data["id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.title = data["title"]
        self.data = data["fields"]

    def __str__(self) -> str:
        return f"Record(title={self.__record.get('title')}, item_id={self.item_id})"
    
    def __repr__(self) -> str:
        return f"Record(app_id={self.app_id}, collection_id={self.collection_id}, item_id={self.item_id})"
    
    def lock(self, **kwargs):
        return self.sailor.lock(self, **kwargs)
    
    def unlock(self):
        return self.sailor.unlock(self)
    
    def update(self, map):
        return self.sailor.update(self, map)

    
class Context:
    def __init__(self, sailor, task, logger):
        self.task = task
        self.sailor = sailor
        self.logger = logger

    def create(self, app_id, collection_id, data):
        return self.sailor.create(app_id, collection_id, data)

class Sailor:
    def __init__(self, url=None, token=None, sailor_id=None):
        self.url = url
        self.token = token
        self.tasks = []
        self.logger = Logger("cybersailor")
        if sailor_id == None:
            self.sailor_id = os.uname().nodename
        else:
            self.sailor_id = sailor_id

    def subscribe(self, **kwargs):
        task = Task(**kwargs)
        self.tasks.append(task)

    def lock(self, record, lock_timeout=600, subject=None):
        self.logger.info(f"Locking task: {record}")
        return self.client.lock_item(record.app_id, record.collection_id, record.item_id, lock_timeout=lock_timeout, lock_id=self.sailor_id, subject=subject)

    def unlock(self, record):
        self.logger.info(f"Unlocking task: {record}")
        return self.client.unlock_item(record.app_id, record.collection_id, record.item_id, lock_id=self.sailor_id)

    def update(self, task, map):
        self.logger.info(f"Updating task: {task} with map: {map}")
        pass

    def create(self, app_id, collection_id, data):
        self.logger.info(f"Creating record in app_id: {app_id}, collection_id: {collection_id} with data: {data}")
        result = self.client.create_item(app_id, collection_id, data)
        return result

    def run(self):
        self.logger.info("Running...")

        self.client = Client(base_url = self.url)
        self.client.set_access_token(self.token)

        for task in self.tasks:
            if task.trigger == "pulling_items":
                print(task.pulling_options)
                app_id = task.pulling_options["app_id"]
                collection_id = task.pulling_options["collection_id"]
                self.logger.info(f"Pulling items from app_id: {app_id}, collection_id: {collection_id}")

                options = {
                    "limit": task.pulling_options["pagelimit"],
                }

                if task.pulling_options["include_locked"] == False:
                    options["unlockedOrLockedBy"] = self.sailor_id

                result = self.client.get_items(app_id, collection_id, **options)
                            # filter=task.pulling_options.filter, 
                            # limit=task.pulling_options["pagelimit"],
                            # sort=task.pulling_options.sort
                        # )
                items = result.data
                if items.__len__() > 0:
                    context = Context(sailor=self, task=task, logger=self.logger)
                    for item in items:
                        self.logger.info(f"Handling item: {item['id']}")
                        record = Record(sailor=self, app_id=app_id, collection_id=collection_id, item_id=item['id'], data=item)
                        task.handler(context, record)