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
        queue_lst = []
        while not self.patients_queue.is_empty():
            queue_lst.append(self.patients_queue.dequeue())
        flag = False
        for i in range(len(queue_lst)):
            if patient.severity > queue_lst[i].severity:
                queue_lst.insert(i, patient)
                flag = True
                break
        if not flag:
            queue_lst.append(patient)
        for patient in queue_lst:
            self.patients_queue.enqueue(patient)

    def treat_patient(self):
        if self.patients_queue.is_empty():
            return None
        return self.patients_queue.dequeue()


    def __repr__(self):
        return f"Doc ID: {self.d_id}, Doc name: {self.name}, Pat queue: {self.patients_queue}"

class Hospital:
    def __init__(self, name: str):
        self.name = name
        self.doc_list = []
        self.pat_list = []

    def add_doctor(self, doc):
        if doc not in self.doc_list:
            self.doc_list.append(doc)

    def add_patient(self, patient):
        if patient not in self.pat_list:
            self.pat_list.append(patient)

    def assign_patient_to_doctor(self, p_id, d_id):
        for patient in self.pat_list:
            if patient.p_id == p_id:
                for doctor in self.doc_list:
                    if doctor.d_id == d_id:
                        doctor.patients_queue.enqueue(patient)

    def treat_next_patient(self, d_id):
        for doctor in self.doc_list:
            if doctor.d_id == d_id:
                return doctor.patients_queue.dequeue()
        return None

    def patient_statistics(self):
        dct = {}
        for patient in self.pat_list:
            if patient.severity not in dct:
                dct[patient.severity] = []
            dct[patient.severity].append(patient.name)
        return dct

    def patient_by_priority(self, priority):
        dct = self.patient_statistics()
        if priority not in dct:
            return []
        return dct[priority]

    def all_doctors(self):
        sorted_docs = self.quick_sort(self.doc_list)
        return [doc.name for doc in sorted_docs]

    def quick_sort(self, lst):
        if len(lst) <= 1:
            return lst
        pivot = lst[0]
        small = [doc for doc in lst[1:] if doc.patients_queue.size() <= pivot.patients_queue.size()]
        greater = [doc for doc in lst[1:] if doc.patients_queue.size() > pivot.patients_queue.size()]
        return self.quick_sort(greater) + [pivot] + self.quick_sort(small)

    def __repr__(self):
        return f"Hospital name: {self.name}, Doc list: {self.doc_list}, Pat list: {self.pat_list}"

pat1 = Patient(1, 'Ariel', 'Flu', 2)
pat2 = Patient(2, 'Moshe', 'Broken Leg', 4)
pat3 = Patient(3, 'Ron', 'Gunshot', 5)
pat4 = Patient(4, 'Dudu', 'Headache', 1)
pat5 = Patient(5, 'Sarah', 'Stomach Ache', 3)
doc1 = Doctor(789, 'John')
doc2 = Doctor(543, 'Larry')
hospital = Hospital('Soroka')
# doc1.add_patient(pat1)
# doc1.add_patient(pat2)
# doc1.add_patient(pat3)
doc1.treat_patient()
hospital.add_doctor(doc1)
hospital.add_doctor(doc2)
hospital.add_patient(pat1)
hospital.add_patient(pat2)
hospital.add_patient(pat3)
hospital.add_patient(pat4)
hospital.add_patient(pat5)
hospital.assign_patient_to_doctor(2, 543)
hospital.assign_patient_to_doctor(1, 789)
hospital.assign_patient_to_doctor(3, 543)
hospital.assign_patient_to_doctor(4, 543)
hospital.assign_patient_to_doctor(5, 789)
hospital.patient_statistics()
print(hospital.pat_list)
print(hospital.patient_by_priority(4))
print(hospital.all_doctors())

queue = doc2.patients_queue
while not queue.is_empty():
    print(queue.dequeue())













