# cloud-log-monitorerror = 0
warning = 0
info = 0

with open("app.log", "r") as file:
    for line in file:
        if "ERROR" in line:
            error += 1
        elif "WARNING" in line:
            warning += 1
        elif "INFO" in line:
            info += 1

print("☁️ Cloud Log Monitoring Report")
print("------------------------------")
print("ERRORS:", error)
print("WARNINGS:", warning)
print("INFO:", info)
