class MemoryManager:
    def __init__(self, blocks):
        self.blocks = [{"size": size, "allocated": False} for size in blocks]
    def allocate_best_fit(self, process_size):
        best_fit = min(
            (block for block in self.blocks if not block["allocated"] and block["size"] >= process_size),
            key=lambda x: x["size"] - process_size, default=None
        )
        if best_fit:
            best_fit["allocated"] = True
            print(f"Process {process_size} KB -> Block {best_fit['size']} KB (Remaining: {best_fit['size'] - process_size} KB)")
        else:
            print(f"Process {process_size} KB could not be allocated.")
    def release(self, index):
        if 0 <= index < len(self.blocks):
            self.blocks[index]["allocated"] = False
            print(f"Block {self.blocks[index]['size']} KB is now free.")

memory_manager = MemoryManager([100, 200, 50, 150, 300, 80, 120, 200])
for process in [70, 155, 95, 120, 300, 10]:
    memory_manager.allocate_best_fit(process)
memory_manager.release(0)
