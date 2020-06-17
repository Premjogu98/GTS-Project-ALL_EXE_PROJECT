import pymysql.cursors
import sys, os


def Local_connection_links():
    try:
        connection = pymysql.connect(host='192.168.0.202',
                                     user='test',
                                     password='test',
                                     db='test_DB',
                                     charset='utf8',
                                     cursorclass=pymysql.cursors.DictCursor)
        return connection
    except pymysql.connect  as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print("Error ON : ", sys._getframe().f_code.co_name + "--> " + str(e), "\n", exc_type, "\n", fname,
              "\n", exc_tb.tb_lineno)


def Sql_Commands():
    sql_connection = Local_connection_links()  # RETURNED Connection was useful for Connect the database
    # sql_connection is Connection

    SQL_Cursor = sql_connection.cursor()
    # SQL_Cursor useful for execute the sql command

    # Check Duplicate using if statement
    Duplicate_command = "Select ID from test_table where ID = '123'"
    SQL_Cursor.execute(Duplicate_command)
    results = SQL_Cursor.fetchall()  # fetchall means any ID found same as above iD then its store the data on Results
    # if statement check the len of result (Means how many data found as per Above ID)
    # IF ID = 123 Found Then its an duplicate data & its not gonna insert on database so it print Duplicate Data
    if len(results) > 0:
        print('Duplicate Data')
    else:
        # TYPE 1 Insert command
        insert_Command = "INSERT INTO test_table(Address,city)VALUES(%s,%s)"  # insert the data using this command %s means string

        values = (str('Address_OBJECT'), str('city_OBJECT'))
        # SQL insert_Command = INSERT INTO CompanyInfoIndia(Address,city)VALUES('Address','city')

        SQL_Cursor.execute(insert_Command, values)  # This Execute Command marge this both Object LIKE INSERT_COMMAND
        # & VALUES THEN ITS CREATE PROPER COMMAND

        sql_connection.commit()  # this commit Statement asking that you are confirm to execute this command
        # Commit = Confirm
        sql_connection.rollback()  # this rollback Statement asking that you are confirm to Cancel execute this command
        # rollback = Cancel

        Update_Command = "UPDATE test_table SET ID = 'Y' WHERE Company_Name = '" + str('OBJECT') + "'"
        SQL_Cursor.execute(Update_Command)
        sql_connection.commit()


