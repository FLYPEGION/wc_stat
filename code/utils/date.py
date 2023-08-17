import datetime
import re
from datetime import datetime as dt
from chinese_calendar import get_workdays
from utils.log import logger

def generate_dates(start_date:str, end_date:str):
    def _convert_end_date(end_date:str) -> datetime.date:
        if end_date == "今天":
            return datetime.date.today()
        return dt.strptime(end_date,"%Y/%m/%d").date()
    def _convert_start_date(start_date:str) -> datetime.date:
        return dt.strptime(start_date,"%Y/%m/%d").date()
    try:        
        assert _convert_start_date(start_date) < _convert_end_date(end_date), 'start date later than end date'
        return list(reversed(get_workdays(_convert_start_date(start_date),_convert_end_date(end_date),include_weekends=False)))
    except ValueError as e:
        logger.error(f'日期输入错误,返回{e}')
    except Exception as e:
        logger.error(f'获取日期错误,返回{e}')

def convert_querys(date, querys):
    def replace_keywords(query):
        query = re.sub('当天前一天', f"{(date+datetime.timedelta(days=-1)).year}年{(date+datetime.timedelta(days=-1)).month}月{(date+datetime.timedelta(days=-1)).day}日",query, count=0, flags=0)
        return re.sub('当天', f"{date.year}年{date.month}月{date.day}日", query, count=0, flags=0)
    return [replace_keywords(query) for query in querys]   

