import subprocess
import unittest

class TestTaskfile(unittest.TestCase):

    def run_task(self, task_name):
        """Helper function to run a Task and return the result."""
        try:
            result = subprocess.run(['task', task_name], check=True, text=True, capture_output=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            self.fail(f"Task '{task_name}' failed with error: {e.output}")

    def test_venv_full(self):
        """Test the venv-full task."""
        output = self.run_task('venv-full')
        self.assertIn("passed", output, "venv-full task did not complete successfully")

    def test_run_webserver(self):
        """Test the run-webserver task."""
        output = self.run_task('run-webserver')
        self.assertIn("Web server started", output, "run-webserver task did not start properly")

    def test_lint(self):
        """Test the lint task."""
        output = self.run_task('lint')
        self.assertIn("completed", output, "Lint task did not complete successfully")
