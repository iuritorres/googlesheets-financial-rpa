from enum import Enum

class ServiceOrderStatus(Enum):
    DELIVERED = 'ENTREGUE'
    PENDING = 'PENDENTE'
    LATE = 'ATRASADA'
