import sys
from pathlib import Path
from logs_handlers import *



def main(): 
        try:
            path = Path(sys.argv[1])
        except IndexError as e: 
            print(f"Use the path")
            exit()

        try:
            logs_list = load_logs(path)
        except FileNotFoundError: 
            print("File does not exist")
            exit()
        logs_count = count_logs_by_level(logs_list)
        logs_disp = display_log_counts(logs_count)
        
        if len(sys.argv) == 2: 
            print(logs_disp)

        elif len(sys.argv) == 3: 
            filtred_logs_list = filter_logs_by_level(logs_list, sys.argv[2].upper()) 
            message = f"{logs_disp} \nДеталі для логів рівня {sys.argv[2].upper()} \n"

            for log in filtred_logs_list: 
                 del log["log_level"]
                 message += f"{log["date"]} {log["time"]} - {log["log_message"]} \n"
            
            print(message)
            
        else: 
            print("You need to use only 2 or 3 args") 

 

if __name__ == "__main__":
    main()