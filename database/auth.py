class Database:
    host = "127.0.0.1"
    port = "27017"
    database = "COCONUT"
    user_id = "swlee"
    user_password = "camd5882"
    connection_info = "mongodb://{}:{}@{}:{}/{}".format(
        user_id, user_password, host, port, database
    )