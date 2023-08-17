import requests as rq
from .log import logger

def get_proxy(proxy_url):
    if proxy_url is not None:
        res = rq.get(proxy_url)
        if res.status_code == 200:
            logger.info('ip返回状态{ip_address}'.format(ip_address=res.text))  
            proxies = {'http': 'http://' + res.text}
            return proxies
        else:
            logger.error('代理连接状态异常 状态码{status_code}'.format(status_code=res.status_code)) 
    else:
        logger.info('未使用代理')
        return None



import pywencai
# import asyncio
from .log import logger
class Wencai:
    def _query(self, query:str, cookie=None,proxies=None):
        try:
            pro = True if cookie is not None else False
            res = pywencai.get(query=query, loop=True, pro=pro, cookie=cookie, request_params={ 'proxies': proxies})
            return res['code'].tolist()
        except AttributeError:
           logger.error(f'问财接口状态异常,查询问句{query}')
           return []
        except KeyError:
            logger.error(f'问财返回结果异常,查询问句{query}')
            return []

    def _poll(self, querys:list,cookie=None,proxies=None):
        stocks = set()
        for query in querys:
            stocks = stocks | set(self._query(query,cookie,proxies))
        return stocks

    def _limit(self, stocks, limits):
        if limits != None:
            stocks = stocks & set(limits)
        return list(stocks)
    
    def get(self, querys:list, limits=None, cookie=None,proxies=None):
        return self._limit(self._poll(querys,cookie,proxies),limits)