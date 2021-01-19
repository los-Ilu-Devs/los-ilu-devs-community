import config
import pymysql
import pymysql.cursors

# Connect to the database

def execute_select_query(query):
    connection_bd = pymysql.connect(**config.config)
    cursor = connection_bd.cursor()
    select_member_query = query
    cursor.execute(select_member_query)
    result = cursor.fetchall()
    cursor.close()
    connection_bd.close()
    return result

def get_all_members():
    all_members_query = "SELECT * FROM MEMBER"
    rows = execute_select_query(all_members_query)
    all_members_obj = []
    for row in rows:
        all_members_obj.append(bd_member_to_obj_member(row))
    return all_members_obj
    
def bd_member_to_obj_member(row):
    return {'userId' : row[0], 'fullName' : row[1], 'imgProfile' : row[2]}

