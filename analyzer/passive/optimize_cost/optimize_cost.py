import json
import pandas as pd

optimal_memory_found = 0
memory_to_set = 128
analyzed_memories = []
initial_memory = 128

def lambda_handler(event, context):
    global memory_to_set
    memory_to_set = perform_cost_minimization(event["logs"])

    response = {
        "optimal_memory_found": optimal_memory_found,
        "memory_to_set": memory_to_set,
        "analyzed_memories": analyzed_memories,
        "initial_memory": initial_memory
    }

    return {'statusCode': 200, 'body': json.dumps(response)}


def perform_cost_minimization(values: []):
    aws_compute_coef = 0.00001667
    global analyzed_memories, initial_memory, optimal_memory_found, memory_to_set
    df = pd.DataFrame(values)
    df.sort_values(by=['allocated_memory'], inplace=True)

    memory_prev = df.iloc[0]["allocated_memory"]
    initial_memory = memory_prev
    duration_prev = df.iloc[0]["duration"]
    value = [duration_prev, memory_prev, duration_prev * memory_prev * aws_compute_coef / 1024000]
    analyzed_memories.append(value)

    attempts_counter = 0
    max_attempts = 3
    step_increment = 128

    print("------- setting first global_min: ", memory_prev)
    global_min = {
        "duration": duration_prev,
        "memory": memory_prev
    }  # first possible global minimum

    while attempts_counter <= max_attempts:
        memory = memory_prev + step_increment
        if not (memory in df['allocated_memory'].values):
            print("need to set this memory level: " + str(memory))
            optimal_memory_found = 0
            memory_to_set = memory
            return

        duration = df.loc[df['allocated_memory'] == memory, 'duration'].values[0]
        if duration * memory > duration_prev * memory_prev:
            if duration_prev * memory_prev <= global_min["memory"] * global_min["duration"]:
                print("------- Setting new global_min:  ", memory_prev)
                global_min["memory"] = memory_prev
                global_min["duration"] = duration_prev
            else:
                print("------- this minimum is bigger than global one: ", memory)
                attempts_counter += 1

        duration_prev = duration
        memory_prev = memory

        value = [duration_prev, memory_prev, duration_prev * memory_prev * aws_compute_coef / 1024000]
        analyzed_memories.append(value)

    print("------- analyzed_memories:", analyzed_memories)
    print(global_min["memory"])
    optimal_memory_found = 1

    return global_min["memory"]
