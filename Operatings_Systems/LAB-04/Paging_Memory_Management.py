class PagingMemoryManager:
    def __init__(self, total_pages, page_size):
        self.page_size = page_size
        self.total_pages = total_pages
        self.pages = [False] * total_pages  
    def allocate(self, process_size):
        required_pages = (process_size + self.page_size - 1) // self.page_size 
        free_pages = [i for i, allocated in enumerate(self.pages) if not allocated]
        if len(free_pages) < required_pages:
            print(f"Process {process_size} KB could not be allocated. Not enough free pages.")
            return
        allocated_pages = free_pages[:required_pages]
        for i in allocated_pages:
            self.pages[i] = True
        print(f"Process {process_size} KB allocated pages: {allocated_pages}")
    def release(self, page_indices):
        for i in page_indices:
            if 0 <= i < self.total_pages:
                self.pages[i] = False
        print(f"Pages {page_indices} are now free.")

memory_manager = PagingMemoryManager(total_pages=20, page_size=200)
process_requests = [300, 450, 1000, 150, 600, 200]

for process in process_requests:
    memory_manager.allocate(process)
memory_manager.release([0, 1, 2])
