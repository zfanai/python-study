
::python cleanpyc.py C:\Users\zhoufan\Projects\Python\TrumCloud\app
::python cleanpyc.py C:\Users\zhoufan\Projects\Python\Flask\FlaskBase\flask
::python cleanpyc.py C:\Users\zhoufan\Projects\Python\TrumCloudMaster
::python cleanpyc.py C:\Users\zhoufan\Projects\Python\TestVenv
::python cleanpyc.py C:\Users\zhoufan\Projects\Python\VirtualEnv\Flask
::python cleanpyc.py C:\Python27\Lib
::python cleanpyc.py C:\Users\zhoufan\Desktop\Temp\dwead\Python27
::python cleanpyc.py C:\Users\zhoufan\Desktop\dlksdf\TrumCloud_cfq_dev
::python cleanpyc.py C:\Users\zhoufan\Desktop\cfq_merge_20150428
::python cleanpyc.py C:\Users\zhoufan\Desktop\temp_comp
::pause
@echo off
echo %1 
echo %2
set PYTHON_SRCIPT=C:\Users\zhoufan\Projects\Python\CommonTools\source\cleanpyc\cleanpyc.py 
if %1==tcld (
    set TARGET_DIR=C:\Users\zhoufan\Projects\Python\TrumCloud\app
) else if %1==prod (
    set TARGET_DIR=C:\Users\zhoufan\Projects\TrumCloud\PROD\%2
) else if %1==cfq (
    set TARGET_DIR=C:\Users\zhoufan\Projects\TrumCloud\CFQBranch\%2
)

echo %TARGET_DIR%

if exist %TARGET_DIR% (
    call python %PYTHON_SRCIPT% %TARGET_DIR%
)