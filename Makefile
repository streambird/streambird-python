local-shell:
	pip install -e . && ipython --InteractiveShellApp.exec_lines="['import streambird']"