class MFTMemoryManager:
    def __init__(self, partition_size, total_partitions):
        self.partitions = [{"size": partition_size, "allocated": False} for _ in range(total_partitions)]
    def allocate(self, process_size):
        if process_size > self.partitions[0]["size"]:
            print(f"Process {process_size} KB too large, rejected.")
            return
        for i, part in enumerate(self.partitions):
            if not part["allocated"]:
                part["allocated"] = True
                print(f"Process {process_size} KB -> Partition {i+1} ({part['size']} KB)")
                return
        print(f"Process {process_size} KB could not be allocated, all partitions full.")
    def release(self, index):
        if 0 <= index < len(self.partitions):
            self.partitions[index]["allocated"] = False
            print(f"Partition {index+1} ({self.partitions[index]['size']} KB) now free.")

memory_manager = MFTMemoryManager(partition_size=800, total_partitions=8)
for process in [300, 700, 900, 150, 800, 750]:
    memory_manager.allocate(process)
memory_manager.release(1)  
