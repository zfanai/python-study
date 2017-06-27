@echo off
if %1==venv (
    flaskpython iconv.py C:\Users\zhoufan\Projects\Python\CodeRepository\CodeRepository\GadgetTest
) else if %1==prod (
	python iconv.py C:\Users\zhoufan\Projects\Python\CodeRepository\CodeRepository\GadgetTest
)



