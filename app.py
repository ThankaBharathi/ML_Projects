from src.exception import CustomException
import sys

def divide_numbers(a, b):
    try:
        return a / b
    except Exception as e:
        raise CustomException(e, sys)

# Your script logic
if __name__ == "__main__":
    try:
        # Test the exception handling by dividing by zero
        result = divide_numbers(10, 0)
        print(f"Result: {result}")
    except CustomException as ce:
        print(f"Handled exception: {str(ce)}")
