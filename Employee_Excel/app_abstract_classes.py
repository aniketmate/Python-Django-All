from abc import ABC, abstractmethod

class EmployeeAbstraction(ABC):

    @abstractmethod
    def write_headers(self):
        pass

    @abstractmethod
    def read_data_from_excel(self):
        pass


    @abstractmethod    
    def write_data_to_excel(self):
        pass