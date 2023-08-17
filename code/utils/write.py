
import os
import openpyxl # 没用pandas的to_excel是因为每个日期下的股票数目不一致
from utils.log import logger

def write_excel(file_name: str, content: list, headers: list = None) -> None:
    def write_list(list:list,skiprows:int=0):
        for row in range(len(list)):
            for col, val in enumerate(list[row]):
                wb.active.cell(skiprows + row + 1, col + 1).value = val # excel中的行和列是从1开始计数的，所以需要+1
        return len(list)
    if not os.path.exists(os.path.join(__file__, os.pardir, os.pardir, "file" ,f"{file_name}.xlsx")):
        wb = openpyxl.Workbook()
        wb.active.title = '内容'
        header_lens = write_list(headers)
        write_list(content, skiprows=header_lens)
        wb.save(os.path.join(__file__, os.pardir, os.pardir, "file" ,f"{file_name}.xlsx"))
        logger.info('成功写入文件: ' + file_name)
    else:
        logger.error('同名文件已存在')