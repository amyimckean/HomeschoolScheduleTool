from HomeschoolTool.models import scheduledItem
from datetime import datetime


def getEventSource(events):
    eventArr = []
    for e in events:
        event = {'title': e.description, 'description': e.details}
        start_date = e.start.strftime("%Y-%m-%d %H:%M:%S")
        event['start'] = start_date
        if e.end:
            end_date = e.end.strftime("%Y-%m-%d %H:%M:%S")
            event['end'] = end_date
        event['allDay'] = e.allDay
        if e.recurType:
            recurStart = e.start.date().strftime("%Y%m%dT%H%M%S")
            recurEnd = e.recurEnd.date().strftime("%Y%m%d")
            event['rrule'] = 'DTSTART:' + recurStart + 'Z\nRRULE:FREQ=' + e.recurType.recurrenceTypeName \
                             + ';UNTIL=' + recurEnd
        eventArr.append(event)
    return eventArr
