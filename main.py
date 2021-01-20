import csv

if __name__ == "__main__":

    new_csv = []

    with open('transactions.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                pass
                line_count += 1
            elif line_count == 1 or line_count == 2:
                if row["CandidateOrCommittee"]:
                    new_dict = {
                        "ReportFiledDate": row["ReportFiledDate"],
                        "CandidateName": row["CandidateFirstName"] + " " + row["CandidateLastName"],
                        "PeriodBegining": row["PeriodBegining"],
                        "PeriodEnding": row["PeriodEnding"],
                        "TransactionID": row["TransactionID"],
                        "TransactionType": row["TransactionType"],
                        "TransactionAmount": row["TransactionAmount"]
                    }
                    print(new_dict)
                    new_csv.append(new_dict)
                    line_count += 1


    with open('result.csv', mode='w') as csv_file:
        fieldnames = ["ReportFiledDate", "CandidateName", "PeriodBegining", "PeriodEnding", "TransactionID", "TransactionType", "TransactionAmount"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for row_dict in new_csv:
            writer.writerow(row_dict)
