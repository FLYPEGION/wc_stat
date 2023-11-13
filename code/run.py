from time import time
from tqdm import tqdm
from utils import log 
from utils.log import logger
from utils.load import load_config
from utils.date import generate_dates, convert_querys
from utils.query import Wencai, get_proxy
from utils.write import write_excel

if __name__ == '__main__':
    configs = load_config('config.yaml')
    cnt_ip = 0
    start_time = time()
    duration = 0
    rows = []
    logger.info('程序启动')
    try:
        for date in tqdm(generate_dates(configs["start_date"],configs["end_date"])):
            duration = time() - start_time
            if duration >= cnt_ip * configs['ip_internal']:
                cnt_ip += 1
                proxy = get_proxy(configs['proxy_url'])
            querys = convert_querys(date,configs["querys"])
            stocks = Wencai().query(querys,configs["limits"],configs["cookie"],proxy)
            rows.append([f"{date.year}年{date.month}月{date.day}日", len(stocks)]+stocks)
        write_excel(configs["file_name"], content = rows, headers = [['日期','共计','分别是']])
    except BaseException as e:
        logger.error('程序发生未知异常{e}'.format(e=e))
    finally:
        logger.info('程序完成')
    