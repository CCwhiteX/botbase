# MIT License
# Copyright (c) 2024 CCwhiteX

import subprocess
import sys

def get_system_usage():
    result = subprocess.run(
    ['top', '-b', '-n', '1'],
    stdout=subprocess.PIPE, 
    text=True
    )
    return result.stdout
    
def parse_top_output(output):
    lines = output.splitlines()
    cpu_line = lines[2]
    cpu_usage = cpu_line.split()[1]
    mem_line = lines[3]
    mem_usage = mem_line.split()[2]
    return cpu_usage, mem_usage   
    
def status():
    output = get_system_usage()
    cpu_usage, mem_usage = parse_top_output(output)
    version = sys.version
    from command.plugin import API_PLUGIN
    print(f"""

 Загрузка процессора: {cpu_usage}%
 Использование оперативной памяти: {mem_usage}%
 Версия Python: {version}

    """)
