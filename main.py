import csv
import time
import datetime


def unix_format(date):
    date = date[:-3]
    return time.mktime(datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f").timetuple())

def iso_format(date):
    print(date)
    new_date = datetime.datetime.strptime(date, "%m/%d/%Y")
    return datetime.datetime.strftime(new_date, "%Y-%m-%d")


if __name__ == "__main__":

    new_csv = []

    with open('transactions.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 1
        for row in csv_reader:
            line_count += 1
            if row["CandidateOrCommittee"]:
                print(line_count)
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


    with open('result.csv', mode='w') as csv_file:
        fieldnames = ["ReportFiledDate", "CandidateName", "PeriodBegining", "PeriodEnding", "TransactionID", "TransactionType", "TransactionAmount"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for row_dict in new_csv:
            writer.writerow(row_dict)
