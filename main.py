# Main file for the app
from excel_util import get_ips, write_data
from ping import ping_all


def main():
    # Get all ips from details.xlsx
    all_ips = get_ips()
    results = ping_all(all_ips)
    write_data(results)
    return 0


if __name__ == "__main__":
    main()

