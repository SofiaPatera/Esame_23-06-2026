from database.DB_connect import DBConnect
from model.user import User

class Dao:
    def __init__(self):
        pass

    @staticmethod
    def read_all_users():
        print("Executing read from database using SQL query")

        results = []
        cnx = DBConnect.get_connection()

        if cnx is None:
            print("Connection failed")
            return None

        cursor = cnx.cursor(dictionary=True)

        query = """ SELECT * FROM Users """

        cursor.execute(query)

        for row in cursor:
            user = User(
                row["user_id"],
                row["votes_funny"],
                row["votes_useful"],
                row["votes_cool"],
                row["name"],
                row["average_stars"],
                row["review_count"]
            )

            results.append(user)

        cursor.close()
        cnx.close()

        return results

    @staticmethod
    def get_nodi(n_bus):
        print("Executing read from database using SQL query")

        results = []
        cnx = DBConnect.get_connection()

        if cnx is None:
            print("Connection failed")
            return None

        cursor = cnx.cursor(dictionary=True)

        query = """ SELECT DISTINCT u.user_id
                    FROM users u, reviews r
                    WHERE u.user_id = r.user_id
                    GROUP BY u.user_id
                HAVING COUNT(r.business_id) >= %s"""

        cursor.execute(query,(n_bus,))

        for row in cursor:
            user = (row['user_id'])

            results.append(user)

            results.append(user)

        cursor.close()
        cnx.close()

        return results

    @staticmethod
    def get_archi(n_bus):
        print("Executing read from database using SQL query")

        results = []
        cnx = DBConnect.get_connection()

        if cnx is None:
            print("Connection failed")
            return None

        cursor = cnx.cursor(dictionary=True)

        query = """ select distinct u1.user_id as us1, u2.user_id as us2, count(r1.business_id) as peso
                    from users u1, users u2, reviews r1, reviews r2
                    where u1.user_id = r1.user_id and 
                        u2.user_id = r2.user_id and 
                        r1.business_id = r2.business_id and 
                        u1.user_id < u2.user_id and
                            u1.user_id in (SELECT DISTINCT u.user_id
                                            FROM yelp_reduced.users u, yelp_reduced.reviews r
                                            WHERE u.user_id = r.user_id
                                            GROUP BY u.user_id
                                            HAVING COUNT(r.business_id) >= %s ) and 
                            u2.user_id in (SELECT DISTINCT u.user_id
                                            FROM yelp_reduced.users u, yelp_reduced.reviews r
                                            WHERE u.user_id = r.user_id
                                            GROUP BY u.user_id
                                            HAVING COUNT(r.business_id) >= %s )
                    group by u1.user_id, u2.user_id  """

        cursor.execute(query,(n_bus,))

        for row in cursor:
            user = (row['us1'], row['us2'], row['peso'])

            results.append(user)

        cursor.close()
        cnx.close()

        return results

