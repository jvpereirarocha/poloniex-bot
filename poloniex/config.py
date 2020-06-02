import pymysql.cursors


"""

Configurações essenciais para o funcionamento da aplicação

"""


def get_url_api():
    return "https://poloniex.com/public?command=returnTicker"


def get_db_config():
    connection = pymysql.connect(host='db', user='jv',
                                 password='sci@2017', db='poloniex')
    return connection
