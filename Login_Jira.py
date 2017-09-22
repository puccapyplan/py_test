#coding: utf-8
'''
Created on 2017��9��21��

@author: lenovo
'''
from jira import JIRA
import urllib, urllib2
import json
#登录jira
class Login:

    def __init__(self):
        self.username = 'huangdxb'
        self.password = '831292pu'
        self.jira = JIRA("http://", basic_auth=(self.username, self.password))
        self.ISSUE_ID = 'WPT-872'
        
    def print_jira(self):
        issue = self.jira.issue(self.ISSUE_ID)
        print issue.fields.summary + '\n'
        print issue.fields.description + '\n'
        print type(issue.fields.description)
        print str(issue.fields.issuetype) + '\n'
        print type(issue.fields.issuetype)
        print issue.fields.project.name + '\n'
        print issue.fields.creator.displayName + '\n'
    
    def get(self):
        url = 'http://172.29.3.241/rest/api/2/issue/' + self.ISSUE_ID
        textmod = {'os_username':self.username, 'os_password':self.password,'fields':'summary,priority,assignee,updated,description,versions,issuetype'}
        textmod = urllib.urlencode(textmod)
        print(textmod)
        req = urllib2.Request(url='%s%s%s' % (url, '?', textmod))
        res = urllib2.urlopen(req)
        res = res.read()
        print res
        return res
        #print(res_dict[u'fields'])

if __name__ == '__main__':
    login = Login()
    login.get()
