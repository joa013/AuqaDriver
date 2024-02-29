from mainApp.routes import db

class Devices(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    deviceIP = db.Column(db.String())
    deviceName = db.Column(db.String())
    deviceStatus = db.Column(db.String())

    def __init__(self, deviceIP, deviceName, deviceStatus):
        self.deviceIP = deviceIP
        self.deviceName = deviceName
        self.deviceStatus = deviceStatus


class DevicesFunctions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    deviceId = db.Column(db.Integer())
    actionLink = db.Column(db.String())
    functionParameters = db.Column(db.String())
    functionDescription = db.Column(db.String())
    functionStatus = db.Column(db.String())

    def __init__(self, deviceId, actionLink, functionParameters, functionDescription, functionStatus):
        self.deviceId = deviceId
        self.actionLink = actionLink
        self.functionParameters = functionParameters
        self.functionDescription = functionDescription
        self.functionStatus = functionStatus


class FunctionScheduler(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    functionId = db.Column(db.String())
    trigger = db.Column(db.String())
    schedulerID = db.Column(db.String())
    year = db.Column(db.Integer()) #4-digit year
    month = db.Column(db.Integer()) #(1-12)
    day = db.Column(db.Integer()) #(1-31)
    day_of_week = db.Column(db.String()) #mon,tue,wed,thu,fri,sat,sun
    hour = db.Column(db.Integer()) #(0-23)
    minute = db.Column(db.Integer()) #(0-59)
    second = db.Column(db.Integer()) #(0-59)
    schedulerStatus = db.Column(db.String())

    def __init__(self, functionId , trigger, schedulerID, year , month , day , day_of_week , hour , minute, second, schedulerStatus):
        self.functionId = functionId
        self.trigger = trigger
        self.schedulerID = schedulerID
        self.year = year
        self.month = month
        self.day = day
        self.day_of_week = day_of_week
        self.hour = hour
        self.minute = minute
        self.second = second
        self.schedulerStatus = schedulerStatus


class Archive(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.Integer())
    deviceIP = db.Column(db.String())
    deviceName = db.Column(db.String())
    addInfo = db.Column(db.String())
    value = db.Column(db.Integer())
    type = db.Column(db.String())

    def __init__(self, timestamp, deviceIP, deviceName, addInfo, value, type):
        self.timestamp = timestamp
        self.deviceIP = deviceIP
        self.deviceName = deviceName
        self.addInfo = addInfo
        self.value = value
        self.type = type     

class ArchiveReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    description = db.Column(db.String())
    deviceIP = db.Column(db.String())
    deviceName = db.Column(db.String())
    addInfo = db.Column(db.String())
    type = db.Column(db.String())
    avgOrSum = db.Column(db.String())
    timerRangeHours = db.Column(db.Integer())
    quantityValues = db.Column(db.Integer())
    minValue = db.Column(db.Integer())
    okMinValue = db.Column(db.Integer())
    okMaxValue = db.Column(db.Integer())
    maxValue = db.Column(db.Integer())

    def __init__(self, deviceIP, title, description, deviceName, addInfo, type, avgOrSum, timerRangeHours, quantityValues, minValue, okMinValue, okMaxValue, maxValue):
        self.deviceIP = deviceIP
        self.title = title
        self.description = description
        self.deviceName = deviceName
        self.addInfo = addInfo
        self.type = type
        self.avgOrSum = avgOrSum
        self.timerRangeHours = timerRangeHours
        self.quantityValues = quantityValues
        self.minValue = minValue
        self.okMinValue = okMinValue
        self.okMaxValue = okMaxValue
        self.maxValue = maxValue

class ArchiveFunctions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    description = db.Column(db.String())
    archiveReportIds = db.Column(db.String())
    functionStatus = db.Column(db.String())

    def __init__(self, title, description, archiveReportIds, functionStatus):
        self.title = title
        self.description = description
        self.archiveReportIds = archiveReportIds
        self.functionStatus = functionStatus