class MemoryManager:
    def __init__(self, partitions):
        self.partitions = [{"size": size, "allocated": False} for size in partitions]

    def allocate(self, process_size):
        for part in self.partitions:
            if not part["allocated"] and part["size"] >= process_size:
                part["allocated"] = True
                print(f"Process {process_size} KB -> Partition {part['size']} KB")
                return
        print(f"Process {process_size} KB could not be allocated.")

    def release(self, index):
        if 0 <= index < len(self.partitions):
            self.partitions[index]["allocated"] = False
            print(f"Partition {self.partitions[index]['size']} KB is now free.")

memory_manager = MemoryManager([300, 500, 200])
for process in [200, 250, 450]:
    memory_manager.allocate(process)

memory_manager.release(0)  
