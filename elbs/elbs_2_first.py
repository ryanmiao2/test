
"""
Generated by airflow console
fileName:  elbs/elbs_2_first.py
date    :  2019-09-21 10:19:47
"""


from airflow import DAG
from datetime import datetime

default_args = {
    'owner': 'sdfsdf',
    'depends_on_past': False,
    'start_date': datetime(2019,9,18),
}

dag = DAG(
    'elbs_2_first',
    description='sdffsdfs',
    default_args=default_args,
    schedule_interval="0 * * * *")


from airflow.operators.bash_operator import BashOperator






aa = BashOperator(
    task_id='aa',
    bash_command='date',
    dag=dag)






bb = BashOperator(
    task_id='bb',
    bash_command='echo \'Hello Ryan\'',
    dag=dag)


aa << bb