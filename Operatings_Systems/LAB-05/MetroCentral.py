class MemoryBlock:
    def __init__(self, start, size):
        self.start = start
        self.size = size
        self.allocated = False
        self.process_name = None
    def allocate(self, process_name):
        self.allocated = True
        self.process_name = process_name
    def __str__(self):
        status = "Free" if not self.allocated else f"Allocated to {self.process_name}"
        return f"[Start: {self.start}, Size: {self.size}, Status: {status}]"

class MemoryManager:
    def __init__(self, total_memory):
        self.memory_blocks = [MemoryBlock(0, total_memory)]
    def allocate_memory(self, process_name, size):
        for block in self.memory_blocks:
            if not block.allocated and block.size >= size:
                block.allocate(process_name)
                if block.size > size:
                    self.memory_blocks.insert(self.memory_blocks.index(block) + 1, MemoryBlock(block.start + size, block.size - size))
                    block.size = size
                print(f"{process_name} allocated {size} units.")
                return True
        print(f"Not enough memory for {process_name}.")
        return False
    def print_memory_status(self):
        print("Memory Status:")
        for block in self.memory_blocks:
            print(block)
    def print_total_memory_used(self):
        total_used = sum(block.size for block in self.memory_blocks if block.allocated)
        print(f"Total Memory Used: {total_used} units")

memory_manager = MemoryManager(5000)
requests = [
    ("TrafficControl", 1200),
    ("RoutePlanning", 800)
]

for process_name, size in requests:
    memory_manager.allocate_memory(process_name, size)
    memory_manager.print_memory_status()
memory_manager.print_total_memory_used()
