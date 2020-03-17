import pickle


class PersistenceUtils:

    def __init__(self):
        pass

    @staticmethod
    def write_pickle(file_path, data):
        with open(file_path, 'wb') as file_handler:
            pickle.dump(data, file_handler)

    @staticmethod
    def load_pickle(file_path):
        with open(file_path, 'rb') as file_handler:
            data = pickle.load(file_handler)
        return data
