#coding: utf-8
'''
Created on 2017��9��22��

@author: lenovo
'''
import Login_Jira
import json  
  

def format_json():
    jsonstr=Login_Jira.Login().get()
    length = len(jsonstr)  
    print "=================================="  
    if length > 1:  
        try:  
            jsonObj = json.loads(jsonstr)  
            formatJsonStr = json.dumps(jsonObj,indent=4,ensure_ascii=False,sort_keys=True)  
            print formatJsonStr
            print type(formatJsonStr)
            print type(jsonObj)
        except Exception, e:  
            print e  
            print "json parse error."  
        else :  
            print "argv's length is 1, no json text input."  
        return formatJsonStr
        
if __name__=='__main__':        
    format_json()