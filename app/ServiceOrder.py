from ServiceOrderStatus import ServiceOrderStatus

class ServiceOrder:
    def __init__(self, status: ServiceOrderStatus) -> None:
        self.status = status
