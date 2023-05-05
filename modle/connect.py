class Connection:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def __str__(self):
        return f"Connection to {self.host}:{self.port}"

    def __enter__(self):
        print("Entering")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting")
        if exc_type is None:
            print("No exception")
        else:
            print(f"Exception: {exc_type}")