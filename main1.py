from stack_queue import Queue

class Patient:
    def __init__(self, p_id: int, name: str, disease_desc: str, severity: int):
        self.p_id = p_id
        self.name = name
        self.d_desc = disease_desc
        self.severity = severity

    def update_priority(self, new_prio):
        self.severity = new_prio

    def __repr__(self):
        return f"Pat ID: {self.p_id}, Pat name: {self.name}, Disease desc: {self.d_desc}, Severity: {self.severity}"

class Doctor:
    def __init__(self, d_id: int, name: str):
        self.d_id = d_id
        self.name = name
        self.patients_queue = Queue()

    def add_patient(self, patient):
        pass

    def __repr__(self):
        return f"Doc ID: {self.d_id}, Doc name: {self.name}, Pat queue: {self.patients_queue}"

class Hospital:
    def __init__(self, name: str):
        self.name = name
        self.doc_list = []
        self.pat_list = []

    def __repr__(self):
        return f"Hospital name: {self.name}, Doc list: {self.doc_list}, Pat list: {self.pat_list}"