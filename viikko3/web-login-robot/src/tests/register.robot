*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Main Page


*** Test Cases ***

Register With Valid Username And Password
    Click Link  Register new user
    Register Page Should Be Open
    Set Username  eveliina    
    Set Password  eveliina123
    Set Password_confirmation  eveliina123
    Submit Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Click Link  Register new user
    Register Page Should Be Open
    Set Username  ev   
    Set Password  eveliina123
    Set Password_confirmation  eveliina123
    Submit Register
    Register Should Fail With Message  Username has to be more than 3 characters
    
Register With Valid Username And Too Short Password
    Click Link  Register new user
    Register Page Should Be Open
    Set Username  eveliina
    Set Password  eve123
    Set Password_confirmation  eve123
    Submit Register
    Register Should Fail With Message  Password has to be more than 8 characters


*** Keywords ***
Submit Register
    Click Button  Register

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

