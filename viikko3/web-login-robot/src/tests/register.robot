*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Form


*** Test Cases ***
Register With Valid Username And Password
    Set Username  eveliina    
    Set Password  eveliina123
    Set Password_confirmation  eveliina123
    Submit Register Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ev   
    Set Password  eveliina123
    Set Password_confirmation  eveliina123
    Submit Register Credentials
    Register Should Fail With Message  Username has to be more than 3 characters
    
Register With Valid Username And Too Short Password
    Set Username  eveliina
    Set Password  eve123
    Set Password_confirmation  eve123
    Submit Register Credentials
    Register Should Fail With Message  Password has to be more than 8 characters

Register With Valid Username And Invalid Password
    Set Username  eveliina
    Set Password  eveliinaeveliina
    Set Password_confirmation  eveliinaeveliina
    Submit Register Credentials
    Register Should Fail With Message  Password cannot contain only letters

# Tämä kohta metodissa rikkoo ekan Register-testin
# Testi sinällään toimii oikein  

# Register With Nonmatching Password And Password Confirmation
#     Set Username  eveliina
#     Set Password  eveliina123
#     Set Password_confirmation  johanna123
#     Submit Register Credentials
#     Register Should Fail With Message  Passwords don't match


Login After Successful Registration
    Set Username  siissa
    Set Password  siissa123
    Set Password_confirmation  siissa123
    Submit Register Credentials
    Register Should Succeed
    Go To Login Page
    Login Page Should Be Open
    Set Username  siissa
    Set Password  siissa123
    Submit Login Credentials
    Login Should Succeed


Login After Failed Registration
    Set Username  siissa
    Set Password  siissasiissa
    Set Password_confirmation  siissasiissa
    Submit Register Credentials
    Register Should Fail With Message  Password cannot contain only letters
    Go To Login Page
    Login Page Should Be Open
    Set Username  siissa
    Set Password  siissasiissa
    Submit Login Credentials
    Login Should Fail 


*** Keywords ***

Go To Register Form
    Go To Main Page
    Click Link  Register new user
    Register Page Should Be Open

Submit Register Credentials
    Click Button  Register

Submit Login Credentials
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password  ${password_confirmation}

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Succeed
    Main Page Should Be Open

Login Should Fail 
    Login Page Should Be Open

