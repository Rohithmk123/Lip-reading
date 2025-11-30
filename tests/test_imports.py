# Basic test to check imports and package structure

def test_imports():
    try:
        import numpy
        import pandas
        import sklearn
        import matplotlib
        print("All major libraries imported successfully.")
        return True
    except ImportError as e:
        print(f"Missing library: {e}")
        return False

if __name__ == "__main__":
    assert test_imports(), "Required libraries missing! Check requirements.txt."