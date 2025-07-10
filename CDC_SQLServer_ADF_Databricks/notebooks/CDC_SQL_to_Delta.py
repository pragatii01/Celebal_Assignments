# Databricks notebook source
# STEP 1: JDBC connection details
jdbcHostname = "10.11.134.184"  # ✅ Your actual IP
jdbcPort = 1433
jdbcDatabase = "MyCDCDatabase"
jdbcUsername = "cdcuser"
jdbcPassword = "Cdc@12345"

# JDBC URL
jdbcUrl = f"jdbc:sqlserver://{jdbcHostname}:{jdbcPort};databaseName={jdbcDatabase};encrypt=false;trustServerCertificate=true"

connectionProperties = {
  "user": jdbcUsername,
  "password": jdbcPassword,
  "driver": "com.microsoft.sqlserver.jdbc.SQLServerDriver"
}


# COMMAND ----------

# ✅ Use ngrok tunnel to reach local SQL Server
jdbcHostname = "0.tcp.in.ngrok.io"
jdbcPort = 15962
jdbcDatabase = "MyCDCDatabase"
jdbcUsername = "cdcuser"
jdbcPassword = "Cdc@12345"

jdbcUrl = f"jdbc:sqlserver://{jdbcHostname}:{jdbcPort};databaseName={jdbcDatabase};encrypt=false;trustServerCertificate=true"

connectionProperties = {
  "user": jdbcUsername,
  "password": jdbcPassword,
  "driver": "com.microsoft.sqlserver.jdbc.SQLServerDriver"
}


# COMMAND ----------

df_customer = spark.read.jdbc(
    url=jdbcUrl,
    table="Customer",
    properties=connectionProperties
)

df_customer.show()


# COMMAND ----------

# STEP 3: Write to Delta table
df_customer.write.format("delta").mode("overwrite").save("/tmp/customer_cdc_delta")


# COMMAND ----------

# STEP 4: Read back from Delta
df_delta = spark.read.format("delta").load("/tmp/customer_cdc_delta")
df_delta.show()
