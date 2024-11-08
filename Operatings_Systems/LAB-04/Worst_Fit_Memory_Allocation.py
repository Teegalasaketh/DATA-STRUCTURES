class MemoryManager:
    def __init__(self, blocks):
        self.blocks = [{"size": size, "allocated": False} for size in blocks]
    def allocate_worst_fit(self, process_size):
        worst_fit = max(
            (block for block in self.blocks if not block["allocated"] and block["size"] >= process_size),
            key=lambda x: x["size"], default=None
        )
        if worst_fit:
            worst_fit["allocated"] = True
            print(f"Process {process_size} KB -> Block {worst_fit['size']} KB (Remaining: {worst_fit['size'] - process_size} KB)")
        else:
            print(f"Process {process_size} KB could not be allocated.")
    def release(self, index):
        if 0 <= index < len(self.blocks):
            self.blocks[index]["allocated"] = False
            print(f"Block {self.blocks[index]['size']} KB is now free.")

memory_manager = MemoryManager([150, 300, 100, 200, 250, 50, 350, 180, 120, 200])
process_requests = [80, 210, 140, 300, 50, 120]

for process in process_requests:
    memory_manager.allocate_worst_fit(process)
memory_manager.release(2)
