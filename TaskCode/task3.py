__author__ = 'YangJun'

with open('2.txt', 'w') as infile, open('1.txt', 'r') as outfile:
    # data = outfile.read().splitlines()
    data = outfile.readlines()
    for one in data:
        one = str(one)
        mid = one.split(';')
        namePart = mid[0].split(':')[1].strip()
        wagePart = mid[1].split(':')[1].strip()
        tax = int(int(wagePart) * 0.9)
        income = int(wagePart) - tax
        outPutStr = 'name: {:10}   ;    salary:  {:6} ;  tax: {:6} ; income:  {:6}'.format(namePart, wagePart, tax,
                                                                                           income)
        infile.write(outPutStr + '\n')

#
# with open(inFileName) as ifile, open(outFileName, 'w') as ofile:
#     beforeTax = ifile.read().splitlines()
#     # or we could use   beforeTax = ifile.read().split('\n')
#     for one in beforeTax:
#         if one.count(';') != 1:  # ensure valid
#             continue
#
#         namePart, salaryPart = one.split(';')
#         # name Part like  name: Jack  |  salaryPart like    salary:  12000]
#
#         if namePart.count(':') != 1:  # ensure valid
#             continue
#         if salaryPart.count(':') != 1:  # ensure valid
#             continue
#
#         name = namePart.split(':')[1].strip()
#         print name
#         salary = int(salaryPart.split(':')[1].strip())
#         print salary
#
#         income = int(salary * 0.9)
#         tax = int(salary * 0.1)
#
#         outPutStr = 'name: {:10}   ;    salary:  {:6} ;  tax: {:6} ; income:  {:6}'.format(name, salary, tax, income)
#
#         print outPutStr
#
#         ofile.write(outPutStr + '\n')



