from time import sleep
import os, time, json
os.system("cls")
volba = str(input("Null json data y/n: "))
volba = volba.strip().lower()
if volba == "y":
            with open("stats.json","r") as file:
                data = json.load(file)  

            for x in data:
                if data[x] == data["total_records"]:
                    continue
                data[x]["stats"]["count"] = 0
                data[x]["stats"]["next_higher"] = 0
                data[x]["stats"]["next_lower"] = 0
                data[x]["stats"]["equal"] = 0

            data["total_records"] = 0

                
            with open("stats.json","w") as file:
                json.dump(data, file, indent=4)
            print("json cleared")

sleep(1)
os.system("cls")
   
       
       
       


