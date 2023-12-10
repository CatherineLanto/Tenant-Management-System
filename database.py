import sqlite3

#CREATES TABLE FOR TENANTS
def create_table_tenants():
  connect = sqlite3.connect('database.db')
  cursor = connect.cursor()     # used to interact with a database         
  
  cursor.execute('''
                 CREATE TABLE IF NOT EXISTS tenants (
                   id TEXT PRIMARY KEY,
                   name TEXT,
                   contact TEXT,
                   gender TEXT,
                   status TEXT)''')
  connect.commit()
  connect.close()
  
def view_tenants():
  connect = sqlite3.connect('database.db')
  cursor = connect.cursor()
  cursor.execute('SELECT * FROM tenants')
  tenants = cursor.fetchall()
  connect.close()
  return tenants
  
def add_tenant(id, name, contact, gender, status):
  connect = sqlite3.connect('database.db')
  cursor = connect.cursor()
  cursor.execute('INSERT INTO tenants(id, name, contact, gender, status) VALUES(?, ?, ?, ?, ?)',
                 (id, name, contact, gender, status))
  connect.commit()
  connect.close()
    
def remove_tenant(id):
  connect = sqlite3.connect('database.db')
  cursor = connect.cursor()
  cursor.execute('DELETE FROM tenants WHERE id = ?', (id,))
  connect.commit()
  connect.close()
      
def update_tenant(new_name, new_contact, new_gender, new_status, new_id):
  connect = sqlite3.connect('database.db')
  cursor = connect.cursor()
  cursor.execute('UPDATE tenants SET name = ?, contact = ?, gender = ?, status = ? WHERE id = ?',
                 (new_name, new_contact, new_gender, new_status, new_id))
  connect.commit()
  connect.close()
      
def tenant_exists(id):
  connect = sqlite3.connect('database.db')
  cursor = connect.cursor()
  cursor.execute('SELECT COUNT(*) FROM tenants WHERE id = ?', (id,))
  result = cursor.fetchone()
  connect.close()
  return result[0] > 0
    
create_table_tenants()



#CREATES TABLE FOR ROOMS
def create_table_rooms():
  connect = sqlite3.connect("database.db")
  cursor = connect.cursor()
  
  cursor.execute('''
                 CREATE TABLE IF NOT EXISTS rooms (
                   room_id TEXT PRIMARY KEY,
                   additional_fees TEXT,
                   monthly_rent TEXT,
                   slots_taken TEXT,
                   total_slots TEXT)''')
  connect.commit()
  connect.close()
  
def view_rooms():
  connect = sqlite3.connect('database.db')
  cursor = connect.cursor()
  cursor.execute('SELECT * FROM rooms')
  rooms = cursor.fetchall()
  connect.close()
  return rooms

def add_room(room_id, additional_fees, monthly_rent, slots_taken, total_slots):
  connect = sqlite3.connect('database.db')
  cursor = connect.cursor()
    
  try:
    monthly_rent = int(monthly_rent)
  except ValueError:
    monthly_rent = 0
  
  cursor.execute('INSERT INTO rooms(room_id, additional_fees, monthly_rent, slots_taken, total_slots) VALUES(?, ?, ?, ?, ?)',
                 (room_id, additional_fees, monthly_rent, slots_taken, total_slots ))
  connect.commit()
  connect.close()
  
def remove_room(room_id):
  connect = sqlite3.connect('database.db')
  cursor = connect.cursor()
  cursor.execute('DELETE FROM rooms WHERE room_id = ?', (room_id,))
  connect.commit()
  connect.close()
  
def update_room(new_fees, new_rent, new_slots_taken, new_total_slots, new_room_id):
  connect = sqlite3.connect('database.db')
  cursor = connect.cursor()
  cursor.execute('UPDATE rooms SET additional_fees = ?, monthly_rent = ?, slots_taken = ?, total_slots = ? WHERE room_id = ?',
                 (new_fees, new_rent, new_slots_taken, new_total_slots, new_room_id))
  connect.commit()
  connect.close()

