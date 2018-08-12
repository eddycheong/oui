import collections
import csv

def parser(ouiFile, encoding = "utf-8"):
    data = collections.OrderedDict()

    with open(ouiFile, encoding=encoding) as ouis:
        reader = csv.DictReader(ouis)
        for oui in reader:
            data[oui["Assignment"]] = {
                "name": oui["Organization Name"],
                "address": oui["Organization Address"]
            }
    
    return dict(data.items())