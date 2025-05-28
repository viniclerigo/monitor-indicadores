from funcs.ipca_etl import run_ipca_etl
from funcs.desemprego_etl import run_desemprego_etl
from funcs.pib_etl import run_pib_etl
from funcs.salario_medio_real_etl import run_salario_medio_real_etl
from funcs.selic_etl import run_selic_etl
from funcs.cambio_dolar_etl import run_cambio_dolar_etl

run_ipca_etl()
run_desemprego_etl()
run_pib_etl()
run_salario_medio_real_etl()
run_selic_etl()
run_cambio_dolar_etl()