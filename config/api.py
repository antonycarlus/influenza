#### api do sistema influenza


from flask import Flask, make_response,jsonify, Response,  redirect, url_for, render_template, request, session, flash
from flask_caching import Cache
from conexao import *
import json


config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}
api = Flask(__name__)
api.config.from_mapping(config)
cache = Cache(api)



############## fazenda de SQL

tb_srag = """
select 
cs_sexo as sexo,
cod_idade as idade,
cs_raca as raca,
co_mun_res as ibge_res,
co_mun_not as ibge_not,
classi_fin as class,
criterio as criterio,
evolucao as evolucao,
uti as uti from tb_srag ts where ts.SG_UF = "MA" and ts.SG_UF_NOT = "MA"
"""

tb_local = """
select 
mun_ibge6 as igbe,
mun_ibge7 as igbe7,
mun_municipio as municipio,
mun_codreg as codreg,
mun_regional as regional,
mun_codmac as codmac,
mun_macroreg as macro,
mun_uf as uf,
mun_longitude as longitude,
mun_latitude as latitude
from tb_municipios tm
"""




########### --- TABELA SRAG  ################
@api.route("/srag", methods=['GET'])
# @cache.cached()
#@lru_cache
def srag():
    df_db = consultar(tb_srag)
    json_str = df_db.to_json(orient='records')
    json_obj = json.loads(json_str)
    print(json_obj)
    return (
        make_response(
            jsonify(
                json_obj

            )))

@api.route("/local", methods=['GET'])
# @cache.cached()
#@lru_cache
def local():
    df_db = consultar(tb_local)
    json_str = df_db.to_json(orient='records')
    json_obj = json.loads(json_str)
    print(json_obj)
    return (
        make_response(
            jsonify(
                json_obj

            )))

if __name__ == "__main__":
    #api.run(debug=True, threaded=False, port = 5000)
    api.run(debug=False)
