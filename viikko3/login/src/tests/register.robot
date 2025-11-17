*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  newuser
    Set Password  ValidPass123
    Set Password Confirmation  ValidPass123
    Click Button  Register
    Registration Should Succeed With Message  Welcome to Ohtu Application!

Register With Too Short Username And Valid Password
# käyttäjätunnus alle 3 merkkiä
    Set Username  us
    Set Password  ValidPass123
    Set Password Confirmation  ValidPass123
    Click Button  Register
    Registration Should Fail With Message  Username should be at least 3 characters long

Register With Valid Username And Too Short Password
# salasana alle 8 merkkiä
    Set Username  newuser
    Set Password  short
    Set Password Confirmation  short
    Click Button  Register
    Registration Should Fail With Message  Password should be at least 8 characters long

Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
    Set Username  newuser
    Set Password  onlyletters
    Set Password Confirmation  onlyletters
    Click Button  Register
    Registration Should Fail With Message  Password should contain at least one non-alphabetic character

Register With Nonmatching Password And Password Confirmation
# salasanan ja salasanan vahvistuksen eroavuus
    Set Username  newuser
    Set Password  ValidPass123
    Set Password Confirmation  DifferentPass123
    Click Button  Register
    Registration Should Fail With Message  Password and password confirmation do not match

Register With Username That Is Already In Use
# käyttäjätunnus on jo olemassa
    Set Username  kalle
    Set Password  ValidPass123
    Set Password Confirmation  ValidPass123
    Click Button  Register
    Set Username  kalle
    Set Password  AnotherPass123
    Set Password Confirmation  AnotherPass123
    Click Button  Register
    Registration Should Fail With Message  Username already exists

*** Keywords ***
set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

set Password
    [Arguments]  ${password}
    Input Text  password  ${password}

set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Text  password_confirmation  ${password_confirmation}

Registration Should Succeed With Message
    [Arguments]  ${message}
    Page Should Contain  ${message}

Registration Should Fail With Message
    [Arguments]  ${message}
    Page Should Contain  ${message}    


*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  password123
    Go To Register Page
