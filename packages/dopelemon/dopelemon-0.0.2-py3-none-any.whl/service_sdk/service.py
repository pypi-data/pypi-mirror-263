import os
from logging import Logger
from typing import Optional, Callable, Any

import uvicorn
from fastapi import FastAPI, APIRouter, HTTPException
from starlette.routing import Route

from service_sdk.utils import force_kill_process, setup_logger
from service_sdk.manager.work_manager import WorkManager


class Service:
    def __init__(
            self,
            api: Optional[FastAPI] = None,
            worker_callback: Optional[Callable[[], Any]] = None,
            manager: Optional[WorkManager] = None,
            logger: Optional[Logger] = None
    ):
        self.logger = logger or setup_logger()
        self.api = api or FastAPI()
        self.manager = manager or WorkManager(work_callback=worker_callback)

        router = APIRouter()
        router.add_api_route(path="/", endpoint=self.root, methods=["GET"])
        router.add_api_route(path="/exit", endpoint=self.exit, methods=["POST"])
        router.add_api_route(path="/kill_service", endpoint=self.kill_service, methods=["POST"])
        router.add_api_route(path="/stop_all", endpoint=self.stop_all_worker, methods=["POST"])
        router.add_api_route(path="/start_worker", endpoint=self.start_worker, methods=["POST"])
        router.add_api_route(path="/stop_worker/{uid}", endpoint=self.stop_worker, methods=["POST"])
        self.api.include_router(router=router)

    def run(self, start_worker: bool = True):
        if start_worker:
            self.manager.start_worker()
        uvicorn.run(self.api, host="127.0.0.1", port=8087, log_level="info")

    def exit(self, force: bool = False, wait: bool = True):
        self.stop_all_worker(force=force, wait=wait)
        self.kill_service()

    def stop_all_worker(self, force: bool = False, wait: bool = True):
        if force:
            self.manager.kill_all(wait=wait)
        else:
            self.manager.stop_all(wait=wait)

    @staticmethod
    def kill_service():
        force_kill_process(os.getpid())

    def start_worker(self):
        self.manager.start_worker()
        return {"message": "worker started"}

    def stop_worker(self, uid: str):
        result = self.manager.stop_by_uid(uid=uid)
        if result is None:
            raise HTTPException(
                status_code=404,
                detail="Worker not found",
                headers={"X-Error": f"Worker {uid=} is not exist."},
            )
        return {"message": "worker stopped", "uid": result}

    def root(self):
        return {
            "name": self.manager.name,
            "status": self.manager.get_status(),
            "paths": [route.path for route in self.api.routes if isinstance(route, Route)]
        }
