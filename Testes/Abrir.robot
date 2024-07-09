*** Settings ***
Library    SeleniumLibrary
Library    String
Library    Dialogs

*** Variables ***
${BROWSER}           Chrome
${ENVIRONMENT}       staging

${PROFILE_PATH}      C:/Users/pedroca/AppData/Local/Google/Chrome/User Data/Default
${CHROME_OPT}        add_argument("--user-data-dir=${PROFILE_PATH}")
${CHROME_OPT}        add_argument("--start-maximized")

*** Test Cases ***
Abrir o site do Hero Wars
    Open Browser    https://www.hero-wars.com    browser=${BROWSER}    options=${CHROME_OPT}

#<canvas width="1349" height="640" style="transform: translateZ(0px); width: 1349px; height: 640px; text-align: center;"></canvas>