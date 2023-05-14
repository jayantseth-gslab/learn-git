# Main file for the app
from excel_util import get_ips, write_data
from ping import ping_all
from datetime import datetime as dt


def main():
    # Get all ips from details.xlsx
    start_time = dt.now()
    all_ips = get_ips()
    results = ping_all(all_ips)
    write_data(results)
    end_time = dt.now()
    print(f"Total execution time: {end_time - start_time}")
    return 0


if __name__ == "__main__":
    main()

