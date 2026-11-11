from mysql import connector
from datetime import datetime


class bloodDonorManager:

    def __init__(self):
        self.connection = connector.connect(
            host='localhost',
            user='root',
            password='akshaynr_@2005',
            db='blood_db_26'
        )

        if self.connection:
            print("Successfully connected")

        self.cursor = self.connection.cursor()

    # INSERT
    def post(self, **kwargs):
        try:
            self.cursor = self.connection.cursor()

            query = """INSERT INTO donor
            (name, blood_group, phone, city, last_donation)
            VALUES (%s, %s, %s, %s, %s)"""

            values = (
                kwargs['name'],
                kwargs['blood_group'],
                kwargs['phone'],
                kwargs['city'],
                kwargs['last_donation']
            )

            self.cursor.execute(query, values)
            self.connection.commit()

            print("Data inserted successfully!")

        except Exception as e:
            print(e)

    # GET OBJECT
    def get_object(self, id=None):
        try:
            self.cursor = self.connection.cursor()

            query = "SELECT * FROM donor WHERE id=%s"
            values = (id,)

            self.cursor.execute(query, values)
            record = self.cursor.fetchone()

            return record

        except Exception as e:
            print(e)

    # DISPLAY ALL RECORDS
    def get(self):
        try:
            self.cursor = self.connection.cursor()

            query = "SELECT * FROM donor"

            self.cursor.execute(query)
            records = self.cursor.fetchall()

            return records

        except Exception as e:
            print(e)

    # RETRIEVE SINGLE RECORD
    def retreive(self, id=None):
        try:
            record = self.get_object(id=id)

            if record is not None:
                print(record)
            else:
                print("No donors found!")

        except Exception as e:
            print(e)

    # DELETE
    def delete(self, id=None):
        try:
            record = self.get_object(id=id)

            if record is not None:

                self.cursor = self.connection.cursor()

                query = "DELETE FROM donor WHERE id=%s"

                self.cursor.execute(query, (id,))
                self.connection.commit()

                print("Donor deleted successfully!")

            else:
                print("No donors found!")

        except Exception as e:
            print(e)

    # UPDATE
    def put(self, id=None, **kwargs):
        try:
            record = self.get_object(id=id)

            if record is not None:

                self.cursor = self.connection.cursor()

                allowed_columns = {
                    'name', 'blood_group', 'phone',
                    'city', 'last_donation'
                }

                if not kwargs:
                    print("No values provided for update!")
                    return

                if not set(kwargs).issubset(allowed_columns):
                    print("Invalid column name!")
                    return

                placeholder = ""

                for k in kwargs.keys():
                    placeholder += f"{k}=%s,"

                placeholder = placeholder.rstrip(",")

                query = f"UPDATE donor SET {placeholder} WHERE id=%s"

                values = list(kwargs.values())
                values.append(id)

                self.cursor.execute(query, values)
                self.connection.commit()

                print("Donor updated successfully!")
                return True,"Donor updated successfully"
            else:
                return False,"No donors found..."

        except Exception as e:
            print(e)


# OBJECT CREATION

donor_instance = bloodDonorManager()
# INSERT
#donor_instance.post(
 #    name="akshay",
  #   blood_group="o+",
   #  phone=9187654321,
    # city="kochi",
    #last_donation=datetime.today()
 #)

# DISPLAY ALL
#donor_instance.get()

# RETRIEVE
donor_instance.retreive(id=0)

# DELETE
# donor_instance.delete(id=2)

# UPDATE
# donor_instance.put(id=1, city="Kochi", blood_group="A+")


# CLOSE CONNECTION
donor_instance.cursor.close()
donor_instance.connection.close()
