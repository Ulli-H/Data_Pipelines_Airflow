from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadDimensionOperator(BaseOperator):

    ui_color = '#80BD9E'

    @apply_defaults
    def __init__(self,
                 redshift_conn_id = "",
                 destination_table="",
                 sql_query="",
                 truncate=False
                 *args, **kwargs):

        super(LoadDimensionOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id=redshift_conn_id
        self.destination_table=destination_table
        self.sql_query=sql_query
        self.truncate=truncate

    def execute(self, context):
        self.log.info('Loading dimension tables')

        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        if self.truncate:
            redshift.run(f"TRUNCATE TABLE {self.destination_table}")
        redshift.run(f"INSERT INTO {self.destination_table} {self.sql_query}")
        