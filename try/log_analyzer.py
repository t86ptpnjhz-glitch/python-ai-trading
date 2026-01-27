import logging

logging.basicConfig(level=logging.INFO)

def parse_logs(filename):
	logs = []
	stats = {
		"INFO": 0,
		"WARNING": 0,
		"ERROR": 0
	}

	try:
		with open(filename, "r") as file:
			for line in file:
				line = line.strip()

				if not line:
					continue

				try:
					date, level, message = line.split(" ", 2)

					log_entry = {
						"date": date,
						"level": level,
						"message": message

					}

					logs.append(log_entry)

					if level in stats:
						stats[level] += 1

					else:
						logging.warning(f"Noname level log: {level}")

				except ValueError:
					logging.warning(f"False form string: {line}")

	except FileNotFoundError:
		logging.warning(f"File: {filename} not found")
		return [], {}

	return logs, stats

logs, stats = parse_logs("log.txt")
print("Logs:")
for log in logs:
	print(log)

print("\nStatistic:")
print(f"Total ogs: {len(logs)}")
for level, count in stats.items():
	print(f"{level}: {count}")
# print(logs)
# print(stats)

# for item in stats.items():
#     print(f"\n{item}\n {type(item)}")









