class MemoryBlock:
    def __init__(self, start, size):
        self.start = start
        self.size = size
        self.allocated = False
        self.process_name = None
    def is_free(self):
        return not self.allocated
    def allocate(self, process_name):
        self.allocated = True
        self.process_name = process_name
    def deallocate(self):
        self.allocated = False
        self.process_name = None
    def __str__(self):
        status = "Free" if not self.allocated else f"Allocated to {self.process_name}"
        return f"[Start: {self.start}, Size: {self.size}, Status: {status}]"

class MemoryManager:
    def __init__(self, total_memory):
        self.memory_blocks = [MemoryBlock(0, total_memory)]
    def allocate_memory(self, process_name, size):
        best_fit_index = min(
            (i for i, block in enumerate(self.memory_blocks) if block.is_free() and block.size >= size),
            key=lambda i: self.memory_blocks[i].size, default=-1
        )
        if best_fit_index != -1:
            block = self.memory_blocks[best_fit_index]
            block.allocate(process_name)
            if block.size > size:
                self.memory_blocks.insert(best_fit_index + 1, MemoryBlock(block.start + size, block.size - size))
                block.size = size
            return True
        return False
    def print_memory_status(self):
        print("Memory Status:")
        for block in self.memory_blocks:
            print(block)
    def print_total_memory_used(self):
        total_used = sum(block.size for block in self.memory_blocks if block.allocated)
        print(f"Total Memory Used: {total_used} units")


memory_manager = MemoryManager(8000)
requests = [("SubsysA", 1500), ("SubsysB", 1000), ("SubsysC", 700), ("SubsysD", 2200), ("SubsysE", 500), ("SubsysF", 1200)]

for process_name, size in requests:
    if memory_manager.allocate_memory(process_name, size):
        print(f"{process_name} allocated {size} units.")
    else:
        print(f"Not enough memory for {process_name}.")
    memory_manager.print_memory_status()
memory_manager.print_total_memory_used()
