from auto_Data import *
from BronKerbosch import bronker_bosch1
from PivotBronKerbosch import bronker_bosch2
from Reporter import *

if __name__ == '__main__':
    funcs = [bronker_bosch1,
             bronker_bosch2]

    for func in funcs:
        report = Reporter(func)
        func([], set(NODES), set(), report)
        report.print_report()
        report.export_report()