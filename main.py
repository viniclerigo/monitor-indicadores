from ipca_etl import run_ipca_etl
from desemprego_etl import run_desemprego_etl
from pib_etl import run_pib_etl
from salario_medio_real_etl import run_salario_medio_real_etl
from selic_etl import run_selic_etl
from cambio_dolar_etl import run_cambio_dolar_etl

run_ipca_etl()
run_desemprego_etl()
run_pib_etl()
run_salario_medio_real_etl()
run_selic_etl()
run_cambio_dolar_etl()