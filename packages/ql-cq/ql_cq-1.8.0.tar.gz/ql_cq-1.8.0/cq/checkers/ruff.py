import cq.checker
import cq.utils


class RuffChecker(cq.checker.Checker):

	NAME = 'ruff'
	DESCRIPTION = 'Run ruff linter on given modules.'
	HELP_LINE = 'use `# noqa: <rule-id>` for disabling ruff on particular line'

	def run(self, modules: list[str]) -> cq.checker.CheckerResult:
		options = [
			'check',
		]
		stdout, return_code = cq.utils.run_external_checker('ruff', options + modules)

		output: list[cq.checker.ResultLine] = []

		for output_line in stdout.split('\n'):
			if not output_line:
				continue

			# Ruff has a nice enough output, no need to split into file/line (there is also char pos)
			output.append(cq.checker.ResultLine(file = None, line = None, message = output_line, is_error = True))

		return cq.checker.CheckerResult(
			checker_name = self.NAME,
			help_line = self.HELP_LINE,
			return_code = return_code,
			output = output,
		)
