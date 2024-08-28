from src.data_service import get_data

def get_data_from_module():
    data = get_data()
    return {
        'data': data
    }
