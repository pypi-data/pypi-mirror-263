import os
import sys
import json
import time
import logging
import sys
import io
import shutil
from datetime import datetime
import subprocess
from dnbc4tools.__init__ import __root_dir__

def str_mkdir(arg):
    if not os.path.exists(arg):
        os.system('mkdir -p %s'%arg)

def change_path():
    os.environ['PATH'] += ':'+'/'.join(str(__root_dir__).split('/')[0:-4])+ '/bin'
    os.environ['LD_LIBRARY_PATH'] = '/'.join(str(__root_dir__).split('/')[0:-4]) + '/lib'

def bin_path():
    bin_command = '/'.join(str(__root_dir__).split('/')[0:-4])+ '/bin'
    return bin_command
    
def rm_temp(*args):
    for filename in args:
        if os.path.exists(filename):
            if os.path.isdir(filename):
                shutil.rmtree(filename)
            else:
                os.remove(filename)
        else:
            pass

def start_print_cmd(arg, log_dir):
    today = time.strftime('%Y%m%d', time.localtime(time.time()))
    logfile = f'{log_dir}/log/{today}.txt'
    logging.basicConfig(filename=logfile,level=logging.INFO, format='%(message)s')
    logger = logging.getLogger()
    logger.info(arg)
    subprocess.check_call(arg, shell=True)

def get_formatted_time():
    current_time = datetime.now()
    formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')
    return formatted_time

def setup_logging(name, log_dir):
    today = time.strftime('%Y%m%d', time.localtime(time.time()))
    logfile = f'{log_dir}/log/{today}.txt'
    logger = logging.getLogger(name)
    
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s \n%(message)s')
        
        file_handler = logging.FileHandler(logfile, encoding="utf8")
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.ERROR)
        console_handler.setFormatter(formatter)
        
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
    
    return logger

def logging_call(popenargs, name, log_dir):
    logger = setup_logging(name, log_dir)
    #logger.info('Executing command: %s', ''.join(popenargs))

    try:
        output = subprocess.check_output(popenargs, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        logger.info('%s', output)
    except subprocess.CalledProcessError as e:
        logger.error('Command failed with exit code %d', e.returncode)
        logger.error('%s', e.output)

def logfunc(func):
    from functools import wraps
    default_outdir = '.'
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger = logging.getLogger(func.__name__)
        logger.setLevel(logging.INFO)
        outdir = kwargs.pop('logdir', default_outdir)
        today = time.strftime('%Y%m%d', time.localtime(time.time()))
        full_logfile = f'{outdir}/{today}.txt'
        
        file_handler = logging.FileHandler(full_logfile, mode='a', encoding='utf-8')
        file_handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        if not logger.handlers:
            logger.addHandler(file_handler)
        stdout_buffer = io.StringIO()
        original_stdout = sys.stdout
        sys.stdout = stdout_buffer
        result = func(*args, **kwargs)
        sys.stdout = original_stdout
        stdout_buffer.seek(0)
        logger.info(stdout_buffer.read())
        return result
    return wrapper
    

def judgeFilexits(*args):
    for input_files in args:
        for input_file in input_files.split(','):
            if not os.path.exists(input_file): 
                print(" ------------------------------------------------") 
                print("Error: Cannot find input file or dir %s"%(str(input_file))) 
                print(" ------------------------------------------------") 
                sys.exit()
            else:
                pass

def hamming_distance(chain1, chain2):
    return len(list(filter(lambda x : ord(x[0])^ord(x[1]), zip(chain1, chain2))))


def read_json(file):
    with open(file,'r',encoding='utf8')as fp:
        json_data = json.load(fp)
    return json_data

def seq_comp(seq):
    nt_comp = {'A':'0', 'C':'1', 'G':'2', 'T':'3'}
    length = len(seq)-1
    sum = 0
    for k,v in enumerate(seq.upper()):
        sum += int(nt_comp[v])*(4**(length-k))
    return str('%010x'%sum).upper()

def png_to_base64(file,base64_path):
    import base64
    if os.path.isfile(file):
        with open(file, "rb") as f:
            base64_data = base64.b64encode(f.read())
            s = base64_data.decode()
            base64_path_f = open(base64_path, 'w')
            base64_path_f.write('<img src=data:image/'+'png'+';base64,'+s+">")
            base64_path_f.close()

def csv_datatable(file,outfile):
    import pandas as pd
    if os.path.exists(file):
        df= pd.read_csv(open(file),encoding="utf-8",dtype=str,)
        fw = open(outfile,'w')
        for index, row in df.iterrows():
            fw.write('<tr><td>'+row['gene']+'</td>'\
                +'<td>'+row['cluster']+'</td>'\
                +'<td>'+row['p_val_adj']+'</td>'\
                +'<td>'+row['p_val']+'</td>'\
                +'<td>'+row['avg_log2FC']+'</td>'\
                +'<td>'+row['pct.1']+'</td>'\
                +'<td>'+row['pct.2']+'</td>'\
            )
        fw.close()

# atac fragments gz and index
def bgzip_index(fragments, threads):
    bgzip_cmd = [f'{bin_path()}/bgzip', "--force", "--threads", threads, fragments]
    subprocess.run(bgzip_cmd, check=True)
    tabix_cmd = [f'{bin_path()}/tabix','--force' ,'-p', 'bed', f'{fragments}.gz']
    subprocess.run(tabix_cmd, check=True)