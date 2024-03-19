"""Strangeworks SDK."""

import importlib.metadata

from .core.config import config
from .sw_client import SWClient

__version__ = importlib.metadata.version("strangeworks")

cfg = config.Config()
client = SWClient(cfg=cfg)  # instantiate a client on import by default

# strangeworks.(public method) shortcuts.
authenticate = client.authenticate
workspace_info = client.workspace_info
resources = client.resources
execute = client.execute
jobs = client.jobs
upload_file = client.upload_file
download_job_files = client.download_job_files
backends = client.get_backends
set_resource_for_product = client.set_resource_for_product
get_resource_for_product = client.get_resource_for_product
execute_post = client.execute_post
execute_get = client.execute_get
experiment = client.experiment
experiment_download = client.experiment_download
experiment_upload = client.experiment_upload
experiment_get_result = client.experiment_get_result
