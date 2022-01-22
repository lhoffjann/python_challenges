"""Question: A website requires the users to input username and password to register. Write a program to check the validity of password input by users. Following are the criteria for checking the password:

        At least 1 letter between [a-z]
        At least 1 number between [0-9]
        At least 1 letter between [A-Z]
        At least 1 character from [$#@]
        Minimum length of transaction password: 6
        Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma. Example If the following passwords are given as input to the program: ABd1234@1,a F1#,2w3E*,2We3345 Then, the output of the program should be: ABd1234@1
"""

passwd = [x for x in input().split()]
result = []
for x in passwd:
    if len(x) >= 6 and len(x) <= 12:
        upperC=0
        lowerC=0
        symC=0
        for i in range(len(x)):
            if x[i].isupper():
                upperC += 1
            elif x[i].islower():
                lowerC += 1
            elif x[i] == '$' or x[i]=='#' or x[i]=='@':
                symC += 1
        if upperC >= 1 and lowerC >= 1 and symC >= 1:
            result.append(x)
print(','.join(result))
