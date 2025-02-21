import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("solmaris.db")
cursor = conn.cursor()

# Fetch all renters
cursor.execute("SELECT * FROM Renters;")
renters = cursor.fetchall()

print("\nRenters data:")
for renter in renters:
    print(renter)

# Fetch all rental agreements
cursor.execute("SELECT * FROM RentalAgreements;")
agreements = cursor.fetchall()

print("\nRental Agreements data:")
for agreement in agreements:
    print(agreement)

# Close the connection
conn.close()
