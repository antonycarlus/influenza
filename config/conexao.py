
from sqlalchemy import create_engine
import pandas as pd


################ servidor

servidor = 'localhost'; usuario = 'root' ; senha = '12345'; banco = 'ssd_db_srag'; porta = '3306'


def consultar(sql):
    #engine = sqlalchemy.create_engine('mariadb+pymysql://'+usuario+':'+senha+'@'+servidor+'/'+banco+'?charset=utf8mb4')
    engine = create_engine(
        'mariadb+pymysql://' + usuario + ':' + senha + '@' + servidor + '/' + banco + '?charset=utf8mb4')
    #conexao = dados.connect()
    #output = conexao.execute(sql)
    #output = conexao.execute(sql)
    #dadosx = pd.DataFrame(output)
    #return dadosx
    df = pd.read_sql(sql,con=engine)
    return df