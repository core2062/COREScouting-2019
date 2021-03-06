#!/usr/bin/python3
# -*- coding: latin-1 -*-
# Allow Display of elements in HTML

""" Creates an 'advanced' team analysis interface. Displays all calculated report statistics in
    addition to all raw data for the team in the database. Supports providing a picture of the
    team's robot in folder '../RobotPictures'. The picture should be the team number in order
    for the display to recognize it. """

import COREDependencies
import CORETeamData
import DataCalculation
# import sys
# reload(sys)
# sys.setdefaultencoding('UTF8')
form = COREDependencies.cgi.FieldStorage()
team_number = int(form.getvalue('team_number'))
raw_team_data = CORETeamData.Team(team_number)
calculated_team_data = DataCalculation.TeamData(team_number)
calculated_team_data.populate_data()

COREDependencies.framework_begining()
print('<body link="##000000">')
print(str(team_number))
print('<img src="http://2062scouting.imgix.net/' + str(team_number) +
      '.jpg?h=200" alt="Team Image Not Available">')
print('<table>')
print('<tr>')
for dictionary_key in COREDependencies.COREConstants.RANK_AND_MATCH_HEADERS:
    print('<td>', dictionary_key, '</td>')
for dictionary_key in COREDependencies.COREConstants.MATCH_HEADERS:
    print('<td>', dictionary_key, '</td>')
for dictionary_key in COREDependencies.COREConstants.RANK_ONLY_HEADERS:
    print('<td>', dictionary_key, '</td>')
print('</tr>')
print('<tr>')
for dictionary_key in COREDependencies.COREConstants.RANK_AND_MATCH_HEADERS:
    if(type(calculated_team_data.team_data[dictionary_key]) == str):
        print('<td>' + str((calculated_team_data.team_data[dictionary_key]).encode("ascii", 'ignore')) + '</td>')
    else: 
        print('<td>' + str(calculated_team_data.team_data[dictionary_key]) + '</td>')
for dictionary_key in COREDependencies.COREConstants.MATCH_HEADERS:
    if(type(calculated_team_data.team_data[dictionary_key]) == str):
        b = str((calculated_team_data.team_data[dictionary_key]).encode("ascii", 'ignore'))
        print('<td>' + b[2:len(b)-2] + '</td>')
    else: 
        print('<td>' + str(calculated_team_data.team_data[dictionary_key]) + '</td>')
for dictionary_key in COREDependencies.COREConstants.RANK_ONLY_HEADERS:
    if(type(calculated_team_data.team_data[dictionary_key]) == str):
        print('<td>' + str((calculated_team_data.team_data[dictionary_key]).encode("ascii", 'ignore')) + '</td>')
    else: 
        print('<td>' + str(calculated_team_data.team_data[dictionary_key]) + '</td>')
print('</tr>')
print('</table>')

print('<table>')
print('<tr>')
for dictionary_key in COREDependencies.COREConstants.ALL_NAMES:
    print('<td>', dictionary_key, '</td>')
print('</tr>')
for rows in range(0, (raw_team_data.num_data_entries(COREDependencies.COREConstants.MATCH_NUMBER['match_number']))):
    print('<tr>')
    for dictionary_key in COREDependencies.COREConstants.ALL_NAMES:
        if(type(raw_team_data._category_dictionary[dictionary_key][rows-1]) == str):
            a = str((raw_team_data._category_dictionary[dictionary_key][rows-1]).encode("ascii", 'ignore'))
            print('<td>', a[2:len(a)-1], '</td>')
        else:
           print('<td>', raw_team_data._category_dictionary[dictionary_key][rows-1], '</td>') 
    print('</tr>')
print('</table>')
COREDependencies.framework_end()
