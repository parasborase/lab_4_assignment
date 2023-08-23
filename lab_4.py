class FlightTable:
    def __init__(self):
        self.data = {
            "AI161E90": ("BLR", "BOM", 5600),
            "BR161F91": ("BOM", "BBI", 6750),
            "AI161F99": ("BBI", "BLR", 8210),
            "VS171E20": ("JLR", "BBI", 5500),
            "AS171G30": ("HYD", "JLR", 4400),
            "AI131F49": ("HYD", "BOM", 3499)
        }

    def search_by_city(self, city):
        results = []
        for flight_id, (src, dest, price) in self.data.items():
            if city in (src, dest):
                results.append((flight_id, src, dest, price))
        return results

    def search_by_source(self, source):
        results = []
        for flight_id, (src, dest, price) in self.data.items():
            if src == source:
                results.append((flight_id, src, dest, price))
        return results

    def search_between_cities(self, source, destination):
        results = []
        for flight_id, (src, dest, price) in self.data.items():
            if src == source and dest == destination:
                results.append((flight_id, src, dest, price))
        return results

def main():
    flight_table = FlightTable()

    print("Search Options:")
    print("1. Flights for a particular City")
    print("2. Flights From a city")
    print("3. Flights between two given cities")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        city = input("Enter city name: ")
        results = flight_table.search_by_city(city)
    elif choice == 2:
        source = input("Enter source city: ")
        results = flight_table.search_by_source(source)
    elif choice == 3:
        source = input("Enter source city: ")
        destination = input("Enter destination city: ")
        results = flight_table.search_between_cities(source, destination)
    else:
        print("Invalid choice")
        return

    if not results:
        print("No flights found.")
    else:
        print("Flight ID  |  Source  |  Destination  |  Price")
        print("-" * 45)
        for flight_id, src, dest, price in results:
            print(f"{flight_id}  |  {src}  |  {dest}  |  {price}")

if __name__ == "__main__":
    main()
