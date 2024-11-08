def worst_fit(memory_blocks, requests):
    allocation = {}
    for program, size in requests.items():
        worst_fit_block = max((i for i, block in enumerate(memory_blocks) if block >= size), 
                                key=lambda i: memory_blocks[i], default=-1)
        if worst_fit_block != -1:
            allocation[program] = worst_fit_block
            memory_blocks[worst_fit_block] -= size
    return allocation, memory_blocks

memory_blocks = [400, 250, 350, 200, 150]
requests = {'Program A': 150, 'Program B': 300, 'Program C': 200}
allocation, remaining_memory = worst_fit(memory_blocks, requests)
print("Memory Allocation:", {program: f"Block {block + 1}" for program, block in allocation.items()})
print("Remaining Memory:", remaining_memory)
