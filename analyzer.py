success = 0
failed = 0
new_users = 0
deleted_users = 0
admin_events = 0
log_cleared = False

failed_users = {}

with open("security_log.csv", "r") as file:

    next(file)  # Skip header

    for line in file:

        data = line.strip().split(",")

        event_id = data[1]
        user = data[2]

        # Successful Logon
        if event_id == "4624":
            success += 1

        # Failed Logon
        elif event_id == "4625":
            failed += 1

            failed_users[user] = failed_users.get(user, 0) + 1

        # Special Privileges Assigned
        elif event_id == "4672":
            admin_events += 1

        # User Created
        elif event_id == "4720":
            new_users += 1

        # User Deleted
        elif event_id == "4726":
            deleted_users += 1

        # Security Log Cleared
        elif event_id == "1102":
            log_cleared = True


print("\n======================================")
print("     WINDOWS SECURITY REPORT")
print("======================================")

print(f"Successful Logons : {success}")
print(f"Failed Logons     : {failed}")
print(f"New Users         : {new_users}")
print(f"Deleted Users     : {deleted_users}")
print(f"Admin Events      : {admin_events}")

if log_cleared:
    print("Security Log Cleared : YES")
else:
    print("Security Log Cleared : NO")

print("\nFailed Login Users")
print("------------------")

for user, count in failed_users.items():
    print(f"{user} -> {count}")