def room_exists(room_id):
  connect = sqlite3.connect('database.db')
  cursor = connect.cursor()
  cursor.execute('SELECT COUNT(*) FROM rooms WHERE room_id = ?', (room_id,))
  result = cursor.fetchone()
  connect.close()
  return result[0] > 0
    
create_table_rooms()
    
    
    
#CREATES TABLE FOR PAYMENTS
def create_table_payments():
  connect = sqlite3.connect('database.db')
  cursor = connect.cursor()     # used to interact with a database    
  
  cursor.execute('''
                 CREATE TABLE IF NOT EXISTS payments (
                   tenant_id TEXT PRIMARY KEY, 
                   tenant_room_id TEXT, 
                   payment_status TEXT,
                   last_payment TEXT,
                   payment_due TEXT,
                   
                   FOREIGN KEY (tenant_id) REFERENCES tenants(id),
                   FOREIGN KEY (tenant_room_id) REFERENCES rooms(room_id)
                   )''')
  connect.commit()
  connect.close()

  
def view_payments():
  connect = sqlite3.connect('database.db')
  cursor = connect.cursor()
  cursor.execute('SELECT * FROM payments')
  result = cursor.fetchall()
  connect.close()
  return result


def add_payment(tenant_id, tenant_room_id, payment_status, last_payment, payment_due):
  connect = sqlite3.connect('database.db')
  cursor = connect.cursor()
  cursor.execute('INSERT INTO payments(tenant_id, tenant_room_id, payment_status, last_payment, payment_due) VALUES(?, ?, ?, ?, ?)',
                 (tenant_id, tenant_room_id, payment_status, last_payment, payment_due))
  connect.commit()
  connect.close()
  
def remove_payment(tenant_id):
  connect = sqlite3.connect('database.db')
  cursor = connect.cursor()
  cursor.execute('DELETE FROM payments WHERE tenant_id = ?', (tenant_id,))
  connect.commit()
  connect.close()
  
def update_payment(new_tenant_room_id, new_payment_status, new_last_payment, new_payment_due, new_tenant_id):
  connect = sqlite3.connect('database.db')
  cursor = connect.cursor()
  cursor.execute('UPDATE payments SET tenant_room_id = ?, payment_status = ?, last_payment = ?, payment_due = ? WHERE tenant_id = ?',
                 (new_tenant_room_id, new_payment_status, new_last_payment, new_payment_due, new_tenant_id))
  connect.commit()
  connect.close()

def payment_exists(tenant_id):
  connect = sqlite3.connect('database.db')
  cursor = connect.cursor()
  cursor.execute('SELECT COUNT(*) FROM payments WHERE tenant_id = ?', (tenant_id,))
  result = cursor.fetchone()
  connect.close()
  return result[0] > 0

def get_tenant_ids():
    try:
        connect = sqlite3.connect('database.db')
        cursor = connect.cursor()
        cursor.execute('SELECT id FROM tenants')
        tenant_ids = [row[0] for row in cursor.fetchall()]
        return tenant_ids
    except sqlite3.Error as e:
        print(f"Error: {e}")
    finally:
        if connect:
            connect.close()

def get_room_ids():
    try:
        connect = sqlite3.connect('database.db')
        cursor = connect.cursor()
        cursor.execute('SELECT room_id FROM rooms')
        room_ids = [row[0] for row in cursor.fetchall()]
        return room_ids
    except sqlite3.Error as e:
            print(f"Error: {e}")
    finally:
        if connect:
            connect.close()
            
def get_tenant_ids_and_names(self):
        try:
            connect = sqlite3.connect('database.db')
            cursor = connect.cursor()
            cursor.execute('SELECT id, name FROM tenants')
            tenant_data = [{"id": row[0], "name": row[1]} for row in cursor.fetchall()]
            return tenant_data
        except sqlite3.Error as e:
            print(f"Error: {e}")
        finally:
            if connect:
                connect.close()

create_table_payments()