from .debug import debug_message

import typing
from subprocess import run
from pathlib import Path
from threading import Thread

def run_command_line(cmd_line_list : typing.List[str], working_directory : Path) -> bool :
	cmd_line_join = " ".join(cmd_line_list)
	debug_message(f"Running command \"{cmd_line_join}\" ...")

	successful = False
	try:
		rc = run(cmd_line_list, cwd=working_directory)

		if rc.returncode != 0 :
			debug_message(f"... command \"{cmd_line_join}\" ran with error!")
		else :
			debug_message(f"... command \"{cmd_line_join}\" successfully ran!")
			successful = True

	except Exception as e:
		debug_message(f"... command \"{cmd_line_join}\" call FAILED with exception: {e}")

	return successful
	
def run_command(cmd_path : Path, working_path : Path) -> bool :
	return run_command_line([str(cmd_path)], working_path)

class batch_pool :

	def __init__(self) :
		self.thread_list = []

	def run_command(self, source_path : Path, working_path : Path) -> None :		
		assert source_path is not None and source_path != ""

		new_thread = Thread(target=run_command, args=[source_path, working_path])
		self.thread_list.append(new_thread)
		new_thread.start()

	def finish(self) :
		while len(self.thread_list) > 0 :
			finished_thread = None
			for running_thread in self.thread_list :
				if not running_thread.is_alive() :
					finished_thread = running_thread
					break
			if finished_thread is not None :
				finished_thread.join()
				self.thread_list.remove(finished_thread)
