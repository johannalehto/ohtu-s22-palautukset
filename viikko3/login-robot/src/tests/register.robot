*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User



*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  johanna  johanna123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  johanna123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  jo  johanna123
    Output Should Contain  Username has to be longer than 3 characters

Register With Valid Username And Too Short Password
    Input Credentials  johanna  j2
    Output Should Contain  Password has to be longer than 3 characters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  johanna  johannajohanna
    Output Should Contain  Password cannot contain only letters


*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command