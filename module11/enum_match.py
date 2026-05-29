from enum import Enum, auto


class OrderStatus(Enum):
    PENDING    = auto()
    PROCESSING = auto()
    SHIPPED    = auto()
    DELIVERED  = auto()
    CANCELLED  = auto()


class UserRole(Enum):
    GUEST  = auto()
    MEMBER = auto()
    ADMIN  = auto()


def describe_status(status):
    match status:
        case OrderStatus.PENDING:
            return "Waiting for payment confirmation"
        case OrderStatus.PROCESSING:
            return "Order is being prepared"
        case OrderStatus.SHIPPED:
            return "Order is on the way"
        case OrderStatus.DELIVERED:
            return "Order delivered successfully"
        case OrderStatus.CANCELLED:
            return "Order has been cancelled"


def access_level(role):
    match role:
        case UserRole.ADMIN:
            return ["read", "write", "delete", "manage_users"]
        case UserRole.MEMBER:
            return ["read", "write"]
        case UserRole.GUEST:
            return ["read"]


# iterating over enum members
print("=== Order statuses ===")
for status in OrderStatus:
    print(f"  {status.name:<12} → {describe_status(status)}")

print("\n=== Access levels ===")
for role in UserRole:
    print(f"  {role.name:<8} → {access_level(role)}")

# comparison
current = OrderStatus.SHIPPED
print(f"\nIs delivered: {current == OrderStatus.DELIVERED}")   # False
print(f"Is shipped:   {current == OrderStatus.SHIPPED}")      # True
