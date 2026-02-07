import logging

# Настройка логирования
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)
logger = logging.getLogger(__name__)

def add(a, b):
    logger.debug(f"Adding {a} + {b}")
    return a + b

def multiply(a, b):
    logger.debug(f"Multiplying {a} * {b}")
    return a * b

def divide(a, b):
    if b == 0:
        logger.error("Division by zero attempt: %s / %s", a, b)
        return None
    logger.debug(f"Dividing {a} / {b}")
    return a / b

# Тестирование функций
if __name__ == "__main__":
    print(add(3, 5))
    print(multiply(4, 7))
    print(divide(10, 0))
    print(divide(10, 2))
