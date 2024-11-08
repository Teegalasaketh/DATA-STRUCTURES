class StudentRecord:
    def __init__(self, name, student_id, grade, address):
        self.name = name
        self.student_id = student_id
        self.grade = grade
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, ID: {self.student_id}, Grade: {self.grade}, Address: {self.address}"

class SequentialFileAllocation:
    def __init__(self, block_size):
        self.disk_blocks = []
        self.fat = {} 
        self.block_size = block_size
        self.next_free_block = 0  

    def calculate_record_size(self, student_record):
        return 1

    def add_record(self, student_record):
        record_size = self.calculate_record_size(student_record)
        start_block = self.next_free_block
        self.fat[student_record.student_id] = (start_block, record_size)
        self.next_free_block += record_size
        self.disk_blocks.extend([student_record] * record_size)

    def get_record(self, student_id):
        if student_id in self.fat:
            start_block, record_size = self.fat[student_id]
            return self.disk_blocks[start_block]
        return None

    def delete_record(self, student_id):
        if student_id in self.fat:
            start_block, record_size = self.fat.pop(student_id)
            for i in range(start_block, start_block + record_size):
                self.disk_blocks[i] = None  

    def print_disk_status(self):
        print("\nStudents Data:")
        j = 'A'
        for i, block in enumerate(self.disk_blocks):
            if block is None:
                print(f"Student {j} ==> Free")
            else:
                print(f"Student {j} ==> {block}")
                j = chr(ord(j)+1)

        print("\nFile Allocation Table (FAT):")
        for student_id, (start_block, record_size) in self.fat.items():
            print(f"Student ID: {student_id}, Start Block: {start_block}, Size: {record_size} block(s)")

block_size = 1  
file_system = SequentialFileAllocation(block_size)
student_records = [
    StudentRecord("John Doe", 101, 10, "123 Main Street"),
    StudentRecord("Jane Smith", 102, 11, "456 Elm Street"),
    StudentRecord("Michael Brown", 103, 9, "789 Oak Avenue")
]
print("---------------------------Sequential File Allocation----------------------------")
for record in student_records:
    file_system.add_record(record)
file_system.print_disk_status()

student_id = 102
retrieved_record = file_system.get_record(student_id)
if retrieved_record:
    print(f"\nRetrieved Record for ID {student_id}:")
    print(retrieved_record)
else:
    print(f"\nRecord with ID {student_id} not found.")