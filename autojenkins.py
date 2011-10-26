import requests

ROOT = 'http://jenkins.pe.local/'

API = '/api/python'
DELETE  = ROOT + 'job/{0}/doDelete'
BUILD   = ROOT + 'job/{0}/build'
CONFIG  = ROOT + 'job/{0}/config.xml'
NEWJOB  = ROOT + 'createItem'
JOBINFO = ROOT + 'job/{0}' + API
LAST_SUCCESS = ROOT + 'job/{0}/lastSuccessfulBuild' + API
TEST_REPORT  = ROOT + 'job/{0}/lastSuccessfulBuild/testReport' + API


def build(jobname):
    return requests.post(BUILD.format(jobname))

def job_info(jobname):
    response = requests.get(JOBINFO.format(jobname))
    return eval(response.content)

def copy(jobname, copy_from='template'):
    params = { 'name': jobname, 'mode': 'copy', 'from': copy_from }
    return requests.post(NEWJOB, params=params)

def get_config_xml(jobname):
    response = requests.get(CONFIG.format(jobname))
    return response.content

def delete(jobname):
    return requests.post(DELETE.format(jobname))

