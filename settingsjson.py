import json

settings_json = json.dumps([
    {'type': 'title',
     'title': 'Survey Settings'},
    {'type': 'bool',
     'title': 'Enable Survey',
     'desc': 'Enable or Disable User Surveys',
     'section': 'example',
     'key': 'enablesurvey'},
    {'type': 'string',
     'title': 'Survey Name',
     'desc': 'Enter a name for your survey',
     'section': 'example',
     'key': 'surveyname'},
    {'type': 'title',
     'title': ' Settings'},
    {'type': 'numeric',
     'title': 'Slide Length',
     'desc': 'Enter a length in seconds for your presentation slides',
     'section': 'example',
     'key': 'slidetime'}])
