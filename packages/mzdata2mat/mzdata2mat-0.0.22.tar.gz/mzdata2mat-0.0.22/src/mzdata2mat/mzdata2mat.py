import execjs
import json
from pydantic import BaseModel
from mat4py import savemat
import os
import shutil

class mzDataXMLStruct(BaseModel):
    metadata : dict
    times : list[float]
    series : dict

class mzData(BaseModel):
    fileName : str = None
    filePath : str = None
    mz : list[list[float]] = [[]]
    intensities : list[list[float]] = [[]]
    time : list[float] = []

    def toDict(self):
        tempDict = self.model_dump()
        return {self.fileName.lower().split(".mzdata")[0] : tempDict}

class mzDataError(Exception):
    """Class used by mzDataXML package to throw errors"""

    def __init__(self, errorMsg : str, errorCode : int):
        self.errorMsg = errorMsg
        self.errorCode = errorCode
        super().__init__(f"An error occured : Error {self.errorCode} - {self.errorMsg}")

class mzDataManager(BaseModel):
    path2mzDataXMLFiles : str = None
    path2exportedMatFiles : str = None
    jsFunc : str = None

    def __init__(self, useDirectory : bool, mzDataPath : str = None, exportPath : str = None):
        """Main class for converting .mzData.xml files into .mat files for realeases of Matlab r2019b and newer.
        -> `mzDataPath` : Path to the folder containing the .mzdata.xml files \n
        -> `exportPath` : Path to save the converted .mat files \n
        -> `useDirectory` : Set this parameter to `False` to not use directories and specify them when using the functions.
        
        """
        if useDirectory:
            if os.path.isdir(mzDataPath) and os.path.exists(mzDataPath):
                self.path2mzDataXMLFiles = mzDataPath
            else:
                raise mzDataError("The directory entered for .mzdata.xml files is not valid", 3)
            if os.path.isdir(exportPath) and os.path.exists(exportPath):
                self.path2exportedMatFiles = exportPath
            else:
                raise mzDataError("The directory entered for converted .mat files is not valid")
        super().__init__()
        file = open(os.path.join(__file__.rsplit("mzdata", 1)[0], "script.js")).read()
        self.jsFunc = execjs.compile(file)

    def mzDataXMLread(self, fileName : str, customDirectory : bool = False):
        """
        Reads mzML files and returns the given object.\n
        -> `fileName` :\n
            -> Should be the full path to the file and it's extension (.mzdata.xml) to convert if no value was given to `mzDataPath` when initializing the class.\n
            -> Otherwise, the file's relative path with it's extension (.mzdata.xml)\n
        -> `customDirectory` : Set this parameter to `True` if the `fileName` is in a different path than the one given in configuration.
        """
        try:
            if self.path2mzDataXMLFiles == None or customDirectory:
                    result = self.jsFunc.call("mzMLread", fileName, __file__.rsplit("mzdata", 1)[0])
            else:
                result = self.jsFunc.call("mzMLread", os.path.join(self.path2mzDataXMLFiles, fileName), __file__.rsplit("mzdata", 1)[0])
        except execjs.RuntimeError as e:
            raise mzDataError("Runtime Error, did you forgot to install node.js ?", 6)
        x = json.loads(json.dumps(result))
        dataStruct = mzDataXMLStruct(metadata=x["metadata"], times=x["times"], series=x["series"])
        returnStruct = mzData()
        totalMasseDataSet = []
        totalIntensityDataSet = []
        for i in dataStruct.series["ms"]["data"]:
            massesDataSet = []
            intensityDataSet = []
            for y in range(len(i[0])):
                massesDataSet.append(i[0][str(y)])
            for z in range(len(i[1])):
                intensityDataSet.append(i[1][str(z)])
            totalMasseDataSet.append(massesDataSet)
            totalIntensityDataSet.append(intensityDataSet)
        returnStruct.mz = totalMasseDataSet
        returnStruct.intensities = totalIntensityDataSet
        returnStruct.time = dataStruct.times
        if customDirectory or self.path2mzDataXMLFiles == None:
            file = fileName
        else:
            file = self.path2mzDataXMLFiles
        returnStruct.filePath = file
        returnStruct.fileName = file.rsplit("/", 1)[1]
        return returnStruct
    
    def saveMatfile(self, mzData : mzData, remove : bool = False, dir2Save : str = None, force : bool = False):
        """
        Saves a `mzData` structure to a .mat file.\n
        -> `mzData`     : The structure got from `mzMLread` function.\n
        -> `remove`     : Should the original file be removed when it is saved as .mat file ?\n
        -> `dir2Save`   : Save directory to save the .mat file. If path was given in configuration, it is not needed. This parameter will be prioritised over the path given in configuration (if any).\n
        -> `force`      : If a file has the same name in the converted folder, should it be replaced ? (File will not be saved if sibling found in convert folder and this parameter set to `False`.)
        """
        
        if self.path2exportedMatFiles == None or dir2Save != None:
            if os.path.exists(dir2Save):
                saveDir = os.path.join(dir2Save, f"{mzData.fileName.lower().split(".mzdata")[0]}.mat")
            else:
                raise mzDataError("No save directory specified", 4)
        else:
            saveDir = os.path.join(self.path2exportedMatFiles, f"{mzData.fileName.split(".mzdata")[0]}.mat")
        
        if os.path.exists(saveDir):
            if force:
                os.remove(saveDir)
                savemat(saveDir, mzData.toDict())
            else:
                print(f"File {mzData.fileName} skipped because same file exists in export folder and parameter `force` is not set to `True`")
        else:
            savemat(saveDir, mzData.toDict())
        if remove:
            os.remove(os.path.join(mzData.filePath, mzData.fileName))
        return

def verify():
    try:
        path = os.getcwd()
        testFile = os.path.join(__file__.rsplit("mzdata", 1)[0], "tiny1.mzData.xml")
        testClass = mzDataManager(useDirectory=False)
        shutil.copyfile(testFile, os.path.join(path, "tiny1.mzData.xml"))
        value = testClass.mzDataXMLread(os.path.join(path, "tiny1.mzData.xml"))
        testClass.saveMatfile(value, dir2Save=path)
        print("mzdata2mat - Ready to use !")
    except Exception as e:
        raise e