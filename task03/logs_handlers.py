def parse_log_line(line: str) -> dict: 
    date, time, level, *message = line.split()
    return {
        "date": date,
        "time": time,
        "log_level": level,
        "log_message": " ". join(message)
    }


def load_logs(file_path: str) -> list: 
    with open(file_path, "r") as file:
        logs_list = [] 
        for log in file: 
            parsed_log = parse_log_line(log)
            logs_list.append(parsed_log)
        return logs_list


def filter_logs_by_level(logs: list, level: str) -> list: 
    filtred = list(filter(lambda log: log["log_level"] == level, logs ))
    return filtred



def count_logs_by_level(logs: list) -> dict:
    logs_level_counter ={ 
    }

    for log in logs: 
        if log["log_level"] in logs_level_counter: 
            logs_level_counter[log["log_level"]] += 1
        else: 
            logs_level_counter[log["log_level"]] = 1
    return logs_level_counter



def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    disp_massage = ""
    for level, count in counts.items():
        disp_massage += f"{level:<16} | {count}\n"
    print(disp_massage)
    
 