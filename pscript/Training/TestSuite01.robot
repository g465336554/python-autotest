*** Variables ***
&{dict}           name=zhangsan    sex=nan    age=22

*** Test Cases ***
Testcase001
    [Documentation]    brand型号非空
    [Tags]    login    online    mikezhou
    [Template]    login_asserclass    # \ BBC937DA541E4AF6884c2
    ${name}    set variable    robot framework
    ${姓名}    set variable    张三

jjj

hello

*** Keywords ***
login_assertClass|
    [Arguments]    ${brandEquipment}    ${password}    ${phone}    ${pushclient}    ${vcoede}
