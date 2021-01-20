import csv
import datetime
import logging


logging.basicConfig(handlers=[logging.FileHandler(filename="errors.log",
                                                  encoding="utf-8")],
                    level=logging.INFO)


def export_from(export_file):
    with open(export_file, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if row["CandidateOrCommittee"] == "COH":
                add_dictionary_to_list(row)


def import_to(new_csv, import_file):
    with open(import_file, mode='w') as csv_file:
        fieldnames = ["ReportFiledDate", "CandidateName", "PeriodBegining", "PeriodEnding", "TransactionID", "TransactionType", "TransactionAmount"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for row_dict in new_csv:
            try:
                writer.writerow(row_dict)
            except Exception:
                logging.info(row_dict)


def add_dictionary_to_list(row):
    try:
        new_dict = {
            "ReportFiledDate": unix_format(row["ReportFiledDate"]),
            "CandidateName": row["CandidateFirstName"] + " " + row["CandidateLastName"],
            "PeriodBegining": iso_format(row["PeriodBegining"]),
            "PeriodEnding": iso_format(row["PeriodEnding"]),
            "TransactionID": row["TransactionID"],
            "TransactionType": row["TransactionType"],
            "TransactionAmount": row["TransactionAmount"]
        }
        new_csv.append(new_dict)
    except Exception:
        logging.info(row)


def unix_format(date):
    date = date[:-3]
    new_date = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")
    return new_date.timestamp()


def iso_format(date):
    new_date = datetime.datetime.strptime(date, "%m/%d/%Y")
    return datetime.datetime.strftime(new_date, "%Y-%m-%d")


if __name__ == "__main__":

    new_csv = []
    export_file = 'transactions.csv'
    import_file = 'result.csv'

    print("Starting export")
    export_from(export_file)
    print("Ending export")
    print("Starting import")
    import_to(new_csv, import_file)
    print("Ending import")
