from typing import Optional

import typer

from service_sdk.client import Client

cli = typer.Typer()


@cli.command()
def ping(host: str = "http://127.0.0.1", port: str = "8080"):
    client = Client(host=host, port=port)
    result = client.ping()
    print(result)


@cli.command()
def exit_service(
        host: str = "http://127.0.0.1", port: str = "8080", force: Optional[bool] = None, wait: Optional[bool] = None
):
    client = Client(host=host, port=port)
    result = client.exit(force=force, wait=wait)
    print(result)


@cli.command()
def start(host: str = "http://127.0.0.1", port: str = "8080"):
    client = Client(host=host, port=port)
    result = client.start_worker()
    print(result)


@cli.command()
def start(host: str = "http://127.0.0.1", port: str = "8080"):
    client = Client(host=host, port=port)
    result = client.start_worker()
    print(result)


@cli.command()
def stop(uid: str, host: str = "http://127.0.0.1", port: str = "8080"):
    client = Client(host=host, port=port)
    result = client.stop_worker(uid=uid)
    print(result)


if __name__ == "__main__":
    cli()
