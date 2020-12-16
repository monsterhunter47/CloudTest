import psycopg2
try:
    connection = psycopg2.connect(user="webadmin",
                                  password="YIRtlh68318",
                                  #host="10.101.1.34",
                                  host="node7515-nonetheless.app.ruk-com.cloud:11066",
                                  port="5432",
                                  database="CloudDB")

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print(connection.get_dsn_parameters(), "\n")

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    # closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")