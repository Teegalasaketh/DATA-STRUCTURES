class PatientRecord:
    def __init__(self, name, age, medical_id, address):
        self.name = name
        self.age = age
        self.medical_id = medical_id
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Medical ID: {self.medical_id}, Address: {self.address}"

class SequentialFileAllocation:
    def __init__(self, block_size):
        self.disk_blocks = []
        self.index_table = {} 
        self.block_size = block_size
        self.next_free_block = 0  

    def calculate_record_size(self, student_record):
        return 1

    def add_record(self, patient_record):
        record_size = self.calculate_record_size(patient_record)
        start_block = self.next_free_block
        self.index_table[patient_record.medical_id] = (start_block, record_size)
        self.next_free_block += record_size
        self.disk_blocks.extend([patient_record] * record_size)

    def get_record(self, medical_id):
        if medical_id in self.index_table:
            start_block, record_size = self.index_table[medical_id]
            return self.disk_blocks[start_block]
        return None

    def delete_record(self, medical_id):
        if medical_id in self.index_table:
            start_block, record_size = self.index_table.pop(medical_id)
            for i in range(start_block, start_block + record_size):
                self.disk_blocks[i] = None  

    def print_disk_status(self):
        print("\nPatients Data :")
        j = 'A'
        for i, block  in enumerate(self.disk_blocks):
            if block is  None:
                print(f"Patient {j} ==> Free")
            else:
                print(f"Patient {j} ==> {block}")
                j = chr(ord(j) + 1)

        print("\nIndex Table :")
        for student_id, (start_block, record_size) in self.index_table.items():
            print(f"Medical ID: {student_id}, Start Block: {start_block}, Size: {record_size} block(s)")

block_size = 1  
file_system = SequentialFileAllocation(block_size)
patient_records = [
    PatientRecord("John Smith", 45, 1001, "123 Hospital Road."),
    PatientRecord("Jane Doe", 32, 1002, "456 Clinic Avenue."),
    PatientRecord("Michael Johnson", 58, 1003, "789 Medical Plaza.")
]
print("---------------------------Indexed File Allocation----------------------------")
for record in patient_records:
    file_system.add_record(record)
file_system.print_disk_status()

medical_id = 1002
retrieved_record = file_system.get_record(medical_id)
if retrieved_record:
    print(f"\nRetrieved Record for ID {medical_id}:")
    print(retrieved_record)
else:
    print(f"\nRecord with ID {medical_id} not found.")